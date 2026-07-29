#!/usr/bin/env python3
"""Validate GEO-Master's upstream capability registry.

The JSON Schema checks structure. This script adds semantic checks that are
important for license safety and for keeping capability references consistent.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "integration-registry.schema.json"
REGISTRY_PATH = ROOT / "integrations" / "upstream-capabilities.json"


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except FileNotFoundError as exc:
        raise RuntimeError(f"missing file: {path.relative_to(ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"invalid JSON in {path.relative_to(ROOT)} at line {exc.lineno}, "
            f"column {exc.colno}: {exc.msg}"
        ) from exc

    if not isinstance(value, dict):
        raise RuntimeError(f"expected JSON object in {path.relative_to(ROOT)}")
    return value


def duplicate_values(values: list[str]) -> list[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return sorted(duplicates)


def validate_schema(schema: dict[str, Any], registry: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors: list[str] = []
    for error in sorted(validator.iter_errors(registry), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        errors.append(f"schema: {location}: {error.message}")
    return errors


def validate_semantics(registry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    capabilities = registry.get("capabilities", [])
    upstreams = registry.get("upstreams", [])

    capability_ids = [item["id"] for item in capabilities]
    upstream_ids = [item["id"] for item in upstreams]
    repositories = [item["repository"].lower() for item in upstreams]

    for duplicate in duplicate_values(capability_ids):
        errors.append(f"semantic: duplicate capability id: {duplicate}")
    for duplicate in duplicate_values(upstream_ids):
        errors.append(f"semantic: duplicate upstream id: {duplicate}")
    for duplicate in duplicate_values(repositories):
        errors.append(f"semantic: duplicate upstream repository: {duplicate}")

    known_capabilities = set(capability_ids)
    for upstream in upstreams:
        upstream_id = upstream["id"]
        unknown = sorted(set(upstream["capability_ids"]) - known_capabilities)
        if unknown:
            errors.append(
                f"semantic: {upstream_id} references unknown capabilities: "
                + ", ".join(unknown)
            )

        adoption = upstream["adoption"]
        if not adoption["retained"]:
            errors.append(f"semantic: {upstream_id} must retain at least one capability")
        if not adoption["geo_master_differentiation"]:
            errors.append(
                f"semantic: {upstream_id} must document GEO-Master differentiation"
            )
        if not adoption["prohibited"]:
            errors.append(f"semantic: {upstream_id} must document prohibited actions")

        if upstream["compatibility"] == "copyleft-process-boundary":
            if upstream["integration_mode"] != "external-service-adapter":
                errors.append(
                    f"license: {upstream_id} is copyleft and must use an "
                    "external-service-adapter"
                )
            if upstream["status"] not in {"external-only", "adapter-planned"}:
                errors.append(
                    f"license: {upstream_id} copyleft status must remain external-only "
                    "or adapter-planned"
                )

        if upstream["status"] == "reference" and upstream["integration_mode"] != "reference-standard":
            errors.append(
                f"semantic: {upstream_id} reference status requires reference-standard mode"
            )

        if upstream["integration_mode"] == "reference-standard" and upstream["status"] not in {
            "reference",
            "absorbed",
        }:
            errors.append(
                f"semantic: {upstream_id} reference-standard mode must be reference or absorbed"
            )

    return errors


def main() -> int:
    try:
        schema = load_json(SCHEMA_PATH)
        registry = load_json(REGISTRY_PATH)
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    errors = validate_schema(schema, registry)
    if not errors:
        errors.extend(validate_semantics(registry))

    if errors:
        print("Integration registry validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Integration registry valid: "
        f"{len(registry['capabilities'])} capabilities, "
        f"{len(registry['upstreams'])} upstream projects."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
