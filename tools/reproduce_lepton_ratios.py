#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
Lepton mass ratio reproduction script for UBT psi-mode generation mechanism.

Evaluates candidate mass formulas for the lepton mass ratios.
The observed ratios are:
    m_e : m_mu : m_tau  ~  1 : 207 : 3477   (PDG 2022)

The naive Kaluza-Klein formula gives m0:m1:m2 = 0:1:2 (ratio 1:2),
which is INCOMPATIBLE with the observed 207:3477 by a factor of ~1700.
This script documents the KK mismatch and evaluates three alternative
mechanisms (A: parity-breaking mass matrix, B: linear Yukawa, C: psi-instantons).

Usage:
    python tools/reproduce_lepton_ratios.py [--mechanism MECH] [--R_psi R]

Mechanisms:
    kk        Naive Kaluza-Klein (proves mismatch — mandatory first step)
    A         psi-parity breaking mass matrix (linear mixing)
    B         Linear Yukawa from <Theta_0> (ratio 1:2:3)
    C         psi-instantons: m_n ~ exp(-S_inst*n) / n!   [most promising]
    all       Run all mechanisms

Exit codes:
    0 — at least one mechanism reproduces both ratios within 1%
    1 — no mechanism reproduces both ratios (expected for KK)
"""

import argparse
import math
import sys


# PDG 2022 experimental values (MeV/c^2)
M_E_MEV = 0.51099895
M_MU_MEV = 105.6583755
M_TAU_MEV = 1776.86

# Experimental ratios  (m_e = 1 unit)
EXP_RATIO_MU_E = M_MU_MEV / M_E_MEV    # ~206.77
EXP_RATIO_TAU_E = M_TAU_MEV / M_E_MEV  # ~3477.15

# Compact in the form 1 : r1 : r2
EXP = (1.0, EXP_RATIO_MU_E, EXP_RATIO_TAU_E)

# Physical constants (SI, for S_inst computation)
HBAR_J_S = 1.054571817e-34   # J·s
C_M_S = 2.99792458e8         # m/s
M_E_KG = 9.1093837015e-31    # kg
# Compton wavelength of electron: R_psi = hbar/(m_e c)
R_PSI_DEFAULT = HBAR_J_S / (M_E_KG * C_M_S)  # ~3.86e-13 m


# ──────────────────────────────────────────────────────────────────────────────
# Mechanism KK  — naive Kaluza-Klein (proves the mismatch)
# ──────────────────────────────────────────────────────────────────────────────

def mechanism_kk(R_psi: float = R_PSI_DEFAULT) -> dict:
    """
    Standard KK mass formula on psi-circle of radius R_psi:
        m_n(KK) = n / R_psi   [DERIVED — standard Kaluza-Klein result]

    n=0 (massless zero mode), n=1, n=2 give ratio 0:1:2.
    This is INCOMPATIBLE with the observed 1:207:3477 by a factor of ~1700.
    Label: [DERIVED — mismatch is a theorem]
    """
    m = [n / R_psi for n in range(3)]
    r1 = m[1] / m[1] if m[1] != 0 else 0.0  # = 1
    r2 = m[2] / m[1] if m[1] != 0 else 0.0  # = 2
    pred = (1.0, r1, r2)
    return {
        "mechanism": "KK (naive Kaluza-Klein)",
        "label": "[DERIVED — mismatch is a theorem]",
        "formula": "m_n = n / R_psi",
        "parameters": {"R_psi": R_psi},
        "free_params": 0,
        "predicted": pred,
        "experimental": EXP,
        "verdict": "DEAD END — ratio 1:2, incompatible with 207:3477 by factor ~1700",
    }


# ──────────────────────────────────────────────────────────────────────────────
# Mechanism A  — psi-parity breaking mass matrix
# ──────────────────────────────────────────────────────────────────────────────

def mechanism_A(R_psi: float = R_PSI_DEFAULT, delta: float = None) -> dict:
    """
    psi-parity breaking mass matrix:
        M_nn' = delta_nn' * m_n(KK) + Delta_nn'
    with off-diagonal mixing Delta.

    For modes n=0,1,2 the eigenvalue matrix (in units of 1/R_psi) is:
        [[0, delta, 0],
         [delta, 1, delta],
         [0, delta, 2]]

    The eigenvalues depend on the single mixing parameter delta.
    We scan delta to find the best fit to the observed ratios.
    Result: linear mixing gives a limited range of ratios. [DEAD END]
    """
    best_chi2 = 1e18
    best_delta = 0.0
    best_pred = (0.0, 0.0, 0.0)

    for d in [i * 0.001 for i in range(1, 500)]:
        mat = [[0.0, d, 0.0],
               [d, 1.0, d],
               [0.0, d, 2.0]]
        try:
            evals = sorted(abs(v) for v in _eigvals3(mat))
        except Exception:
            continue
        if len(evals) < 3 or evals[0] < 1e-12:
            continue
        r1 = evals[1] / evals[0]
        r2 = evals[2] / evals[0]
        chi2 = ((r1 - EXP[1]) / EXP[1]) ** 2 + ((r2 - EXP[2]) / EXP[2]) ** 2
        if chi2 < best_chi2:
            best_chi2 = chi2
            best_delta = d
            best_pred = (1.0, r1, r2)

    max_ratio = best_pred[2]
    verdict = (
        "DEAD END — max achievable m2/m0 ratio ~{:.1f} in linear mixing; "
        "experimental 3477 is far out of range".format(max_ratio)
    )
    return {
        "mechanism": "A (psi-parity breaking mass matrix)",
        "label": "[DEAD END — linear mixing limited range]",
        "formula": "M_nn' = delta_nn' * m_n(KK) + Delta_nn'",
        "parameters": {"R_psi": R_psi, "best_delta": best_delta},
        "free_params": 1,
        "predicted": best_pred,
        "experimental": EXP,
        "chi_squared": best_chi2,
        "verdict": verdict,
    }


def _eigvals3(mat):
    """Compute eigenvalues of 3x3 real symmetric tridiagonal matrix.

    Assumes mat is symmetric: mat[i][j] = mat[j][i].
    Uses numpy if available; falls back to Cardano's method.
    """
    try:
        import numpy as np
        return list(np.linalg.eigvalsh(np.array(mat)))
    except ImportError:
        # Fallback: characteristic polynomial for 3x3 symmetric matrix.
        # For a symmetric matrix [[a,b,c],[b,d,e],[c,e,f]]:
        a, b, c, d, e, f = (mat[0][0], mat[0][1], mat[0][2],
                             mat[1][1], mat[1][2], mat[2][2])
        # Coefficients of det(mat - λI) = -λ³ + p·λ² - q·λ + r
        p = -(a + d + f)
        q = a * d + a * f + d * f - b * b - c * c - e * e
        r = (a * (d * f - e * e) - b * (b * f - e * c) + c * (b * e - d * c))
        return _cardano_roots(1, p, q, -r)


def _cardano_roots(a, b, c, d):
    """Return real roots of ax^3+bx^2+cx+d via trigonometric method."""
    p = c / a - b ** 2 / (3 * a ** 2)
    q = (2 * b ** 3 / (27 * a ** 3) - b * c / (3 * a ** 2) + d / a)
    disc = -(4 * p ** 3 + 27 * q ** 2)
    if disc >= 0:
        m_val = 2 * math.sqrt(max(0.0, -p / 3))
        theta = math.acos(max(-1.0, min(1.0, 3 * q / (p * m_val)))) / 3 if m_val > 0 else 0.0
        roots = [m_val * math.cos(theta - 2 * math.pi * k / 3) for k in range(3)]
    else:
        inner = max(0.0, q ** 2 / 4 + p ** 3 / 27)
        sqrt_inner = math.sqrt(inner)
        half_q = -q / 2
        if half_q + sqrt_inner >= 0:
            A = (half_q + sqrt_inner) ** (1 / 3)
        else:
            A = -((-half_q - sqrt_inner) ** (1 / 3))
        B_val = -p / (3 * A) if A != 0 else 0
        roots = [A + B_val]
    return [r - b / (3 * a) for r in roots]


# ──────────────────────────────────────────────────────────────────────────────
# Mechanism B  — Linear Yukawa from <Theta_0>
# ──────────────────────────────────────────────────────────────────────────────

def mechanism_B(R_psi: float = R_PSI_DEFAULT, vev: float = M_E_MEV,
                g_yukawa: float = 1.0) -> dict:
    """
    Linear Yukawa from <Theta_0>:
        m_f(n) ~ <Theta_0> * g_Yukawa * (n+1)   ->  ratio 1:2:3

    This gives ratio m0:m1:m2 = 1:2:3, far from 1:207:3477.
    Label: [DEAD END — linear hierarchy]
    """
    masses = [vev * g_yukawa * (n + 1) for n in range(3)]
    pred = (1.0, masses[1] / masses[0], masses[2] / masses[0])
    chi2 = ((pred[1] - EXP[1]) / EXP[1]) ** 2 + ((pred[2] - EXP[2]) / EXP[2]) ** 2
    return {
        "mechanism": "B (linear Yukawa from <Theta_0>)",
        "label": "[DEAD END — linear hierarchy]",
        "formula": "m_f(n) ~ <Theta_0> * g_Yukawa * (n+1)",
        "parameters": {"vev_MeV": vev, "g_yukawa": g_yukawa},
        "free_params": 1,
        "predicted": pred,
        "experimental": EXP,
        "chi_squared": chi2,
        "verdict": "DEAD END — ratio 1:2:3, incompatible with 1:207:3477",
    }


# ──────────────────────────────────────────────────────────────────────────────
# Mechanism C  — psi-instantons
# ──────────────────────────────────────────────────────────────────────────────

def mechanism_C(R_psi: float = R_PSI_DEFAULT, S_inst: float = None) -> dict:
    """
    psi-instanton mechanism (most promising):
        m_n ~ m_0 * exp(S_inst * n) / n!

    For masses to grow with mode number (m_muon > m_e), the exponent must
    be positive (S_inst > 0). This corresponds to instanton-enhanced mass
    generation (anti-instanton sector contribution).

    Steps:
    (a) S_inst for winding-n instanton on psi-circle:
            S_inst = 2*pi*n*R_psi*m_field*c/hbar   [SKETCH — from kinetic term]
        Here S_inst is the single free parameter.
    (b) Mass ratios (normalised to m_0):
            m1/m0 = exp(S_inst) / 1
            m2/m0 = exp(2*S_inst) / 2
    (c) Require m1/m0 = 207: S_inst = ln(207) ~ 5.333
    (d) Check prediction for m2/m0:
            exp(2*5.333)/2 = (207)^2/2 ~ 21424
        Experimental: m2/m0 = 3477.
        Mismatch: factor ~6. The dilute-gas formula does NOT reproduce tau mass.
    (e) Check S_inst ~ 5.33 vs R_psi = hbar/(m_e*c):
            S_inst = 2*pi*R_psi*m_field*c/hbar => m_field = S_inst*hbar/(2*pi*R_psi*c)
        Computed m_field and comparison to known UBT mass scales is reported.

    Label: [OPEN HARD PROBLEM — instanton formula does not reproduce tau mass]
    """
    # Step (c): fix S_inst from muon ratio
    S_inst_fixed = math.log(EXP[1])  # ln(206.77) ~ 5.333

    # Use provided S_inst or the one fixed by muon ratio
    S = S_inst if S_inst is not None else S_inst_fixed

    m0 = 1.0
    m1 = math.exp(S) / 1.0          # n=1, calibrated to muon
    m2 = math.exp(2.0 * S) / 2.0    # n=2 prediction for tau

    # Normalise to m0
    pred = (1.0, m1 / m0, m2 / m0)

    chi2 = ((pred[1] - EXP[1]) / EXP[1]) ** 2 + ((pred[2] - EXP[2]) / EXP[2]) ** 2

    # Step (e): check m_field compatibility with R_psi
    # S_inst = 2*pi*R_psi*m_field*c/hbar => m_field = S_inst*hbar/(2*pi*R_psi*c)
    m_field_kg = S_inst_fixed * HBAR_J_S / (2 * math.pi * R_psi * C_M_S)
    m_field_MeV = m_field_kg * C_M_S ** 2 / 1.602176634e-13  # J -> MeV

    mismatch_mu = abs(pred[1] - EXP[1]) / EXP[1] * 100
    mismatch_tau = abs(pred[2] - EXP[2]) / EXP[2] * 100

    verdict = (
        "OPEN HARD PROBLEM — instanton formula calibrated to muon (S_inst={:.4f}) "
        "predicts m2/m0 = {:.1f}, experimental is {:.1f} (factor {:.1f} mismatch). "
        "Non-perturbative resummation or modified instanton action required.".format(
            S, pred[2], EXP[2], pred[2] / EXP[2])
    )

    return {
        "mechanism": "C (psi-instantons, dilute-gas approximation)",
        "label": "[OPEN HARD PROBLEM — instanton formula]",
        "formula": "m_n ~ exp(S_inst*n) / n!  [positive exponent for growing masses]",
        "parameters": {
            "R_psi": R_psi,
            "S_inst_fixed_from_muon": S_inst_fixed,
            "S_inst_used": S,
            "m_field_MeV": m_field_MeV,
        },
        "free_params": 1,
        "predicted": pred,
        "experimental": EXP,
        "chi_squared": chi2,
        "mismatch_pct": (mismatch_mu, mismatch_tau),
        "verdict": verdict,
    }


# ──────────────────────────────────────────────────────────────────────────────
# Reporting helpers
# ──────────────────────────────────────────────────────────────────────────────

def _report(result: dict) -> bool:
    """Print a single mechanism report; return True if ratios match within 1%."""
    print("=" * 72)
    print(f"Mechanism: {result['mechanism']}")
    print(f"Label:     {result['label']}")
    print(f"Formula:   {result['formula']}")
    print()
    print("Parameters:")
    for k, v in result["parameters"].items():
        print(f"  {k} = {v:.6g}")
    print(f"  free parameters used: {result['free_params']}")
    print()
    pred = result["predicted"]
    exp = result["experimental"]
    print(f"  Predicted  m0:m1:m2 = 1 : {pred[1]:.4g} : {pred[2]:.4g}")
    print(f"  Experiment m0:m1:m2 = 1 : {exp[1]:.4g} : {exp[2]:.4g}")
    if "chi_squared" in result:
        print(f"  chi-squared = {result['chi_squared']:.4g}")
    print()
    print(f"Verdict: {result['verdict']}")
    print()

    # Accept criterion: <1% error on both ratios with <=1 free parameter
    if pred[1] > 0 and pred[2] > 0:
        err1 = abs(pred[1] - exp[1]) / exp[1]
        err2 = abs(pred[2] - exp[2]) / exp[2]
        if err1 < 0.01 and err2 < 0.01 and result["free_params"] <= 1:
            print("  >>> ACCEPTED: <1% error with <=1 free parameter <<<")
            return True
    return False


def main():
    parser = argparse.ArgumentParser(
        description="UBT psi-mode lepton mass ratio tool")
    parser.add_argument(
        "--mechanism", default="all",
        choices=["kk", "A", "B", "C", "all"],
        help="Mass mechanism to evaluate (default: all)")
    parser.add_argument(
        "--R_psi", type=float, default=R_PSI_DEFAULT,
        help=f"psi-circle radius in metres (default: Compton wavelength = {R_PSI_DEFAULT:.4e} m)")
    args = parser.parse_args()

    R = args.R_psi
    mechs = (["kk", "A", "B", "C"] if args.mechanism == "all"
             else [args.mechanism])

    print("=" * 72)
    print("UBT Lepton Mass Ratio Analysis — psi-Mode Generation Mechanism")
    print("=" * 72)
    print()
    print("Experimental lepton mass ratios (PDG 2022, m_e = 1):")
    print(f"  m_e : m_mu : m_tau = 1 : {EXP[1]:.4f} : {EXP[2]:.4f}")
    print()
    print("STEP 1 — KK MISMATCH (mandatory)")
    print("  Standard KK formula: m0:m1:m2 = 0:1:2, ratio m1:m2 = 1:2")
    print("  Observed:            m_mu:m_tau ~ 207:3477 = 1:16.8")
    print("  KK is incompatible with observed ratios by a factor of ~1700.")
    print("  [DERIVED — mismatch is a theorem]")
    print()
    print("  The naive KK formula gives m1:m2 = 1:2, incompatible with the")
    print("  observed ratio 207:3477. Additional mass dynamics are required.")
    print("  The psi-mode generation mechanism is conjectural pending")
    print("  identification of the correct mass generation mechanism.")
    print()

    any_accepted = False
    for mech in mechs:
        if mech == "kk":
            result = mechanism_kk(R)
        elif mech == "A":
            result = mechanism_A(R)
        elif mech == "B":
            result = mechanism_B(R)
        elif mech == "C":
            result = mechanism_C(R)
        else:
            continue
        accepted = _report(result)
        any_accepted = any_accepted or accepted

    print("=" * 72)
    if any_accepted:
        print("SUMMARY: At least one mechanism reproduces lepton ratios within 1%.")
        return 0
    else:
        print("SUMMARY: No mechanism reproduces the observed lepton mass ratios.")
        print()
        print("HONEST FALLBACK:")
        print("  The psi-mode generation conjecture is currently incompatible with")
        print("  observed lepton mass ratios. The mass generation mechanism is an")
        print("  OPEN HARD PROBLEM. The identification Theta_0/Theta_1/Theta_2 <->")
        print("  e/mu/tau remains a conjecture.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
