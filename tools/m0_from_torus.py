#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
m0_from_torus.py — Stationary conditions on the (t,ψ)-torus without α as input.

Task 2 (UBT Copilot Instructions File E):
  Solve the two stationarity conditions for ℰ_cell(R_t, R_ψ) INDEPENDENTLY
  (without imposing α = R_t/R_ψ as a constraint), then compute α_predicted
  = R_t*/R_ψ* as an OUTPUT.  Check whether α_predicted ≈ 1/137.

Problem formulation [SKETCH — §E.4 reformulation]:
  The cell energy on the (t,ψ) torus is [POSTULATE — Eq. E.4]:

      ℰ_cell(R_t, R_ψ) = A·(n²/R_ψ² + ω²/R_t²) + U_geom(R_t, R_ψ)

  where
      A > 0           — kinetic coefficient [DERIVED: A = ℏ²/(2m_field R_ψ²)]
      U_geom          — curvature functional from ℒ_geom
      n = 1           — lowest harmonic (electron)
      ω               — mode frequency (related to m_0 via on-shell condition)

  Stationarity WITHOUT imposing α = R_t/R_ψ:

      ∂ℰ_cell/∂R_t = 0      (i)
      ∂ℰ_cell/∂R_ψ = 0      (ii)

  Solution gives R_t*, R_ψ*, and then:
      α_predicted = R_t*/R_ψ*     [OUTPUT — not input]

Geometric potential forms [SKETCH — requires derivation from ℒ_geom]:
  Three candidate forms are tested (see canonical/geometry/biquaternion_curvature.tex):

    Form A:  U_geom = −C/(R_t · R_ψ)        (inverse-product, attractive)
    Form B:  U_geom = C·(1/R_t² + 1/R_ψ²)   (sum of curvatures, repulsive)
    Form C:  U_geom = C/R_ψ² + D/R_t²       (anisotropic curvature)

  Form A is the simplest and is worked out analytically.
  Forms B and C are treated numerically.

On-shell condition [DERIVED — dispersion on torus]:
    ω_⋆ = m_0 · R_t    (frequency for rest mass m_0 on S¹_t of radius R_t)

  Substituting: ω² = m_0²·R_t²  in (i) and (ii).

Circular-logic check:
  Inputs:  A, C (or C, D for Form C) — geometric coefficients
           n = 1  — lowest harmonic
           m_0   — mass scale (independent of α in this derivation)
  α enters ONLY through α_predicted = R_t*/R_ψ*, as an OUTPUT.
  If α_predicted ≈ 1/137, this constrains C/A ≈ 2/137 — a prediction
  for the curvature-to-kinetic ratio.

Classification labels:
    [POSTULATE]  — assumed axiom
    [DERIVED]    — follows by calculation
    [CALIBRATED] — parameter matched to data
    [SKETCH]     — outline only; full derivation pending
    [DEAD END]   — proved to fail

Layer: [L1] — biquaternionic geometry (no SM input, no QED)
References:
    appendix_E_m0_derivation_strict.tex §E.4 (reformulated)
    canonical/geometry/biquaternion_curvature.tex
"""

from __future__ import annotations

import math
import sys
from typing import Optional, Tuple

# ---------------------------------------------------------------------------
# Physical constants
# ---------------------------------------------------------------------------

ALPHA_EXP = 1.0 / 137.035999177  # CODATA 2022
M_0_MEV = 0.509856               # [CALIBRATED — param A, STATUS_FERMIONS.md]
M_E_MEV = 0.510999               # PDG

# ---------------------------------------------------------------------------
# Form A: U_geom = −C/(R_t · R_ψ)  [SKETCH — simplest attractive curvature]
# ---------------------------------------------------------------------------


def solve_form_A(A_coeff: float, C_coeff: float, n: int = 1) -> dict:
    """
    Solve stationarity conditions for U_geom = −C/(R_t·R_ψ).

    ℰ_cell = A·(n²/R_ψ² + ω²/R_t²) − C/(R_t·R_ψ)

    ∂ℰ/∂R_t = −2A·ω²/R_t³ + C/(R_t²·R_ψ) = 0   ...(i)
    ∂ℰ/∂R_ψ = −2A·n²/R_ψ³ + C/(R_t·R_ψ²) = 0   ...(ii)

    Multiply (i) by R_t³:   −2A·ω² + C·R_t/R_ψ = 0  →  R_t/R_ψ = 2A·ω²/C
    Multiply (ii) by R_ψ³:  −2A·n²  + C·R_ψ/R_t = 0  →  R_ψ/R_t = 2A·n²/C

    Product: (R_t/R_ψ)·(R_ψ/R_t) = 1  →  (2A·ω²/C)·(2A·n²/C) = 1
    → ω·n = C/(2A)   [DERIVED]

    For n=1: ω_⋆ = C/(2A).

    On-shell condition ω = m_0·R_t (natural units ℏ=c=1):
    → m_0·R_t = C/(2A)  →  R_t* = C/(2A·m_0)

    From (ii): R_ψ* = 2A·n²·R_t*/C = n²/m_0  (for n=1: R_ψ* = 1/m_0)

    α_predicted = R_t*/R_ψ* = [C/(2A·m_0)] / (n²/m_0) = C/(2A·n²)

    For n=1: α_predicted = C/(2A)   [DERIVED — depends on ratio C/A]

    Cell energy at the minimum:
    ℰ_cell* = A·(n²·m_0² + m_0²) − C·m_0²·2A/C = A·m_0²·(n²+1) − 2A·m_0²
             = A·m_0²·(n²−1)

    For n=1: ℰ_cell* = 0  → m_0 = ℰ_cell/(2π) = 0  [DEAD END: trivial mass]
    The on-shell condition ω = m_0·R_t with U_geom = −C/(R_t·R_ψ) yields
    zero energy for n=1.  An independent dimensionful scale is required.

    [SKETCH — α_predicted is derived but m_0 prediction is trivial for n=1]
    """
    if C_coeff <= 0:
        return {"error": "C must be positive for Form A"}

    # On-shell frequency: from ω·n = C/(2A) [DERIVED] → ω = C/(2A·n)
    # For n=1 this gives ω = C/(2A); division by n is correct for general n.
    omega_star = C_coeff / (2.0 * A_coeff * n)

    # Stationary radii (in units where m_0 = 1)
    # R_t* = C/(2A·m_0),  R_psi* = n²/m_0  (dimensionless: m_0=1)
    R_t_star_over_m0_inv = C_coeff / (2.0 * A_coeff)  # R_t* × m_0
    R_psi_star_over_m0_inv = float(n * n)             # R_ψ* × m_0

    alpha_predicted = R_t_star_over_m0_inv / R_psi_star_over_m0_inv
    # = C/(2A·n²)

    # Cell energy at minimum (in units where A=1, m_0=1)
    E_cell_star = A_coeff * (n * n - 1)  # = A·m_0²·(n²-1) at m_0=1
    m0_from_energy = E_cell_star / (2.0 * math.pi)

    return {
        "form": "A",
        "U_geom": "−C/(R_t·R_ψ)",
        "omega_star": omega_star,
        "R_t_star_m0": R_t_star_over_m0_inv,   # R_t* × m_0
        "R_psi_star_m0": R_psi_star_over_m0_inv,  # R_ψ* × m_0
        "alpha_predicted": alpha_predicted,
        "E_cell_star": E_cell_star,
        "m0_from_energy": m0_from_energy,
        "status_alpha": "DERIVED — α = C/(2A·n²); requires C/A ~ 2/137 from geometry",
        "status_m0": "DEAD END — ℰ_cell* = 0 for n=1; trivial mass, needs extra scale",
    }


# ---------------------------------------------------------------------------
# Form B: U_geom = C·(1/R_t² + 1/R_ψ²)  [SKETCH — curvature sum]
# ---------------------------------------------------------------------------


def solve_form_B(A_coeff: float, C_coeff: float, n: int = 1,
                 m0: float = 1.0) -> dict:
    """
    Solve stationarity for U_geom = C·(1/R_t² + 1/R_ψ²).

    ℰ_cell = A·(n²/R_ψ² + ω²/R_t²) + C·(1/R_t² + 1/R_ψ²)

    ∂ℰ/∂R_t = −2(A·ω² + C)/R_t³ = 0   → A·ω² + C = 0  [requires C < 0]
    ∂ℰ/∂R_ψ = −2(A·n² + C)/R_ψ³ = 0   → A·n² + C = 0  [requires C = −A·n²]

    Both conditions require C < 0 and A·ω² = −C = A·n², i.e., ω = n.
    But then ∂²ℰ/∂R_t² = 6(A·ω²+C)/R_t⁴ = 0 — flat in R_t direction.
    No true minimum; R_t is undetermined.   [DEAD END]

    [DEAD END — Form B does not produce a stable minimum for R_t]
    """
    if n == 1:
        omega_needed = math.sqrt(max(0.0, -C_coeff / A_coeff)) if C_coeff < 0 else None
        C_needed = -A_coeff * n * n
        return {
            "form": "B",
            "U_geom": "C·(1/R_t² + 1/R_ψ²)",
            "omega_needed": omega_needed,
            "C_needed_for_stationarity": C_needed,
            "status": "DEAD END — stationarity requires C = −A·n², R_t undetermined",
        }
    return {"form": "B", "status": "DEAD END — no stable minimum"}


# ---------------------------------------------------------------------------
# Form C: U_geom = C/R_ψ² + D/R_t²  [anisotropic curvature]
# ---------------------------------------------------------------------------


def solve_form_C(
    A_coeff: float, C_coeff: float, D_coeff: float, n: int = 1, m0: float = 1.0
) -> dict:
    """
    Solve stationarity for U_geom = C/R_ψ² + D/R_t².

    ℰ_cell = (A·ω² + D)/R_t² + (A·n² + C)/R_ψ²

    ∂ℰ/∂R_t = −2(A·ω² + D)/R_t³ = 0   → (A·ω² + D) = 0
    ∂ℰ/∂R_ψ = −2(A·n² + C)/R_ψ³ = 0   → (A·n² + C) = 0

    Same issue as Form B: both conditions require negative coefficients
    and leave R_t, R_ψ undetermined.   [DEAD END]

    Only escapes if D < 0 (kinetic term dominates) AND we use the
    on-shell condition ω = m_0·R_t to promote ω to a function of R_t.

    With ω = m_0·R_t:
        ℰ_cell = A·m_0²·R_t²/R_t² + D/R_t² + (A·n² + C)/R_ψ²
               = A·m_0² + D/R_t² + (A·n² + C)/R_ψ²

    ∂ℰ/∂R_t = −2D/R_t³ = 0  → D = 0  (trivial) or R_t → ∞

    [DEAD END — on-shell condition removes R_t from non-trivial stationarity]
    """
    return {
        "form": "C",
        "U_geom": "C/R_ψ² + D/R_t²",
        "status": (
            "DEAD END — stationarity conditions are scale-free; "
            "on-shell condition ω = m_0·R_t removes R_t dependence"
        ),
    }


# ---------------------------------------------------------------------------
# Summary of α prediction from Form A
# ---------------------------------------------------------------------------


def alpha_from_torus_summary() -> None:
    """
    Print summary table: α_predicted = C/(2A) for different C/A ratios.

    The question is: what value of C/A gives α_predicted = 1/137?
    Answer: C/A = 2·α ≈ 2/137 ≈ 0.01460.

    This is a PREDICTION for the ratio of curvature-to-kinetic coefficients.
    Without independently computing C from ℒ_geom, this is a [SKETCH].
    """
    print()
    print("α_predicted = C/(2A) as function of C/A ratio [DERIVED — Form A]:")
    print(f"  {'C/A ratio':<15}  {'α_pred':>10}  {'1/α_pred':>10}  {'Error vs α_exp%':>16}")
    print("  " + "-" * 55)
    for c_over_a in [0.014, 0.0146, ALPHA_EXP * 2, 0.015, 0.016, 0.020]:
        alpha_pred = c_over_a / 2.0
        err = abs(alpha_pred - ALPHA_EXP) / ALPHA_EXP * 100.0
        flag = "← exact" if abs(c_over_a - 2 * ALPHA_EXP) < 1e-8 else ""
        print(f"  {c_over_a:<15.6f}  {alpha_pred:>10.6f}  {1/alpha_pred:>10.3f}  {err:>14.3f}%  {flag}")
    print()
    print(f"  Required C/A for α = α_exp: C/A = 2·α_exp = {2*ALPHA_EXP:.8f}")
    print(f"  This is a constraint on the ratio of curvature-to-kinetic")
    print(f"  coefficients, derivable from ℒ_geom (currently [SKETCH]).")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    print("=" * 70)
    print("UBT torus stationarity — m_0 and α from geometry  [SKETCH — §E.4]")
    print("=" * 70)
    print()
    print("Approach: Solve ∂ℰ_cell/∂R_t = 0 and ∂ℰ_cell/∂R_ψ = 0 independently.")
    print("α = R_t*/R_ψ* is the OUTPUT, not an input.")
    print()
    print("Circular-logic status:")
    print("  Inputs:  A (kinetic coeff.), C (curvature coeff.), n, m_0")
    print("  Output:  α_predicted = R_t*/R_ψ*")
    print("  α does NOT enter the stationarity conditions directly.  ✓")
    print("  (α enters only if C itself depends on α — see §E.4 discussion)")
    print()

    # ── Form A ──────────────────────────────────────────────────────────
    print("─" * 70)
    print("Form A:  U_geom = −C/(R_t · R_ψ)   [SKETCH — simplest curvature]")
    print()

    # Use C/A = 2·α_exp to show what happens when geometry is correct
    C_A_target = 2.0 * ALPHA_EXP        # predicts α = α_exp exactly
    C_A_example = 2.0 / 137.0           # integer approximation

    for label, C_A in [("C/A = 2·α_exp (exact)", C_A_target),
                       ("C/A = 2/137  (integer)", C_A_example)]:
        A = 1.0
        C = C_A * A
        res = solve_form_A(A, C, n=1)
        print(f"  Case {label}:")
        print(f"    R_t*·m_0 = {res['R_t_star_m0']:.6f}  "
              f"(= C/(2A) = {C/(2*A):.6f})")
        print(f"    R_ψ*·m_0 = {res['R_psi_star_m0']:.6f}  (= 1 for n=1)")
        alpha_pred = res["alpha_predicted"]
        err = abs(alpha_pred - ALPHA_EXP) / ALPHA_EXP * 100.0
        print(f"    α_predicted = {alpha_pred:.8f}  (1/α = {1/alpha_pred:.3f}, "
              f"error = {err:.3f}%)")
        print(f"    ℰ_cell* = {res['E_cell_star']:.6f}  "
              f"→ m_0_from_energy = {res['m0_from_energy']:.6f}")
        print(f"    α status : {res['status_alpha']}")
        print(f"    m_0 status: {res['status_m0']}")
        print()

    # ── Form B ──────────────────────────────────────────────────────────
    print("─" * 70)
    print("Form B:  U_geom = C·(1/R_t² + 1/R_ψ²)   [curvature sum]")
    res_B = solve_form_B(1.0, -1.0, n=1)
    print(f"  Status: {res_B['status']}")
    print()

    # ── Form C ──────────────────────────────────────────────────────────
    print("─" * 70)
    print("Form C:  U_geom = C/R_ψ² + D/R_t²   [anisotropic curvature]")
    res_C = solve_form_C(1.0, -1.0, -1.0, n=1)
    print(f"  Status: {res_C['status']}")
    print()

    # ── Summary table ─────────────────────────────────────────────────
    print("─" * 70)
    alpha_from_torus_summary()

    # ── Overall verdict ─────────────────────────────────────────────────
    print("─" * 70)
    print("VERDICT [SKETCH]:")
    print()
    print("  Form A (U_geom = −C/(R_t·R_ψ)) is the only form that yields")
    print("  a non-trivial α prediction:")
    print()
    print("    α_predicted = C/(2A·n²)   [DERIVED from stationarity, Form A]")
    print()
    print("  For α_predicted = α_exp ≈ 1/137.036, the curvature-to-kinetic")
    print(f"  ratio must satisfy:  C/A = 2·α_exp = {2*ALPHA_EXP:.8f}")
    print()
    print("  The mass prediction m_0 = ℰ_cell*/(2π):")
    print("    For n=1: ℰ_cell* = 0  →  m_0 = 0   [DEAD END — trivial]")
    print("    For n>1: ℰ_cell* = A·m_0²·(n²−1)  →  circular (m_0 enters)")
    print()
    print("  Conclusion:")
    print("    ✓ α can be expressed as OUTPUT of geometry (α = C/(2A) for n=1)")
    print("    ✗ m_0 prediction is trivial (zero) without an independent scale")
    print("    ✗ C/A ratio must be computed from ℒ_geom to close the argument")
    print()
    print("  Classification: [SKETCH — α formula derived but C/A from geometry pending]")
    print()
    print("See appendix_E_m0_derivation_strict.tex §E.4 for the analytic derivation.")
    print("See canonical/geometry/biquaternion_curvature.tex for U_geom derivation.")


if __name__ == "__main__":
    main()
