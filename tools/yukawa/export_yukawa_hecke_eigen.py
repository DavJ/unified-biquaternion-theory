#!/usr/bin/env python3
from __future__ import annotations
import argparse, math, csv, pathlib

# Phase IV: Hecke Eigenform Normalization (no-fit)
# Φ(τ) = (E4(τ)/E6(τ)) * [Θ(τ)]^2,   Θ = θ2 θ3 θ4  at z=0, τ = i κ (pure imaginary)
# Yukawa ratios (candidates):  Y_n = |Φ(nτ)/Φ(τ)|  for n in {3,9}
#
# Implementation details:
# - No external deps; uses real q-series for E4, E6 since τ is purely imaginary.
# - Robust theta product computed in log-domain with κ-asymptotics (no underflow).
# - No fitted parameters; κ is a geometric modulus, here provided as an input.

# ------------------------------
# Robust theta constants (log-domain) for τ = i κ
# ------------------------------

KAPPA_THETA2_ASYM = 30.0
KAPPA_THETA34_ASYM = 30.0

def _log_theta2_from_kappa(kappa: float) -> float:
    if kappa >= KAPPA_THETA2_ASYM:
        return math.log(2.0) - 0.25 * math.pi * kappa
    lnq = -math.pi * kappa
    terms = 200
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

def theta_prod(kappa: float) -> float:
    # linear domain via exponentiating log (safe for moderate κ)
    return math.exp(_log_theta_product(kappa))

# ------------------------------
# Eisenstein series E4, E6 via real q-series for τ = i κ
# q_std = exp(2π i τ) = exp(-2π κ) \in (0,1)
# E4(τ) = 1 + 240 Σ_{n≥1} σ_3(n) q^n
# E6(τ) = 1 - 504 Σ_{n≥1} σ_5(n) q^n
# ------------------------------

def sigma_power(n: int, k: int) -> int:
    # σ_k(n) = sum_{d|n} d^k
    s = 0
    r = int(math.isqrt(n))
    for d in range(1, r+1):
        if n % d == 0:
            s += d**k
            e = n // d
            if e != d:
                s += e**k
    return s

def eisenstein_E4_E6(kappa: float, tol: float = 1e-30, nmax: int = 100000) -> tuple[float, float]:
    q = math.exp(-2.0 * math.pi * kappa)  # q_std
    # Simple bound: terms shrink like q^n; stop when next term below tol
    E4 = 1.0
    E6 = 1.0
    n = 1
    while n <= nmax:
        qn = q**n
        if qn < tol:
            break
        s3 = sigma_power(n, 3)
        s5 = sigma_power(n, 5)
        E4 += 240.0 * s3 * qn
        E6 -= 504.0 * s5 * qn
        n += 1
    return E4, E6

# ------------------------------
# Φ(τ) and Yukawa ratios
# ------------------------------

def phi_eigen(kappa: float) -> float:
    # Φ(τ)= (E4/E6) * [Θ]^2 ; for τ=i κ
    E4, E6 = eisenstein_E4_E6(kappa)
    Th = theta_prod(kappa)
    return (E4 / E6) * (Th * Th)

def compute_ratios(kappa: float) -> dict:
    Phi1 = phi_eigen(kappa)
    Phi3 = phi_eigen(3.0 * kappa)
    Phi9 = phi_eigen(9.0 * kappa)
    # Phase-I Rn for reference (not used directly in Y; Φ already carries structure)
    prod1 = theta_prod(kappa); prod3 = theta_prod(3.0*kappa); prod9 = theta_prod(9.0*kappa)
    R3 = prod3 / prod1 if prod1 != 0 else float('nan')
    R9 = prod9 / prod1 if prod1 != 0 else float('nan')
    Y3 = abs(Phi3 / Phi1)
    Y9 = abs(Phi9 / Phi1)
    return dict(kappa=kappa, R3=R3, R9=R9, Phi_tau=Phi1, Phi_3tau=Phi3, Phi_9tau=Phi9, Y3=Y3, Y9=Y9)

def main():
    ap = argparse.ArgumentParser(description="Phase IV: Hecke eigenform normalized Yukawa ratios (no-fit)")
    ap.add_argument("--kappa", type=float, default=0.72, help="purely imaginary τ=i κ")
    ap.add_argument("--outfile", type=pathlib.Path, default=pathlib.Path("validation/yukawa_ratios_theta_eigen.csv"))
    args = ap.parse_args()

    res = compute_ratios(args.kappa)

    out = args.outfile
    out.parent.mkdir(parents=True, exist_ok=True)
    hdr = not out.exists()
    with out.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if hdr:
            w.writerow(["kappa","R3","R9","Phi_tau","Phi_3tau","Phi_9tau","Y3","Y9"])
        w.writerow([res["kappa"],
                    f'{res["R3"]:.12e}', f'{res["R9"]:.12e}',
                    f'{res["Phi_tau"]:.12e}', f'{res["Phi_3tau"]:.12e}', f'{res["Phi_9tau"]:.12e}',
                    f'{res["Y3"]:.12e}', f'{res["Y9"]:.12e}'])

    print(f'[theta-eigen] κ={args.kappa} → R3={res["R3"]:.6e}, R9={res["R9"]:.6e}, '
          f'Y3={res["Y3"]:.6e}, Y9={res["Y9"]:.6e}')
    print(f'[theta-eigen] wrote → {out}')

if __name__ == "__main__":
    main()
