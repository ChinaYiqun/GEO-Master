#!/usr/bin/env python3
"""Tests for summarize_visibility.py using only the standard library."""

from __future__ import annotations

import csv
import importlib.util
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).with_name("summarize_visibility.py")
SPEC = importlib.util.spec_from_file_location("summarize_visibility", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def write_fixture(path: Path) -> None:
    fields = [
        "platform",
        "brand_mentioned",
        "official_site_cited",
        "recommended",
        "product_facts_accurate",
        "sentiment",
    ]
    rows = [
        ["ChatGPT Search", "yes", "yes", "yes", "accurate", "positive"],
        ["ChatGPT Search", "no", "no", "no", "partial", "neutral"],
        ["豆包", "yes", "unknown", "no", "unknown", "negative"],
        ["豆包", "unknown", "no", "unknown", "incorrect", "unknown"],
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(fields)
        writer.writerows(rows)


def main() -> None:
    with tempfile.TemporaryDirectory() as temporary:
        path = Path(temporary) / "runs.csv"
        write_fixture(path)
        summary = MODULE.build_summary(path, MODULE.load_rows(path))

    overall = summary["overall"]
    assert overall["runs"] == 4
    assert overall["brand_mention"] == {"yes": 2, "evaluable": 3, "rate_pct": 66.67}
    assert overall["official_site_citation"] == {"yes": 1, "evaluable": 3, "rate_pct": 33.33}
    assert overall["recommendation"] == {"yes": 1, "evaluable": 3, "rate_pct": 33.33}
    assert overall["fact_accuracy"]["rate_pct"] == 33.33
    assert overall["sentiment"]["negative_rate_pct"] == 33.33
    assert set(summary["platforms"]) == {"ChatGPT Search", "豆包"}
    output = MODULE.markdown(summary)
    assert "Unknown and blank observations" in output
    assert "ChatGPT Search" in output and "豆包" in output
    print("summarize_visibility tests passed")


if __name__ == "__main__":
    main()
