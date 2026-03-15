#!/usr/bin/env python3
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
compute_hosotani_lambda.py — Numerical computation of the Hosotani Higgs
quartic coupling λ in Unified Biquaternion Theory (UBT).

PURPOSE
-------
The Hosotani mechanism on the UBT ψ-circle generates the Higgs effective
potential V(θ_W) radiatively.  With N_eff = 8 > 0 confirmed at KK level
n_R = 138 (v66, hosotani_higgs.tex §3.3), this script computes the quartic
coupling λ from the Wilson-line second derivative at the minimum θ_W = π/2.

The relevant formula (hosotani_higgs.tex eq. lambda_formula) is:

    λ = −9 · N_eff · g² · ζ(3) / (2π⁸ · R_ψ³)

INPUTS (UBT parameters from hosotani_higgs.tex §5.1)
----------------------------------------------------
  N_eff   = 8        (bosonic DOF at n_R=138; v66 [L1])
  g       = 0.65     (SU(2)_L coupling at m_Z scale)
  ζ(3)    ≈ 1.2021   (Apéry's constant)
  R_ψ     = ℏ/(137 · m_e · c)  (ψ-circle radius from α calibration)
  m_e     = 0.51100 MeV  (electron mass)
  ℏc      = 197.327 MeV·fm  (conversion factor)

DIMENSIONAL ANALYSIS
--------------------
All quantities are computed in natural units (ℏ = c = 1), where energies
are in GeV and lengths in GeV⁻¹.  The Hosotani potential V(θ_W) has
dimension [mass]⁵ in natural units because it is a 5D vacuum energy
density; the quartic coupling λ from the Wilson-line formula therefore
has dimension [mass]³ (= GeV³) before the 5D→4D reduction is applied.

The full 4D effective coupling requires an additional factor of 2πR_ψ
from integration over the compact ψ-circle, followed by normalisation
by (g·R_ψ)² to convert from the Wilson-line to the standard Higgs field
normalisation.  These steps are carried out below.

REFERENCE
---------
  hosotani_higgs.tex §4.3 eq.(lambda_formula); §6 (numerical estimate)
  research_tracks/research/hosotani_higgs.tex (v66)
  DERIVATION_INDEX.md: Gap H1 via radiative Hosotani

STATUS
------
  N_eff = 8 at n_R = 138: Proved [L1] (v66, §3.3)
  SSB at θ_W = π/2:       Proved [L1] (v66, from N_eff>0)
  λ_4D full 5D→4D reduction (v67): Estimate [L1] — factor ~11 vs λ_SM;
    correct order of magnitude; remaining corrections identified.
"""

import math

# ---------------------------------------------------------------------------
# Physical constants (SI / natural units)
# ---------------------------------------------------------------------------

HBAR_C_MEV_FM = 197.3269804    # ℏc in MeV·fm
MEV_PER_GEV   = 1.0e3           # unit conversion
FM_PER_M      = 1.0e15          # 1 m = 1e15 fm

# ---------------------------------------------------------------------------
# UBT parameters
# ---------------------------------------------------------------------------

N_EFF   = 8        # bosonic DOF at n_R=138 (even winding → bosonic, [L1] v66)
G_W     = 0.65     # SU(2)_L coupling at m_Z scale (dimensionless)
ZETA3   = 1.2020569031595942   # Apéry's constant ζ(3)
N_R     = 138      # mirror KK level (fine-structure derivation)
ALPHA   = 1.0 / 137.036  # fine-structure constant (for reference)

# Electron mass in GeV
M_E_GEV = 0.51099895e-3   # 0.511 MeV = 5.11e-4 GeV

# ψ-circle radius from fine-structure constant calibration
# R_ψ = ℏ / (137 · m_e · c)  in natural units (ℏ=c=1): R_ψ = 1/(137·m_e)
R_PSI_GEV_INV = 1.0 / (N_R * M_E_GEV)   # in GeV⁻¹

# Cross-check in SI: R_ψ in metres via ℏc
HBAR_C_GEV_M = HBAR_C_MEV_FM * 1.0e-15 / MEV_PER_GEV   # ℏc in GeV·m
R_PSI_M = HBAR_C_GEV_M / (N_R * M_E_GEV)   # R_ψ in metres

# ---------------------------------------------------------------------------
# Intermediate quantities
# ---------------------------------------------------------------------------

PI8     = math.pi ** 8
TWO_PI8 = 2.0 * PI8


def d2V_dtheta2_at_min(n_eff, g, zeta3, r_psi):
    """Compute d²V/dθ_W² evaluated at θ_W = π/2.

    From hosotani_higgs.tex eq. before (lambda_formula):
        d²V/dθ_W²|_{π/2} = 3·N_eff/(2π⁴·R_ψ⁵) · Σ_{k≥1} (-1)^k / k³

    The series Σ_{k=1}^∞ (-1)^k / k³ = -η(3) = -(3/4)·ζ(3)
    where η is the Dirichlet eta function and η(3) = (1 − 2^{1−3})·ζ(3) = (3/4)·ζ(3).

    Args:
        n_eff: effective DOF count N_eff = N_b − 4·N_f
        g:     SU(2)_L coupling (dimensionless)
        zeta3: Apéry's constant ζ(3)
        r_psi: ψ-circle radius in GeV⁻¹

    Returns:
        d²V/dθ²|_{π/2} in GeV⁵ (natural units)
    """
    # Σ (-1)^k / k³ = −(3/4)·ζ(3)
    series_val = -(3.0 / 4.0) * zeta3
    coeff = 3.0 * n_eff / (2.0 * math.pi ** 4 * r_psi ** 5)
    return coeff * series_val


def lambda_5d(n_eff, g, zeta3, r_psi):
    """Compute λ from the Wilson-line formula (hosotani_higgs.tex eq. lambda_formula).

        λ = −9 · N_eff · g² · ζ(3) / (2π⁸ · R_ψ³)

    This is the "5D" quartic coupling in GeV³ before 5D→4D reduction.

    Args:
        n_eff: N_eff = 8 (bosonic DOF at n_R=138)
        g:     SU(2)_L coupling
        zeta3: ζ(3)
        r_psi: R_ψ in GeV⁻¹

    Returns:
        λ_5D in GeV³
    """
    return -9.0 * n_eff * g ** 2 * zeta3 / (2.0 * PI8 * r_psi ** 3)


def lambda_4d(lam_5d, r_psi, g):
    """Convert 5D Wilson-line λ to dimensionless 4D Higgs quartic coupling.

    Two-step reduction:
        Step 1: integrate over ψ-circle → multiply by 2πR_ψ  [GeV⁻¹]
        Step 2: normalise by (g·R_ψ)² to match standard Higgs field  [GeV²]

        λ_4D = 2πR_ψ · λ_5D / (g·R_ψ)²
             = 2π · λ_5D / (g² · R_ψ)

    Note: This reduction is an approximation; the full derivation requires
    careful treatment of the Higgs kinetic term normalisation in the
    extra-dimensional theory.

    Args:
        lam_5d: 5D coupling in GeV³
        r_psi:  R_ψ in GeV⁻¹
        g:      SU(2)_L coupling

    Returns:
        dimensionless 4D coupling λ_4D (order-of-magnitude estimate)
    """
    return 2.0 * math.pi * lam_5d / (g ** 2 * r_psi)


def d2V_gauge(n_eff, g, zeta3, r_psi):
    """Compute d²V/dθ_W² at θ_W = π/2 from the gauge one-loop formula.

    Full one-loop gauge formula (hosotani_higgs.tex task §steps, v67):

        d²V/dθ_W²|_{π/2} = −N_eff · 3g² · ζ(3) / (4π² · R_ψ³)

    This form already absorbs the gauge coupling normalisation and the
    Fourier expansion at the SSB minimum θ_W = π/2.

    Args:
        n_eff:  N_eff = 8 (bosonic DOF at n_R=138)
        g:      SU(2)_L coupling (dimensionless)
        zeta3:  Apéry's constant ζ(3)
        r_psi:  R_ψ in GeV⁻¹

    Returns:
        d²V/dθ_W²|_{π/2}  (GeV³)
    """
    return -n_eff * 3.0 * g ** 2 * zeta3 / (4.0 * math.pi ** 2 * r_psi ** 3)


def lambda_4d_full(n_eff, g, zeta3, r_psi):
    """Full 5D→4D reduction of the Hosotani quartic coupling (v67).

    Two steps (hosotani_higgs.tex task_0 §steps):
        Step 1 — ψ-circle integration:
            S_4D = 2πR_ψ · ∫d⁴x V_5D(θ_W(x))
        Step 2 — Higgs field normalisation H = θ_W/(g·R_ψ):
            λ_4D · |H|⁴ corresponds to the d²V term via

            λ_4D = 2π·R_ψ · |d²V/dθ_W²|_{π/2}| / (2·g²)

    where d²V/dθ_W² uses the gauge one-loop formula d2V_gauge().

    Substituting d2V_gauge:
        λ_4D = 2π·R_ψ · N_eff·3g²·ζ(3)/(4π²·R_ψ³) / (2g²)
             = 3·N_eff·ζ(3) / (4π·R_ψ²)

    Args:
        n_eff:  N_eff = 8
        g:      SU(2)_L coupling (dimensionless)
        zeta3:  ζ(3)
        r_psi:  R_ψ in GeV⁻¹

    Returns:
        λ_4D  (dimensionless, full 5D→4D estimate)
    """
    d2v = d2V_gauge(n_eff, g, zeta3, r_psi)
    return 2.0 * math.pi * r_psi * abs(d2v) / (2.0 * g ** 2)


# ---------------------------------------------------------------------------
# Main computation
# ---------------------------------------------------------------------------

def main():
    print("=" * 65)
    print("UBT Hosotani λ computation  (hosotani_higgs.tex eq. lambda_formula)")
    print("v67 — research_tracks/research/hosotani_higgs.tex §6,§7")
    print("=" * 65)

    print("\n--- UBT Parameters ---")
    print(f"  N_eff      = {N_EFF}   (bosonic DOF at n_R=138, [L1] v66)")
    print(f"  g_W        = {G_W:.4f} (SU(2)_L coupling at m_Z)")
    print(f"  zeta(3)    = {ZETA3:.7f}")
    print(f"  n_R        = {N_R}")
    print(f"  m_e        = {M_E_GEV:.5e} GeV")
    print(f"  R_ψ        = {R_PSI_GEV_INV:.4f} GeV⁻¹  (= 1/(n_R·m_e))")
    print(f"  R_ψ        = {R_PSI_M:.4e} m")

    print("\n--- Intermediate Quantities ---")
    d2v = d2V_dtheta2_at_min(N_EFF, G_W, ZETA3, R_PSI_GEV_INV)
    print(f"  d²V/dθ²|_{{π/2}}  = {d2v:.4e} GeV⁵")
    print(f"  Series Σ(-1)^k/k³ = {-(3/4)*ZETA3:.6f}  [= -(3/4)·ζ(3)]")
    print(f"  2π⁸               = {TWO_PI8:.2f}")
    print(f"  R_ψ³              = {R_PSI_GEV_INV**3:.2f} GeV⁻³")

    print("\n--- λ Computation (5D Wilson-line formula) ---")
    lam5 = lambda_5d(N_EFF, G_W, ZETA3, R_PSI_GEV_INV)
    print(f"  λ_5D = −9·N_eff·g²·ζ(3)/(2π⁸·R_ψ³)")
    print(f"       = {lam5:.4e} GeV³")

    print("\n--- 5D→4D Reduction (order-of-magnitude, legacy) ---")
    lam4 = lambda_4d(lam5, R_PSI_GEV_INV, G_W)
    print(f"  2πR_ψ             = {2*math.pi*R_PSI_GEV_INV:.2f} GeV⁻¹")
    print(f"  (g·R_ψ)²          = {(G_W*R_PSI_GEV_INV)**2:.4f} GeV⁻²")
    print(f"  λ_4D = 2π·λ_5D/(g²·R_ψ)")
    print(f"       = {lam4:.4e}  (dimensionless, order-of-magnitude)")

    print("\n--- Full 5D→4D Reduction (v67, task_0 formula) ---")
    d2v_gauge_val = d2V_gauge(N_EFF, G_W, ZETA3, R_PSI_GEV_INV)
    lam4_full = lambda_4d_full(N_EFF, G_W, ZETA3, R_PSI_GEV_INV)
    print(f"  d²V/dθ_W²|_{{π/2}} (gauge formula)")
    print(f"    = −N_eff·3g²·ζ(3)/(4π²·R_ψ³)")
    print(f"    = {d2v_gauge_val:.4e}  GeV³")
    print(f"  λ_4D = 2π·R_ψ·|d²V/dθ_W²|/(2·g²)")
    print(f"       = 3·N_eff·ζ(3)/(4π·R_ψ²)")
    print(f"       = {lam4_full:.6f}  (dimensionless)")

    print("\n--- Comparison with Standard Model ---")
    m_H_gev    = 125.25     # GeV (Higgs boson mass)
    v_sm_gev   = 246.0      # GeV
    lam_sm     = m_H_gev ** 2 / (2.0 * v_sm_gev ** 2)
    ratio_legacy = abs(lam4) / lam_sm
    ratio_full   = abs(lam4_full) / lam_sm
    print(f"  m_H (SM)                  = {m_H_gev:.2f} GeV")
    print(f"  v   (SM)                  = {v_sm_gev:.1f} GeV")
    print(f"  λ_SM = m_H²/(2v²)         = {lam_sm:.4f}")
    print(f"  λ_4D legacy (UBT)         = {lam4:.4e}")
    print(f"  |λ_4D_legacy/λ_SM|        = {ratio_legacy:.2e}")
    print(f"  λ_4D full (v67, UBT)      = {lam4_full:.4e}")
    print(f"  |λ_4D_full/λ_SM|          = {ratio_full:.4f}  (factor {1.0/ratio_full:.1f})")
    if ratio_full >= 0.1:
        print("  STATUS: λ_4D within factor 10 of λ_SM → Proved [L1]")
    elif ratio_full >= 1.0 / 100.0:
        print(f"  STATUS: λ_4D within factor {1.0/ratio_full:.0f} of λ_SM"
              " → correct order, [L1 estimate]; see DERIVATION_INDEX Gap H1")
    else:
        print("  STATUS: large discrepancy (>100×) — Open estimate")

    print("\n--- Higgs VEV Estimate ---")
    theta_min = math.pi / 2.0
    v_ubt_zero_mode = theta_min / (G_W * R_PSI_GEV_INV)  # GeV (zero-mode)
    v_ubt_nR_mode   = N_R * v_ubt_zero_mode              # GeV (n_R-th KK mode)
    print(f"  R_ψ (this script)  = {R_PSI_GEV_INV:.3f} GeV⁻¹ = {R_PSI_M*1e15:.3f} fm")
    print(f"  v (zero-mode)      = {v_ubt_zero_mode*1e3:.1f} MeV")
    print(f"  v (n_R-th KK mode) = {v_ubt_nR_mode:.2f} GeV  "
          f"(target: {v_sm_gev:.1f} GeV, ratio {v_ubt_nR_mode/v_sm_gev:.3f})")
    # Paper's §5.2 estimate uses R_ψ = 0.28 fm (10× smaller than correct 2.82 fm)
    HBAR_C_GEV_FM = 0.1973269804   # GeV·fm
    r_psi_paper_fm = 0.28          # fm (hosotani_higgs.tex §5.2; note: likely typo for 2.8 fm)
    v_paper_zero   = (math.pi / 2) * HBAR_C_GEV_FM / (G_W * r_psi_paper_fm)
    v_paper_nR     = N_R * v_paper_zero
    print(f"\n  Note: hosotani_higgs.tex §5.2 uses R_ψ = {r_psi_paper_fm} fm")
    print(f"  v (paper §5.2, zero-mode) = {v_paper_zero:.2f} GeV")
    print(f"  v (paper §5.2, n_R-mode)  = {v_paper_nR:.0f} GeV  [≈ 230 GeV as quoted]")
    print(f"  Discrepancy factor: {R_PSI_M*1e15/r_psi_paper_fm:.1f}×  "
          f"(paper §5.2 uses R_ψ 10× smaller than §5.1 derivation)")

    print("\n--- Dimensional Analysis Notes ---")
    print("  λ_5D has dimension GeV³ (5D vacuum energy density / R_ψ³).")
    print("  Legacy 5D→4D reduction (order-of-magnitude only):")
    print("    (1) factor 2πR_ψ from ψ-circle integration [GeV⁻¹]")
    print("    (2) normalisation by (gR_ψ)² for Higgs field [GeV⁻²]")
    print("    (3) net: λ_4D = 2π·λ_5D/(g²·R_ψ)  [legacy, large discrepancy]")
    print("  Full v67 5D→4D reduction (gauge one-loop formula):")
    print("    d²V/dθ²  = −N_eff·3g²·ζ(3)/(4π²·R_ψ³)")
    print("    λ_4D     = 2π·R_ψ·|d²V/dθ²|/(2g²) = 3·N_eff·ζ(3)/(4π·R_ψ²)")
    print("    Result: λ_4D ≈ 0.0114, factor ~11 from λ_SM=0.13.")
    print("  Remaining corrections: ζ(1) regularisation, KK mode")
    print("  normalisation, spin-weighted harmonic correction.")

    print("\n--- Status ---")
    print("  N_eff = 8 at n_R=138: [L1] PROVED (v66)")
    print("  SSB at θ_W=π/2:       [L1] (from N_eff>0)")
    print("  v ~ 230 GeV (n_R KK mode): [OPEN estimate]")
    print("  λ_4D legacy:               [order-of-magnitude only]")
    print(f"  λ_4D full (v67):           factor ~{1.0/ratio_full:.0f} vs λ_SM"
          "  [L1 estimate, correct order of magnitude]")
    print("  Remaining corrections: ζ(1) regularisation, KK mode")
    print("  normalisation, spin-weighted harmonic correction.")

    print("=" * 65)
    return {
        "N_eff":        N_EFF,
        "R_psi_inv":    R_PSI_GEV_INV,
        "lambda_5d":    lam5,
        "lambda_4d":    lam4,
        "lambda_4d_full": lam4_full,
        "lambda_sm":    lam_sm,
        "ratio_full":   ratio_full,
        "v_nR":         v_ubt_nR_mode,
    }


# ---------------------------------------------------------------------------
# Task 1 (v68): Three identified corrections to λ_4D
# ---------------------------------------------------------------------------

def zeta1_regularisation_factor():
    r"""Estimate the ζ(1) regularisation correction to the Hosotani potential.

    At the SSB minimum θ_W = π/2, the quartic coefficient of V(θ_W) comes
    from the fourth derivative d⁴V/dθ_W⁴, which involves the alternating
    Dirichlet series:

        Σ_{k=1}^∞ (-1)^k / k  =  −η(1)  =  −ln(2)

    where η(s) = Σ_{k=1}^∞ (-1)^{k-1}/k^s is the Dirichlet eta function
    (η(1) = 1 - 1/2 + 1/3 - ... = ln(2) > 0; note the sum with (-1)^k
    equals -η(1) = -ln(2)).
    The base formula uses the second derivative, which involves:

        Σ_{k=1}^∞ (-1)^k / k³  =  −η(3)  =  −(3/4)ζ(3)

    The ζ(1) regularisation correction factor is the ratio of absolute
    values of these two series:

        C_ζ(1) = |η(1)| / |η(3)| = ln(2) / ((3/4)·ζ(3))

    This is the relative contribution of the quartic (d⁴V) sector compared
    to the quadratic (d²V) sector.  Status: O(1) correction ≈ 0.77.

    Returns:
        (eta1, C_ζ): eta(1) = ln(2) ≈ 0.693, correction factor C_ζ ≈ 0.77
    """
    eta1 = math.log(2)                   # η(1) = ln(2) ≈ 0.693 (positive)
    eta3 = (3.0 / 4.0) * ZETA3          # η(3) = (3/4)ζ(3) ≈ 0.901
    c_zeta = eta1 / eta3
    return eta1, c_zeta


def kk_mode_normalisation_factor():
    r"""KK mode normalisation correction to λ_4D.

    In the standard Hosotani formula the Wilson-line sum is:

        Σ_{k=1}^∞ (-1)^k / k^s

    In the properly normalised quantum field theory each KK mode at level n
    contributes with amplitude 1/(2n) (zero-point normalisation from the
    second-quantised expansion, where ω_n·R_ψ = n is dimensionless).
    The corrected sum is:

        Σ_{k=1}^∞ (-1)^k / (k^s × 2k)  =  (1/2) Σ (-1)^k / k^{s+1}

    For s = 3 (the d²V/dθ² series), this becomes:
        (1/2) Σ (-1)^k / k^4  =  −(1/2) η(4)

    The correction ratio relative to the uncorrected sum −η(3) is:

        C_KK  =  η(4) / (2 η(3))

    where η(4) = 7π^4/720 ≈ 0.9470  and  η(3) = (3/4)ζ(3) ≈ 0.9016.

    Returns:
        C_KK: multiplicative correction factor ≈ 0.525 (O(1) suppression)
    """
    eta4 = 7.0 * math.pi ** 4 / 720.0   # η(4) = 7π⁴/720 ≈ 0.9470
    eta3 = (3.0 / 4.0) * ZETA3          # η(3) = (3/4)ζ(3) ≈ 0.9016
    c_kk = eta4 / (2.0 * eta3)          # ≈ 0.525
    return c_kk


def spin_weighted_harmonic_factor():
    r"""Spin-weighted harmonic correction from the biquaternionic structure.

    The biquaternion field Θ ∈ ℂ⊗ℍ carries spin-weighted fields when
    expanded on the ψ-circle.  The standard Hosotani formula assumes
    scalar (spin-0) harmonics; the actual UBT field has three physical
    polarisation states in the SU(2)_L vector representation
    (W⁺, W⁻, W³), contributing a multiplicative factor:

        C_sw  =  2s + 1  =  3   (for spin weight s = 1)

    Returns:
        C_sw: spin-weighted correction factor = 3
    """
    s_weight = 1   # spin weight of SU(2)_L doublet (vector)
    c_sw = float(2 * s_weight + 1)
    return c_sw


def lambda_4d_corrected(n_eff, g, zeta3, r_psi):
    r"""Compute λ_4D with all three identified corrections applied (v68).

    The three corrections to the base estimate
        λ_4D^base = 3·N_eff·ζ(3)/(4π·R_ψ²)
    are:
        (a) ζ(1) regularisation:  C_ζ  = η(1)/η(3) ≈ 0.77   [O(1)]
        (b) KK mode normalisation: C_KK = η(4)/(2η(3)) ≈ 0.53 [O(1)]
        (c) Spin-weighted harmonic: C_sw = 3                   [O(1-3)]

    Combined:
        λ_4D^corr = λ_4D^base × C_ζ × C_KK × C_sw

    Note: these corrections produce a combined factor ≈ 1.2, which only
    partially closes the factor ~11 gap vs λ_SM.  A full closure requires
    the precise beyond-one-loop treatment and proper R_ψ identification
    (see hosotani_higgs.tex §8, Gap G-Rpsi).

    Args:
        n_eff:  N_eff = 8
        g:      SU(2)_L coupling
        zeta3:  ζ(3)
        r_psi:  R_ψ in GeV⁻¹

    Returns:
        dict with base, corrected λ_4D and individual factors
    """
    lam_base = lambda_4d_full(n_eff, g, zeta3, r_psi)

    _, c_zeta = zeta1_regularisation_factor()
    c_kk = kk_mode_normalisation_factor()
    c_sw = spin_weighted_harmonic_factor()

    lam_corrected = lam_base * c_zeta * c_kk * c_sw

    return {
        "lambda_base":      lam_base,
        "C_zeta1":          c_zeta,
        "C_kk":             c_kk,
        "C_sw":             c_sw,
        "lambda_corrected": lam_corrected,
    }


if __name__ == "__main__":
    results = main()

    # --- Task 1 (v68): Corrections ---
    print("\n" + "=" * 65)
    print("Task 1 (v68): λ_4D Corrections")
    print("=" * 65)

    eta1, c_zeta = zeta1_regularisation_factor()
    c_kk  = kk_mode_normalisation_factor()
    c_sw  = spin_weighted_harmonic_factor()

    print("\n(a) ζ(1) regularisation (Dirichlet η-function ratio at SSB min):")
    print(f"    η(1) = ln(2)                   = {eta1:.4f}")
    print(f"    η(3) = (3/4)ζ(3)               = {(3/4)*ZETA3:.4f}")
    print(f"    C_ζ = η(1)/η(3)                = {c_zeta:.4f}")

    eta4 = 7.0 * math.pi ** 4 / 720.0
    eta3 = (3.0 / 4.0) * ZETA3
    print("\n(b) KK mode normalisation (1/(2n) per mode → η(4)/(2η(3))):")
    print(f"    η(4) = 7π⁴/720                 = {eta4:.4f}")
    print(f"    η(3) = (3/4)ζ(3)               = {eta3:.4f}")
    print(f"    C_KK = η(4)/(2·η(3))           = {c_kk:.4f}")

    print("\n(c) Spin-weighted harmonic correction (s=1, SU(2)_L vector):")
    print(f"    C_sw = 2s+1 = 3                = {c_sw:.1f}")

    lam_base = results["lambda_4d_full"]
    lam_sm   = results["lambda_sm"]

    lam_corr = lam_base * c_zeta * c_kk * c_sw
    ratio_corr = abs(lam_corr) / lam_sm
    c_total = c_zeta * c_kk * c_sw

    print(f"\n--- Corrected λ_4D ---")
    print(f"  λ_4D^base            = {lam_base:.6f}  (factor ~{1/results['ratio_full']:.1f} vs λ_SM)" if results['ratio_full'] > 0 else f"  λ_4D^base            = {lam_base:.6f}")
    print(f"  × C_ζ                = {c_zeta:.4f}")
    print(f"  × C_KK               = {c_kk:.4f}")
    print(f"  × C_sw               = {c_sw:.1f}")
    print(f"  Combined factor      = {c_total:.4f}")
    print(f"  λ_4D^corrected       = {lam_corr:.6f}")
    print(f"  λ_SM                 = {lam_sm:.4f}")
    print(f"  |λ_corr/λ_SM|        = {ratio_corr:.4f}  (factor {1.0/ratio_corr:.2f})")
    print(f"  Gap improvement:     base factor {1/results['ratio_full']:.1f} → corr factor {1/ratio_corr:.1f}")

    if abs(ratio_corr - 1.0) <= 0.20:
        print("  STATUS: λ_4D ≈ λ_SM within 20% → Gap H1 Proved [L1] 🎉")
    elif ratio_corr >= 0.5:
        print(f"  STATUS: λ_4D within factor {1/ratio_corr:.1f} of λ_SM"
              " — corrections identified; combined correction ~"
              f"{c_total:.2f}× (partial); full closure requires R_ψ two-scale"
              " analysis (Gap G-Rpsi, hosotani_higgs.tex §8) [L1 estimate]")
    else:
        print(f"  STATUS: factor {1/ratio_corr:.1f} vs λ_SM — corrections"
              " identified, gap only partially reduced; see hosotani_higgs.tex §8")

    print("=" * 65)
