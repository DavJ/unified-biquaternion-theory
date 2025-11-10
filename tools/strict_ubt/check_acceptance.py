#!/usr/bin/env python3
from __future__ import annotations
import csv, sys, math
from pathlib import Path

# PDG reference values (MeV)
PDG = {"me":0.51099895, "mmu":105.6583755, "mtau":1776.86}
TH  = {"abs_rel_me":0.05, "abs_rel_mmu":0.05, "abs_rel_mtau":0.05,
       "ratio_mmu_me":0.10, "ratio_mtau_me":0.10}

def f2(x):
    try:
        v = float(x)
        if math.isfinite(v):
            return v
    except Exception:
        pass
    return float("nan")

def last_row(path: Path):
    rows = list(csv.DictReader(path.open()))
    return rows[-1] if rows else None

def main():
    cand = Path("validation/lepton_masses_nonpert_p137.csv")
    if not cand.exists():
        print("REJECTED: missing", cand); sys.exit(2)
    r = last_row(cand)
    if not r:
        print("REJECTED: empty CSV", cand); sys.exit(2)

    me   = f2(r.get("me_MeV"))
    mmu  = f2(r.get("mmu_MeV"))
    mtau = f2(r.get("mtau_MeV"))

    # Basic sanity
    bad = []
    for name,val in [("me",me),("mmu",mmu),("mtau",mtau)]:
        if not math.isfinite(val) or val <= 0.0:
            bad.append(name)
    if bad:
        print(f"REJECTED: non-physical masses for {', '.join(bad)} (<=0 or NaN).")
        print(f"  Values: me={me}, mmu={mmu}, mtau={mtau}")
        print("  Hint: Exponential suppression too strong (S/alpha is huge) – adjust geometric normalization or kappa.")
        sys.exit(1)

    # Relative errors
    r_me   = abs(me  - PDG["me"])   / PDG["me"]
    r_mmu  = abs(mmu - PDG["mmu"])  / PDG["mmu"]
    r_mtau = abs(mtau- PDG["mtau"]) / PDG["mtau"]

    # Ratios vs PDG
    ratio_mmu_me, ratio_mtau_me = mmu/me, mtau/me
    Rm, Rt = PDG["mmu"]/PDG["me"], PDG["mtau"]/PDG["me"]
    r_ratio_mmu_me  = abs(ratio_mmu_me - Rm) / Rm
    r_ratio_mtau_me = abs(ratio_mtau_me - Rt) / Rt

    ok = True
    if r_me   > TH["abs_rel_me"]:    ok=False; print(f"me fail: rel={r_me:.3%} (pred={me}, PDG={PDG['me']})")
    if r_mmu  > TH["abs_rel_mmu"]:   ok=False; print(f"mmu fail: rel={r_mmu:.3%} (pred={mmu}, PDG={PDG['mmu']})")
    if r_mtau > TH["abs_rel_mtau"]:  ok=False; print(f"mtau fail: rel={r_mtau:.3%} (pred={mtau}, PDG={PDG['mtau']})")
    if r_ratio_mmu_me  > TH["ratio_mmu_me"]:  ok=False; print(f"mmu/me ratio fail: rel={r_ratio_mmu_me:.3%} (pred={ratio_mmu_me}, PDG={Rm})")
    if r_ratio_mtau_me > TH["ratio_mtau_me"]: ok=False; print(f"mtau/me ratio fail: rel={r_ratio_mtau_me:.3%} (pred={ratio_mtau_me}, PDG={Rt})")

    if ok:
        print("ACCEPTED: non-perturbative masses meet thresholds")
        sys.exit(0)
    print("REJECTED: theory off; do not publish to data/leptons.csv")
    sys.exit(1)

if __name__ == "__main__":
    main()
