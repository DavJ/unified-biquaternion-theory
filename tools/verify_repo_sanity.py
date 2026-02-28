#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
UBT Repository Sanity Guard
============================

Scans core-facing LaTeX files for symbol collisions and notation errors.

Enforced rules
--------------
1. SYMBOL RULE: \\mathcal{G}_{\\mu\\nu} denotes ONLY the biquaternionic metric.
   \\mathcal{E}_{\\mu\\nu} denotes the biquaternionic Einstein tensor.
   Any line using \\mathcal{G}_{\\mu\\nu} as an Einstein-tensor (LHS of field equation,
   Einstein tensor definition, or labelled as "Einstein tensor") is a collision.

Usage
-----
    python tools/verify_repo_sanity.py [--verbose] [--fix-dry-run]

Exit codes
----------
    0  — no violations found
    1  — violations found (printed to stdout)
"""

import argparse
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Repository root detection
# ---------------------------------------------------------------------------

def _find_repo_root() -> Path:
    """Walk up from this file until we find the repo root (has pytest.ini)."""
    current = Path(__file__).resolve().parent
    while current != current.parent:
        if (current / "pytest.ini").exists():
            return current
        current = current.parent
    # Fallback: assume script is in tools/ subdirectory of root
    return Path(__file__).resolve().parent.parent


REPO_ROOT = _find_repo_root()


# ---------------------------------------------------------------------------
# Guarded file set
# Core-facing files where symbol collisions must not exist.
# These globs are evaluated relative to REPO_ROOT.
# ---------------------------------------------------------------------------

GUARDED_GLOBS = [
    # Canonical geometry
    "canonical/geometry/*.tex",
    # Canonical main document
    "canonical/UBT_canonical_main.tex",
    # Root-level theory documents
    "UBT_Main.tex",
    "THEORY_STATUS_DISCLAIMER.tex",
    # Consolidation appendices (core theory, not speculative)
    "consolidation_project/appendix_R_GR_equivalence.tex",
    "consolidation_project/appendix_FORMAL_emergent_metric.tex",
    "consolidation_project/appendix_A_biquaternion_gravity_consolidated.tex",
    "consolidation_project/appendix_B0_metric_rigor.tex",
]


def _expand_guarded_files() -> list[Path]:
    """Expand globs and return sorted list of existing paths."""
    files = []
    for pattern in GUARDED_GLOBS:
        matches = sorted(REPO_ROOT.glob(pattern))
        files.extend(matches)
    # Deduplicate while preserving order
    seen = set()
    result = []
    for f in files:
        if f not in seen:
            seen.add(f)
            result.append(f)
    return sorted(result)


# ---------------------------------------------------------------------------
# Collision patterns: \\mathcal{G}_{\\mu\\nu} used as Einstein tensor
# ---------------------------------------------------------------------------

# Pattern helpers — raw strings with no escaping issues
_G_MN = r"\\mathcal\{G\}_\{\\mu\\nu\}"   # \mathcal{G}_{\mu\nu}
_E_OK = r"\\mathcal\{E\}_\{\\mu\\nu\}"   # \mathcal{E}_{\mu\nu} (correct)

# P1: field equation LHS  — \mathcal{G}_{\mu\nu} = \kappa or = 8\pi
_P1_FIELD_EQ = re.compile(
    _G_MN + r"\s*=\s*(\\kappa|8\\pi|\\mathcal\{R\})"
)
# P2: Einstein tensor definition
#     \mathcal{G}_{\mu\nu} = \mathcal{R}_{\mu\nu} - ...
_P2_EINSTEIN_DEF = re.compile(
    _G_MN + r"\s*=\s*\\mathcal\{R\}_\{\\mu\\nu\}"
)
# P3: Prose labelling — "Einstein tensor \mathcal{G}" or "biquaternionic Einstein tensor" + \mathcal{G}
_P3_PROSE = re.compile(
    r"(Einstein\s+tensor|biquaternionic\s+Einstein\s+tensor)"
    r".*" + _G_MN,
    re.IGNORECASE,
)
_P3_PROSE_REV = re.compile(
    _G_MN + r".*"
    r"(is\s+the\s+biquaternionic\s+Einstein\s+tensor|is\s+the\s+Einstein\s+tensor)",
    re.IGNORECASE,
)
# P4: Real projection of Einstein tensor — G_{\mu\nu} = Re(\mathcal{G}_{\mu\nu})
#     (capital G followed by Re of \mathcal{G}) or Re(\mathcal{G}) = \kappa
_P4_RE_PROJECTION = re.compile(
    r"G_\{\\mu\\nu\}\s*(=|:=).*"
    r"(\\Re|\\text\{Re\}|\\mathrm\{Re\})\s*\\?\(?\s*" + _G_MN
)
_P4_RE_FIELD_EQ = re.compile(
    r"(\\Re|\\text\{Re\}|\\mathrm\{Re\})\s*\\?\(?\s*" + _G_MN
    + r"\s*\\?\)?\s*(&\s*=|=)\s*(\\Re|\\kappa|\\text\{Re\})"
)

# Combined: any pattern that fires on a line means collision
COLLISION_PATTERNS: list[tuple[str, re.Pattern]] = [
    ("P1-field-equation",      _P1_FIELD_EQ),
    ("P2-einstein-def",        _P2_EINSTEIN_DEF),
    ("P3-prose-label",         _P3_PROSE),
    ("P3-prose-label-rev",     _P3_PROSE_REV),
    ("P4-Re-projection-G",     _P4_RE_PROJECTION),
    ("P4-Re-field-eq",         _P4_RE_FIELD_EQ),
]

# Lines that must NOT be flagged (metric uses — whitelist by substring)
# If a line matches any of these, it is exempt from P1/P2/P3/P4 above.
METRIC_USE_EXEMPTIONS = [
    # Real metric definition g (lowercase) = Re(\mathcal{G})
    r"g_\{\\mu\\nu\}",           # g_{\mu\nu} := Re(\mathcal{G})
    r"\\text\{Re\}.*g_",         # Re(...) -> g_
    # Metric definition via tetrads
    r"\\text\{Sc\}\(E_",
    r"\\mathrm\{Sc\}",
    # Imaginary part of metric (dark sector)
    r"\\text\{Im\}.*\\mathcal\{G\}|\\Im.*\\mathcal\{G\}",
    # RHS metric × Ricci scalar term (not an Einstein tensor use)
    r"\\frac\{1\}\{2\}\s*\\mathcal\{G\}_\{\\mu\\nu\}\s*\\mathcal\{R\}",
    # Metric in stress-energy (half-trace term)
    r"\\mathcal\{G\}_\{\\mu\\nu\}\\langle",
    r"\\frac\{1\}\{2\}\s*\\mathcal\{G\}_\{\\mu\\nu\}\s*\\langle",
    # Pressure term: \mathcal{P}\mathcal{G}
    r"\\mathcal\{P\}.*\\mathcal\{G\}_\{\\mu\\nu\}",
    # EM tensor: \mathcal{G}_{\mu\nu}\mathcal{F}
    r"\\mathcal\{G\}_\{\\mu\\nu\}\\mathcal\{F\}",
    # Inverse metric \mathcal{G}^
    r"\\mathcal\{G\}\^",
    # Metric → g limit in summary (Biquaternionic metric \mathcal{G} \to g)
    r"Biquaternionic metric.*\\mathcal\{G\}.*\\to",
    # determinant
    r"\\det\\mathcal\{G\}|\\det\s*\\mathcal\{G\}",
    # action integral
    r"S_\\Theta\s*=.*\\mathcal\{G\}",
    # Cosmological constant term: \Lambda \mathcal{G}_{\mu\nu} is a metric (not Einstein)
    r"\\Lambda\s*\\mathcal\{G\}_\{\\mu\\nu\}",
    # Already-fixed lines containing \mathcal{E} (Einstein) alongside metric \mathcal{G}
    r"\\mathcal\{E\}_\{\\mu\\nu\}.*\\mathcal\{G\}_\{\\mu\\nu\}",
]

_EXEMPTION_PATTERNS = [re.compile(p) for p in METRIC_USE_EXEMPTIONS]


def _is_exempt(line: str) -> bool:
    """Return True if line should be skipped (metric use, not Einstein-tensor use)."""
    for pat in _EXEMPTION_PATTERNS:
        if pat.search(line):
            return True
    return False


# ---------------------------------------------------------------------------
# Main scanner
# ---------------------------------------------------------------------------

class Violation:
    def __init__(self, path: Path, lineno: int, line: str, pattern_id: str):
        self.path = path
        self.lineno = lineno
        self.line = line.rstrip()
        self.pattern_id = pattern_id

    def __str__(self):
        rel = self.path.relative_to(REPO_ROOT)
        snippet = self.line[:120] + ("..." if len(self.line) > 120 else "")
        return f"  {rel}:{self.lineno} [{self.pattern_id}]\n    {snippet}"


def scan_file(path: Path) -> list[Violation]:
    """Scan a single file for symbol collisions."""
    violations = []
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return violations

    for lineno, line in enumerate(lines, start=1):
        if _is_exempt(line):
            continue
        for pattern_id, pattern in COLLISION_PATTERNS:
            if pattern.search(line):
                violations.append(Violation(path, lineno, line, pattern_id))
                break  # one violation per line is enough
    return violations


def scan_all(verbose: bool = False) -> list[Violation]:
    """Scan all guarded files and return all violations."""
    guarded = _expand_guarded_files()
    all_violations = []

    if verbose:
        print(f"[verify_repo_sanity] Scanning {len(guarded)} guarded files...")
        for f in guarded:
            print(f"  {f.relative_to(REPO_ROOT)}")
        print()

    for path in guarded:
        file_violations = scan_file(path)
        if verbose and file_violations:
            print(f"  VIOLATIONS in {path.relative_to(REPO_ROOT)}:")
            for v in file_violations:
                print(f"    line {v.lineno} [{v.pattern_id}]: {v.line[:100]}")
        all_violations.extend(file_violations)

    return all_violations


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="UBT repo sanity guard: detect \\mathcal{G} Einstein-tensor collisions.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Print each scanned file and all violation details"
    )
    args = parser.parse_args()

    violations = scan_all(verbose=args.verbose)

    if violations:
        print(f"\n{'='*65}")
        print(f"verify_repo_sanity: {len(violations)} VIOLATION(S) FOUND")
        print(f"{'='*65}")
        print()
        print("\\mathcal{G}_{\\mu\\nu} must denote ONLY the biquaternionic metric.")
        print("Use \\mathcal{E}_{\\mu\\nu} for the biquaternionic Einstein tensor.")
        print()
        for v in violations:
            print(str(v))
        print()
        print(f"Total: {len(violations)} violation(s) in "
              f"{len({v.path for v in violations})} file(s).")
        print("Fix: replace \\mathcal{G}_{\\mu\\nu} with \\mathcal{E}_{\\mu\\nu}"
              " in Einstein-tensor contexts.")
        print("See: reports/symbol_sweep/collision_hits.md")
        return 1

    if args.verbose:
        print(f"verify_repo_sanity: OK — 0 violations in {len(_expand_guarded_files())} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
