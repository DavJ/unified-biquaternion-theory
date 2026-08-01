#!/usr/bin/env python3
"""Regenerate SHA256SUMS.txt for its declared repository-relative file set."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SUMS = ROOT / "SHA256SUMS.txt"


def _parse_paths(sums_file: Path) -> list[str]:
    paths: list[str] = []
    for lineno, raw in enumerate(sums_file.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(maxsplit=1)
        if len(parts) != 2:
            raise ValueError(f"Malformed line {lineno} in {sums_file}: {raw!r}")
        relative = parts[1].lstrip("*")
        paths.append(relative)
    return paths


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def regenerate(sums_file: Path = DEFAULT_SUMS) -> None:
    paths = _parse_paths(sums_file)
    output: list[str] = []
    for relative in paths:
        candidate = ROOT / relative
        if not candidate.is_file():
            raise FileNotFoundError(f"Cannot hash missing file: {relative}")
        output.append(f"{_sha256(candidate)}  {relative}")
    sums_file.write_text("\n".join(output) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--file",
        type=Path,
        default=DEFAULT_SUMS,
        help="Checksum manifest to regenerate (default: repository SHA256SUMS.txt)",
    )
    args = parser.parse_args()
    regenerate(args.file.resolve())


if __name__ == "__main__":
    main()
