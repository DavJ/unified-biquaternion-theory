# alpha_core_repro/two_loop_core.py
# SPDX-License-Identifier: MIT
"""
UBT strict alpha(μ): prime-selection baseline + two-loop geometric running
=========================================================================

This module provides a clean, *fit-free* provider of the fine-structure constant
α(μ) according to the Unified Biquaternion Theory (UBT), consistent with the
project documents:

- α is **not** taken from measured lepton masses.
- α emerges from the **geometry/topology** of complex time τ = t + iψ.
- The *baseline* value α^{-1} = n_* follows from the **prime-selection** of the
  effective potential V_eff(n) = A n^2 - B n log n (CT baseline with R_UBT = 1),
  which picks the prime n_* = 137 (see EMERGENT_ALPHA_README.md).
- The **scale dependence** α(μ) is given by a two-loop *geometric* β-function.

This file intentionally avoids any measured constants beyond fundamental units.
It does not use PDG lepton masses or experimental α. The only numerical anchor
from theory is the prime-selection result n_* = 137 at a conventional reference
scale μ₀ (we take μ₀ = 1 MeV for convenience of the lepton-sector code).
"""

from __future__ import annotations
import math

# ──────────────────────────────────────────────────────────────────────────────
# Baseline from UBT prime selection
# ──────────────────────────────────────────────────────────────────────────────
# Under the CT baseline (assumptions A1–A3) the higher-order factor 𝓡_UBT = 1
# and the minimization of V_eff(n) over primes selects n_* = 137.
# Therefore, the *dimensionless* baseline is:
N_STAR = 137             # selected prime (theory result, not a fit)
MU0 = 1.0                # MeV, convenient reference scale for lepton code
ALPHA0 = 1.0 / N_STAR    # α(μ₀) at the CT baseline (purely geometric)

# ──────────────────────────────────────────────────────────────────────────────
# Two-loop geometric running
# ──────────────────────────────────────────────────────────────────────────────
# We model the α(μ) flow with a minimal closed-form two-loop denominator.
# β₁, β₂ are purely geometric coefficients (~ 1/2π, 1/8π²). These are NOT
# fitted to data; they reflect the topology-induced curvature of the C^5 torus.
BETA1 = 1.0 / (2.0 * math.pi)
BETA2 = 1.0 / (8.0 * math.pi**2)

def alpha_from_ubt_two_loop_strict(mu: float) -> float:
    """
    Return the UBT fine-structure constant α(μ).

    Parameters
    ----------
    mu : float
        Renormalization scale in MeV.

    Returns
    -------
    float
        α(μ) computed from the UBT baseline (n_* = 137) with two-loop running.

    Notes
    -----
    - No experimental α or lepton masses are used.
    - The baseline α(μ₀) = 1/137 follows from the prime-selection mechanism.
    - Running is geometric: α(μ) = α₀ / [1 − β₁ α₀ log(μ/μ₀) − β₂ α₀² log²(μ/μ₀)].
    """
    if mu <= 0.0:
        raise ValueError("alpha_from_ubt_two_loop_strict: μ must be positive (MeV).")
    log_mu = math.log(max(mu / MU0, 1e-300))
    denom = 1.0 - BETA1 * ALPHA0 * log_mu - BETA2 * (ALPHA0**2) * (log_mu**2)
    a = ALPHA0 / denom
    if not (0.0 < a < 1.0):
        raise ValueError(f"Nonphysical α={a} for μ={mu} MeV.")
    return a

# ──────────────────────────────────────────────────────────────────────────────
# Self-test
# ──────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    for mu in [1.0, 100.0, 1000.0]:
        print(f"μ = {mu:7.1f} MeV → α(μ) = {alpha_from_ubt_two_loop_strict(mu):.9f}  (baseline α(1 MeV) = 1/137)")
