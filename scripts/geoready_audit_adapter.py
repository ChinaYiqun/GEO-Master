#!/usr/bin/env python3
"""Run GeoReady and preserve an evidence-first GEO-Master audit bundle.

The adapter keeps the upstream JSON untouched, normalizes category-level
checks into audit findings, creates a remediation checklist, and can rerun a
previous bundle after optimization to produce a deterministic delta.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ADAPTER_VERSION = "0.1.0"
UPSTREAM_REPOSITORY = "Auriti-Labs/geo-optimizer-skill"
CHECK_ORDER = (
    "robots_txt",
    "llms_txt",
    "schema_jsonld",
    "meta_tags",
    "content",
    "signals",
    "ai_discovery",
    "brand_entity",
)
CHECK_METADATA = {
    "robots_txt": {
        "category": "crawler-access",
        "title": "AI crawler access through robots.txt",
        "severity": "critical",
        "action": "Publish or update robots.txt so citation-oriented AI crawlers can access the intended public pages.",
    },
    "llms_txt": {
        "category": "llm-readable-delivery",
        "title": "llms.txt availability and structure",
        "severity": "high",
        "action": "Publish a valid llms.txt with an H1, a concise description, sections, and links to canonical source pages.",
    },
    "schema_jsonld": {
        "category": "structured-data",
        "title": "JSON-LD entity and page schema",
        "severity": "high",
        "action": "Add valid JSON-LD for the site and relevant page types, then verify the rendered markup.",
    },
    "meta_tags": {
        "category": "page-metadata",
        "title": "Canonical page metadata",
        "severity": "medium",
        "action": "Add a unique title, description, canonical URL, and complete Open Graph metadata.",
    },
    "content": {
        "category": "content-citability",
        "title": "Extractable and citable page content",
        "severity": "high",
        "action": "Strengthen the H1, factual density, source links, heading hierarchy, lists or tables, and front-loaded answer text.",
    },
    "signals": {
        "category": "site-signals",
        "title": "Language, feed, and freshness signals",
        "severity": "low",
        "action": "Declare the document language and expose freshness and feed signals where they are supported.",
    },
    "ai_discovery": {
        "category": "ai-discovery",
        "title": "Machine-readable AI discovery endpoints",
        "severity": "medium",
        "action": "Expose appropriate AI discovery files or endpoints and keep their claims aligned with canonical pages.",
    },
    "brand_entity": {
        "category": "brand-entity",
        "title": "Brand entity consistency",
        "severity": "high",
        "action": "Use a consistent brand identity and connect authoritative organization and sameAs references.",
    },
}


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run or import a GeoReady JSON audit and create a GEO-Master evidence bundle."
    )
    parser.add_argument("--url", help="Public URL to audit.")
    parser.add_argument("--project-id", help="GEO-Master project identifier.")
    parser.add_argument("--task-id", help="GEO-Master audit task identifier.")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "--retest-from",
        type=Path,
        help="Previous adapter output directory. Reuses its target and compares findings.",
    )
    parser.add_argument(
        "--input",
        type=Path,
        help="Import an existing GeoReady JSON report instead of invoking the CLI.",
    )
    parser.add_argument("--geo-executable", default="geo")
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument(
        "--upstream-version",
        help="Override the detected GeoReady version, for reproducible imports.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow replacing adapter-owned files in an existing output directory.",
    )
    return parser.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def stable_id(prefix: str, *parts: object) -> str:
    material = "|".join("" if part is None else str(part) for part in parts)
    digest = hashlib.sha256(material.encode("utf-8")).hexdigest()[:20].upper()
    return f"{prefix}-{digest}"


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"File does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Invalid JSON in {path} at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return value


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError as exc:
        raise ValueError(f"Baseline findings do not exist: {path}") from exc
    records: list[dict[str, Any]] = []
    for index, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSONL in {path} at line {index}: {exc.msg}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"Expected an object in {path} at line {index}")
        records.append(value)
    return records


def prepare_output(output_dir: Path, force: bool) -> None:
    owned = (
        output_dir / "raw" / "geoready-audit.json",
        output_dir / "findings.jsonl",
        output_dir / "remediation-checklist.md",
        output_dir / "adapter-result.json",
        output_dir / "retest-delta.json",
    )
    existing = [path for path in owned if path.exists()]
    if existing and not force:
        names = ", ".join(str(path) for path in existing)
        raise ValueError(f"Output already contains adapter files; use --force to replace: {names}")
    if force:
        for path in existing:
            path.unlink()
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "raw").mkdir(parents=True, exist_ok=True)


def read_baseline(path: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    result = load_json(path / "adapter-result.json")
    findings = load_jsonl(path / "findings.jsonl")
    return result, findings


def resolve_run_context(args: argparse.Namespace) -> tuple[str, str, str, list[dict[str, Any]]]:
    baseline_findings: list[dict[str, Any]] = []
    if args.retest_from:
        baseline_result, baseline_findings = read_baseline(args.retest_from)
        summary = baseline_result.get("summary") or {}
        url = args.url or summary.get("target_url")
        project_id = args.project_id or baseline_result.get("project_id")
        task_id = args.task_id or baseline_result.get("task_id")
    else:
        url, project_id, task_id = args.url, args.project_id, args.task_id

    missing = [
        name
        for name, value in (("--url", url), ("--project-id", project_id), ("--task-id", task_id))
        if not value
    ]
    if missing:
        raise ValueError("Missing required run context: " + ", ".join(missing))
    return str(url), str(project_id), str(task_id), baseline_findings


def detect_version(executable: str, override: str | None) -> str:
    if override:
        return override
    if not shutil.which(executable):
        return "unknown"
    try:
        result = subprocess.run(
            [executable, "--version"],
            capture_output=True,
            text=True,
            check=False,
            timeout=15,
        )
    except (OSError, subprocess.SubprocessError):
        return "unknown"
    text = (result.stdout or result.stderr).strip()
    return text or "unknown"


def collect_report(
    args: argparse.Namespace, url: str
) -> tuple[bytes, str, int, str, str, int]:
    started_at = utc_now()
    started = time.monotonic()
    if args.input:
        try:
            raw = args.input.read_bytes()
        except FileNotFoundError as exc:
            raise ValueError(f"Input file does not exist: {args.input}") from exc
        command = f"import {args.input}"
        return raw, command, 0, started_at, utc_now(), 0

    command_parts = [
        args.geo_executable,
        "audit",
        "--url",
        url,
        "--format",
        "json",
    ]
    try:
        result = subprocess.run(
            command_parts,
            capture_output=True,
            check=False,
            timeout=args.timeout,
        )
    except FileNotFoundError as exc:
        raise ValueError(
            f"GeoReady executable not found: {args.geo_executable}. "
            "Install geo-optimizer-skill or use --input."
        ) from exc
    except subprocess.TimeoutExpired as exc:
        raise ValueError(f"GeoReady audit exceeded {args.timeout} seconds") from exc

    latency_ms = round((time.monotonic() - started) * 1000)
    if result.returncode != 0:
        stderr = result.stderr.decode("utf-8", errors="replace").strip()
        detail = stderr.splitlines()[-1][:300] if stderr else "no stderr"
        raise ValueError(f"GeoReady exited with code {result.returncode}: {detail}")
    return (
        result.stdout,
        " ".join(command_parts),
        result.returncode,
        started_at,
        utc_now(),
        latency_ms,
    )


def parse_report(raw: bytes) -> dict[str, Any]:
    try:
        report = json.loads(raw.decode("utf-8"))
    except UnicodeDecodeError as exc:
        raise ValueError("GeoReady output is not UTF-8 JSON") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"GeoReady output is invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc
    if not isinstance(report, dict):
        raise ValueError("GeoReady output must be a JSON object")
    if report.get("error"):
        raise ValueError(f"GeoReady reported an audit error: {report['error']}")
    if not isinstance(report.get("checks"), dict):
        raise ValueError("GeoReady output is missing the checks object")
    return report


def check_passed(check_id: str, value: dict[str, Any]) -> bool | None:
    if isinstance(value.get("passed"), bool):
        return value["passed"]
    details = value.get("details") if isinstance(value.get("details"), dict) else value
    rules = {
        "robots_txt": lambda item: item.get("citation_bots_ok"),
        "llms_txt": lambda item: bool(item.get("found") and item.get("has_h1")),
        "schema_jsonld": lambda item: item.get("has_website"),
        "meta_tags": lambda item: bool(item.get("has_title") and item.get("has_description")),
        "content": lambda item: item.get("has_h1"),
        "signals": lambda item: item.get("has_lang"),
        "ai_discovery": lambda item: (item.get("endpoints_found") or 0) >= 1,
        "brand_entity": lambda item: item.get("brand_name_consistent"),
    }
    candidate = rules[check_id](details)
    return candidate if isinstance(candidate, bool) else None


def normalize_findings(
    report: dict[str, Any],
    *,
    project_id: str,
    task_id: str,
    target_url: str,
    raw_artifact_id: str,
    raw_sha256: str,
    upstream_version: str,
) -> tuple[list[dict[str, Any]], list[str]]:
    checks = report["checks"]
    observed_at = str(report.get("timestamp") or utc_now())
    findings: list[dict[str, Any]] = []
    warnings: list[str] = []

    for check_id in CHECK_ORDER:
        value = checks.get(check_id)
        if not isinstance(value, dict):
            warnings.append(f"GeoReady output omitted check: {check_id}")
            continue
        metadata = CHECK_METADATA[check_id]
        passed = check_passed(check_id, value)
        status = "pass" if passed is True else "fail" if passed is False else "not_evaluable"
        score = value.get("score")
        max_score = value.get("max")
        if not isinstance(score, (int, float)):
            score = (report.get("score_breakdown") or {}).get(
                check_id.replace("_txt", "").replace("_jsonld", "")
            )
        if not isinstance(score, (int, float)):
            score = None
        if not isinstance(max_score, (int, float)):
            max_score = None
        score_text = (
            f"score={score:g}/{max_score:g}"
            if score is not None and max_score is not None
            else "score=not provided"
        )
        observed_summary = f"passed={str(passed).lower() if passed is not None else 'unknown'}; {score_text}"
        finding_id = stable_id("FINDING", project_id, target_url, check_id)
        findings.append(
            {
                "schema_version": "0.1.0",
                "finding_id": finding_id,
                "project_id": project_id,
                "task_id": task_id,
                "target_url": target_url,
                "observed_at": observed_at,
                "category": metadata["category"],
                "check_id": check_id,
                "title": metadata["title"],
                "status": status,
                "severity": "info" if status == "pass" else metadata["severity"],
                "score": score,
                "max_score": max_score,
                "observed_summary": observed_summary,
                "remediation": {
                    "state": "not_required" if status == "pass" else "open",
                    "action": metadata["action"],
                },
                "evidence": {
                    "artifact_id": raw_artifact_id,
                    "location": "raw/geoready-audit.json",
                    "sha256": raw_sha256,
                    "json_pointer": f"/checks/{check_id}",
                },
                "source": {
                    "adapter": "geoready-cli",
                    "adapter_version": ADAPTER_VERSION,
                    "upstream_repository": UPSTREAM_REPOSITORY,
                    "upstream_version": upstream_version,
                    "upstream_schema_version": report.get("schema_version"),
                },
                "review": {
                    "state": "machine_reviewed",
                    "notes": "Verify the raw evidence before changing production crawler, schema, or publishing settings.",
                },
            }
        )
    if not findings:
        raise ValueError("GeoReady output did not contain any supported audit checks")
    return findings, warnings


def compare_findings(
    baseline: list[dict[str, Any]], current: list[dict[str, Any]]
) -> dict[str, Any]:
    before = {item["finding_id"]: item for item in baseline}
    after = {item["finding_id"]: item for item in current}
    changes: list[dict[str, Any]] = []
    counts = {
        "fixed": 0,
        "regressed": 0,
        "still_failing": 0,
        "still_passing": 0,
        "new": 0,
        "removed": 0,
    }
    for finding_id in sorted(set(before) | set(after)):
        old = before.get(finding_id)
        new = after.get(finding_id)
        old_status = old.get("status") if old else None
        new_status = new.get("status") if new else None
        if old is None:
            classification = "new"
        elif new is None:
            classification = "removed"
        elif old_status != "pass" and new_status == "pass":
            classification = "fixed"
        elif old_status == "pass" and new_status != "pass":
            classification = "regressed"
        elif new_status == "pass":
            classification = "still_passing"
        else:
            classification = "still_failing"
        counts[classification] += 1
        changes.append(
            {
                "finding_id": finding_id,
                "check_id": (new or old).get("check_id"),
                "before_status": old_status,
                "after_status": new_status,
                "classification": classification,
                "before_score": old.get("score") if old else None,
                "after_score": new.get("score") if new else None,
            }
        )
    return {
        "schema_version": "0.1.0",
        "generated_at": utc_now(),
        "summary": counts,
        "changes": changes,
    }


def markdown_escape(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def write_checklist(
    path: Path,
    *,
    target_url: str,
    result_id: str,
    raw_sha256: str,
    findings: list[dict[str, Any]],
    recommendations: list[Any],
    delta: dict[str, Any] | None,
) -> None:
    open_findings = [item for item in findings if item["status"] != "pass"]
    lines = [
        "# GeoReady evidence remediation checklist",
        "",
        f"- Target: `{target_url}`",
        f"- Adapter result: `{result_id}`",
        f"- Raw evidence: `raw/geoready-audit.json`",
        f"- Raw SHA-256: `{raw_sha256}`",
        f"- Open findings: **{len(open_findings)}** / {len(findings)}",
        "",
        "| State | Severity | Check | Observation | Evidence | Remediation |",
        "|---|---|---|---|---|---|",
    ]
    for finding in open_findings:
        lines.append(
            "| [ ] | {severity} | `{check}` | {observation} | "
            "`{location}#{pointer}` | {action} |".format(
                severity=markdown_escape(finding["severity"]),
                check=markdown_escape(finding["check_id"]),
                observation=markdown_escape(finding["observed_summary"]),
                location=markdown_escape(finding["evidence"]["location"]),
                pointer=markdown_escape(finding["evidence"]["json_pointer"]),
                action=markdown_escape(finding["remediation"]["action"]),
            )
        )
    if not open_findings:
        lines.append("| [x] | info | — | All normalized checks passed. | raw report | No action required. |")

    if recommendations:
        lines.extend(["", "## Upstream recommendations", ""])
        for index, recommendation in enumerate(recommendations):
            lines.append(
                f"- `{markdown_escape(f'/recommendations/{index}')}` — "
                f"{markdown_escape(recommendation)}"
            )

    if delta:
        summary = delta["summary"]
        lines.extend(
            [
                "",
                "## Retest result",
                "",
                f"- Fixed: **{summary['fixed']}**",
                f"- Regressed: **{summary['regressed']}**",
                f"- Still failing: **{summary['still_failing']}**",
                f"- Still passing: **{summary['still_passing']}**",
            ]
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def artifact(
    artifact_id: str,
    kind: str,
    location: str,
    media_type: str,
    sha256: str,
    *,
    schema_id: str | None = None,
    record_count: int | None = None,
) -> dict[str, Any]:
    return {
        "artifact_id": artifact_id,
        "kind": kind,
        "location": location,
        "media_type": media_type,
        "sha256": sha256,
        "schema_id": schema_id,
        "record_count": record_count,
    }


def main() -> int:
    args = arguments()
    try:
        target_url, project_id, task_id, baseline_findings = resolve_run_context(args)
        prepare_output(args.output_dir, args.force)
        upstream_version = detect_version(args.geo_executable, args.upstream_version)
        raw, command, _, started_at, completed_at, latency_ms = collect_report(args, target_url)

        raw_path = args.output_dir / "raw" / "geoready-audit.json"
        raw_path.write_bytes(raw)
        raw_sha256 = sha256_bytes(raw)
        raw_artifact_id = stable_id("RAW-GEOREADY", raw_sha256)
        report = parse_report(raw)
        findings, normalization_warnings = normalize_findings(
            report,
            project_id=project_id,
            task_id=task_id,
            target_url=target_url,
            raw_artifact_id=raw_artifact_id,
            raw_sha256=raw_sha256,
            upstream_version=upstream_version,
        )

        findings_path = args.output_dir / "findings.jsonl"
        findings_bytes = "".join(
            json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n"
            for item in findings
        ).encode("utf-8")
        findings_path.write_bytes(findings_bytes)
        findings_sha256 = sha256_bytes(findings_bytes)

        delta = compare_findings(baseline_findings, findings) if baseline_findings else None
        if delta:
            (args.output_dir / "retest-delta.json").write_text(
                json.dumps(delta, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

        result_id = stable_id("ADAPTER-RESULT", project_id, task_id, completed_at, raw_sha256)
        checklist_path = args.output_dir / "remediation-checklist.md"
        recommendations = report.get("recommendations")
        if not isinstance(recommendations, list):
            recommendations = []
        write_checklist(
            checklist_path,
            target_url=target_url,
            result_id=result_id,
            raw_sha256=raw_sha256,
            findings=findings,
            recommendations=recommendations,
            delta=delta,
        )
        checklist_sha256 = sha256_bytes(checklist_path.read_bytes())

        status_counts = {
            state: sum(1 for item in findings if item["status"] == state)
            for state in ("pass", "fail", "not_evaluable")
        }
        warnings = [
            {
                "code": "UPSTREAM_SCORE_NOT_CANONICAL",
                "severity": "info",
                "message": "GeoReady's aggregate score is preserved as upstream evidence, not a GEO-Master official metric.",
            }
        ]
        warnings.extend(
            {
                "code": "UPSTREAM_CHECK_OMITTED",
                "severity": "warning",
                "message": message,
            }
            for message in normalization_warnings
        )
        normalized_artifacts = [
            artifact(
                stable_id("NORMALIZED-FINDINGS", findings_sha256),
                "normalized-records",
                "findings.jsonl",
                "application/x-ndjson",
                findings_sha256,
                schema_id="geo-master/audit-finding/0.1.0",
                record_count=len(findings),
            ),
            artifact(
                stable_id("REMEDIATION-CHECKLIST", checklist_sha256),
                "report",
                "remediation-checklist.md",
                "text/markdown",
                checklist_sha256,
                record_count=len([item for item in findings if item["status"] != "pass"]),
            ),
        ]
        if delta:
            delta_path = args.output_dir / "retest-delta.json"
            delta_sha256 = sha256_bytes(delta_path.read_bytes())
            normalized_artifacts.append(
                artifact(
                    stable_id("RETEST-DELTA", delta_sha256),
                    "report",
                    "retest-delta.json",
                    "application/json",
                    delta_sha256,
                    schema_id="geo-master/audit-retest-delta/0.1.0",
                    record_count=len(delta["changes"]),
                )
            )

        adapter_result = {
            "schema_version": "0.1.0",
            "result_id": result_id,
            "project_id": project_id,
            "task_id": task_id,
            "capability_id": "site-technical-audit",
            "adapter": {
                "name": "geoready-cli",
                "version": ADAPTER_VERSION,
                "integration_mode": "cli-adapter",
                "upstream_repository": UPSTREAM_REPOSITORY,
                "upstream_version": upstream_version,
            },
            "started_at": started_at,
            "completed_at": completed_at,
            "status": "completed" if not normalization_warnings else "partial",
            "execution": {
                "collection_method": "imported_dataset" if args.input else "external_cli",
                "attempt": 1,
                "request_id": None,
                "command": command,
                "latency_ms": latency_ms,
                "cost": 0,
                "cost_currency": "USD",
            },
            "raw_artifacts": [
                artifact(
                    raw_artifact_id,
                    "audit-report",
                    "raw/geoready-audit.json",
                    "application/json",
                    raw_sha256,
                    record_count=1,
                )
            ],
            "normalized_artifacts": normalized_artifacts,
            "warnings": warnings,
            "summary": {
                "target_url": target_url,
                "upstream_schema_version": report.get("schema_version"),
                "upstream_score": report.get("score"),
                "finding_count": len(findings),
                "pass_count": status_counts["pass"],
                "fail_count": status_counts["fail"],
                "not_evaluable_count": status_counts["not_evaluable"],
                "retest": delta["summary"] if delta else None,
            },
            "evidence": {
                "state": "machine_reviewed",
                "raw_preserved": True,
                "reviewer": "geo-master-geoready-adapter",
                "notes": "Human review is required before production changes.",
            },
        }
        result_path = args.output_dir / "adapter-result.json"
        result_path.write_text(
            json.dumps(adapter_result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(json.dumps(adapter_result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
