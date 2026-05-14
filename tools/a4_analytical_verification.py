#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""Symbolic consistency checks for the a4/theta3 bridge candidate.

This script verifies algebraic identities used in the Gap G137-B a4 note:
1) theta3(0|i) = pi^(1/4)/Gamma(3/4)
2) B_target = 12^(3/2) * 2^(1/8) * theta3(0|i)^(1/4)
"""

from __future__ import annotations

import math
from typing import Optional

try:
    import sympy as sp
except ModuleNotFoundError:
    sp = None


def D2(n: int) -> int:
    """Number of positive divisor pairs (a,b) with a*b = n."""
    count = 0
    for a in range(1, int(math.sqrt(n)) + 1):
        if n % a == 0:
            b = n // a
            count += 1 if a == b else 2
    return count


def veff_t2(n: int, b: float, r: float = 1.0) -> float:
    """Asymptotic T²-motivated model: V_eff(n)=n²-B*n*ln(n/R)."""
    if n <= 0:
        raise ValueError("n must be positive")
    return n**2 - b * n * math.log(n / r)




def chowla_selberg_numeric_check() -> None:
    """Numerically check Z'_Z2(0) and theta/eta identities (mpmath path)."""
    try:
        import mpmath as mp
    except ModuleNotFoundError:
        print("mpmath not installed; skipping Chowla-Selberg numeric check.")
        return

    mp.mp.dps = 60
    L0 = mp.dirichlet(0, [0, 1, 0, -1])
    z0 = mp.zeta(0)
    zp0 = mp.diff(mp.zeta, 0)
    Lp0 = mp.diff(lambda s: mp.dirichlet(s, [0, 1, 0, -1]), 0)
    zprime_z2 = 4 * (zp0 * L0 + z0 * Lp0)

    theta3 = mp.jtheta(3, 0, mp.e ** (-mp.pi))
    eta_i = mp.qp(mp.e ** (-2 * mp.pi), mp.e ** (-2 * mp.pi)) * mp.e ** (mp.pi / 12)

    print("=== Chowla-Selberg numeric check ===")
    print(f"L(0,chi_-4)      = {L0}")
    print(f"L'(0,chi_-4)     = {Lp0}")
    print(f"Z'_Z2(0)         = {zprime_z2}")
    print(f"theta3(0|i)      = {theta3}")
    print(f"eta(i)           = {eta_i}")
    print(f"theta3/eta       = {theta3/eta_i}")
    print(f"ln(theta3)       = {mp.log(theta3)}")
    print()

def main() -> None:
    target_b: Optional[float] = None

    if sp is not None:
        pi = sp.pi
        theta3 = sp.functions.special.elliptic_functions.jtheta(3, 0, sp.exp(-pi))
        theta3_ramanujan = pi ** sp.Rational(1, 4) / sp.gamma(sp.Rational(3, 4))
        diff_theta = sp.simplify(theta3 - theta3_ramanujan)

        b_from_theta = 12 ** sp.Rational(3, 2) * 2 ** sp.Rational(1, 8) * theta3 ** sp.Rational(1, 4)
        b_from_ramanujan = (
            12 ** sp.Rational(3, 2)
            * 2 ** sp.Rational(1, 8)
            * (pi ** sp.Rational(1, 4) / sp.gamma(sp.Rational(3, 4))) ** sp.Rational(1, 4)
        )
        diff_b = sp.simplify(b_from_theta - b_from_ramanujan)

        print("theta3(0|i) symbolic:", theta3)
        print("theta3 Ramanujan form:", theta3_ramanujan)
        print("theta3 difference (symbolic):", diff_theta)
        print("theta3 difference (numeric):", sp.N(diff_theta, 50))
        print()
        print("B(theta3) symbolic:", b_from_theta)
        print("B(Ramanujan) symbolic:", b_from_ramanujan)
        print("B difference (symbolic):", diff_b)
        print("B difference (numeric):", sp.N(diff_b, 50))
        print("B value (numeric):", sp.N(b_from_theta, 30))
        print()

        target_b = float(sp.N(b_from_theta, 25))
    else:
        print("sympy not installed; using numeric fallback only.")
        # Ramanujan/theta3 bridge:
        # B = 12^(3/2) * 2^(1/8) * (pi^(1/4)/Gamma(3/4))^(1/4)
        target_b = 12**1.5 * 2**0.125 * (math.pi**0.25 / math.gamma(0.75)) ** 0.25
        print(f"B_target fallback = {target_b:.12f}")
        print()

    print("=== T² divisor-sum asymptotic checks ===")
    print(f"B_target (numeric): {target_b:.8f}")
    print()

    vals = [10, 50, 100, 200, 500]
    for N in vals:
        total = sum(k * D2(k) for k in range(1, N + 1))
        expected = N**2 * math.log(N) / 2.0
        ratio = total / expected if expected != 0 else float("nan")
        print(
            f"N={N:>3}: Σ[k·D2(k)]={total:>12.4f}, "
            f"N²lnN/2={expected:>12.4f}, ratio={ratio:.6f}"
        )
    print()

    for n in [10, 50, 137, 200]:
        print(f"Veff_T2(n={n}) = {veff_t2(n, target_b):.8f}")

    print()
    chowla_selberg_numeric_check()


if __name__ == "__main__":
    main()
