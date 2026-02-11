#!/usr/bin/env python3
"""
Audit v2: verify that LaTeX/docs present computed (pipeline-derived) values,
not hard-coded reference numbers. Distinguishes FATAL vs WARN hits and fixes
previous script's missing `json` import.

Usage:
  python tools/audit_computed_not_reference.py --root . [--main-tex emergent_alpha_from_ubt.tex]

FATAL categories (cause non-zero exit):
  - Hard-coded precise constants in core .tex (outside known generated snippets)
  - Hard-coded precise constants in core .py (outside tests/tools/scripts)
  - Main TeX missing CSV linkage (pgfplotstable + .csv)
  - Missing data/alpha_two_loop_grid.csv

WARN categories (reported but do not fail):
  - Precise constants in .md, reports/, tools/, tests/, scripts/, validation/

Outputs a JSON report to reports/audit_computed_not_reference.json
"""
from __future__ import annotations
import argparse, re, sys, json
from pathlib import Path
from typing import List, Dict

FORBIDDEN_PATTERNS = [
    (r"137\.0359990\d+", "alpha^{-1} precise"),
    (r"\b0\.5109989\d{2,}\b", "m_e precise"),
    (r"\b105\.6583\d{2,}\b", "m_mu precise"),
    (r"\b1776\.8\d{2,}\b", "m_tau precise"),
]

TEXT_EXT = {".tex",".md",".py",".rst",".txt",".json",".yaml",".yml"}

# classify paths: return "fatal" or "warn"
def classify_file(p: Path) -> str:
    parts = set(p.parts)
    if any(seg in parts for seg in (".git","venv",".venv","build","dist","_build","__pycache__")):
        return "ignore"
    # Generated reference constants file is exempt (contains external refs by design)
    if p.name == "reference_constants.tex" and "tex" in parts:
        return "ignore"
    # soft areas → WARN
    if any(seg in parts for seg in ("reports","tools","tests","scripts","validation","docs","archive","speculative_extensions")):
        return "warn"
    if p.suffix.lower() == ".md":
        return "warn"
    # core .tex/.py → FATAL
    if p.suffix.lower() in (".tex",".py"):
        return "fatal"
    return "warn"

def read_text(p: Path) -> str:
    for enc in ("utf-8","latin-1","windows-1250"):
        try:
            return p.read_text(encoding=enc)
        except Exception:
            continue
    return ""

def scan_forbidden_literals(root: Path) -> Dict[str, List[Dict]]:
    hits = {"fatal": [], "warn": []}
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix.lower() not in TEXT_EXT:
            continue
        klass = classify_file(p)
        if klass == "ignore":
            continue
        txt = read_text(p)
        for rgx, label in FORBIDDEN_PATTERNS:
            for m in re.finditer(rgx, txt):
                s = max(0, m.start()-80); e = min(len(txt), m.end()+80)
                ctx = txt[s:e].replace("\n"," ")
                hits[klass].append({"file": str(p), "what": label, "match": m.group(0), "context": ctx})
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
    prov = {"alpha_from_ubt_two_loop_strict": [], "compute_two_loop_delta": [], "ubt_alpha_msbar": []}
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

    # scan literals
    hits = scan_forbidden_literals(root)
    if hits["fatal"]:
        failures.append(f"Hard-coded precise constants found in {len(hits['fatal'])} FATAL file(s).")
        # Print detailed FATAL file list
        print("\n== FATAL Files with Hard-coded Constants ==")
        fatal_by_file = {}
        for h in hits["fatal"]:
            if h["file"] not in fatal_by_file:
                fatal_by_file[h["file"]] = []
            fatal_by_file[h["file"]].append(h)
        
        for fpath in sorted(fatal_by_file.keys()):
            relpath = Path(fpath).relative_to(root) if Path(fpath).is_relative_to(root) else Path(fpath)
            print(f"\n  {relpath}")
            for h in fatal_by_file[fpath]:
                print(f"    - {h['what']}: {h['match']}")
                # Print context snippet (first 60 chars)
                ctx = h['context'].strip()[:60]
                print(f"      Context: {ctx}...")
        print()
    if hits["warn"]:
        warnings.append(f"Precise constants found in {len(hits['warn'])} non-core (WARN) file(s).")

    # main TeX checks
    chk = check_main_tex(main_tex)
    if not chk["exists"]:
        warnings.append(f"Main TeX not found: {main_tex}")
    else:
        if not (chk["uses_pgfplotstable"] and chk["mentions_csv"]):
            failures.append("Main TeX does not clearly include CSV tables via pgfplotstable.")
        if not chk["has_input_patch"]:
            warnings.append("Main TeX missing \\input{UBT_alpha_per_sector_patch} (recommended).")
        if not chk["has_input_hecke"]:
            warnings.append("Main TeX missing \\input{tex/UBT_hecke_L_route} (recommended).")

    # CSV presence
    csv = check_csv_presence(root)
    if not csv["alpha_csv"]:
        failures.append("Missing data/alpha_two_loop_grid.csv (export alpha grid first).")
    if not csv["leptons_csv"]:
        warnings.append("Missing data/leptons.csv (lepton table won't render).")

    # provenance
    prov = code_provenance(root)
    if not prov["alpha_from_ubt_two_loop_strict"] and not prov["compute_two_loop_delta"]:
        warnings.append("Alpha provider not found (no alpha_from_ubt_two_loop_strict or compute_two_loop_delta).")
    if not prov["ubt_alpha_msbar"]:
        warnings.append("Mass pipeline provider ubt_alpha_msbar() not found (cannot audit mass provenance).")

    # results
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

    report = {
        "root": str(root), "main_tex": str(main_tex),
        "failures": failures, "warnings": warnings,
        "hits": hits, "tex_check": chk, "csv_presence": csv, "provenance": prov
    }
    (root / "reports").mkdir(exist_ok=True, parents=True)
    (root / "reports" / "audit_computed_not_reference.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )
    raise SystemExit(rc)

if __name__ == "__main__":
    main()
