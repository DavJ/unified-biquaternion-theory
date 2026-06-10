#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Guardrail checker for alpha over-claim language in docs, canonical, reports, and root files.

Scans docs/, canonical/, reports/, research_tracks/, and root *.md / *.tex files.
Warns on paragraphs that contain alpha-context overclaim phrases without safe context.
Files with a LEGACY / SUPERSEDED banner are skipped entirely.
ARCHIVE/ and original_release_of_ubt/ are always excluded.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable, List, Tuple

# Phrases that constitute active alpha overclaims when found in an alpha context.
TARGET_PHRASES = [
    "fully derived",
    "derived from first principles",
    "alpha derived",
    "\u03b1 derived",                              # α derived (Unicode Greek alpha)
    "137.036 is derived",
    "137.036 achieved",
    "exact prediction",
    "~90% derived",
    "breakthrough",
    "zero fitted parameters",
    "claim: \u03b1\u207b\u00b9 = 137.036 is derived",  # Claim: α⁻¹ = 137.036 is derived
    "b is derived",
    "b_phenom is derived",
    "gap g137-b is closed",
    "gap g137-b closed",
    "g137-b: closed",
    "mellin insertion proved",
    "z_1real derived",
    "z_{1real} derived",
    "volumetric factor proved",
]

# Safe-context phrases: if one of these appears in the same paragraph, no warning.
SAFE_PHRASES = [
    "not derived",
    "not yet derived",
    "not been derived",
    "not fully derived",
    "no derivation",
    "no first-principles derivation",
    "no active canonical",  # "No active canonical file claims alpha is fully derived"
    "no confirmed",         # "No confirmed hidden fit"
    "conditional",
    "open gap",
    "gap g137-b",
    "superseded",
    "legacy",
    "obsolete",
    "historical",
    "forbidden",            # LAYERS.md: "Forbidden: 'α⁻¹ = 137 is derived from first principles'"
    "probability",          # breakthrough probability — planning language
    "known issue",          # status_legend.md explicitly tagging overclaims
    "remove claim",         # instructions to remove overclaims
    "circular",             # audit reports noting circular reasoning defeats the claim
    "not parameter-free",   # "not a zero-parameter prediction"
    "requires resolution",  # documents noting unresolved gaps
    "imprecise",            # before/after meta-discussion of precise language
    "banned phrase",        # SCIENTIFIC_PRECISION_SUMMARY.md banned phrases section
    "should be labeled",    # ALPHA_STABILITY_SELECTION_RULE.md: "should be labeled 'Hypothesis'"
    "falsifies",            # "What it falsifies: n=137 is uniquely selected..."
    "or fitted",            # "derived from first principles, or fitted to match"
    "fallback",             # future-plan context ("Current fallback: Document")
    "breakthrough mission", # "Alpha Breakthrough Mission" label (not a scientific claim)
    "breakthrough report",  # reference to mission report file
    "graveyard",            # failed_routes_graveyard.md
    "cleanup session",      # files_merged_deleted_redirected.md recommendation
    "near-breakthrough",    # steering memo: "near-breakthrough identification" for SM gauge (not α)
    "transformative if",    # PRIORITIES_2026.md conditional future scenario
    "historic if",          # same conditional
    "if closed",            # "Transformative if closed" (conditional future)
    "if α is derived",      # explicit conditional
    "hypothesis",           # SCIENTIFIC_PRECISION_SUMMARY.md and ALPHA_STABILITY_SELECTION_RULE.md
    "attack plan",          # failed_routes_graveyard.md: references to "ALPHA_BREAKTHROUGH_REPORT.md attack plan"
    "structurally specified",  # precision legend table that also lists 'zero fitted params' as a category level
    "action principle",     # COSMOLOGICAL_ATTRACTOR_SCENARIO.md: "V(ψ) fully derived from action"
    "structural evidence",
    "6 no-go",
    "six routes",
    "time-box expired",
    "g137-b-i",
    "g137-b-ii",
    "g137-b-iii",
    "not derived after",
    "formal no-go",
    "no-go record",
]

SPECIFIC_GAP_OVERCLAIMS = [
    "gap g137-b is closed",
    "gap g137-b closed",
    "g137-b: closed",
    "b_phenom derived",
    "b is derived from s[",
    "b is derived from the ubt",
    "mellin insertion: proved",
    "mellin insertion proved",
    "z_1real = 2eta derived",
    "z_1real=2eta derived",
    "volumetric factor: proved",
    "n_eff^{1/2} proved",
    "n_eff^(1/2) proved",
    "alpha is derived",   # the nuclear option — this should never appear without safe context
]

# Phrases indicating the paragraph concerns alpha/fine-structure.
# A target phrase only triggers a warning when the paragraph also contains
# at least one alpha-context indicator (to avoid false positives on
# electron mass or other "fully derived" uses).
ALPHA_CONTEXT_PHRASES = [
    "alpha",
    "\u03b1",      # Unicode α
    "fine structure",
    "fine-structure",
    "137",
    "coupling constant",
]

# File-level legacy markers: if the first 1 500 characters of a file contain
# one of these strings (case-insensitive), the entire file is skipped.
LEGACY_FILE_MARKERS = [
    "legacy / superseded",
    "superseded document",
    "\u26a0 legacy",        # ⚠ legacy (without variation selector)
    "\u26a0\ufe0f legacy",  # ⚠️ legacy (with variation selector)
    "this document is superseded",
    "legacy banner",
]

# Directories to scan (relative to repo root).
SCAN_DIRS = [
    "docs",
    "canonical",
    "reports",
    "research_tracks",
]

# Root-level glob patterns.
ROOT_GLOBS = ["*.md", "*.tex"]

# Paths / prefix fragments that are always excluded.
EXCLUDE_PREFIXES = ("archive/", "original_release_of_ubt/")


# ---------------------------------------------------------------------------
# File collection
# ---------------------------------------------------------------------------

def iter_candidate_files(repo_root: Path) -> Iterable[Path]:
    seen: set[Path] = set()

    def _add(path: Path) -> None:
        rel = path.relative_to(repo_root).as_posix()
        rel_lower = rel.lower()
        if any(rel_lower.startswith(prefix) for prefix in EXCLUDE_PREFIXES):
            return
        if path.is_file() and path not in seen:
            seen.add(path)

    # Scan each target directory recursively.
    for dir_name in SCAN_DIRS:
        scan_dir = repo_root / dir_name
        if not scan_dir.is_dir():
            continue
        for path in scan_dir.rglob("*.md"):
            _add(path)
        for path in scan_dir.rglob("*.tex"):
            _add(path)

    # Scan root-level files.
    for pattern in ROOT_GLOBS:
        for path in repo_root.glob(pattern):
            _add(path)

    yield from seen


# ---------------------------------------------------------------------------
# Text helpers
# ---------------------------------------------------------------------------

def file_has_legacy_banner(text: str) -> bool:
    """Return True if the file starts with a legacy / superseded banner."""
    header = text[:1500].lower()
    return any(marker in header for marker in LEGACY_FILE_MARKERS)


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


def paragraph_has_alpha_context(text_lower: str) -> bool:
    return any(phrase in text_lower for phrase in ALPHA_CONTEXT_PHRASES)


def _normalise(text_lower: str) -> str:
    """Replace newlines and tabs with a single space for substring matching."""
    return " ".join(text_lower.split())


def paragraph_has_target(text_lower: str) -> bool:
    norm = _normalise(text_lower)
    return any(phrase in norm for phrase in TARGET_PHRASES)


def paragraph_has_safe_context(text_lower: str) -> bool:
    norm = _normalise(text_lower)
    return any(phrase in norm for phrase in SAFE_PHRASES)


# ---------------------------------------------------------------------------
# File scanning
# ---------------------------------------------------------------------------

def scan_file(path: Path, repo_root: Path) -> List[Tuple[int, str]]:
    text = path.read_text(encoding="utf-8", errors="ignore")

    if file_has_legacy_banner(text):
        return []

    warnings: List[Tuple[int, str]] = []
    for line_no, para in paragraphs_with_offsets(text):
        para_l = para.lower()
        stripped = para_l.strip()
        # Skip heading-only paragraphs.
        if stripped.startswith("\\title{") or stripped.startswith("#"):
            continue

        # Only flag target phrases that appear in an alpha context.
        if not paragraph_has_alpha_context(para_l):
            continue
        if not paragraph_has_target(para_l):
            continue
        if paragraph_has_safe_context(para_l):
            continue

        snippet = " ".join(para.strip().split())[:220]
        warnings.append((line_no, snippet))

    return warnings


def scan_file_specific_gaps(path: Path, repo_root: Path) -> List[Tuple[int, str]]:
    text = path.read_text(encoding="utf-8", errors="ignore")

    if file_has_legacy_banner(text):
        return []

    warnings: List[Tuple[int, str]] = []
    for line_no, para in paragraphs_with_offsets(text):
        norm = _normalise(para.lower())
        for phrase in SPECIFIC_GAP_OVERCLAIMS:
            if phrase not in norm:
                continue
            snippet = " ".join(para.strip().split())[:220]
            warnings.append((line_no, f"[{phrase}] {snippet}"))
    return warnings


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def print_status_summary() -> None:
    print("─" * 60)
    print("T3_ALPHA status: STRUCTURAL EVIDENCE (downgraded 2026-06-11)")
    print("Gap G137-B: OPEN — 6 routes NO-GO")
    print("Sub-gaps: G137-B-i (volumetric factor), G137-B-ii (Z_1real derivation), G137-B-iii (N_eff^1/2 prefactor)")
    print("Alpha: NOT DERIVED")
    print("─" * 60)

def main() -> int:
    parser = argparse.ArgumentParser(description="Check alpha over-claim language")
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()

    repo_root = args.root.resolve()
    all_warnings: List[Tuple[str, int, str]] = []

    for file_path in iter_candidate_files(repo_root):
        file_warnings = scan_file(file_path, repo_root)
        for line_no, snippet in file_warnings:
            all_warnings.append((file_path.relative_to(repo_root).as_posix(), line_no, snippet))
        specific_warnings = scan_file_specific_gaps(file_path, repo_root)
        for line_no, snippet in specific_warnings:
            all_warnings.append((file_path.relative_to(repo_root).as_posix(), line_no, snippet))

    all_warnings.sort()

    if not all_warnings:
        print("check_alpha_claims: no active alpha overclaim warnings found")
        print("Gap G137-B remains open.")
        print("No first-principles derivation of alpha was achieved.")
        print_status_summary()
        return 0

    print("check_alpha_claims: ACTIVE ALPHA OVERCLAIM WARNINGS FOUND")
    for rel, line_no, snippet in all_warnings:
        print(f"  {rel}:{line_no}: {snippet}")

    print()
    print("Required safe context: 'not derived' / 'conditional' / 'open gap' / 'Gap G137-B' /")
    print("  'superseded' / 'legacy' / 'obsolete' / 'historical'")
    print("OR add a LEGACY / SUPERSEDED banner to the file to mark it as entirely historical.")
    print_status_summary()
    return 1


if __name__ == "__main__":
    sys.exit(main())
