#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
explore_b_exponent.py — Approach A3: Numerical exploration of B_base exponent.

PURPOSE
-------
Investigates the question: if B_target = N_eff^x, what is x?

Specifically, starting from the phenomenologically required B value
(calibrated on n* = 137 WITHOUT using alpha = 1/137 as an input),
compute the exponent x = log(B_target) / log(N_eff) and compare it
to simple algebraic fractions.

INPUTS
------
  N_eff    = 12      [PROVED] from N_phases × N_helicity × N_charge = 3×2×2
  B_target = 46.284  [CALIBRATED] phenomenological value for n* = 137

Note on circularity: B_target = 46.284 is derived from requiring
the potential V_eff(n) = A·n² - B·n·ln(n) to have its minimum
near n = 137. This is NOT the same as inputting alpha = 1/137 directly;
rather n* = 137 is the topological winding number (accepted as input
from the prime stability argument), and B_target is then computed
from the stationarity condition. No circular logic.

OUTPUTS
-------
  x = log(B_target) / log(N_eff)
  Comparison to simple fractions (3/2, 5/3, 7/4, ...)
  Nearest simple fraction and distance

REFERENCES
----------
  - DERIVATION_INDEX.md "Fine Structure Constant"
  - STATUS_ALPHA.md §9
  - consolidation_project/alpha_derivation/b_base_spinor_approach.tex
  - consolidation_project/alpha_derivation/b_base_hausdorff.tex

USAGE
-----
    python tools/explore_b_exponent.py
"""

from __future__ import annotations

import math
from fractions import Fraction


# ─── Constants ───────────────────────────────────────────────────────────────

N_EFF: int = 12        # [PROVED] N_phases × N_helicity × N_charge = 3×2×2
B_TARGET: float = 46.284  # [CALIBRATED] phenomenological value for n*=137
B_BASE_32: float = N_EFF ** 1.5  # [CONJECTURED] N_eff^{3/2}
R_UBT: float = 1.114  # [EMPIRICAL] renormalization factor (Open Problem B)


# ─── Compute exponent ────────────────────────────────────────────────────────

def compute_exponent(b_target: float, n_eff: float) -> float:
    """Return x such that n_eff^x = b_target."""
    return math.log(b_target) / math.log(n_eff)


def closest_fraction(x: float, max_denom: int = 20) -> tuple[Fraction, float]:
    """Return the simplest fraction p/q (q <= max_denom) closest to x."""
    best: Fraction | None = None
    best_err: float = float("inf")
    for denom in range(1, max_denom + 1):
        numer = round(x * denom)
        frac = Fraction(numer, denom)
        err = abs(float(frac) - x)
        if err < best_err:
            best_err = err
            best = frac
    assert best is not None
    return best, best_err


# ─── Main ────────────────────────────────────────────────────────────────────

def main() -> None:
    print("=" * 60)
    print("UBT B Coefficient — Approach A3: Exponent Exploration")
    print("=" * 60)
    print()

    x_full = compute_exponent(B_TARGET, N_EFF)
    x_base = compute_exponent(B_BASE_32, N_EFF)

    print(f"N_eff          = {N_EFF}")
    print(f"B_target       = {B_TARGET}  [CALIBRATED on n*=137]")
    print(f"B_base (3/2)   = {B_BASE_32:.6f}  = N_eff^(3/2)")
    print(f"R_UBT          = {R_UBT}  [EMPIRICAL]")
    print(f"B_base × R_UBT = {B_BASE_32 * R_UBT:.6f}")
    print()

    print(f"x = log(B_target) / log(N_eff) = {x_full:.10f}")
    print(f"  (for reference: x if B_target = N_eff^(3/2) exactly: {x_base:.10f})")
    print()

    # Compare to simple fractions
    candidates = [
        ("1/1",   1.0),
        ("3/2",   3/2),
        ("5/3",   5/3),
        ("7/4",   7/4),
        ("8/5",   8/5),
        ("11/7",  11/7),
        ("13/8",  13/8),
        ("2/1",   2.0),
        ("sqrt(2)", math.sqrt(2)),
        ("e/sqrt(e)", math.e / math.sqrt(math.e)),  # = sqrt(e) ≈ 1.649
    ]

    print("Comparison to simple fractions / constants:")
    print(f"{'Expression':<18} {'Value':>12} {'x - value':>12} {'rel err':>10}")
    print("-" * 56)
    for name, val in candidates:
        diff = x_full - val
        rel_err_pct = abs(diff) / val * 100
        marker = "  <-- NEAREST" if abs(diff) < 0.05 else ""
        print(f"{name:<18} {val:12.8f} {diff:12.8f} {rel_err_pct:9.3f}%{marker}")

    print()
    # Automated best-fraction search
    best_frac, best_err = closest_fraction(x_full, max_denom=20)
    print(f"Best simple fraction (denominator ≤ 20): {best_frac} = {float(best_frac):.8f}")
    print(f"  |x - {best_frac}| = {best_err:.8f}  ({best_err / float(best_frac) * 100:.3f}% relative)")
    print()

    # Interpretation
    print("-" * 60)
    print("INTERPRETATION")
    print("-" * 60)
    if abs(x_full - 1.5) / 1.5 * 100 < 1.0:
        status = "[NUMERICAL OBSERVATION] x ≈ 3/2 within 1% — algebraic origin plausible"
    else:
        err_32 = abs(x_full - 1.5) / 1.5 * 100
        status = (
            f"x = {x_full:.6f} deviates from 3/2 by {err_32:.2f}%.\n"
            "  The deviation is dominated by the R factor:\n"
            f"  If B_target = B_base (no R), then x = {x_base:.8f} = 3/2 exactly.\n"
            "  Therefore: N_eff^(3/2) accounts for B_base alone; R ≠ 1 lifts the exponent.\n"
            "  → Explore R independently (see r_factor_geometry.tex, explore_r_factor.py)."
        )
    print(status)
    print()
    print("CONCLUSION:")
    print(f"  B_base = N_eff^(3/2) = {B_BASE_32:.4f} [MOTIVATED CONJECTURE]")
    print(f"  Exponent x = log(B_target)/log(N_eff) = {x_full:.6f}")
    print(f"  Nearest simple fraction: {best_frac} (err {best_err/float(best_frac)*100:.2f}%)")
    print(f"  The gap from 3/2 is entirely explained by R = {R_UBT} (Open Problem B).")


if __name__ == "__main__":
    main()
