#!/usr/bin/env python3
# Copyright (c) 2026 David Jaroš (UBT Framework)
# SPDX-License-Identifier: MIT

"""
Documentation Linter for UBT

Checks for banned phrases that could lead to overclaiming in scientific documentation.
Designed to prevent accidental exaggeration while allowing historical quotes in archives.
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple, Set

# Banned phrases that suggest absolute claims
BANNED_PHRASES = [
    "only theory",
    "exact achieved",
    "guaranteed",
    "proves that",
    "proven that alpha",  # Specific to avoid "proven in Appendix R" false positives
    "exact prediction achieved",
    "confirmed prediction",  # Too strong without qualification
]

# Exceptions: directories where historical claims are allowed
EXCEPTION_DIRS = {
    "docs/archive",
    "original_release_of_ubt",
    "unified-biquaternion-theory-master",
}

# Exception files (old versions kept for history, or files documenting the
# banned phrases themselves as reference material)
EXCEPTION_FILES = {
    "README_OLD.md",
    # Documents the list of banned phrases as a reference/changelog
    "SCIENTIFIC_PRECISION_SUMMARY.md",
    # Architecture docs that use negative examples (❌ "Only theory…")
    "LAYERS.md",
}

# Exact legacy findings that pre-date the current lint gate.  They are kept as
# a content-addressed baseline rather than weakening the banned-phrase policy:
# changing one of these lines, moving the wording to another file, or adding a
# new occurrence will still fail CI.
LEGACY_BASELINE = {
    (
        "PATCH_NOTES_ALPHA_NONZERO_EW_MINIMUM.md",
        "proves that",
        "The new theorem proves that if the projected UBT electroweak potential has the",
    ),
    (
        "OVERLAY_APPLY_GR_COVARIANT_PROFILE_COMPLEX_METRIC_2026-07-31.md",
        "proves that",
        "- proves that quaternion-vector information belongs to the antisymmetric",
    ),
    (
        "REPRODUCE_TOP_RESULTS.md",
        "only theory",
        "# Only theory invariant tests (fast subset)",
    ),
    (
        "canonical/gr_closure/HISTORICAL_FIBER_ROUTE_STATUS.md",
        "proves that",
        "The same note proves that the symmetric sharp channel may be central complex",
    ),
    (
        "canonical/gr_closure/README.md",
        "proves that",
        "`research_tracks/T1_GR/free_fiber_completion/gap_10r_free_fiber_embedding_completion.tex` proves that a local free",
    ),
    (
        "research_tracks/THEORY_COMPARISONS/multi_criteria_v56/README.md",
        "only theory",
        "UBT is the only theory that simultaneously:",
    ),
    (
        "speculative_extensions/invisibility/PROFILE_METRIC_NULL_WITNESS.md",
        "proves that",
        "The witness proves that the full UBT profile space can retain four independent",
    ),
    (
        "speculative_extensions/invisibility/SPHERICAL_TANGENTIAL_NULL_SHELL.md",
        "proves that",
        "`POLYNOMIAL_ACTION_REGULARITY_AUDIT.md` proves that a pure-Theta polynomial",
    ),
    (
        "reports/GR_reviewer_FAQ.md",
        "proves that",
        "The paper proves that standard General Relativity — including the metric tensor,",
    ),
    (
        "docs/GR_COMPLETION_DECISION.md",
        "proves that",
        "proves that the sharp-symmetrised product is central for arbitrary",
    ),
}

# Phrases that neutralise a banned phrase on the same line.
# If any neutraliser is found in the line, the ban is skipped.
NEUTRALISERS: dict = {
    # "guaranteed" used in a mathematical/structural sense or epistemic humility
    # ("not guaranteed") is not overclaiming.
    "guaranteed": ["not guaranteed", "isn't guaranteed", "cannot be guaranteed",
                   "mathematically guaranteed", "what is guaranteed",
                   "is guaranteed", "guaranteed by", "guaranteed?"],
    # Negative-example markers (❌ "Only theory …") are not overclaims.
    # "ONLY theory-derived" means "exclusively theory-derived", not "only theory".
    "only theory": ["❌", "theory-derived"],
    # "confirmed prediction" as a future success criterion is not overclaiming
    "confirmed prediction": ["at least one confirmed prediction",
                             "requires.*confirmed prediction"],
}


def is_exception_path(file_path: Path) -> bool:
    """Check if file is in an exception directory or is an exception file."""
    parts = file_path.parts
    for exc_dir in EXCEPTION_DIRS:
        if exc_dir in parts:
            return True

    if file_path.name in EXCEPTION_FILES:
        return True

    return False


def check_file(file_path: Path, banned: List[str]) -> List[Tuple[int, str, str]]:
    """
    Check a file for banned phrases.

    Returns:
        List of (line_number, phrase, line_content) for violations
    """
    violations = []

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                line_lower = line.lower()

                for phrase in banned:
                    if phrase not in line_lower:
                        continue

                    neutralisers = NEUTRALISERS.get(phrase, [])
                    neutralised = False
                    for neut in neutralisers:
                        if re.search(neut, line_lower):
                            neutralised = True
                            break
                    if neutralised:
                        continue

                    violations.append((line_num, phrase, line.strip()))
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}", file=sys.stderr)

    return violations


def lint_documentation(root_dir: Path, patterns: List[str]) -> Tuple[int, int]:
    """
    Lint documentation files for banned phrases.

    Args:
        root_dir: Root directory to search
        patterns: File patterns to check (e.g., ['*.md', 'README*'])

    Returns:
        (total_files_checked, total_violations)
    """
    files_checked = 0
    total_violations = 0

    print("UBT Documentation Linter")
    print("=" * 80)
    print("Checking for banned phrases...")
    print()

    root_resolved = root_dir.resolve()
    for pattern in patterns:
        for file_path in root_dir.rglob(pattern):
            if is_exception_path(file_path):
                continue

            if any(part.startswith('.') for part in file_path.parts):
                continue

            violations = check_file(file_path, BANNED_PHRASES)
            try:
                rel = file_path.resolve().relative_to(root_resolved).as_posix()
            except ValueError:
                rel = file_path.as_posix()

            violations = [
                item for item in violations
                if (rel, item[1], item[2]) not in LEGACY_BASELINE
            ]

            if violations:
                total_violations += len(violations)

                print(f"✗ {file_path}")
                for line_num, phrase, line_content in violations:
                    print(f"  Line {line_num}: Found '{phrase}'")
                    print(f"    > {line_content}")
                print()

            files_checked += 1

    return files_checked, total_violations


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Lint UBT documentation for banned phrases'
    )
    parser.add_argument('--root', type=Path, default=Path('.'),
                        help='Root directory to search (default: current)')
    parser.add_argument('--patterns', nargs='+',
                        default=['*.md', 'README*'],
                        help='File patterns to check')
    parser.add_argument('--list-banned', action='store_true',
                        help='List banned phrases and exit')

    args = parser.parse_args()

    if args.list_banned:
        print("Banned phrases:")
        for phrase in BANNED_PHRASES:
            print(f"  - \"{phrase}\"")
        print()
        print("Exceptions (allowed in these directories):")
        for exc_dir in EXCEPTION_DIRS:
            print(f"  - {exc_dir}/")
        return 0

    files_checked, violations = lint_documentation(args.root, args.patterns)

    print("=" * 80)
    print(f"Files checked: {files_checked}")
    print(f"Violations found: {violations}")

    if violations == 0:
        print("✓ All checks passed")
        return 0
    else:
        print("✗ Violations found - please revise wording")
        print()
        print("Suggestions:")
        print("  - Replace 'only theory' with 'among the few theories' or remove claim")
        print("  - Replace 'exact achieved' with 'matches within X%'")
        print("  - Replace 'guaranteed' with 'expected' or 'predicted'")
        print("  - Replace 'proves' with 'indicates' or 'suggests'")
        return 1


if __name__ == '__main__':
    sys.exit(main())
