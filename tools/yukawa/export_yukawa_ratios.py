#!/usr/bin/env python3
from __future__ import annotations
import argparse, math, csv, pathlib

def theta2(q: float, terms: int=200) -> float:
    s = 0.0
    for n in range(terms):
        s += q**((n+0.5)*(n+0.5))
    return 2.0*s

def theta3(q: float, terms: int=500) -> float:
    s = 1.0
    for n in range(1, terms+1):
        s += 2.0 * (q**(n*n))
    return s

def theta4(q: float, terms: int=500) -> float:
    s = 1.0
    for n in range(1, terms+1):
        s += 2.0 * ((-1.0)**n) * (q**(n*n))
    return s

def theta_product(kappa: float) -> float:
    q = math.exp(-math.pi * kappa)
    return theta2(q) * theta3(q) * theta4(q)

def main():
    ap = argparse.ArgumentParser(description="Export no-fit Yukawa theta ratios R3, R9 into CSV")
    ap.add_argument("--kappa", type=float, default=0.72, help="purely imaginary τ=i κ")
    ap.add_argument("--p", type=int, default=137, help="Hecke sector label (not used in Phase I)")
    ap.add_argument("--outfile", type=pathlib.Path, default=pathlib.Path("validation/yukawa_ratios_theta.csv"))
    args = ap.parse_args()

    prod1 = theta_product(args.kappa)
    prod3 = theta_product(3.0*args.kappa)
    prod9 = theta_product(9.0*args.kappa)

    R3 = prod3 / prod1 if prod1 != 0 else float('nan')
    R9 = prod9 / prod1 if prod1 != 0 else float('nan')

    out = args.outfile
    out.parent.mkdir(parents=True, exist_ok=True)
    hdr = not out.exists()
    with out.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if hdr:
            w.writerow(["kappa","p","R3","R9"])
        w.writerow([args.kappa, args.p, f"{R3:.12e}", f"{R9:.12e}"])

    print(f"[theta-yukawa] κ={args.kappa}, p={args.p} → R3={R3:.6e}, R9={R9:.6e}")
    print(f"[theta-yukawa] wrote → {out}")

if __name__ == "__main__":
    main()
