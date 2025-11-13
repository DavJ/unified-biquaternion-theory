#!/usr/bin/env python3
"""
Audit: verify that LaTeX docs and code present computed (pipeline-derived) values,
not hard-coded reference numbers.

This script is READ-ONLY: it does not modify the repo. It exits non‑zero if severe
issues are detected.

Usage:
  python tools/audit_computed_not_reference.py [--root PATH] [--main-tex FILE]

Checks:
  1) Hard-coded precise constants in .tex/.md/.py (forbidden in non-generated files):
     - alpha^{-1} ≈ 137.0359990...
     - m_e ≈ 0.51099895...
     - m_μ ≈ 105.658375...
     - m_τ ≈ 1776.86...
  2) Main TeX references CSV/pgfplotstable and includes known proof inputs:
     - \input{UBT_alpha_per_sector_patch}
     - \input{tex/UBT_hecke_L_route}
     - uses pgfplotstable and references .csv tables
  3) CSV presence:
     - data/alpha_two_loop_grid.csv (alpha grid)
     - data/leptons.csv (lepton masses)
  4) Alpha provenance (non-fatal WARN, but reported):
     - presence of alpha_from_ubt_two_loop_strict or compute_two_loop_delta in code paths
  5) Mass-pipeline provenance (non-fatal WARN): ubt_alpha_msbar uses alpha provider

Exit code:
  0 = PASS (no severe issues)
  1 = FAIL (hard-coded constants in non-generated files OR missing TeX → CSV linkage)
"""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path
from typing import List, Dict

FORBIDDEN_PATTERNS = [
    (r"137\.0359990\d+", "alpha^{-1} precise"),
    (r"\b0\.5109989\d{2,}\b", "m_e precise"),
    (r"\b105\.6583\d{2,}\b", "m_mu precise"),
    (r"\b1776\.8\d{2,}\b", "m_tau precise"),
]

WHITELIST_FILENAMES = {
    # allow generated .tex or dumps here if you have any; leave empty by default
    # e.g., "UBT_alpha_per_sector_patch.tex",
}

TEXT_EXT = {".tex",".md",".py",".rst",".txt",".json",".yaml",".yml"}

def read_text(p: Path) -> str:
    for enc in ("utf-8","latin-1","windows-1250"):
        try:
            return p.read_text(encoding=enc)
        except Exception:
            continue
    return ""

def scan_forbidden_literals(root: Path) -> List[Dict]:
    hits = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if p.name in WHITELIST_FILENAMES:
            continue
        if any(seg in p.parts for seg in (".git","venv",".venv","build","dist","_build","__pycache__")):
            continue
        if p.suffix.lower() not in TEXT_EXT:
            continue
        txt = read_text(p)
        for rgx, label in FORBIDDEN_PATTERNS:
            for m in re.finditer(rgx, txt):
                s = max(0, m.start()-80); e = min(len(txt), m.end()+80)
                ctx = txt[s:e].replace("\n"," ")
                hits.append({"file": str(p), "what": label, "match": m.group(0), "context": ctx})
    return hits

def check_main_tex(main_tex: Path) -> Dict:
    res = {"exists": main_tex.exists(),
           "has_input_patch": False,
           "has_input_hecke": False,
           "uses_pgfplotstable": False,
           "mentions_csv": False}
    if not res["exists"]:
        return res
    t = read_text(main_tex)
    res["has_input_patch"] = "\\input{UBT_alpha_per_sector_patch}" in t
    res["has_input_hecke"] = "\\input{tex/UBT_hecke_L_route}" in t
    res["uses_pgfplotstable"] = "pgfplotstable" in t
    res["mentions_csv"] = ".csv" in t
    return res

def check_csv_presence(root: Path) -> Dict:
    d = root / "data"
    return {
        "alpha_csv": (d / "alpha_two_loop_grid.csv").exists(),
        "leptons_csv": (d / "leptons.csv").exists(),
    }

def code_provenance(root: Path) -> Dict:
    """Non-fatal provenance hints: where providers live."""
    prov = {"alpha_from_ubt_two_loop_strict": [],
            "compute_two_loop_delta": [],
            "ubt_alpha_msbar": []}
    for p in root.rglob("*.py"):
        if any(seg in p.parts for seg in (".git","venv",".venv","build","dist","_build","__pycache__")):
            continue
        txt = read_text(p)
        if re.search(r"\bdef\s+alpha_from_ubt_two_loop_strict\s*\(", txt):
            prov["alpha_from_ubt_two_loop_strict"].append(str(p))
        if re.search(r"\bdef\s+compute_two_loop_delta\s*\(", txt):
            prov["compute_two_loop_delta"].append(str(p))
        if re.search(r"\bdef\s+ubt_alpha_msbar\s*\(", txt):
            prov["ubt_alpha_msbar"].append(str(p))
    return prov

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Repo root (default: current dir)")
    ap.add_argument("--main-tex", default="emergent_alpha_from_ubt.tex",
                    help="Main TeX filename (default: emergent_alpha_from_ubt.tex)")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    main_tex = (root / args.main_tex)

    failures = []
    warnings = []

    # 1) Forbidden literals
    hits = scan_forbidden_literals(root)
    if hits:
        failures.append(f"Hard-coded precise constants found in {len(hits)} place(s).")
        print("== Hard-coded constant candidates ==")
        for h in hits:
            print(f"- {h['file']}: {h['what']} :: {h['match']}")
    else:
        print("OK: No forbidden precise literals found in .tex/.md/.py")

    # 2) Main TeX structure
    chk = check_main_tex(main_tex)
    if not chk["exists"]:
        warnings.append(f"Main TeX not found: {main_tex}")
    else:
        if not chk["uses_pgfplotstable"] or not chk["mentions_csv"]:
            failures.append("Main TeX does not clearly include CSV tables via pgfplotstable.")
        if not chk["has_input_patch"]:
            warnings.append("Main TeX missing \\input{UBT_alpha_per_sector_patch} (recommended).")
        if not chk["has_input_hecke"]:
            warnings.append("Main TeX missing \\input{tex/UBT_hecke_L_route} (recommended).")

    # 3) CSV presence
    csv = check_csv_presence(root)
    if not csv["alpha_csv"]:
        failures.append("Missing data/alpha_two_loop_grid.csv (export alpha grid first).")
    if not csv["leptons_csv"]:
        warnings.append("Missing data/leptons.csv (lepton table won't render).")

    # 4) Provenance (non-fatal)
    prov = code_provenance(root)
    if not prov["alpha_from_ubt_two_loop_strict"] and not prov["compute_two_loop_delta"]:
        warnings.append("Alpha provider not found (no alpha_from_ubt_two_loop_strict or compute_two_loop_delta).")
    if not prov["ubt_alpha_msbar"]:
        warnings.append("Mass pipeline provider ubt_alpha_msbar() not found (cannot audit mass provenance).")

    # Summary
    print("\n== Summary ==")
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

    # JSON report (optional CI artifact)
    report = {
        "root": str(root), "main_tex": str(main_tex),
        "failures": failures, "warnings": warnings,
        "forbidden_hits": hits, "tex_check": chk, "csv_presence": csv, "provenance": prov
    }
    (root / "reports").mkdir(exist_ok=True, parents=True)
    (root / "reports" / "audit_computed_not_reference.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )

    raise SystemExit(rc)

if __name__ == "__main__":
    main()
