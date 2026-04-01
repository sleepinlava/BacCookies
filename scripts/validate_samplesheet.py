#!/usr/bin/env python3
"""Validate pipeline samplesheet for required columns and platform-specific fields."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

REQUIRED_COLUMNS = [
    "sample_id",
    "platform",
    "group",
    "fastq_1",
    "fastq_2",
    "long_read",
    "methylation_file",
]

VALID_PLATFORMS = {"illumina", "nanopore", "pacbio"}


def non_empty(value: str | None) -> bool:
    return bool(value and value.strip())


def validate_row(row: dict[str, str], line_no: int) -> list[str]:
    errors: list[str] = []
    platform = (row.get("platform") or "").strip().lower()

    if platform not in VALID_PLATFORMS:
        errors.append(
            f"Line {line_no}: invalid platform '{row.get('platform', '')}'. "
            f"Expected one of {sorted(VALID_PLATFORMS)}"
        )
        return errors

    if not non_empty(row.get("sample_id")):
        errors.append(f"Line {line_no}: sample_id is required")

    if platform == "illumina":
        if not non_empty(row.get("fastq_1")) or not non_empty(row.get("fastq_2")):
            errors.append(
                f"Line {line_no}: illumina requires fastq_1 and fastq_2"
            )
    else:
        if not non_empty(row.get("long_read")):
            errors.append(f"Line {line_no}: {platform} requires long_read")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate samplesheet CSV")
    parser.add_argument("--samplesheet", required=True, help="Path to samplesheet CSV")
    args = parser.parse_args()

    path = Path(args.samplesheet)
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []

        missing_cols = [c for c in REQUIRED_COLUMNS if c not in headers]
        if missing_cols:
            print(
                "ERROR: missing required columns: " + ", ".join(missing_cols),
                file=sys.stderr,
            )
            return 2

        all_errors: list[str] = []
        sample_ids: set[str] = set()

        for index, row in enumerate(reader, start=2):
            all_errors.extend(validate_row(row, index))
            sid = (row.get("sample_id") or "").strip()
            if sid:
                if sid in sample_ids:
                    all_errors.append(f"Line {index}: duplicated sample_id '{sid}'")
                sample_ids.add(sid)

        if all_errors:
            print("Samplesheet validation failed:", file=sys.stderr)
            for err in all_errors:
                print(f"- {err}", file=sys.stderr)
            return 1

    print(f"Samplesheet validation passed: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
