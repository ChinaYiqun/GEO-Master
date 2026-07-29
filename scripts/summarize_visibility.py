#!/usr/bin/env python3
"""Summarize GEO-Master weekly monitoring CSV files.

The script intentionally excludes unknown or blank observations from rate
calculations instead of silently treating missing data as a negative result.
It uses only the Python standard library so it can run locally or in CI.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable

REQUIRED_COLUMNS = {
    "platform",
    "brand_mentioned",
    "official_site_cited",
    "recommended",
    "product_facts_accurate",
    "sentiment",
}

TRUE_VALUES = {"1", "true", "yes", "y"}
FALSE_VALUES = {"0", "false", "no", "n"}
UNKNOWN_VALUES = {"", "unknown", "not_provided", "not_applicable", "null", "na", "n/a"}
FACT_EVALUABLE = {"accurate", "partial", "incorrect", "outdated", "conflicting"}


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Summarize brand mention, citation, recommendation and accuracy rates."
    )
    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        default=Path("templates/weekly-monitoring.csv"),
        help="GEO-Master weekly monitoring CSV (default: templates/weekly-monitoring.csv)",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format (default: markdown)",
    )
    parser.add_argument("--output", type=Path, help="Write output to a file instead of stdout")
    return parser.parse_args()


def normalized(value: object) -> str:
    return "" if value is None else str(value).strip().lower()


def parse_bool(value: object) -> bool | None:
    text = normalized(value)
    if text in TRUE_VALUES:
        return True
    if text in FALSE_VALUES:
        return False
    if text in UNKNOWN_VALUES:
        return None
    raise ValueError(f"Unsupported boolean value: {value!r}")


def percentage(numerator: int, denominator: int) -> float | None:
    if denominator == 0:
        return None
    return round(numerator * 100.0 / denominator, 2)


def metric(rows: Iterable[dict[str, str]], column: str) -> dict[str, int | float | None]:
    yes = 0
    evaluable = 0
    for row in rows:
        value = parse_bool(row.get(column))
        if value is None:
            continue
        evaluable += 1
        yes += int(value)
    return {"yes": yes, "evaluable": evaluable, "rate_pct": percentage(yes, evaluable)}


def fact_metric(rows: Iterable[dict[str, str]]) -> dict[str, object]:
    counts: dict[str, int] = defaultdict(int)
    evaluable = 0
    accurate = 0
    for row in rows:
        value = normalized(row.get("product_facts_accurate"))
        if value in UNKNOWN_VALUES:
            continue
        counts[value] += 1
        if value in FACT_EVALUABLE:
            evaluable += 1
            accurate += int(value == "accurate")
    return {
        "accurate": accurate,
        "evaluable": evaluable,
        "rate_pct": percentage(accurate, evaluable),
        "counts": dict(sorted(counts.items())),
    }


def sentiment_metric(rows: Iterable[dict[str, str]]) -> dict[str, object]:
    counts: dict[str, int] = defaultdict(int)
    evaluable = 0
    negative = 0
    for row in rows:
        value = normalized(row.get("sentiment"))
        if value in UNKNOWN_VALUES:
            continue
        counts[value] += 1
        evaluable += 1
        negative += int(value == "negative")
    return {
        "negative": negative,
        "evaluable": evaluable,
        "negative_rate_pct": percentage(negative, evaluable),
        "counts": dict(sorted(counts.items())),
    }


def summarize_group(rows: list[dict[str, str]]) -> dict[str, object]:
    return {
        "runs": len(rows),
        "brand_mention": metric(rows, "brand_mentioned"),
        "official_site_citation": metric(rows, "official_site_cited"),
        "recommendation": metric(rows, "recommended"),
        "fact_accuracy": fact_metric(rows),
        "sentiment": sentiment_metric(rows),
    }


def load_rows(path: Path) -> list[dict[str, str]]:
    try:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None:
                raise ValueError("CSV has no header row.")
            missing = sorted(REQUIRED_COLUMNS - set(reader.fieldnames))
            if missing:
                raise ValueError(f"CSV is missing required columns: {', '.join(missing)}")
            rows = [dict(row) for row in reader]
    except FileNotFoundError as exc:
        raise ValueError(f"Input file does not exist: {path}") from exc
    if not rows:
        raise ValueError("CSV contains no data rows.")
    return rows


def build_summary(path: Path, rows: list[dict[str, str]]) -> dict[str, object]:
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[row.get("platform", "").strip() or "unknown"].append(row)
    return {
        "schema_version": "0.1.0",
        "source": str(path),
        "methodology": "Unknown and blank values are excluded from denominators.",
        "overall": summarize_group(rows),
        "platforms": {name: summarize_group(groups[name]) for name in sorted(groups)},
    }


def display_rate(value: object) -> str:
    return "—" if value is None else f"{value}%"


def markdown(summary: dict[str, object]) -> str:
    overall = summary["overall"]
    assert isinstance(overall, dict)
    lines = [
        "# GEO Visibility Summary",
        "",
        f"Source: `{summary['source']}`",
        "",
        "> Unknown and blank observations are excluded from rate denominators.",
        "",
        "| Scope | Runs | Brand mention | Official citation | Recommendation | Fact accuracy | Negative sentiment |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]

    def row(label: str, data: dict[str, object]) -> str:
        return "| {label} | {runs} | {mention} | {citation} | {recommendation} | {accuracy} | {negative} |".format(
            label=label,
            runs=data["runs"],
            mention=display_rate(data["brand_mention"]["rate_pct"]),
            citation=display_rate(data["official_site_citation"]["rate_pct"]),
            recommendation=display_rate(data["recommendation"]["rate_pct"]),
            accuracy=display_rate(data["fact_accuracy"]["rate_pct"]),
            negative=display_rate(data["sentiment"]["negative_rate_pct"]),
        )

    lines.append(row("Overall", overall))
    platforms = summary["platforms"]
    assert isinstance(platforms, dict)
    for name, data in platforms.items():
        lines.append(row(str(name), data))
    lines.append("")
    return "\n".join(lines)


def render(summary: dict[str, object], output_format: str) -> str:
    if output_format == "json":
        return json.dumps(summary, ensure_ascii=False, indent=2) + "\n"
    return markdown(summary)


def main() -> int:
    args = arguments()
    try:
        rows = load_rows(args.input)
        text = render(build_summary(args.input, rows), args.format)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(text, encoding="utf-8")
        else:
            sys.stdout.write(text)
        return 0
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
