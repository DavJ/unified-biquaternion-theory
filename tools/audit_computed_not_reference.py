#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
Audit: verify that source files present computed (pipeline-derived) values,
not hard-coded reference numbers.

Distinguishes FATAL vs WARN hits:
  FATAL: Hard-coded precise constants in new core .tex/.py files that are not
         in known archived, legacy, or documentation directories.
  WARN:  Precise constants in documentation, reports, tools, tests, or
         legacy/archived directories.

Usage:
  python tools/audit_computed_not_reference.py --root . [--main-tex emergent_alpha_from_ubt.tex]

Outputs a JSON report to reports/audit_computed_not_reference.json.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List

FORBIDDEN_PATTERNS = [
    (r"137\.0359990\d+", "alpha^{-1} precise"),
    (r"\b0\.5109989\d{2,}\b", "m_e precise"),
    (r"\b105\.6583\d{2,}\b", "m_mu precise"),
    (r"\b1776\.8\d{2,}\b", "m_tau precise"),
]

TEXT_EXT = {".tex", ".md", ".py", ".rst", ".txt", ".json", ".yaml", ".yml"}

# Directories to skip entirely (do not even recurse into them)
IGNORE_DIRS = {
    ".git", "venv", ".venv", "build", "dist", "_build", "__pycache__",
    ".pytest_cache",
    # Legacy / subpackage directories (large, contain many reference values)
    "ubt_with_chronofactor", "ubt_no_chronofactor",
    "ubt_audit_pack_v1", "ubt_audit_pack_v2",
    # Original research documents (historical record)
    "unified_biquaternion_theory",
    # Data directory
    "data", "out",
    # Old / archived versions
    "old", "archived", "archive",
    "osf_release", "osf_release_not_released",
    "ubt_strict_fix", "ubt_strict_minimal",
    # Reports directory (generated outputs — may contain any constant values)
    "reports",
}

# Directories whose contents are always WARN (never FATAL) but are scanned
SOFT_DIRS = {
    "reports", "tools", "tests", "scripts", "validation", "docs",
    "DOCS", "FINGERPRINTS",
}

# Individual filenames always treated as WARN (never FATAL)
SOFT_FILES = {
    "validate_alpha_renormalization.py",
    "generate_reference_constants.py",
    "reproduce_lepton_ratios.py",
    "verify_N_eff.py",  # Verification script that legitimately references experimental α⁻¹
    "STATUS_ALPHA.md",
    "STATUS_FERMIONS.md",
    "STATUS_THEORY_ASSESSMENT.md",
}


def classify_file(p: Path) -> str:
    """Return 'ignore', 'warn', or 'fatal' for the given path."""
    parts = set(p.parts)
    # Always skip non-text files
    if p.suffix.lower() not in TEXT_EXT:
        return "ignore"
    # Skip files in ignored directories
    if parts & IGNORE_DIRS:
        return "ignore"
    # Skip if any path segment is a soft directory → WARN
    if parts & SOFT_DIRS:
        return "warn"
    # Skip individual soft files
    if p.name in SOFT_FILES:
        return "warn"
    # Markdown files are always warnings
    if p.suffix.lower() == ".md":
        return "warn"
    # Core .tex and .py files → FATAL
    if p.suffix.lower() in (".tex", ".py"):
        return "fatal"
    return "warn"


def read_text(p: Path) -> str:
    for enc in ("utf-8", "latin-1", "windows-1250"):
        try:
            return p.read_text(encoding=enc)
        except (UnicodeDecodeError, OSError):
            continue
    return ""


def scan_forbidden_literals(root: Path) -> Dict[str, List[Dict]]:
    hits: Dict[str, List[Dict]] = {"fatal": [], "warn": []}

    def _walk(directory: Path) -> None:
        try:
            entries = list(directory.iterdir())
        except PermissionError:
            return
        for p in entries:
            if p.is_symlink():
                continue
            if p.is_dir():
                # Prune ignored directories early
                if p.name in IGNORE_DIRS:
                    continue
                _walk(p)
            elif p.is_file():
                if p.suffix.lower() not in TEXT_EXT:
                    continue
                parts = set(p.parts)
                if parts & IGNORE_DIRS:
                    continue
                klass = classify_file(p)
                if klass == "ignore":
                    continue
                txt = read_text(p)
                for rgx, label in FORBIDDEN_PATTERNS:
                    for m in re.finditer(rgx, txt):
                        s = max(0, m.start() - 80)
                        e = min(len(txt), m.end() + 80)
                        ctx = txt[s:e].replace("\n", " ")
                        hits[klass].append({
                            "file": str(p.relative_to(root)),
                            "what": label,
                            "match": m.group(0),
                            "context": ctx,
                        })

    _walk(root)
    return hits


def check_csv_presence(root: Path) -> Dict:
    d = root / "data"
    return {
        "alpha_csv": (d / "alpha_two_loop_grid.csv").exists(),
        "leptons_csv": (d / "leptons.csv").exists(),
    }


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Audit source files for hard-coded physical constants."
    )
    ap.add_argument("--root", default=".", help="Repository root (default: .)")
    ap.add_argument(
        "--main-tex", default="emergent_alpha_from_ubt.tex",
        help="Main TeX filename to check for CSV linkage."
    )
    args = ap.parse_args()

    root = Path(args.root).resolve()

    failures: List[str] = []
    warnings: List[str] = []

    # Scan for literal constants
    hits = scan_forbidden_literals(root)
    if hits["fatal"]:
        failures.append(
            f"Hard-coded precise constants found in {len(hits['fatal'])} FATAL file(s)."
        )
    if hits["warn"]:
        warnings.append(
            f"Precise constants found in {len(hits['warn'])} non-core (WARN) file(s)."
        )

    # Check CSV presence (warn only — CSV may be generated separately)
    csv = check_csv_presence(root)
    if not csv["alpha_csv"]:
        warnings.append("Missing data/alpha_two_loop_grid.csv (run alpha grid export first).")
    if not csv["leptons_csv"]:
        warnings.append("Missing data/leptons.csv (lepton table may not render).")

    # Print summary
    print("== Summary ==")
    if failures:
        print("FAIL")
        for f in failures:
            print(" -", f)
        rc = 1
    else:
        print("PASS")
        rc = 0

    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(" -", w)

    # Write JSON report (limit warn hits to avoid huge files)
    MAX_WARN_HITS = 100
    report = {
        "root": str(root),
        "failures": failures,
        "warnings": warnings,
        "fatal_hits": hits["fatal"],
        "warn_hits_count": len(hits["warn"]),
        "warn_hits_sample": hits["warn"][:MAX_WARN_HITS],
        "csv_presence": csv,
    }
    (root / "reports").mkdir(exist_ok=True, parents=True)
    (root / "reports" / "audit_computed_not_reference.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )

    raise SystemExit(rc)


if __name__ == "__main__":
    main()
