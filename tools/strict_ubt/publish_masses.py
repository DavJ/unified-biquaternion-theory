#!/usr/bin/env python3
import csv, sys
from pathlib import Path

def main():
    cand = Path("validation/lepton_masses_strict_p137.csv")
    if not cand.exists():
        cand = Path("validation/lepton_masses_strict.csv")
    if not cand.exists():
        print("No strict masses CSV found; run `make masses-strict` first.", file=sys.stderr)
        sys.exit(1)

    rows = list(csv.DictReader(cand.open()))
    if not rows:
        print("Empty CSV:", cand, file=sys.stderr)
        sys.exit(1)
    row = rows[0]

    outdir = Path("data"); outdir.mkdir(exist_ok=True)
    with (outdir/"leptons.csv").open("w", newline="") as fo:
        w = csv.writer(fo)
        w.writerow(['name','symbol','msbar_mass_mev','pole_mass_mev','mu_mev','alpha_mu'])
        w.writerow(['electron','e','', row.get('me_MeV',''), '', ''])
        w.writerow(['muon','mu','', row.get('mmu_MeV',''), '', ''])
        w.writerow(['tau','tau','', row.get('mtau_MeV',''), '', ''])
    print("OK: data/leptons.csv updated from strict results")

if __name__ == "__main__":
    main()

