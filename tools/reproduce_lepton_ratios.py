#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""

Evaluates multiple candidate formulas for the lepton mass ratios
m_μ/m_e ≈ 207.3 and m_τ/m_μ ≈ 16.9 claimed in Appendix W.

KNOWN ISSUE: The canonical Appendix W2 formula (E_{n,m} = (1/R) *
sqrt((n+delta)^2 + (m+delta')^2)) produces eigenvalue *ratios* of order ~1,
not ~207 and ~16.9. See reports/lepton_audit/inventory.md for the full
forensic analysis. This script documents that discrepancy for transparency.

Usage:
    python tools/reproduce_lepton_ratios.py [--variant VARIANT]

Variants:
    canonical          (default) Formula W.2 as written in Appendix W
    candidate_integer  Old Appendix N "integer mode law": m = n × m_e
    candidate_hopf     ThetaM_MassHierarchy: m = a × n^p (Hopf charge model)
    all                Run all variants

Each variant prints:
  - Exact formula used
  - All parameters (calibrated vs fixed)
  - Computed ratios
  - Verdict (REPRODUCED / MISMATCH / NOT_A_PREDICTION)

Exit codes (for --variant canonical or default):
    0 — ratios reproduce the claim within 1 %
    1 — ratios do NOT reproduce the claim (mismatch is documented on stdout)

Exit codes (for --variant all):
    0 — at least one variant reproduces both ratios
    1 — no variant reproduces both ratios
"""

import argparse
Reproduce lepton mass ratios from UBT toroidal eigenmode conjecture.

This script implements the formula from Appendix W2 (appendix_W2_lepton_spectrum.tex):

    E_{n,m} = (1/R) * sqrt((n + delta)^2 + (m + delta')^2)

with delta = 1/2 (Hosotani shift for Q=-1, theta_H=pi) and delta' = 0 (assumed).

Electron identified with mode (0,1), muon with (0,2), tau with (1,0) or (1,1).

KNOWN ISSUE: The formula as stated produces ratios ~1.8 and ~0.73, NOT the claimed
~207 and ~16.9. See reports/lepton_audit/inventory.md for full forensic analysis.
This script documents that discrepancy for transparency.
"""

import math
import sys


# PDG 2022 experimental values
M_E_MEV = 0.51099895  # electron mass, MeV
M_MU_MEV = 105.6583755  # muon mass, MeV
M_TAU_MEV = 1776.86  # tau mass, MeV

EXP_RATIO_MU_E = M_MU_MEV / M_E_MEV
EXP_RATIO_TAU_MU = M_TAU_MEV / M_MU_MEV


def torus_eigenvalue(n: int, m: int, delta: float = 0.5, delta_prime: float = 0.0) -> float:
    """
    Compute dimensionless eigenvalue E_{n,m} * R from the Appendix W2 Dirac spectrum.

    Args:
        n: First mode number (integer)
        m: Second mode number (integer)
        delta: Hosotani shift along first cycle (default 0.5 for Q=-1, theta_H=pi)
        delta_prime: Shift along second cycle (default 0.0; spin structure dependent)

    Returns:
        Dimensionless eigenvalue sqrt((n+delta)^2 + (m+delta_prime)^2)
    """
    return math.sqrt((n + delta) ** 2 + (m + delta_prime) ** 2)


def compute_ratios(delta: float = 0.5, delta_prime: float = 0.0) -> dict:
    """
    Compute eigenvalue ratios for lepton mass predictions.

    Returns dict with eigenvalues and ratios.
    """
    e01 = torus_eigenvalue(0, 1, delta, delta_prime)
    e02 = torus_eigenvalue(0, 2, delta, delta_prime)
    e10 = torus_eigenvalue(1, 0, delta, delta_prime)
    e11 = torus_eigenvalue(1, 1, delta, delta_prime)

    ratio_mu_e = e02 / e01
    ratio_tau_mu_v1 = e10 / e02   # tau ~ (1,0) mode
    ratio_tau_mu_v2 = e11 / e02   # tau ~ (1,1) alternative

    return {
        "delta": delta,
        "delta_prime": delta_prime,
        "E(0,1)": e01,
        "E(0,2)": e02,
        "E(1,0)": e10,
        "E(1,1)": e11,
        "ratio_mu_e": ratio_mu_e,
        "ratio_tau_mu_v1": ratio_tau_mu_v1,
        "ratio_tau_mu_v2": ratio_tau_mu_v2,
    }


def main():
    print("=" * 65)
    print("UBT Lepton Mass Ratio Reproduction Script")
    print("Formula: E_{n,m} = (1/R) sqrt((n+delta)^2 + (m+delta')^2)")
    print("Based on Appendix W2 (appendix_W2_lepton_spectrum.tex)")
    print("=" * 65)
    print()

    # Default parameters from Appendix W2
    delta = 0.5
    delta_prime = 0.0

    r = compute_ratios(delta, delta_prime)

    print(f"Parameters: delta = {r['delta']}, delta' = {r['delta_prime']}")
    print()
    print("Eigenvalues (dimensionless, in units of 1/R):")
    print(f"  E(0,1) = {r['E(0,1)']:.6f}  [electron = first non-trivial mode]")
    print(f"  E(0,2) = {r['E(0,2)']:.6f}  [muon candidate]")
    print(f"  E(1,0) = {r['E(1,0)']:.6f}  [tau candidate v1]")
    print(f"  E(1,1) = {r['E(1,1)']:.6f}  [tau candidate v2]")
    print()

    print("Computed ratios:")
    print(f"  m_mu/m_e = E(0,2)/E(0,1) = {r['ratio_mu_e']:.4f}")
    print(f"  m_tau/m_mu = E(1,0)/E(0,2) = {r['ratio_tau_mu_v1']:.4f}  [tau ~ (1,0)]")
    print(f"  m_tau/m_mu = E(1,1)/E(0,2) = {r['ratio_tau_mu_v2']:.4f}  [tau ~ (1,1)]")
    print()

    print("Experimental values (PDG 2022):")
    print(f"  m_mu/m_e = {EXP_RATIO_MU_E:.4f}")
    print(f"  m_tau/m_mu = {EXP_RATIO_TAU_MU:.4f}")
    print()

    # Check mismatch
    mismatch_mu_e = abs(r['ratio_mu_e'] - EXP_RATIO_MU_E) / EXP_RATIO_MU_E * 100
    mismatch_tau_mu = abs(r['ratio_tau_mu_v1'] - EXP_RATIO_TAU_MU) / EXP_RATIO_TAU_MU * 100

    print("Discrepancies:")
    print(f"  m_mu/m_e:  {r['ratio_mu_e']:.4f} vs {EXP_RATIO_MU_E:.4f} "
          f"  => {mismatch_mu_e:.1f}% mismatch")
    print(f"  m_tau/m_mu: {r['ratio_tau_mu_v1']:.4f} vs {EXP_RATIO_TAU_MU:.4f} "
          f"  => {mismatch_tau_mu:.1f}% mismatch")
    print()

    # Diagnosis
    print("=" * 65)
    print("DIAGNOSIS")
    print("=" * 65)
    if mismatch_mu_e > 10.0 or mismatch_tau_mu > 10.0:
        print()
        print("FAILURE: Formula does NOT reproduce claimed ratios ~207 and ~16.9.")
        print()
        print("The eigenvalue ratios from the Appendix W formula are of order ~1,")
        print("not ~200 or ~17. The claimed values '207.3' and '16.9' in Appendix W")
        print("are the EXPERIMENTAL values, not computed predictions.")
        print()
        print("Status: The toroidal eigenmode derivation is a CONJECTURE.")
        print("        A corrected formula or derivation is required.")
        print("        See reports/lepton_audit/inventory.md for full analysis.")
        return 1
    else:
        print("OK: Formula reproduces experimental ratios within 10%.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
