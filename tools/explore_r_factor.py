#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
explore_r_factor.py — Approach B2: Numerical exploration of R ≈ 1.114.

PURPOSE
-------
Tests whether the correction factor R ≈ 1.114 in

    B = B_base × R = N_eff^{3/2} × R ≈ 41.57 × 1.114 ≈ 46.3

can be expressed as a simple algebraic combination of N_eff = 12 and
standard mathematical constants (π, e, √2, √3, ...).

METHOD
------
Evaluates a large set of candidate expressions f(N_eff) and reports:
  - MATCH  if |f - R_target| / R_target < 0.1%
  - CLOSE  if |f - R_target| / R_target < 1.0%
  - FAR    otherwise

No circular inputs: R_target = 1.114 is taken from phenomenology
(calibrated on n*=137, the topological winding number, NOT from α=1/137).

INPUTS
------
  N_eff    = 12      [PROVED]
  R_target = 1.114   [EMPIRICAL] correction factor (Open Problem B)

OUTPUTS
-------
  Table of candidates sorted by absolute error.
  Summary of closest match.
  Classification: MATCH / CLOSE / NUMERICAL OBSERVATION / DEAD END.

REFERENCES
----------
  - DERIVATION_INDEX.md "Fine Structure Constant"
  - docs/PROOFKIT_ALPHA.md §5
  - consolidation_project/alpha_derivation/r_factor_geometry.tex (B1 + B3)

USAGE
-----
    python tools/explore_r_factor.py
"""

from __future__ import annotations

import math
from typing import Dict


# ─── Constants ───────────────────────────────────────────────────────────────

N: int = 12         # [PROVED] N_eff
R_TARGET: float = 1.114   # [EMPIRICAL] correction factor
PI = math.pi
E  = math.e


# ─── Candidate expressions ───────────────────────────────────────────────────

def build_candidates() -> Dict[str, float]:
    """Return a dictionary of {name: value} for all R candidates."""
    cands: Dict[str, float] = {}

    # Simple exponentials involving N
    cands["exp(1/N)"]              = math.exp(1 / N)
    cands["exp(1/(N-1))"]          = math.exp(1 / (N - 1))
    cands["exp(2/N)"]              = math.exp(2 / N)
    cands["exp(1/(2*sqrt(N)))"]    = math.exp(1 / (2 * math.sqrt(N)))
    cands["exp(1/(sqrt(N)*pi))"]   = math.exp(1 / (math.sqrt(N) * PI))
    cands["exp(1/(N*pi))"]         = math.exp(1 / (N * PI))
    cands["exp(pi/N^2)"]           = math.exp(PI / N**2)

    # Roots of 2
    cands["2^(1/6)"]               = 2 ** (1/6)   # sixth root of 2
    cands["2^(1/8)"]               = 2 ** (1/8)
    cands["2^(1/5)"]               = 2 ** (1/5)
    cands["2^(1/4)"]               = 2 ** (1/4)

    # Roots of pi and e
    cands["pi^(1/12)"]             = PI ** (1/12)
    cands["pi^(1/8)"]              = PI ** (1/8)
    cands["e^(1/8)"]               = E ** (1/8)
    cands["e^(1/12)"]              = E ** (1/12)

    # Simple rational
    cands["(N+1)/N"]               = (N + 1) / N
    cands["(N+2)/N"]               = (N + 2) / N
    cands["(2*N+1)/(2*N)"]         = (2*N + 1) / (2*N)
    cands["sqrt(1+1/N)"]           = math.sqrt(1 + 1/N)
    cands["(1+1/N)^(1/2)"]         = (1 + 1/N) ** 0.5
    cands["(1+1/N)^(3/4)"]         = (1 + 1/N) ** 0.75

    # Pi-based
    cands["1+1/(4*pi)"]            = 1 + 1 / (4 * PI)
    cands["1+1/(3*pi)"]            = 1 + 1 / (3 * PI)
    cands["1+pi/(4*N)"]            = 1 + PI / (4 * N)
    cands["1+1/sqrt(N)/pi"]        = 1 + 1 / (math.sqrt(N) * PI)

    # Square-root combos
    cands["1+1/(2*sqrt(N))"]       = 1 + 1 / (2 * math.sqrt(N))
    cands["1+1/(3*sqrt(N))"]       = 1 + 1 / (3 * math.sqrt(N))
    cands["(N+sqrt(N))/(N+1)"]     = (N + math.sqrt(N)) / (N + 1)

    # N^(small fraction)
    cands["N^(1/12)"]              = N ** (1/12)
    cands["N^(1/16)"]              = N ** (1/16)

    # Mixed
    cands["sqrt(2)/2^(5/12)"]      = math.sqrt(2) / 2**(5/12)
    cands["(N+pi)/(N+2)"]          = (N + PI) / (N + 2)
    cands["N/(N-1) × pi/(pi+1)"]   = (N / (N-1)) * PI / (PI + 1)

    # Two-loop approach: 1 + alpha * f(N)
    alpha = 1.0 / 137.0
    for fname, fval in [
        ("N_eff",         N),
        ("N_eff+pi",      N + PI),
        ("N_eff+pi+1/4",  N + PI + 0.25),
        ("N_eff^(3/2)/e", N**1.5 / E),
        ("N_eff*5/4",     N * 1.25),
        ("4*pi",          4 * PI),
    ]:
        cands[f"1+alpha×{fname}"] = 1 + alpha * fval

    return cands


# ─── Main ────────────────────────────────────────────────────────────────────

def main() -> None:
    print("=" * 65)
    print("UBT R Factor — Approach B2: Algebraic Candidate Search")
    print("=" * 65)
    print()
    print(f"N_eff    = {N}")
    print(f"R_target = {R_TARGET}  [EMPIRICAL] Open Problem B")
    print()

    cands = build_candidates()

    # Sort by absolute error
    results = []
    for name, val in cands.items():
        if not math.isfinite(val):
            continue
        err_abs = abs(val - R_TARGET)
        err_pct = err_abs / R_TARGET * 100
        results.append((name, val, err_abs, err_pct))

    results.sort(key=lambda t: t[2])

    print(f"{'Candidate':<35} {'Value':>10} {'|err|':>8} {'% err':>8}  Label")
    print("-" * 75)
    for name, val, err_abs, err_pct in results[:30]:  # top 30
        if err_pct < 0.1:
            label = "[MATCH]"
        elif err_pct < 1.0:
            label = "[CLOSE]"
        else:
            label = ""
        print(f"{name:<35} {val:10.6f} {err_abs:8.5f} {err_pct:7.3f}%  {label}")

    print()
    # Best match
    best_name, best_val, best_err_abs, best_err_pct = results[0]
    print("─" * 65)
    print("BEST MATCH:")
    print(f"  {best_name} = {best_val:.8f}")
    print(f"  |R_target - best| = {best_err_abs:.6f}  ({best_err_pct:.3f}%)")
    print()

    # Classification
    print("─" * 65)
    print("CLASSIFICATION:")
    if best_err_pct < 0.1:
        print(f"  [MATCH] {best_name} ≈ R_target to {best_err_pct:.3f}%")
        print("  → Potential algebraic identification; seek derivation from S[Θ].")
    elif best_err_pct < 1.0:
        print(f"  [NUMERICAL OBSERVATION] Best candidate: {best_name} ≈ {best_val:.6f}")
        print(f"  Error {best_err_pct:.2f}% < 1.0% — motivates algebraic investigation.")
        print("  Status: [NUMERICAL OBSERVATION], not [PROVED].")
    else:
        print(f"  No algebraic combination tested here reproduces R within 1%.")
        print(f"  Best: {best_name} = {best_val:.6f}, err = {best_err_pct:.2f}%")
        print("  Status: [OPEN PROBLEM B] — R origin remains unknown.")

    print()
    print("─" * 65)
    print("NOTE ON 2^(1/6):")
    val_sixth = 2 ** (1/6)
    err_sixth = abs(val_sixth - R_TARGET) / R_TARGET * 100
    print(f"  2^(1/6) = {val_sixth:.8f},  error = {err_sixth:.3f}%")
    print("  Possible structural origin:")
    print("    6 = N_phases × N_helicity = 3 × 2  (from N_eff factorisation)")
    print("    6 = dim_R(Im(C⊗H)) - 1 = 7 - 1")
    print("  Without a derivation from S[Θ], this is [NUMERICAL OBSERVATION].")
    print()


if __name__ == "__main__":
    main()
