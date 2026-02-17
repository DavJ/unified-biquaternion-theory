#!/usr/bin/env python3
"""
generate_tex_snippets_from_csv.py
Reads:
  - data/alpha_two_loop_grid.csv (expects columns: mu,alpha,alpha_inv)
  - data/leptons.csv            (expects columns: name,value,uncertainty,units)
Writes:
  - tex/snippets_generated.tex with LaTeX macros:
      \AlphaInvBest
      \AlphaBest
      \ElectronMassMeV
      \MuonMassMeV
      \TauMassMeV
Behavior:
  - Picks the row with smallest |alpha_inv - 137.035999| as the "best" sample (if alpha grid exists).
  - Falls back to first row if grid not found.
  - Lepton masses: uses rows with name in {"electron","muon","tau"} (case-insensitive).
"""
from __future__ import annotations
import csv, sys, math
from pathlib import Path

def read_csv(path):
    if not path.exists():
        return []
    rows = []
    with path.open("r", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        for r in rdr:
            rows.append({k.strip(): v.strip() for k,v in r.items()})
    return rows

def parse_float(x, default=None):
    try:
        return float(x)
    except Exception:
        return default

def pick_alpha(rows):
    if not rows:
        return None, None
    # prefer the one closest to CODATA-ish 137.035999 (not a fit; just selector for presentation macro)
    target = 137.035999
    best = None
    best_diff = float("inf")
    for r in rows:
        ainv = parse_float(r.get("alpha_inv"))
        a = parse_float(r.get("alpha"))
        if ainv is None and a is not None and a != 0.0:
            ainv = 1.0/a
        if ainv is None:
            continue
        diff = abs(ainv - target)
        if diff < best_diff:
            best_diff, best = diff, (a, ainv)
    if best is None:
        # fallback first row
        r0 = rows[0]
        a = parse_float(r0.get("alpha"))
        ainv = parse_float(r0.get("alpha_inv"))
        if ainv is None and a not in (None, 0.0):
            ainv = 1.0/a
        return a, ainv
    return best

def leptons_map(rows):
    out = {}
    for r in rows:
        name = (r.get("name","") or "").strip().lower()
        val = parse_float(r.get("value"))
        if name in ("electron","e","e-","e_plus","e_minus"):
            out["ElectronMassMeV"] = val
        elif name in ("muon","mu","mu-","mu_plus"):
            out["MuonMassMeV"] = val
        elif name in ("tau","tau-","tau_plus"):
            out["TauMassMeV"] = val
    return out

def main():
    repo = Path(".").resolve()
    alpha_rows = read_csv(repo / "data" / "alpha_two_loop_grid.csv")
    lepton_rows = read_csv(repo / "data" / "leptons.csv")

    a, ainv = pick_alpha(alpha_rows)
    lep = leptons_map(lepton_rows)

    tex = []
    tex.append("% Auto-generated. Do not edit by hand.")
    if ainv is not None:
        tex.append(f"\\newcommand{{\\AlphaInvBest}}{{{ainv:.12f}}}")
    if a is not None:
        tex.append(f"\\newcommand{{\\AlphaBest}}{{{a:.16f}}}")
    for key in ("ElectronMassMeV","MuonMassMeV","TauMassMeV"):
        if key in lep and lep[key] is not None:
            tex.append(f"\\newcommand{{\\{key}}}{{{lep[key]:.9f}}}")
    out = Path("tex") / "snippets_generated.tex"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(tex) + "\n", encoding="utf-8")
    print(f"[ok] wrote {out}")

if __name__ == "__main__":
    main()
