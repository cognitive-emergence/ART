#!/usr/bin/env python3
"""Validate the ART falsification corpus against its schema and index."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "corpus"
SCHEMA_PATH = CORPUS / "schema" / "art-case.schema.json"
INDEX_PATH = CORPUS / "index.json"
CASES_DIR = CORPUS / "cases"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    index = load_json(INDEX_PATH)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    case_files = sorted(CASES_DIR.rglob("ART-CASE-*.json"))
    errors: list[str] = []
    case_ids: list[str] = []

    for path in case_files:
        try:
            case = load_json(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue

        validation_errors = sorted(validator.iter_errors(case), key=lambda e: list(e.path))
        for err in validation_errors:
            location = ".".join(str(x) for x in err.path) or "<root>"
            errors.append(f"{path.relative_to(ROOT)}:{location}: {err.message}")

        case_id = case.get("id")
        if isinstance(case_id, str):
            case_ids.append(case_id)
            if path.stem != case_id:
                errors.append(
                    f"{path.relative_to(ROOT)}: filename/id mismatch ({path.stem!r} != {case_id!r})"
                )

    duplicates = sorted({case_id for case_id in case_ids if case_ids.count(case_id) > 1})
    if duplicates:
        errors.append(f"Duplicate case IDs: {duplicates}")

    indexed_ids = index.get("cases", [])
    if index.get("case_count") != len(indexed_ids):
        errors.append(
            f"index.json case_count={index.get('case_count')} but contains {len(indexed_ids)} IDs"
        )

    if len(case_files) != len(indexed_ids):
        errors.append(
            f"Found {len(case_files)} case files but index declares {len(indexed_ids)} cases"
        )

    file_id_set = set(case_ids)
    index_id_set = set(indexed_ids)
    if file_id_set != index_id_set:
        missing_from_index = sorted(file_id_set - index_id_set)
        missing_files = sorted(index_id_set - file_id_set)
        if missing_from_index:
            errors.append(f"Case files missing from index: {missing_from_index}")
        if missing_files:
            errors.append(f"Indexed IDs without files: {missing_files}")

    if errors:
        print("ART corpus validation FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"ART corpus validation passed: {len(case_files)} cases, "
        f"{len(set(case_ids))} unique IDs, schema v{index.get('corpus_version')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
