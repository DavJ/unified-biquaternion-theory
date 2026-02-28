# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
verify_repo_sanity.py
=====================
Regression guards for the UBT canonical-geometry audit closeout.

Checks enforced:
  C1/C2 — No "psychon", "Consciousness coupling", or "consciousness substrate"
           in core/canonical geometry .tex files.
  S1     — No equation using 𝒢_μν (\\mathcal{G}_{\\mu\\nu}) as the *left-hand
           side* of the biquaternionic field equation (i.e. the Einstein-tensor
           role). The correct symbol is ℰ_μν (\\mathcal{E}_{\\mu\\nu}).

Usage::

    python tools/verify_repo_sanity.py          # exits 0 on pass, 1 on failure
    python tools/verify_repo_sanity.py --verbose
"""

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent

# Core geometry files that must not contain consciousness / symbol-collision issues.
# Paths are relative to REPO_ROOT.
CORE_GEOMETRY_FILES = [
    "canonical/geometry/biquaternion_metric.tex",
    "canonical/geometry/biquaternion_curvature.tex",
    "canonical/geometry/biquaternion_connection.tex",
    "canonical/geometry/biquaternion_tetrad.tex",
    "THEORY/architecture/geometry/biquaternion_metric.tex",
    "THEORY/architecture/geometry/biquaternion_curvature.tex",
    "THEORY/architecture/geometry/biquaternion_connection.tex",
    "THEORY/architecture/geometry/biquaternion_tetrad.tex",
]

# Forbidden plain-text patterns (case-insensitive) in core geometry files.
FORBIDDEN_TERMS = [
    "psychon",
    "Consciousness coupling",
    "consciousness substrate",
]

# Pattern that signals a symbol collision: 𝒢_μν used as the LHS of the
# biquaternionic field / Einstein-tensor equation.
# We flag lines where \mathcal{G}_{\mu\nu} (possibly with optional braces /
# spacing) is immediately followed by = and something related to curvature
# (κ, \kappa, \mathcal{R}, \mathcal{T}).
COLLISION_PATTERN = re.compile(
    r"\\mathcal\{G\}_\{\\mu\\nu\}\s*=\s*"
    r"(?:\\kappa|\\mathcal\{[RTE]\})",
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="latin-1")


def check_forbidden_terms(verbose: bool = False) -> list[str]:
    """Return a list of violation strings for forbidden consciousness terms."""
    violations = []
    for rel in CORE_GEOMETRY_FILES:
        path = REPO_ROOT / rel
        if not path.exists():
            continue
        content = _read(path)
        for line_no, line in enumerate(content.splitlines(), 1):
            for term in FORBIDDEN_TERMS:
                if term.lower() in line.lower():
                    msg = f"{rel}:{line_no}: forbidden term {term!r}: {line.strip()}"
                    violations.append(msg)
                    if verbose:
                        print(f"  FAIL  {msg}")
    return violations


def check_symbol_collision(verbose: bool = False) -> list[str]:
    """Return a list of violation strings for 𝒢_μν used as Einstein-tensor LHS."""
    violations = []
    for rel in CORE_GEOMETRY_FILES:
        path = REPO_ROOT / rel
        if not path.exists():
            continue
        content = _read(path)
        for line_no, line in enumerate(content.splitlines(), 1):
            # Skip lines inside comments
            stripped = line.lstrip()
            if stripped.startswith("%"):
                continue
            if COLLISION_PATTERN.search(line):
                msg = (
                    f"{rel}:{line_no}: symbol collision — "
                    r"\\mathcal{G}_{\mu\nu} used as field-equation LHS "
                    f"(should be \\mathcal{{E}}_{{\\mu\\nu}}): {line.strip()}"
                )
                violations.append(msg)
                if verbose:
                    print(f"  FAIL  {msg}")
    return violations


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def run(verbose: bool = False) -> int:
    """Run all checks; return exit code (0 = pass, 1 = fail)."""
    term_violations = check_forbidden_terms(verbose=verbose)
    collision_violations = check_symbol_collision(verbose=verbose)

    all_violations = term_violations + collision_violations
    if all_violations:
        print("verify_repo_sanity: FAILED")
        for v in all_violations:
            print(f"  {v}")
        return 1

    if verbose:
        print("verify_repo_sanity: all checks passed")
    return 0


if __name__ == "__main__":
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    sys.exit(run(verbose=verbose))
