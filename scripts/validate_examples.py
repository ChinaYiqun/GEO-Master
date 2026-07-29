#!/usr/bin/env python3

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("ERROR: jsonschema is required. Install with: pip install jsonschema", file=sys.stderr)
    raise SystemExit(1)


ROOT = Path(__file__).resolve().parents[1]
PAIRS = [
    (
        ROOT / "schemas" / "engine-run.schema.json",
        ROOT / "data" / "examples" / "engine-run.example.json",
    ),
    (
        ROOT / "schemas" / "monitor-run.schema.json",
        ROOT / "data" / "examples" / "monitor-run.example.json",
    ),
    (
        ROOT / "schemas" / "content-task.schema.json",
        ROOT / "data" / "examples" / "content-task.example.json",
    ),
    (
        ROOT / "schemas" / "adapter-result.schema.json",
        ROOT / "data" / "examples" / "adapter-result.example.json",
    ),
]


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    failed = False
    for schema_path, example_path in PAIRS:
        try:
            schema = load(schema_path)
            example = load(example_path)
            Draft202012Validator.check_schema(schema)
            errors = sorted(
                Draft202012Validator(schema).iter_errors(example),
                key=lambda error: list(error.absolute_path),
            )
        except (OSError, json.JSONDecodeError) as exc:
            print(f"FAIL {schema_path} / {example_path}: {exc}")
            failed = True
            continue

        if errors:
            failed = True
            print(f"FAIL {example_path} against {schema_path}")
            for error in errors:
                location = ".".join(str(part) for part in error.absolute_path) or "<root>"
                print(f"  {location}: {error.message}")
        else:
            print(f"PASS {example_path.relative_to(ROOT)}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
