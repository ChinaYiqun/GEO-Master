#!/usr/bin/env python3
"""Convert Elmo or GEO/AEO Tracker records to GEO-Master monitor JSONL.

The importer preserves observable fields and deliberately does not infer
recommendations, factual accuracy, or model-internal citation attribution.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

SOURCE_NAMES = {
    "elmo": "Elmo",
    "geo-aeo-tracker": "GEO/AEO Tracker",
}


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--source", required=True, choices=sorted(SOURCE_NAMES))
    parser.add_argument("--output-dir", type=Path, default=Path("monitor-import"))
    parser.add_argument("--project-id", required=True)
    parser.add_argument("--brand", required=True)
    parser.add_argument("--brand-alias", action="append", default=[])
    parser.add_argument("--official-domain", action="append", default=[])
    parser.add_argument("--competitor", action="append", default=[])
    parser.add_argument("--country", default="ZZ")
    parser.add_argument("--language", default="und")
    parser.add_argument(
        "--interface",
        default="vendor_representation",
        choices=[
            "web_desktop",
            "web_mobile",
            "native_app",
            "api",
            "vendor_representation",
            "unknown",
        ],
    )
    parser.add_argument(
        "--collection-method",
        default="imported_dataset",
        choices=[
            "official_api",
            "consumer_web_manual",
            "consumer_app_manual",
            "browser_automation",
            "third_party_scraper",
            "data_vendor",
            "imported_dataset",
            "demo_data",
            "unknown",
        ],
    )
    parser.add_argument("--source-version")
    parser.add_argument("--batch-id")
    parser.add_argument("--prompt-map", type=Path)
    return parser.parse_args()


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Input file does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc


def runs_from(root) -> list[dict]:
    if isinstance(root, list):
        runs = root
    elif isinstance(root, dict):
        runs = next(
            (
                root.get(key)
                for key in ("runs", "promptRuns", "prompt_runs", "data")
                if isinstance(root.get(key), list)
            ),
            None,
        )
        if runs is None and isinstance(root.get("state"), dict):
            runs = root["state"].get("runs")
    else:
        runs = None
    if not isinstance(runs, list) or any(not isinstance(item, dict) for item in runs):
        raise ValueError("Expected an array of run objects or an object containing a run array.")
    return runs


def prompt_map_from(root, path: Path | None) -> dict[str, str]:
    mapping: dict[str, str] = {}
    if isinstance(root, dict) and isinstance(root.get("prompts"), list):
        for item in root["prompts"]:
            if not isinstance(item, dict):
                continue
            key = item.get("id") or item.get("promptId")
            value = item.get("value") or item.get("text") or item.get("prompt")
            if key and value:
                mapping[str(key)] = str(value)
    if path:
        external = load_json(path)
        if not isinstance(external, dict):
            raise ValueError("--prompt-map must contain a JSON object.")
        mapping.update({str(key): str(value) for key, value in external.items()})
    return mapping


def stable_id(prefix: str, *parts) -> str:
    material = "|".join("" if part is None else str(part) for part in parts)
    digest = hashlib.sha256(material.encode()).hexdigest()[:20].upper()
    return f"{prefix}-{digest}"


def domain(value: str | None) -> str | None:
    if not value:
        return None
    raw = value.strip().lower()
    parsed = urlparse(raw if "://" in raw else f"https://{raw}")
    return parsed.hostname.removeprefix("www.") if parsed.hostname else None


def is_official(host: str | None, official: set[str]) -> bool:
    return bool(host and any(host == item or host.endswith(f".{item}") for item in official))


def timestamp(value) -> str:
    if not value:
        raise ValueError("A run is missing its timestamp.")
    text = str(value).strip()
    parsed = datetime.fromisoformat(text[:-1] + "+00:00" if text.endswith("Z") else text)
    if parsed.tzinfo is None:
        raise ValueError(f"Timestamp must include a timezone: {text}")
    return parsed.isoformat()


def save_answer(output: Path, run_id: str, answer: str):
    if not answer:
        return None, None
    folder = output / "raw"
    folder.mkdir(parents=True, exist_ok=True)
    filename = re.sub(r"[^A-Za-z0-9._-]+", "_", run_id)[:120] + ".txt"
    path = folder / filename
    path.write_text(answer, encoding="utf-8")
    return str(path.relative_to(output)), hashlib.sha256(answer.encode()).hexdigest()


def search_state(web_search, citations: list[dict]) -> str:
    if web_search is True:
        return "search_visible"
    if citations:
        return "citations_without_clear_search_state"
    return "answer_without_visible_search"


def citation(run_id: str, position: int, url: str, host_hint, official: set[str]):
    host = domain(host_hint) or domain(url)
    official_source = is_official(host, official)
    return {
        "citation_id": stable_id("CIT", run_id, position, url),
        "url": url,
        "canonical_url": None,
        "registrable_domain": host,
        "position": position,
        "source_type": "official_site" if official_source else "unknown",
        "official_brand_source": official_source,
        "page_available": None,
        "absorption_label": "not_evaluable",
        "supported_claim_ids": [],
    }


def record(
    args,
    output: Path,
    *,
    run_id: str,
    batch_id: str,
    collected_at: str,
    prompt_id: str,
    prompt_text: str,
    provider: str,
    model_label,
    country: str,
    answer: str,
    citations: list[dict],
    brand_mentioned: bool,
    mentioned_competitors: list[str],
    sentiment: str,
    visible_search,
    source_record_id,
    notes: str,
):
    answer_location, digest = save_answer(output, run_id, answer)
    competitors = list(dict.fromkeys([*args.competitor, *mentioned_competitors]))
    return {
        "schema_version": "0.1.0",
        "run_id": run_id,
        "batch_id": batch_id,
        "experiment_id": None,
        "collected_at": collected_at,
        "project_id": args.project_id,
        "brand_fact_version": None,
        "query_set_version": None,
        "prompt": {
            "prompt_id": prompt_id,
            "parent_prompt_id": None,
            "text": prompt_text,
            "language": args.language,
            "intent": "other",
            "persona": None,
            "funnel_stage": "unknown",
        },
        "provider": {
            "product": provider,
            "model_label": model_label,
            "adapter": f"geo-master-{args.source}-importer",
            "adapter_version": "0.1.0",
            "collection_method": args.collection_method,
            "vendor_dataset_id": None,
            "request_id": None,
            "cost": None,
            "cost_currency": None,
            "latency_ms": None,
        },
        "context": {
            "country": country,
            "city": None,
            "language": args.language,
            "interface": args.interface,
            "account_state": "unknown",
            "plan_tier": None,
            "conversation_state": "unknown",
        },
        "targets": {
            "brand": args.brand,
            "brand_aliases": args.brand_alias,
            "product": None,
            "official_domains": sorted(args.official_domains),
            "competitors": competitors,
        },
        "status": {
            "state": "completed" if answer else "partial",
            "retry_count": 0,
            "error_code": None,
            "error_message": None if answer else "Source record did not contain answer text.",
        },
        "observation": {
            "search_state": search_state(visible_search, citations),
            "brand_mentioned": brand_mentioned,
            "mention_count": 1 if brand_mentioned else 0,
            "first_mention_position": None,
            "candidate_list_position": None,
            "official_site_cited": any(item["official_brand_source"] for item in citations),
            "explicitly_recommended": False,
            "recommendation_position": None,
            "recommendation_reason": None,
            "sentiment": sentiment,
            "fact_accuracy": "not_evaluable",
            "accuracy_notes": "Fact accuracy was not inferred during import.",
        },
        "citations": citations,
        "competitor_observations": [
            {
                "name": name,
                "mentioned": name in mentioned_competitors,
                "mention_position": None,
                "recommended": False,
                "recommendation_position": None,
                "cited_domains": [],
            }
            for name in competitors
        ],
        "evidence": {
            "answer_saved": bool(answer),
            "answer_location": answer_location,
            "screenshot_location": None,
            "answer_sha256": digest,
            "review_state": "machine_reviewed",
            "reviewer": None,
            "notes": notes,
        },
        "source_system": {
            "name": SOURCE_NAMES[args.source],
            "version": args.source_version,
            "source_record_id": source_record_id,
            "imported_at": datetime.now().astimezone().isoformat(),
        },
    }


def tracker_run(item, args, batch_id: str, output: Path):
    prompt_text = str(item.get("prompt") or "").strip()
    if not prompt_text:
        raise ValueError("GEO/AEO Tracker run is missing prompt text.")
    collected_at = timestamp(item.get("createdAt"))
    provider = str(item.get("provider") or "unknown")
    source_id = str(item["id"]) if item.get("id") else None
    prompt_id = stable_id("Q", prompt_text, args.language)
    run_id = source_id or stable_id("RUN", provider, prompt_text, collected_at, args.country)
    urls = [str(value) for value in item.get("sources", []) if value]
    citations = [
        citation(run_id, index, url, None, args.official_domains)
        for index, url in enumerate(urls, 1)
    ]
    mentions = [str(value) for value in item.get("brandMentions", [])]
    competitors = [str(value) for value in item.get("competitorMentions", [])]
    source_sentiment = str(item.get("sentiment") or "not-mentioned")
    sentiment = source_sentiment if source_sentiment in {"positive", "neutral", "negative"} else "unknown"
    return record(
        args,
        output,
        run_id=run_id,
        batch_id=batch_id,
        collected_at=collected_at,
        prompt_id=prompt_id,
        prompt_text=prompt_text,
        provider=provider,
        model_label=None,
        country=str(item.get("country") or args.country),
        answer=str(item.get("answer") or ""),
        citations=citations,
        brand_mentioned=bool(mentions),
        mentioned_competitors=competitors,
        sentiment=sentiment,
        visible_search=None,
        source_record_id=source_id,
        notes=(
            "Imported from GEO/AEO Tracker-compatible ScrapeRun data. "
            "Visibility scores were not copied; recommendation and accuracy were not inferred."
        ),
    )


def elmo_run(item, args, batch_id: str, prompts: dict[str, str], output: Path):
    source_prompt_id = str(item.get("promptId") or item.get("prompt_id") or "")
    prompt_text = str(
        item.get("prompt")
        or item.get("promptText")
        or item.get("promptValue")
        or prompts.get(source_prompt_id)
        or f"Prompt text unavailable for source prompt ID {source_prompt_id or 'unknown'}"
    )
    collected_at = timestamp(item.get("createdAt") or item.get("created_at"))
    provider = str(item.get("model") or "unknown")
    source_id = str(item["id"]) if item.get("id") else None
    prompt_id = source_prompt_id or stable_id("Q", prompt_text, args.language)
    run_id = source_id or stable_id("RUN", provider, prompt_id, collected_at, args.country)
    raw = item.get("rawOutput") or item.get("raw_output") or {}
    answer = str(item.get("textContent") or item.get("text_content") or raw.get("response") or "")
    citations = []
    for index, value in enumerate(item.get("citations") or [], 1):
        if isinstance(value, str):
            url, host = value, None
        elif isinstance(value, dict):
            url, host = str(value.get("url") or ""), value.get("domain")
        else:
            continue
        if url:
            citations.append(citation(run_id, index, url, host, args.official_domains))
    competitors = [
        str(value)
        for value in item.get("competitorsMentioned", item.get("competitors_mentioned", []))
    ]
    visible_search = item.get("webSearchEnabled")
    if visible_search is None:
        visible_search = item.get("web_search_enabled")
    return record(
        args,
        output,
        run_id=run_id,
        batch_id=batch_id,
        collected_at=collected_at,
        prompt_id=prompt_id,
        prompt_text=prompt_text,
        provider=provider,
        model_label=str(item.get("version")) if item.get("version") is not None else None,
        country=args.country,
        answer=answer,
        citations=citations,
        brand_mentioned=bool(item.get("brandMentioned") or item.get("brand_mentioned")),
        mentioned_competitors=competitors,
        sentiment="unknown",
        visible_search=bool(visible_search) if visible_search is not None else None,
        source_record_id=source_id,
        notes=(
            "Imported from Elmo-compatible prompt-run data. "
            "Recommendation, sentiment, and accuracy were not inferred."
        ),
    )


def main() -> int:
    args = arguments()
    try:
        root = load_json(args.input)
        source_runs = runs_from(root)
        prompts = prompt_map_from(root, args.prompt_map)
        args.official_domains = {
            normalized
            for value in args.official_domain
            if (normalized := domain(value))
        }
        args.output_dir.mkdir(parents=True, exist_ok=True)
        batch_id = args.batch_id or stable_id("BATCH", args.source, args.project_id, args.input.resolve())
        normalized, failures = [], []
        for index, item in enumerate(source_runs):
            try:
                if args.source == "elmo":
                    normalized.append(elmo_run(item, args, batch_id, prompts, args.output_dir))
                else:
                    normalized.append(tracker_run(item, args, batch_id, args.output_dir))
            except (TypeError, ValueError) as exc:
                failures.append({"index": index, "error": str(exc)})

        output_path = args.output_dir / "monitor-runs.jsonl"
        with output_path.open("w", encoding="utf-8") as handle:
            for item in normalized:
                handle.write(json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n")

        manifest = {
            "source": SOURCE_NAMES[args.source],
            "source_version": args.source_version,
            "input": str(args.input),
            "project_id": args.project_id,
            "batch_id": batch_id,
            "records_written": len(normalized),
            "records_failed": len(failures),
            "output_jsonl": str(output_path),
            "raw_directory": str(args.output_dir / "raw"),
            "errors": failures,
        }
        (args.output_dir / "import-manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(json.dumps(manifest, ensure_ascii=False, indent=2))
        return 0 if not failures else 2
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
