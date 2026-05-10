#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Guardrail checker for alpha over-claim language across active docs."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable

TARGET_PHRASES = [
    "fully derived",
    "derived from first principles",
    "alpha derived",
    "α derived",
    "137.036 is derived",
    "137.036 achieved",
    "exact prediction",
    "~90% derived",
    "breakthrough",
    "zero fitted parameters",
    "claim: α⁻¹ = 137.036 is derived",
]

SAFE_PHRASES = [
    "not derived",
    "not yet derived",
    "not solved",
    "not achieved",
    "conditional",
    "open gap",
    "gap",
    "gap g137-b",
    "superseded",
    "legacy",
    "obsolete",
    "historical",
    "blocked",
    "requires",
    "hypothesis",
    "semi-empirical",
    "fitted",
    "forbidden",
    "banned",
    "replace",
    "audit",
    "status",
    "roadmap",
    "graveyard",
    "probability",
    "imprecise",
    "falsifies",
    "without circular reasoning",
    "in future",
    "legend",
    "no active canonical file claims",
    "source inventory",
    "companion",
    "recommendation",
    "mission",
    "explicitly labeled",
    "attack plan",
    "smaller-scope paper",
    "theta_w",
    "could contribute",
    "success would",
]

ALPHA_SCOPE_HINTS = [
    "alpha",
    "alpha⁻¹",
    "alpha^-1",
    "alpha^{-1}",
    "fine structure constant",
    "fine-structure",
    "fine structure",
    "137.036",
    "g137-b",
]

SCAN_GLOBS = [
    "docs/**/*.md",
    "docs/**/*.tex",
    "canonical/**/*.md",
    "canonical/**/*.tex",
    "reports/**/*.md",
    "reports/**/*.tex",
    "research_tracks/**/*.md",
    "research_tracks/**/*.tex",
    "*.md",
    "*.tex",
]

EXCLUDE_PREFIXES = (
    "ARCHIVE/",
    "original_release_of_ubt/",
)


def iter_candidate_files(repo_root: Path) -> Iterable[Path]:
    seen: set[Path] = set()
    for pattern in SCAN_GLOBS:
        for path in repo_root.glob(pattern):
            if not path.is_file():
                continue
            rel = path.relative_to(repo_root).as_posix()
            if any(rel.startswith(prefix) for prefix in EXCLUDE_PREFIXES):
                continue
            if path in seen:
                continue
            seen.add(path)
            yield path


def paragraphs_with_offsets(text: str) -> list[tuple[int, str]]:
    paragraphs: list[tuple[int, str]] = []
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


def paragraph_is_alpha_related(text_lower: str, rel_lower: str) -> bool:
    if "alpha" in rel_lower:
        return True
    return any(hint in text_lower for hint in ALPHA_SCOPE_HINTS)


def scan_file(path: Path, repo_root: Path) -> list[tuple[int, str]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    warnings: list[tuple[int, str]] = []
    rel_lower = path.relative_to(repo_root).as_posix().lower()

    for line_no, para in paragraphs_with_offsets(text):
        para_lower = para.lower()
        stripped = para_lower.strip()
        if stripped.startswith("#"):
            continue
        if not paragraph_is_alpha_related(para_lower, rel_lower):
            continue
        if not paragraph_has_target(para_lower):
            continue
        if paragraph_has_safe_context(para_lower):
            continue

        snippet = " ".join(para.strip().split())[:240]
        warnings.append((line_no, snippet))

    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Check alpha over-claim language")
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()

    repo_root = args.root.resolve()
    all_warnings: list[tuple[str, int, str]] = []

    for file_path in iter_candidate_files(repo_root):
        warnings = scan_file(file_path, repo_root)
        rel = file_path.relative_to(repo_root).as_posix()
        for line_no, snippet in warnings:
            all_warnings.append((rel, line_no, snippet))

    if not all_warnings:
        print("check_alpha_claims: no over-claim warnings found")
        return 0

    print("check_alpha_claims: warnings found")
    for rel, line_no, snippet in sorted(all_warnings):
        print(f"- {rel}:{line_no}: {snippet}")

    print(
        "\nRequired context in same paragraph includes: "
        "not derived / conditional / open gap / Gap G137-B / superseded / legacy / obsolete / historical "
        "(non-exhaustive; checker uses an expanded safe-context list)."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
