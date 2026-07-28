#!/usr/bin/env python3

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("import_monitor_runs.py")


class ImportMonitorRunsTest(unittest.TestCase):
    def run_import(self, source: str, payload, extra_args=None):
        extra_args = extra_args or []
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_path = root / "input.json"
            output_dir = root / "output"
            input_path.write_text(json.dumps(payload), encoding="utf-8")

            command = [
                sys.executable,
                str(SCRIPT),
                str(input_path),
                "--source",
                source,
                "--project-id",
                "PROJECT-TEST",
                "--brand",
                "Example Brand",
                "--official-domain",
                "example.com",
                "--output-dir",
                str(output_dir),
                *extra_args,
            ]
            result = subprocess.run(command, capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

            records = [
                json.loads(line)
                for line in (output_dir / "monitor-runs.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            manifest = json.loads((output_dir / "import-manifest.json").read_text(encoding="utf-8"))
            raw_files = list((output_dir / "raw").glob("*.txt"))
            return records, manifest, raw_files

    def test_geo_aeo_tracker_run(self):
        records, manifest, raw_files = self.run_import(
            "geo-aeo-tracker",
            [
                {
                    "provider": "chatgpt",
                    "prompt": "What are the best AI visibility tools?",
                    "answer": "Example Brand is listed with Competitor A.",
                    "sources": [
                        "https://example.com/product",
                        "https://industry.example.org/tools",
                    ],
                    "createdAt": "2026-07-28T10:00:00+00:00",
                    "visibilityScore": 72,
                    "sentiment": "positive",
                    "brandMentions": ["Example Brand"],
                    "competitorMentions": ["Competitor A"],
                    "country": "US",
                }
            ],
        )

        self.assertEqual(manifest["records_written"], 1)
        self.assertEqual(len(records), 1)
        self.assertEqual(len(raw_files), 1)
        record = records[0]
        self.assertEqual(record["provider"]["product"], "chatgpt")
        self.assertTrue(record["observation"]["brand_mentioned"])
        self.assertTrue(record["observation"]["official_site_cited"])
        self.assertFalse(record["observation"]["explicitly_recommended"])
        self.assertEqual(record["observation"]["fact_accuracy"], "not_evaluable")
        self.assertEqual(record["context"]["country"], "US")
        self.assertEqual(len(record["citations"]), 2)

    def test_elmo_prompt_run_with_prompt_map(self):
        records, manifest, raw_files = self.run_import(
            "elmo",
            {
                "prompts": [
                    {
                        "id": "PROMPT-1",
                        "value": "Compare AI visibility platforms.",
                    }
                ],
                "runs": [
                    {
                        "id": "RUN-ELMO-1",
                        "promptId": "PROMPT-1",
                        "model": "claude",
                        "version": "claude-example",
                        "webSearchEnabled": True,
                        "textContent": "Example Brand and Competitor B are discussed.",
                        "brandMentioned": True,
                        "competitorsMentioned": ["Competitor B"],
                        "citations": [
                            {
                                "url": "https://example.com/comparison",
                                "domain": "example.com",
                                "title": "Comparison",
                            }
                        ],
                        "createdAt": "2026-07-28T11:00:00+00:00",
                    }
                ],
            },
        )

        self.assertEqual(manifest["records_failed"], 0)
        self.assertEqual(len(records), 1)
        self.assertEqual(len(raw_files), 1)
        record = records[0]
        self.assertEqual(record["run_id"], "RUN-ELMO-1")
        self.assertEqual(record["prompt"]["text"], "Compare AI visibility platforms.")
        self.assertEqual(record["provider"]["product"], "claude")
        self.assertEqual(record["provider"]["model_label"], "claude-example")
        self.assertEqual(record["observation"]["search_state"], "search_visible")
        self.assertTrue(record["citations"][0]["official_brand_source"])


if __name__ == "__main__":
    unittest.main()
