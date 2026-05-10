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
    "alpha derivation",
    "derivation of alpha",
    "alpha route closed",
    "fine-structure route closed",
    "breakthrough",
    "b_best",
]

SAFE_PHRASES = [
    "historical",
    "legacy",
    "obsolete",
    "superseded",
    "conditional",
    "open gap",
    "open",
    "gap g137-b",
    "not derived",
    "not yet derived",
    "not achieved",
    "failed",
    "rejected",
    "no-go",
]

SAFE_137036_CONTEXT = [
    "not derived",
    "open",
    "conditional",
    "gap g137-b",
    "historical",
    "obsolete",
    "superseded",
    "legacy",
    "failed",
    "rejected",
    "no-go",
    "not achieved",
    "no expression",
]

FILE_GLOBS = [
    "canonical/alpha/ALPHA_MASTER_STATUS.md",
    "canonical/alpha/alpha_best_route.tex",
    "canonical/alpha/alpha_equation_matrix.tex",
]
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


def is_active_alpha_canonical(path: Path, repo_root: Path, text_lower: str) -> bool:
    rel = path.relative_to(repo_root).as_posix().lower()
    if not rel.startswith("canonical/alpha/"):
        return False
    if any(marker in rel for marker in ("legacy", "superseded", "archive")):
        return False
    if any(marker in text_lower for marker in ("legacy derivation-attempt banner", "legacy / superseded banner")):
        return False
    return True


def scan_file(path: Path, repo_root: Path) -> List[Tuple[int, str]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    text_lower = text.lower()
    warnings: List[Tuple[int, str]] = []
    active_alpha_file = is_active_alpha_canonical(path, repo_root, text_lower)
    if not active_alpha_file:
        return warnings
    for line_no, para in paragraphs_with_offsets(text):
        para_l = para.lower()
        stripped = para_l.strip()
        if stripped.startswith("\\title{") or stripped.startswith("#"):
            continue
        snippet = " ".join(para.strip().split())[:220]

        if paragraph_has_target(para_l) and not paragraph_has_safe_context(para_l):
            warnings.append((line_no, snippet))

        if "g3-k" in para_l and active_alpha_file and not paragraph_has_safe_context(para_l):
            warnings.append((line_no, f"G3-k in active canonical alpha file without safe context: {snippet}"))

        if "137.036" in para_l and not any(ctx in para_l for ctx in SAFE_137036_CONTEXT):
            warnings.append((line_no, f"137.036 without safe context: {snippet}"))
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Check alpha over-claim language")
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()

    repo_root = args.root.resolve()
    all_warnings = []

    for file_path in iter_candidate_files(repo_root):
        warnings = scan_file(file_path, repo_root)
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
