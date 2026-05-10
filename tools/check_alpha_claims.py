#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Guardrail checker for alpha over-claim language in canonical and root docs."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable, List, Tuple

TARGET_PHRASES = [
    "alpha is derived",
    "fine structure constant is derived",
    "137.036 from first principles",
]

SAFE_PHRASES = [
    "conditional",
    "open gap",
    "gap g137-b",
    "not yet derived",
]

FILE_GLOBS = ["canonical/**/*.md", "canonical/**/*.tex", "*.md", "*.tex"]
EXCLUDE_PREFIXES = ("ARCHIVE/", "original_release_of_ubt/")


def iter_candidate_files(repo_root: Path) -> Iterable[Path]:
    seen = set()
    for pattern in FILE_GLOBS:
        for path in repo_root.glob(pattern):
            rel = path.relative_to(repo_root).as_posix()
            if any(rel.startswith(prefix) for prefix in EXCLUDE_PREFIXES):
                continue
            if path.is_file() and path not in seen:
                seen.add(path)
                yield path


def paragraphs_with_offsets(text: str) -> List[Tuple[int, str]]:
    paragraphs: List[Tuple[int, str]] = []
    blocks = re.split(r"\n\s*\n", text)
    cursor = 0
    for block in blocks:
        idx = text.find(block, cursor)
        if idx < 0:
            continue
        line = text.count("\n", 0, idx) + 1
        paragraphs.append((line, block))
        cursor = idx + len(block)
    return paragraphs


def paragraph_has_target(text_lower: str) -> bool:
    return any(phrase in text_lower for phrase in TARGET_PHRASES)


def paragraph_has_safe_context(text_lower: str) -> bool:
    return any(phrase in text_lower for phrase in SAFE_PHRASES)


def scan_file(path: Path) -> List[Tuple[int, str]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    warnings: List[Tuple[int, str]] = []
    for line_no, para in paragraphs_with_offsets(text):
        para_l = para.lower()
        if paragraph_has_target(para_l) and not paragraph_has_safe_context(para_l):
            snippet = " ".join(para.strip().split())
            warnings.append((line_no, snippet[:220]))
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Check alpha over-claim language")
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()

    repo_root = args.root.resolve()
    all_warnings = []

    for file_path in iter_candidate_files(repo_root):
        warnings = scan_file(file_path)
        for line_no, snippet in warnings:
            all_warnings.append((file_path.relative_to(repo_root).as_posix(), line_no, snippet))

    if not all_warnings:
        print("check_alpha_claims: no over-claim warnings found")
        return 0

    print("check_alpha_claims: warnings found")
    for rel, line_no, snippet in all_warnings:
        print(f"- {rel}:{line_no}: {snippet}")

    print("\nRequired context for such claims: conditional / open gap / Gap G137-B / not yet derived")
    return 1


if __name__ == "__main__":
    sys.exit(main())
