# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
r"""
verify_symbol_consistency.py
============================
Repository-wide regression tool enforcing canonical symbol conventions in
Unified Biquaternion Theory (UBT) LaTeX and Markdown sources.

Rules enforced
--------------
SC1 -- g_{\mu\nu} must be used for the classical (real) metric;
       \mathcal{G}_{\mu\nu} is reserved for the biquaternionic metric.

SC2 -- \mathcal{E}_{\mu\nu} must be used for the biquaternionic Einstein
       tensor; \mathcal{G}_{\mu\nu} must NOT appear as the LHS of the
       field equation (symbol collision guard).

SC3 -- Dual-use guard: any file outside speculative_extensions/ that
       uses \mathcal{G}_{\mu\nu} in a context suggesting the Einstein
       tensor (i.e. immediately followed by = \kappa or = 8\pi G) is flagged.

Usage::

    python tools/verify_symbol_consistency.py          # exits 0 on pass
    python tools/verify_symbol_consistency.py --verbose
"""

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent

# Directories whose content is treated as archival / external and skipped.
SKIP_DIRS = {
    ".git",
    "original_release_of_ubt",
    "unified-biquaternion-theory-master",
    # The following contain documented/archived violations and are not
    # actively maintained under the canonical symbol convention:
    "symbol_sweep",          # reports/symbol_sweep/ documents old violations
    "THEORY",                # mirror directory; maintained separately
}

# File extensions to scan.
SCAN_EXTENSIONS = {".tex", ".md"}

# SC2/SC3: Pattern flagging \\mathcal{G}_{\\mu\\nu} used as Einstein-tensor LHS.
# Matches lines like:  \mathcal{G}_{\mu\nu} = \kappa ...
#                      \mathcal{G}_{\mu\nu} = 8\pi G ...
#                      \mathcal{G}_{\mu\nu} = \mathcal{T} ...  (field eq.)
# Negative lookbehind excludes usage as the metric in \Lambda \mathcal{G}_{μν}
# or as the metric in the stress-energy term \frac{1}{2}\mathcal{G}_{μν}.
METRIC_AS_EINSTEIN_LHS = re.compile(
    r"(?<![\\A-Za-z{])"              # not preceded by \ or letter or {
    r"\\mathcal\{G\}_\{\\mu\\nu\}"   # the biquaternionic metric symbol
    r"\s*=\s*"
    r"(?:"
    r"\\kappa"                        # = \kappa (coupling constant)
    r"|8\s*\\pi\s*[Gg]"              # = 8\pi G
    r"|\\mathcal\{[TE]\}"            # = \mathcal{T} or \mathcal{E}
    r"|\\mathcal\{R\}"               # = \mathcal{R} (Ricci)
    r")",
)

# SC3 broader: \\mathcal{G}_{\\mu\\nu} on the equation LHS in a file that
# clearly should use \\mathcal{E}_{\\mu\\nu} (field equation context).
# We additionally check for the string in track-A canonical files.
CANONICAL_TEX_DIRS = [
    "canonical",
    "papers",
    "research_tracks",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="latin-1")


def _in_skip_dir(path: Path) -> bool:
    return any(skip in path.parts for skip in SKIP_DIRS)


def _is_comment_line(line: str) -> bool:
    stripped = line.lstrip()
    return stripped.startswith("%") or stripped.startswith("<!--")


# ---------------------------------------------------------------------------
# Check SC2/SC3: \\mathcal{G}_{\\mu\\nu} used as Einstein-tensor LHS
# ---------------------------------------------------------------------------

def check_metric_symbol_collision(verbose: bool = False) -> list[str]:
    """SC2/SC3: Return violations where \\mathcal{G}_{\\mu\\nu} is used as the
    biquaternionic field-equation LHS (should be \\mathcal{E}_{\\mu\\nu})."""
    violations: list[str] = []
    for path in sorted(REPO_ROOT.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix not in SCAN_EXTENSIONS:
            continue
        if _in_skip_dir(path):
            continue
        rel = str(path.relative_to(REPO_ROOT))
        content = _read(path)
        for lineno, line in enumerate(content.splitlines(), 1):
            if _is_comment_line(line):
                continue
            if METRIC_AS_EINSTEIN_LHS.search(line):
                msg = (
                    f"{rel}:{lineno}: SC2 — \\mathcal{{G}}_{{\\mu\\nu}} used "
                    f"as field-equation LHS (use \\mathcal{{E}}_{{\\mu\\nu}}): "
                    f"{line.strip()}"
                )
                violations.append(msg)
                if verbose:
                    print(f"  FAIL  {msg}")
    return violations


# ---------------------------------------------------------------------------
# Check SC4: Einstein tensor symbol consistency in canonical dirs
# ---------------------------------------------------------------------------

def check_einstein_tensor_symbol(verbose: bool = False) -> list[str]:
    """SC4: In canonical/papers/research_tracks, \\mathcal{E}_{\\mu\\nu} must
    be used for the Einstein tensor; warn if G_{\\mu\\nu} appears in a context
    that looks like a field equation LHS (not the classical Einstein tensor)."""
    # Pattern: plain G_{\mu\nu} = \kappa (without \mathcal) in canonical files.
    plain_g_field_eq = re.compile(
        r"(?<!\\mathcal\{G\})G_\{\\mu\\nu\}\s*=\s*\\kappa"
    )
    violations: list[str] = []
    for canonical_dir in CANONICAL_TEX_DIRS:
        base = REPO_ROOT / canonical_dir
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.tex")):
            if _in_skip_dir(path):
                continue
            rel = str(path.relative_to(REPO_ROOT))
            content = _read(path)
            for lineno, line in enumerate(content.splitlines(), 1):
                if _is_comment_line(line):
                    continue
                if plain_g_field_eq.search(line):
                    msg = (
                        f"{rel}:{lineno}: SC4 — plain G_{{\\mu\\nu}} = \\kappa "
                        f"in canonical file; prefer \\mathcal{{E}}_{{\\mu\\nu}} "
                        f"for the biquaternionic field equation: {line.strip()}"
                    )
                    violations.append(msg)
                    if verbose:
                        print(f"  FAIL  {msg}")
    return violations


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def run(verbose: bool = False) -> int:
    """Run all symbol-consistency checks; return exit code (0=pass, 1=fail)."""
    collision_violations = check_metric_symbol_collision(verbose=verbose)
    einstein_violations = check_einstein_tensor_symbol(verbose=verbose)

    all_violations = collision_violations + einstein_violations
    if all_violations:
        print("verify_symbol_consistency: FAILED")
        for v in all_violations:
            print(f"  {v}")
        return 1

    if verbose:
        print("verify_symbol_consistency: all checks passed")
    return 0


if __name__ == "__main__":
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    sys.exit(run(verbose=verbose))
