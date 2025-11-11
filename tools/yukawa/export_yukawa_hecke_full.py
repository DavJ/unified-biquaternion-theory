#!/usr/bin/env python3
from __future__ import annotations
import argparse, math, csv, pathlib

# ---------- Robust log-theta product Θ = θ2 θ3 θ4 at z=0, τ = i κ ----------

KAPPA_THETA2_ASYM = 30.0
KAPPA_THETA34_ASYM = 30.0

def _log_theta2_from_kappa(kappa: float) -> float:
    if kappa >= KAPPA_THETA2_ASYM:
        return math.log(2.0) - 0.25 * math.pi * kappa
    lnq = -math.pi * kappa
    terms = 200
    # exps_n = ((n+1/2)^2) * lnq, maximum at n=0
    exps0 = (0.5*0.5) * lnq
    s = 1.0
    for n in range(1, terms):
        e = ((n+0.5)*(n+0.5)) * lnq
        s += math.exp(e - exps0)
    return math.log(2.0) + exps0 + math.log(s)

def _log_theta3_from_kappa(kappa: float) -> float:
    if kappa >= KAPPA_THETA34_ASYM:
        return 0.0
    lnq = -math.pi * kappa
    s = 1.0
    for n in range(1, 2000):
        e = (n*n) * lnq
        t = math.exp(e)
        if t == 0.0:
            break
        s += 2.0 * t
    return math.log(s)

def _log_theta4_from_kappa(kappa: float) -> float:
    if kappa >= KAPPA_THETA34_ASYM:
        return 0.0
    lnq = -math.pi * kappa
    s = 1.0
    sign = -1.0
    for n in range(1, 2000):
        e = (n*n) * lnq
        t = math.exp(e)
        if t == 0.0:
            break
        s += 2.0 * sign * t
        sign *= -1.0
    if s <= 0.0:
        return 0.0
    return math.log(s)

def _log_theta_product(kappa: float) -> float:
    return (_log_theta2_from_kappa(kappa)
            + _log_theta3_from_kappa(kappa)
            + _log_theta4_from_kappa(kappa))

def _log_Theta_ratio(kappa_num: float, kappa_den: float) -> float:
    # log (Θ(i*kappa_num)/Θ(i*kappa_den))
    return _log_theta_product(kappa_num) - _log_theta_product(kappa_den)

def _theta_product_linear(kappa: float) -> float:
    return math.exp(_log_theta_product(kappa))

# ---------- Hecke sweep candidates (no-fit) ----------
# We construct two canonical, weight-neutral multiplicative candidates:
#   PUSH:  M_n^push = Π_{ℓ∈P} [ Θ(ℓ n τ)/Θ(n τ) ] / [ Θ(ℓ τ)/Θ(τ) ]
#   PULL:  M_n^pull = Π_{ℓ∈P} [ Θ(ℓ τ)/Θ(τ) ] / [ Θ(ℓ n τ)/Θ(n τ) ]
# Both normalize to 1 at n = 1. No fitted parameters: primes P chosen deterministically.

def hecke_mod_push(kappa: float, n: int, primes: list[int]) -> float:
    L = 0.0
    for ell in primes:
        L += _log_Theta_ratio(ell * n * kappa, n * kappa) - _log_Theta_ratio(ell * kappa, kappa)
    return math.exp(L)

def hecke_mod_pull(kappa: float, n: int, primes: list[int]) -> float:
    L = 0.0
    for ell in primes:
        L += _log_Theta_ratio(ell * kappa, kappa) - _log_Theta_ratio(ell * n * kappa, n * kappa)
    return math.exp(L)

def parse_primes(s: str) -> list[int]:
    s = s.strip()
    if not s:
        return [2,3,5,7,11,13,17,19,23,29]
    return [int(x) for x in s.replace(",", " ").split()]

def main():
    ap = argparse.ArgumentParser(description="Phase III: Hecke-sweep Yukawa ratios (no-fit, CSV-driven)")
    ap.add_argument("--kappa", type=float, default=0.72, help="purely imaginary τ=i κ")
    ap.add_argument("--p", type=int, default=137, help="(kept for provenance; not used directly in sweep)")
    ap.add_argument("--primes", type=str, default="", help="space- or comma-separated primes, default '2 3 5 7 11 13 17 19 23 29'")
    ap.add_argument("--outfile", type=pathlib.Path, default=pathlib.Path("validation/yukawa_ratios_theta_hecke_full.csv"))
    args = ap.parse_args()
    primes = parse_primes(args.primes)

    # Phase I ratios Rn
    prod1 = _theta_product_linear(args.kappa)
    prod3 = _theta_product_linear(3.0 * args.kappa)
    prod9 = _theta_product_linear(9.0 * args.kappa)
    R3 = prod3 / prod1 if prod1 != 0.0 else float('nan')
    R9 = prod9 / prod1 if prod1 != 0.0 else float('nan')

    # Phase III Hecke sweep (PUSH and PULL)
    M3_push = hecke_mod_push(args.kappa, 3, primes)
    M9_push = hecke_mod_push(args.kappa, 9, primes)
    M3_pull = hecke_mod_pull(args.kappa, 3, primes)
    M9_pull = hecke_mod_pull(args.kappa, 9, primes)

    # Candidate Yukawa ratios
    Y3_push = R3 * M3_push
    Y9_push = R9 * M9_push
    Y3_pull = R3 * M3_pull
    Y9_pull = R9 * M9_pull

    out = args.outfile
    out.parent.mkdir(parents=True, exist_ok=True)
    hdr = not out.exists()
    with out.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if hdr:
            w.writerow(["kappa","primes","R3","R9","M3_push","M9_push","M3_pull","M9_pull","Y3_push","Y9_push","Y3_pull","Y9_pull"])
        w.writerow([args.kappa, " ".join(str(p) for p in primes),
                    f"{R3:.12e}", f"{R9:.12e}",
                    f"{M3_push:.12e}", f"{M9_push:.12e}", f"{M3_pull:.12e}", f"{M9_pull:.12e}",
                    f"{Y3_push:.12e}", f"{Y9_push:.12e}", f"{Y3_pull:.12e}", f"{Y9_pull:.12e}"])

    print(f"[theta-hecke-full] κ={args.kappa}, P={primes} → "
          f"R3={R3:.6e}, R9={R9:.6e}, "
          f"M3_push={M3_push:.6e}, M9_push={M9_push:.6e}, "
          f"M3_pull={M3_pull:.6e}, M9_pull={M9_pull:.6e}")
    print(f"[theta-hecke-full] Y3_push={Y3_push:.6e}, Y9_push={Y9_push:.6e}, "
          f"Y3_pull={Y3_pull:.6e}, Y9_pull={Y9_pull:.6e}")
    print(f"[theta-hecke-full] wrote → {out}")

if __name__ == "__main__":
    main()
