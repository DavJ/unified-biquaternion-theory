#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
Lepton Mass Ratios — Forensic Reproduction Script
==================================================

Reproduces (or refutes) the claim from Appendix W of the Unified Biquaternion Theory:

    m_μ/m_e ≈ 207.3
    m_τ/m_μ ≈ 16.9

The script evaluates the eigenmode formula given in Appendix W *exactly as written*,
computes all ratios, and compares them to the claimed values.

Parameters used (max 1 calibration):
  - δ  = 0.5          (Hosotani shift along ψ-cycle; Q=−1, θ_H=π)
                       Source: appendix_W2_lepton_spectrum.tex, W.3
  - δ' = 0.0          (spin-structure shift along φ-cycle; implicit in W.T table)
                       Source: appendix_W2_lepton_spectrum.tex, W.T
  - R  = 1/m_e        (single calibration: sets overall energy scale)
                       Source: appendix_W2_lepton_spectrum.tex, W.3

Run from the repository root:
    python tools/reproduce_lepton_ratios.py

Exit codes:
    0 — ratios reproduce the claim within 1 %
    1 — ratios do NOT reproduce the claim (mismatch is documented on stdout)
"""

import math
import sys


# ---------------------------------------------------------------------------
# Parameters — source: appendix_W2_lepton_spectrum.tex
# ---------------------------------------------------------------------------

DELTA = 0.5   # Hosotani shift along ψ-cycle (n-index); W.3
DELTA_PRIME = 0.0  # Shift along φ-cycle (m-index); implicit from W.T table

# Experimental reference masses (PDG 2022), used only for the one calibration and
# for comparison — NOT as hidden free parameters.
M_E_MEV   = 0.51099895    # electron mass [MeV/c²]   PDG 2022
M_MU_MEV  = 105.6583755   # muon mass     [MeV/c²]   PDG 2022
M_TAU_MEV = 1776.86       # tau mass      [MeV/c²]   PDG 2022

# Claimed ratios from Appendix W, section W.5
CLAIMED_MU_OVER_E   = 207.3
CLAIMED_TAU_OVER_MU = 16.9


# ---------------------------------------------------------------------------
# Eigenvalue formula — source: appendix_W2_lepton_spectrum.tex, eq. W.2
# E_{n,m} = (1/R) * sqrt( (n+δ)² + (m+δ')² )
# ---------------------------------------------------------------------------

def eigenvalue(n: int, m: int, delta: float = DELTA, delta_prime: float = DELTA_PRIME) -> float:
    """
    Compute the Dirac eigenvalue on T²(τ) in units of 1/R.

    Formula (eq. W.2, appendix_W2_lepton_spectrum.tex):
        E_{n,m} · R = sqrt( (n + δ)² + (m + δ')² )

    Parameters
    ----------
    n, m       : integer mode numbers
    delta      : Hosotani shift along ψ-cycle (default: 0.5)
    delta_prime: shift along φ-cycle          (default: 0.0)

    Returns
    -------
    Dimensionless value  E_{n,m} · R
    """
    return math.sqrt((n + delta) ** 2 + (m + delta_prime) ** 2)


# ---------------------------------------------------------------------------
# Main computation
# ---------------------------------------------------------------------------

def main() -> int:
    print("=" * 65)
    print("Lepton Mass Ratios — Forensic Reproduction (Appendix W)")
    print("=" * 65)

    # --- Step 1: parameters --------------------------------------------------
    print("\n[1] Parameters")
    print(f"    δ  = {DELTA}  (Hosotani shift, W.3, source: appendix_W2_lepton_spectrum.tex)")
    print(f"    δ' = {DELTA_PRIME}  (spin-structure shift, W.T, source: appendix_W2_lepton_spectrum.tex)")
    print(f"    Calibration: R = 1/m_e  (one calibration, sets overall scale)")
    print(f"    m_e (exp) = {M_E_MEV} MeV/c²  (PDG 2022, reference only)")

    # --- Step 2: eigenvalues (dimensionless, in units of 1/R) ----------------
    print("\n[2] Eigenvalues  E_{n,m} · R  (formula W.2 evaluated exactly)")
    modes = [(0, 1), (0, 2), (1, 0), (1, 1)]
    ev = {}
    for (n, m) in modes:
        ev[(n, m)] = eigenvalue(n, m)
        print(f"    E_({n},{m}) · R  =  sqrt(({n}+{DELTA})² + ({m}+{DELTA_PRIME})²)"
              f"  =  {ev[(n,m)]:.8f}")

    # --- Step 3: ratios as-written -------------------------------------------
    print("\n[3] Ratios from formula (NO additional fits)")
    ratio_mu_e_formula   = ev[(0, 2)] / ev[(0, 1)]
    ratio_tau_mu_10      = ev[(1, 0)] / ev[(0, 2)]   # tau candidate: (1,0)
    ratio_tau_mu_11      = ev[(1, 1)] / ev[(0, 2)]   # tau candidate: (1,1)
    ratio_tau_e_10       = ev[(1, 0)] / ev[(0, 1)]

    print(f"    E_(0,2)/E_(0,1)  =  {ratio_mu_e_formula:.8f}")
    print(f"    E_(1,0)/E_(0,2)  =  {ratio_tau_mu_10:.8f}")
    print(f"    E_(1,1)/E_(0,2)  =  {ratio_tau_mu_11:.8f}")
    print(f"    E_(1,0)/E_(0,1)  =  {ratio_tau_e_10:.8f}")

    # --- Step 4: comparison to Appendix W claims -----------------------------
    print("\n[4] Comparison with Appendix W claims (section W.5)")
    mismatch_mu  = abs(ratio_mu_e_formula  - CLAIMED_MU_OVER_E)   / CLAIMED_MU_OVER_E
    mismatch_tau = abs(ratio_tau_mu_10     - CLAIMED_TAU_OVER_MU)  / CLAIMED_TAU_OVER_MU

    print(f"    m_μ/m_e : formula={ratio_mu_e_formula:.6f}  claimed={CLAIMED_MU_OVER_E}"
          f"  exp={M_MU_MEV/M_E_MEV:.6f}  rel.error={mismatch_mu*100:.1f}%")
    print(f"    m_τ/m_μ : formula={ratio_tau_mu_10:.6f}  claimed={CLAIMED_TAU_OVER_MU}"
          f"  exp={M_TAU_MEV/M_MU_MEV:.6f}  rel.error={mismatch_tau*100:.1f}%")

    TOLERANCE = 0.01  # 1 % tolerance to count as "reproduced"

    reproduced_mu  = mismatch_mu  < TOLERANCE
    reproduced_tau = mismatch_tau < TOLERANCE

    print("\n[5] Verdict")
    if reproduced_mu and reproduced_tau:
        print("    ✓ BOTH ratios reproduce the Appendix W claims within 1 %.")
        print("    The formula is consistent with the stated results.")
        return 0
    else:
        print("    ✗ MISMATCH — the formula does NOT reproduce the claims.")
        print()
        if not reproduced_mu:
            factor = CLAIMED_MU_OVER_E / ratio_mu_e_formula
            print(f"    m_μ/m_e: formula gives {ratio_mu_e_formula:.4f},"
                  f" claim is {CLAIMED_MU_OVER_E}."
                  f" Missing factor ≈ {factor:.1f}.")
        if not reproduced_tau:
            print(f"    m_τ/m_μ: formula gives E_(1,0)/E_(0,2) = {ratio_tau_mu_10:.4f},"
                  f" claim is {CLAIMED_TAU_OVER_MU}.")
            print(f"    Note: E_(1,0) < E_(0,2) in this formula, so ratio < 1.")
            print(f"    This means mode ordering contradicts the mass hierarchy.")
        print()
        print("    See reports/lepton_audit/missing_step.md for analysis.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
