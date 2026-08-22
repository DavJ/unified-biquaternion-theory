#!/usr/bin/env python3
"""Exact/numerical checks for the GR endgame audit.

Checks:
- split-jet multiplier equations force lambda=0 on non-null patches;
- the proper-time coefficient matches the stated analytic prefactor;
- the self-dual KK constant is reproduced independently by integral and series;
- the N_B=8 reduced-Planck ratio is numerically correct.
"""
from __future__ import annotations

import math
import mpmath as mp
import sympy as sp


def multiplier_rank(x: sp.Matrix, eta: sp.Matrix) -> int:
    """Rank of equations lambda.X=0 and lambda^[a X^{b]}=0 for lambda."""
    n = 4
    x_up = x
    x_lo = eta * x_up
    rows: list[list[sp.Expr]] = []

    # lambda_a X^a = 0, taking lambda_up variables and lowering with eta.
    rows.append([x_lo[i] for i in range(n)])

    # lambda^[a X^{b]} = 0.
    for a in range(n):
        for b in range(a + 1, n):
            row = [sp.Integer(0)] * n
            row[a] = x_up[b]
            row[b] = -x_up[a]
            rows.append(row)
    return sp.Matrix(rows).rank()


def auxiliary_checks() -> dict[str, bool]:
    eta = sp.diag(-1, 1, 1, 1)
    timelike = sp.Matrix([2, 1, 0, 0])   # X^2=-3
    spacelike = sp.Matrix([1, 0, 0, 2])  # X^2=+3
    null = sp.Matrix([1, 1, 0, 0])
    return {
        "timelike_multiplier_rank_4": multiplier_rank(timelike, eta) == 4,
        "spacelike_multiplier_rank_4": multiplier_rank(spacelike, eta) == 4,
        "null_patch_degenerates": multiplier_rank(null, eta) < 4,
    }


def analytic_prefactor_check() -> bool:
    NB, xi, I = sp.symbols("N_B xi I", real=True)
    coeff = -sp.Rational(1, 2) * (4 * sp.pi) ** -2 * NB * (sp.Rational(1, 6) - xi) * I
    target = -NB * (1 - 6 * xi) * I / (192 * sp.pi**2)
    return sp.simplify(coeff - target) == 0


def cpsi_integral(dps: int = 50) -> mp.mpf:
    mp.mp.dps = dps

    # Integrating directly to ``mp.inf`` makes some mpmath releases evaluate
    # jtheta at an astronomically tiny nome and overflow while converting that
    # nome to fixed-point form.  The exact substitution t=1/u removes the
    # infinite interval and the u^-2 Jacobian:
    #
    #   int_1^inf u^-2 theta_3(0,e^-u) du
    #     = int_0^1 theta_3(0,e^(-1/t)) dt.
    #
    # The endpoint value is the continuous limit theta_3(0,0)=1.
    def transformed_integrand(t: mp.mpf) -> mp.mpf:
        if not t:
            return mp.mpf(1)
        # Directly sum theta_3=1+2*sum(exp(-n^2/t)).  On 0<t<=1 the
        # omitted tail after n=20 is below 2*exp(-441), far beneath the
        # working precision, and avoids the tiny-nome jtheta overflow.
        return mp.mpf(1) + 2 * mp.fsum(
            mp.e ** (-(n * n) / t) for n in range(1, 21)
        )

    return mp.quad(transformed_integrand, [0, 1])


def cpsi_series(nmax: int = 40, dps: int = 50) -> mp.mpf:
    mp.mp.dps = dps
    total = mp.mpf(1)
    for n in range(1, nmax + 1):
        a = mp.mpf(n * n)
        total += 2 * (mp.e ** (-a) - a * mp.e1(a))
    return total


def spectral_checks() -> dict[str, bool]:
    ci = cpsi_integral()
    cs = cpsi_series()
    expected = mp.mpf("1.3034102518592793083762365147875847838216766094408744")
    ratio_n8 = mp.sqrt(8 * ci / (96 * mp.pi**2))
    return {
        "proper_time_prefactor": analytic_prefactor_check(),
        "cpsi_integral_value": abs(ci - expected) < mp.mpf("1e-40"),
        "cpsi_series_matches_integral": abs(ci - cs) < mp.mpf("1e-40"),
        "n8_planck_ratio": abs(ratio_n8 - mp.mpf("0.1049059378244545")) < mp.mpf("1e-15"),
        "minimal_boson_sign_positive_G": (1 - 6 * 0) > 0,
    }


def all_checks() -> dict[str, bool]:
    return {**auxiliary_checks(), **spectral_checks()}


def main() -> int:
    checks = all_checks()
    for name, ok in checks.items():
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print("[INFO] C_psi =", mp.nstr(cpsi_integral(), 24))
    print("[INFO] This verifier does not derive N_B, xi, the cutoff, or the UBT path-integral measure.")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
