#!/usr/bin/env python3
from __future__ import annotations
import argparse, math, csv, pathlib

# ------------------------------
# Robust theta constants at z=0 for tau = i*kappa
# We work in log-domain and switch to kappa-asymptotics when kappa is large.
# ------------------------------

# Thresholds: tune if needed (no external deps)
KAPPA_THETA2_ASYM = 30.0   # beyond this, exp(-pi*kappa) underflows in double precision
KAPPA_THETA34_ASYM = 30.0  # theta3, theta4 ~ 1, so log ~ 0 safely

def _log_theta2_from_kappa(kappa: float) -> float:
    """
    log theta2(0|i*kappa).
    For large kappa: theta2 ~ 2 * q^{1/4}, q = exp(-pi*kappa) => log theta2 ~ ln2 - (pi/4)*kappa
    For moderate/small kappa: do a log-sum-exp on 2 * sum q^{(n+1/2)^2}.
    """
    if kappa >= KAPPA_THETA2_ASYM:
        return math.log(2.0) - 0.25 * math.pi * kappa

    # moderate/small kappa: compute via q
    q = math.exp(-math.pi * kappa)  # here it's safe (not underflow)
    # exponents e_n = ((n+1/2)^2) * ln q = -pi*kappa * (n+1/2)^2
    # max exponent is at n=0
    terms = 200
    lnq = -math.pi * kappa
    exps = [ ((n+0.5)*(n+0.5)) * lnq for n in range(terms) ]
    m = exps[0]
    s = 0.0
    for e in exps:
        s += math.exp(e - m)
    return math.log(2.0) + m + math.log(s)

def _log_theta3_from_kappa(kappa: float) -> float:
    """
    log theta3(0|i*kappa).
    For large kappa, theta3 ~ 1 => log ~ 0.
    Otherwise sum 1 + 2 sum_{n>=1} q^{n^2}.
    """
    if kappa >= KAPPA_THETA34_ASYM:
        return 0.0
    q = math.exp(-math.pi * kappa)
    s = 1.0
    # stop when term underflows to 0
    for n in range(1, 2000):
        t = q ** (n*n)
        if t == 0.0:
            break
        s += 2.0 * t
    # numerically s>0
    return math.log(s)

def _log_theta4_from_kappa(kappa: float) -> float:
    """
    log theta4(0|i*kappa).
    For large kappa, theta4 ~ 1 => log ~ 0.
    Otherwise sum 1 + 2 sum (-1)^n q^{n^2}.
    """
    if kappa >= KAPPA_THETA34_ASYM:
        return 0.0
    q = math.exp(-math.pi * kappa)
    s = 1.0
    sign = -1.0
    for n in range(1, 2000):
        t = q ** (n*n)
        if t == 0.0:
            break
        s += 2.0 * sign * t
        sign *= -1.0
    # s should remain >0
    if s <= 0.0:
        # extreme cancellation fallback: treat as ~1
        return 0.0
    return math.log(s)

def _log_theta_product(kappa: float) -> float:
    # log(θ2 θ3 θ4) = log θ2 + log θ3 + log θ4
    return (_log_theta2_from_kappa(kappa)
            + _log_theta3_from_kappa(kappa)
            + _log_theta4_from_kappa(kappa))

# ------------------------------
# Hecke modulation in log-domain
# ------------------------------

def hecke_modulation(kappa: float, p: int, n: int) -> float:
    """
    Minimal, no-fit, weight-neutral Hecke modulation factor:
      M_n = [Θ(p n τ)/Θ(n τ)] / [Θ(p τ)/Θ(τ)],   Θ = θ2 θ3 θ4,  τ = i κ.
    Computed in log-domain to avoid underflow, with asymptotic kappa-handling.
    """
    L_base   = _log_theta_product(kappa)
    L_nbase  = _log_theta_product(n * kappa)
    L_pbase  = _log_theta_product(p * kappa)
    L_pnbase = _log_theta_product(p * n * kappa)
    # log M = (L_pn - L_n) - (L_p - L_1)
    L_M = (L_pnbase - L_nbase) - (L_pbase - L_base)
    return math.exp(L_M)

# ------------------------------
# Phase-II exporter
# ------------------------------

def _theta_product_linear(kappa: float) -> float:
    """
    For Phase-I ratios Rn, linear-domain is safe at base kappa≈O(1).
    To be robust, reuse kappa-based logs and exponentiate.
    """
    return math.exp(_log_theta_product(kappa))

def main():
    ap = argparse.ArgumentParser(description="Export no-fit Yukawa ratios with minimal Hecke modulation (robust)")
    ap.add_argument("--kappa", type=float, default=0.72, help="purely imaginary τ=i κ")
    ap.add_argument("--p", type=int, default=137, help="Hecke sector label (prime)")
    ap.add_argument("--outfile", type=pathlib.Path, default=pathlib.Path("validation/yukawa_ratios_theta_hecke.csv"))
    args = ap.parse_args()

    # Pure modular ratios (Phase I)
    prod1 = _theta_product_linear(args.kappa)
    prod3 = _theta_product_linear(3.0 * args.kappa)
    prod9 = _theta_product_linear(9.0 * args.kappa)
    R3 = prod3 / prod1 if prod1 != 0.0 else float('nan')
    R9 = prod9 / prod1 if prod1 != 0.0 else float('nan')

    # Minimal Hecke modulation (log-domain + kappa-asymptotics)
    M3 = hecke_modulation(args.kappa, args.p, 3)
    M9 = hecke_modulation(args.kappa, args.p, 9)

    # Phase II candidates (still no-fit)
    Y3 = R3 * M3 if (R3 == R3 and M3 == M3) else float('nan')
    Y9 = R9 * M9 if (R9 == R9 and M9 == M9) else float('nan')

    out = args.outfile
    out.parent.mkdir(parents=True, exist_ok=True)
    hdr = not out.exists()
    with out.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if hdr:
            w.writerow(["kappa","p","R3","R9","M3","M9","Y3","Y9"])
        w.writerow([args.kappa, args.p,
                    f"{R3:.12e}", f"{R9:.12e}",
                    f"{M3:.12e}", f"{M9:.12e}",
                    f"{Y3:.12e}", f"{Y9:.12e}"])

    print(f"[theta-hecke] κ={args.kappa}, p={args.p} → "
          f"R3={R3:.6e}, R9={R9:.6e}, M3={M3:.6e}, M9={M9:.6e}, "
          f"Y3={Y3:.6e}, Y9={Y9:.6e}")
    print(f"[theta-hecke] wrote → {out}")

if __name__ == "__main__":
    main()

