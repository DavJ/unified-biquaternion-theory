#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
Lepton Mass Ratios — Forensic Reproduction Script
==================================================

Evaluates multiple candidate formulas for the lepton mass ratios
m_μ/m_e ≈ 207.3 and m_τ/m_μ ≈ 16.9 claimed in Appendix W.

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
import math
import sys


# ---------------------------------------------------------------------------
# Shared constants
# ---------------------------------------------------------------------------

# Experimental reference masses (PDG 2022) — used only for one calibration
# and for comparison.  NOT hidden free parameters.
M_E_MEV   = 0.51099895    # electron mass [MeV/c²]   PDG 2022
M_MU_MEV  = 105.6583755   # muon mass     [MeV/c²]   PDG 2022
M_TAU_MEV = 1776.86       # tau mass      [MeV/c²]   PDG 2022

EXP_MU_OVER_E   = M_MU_MEV / M_E_MEV    # 206.768283
EXP_TAU_OVER_MU = M_TAU_MEV / M_MU_MEV  # 16.817029

# Former claims from Appendix W, section W.5 (now corrected to "experimental reference")
REF_MU_OVER_E   = 206.768283  # experimental reference (PDG 2022)
REF_TAU_OVER_MU = 16.817029   # experimental reference (PDG 2022)

TOLERANCE = 0.01  # 1% tolerance to count as "reproduced"

SEP = "=" * 65


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _verdict_line(ratio_mu_e: float, ratio_tau_mu: float) -> tuple:
    """Return (reproduced_mu, reproduced_tau, overall_ok)."""
    ok_mu  = abs(ratio_mu_e   - REF_MU_OVER_E)   / REF_MU_OVER_E   < TOLERANCE
    ok_tau = abs(ratio_tau_mu - REF_TAU_OVER_MU)  / REF_TAU_OVER_MU < TOLERANCE
    return ok_mu, ok_tau, ok_mu and ok_tau


# ---------------------------------------------------------------------------
# Variant: canonical
# Formula W.2 as written in appendix_W2_lepton_spectrum.tex
# ---------------------------------------------------------------------------

DELTA       = 0.5   # Hosotani shift along ψ-cycle; W.3
DELTA_PRIME = 0.0   # Spin-structure shift; implicit from W.T table


def _eigenvalue(n: int, m: int, delta: float = DELTA,
                delta_prime: float = DELTA_PRIME) -> float:
    """E_{n,m}·R = sqrt((n+δ)² + (m+δ')²) — Appendix W, eq. W.2."""
    return math.sqrt((n + delta) ** 2 + (m + delta_prime) ** 2)


def run_canonical() -> int:
    """
    Evaluate the Dirac eigenvalue formula exactly as written in Appendix W, eq. W.2.

    Formula:
        E_{n,m} = (1/R) * sqrt( (n+δ)² + (m+δ')² )
    Parameters:
        δ  = 0.5   (Hosotani shift; source: appendix_W2_lepton_spectrum.tex W.3)
        δ' = 0.0   (spin-structure shift; source: W.T table)
        R  = 1/m_e (ONE calibration — overall mass scale)
    Returns exit code 0 if reproduced, 1 if mismatch.
    """
    print(SEP)
    print("VARIANT: canonical  (Appendix W, eq. W.2 as written)")
    print(SEP)
    print("\nFormula: E_{n,m}·R = sqrt( (n + δ)² + (m + δ')² )")
    print(f"\nParameters:")
    print(f"  δ  = {DELTA}   [fixed, Hosotani shift; source: appendix_W2_lepton_spectrum.tex W.3]")
    print(f"  δ' = {DELTA_PRIME}   [fixed, spin-structure;  source: appendix_W2_lepton_spectrum.tex W.T]")
    print(f"  R  = 1/m_e  [CALIBRATION #1 — overall mass scale]")
    print(f"  m_e = {M_E_MEV} MeV/c²  [PDG 2022, reference only]")

    modes = [(0, 1), (0, 2), (1, 0), (1, 1), (0, 3)]
    ev = {(n, m): _eigenvalue(n, m) for (n, m) in modes}

    print("\nEigenvalues E_{n,m}·R:")
    for (n, m) in modes:
        print(f"  E_({n},{m}) = sqrt(({n}+{DELTA})² + ({m}+{DELTA_PRIME})²) = {ev[(n,m)]:.8f}")

    ratio_mu_e  = ev[(0, 2)] / ev[(0, 1)]
    ratio_tau_mu_10 = ev[(1, 0)] / ev[(0, 2)]
    ratio_tau_mu_11 = ev[(1, 1)] / ev[(0, 2)]

    print("\nRatios (NO additional fits):")
    print(f"  E_(0,2)/E_(0,1) = {ratio_mu_e:.8f}   [μ/e candidate]")
    print(f"  E_(1,0)/E_(0,2) = {ratio_tau_mu_10:.8f}   [τ/μ candidate, mode (1,0)]")
    print(f"  E_(1,1)/E_(0,2) = {ratio_tau_mu_11:.8f}   [τ/μ candidate, mode (1,1)]")

    err_mu  = abs(ratio_mu_e      - REF_MU_OVER_E)   / REF_MU_OVER_E
    err_tau = abs(ratio_tau_mu_10 - REF_TAU_OVER_MU)  / REF_TAU_OVER_MU

    print("\nComparison with experimental reference values:")
    print(f"  m_μ/m_e : formula={ratio_mu_e:.6f}  exp={REF_MU_OVER_E:.6f}  "
          f"rel.err={err_mu*100:.1f}%")
    print(f"  m_τ/m_μ : formula={ratio_tau_mu_10:.6f}  exp={REF_TAU_OVER_MU:.6f}  "
          f"rel.err={err_tau*100:.1f}%")

    ok_mu, ok_tau, ok = _verdict_line(ratio_mu_e, ratio_tau_mu_10)
    print("\nVerdict:")
    if ok:
        print("  ✓ REPRODUCED — both ratios within 1% of experimental reference.")
        return 0
    else:
        print("  ✗ MISMATCH — formula does NOT reproduce experimental ratios.")
        if not ok_mu:
            print(f"    m_μ/m_e: formula gives {ratio_mu_e:.4f}, exp is {REF_MU_OVER_E:.4f}."
                  f" Missing factor ≈ {REF_MU_OVER_E/ratio_mu_e:.1f}.")
        if not ok_tau:
            print(f"    m_τ/m_μ: formula gives {ratio_tau_mu_10:.4f},"
                  " ratio < 1 (mode (1,0) is lighter than (0,2) — wrong hierarchy).")
        print("  See reports/lepton_audit/missing_step.md for full analysis.")
        return 1


# ---------------------------------------------------------------------------
# Variant: candidate_integer
# Old Appendix N claim: m_lepton = n × m_e with integer n
# Source: consolidation_project/old/appendix_N_mass_predictions_consolidated.tex
# ---------------------------------------------------------------------------

def run_candidate_integer() -> int:
    """
    Integer mode law: m_lepton = n × m_e.

    Source: consolidation_project/old/appendix_N_mass_predictions_consolidated.tex
    Claim: "leading (no-parameter) predictions are m_μ^(0) = 207 m_e, m_τ^(0) = 3477 m_e"

    Parameters:
        m_e   [CALIBRATION #1 — overall mass scale]
        n_mu  = 207   [NOT a prediction — this IS the rounded experimental ratio]
        n_tau = 3477  [NOT a prediction — this IS the rounded experimental ratio]

    Classification: NOT_A_PREDICTION under the 1-calibration rule.
    The integers 207 and 3477 are themselves calibration parameters
    (second and third free parameters), fitted to the experimental ratios.
    """
    N_MU  = 207    # claimed integer mode number for muon
    N_TAU = 3477   # claimed integer mode number for tau

    print(SEP)
    print("VARIANT: candidate_integer  (Old Appendix N integer mode law)")
    print(SEP)
    print("\nFormula: m_lepton = n × m_e")
    print(f"\nParameters:")
    print(f"  m_e   = {M_E_MEV} MeV/c²  [CALIBRATION #1 — overall mass scale, PDG 2022]")
    print(f"  n_mu  = {N_MU}   [NOT derived — rounded experimental ratio m_μ/m_e ≈ 206.77]")
    print(f"  n_tau = {N_TAU}  [NOT derived — rounded experimental ratio m_τ/m_e ≈ 3477.2]")
    print(f"\n  ⚠  STATUS: NOT_A_PREDICTION")
    print(f"  n_mu and n_tau are additional calibration parameters,")
    print(f"  not derived from any formula. This violates the 1-calibration rule.")

    m_mu_pred  = N_MU  * M_E_MEV
    m_tau_pred = N_TAU * M_E_MEV
    ratio_mu_e  = N_MU
    ratio_tau_mu = N_TAU / N_MU

    print(f"\nPredicted masses (using calibrated n values):")
    print(f"  m_μ  = {N_MU} × {M_E_MEV} = {m_mu_pred:.5f} MeV  (exp: {M_MU_MEV})")
    print(f"  m_τ  = {N_TAU} × {M_E_MEV} = {m_tau_pred:.3f} MeV  (exp: {M_TAU_MEV})")

    err_mu_vs_exp  = abs(m_mu_pred  - M_MU_MEV)  / M_MU_MEV
    err_tau_vs_exp = abs(m_tau_pred - M_TAU_MEV) / M_TAU_MEV

    print(f"\nResiduals (vs experiment):")
    print(f"  m_μ error  = {err_mu_vs_exp*100:.4f}% (by construction: just rounding)")
    print(f"  m_τ error  = {err_tau_vs_exp*100:.4f}% (by construction: just rounding)")
    print(f"\nRatios:")
    print(f"  m_μ/m_e  = {ratio_mu_e}  (exp: {EXP_MU_OVER_E:.6f})")
    print(f"  m_τ/m_μ  = {N_TAU}/{N_MU} = {ratio_tau_mu:.6f}  (exp: {EXP_TAU_OVER_MU:.6f})")

    err_ratio_mu  = abs(ratio_mu_e   - REF_MU_OVER_E)   / REF_MU_OVER_E
    err_ratio_tau = abs(ratio_tau_mu - REF_TAU_OVER_MU)  / REF_TAU_OVER_MU
    ok_mu, ok_tau, ok = _verdict_line(float(ratio_mu_e), ratio_tau_mu)

    print(f"\nNumerical comparison with experimental reference:")
    print(f"  m_μ/m_e : {ratio_mu_e}  vs  {REF_MU_OVER_E:.4f}  rel.err={err_ratio_mu*100:.3f}%")
    print(f"  m_τ/m_μ : {ratio_tau_mu:.6f}  vs  {REF_TAU_OVER_MU:.4f}  rel.err={err_ratio_tau*100:.3f}%")

    print("\nVerdict:")
    print("  ✗ NOT_A_PREDICTION — n_mu=207 and n_tau=3477 are calibrated to experiment.")
    print("    Under the 1-calibration rule this variant uses 3 parameters (m_e, n_mu, n_tau).")
    print("    The near-integer property is an observation, not a derived result.")
    # Return 1 because this is not a genuine prediction
    return 1


# ---------------------------------------------------------------------------
# Variant: candidate_hopf
# Hopf charge power law from ThetaM_MassHierarchy.tex
# ---------------------------------------------------------------------------

def run_candidate_hopf() -> int:
    """
    Hopf charge power law: m(n) = a × n^p.

    Source: original_release_of_ubt/solution_P5_dark_matter/ThetaM_MassHierarchy.tex
    Assigns n=1 (electron), n=2 (muon), n=3 (tau).
    With p=3/2 as stated in the file.

    Parameters:
        m_e [CALIBRATION #1 — sets overall scale a = m_e / 1^p]
        p   = 3/2 [fixed, stated in ThetaM_MassHierarchy.tex]

    Classification: FAILS — ratios are off by orders of magnitude.
    """
    P = 1.5   # power exponent stated in ThetaM_MassHierarchy.tex

    print(SEP)
    print("VARIANT: candidate_hopf  (Hopf charge power law, ThetaM_MassHierarchy.tex)")
    print(SEP)
    print("\nFormula: m(n) = a × n^p  where n = Hopf charge (1, 2, 3 for e, μ, τ)")
    print(f"\nParameters:")
    print(f"  p = {P}  [fixed, stated in ThetaM_MassHierarchy.tex]")
    print(f"  a = m_e / 1^p = m_e  [CALIBRATION #1 — set by electron mass]")
    print(f"  m_e = {M_E_MEV} MeV/c²  [PDG 2022]")

    a = M_E_MEV  # calibrated: a × 1^p = m_e

    m_mu_pred  = a * 2**P
    m_tau_pred = a * 3**P
    ratio_mu_e  = 2**P       # = (m(2)/m(1)) = 2^p
    ratio_tau_mu = 3**P / 2**P  # = (m(3)/m(2))

    print(f"\nPredicted masses (1 calibration: a=m_e, p={P} fixed):")
    print(f"  m_μ  = {M_E_MEV} × 2^{P} = {m_mu_pred:.5f} MeV  (exp: {M_MU_MEV})")
    print(f"  m_τ  = {M_E_MEV} × 3^{P} = {m_tau_pred:.3f} MeV  (exp: {M_TAU_MEV})")

    err_mu  = abs(m_mu_pred  - M_MU_MEV)  / M_MU_MEV
    err_tau = abs(m_tau_pred - M_TAU_MEV) / M_TAU_MEV

    print(f"\nRatios:")
    print(f"  m_μ/m_e  = 2^{P} = {ratio_mu_e:.6f}  (exp: {EXP_MU_OVER_E:.6f})")
    print(f"  m_τ/m_μ  = 3^{P}/2^{P} = {ratio_tau_mu:.6f}  (exp: {EXP_TAU_OVER_MU:.6f})")

    err_ratio_mu  = abs(ratio_mu_e   - REF_MU_OVER_E)   / REF_MU_OVER_E
    err_ratio_tau = abs(ratio_tau_mu - REF_TAU_OVER_MU)  / REF_TAU_OVER_MU

    print(f"\nComparison with experimental reference:")
    print(f"  m_μ/m_e : {ratio_mu_e:.6f}  vs  {REF_MU_OVER_E:.6f}  rel.err={err_ratio_mu*100:.1f}%")
    print(f"  m_τ/m_μ : {ratio_tau_mu:.6f}  vs  {REF_TAU_OVER_MU:.6f}  rel.err={err_ratio_tau*100:.1f}%")

    # Sensitivity: what p would be needed to fit mu/e?
    p_needed_mu  = math.log(REF_MU_OVER_E) / math.log(2)
    p_needed_tau_given_mu = math.log(REF_TAU_OVER_MU) / math.log(1.5)  # (3/2)^p
    print(f"\nSensitivity:")
    print(f"  p needed to get m_μ/m_e = 207: p = log(207)/log(2) = {p_needed_mu:.4f}")
    print(f"  p needed to get m_τ/m_μ = 16.8: p = log(16.8)/log(1.5) = {p_needed_tau_given_mu:.4f}")
    print(f"  These two values are inconsistent ({p_needed_mu:.2f} ≠ {p_needed_tau_given_mu:.2f}):")
    print(f"  no single p fits both ratios simultaneously.")

    print("\nVerdict:")
    print("  ✗ MISMATCH — Hopf power law with p=3/2 gives m_μ/m_e ≈ 2.83 (not 207).")
    print("  No single p reproduces both ratios simultaneously.")
    print("  See reports/lepton_audit/alt_hunt_notes.md, Candidate 2.")
    return 1


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Lepton mass ratio forensic reproduction (Appendix W audit).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--variant",
        choices=["canonical", "candidate_integer", "candidate_hopf", "all"],
        default="canonical",
        help="Which formula variant to evaluate (default: canonical)",
    )
    args = parser.parse_args()

    if args.variant == "all":
        results = []
        for fn in [run_canonical, run_candidate_integer, run_candidate_hopf]:
            print()
            rc = fn()
            results.append(rc)
            print()
        any_ok = any(r == 0 for r in results)
        if any_ok:
            print("OVERALL: at least one variant REPRODUCES both ratios.")
        else:
            print("OVERALL: NO variant reproduces both ratios within 1%.")
            print("         Lepton mass ratios remain an open problem in this framework.")
            print("         See reports/lepton_audit/status_summary.md")
        return 0 if any_ok else 1
    elif args.variant == "canonical":
        return run_canonical()
    elif args.variant == "candidate_integer":
        return run_candidate_integer()
    elif args.variant == "candidate_hopf":
        return run_candidate_hopf()
    else:
        print(f"Unknown variant: {args.variant}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
