#!/usr/bin/env python3

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = Path(__file__).with_name("geoready_audit_adapter.py")
FINDING_SCHEMA = json.loads(
    (ROOT / "schemas" / "audit-finding.schema.json").read_text(encoding="utf-8")
)
RESULT_SCHEMA = json.loads(
    (ROOT / "schemas" / "adapter-result.schema.json").read_text(encoding="utf-8")
)


def audit_payload(*, robots_passed=False, llms_passed=False):
    checks = {}
    scores = {
        "robots_txt": (10, 18, robots_passed),
        "llms_txt": (8, 18, llms_passed),
        "schema_jsonld": (16, 16, True),
        "meta_tags": (14, 14, True),
        "content": (6, 12, False),
        "signals": (6, 6, True),
        "ai_discovery": (0, 6, False),
        "brand_entity": (10, 10, True),
    }
    for check_id, (score, maximum, passed) in scores.items():
        checks[check_id] = {
            "score": score,
            "max": maximum,
            "passed": passed,
            "details": {"fixture": True},
        }
    return {
        "url": "https://example.com",
        "timestamp": "2026-07-29T08:00:00+00:00",
        "score": 70,
        "band": "good",
        "score_breakdown": {},
        "recommendations": ["Add a complete llms.txt.", "Front-load factual answers."],
        "error": None,
        "checks": checks,
    }


class GeoReadyAuditAdapterTest(unittest.TestCase):
    def run_adapter(self, root: Path, payload, *extra):
        input_path = root / f"input-{len(list(root.glob('input-*.json')))}.json"
        input_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        output_dir = root / f"output-{len(list(root.glob('output-*')))}"
        command = [
            sys.executable,
            str(SCRIPT),
            "--input",
            str(input_path),
            "--output-dir",
            str(output_dir),
            "--url",
            "https://example.com",
            "--project-id",
            "PROJECT-TEST",
            "--task-id",
            "TASK-AUDIT-TEST",
            "--upstream-version",
            "4.15.0",
            *extra,
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        return output_dir

    def test_creates_schema_valid_evidence_bundle(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output = self.run_adapter(root, audit_payload())
            findings = [
                json.loads(line)
                for line in (output / "findings.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            adapter_result = json.loads(
                (output / "adapter-result.json").read_text(encoding="utf-8")
            )

            self.assertEqual(len(findings), 8)
            self.assertEqual(adapter_result["summary"]["fail_count"], 4)
            self.assertEqual(adapter_result["summary"]["pass_count"], 4)
            self.assertEqual(
                (output / "raw" / "geoready-audit.json").read_text(encoding="utf-8"),
                (root / "input-0.json").read_text(encoding="utf-8"),
            )
            self.assertIn(
                "`raw/geoready-audit.json#/checks/robots_txt`",
                (output / "remediation-checklist.md").read_text(encoding="utf-8"),
            )

            finding_validator = Draft202012Validator(
                FINDING_SCHEMA, format_checker=FormatChecker()
            )
            for finding in findings:
                errors = list(finding_validator.iter_errors(finding))
                self.assertEqual(errors, [], [error.message for error in errors])
            result_errors = list(
                Draft202012Validator(
                    RESULT_SCHEMA, format_checker=FormatChecker()
                ).iter_errors(adapter_result)
            )
            self.assertEqual(result_errors, [], [error.message for error in result_errors])

    def test_retest_compares_the_same_stable_findings(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            baseline = self.run_adapter(root, audit_payload())

            input_path = root / "retest.json"
            input_path.write_text(
                json.dumps(
                    audit_payload(robots_passed=True, llms_passed=True),
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            output = root / "retest-output"
            command = [
                sys.executable,
                str(SCRIPT),
                "--input",
                str(input_path),
                "--output-dir",
                str(output),
                "--retest-from",
                str(baseline),
                "--upstream-version",
                "4.15.0",
            ]
            result = subprocess.run(command, capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

            delta = json.loads((output / "retest-delta.json").read_text(encoding="utf-8"))
            self.assertEqual(delta["summary"]["fixed"], 2)
            self.assertEqual(delta["summary"]["still_failing"], 2)
            self.assertEqual(delta["summary"]["regressed"], 0)
            self.assertIn(
                "Fixed: **2**",
                (output / "remediation-checklist.md").read_text(encoding="utf-8"),
            )


if __name__ == "__main__":
    unittest.main()
