# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text

"""
theta_spectrum_scan.py — Eigenmode spectrum of the UBT Θ field on T²(τ).

Computes eigenvalues and eigenmodes of the d'Alembertian / Laplacian
acting on the Θ field compactified on a 2-torus with complex time
τ = t + iψ, where ψ ∈ [0, 2π R_ψ].

Physical setup
--------------
The UBT field Θ(x, τ) on ℝ^{1,3} × T² (compact imaginary direction) has
the Fourier expansion:

    Θ(x, t, ψ) = Σ_{n=-∞}^{∞}  Θ̂_n(x,t) · exp(i n ψ / R_ψ)

The mass of KK mode n is:

    m_n² = (n / R_ψ)²

The ZERO MODE (n = 0) is exactly massless.  All n≠0 modes have mass
m_n = |n| / R_ψ.  For R_ψ → ∞ the entire KK tower becomes light; for
finite R_ψ only the zero mode remains massless.

Degeneracy on T²(τ = iR_ψ):  on a rectangular torus R_t × R_ψ the 2D
eigenvalues are

    λ_{n_t,n_ψ} = (n_t / R_t)² + (n_ψ / R_ψ)²

The (0,0) mode has λ = 0 (the "Dark Radiation" zero mode).

Reproducibility
---------------
All numbers are derived from geometry; no curve-fitting is used.

Run:
    python simulations/theta_eigenmodes/theta_spectrum_scan.py

Outputs:
    stdout  — formatted table of lowest eigenvalues and degeneracies
    (return value when imported) — dict with spectrum data

References:
    UBT_v28_cosmo_hecke_neff  (this task)
    ubt/spectral/laplacian_torus.py
    THEORY/AXIOMS.md
"""

from __future__ import annotations

import math
import sys
import os

# Allow running from repository root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from ubt.spectral.laplacian_torus import (
    torus_eigenvalues,
    get_lowest_nonzero_eigenvalue,
    mode_count_below_energy,
)


# ---------------------------------------------------------------------------
# Physical parameters (UBT canonical values)
# ---------------------------------------------------------------------------

# Compactification radius of imaginary time direction (in units of ℏ/m_e c)
# This is a free parameter of UBT; we scan a representative range.
R_PSI_FIDUCIAL = 1.0   # normalised units (set = 1 for dimensionless spectrum)

# Torus dimensions: d=2 (real time x imaginary time), or d=1 (ψ-circle only)
D_TORUS = 2

# Maximum mode number to scan
K_MAX = 8

# Biquaternion Θ has 8 real DoF (4 complex quaternion components × 2)
N_THETA_DOF = 8


# ---------------------------------------------------------------------------
# Spectrum computation
# ---------------------------------------------------------------------------

def compute_torus_spectrum(d: int, k_max: int, L: float = 1.0):
    """
    Return sorted list of (eigenvalue, degeneracy) pairs for Laplacian on T^d.

    Eigenvalues: λ_{k} = (2π/L)² |k|²  for k ∈ Z^d.
    The zero mode (k=0) has λ=0 and degeneracy 1.
    """
    eigenvalues, degeneracies = torus_eigenvalues(d, k_max, L)
    pairs = sorted(zip(eigenvalues.tolist(), degeneracies.tolist()))
    return pairs


def identify_zero_modes(spectrum: list,
                        tol: float = 1e-12) -> int:
    """Return total degeneracy of zero (massless) modes."""
    total = 0
    for lam, deg in spectrum:
        if abs(lam) < tol:
            total += deg
    return total


def classify_mode_degeneracy(spectrum: list) -> dict:
    """
    Classify modes by degeneracy type.

    Returns
    -------
    dict with keys:
        'zero'    : list of (λ, deg) for massless modes
        'light'   : list of (λ, deg) for λ < spectral_gap/4
        'massive' : list of (λ, deg) for all other modes
        'spectral_gap' : lowest non-zero eigenvalue
    """
    if not spectrum:
        return {}

    non_zero = [(lam, deg) for lam, deg in spectrum if lam > 1e-12]
    spectral_gap = min(lam for lam, _ in non_zero) if non_zero else float('inf')

    zero_modes   = [(lam, deg) for lam, deg in spectrum if lam <= 1e-12]
    light_modes  = [(lam, deg) for lam, deg in spectrum
                    if 1e-12 < lam <= spectral_gap / 4 + 1e-12]
    massive_modes = [(lam, deg) for lam, deg in spectrum if lam > spectral_gap / 4]

    return {
        'zero':         zero_modes,
        'light':        light_modes,
        'massive':      massive_modes,
        'spectral_gap': spectral_gap,
    }


def theta_zero_mode_dof(n_biquaternion_dof: int = N_THETA_DOF) -> int:
    """
    Number of massless degrees of freedom from Θ zero modes.

    Each of the n_biquaternion_dof real components of Θ has exactly one
    k=0 mode on the torus.  All are massless by the T²-symmetry argument.
    """
    return n_biquaternion_dof   # one zero mode per real DoF


# ---------------------------------------------------------------------------
# Poisson duality check (Poisson summation)
# ---------------------------------------------------------------------------

def poisson_duality_check(R: float, N: int = 50) -> dict:
    """
    Verify Poisson duality: spectral sum <-> winding sum.

    For f(x) = exp(-pi x^2 / R^2) on a circle of radius R:
        Spectral: S(R) = sum_{n in Z} f_hat(n) = sum_{n in Z} R exp(-pi n^2 R^2)
        Winding:  W(R) = sum_{m in Z} f(m)     = sum_{m in Z} exp(-pi m^2 / R^2)

    Poisson: W(R) = R * S(R)  (d=1: tau = R^2, W = tau^{d/2} S)

    Returns dict with spectral_sum, winding_sum, ratio, passes.
    """
    # spectral sum (Jacobi theta-like)
    spectral = sum(math.exp(-math.pi * n * n * R * R) for n in range(-N, N+1))
    # winding sum
    winding  = sum(math.exp(-math.pi * m * m / (R * R)) for m in range(-N, N+1))
    ratio = winding / spectral if spectral > 1e-30 else float('inf')
    return {
        'spectral_sum': spectral,
        'winding_sum':  winding,
        'ratio':        ratio,
        'R':            R,
        'expected_ratio': R,
        'passes':       abs(ratio - R) < 1e-6 * R,
    }


# ---------------------------------------------------------------------------
# Main scan and report
# ---------------------------------------------------------------------------

def run_scan(verbose: bool = True) -> dict:
    """
    Run the full theta-eigenmode scan and return results dict.
    """
    results = {}

    # --- 1D torus (psi-circle only) ---
    spec_1d = compute_torus_spectrum(d=1, k_max=K_MAX, L=2*math.pi*R_PSI_FIDUCIAL)
    classification_1d = classify_mode_degeneracy(spec_1d)

    # --- 2D torus T^2(R_t x R_psi) ---
    spec_2d = compute_torus_spectrum(d=D_TORUS, k_max=K_MAX, L=2*math.pi*R_PSI_FIDUCIAL)
    classification_2d = classify_mode_degeneracy(spec_2d)

    # --- Zero modes and massless DoF ---
    zero_degen_1d = identify_zero_modes(spec_1d)
    zero_degen_2d = identify_zero_modes(spec_2d)
    massless_theta_dof = theta_zero_mode_dof(N_THETA_DOF)

    # --- Poisson duality check ---
    poisson = poisson_duality_check(R=R_PSI_FIDUCIAL)

    # --- Spectral gap ---
    gap_1d = get_lowest_nonzero_eigenvalue(d=1, L=2*math.pi*R_PSI_FIDUCIAL)
    gap_2d = get_lowest_nonzero_eigenvalue(d=D_TORUS, L=2*math.pi*R_PSI_FIDUCIAL)

    results = {
        'R_psi': R_PSI_FIDUCIAL,
        'd_torus': D_TORUS,
        'k_max': K_MAX,
        'spectrum_1d': spec_1d[:20],   # store first 20 levels
        'spectrum_2d': spec_2d[:20],
        'classification_1d': classification_1d,
        'classification_2d': classification_2d,
        'zero_mode_degeneracy_1d': zero_degen_1d,
        'zero_mode_degeneracy_2d': zero_degen_2d,
        'massless_theta_dof': massless_theta_dof,
        'spectral_gap_1d': gap_1d,
        'spectral_gap_2d': gap_2d,
        'poisson_check': poisson,
        'n_theta_dof': N_THETA_DOF,
    }

    if verbose:
        _print_report(results)

    return results


def _print_report(results: dict) -> None:
    """Print formatted scan report to stdout."""
    sep = "=" * 70
    print(sep)
    print("UBT Theta-FIELD EIGENMODE SCAN  (v28)")
    print(sep)
    print(f"  Torus dimension  : d = {results['d_torus']}")
    print(f"  Fiducial radius  : R_psi = {results['R_psi']:.4f}")
    print(f"  Mode cutoff      : |k| <= {results['k_max']}")
    print(f"  Theta real DoF   : {results['n_theta_dof']}")
    print()

    print("-- 1D psi-CIRCLE SPECTRUM (first 12 levels) --")
    print(f"  {'Level':>6}  {'lambda':>14}  {'deg':>5}  {'type':>10}")
    for i, (lam, deg) in enumerate(results['spectrum_1d'][:12]):
        mtype = "ZERO" if lam < 1e-12 else ""
        print(f"  {i:>6}  {lam:>14.6f}  {int(deg):>5}  {mtype:>10}")
    print(f"  Spectral gap Delta_1 = {results['spectral_gap_1d']:.6f}")
    print(f"  Zero-mode degeneracy = {results['zero_mode_degeneracy_1d']}")
    print()

    print("-- 2D T^2 SPECTRUM (first 12 levels) --")
    print(f"  {'Level':>6}  {'lambda':>14}  {'deg':>5}")
    for i, (lam, deg) in enumerate(results['spectrum_2d'][:12]):
        print(f"  {i:>6}  {lam:>14.6f}  {int(deg):>5}")
    print(f"  Spectral gap Delta_2 = {results['spectral_gap_2d']:.6f}")
    print(f"  Zero-mode degeneracy = {results['zero_mode_degeneracy_2d']}")
    print()

    print("-- ZERO MODES (DARK RADIATION CANDIDATES) --")
    print(f"  Massless modes from Theta zero modes : {results['massless_theta_dof']}")
    print(f"  (One per real DoF of Theta field, geometry-dictated)")
    print()

    print("-- POISSON DUALITY CHECK --")
    pc = results['poisson_check']
    status = "PASS" if pc['passes'] else "FAIL"
    print(f"  Spectral sum S = {pc['spectral_sum']:.8f}")
    print(f"  Winding  sum W = {pc['winding_sum']:.8f}")
    print(f"  Ratio W/S      = {pc['ratio']:.8f}  (expected R = {pc['expected_ratio']:.8f})")
    print(f"  Status: {status}")
    print()
    print(sep)


if __name__ == '__main__':
    run_scan(verbose=True)
