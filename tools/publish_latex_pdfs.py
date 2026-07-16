#!/usr/bin/env python3
"""Publish a curated subset of successfully compiled PDFs.

The all-root LaTeX audit stores outputs under ``build/latex-audit/pdfs`` using
source-relative paths.  This script copies only explicitly mapped publication
artifacts into tracked repository locations. Missing builds are reported and do
not abort the batch.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--build-dir", type=Path, default=Path("build/latex-audit/pdfs"))
    parser.add_argument("--map", dest="map_file", type=Path, default=Path(".github/latex_publish_map.tsv"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = args.repo.resolve()
    build_dir = (repo / args.build_dir).resolve() if not args.build_dir.is_absolute() else args.build_dir
    map_file = (repo / args.map_file).resolve() if not args.map_file.is_absolute() else args.map_file
    if not map_file.is_file():
        print(f"ERROR: publish map not found: {map_file}", file=sys.stderr)
        return 2

    copied = 0
    missing = 0
    for number, raw in enumerate(map_file.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        fields = raw.split("\t")
        if len(fields) != 2:
            print(f"WARNING: {map_file}:{number}: expected SOURCE<TAB>DESTINATION", file=sys.stderr)
            missing += 1
            continue
        source_rel, destination_rel = (field.strip() for field in fields)
        source = build_dir / source_rel
        destination = repo / destination_rel
        if not source.is_file():
            print(f"MISSING: {source_rel}")
            missing += 1
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        print(f"PUBLISHED: {source_rel} -> {destination_rel}")
        copied += 1

    print(f"Published {copied} PDFs; {missing} mapped PDFs were unavailable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
