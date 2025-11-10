#!/usr/bin/env python3
from __future__ import annotations
import csv, sys
from pathlib import Path

PDG = {"me":0.51099895,"mmu":105.6583755,"mtau":1776.86}
TH  = {"abs_rel_me":0.05,"abs_rel_mmu":0.05,"abs_rel_mtau":0.05,"ratio_mmu_me":0.10,"ratio_mtau_me":0.10}

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
    me, mmu, mtau = float(r["me_MeV"]), float(r["mmu_MeV"]), float(r["mtau_MeV"])
    r_me, r_mmu, r_mtau = abs(me-PDG["me"])/PDG["me"], abs(mmu-PDG["mmu"])/PDG["mmu"], abs(mtau-PDG["mtau"])/PDG["mtau"]
    ratio_mmu_me, ratio_mtau_me = mmu/me, mtau/me
    Rm = PDG["mmu"]/PDG["me"]; Rt = PDG["mtau"]/PDG["me"]
    r_ratio_mmu_me  = abs(ratio_mmu_me - Rm) / Rm
    r_ratio_mtau_me = abs(ratio_mtau_me - Rt) / Rt
    ok = True
    if r_me   > TH["abs_rel_me"]:    ok=False; print(f"me fail: rel={r_me:.3%}")
    if r_mmu  > TH["abs_rel_mmu"]:   ok=False; print(f"mmu fail: rel={r_mmu:.3%}")
    if r_mtau > TH["abs_rel_mtau"]:  ok=False; print(f"mtau fail: rel={r_mtau:.3%}")
    if r_ratio_mmu_me  > TH["ratio_mmu_me"]:  ok=False; print(f"mmu/me ratio fail: rel={r_ratio_mmu_me:.3%}")
    if r_ratio_mtau_me > TH["ratio_mtau_me"]: ok=False; print(f"mtau/me ratio fail: rel={r_ratio_mtau_me:.3%}")
    if ok:
        print("ACCEPTED: non-perturbative masses meet thresholds"); sys.exit(0)
    print("REJECTED: theory off; do not publish to data/leptons.csv"); sys.exit(1)

if __name__ == "__main__":
    main()
