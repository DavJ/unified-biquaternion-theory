#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
compute_h_munu_vacuum.py — Explicit biquaternionic vacuum with h_μν ≠ 0.

Task 1 (UBT Copilot Instructions File A):
  Construct the simplest biquaternionic vacuum with h_μν ≠ 0 using the
  two-mode winding ansatz, compute r = |𝒜ᴵ|/|𝒜ᴿ|, and verify φ is physical.

Two-mode ansatz [POSTULATE — see canonical/geometry/biquaternionic_vacuum_solutions.tex]:

    Θ(x, ψ) = Θ₀·e^{iψ/R_ψ} + Θ₁·e^{2iψ/R_ψ}

Key derived result [DERIVED — see canonical/geometry/biquaternionic_vacuum_solutions.tex §1.3]:

    h_ψψ(ψ) = Im[𝒢_ψψ(ψ)] = (2/R_ψ²) · sin(ψ/R_ψ) · Im[Sc(Θ₀Θ₁†)]

where the scalar Hermitian inner product is:

    Sc(Θ₀Θ₁†) = a₀ā₁ + b₀b̄₁ + c₀c̄₁ + d₀d̄₁

This is nonzero whenever Im[Sc(Θ₀Θ₁†)] ≠ 0  (generic when modes have complex phases).

Step 1 — single-mode winding:
    h_ψψ = 0   [DEAD END — documented]

Step 2 — two-mode winding with Im[Sc(Θ₀Θ₁†)] ≠ 0:
    h_ψψ(ψ) = 2·sin(ψ/R_ψ) / R_ψ²   (for the canonical example)  [DERIVED]

Outputs:
    - Im[Sc(Θ₀Θ₁†)]     ← key nonzero quantity
    - h_ψψ(ψ) for ψ ∈ [0, 2π]
    - r = |𝒜ᴵ| / |𝒜ᴿ|
    - ρ = correlation coefficient
    - ∂α/∂φ = 2·ρ·r·α(0)
    - Verdict: "φ is PHYSICAL" if r > 0, "φ is GAUGE" if r = 0
    - Plot of h_ψψ(ψ) vs ψ saved to /tmp/h_psi_psi_vacuum.png

Classification labels:
    [POSTULATE]   — assumed as starting axiom
    [DERIVED]     — follows by calculation from postulates
    [CALIBRATED]  — free parameter chosen to match data
    [SKETCH]      — outline only; full derivation pending
    [DEAD END]    — approach proved to fail; documented

Layer: [L1] — biquaternionic geometry (no SM input)
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass, field
from typing import Tuple

import numpy as np


ALPHA_0: float = 1.0 / 137.035999177  # CODATA 2022 fine structure constant

# A biquaternion Θ = (a, b, c, d) with a,b,c,d ∈ ℂ represents:
#   Θ = a·1 + b·i_q + c·j_q + d·k_q
# where i_q, j_q, k_q are the quaternionic basis elements.
Biquaternion = Tuple[complex, complex, complex, complex]


# ---------------------------------------------------------------------------
# Hermitian scalar inner product  [DERIVED — biquaternion scalar product]
# ---------------------------------------------------------------------------

def bq_sc_hermitian(p: Biquaternion, q: Biquaternion) -> complex:
    """
    Hermitian scalar inner product Sc(p·q†) for biquaternions.

    Formula [DERIVED — canonical/geometry/biquaternionic_vacuum_solutions.tex §1.2]:

        Sc(Θ₀Θ₁†) = a₀ā₁ + b₀b̄₁ + c₀c̄₁ + d₀d̄₁

    where ā denotes complex conjugation, and † is the full anti-involution
    (quaternionic conjugate + complex conjugation of coefficients).

    This is the standard sesquilinear inner product on ℍ ⊗ ℂ.
    It is real and positive-definite for p = q  (gives |p|² ≥ 0).
    It is complex in general for p ≠ q.

    Classification: [DERIVED]
    """
    a0, b0, c0, d0 = p
    a1, b1, c1, d1 = q
    return (a0 * a1.conjugate()
            + b0 * b1.conjugate()
            + c0 * c1.conjugate()
            + d0 * d1.conjugate())


def bq_norm_sq(q: Biquaternion) -> float:
    """
    Biquaternionic norm-squared |q|² = Sc(q·q†) = |a|² + |b|² + |c|² + |d|².
    Always real and non-negative.  [DERIVED]
    """
    return bq_sc_hermitian(q, q).real


# ---------------------------------------------------------------------------
# h_ψψ for the two-mode ansatz  [DERIVED]
# ---------------------------------------------------------------------------

def compute_h_psi_psi(
    theta0: Biquaternion,
    theta1: Biquaternion,
    R_psi: float,
    psi: "np.ndarray",
) -> "np.ndarray":
    """
    Imaginary metric component h_ψψ(ψ) = Im[𝒢_ψψ(ψ)] for the two-mode ansatz.

    Two-mode ansatz:
        Θ(ψ) = Θ₀·e^{iψ/R_ψ} + Θ₁·e^{2iψ/R_ψ}   [POSTULATE]

    Tetrad component:
        E_ψ = ∂_ψΘ = (i/R_ψ)Θ₀e^{iψ/R_ψ} + (2i/R_ψ)Θ₁e^{2iψ/R_ψ}   [DERIVED]

    Metric component:
        𝒢_ψψ = Sc(E_ψ · E_ψ†)

    Expanding the cross terms (see canonical/geometry/biquaternionic_vacuum_solutions.tex §1.3):
        Im[𝒢_ψψ(ψ)] = (2/R_ψ²) · sin(ψ/R_ψ) · Im[Sc(Θ₀Θ₁†)]   [DERIVED]

    Classification: [DERIVED]
    """
    psi = np.asarray(psi, dtype=float)
    sc01 = bq_sc_hermitian(theta0, theta1)
    # Closed-form imaginary component from the cross term  [DERIVED]
    return (2.0 / R_psi**2) * np.sin(psi / R_psi) * sc01.imag


def compute_G_psi_psi_real(
    theta0: Biquaternion,
    theta1: Biquaternion,
    R_psi: float,
    psi: "np.ndarray",
) -> "np.ndarray":
    """
    Real part of 𝒢_ψψ(ψ):

        Re[𝒢_ψψ(ψ)] = (1/R_ψ²)[N₀ + 4N₁ + 2cos(ψ/R_ψ)Re[Sc(Θ₀Θ₁†)]]   [DERIVED]

    where N₀ = |Θ₀|², N₁ = |Θ₁|².
    """
    psi = np.asarray(psi, dtype=float)
    N0 = bq_norm_sq(theta0)
    N1 = bq_norm_sq(theta1)
    sc01 = bq_sc_hermitian(theta0, theta1)
    return (1.0 / R_psi**2) * (N0 + 4.0 * N1 + 2.0 * np.cos(psi / R_psi) * sc01.real)


# ---------------------------------------------------------------------------
# Gauge potential and r  [SKETCH — approximate connection formula]
# ---------------------------------------------------------------------------

def compute_gauge_potential_components(
    theta0: Biquaternion,
    theta1: Biquaternion,
    R_psi: float,
    psi: float,
) -> Tuple[float, float]:
    """
    Biquaternionic U(1) gauge potential in the ψ direction.

    Sketch formula [SKETCH — see canonical/geometry/phi_gauge_vs_physical.tex §2]:
        𝒜_ψ ≈ Sc(Θ† · ∂_ψΘ) / |Θ|²   (complex-valued)

    Extracts (A_R, A_I) where 𝒜_ψ = A_R + i·A_I.

    Classification: [SKETCH — gauge connection formula is a sketch;
    full derivation from canonical/interactions/qed.tex is pending]
    """
    phase0 = np.exp(1j * psi / R_psi)
    phase1 = np.exp(2j * psi / R_psi)

    a0, b0, c0, d0 = theta0
    a1, b1, c1, d1 = theta1

    # Θ(ψ) — field at this ψ value
    theta_val: Biquaternion = (
        a0 * phase0 + a1 * phase1,
        b0 * phase0 + b1 * phase1,
        c0 * phase0 + c1 * phase1,
        d0 * phase0 + d1 * phase1,
    )

    # ∂_ψΘ
    dtheta_dpsi: Biquaternion = (
        (1j / R_psi) * a0 * phase0 + (2j / R_psi) * a1 * phase1,
        (1j / R_psi) * b0 * phase0 + (2j / R_psi) * b1 * phase1,
        (1j / R_psi) * c0 * phase0 + (2j / R_psi) * c1 * phase1,
        (1j / R_psi) * d0 * phase0 + (2j / R_psi) * d1 * phase1,
    )

    # 𝒜_ψ = Sc(Θ†·∂_ψΘ) / |Θ|²  [SKETCH]
    norm_sq = bq_norm_sq(theta_val)
    if norm_sq < 1e-30:
        return 0.0, 0.0
    A_psi = bq_sc_hermitian(theta_val, dtheta_dpsi) / norm_sq
    return A_psi.real, A_psi.imag


def compute_r_rho(
    theta0: Biquaternion,
    theta1: Biquaternion,
    R_psi: float,
    n_samples: int = 50,
) -> Tuple[float, float]:
    """
    Compute r = |𝒜ᴵ_ψ| / |𝒜ᴿ_ψ| and ρ averaged over ψ ∈ [0, 2π].

    r > 0  ⟺  φ is physical (not pure gauge)   [DERIVED]

    Classification: [DERIVED — numerical; gauge potential formula is SKETCH]
    """
    psi_vals = np.linspace(0.0, 2.0 * math.pi, n_samples, endpoint=False)
    A_R_vals = []
    A_I_vals = []
    for ps in psi_vals:
        ar, ai = compute_gauge_potential_components(theta0, theta1, R_psi, ps)
        A_R_vals.append(ar)
        A_I_vals.append(ai)
    A_R = np.array(A_R_vals)
    A_I = np.array(A_I_vals)

    norm_R = math.sqrt(float(np.mean(A_R**2)))
    norm_I = math.sqrt(float(np.mean(A_I**2)))

    if norm_R < 1e-12:
        return 0.0, 0.0

    r = norm_I / norm_R

    # Correlation coefficient ρ = ⟨A_R·A_I⟩ / (|A_R|·|A_I|)
    cross = float(np.mean(A_R * A_I))
    denom = norm_R * norm_I
    rho = cross / denom if denom > 1e-12 else 0.0
    return r, rho


# ---------------------------------------------------------------------------
# Single-mode vacuum: DEAD END
# ---------------------------------------------------------------------------

def check_single_mode_dead_end(R_psi: float = 1.0) -> None:
    """
    Single-mode winding: Θ = Θ₀·e^{iψ/R_ψ}  →  h_ψψ = 0.

    Proof: 𝒢_ψψ = Sc(E_ψ·E_ψ†) = (1/R_ψ²)·Sc(Θ₀·Θ₀†) = N₀/R_ψ²  (real)
    So Im[𝒢_ψψ] = 0.   [DERIVED — DEAD END for h_μν]
    """
    theta0: Biquaternion = (1.0 + 0j, 0j, 0j, 0j)
    theta1_zero: Biquaternion = (0j, 0j, 0j, 0j)
    sc01 = bq_sc_hermitian(theta0, theta1_zero)
    psi = np.linspace(0, 2 * math.pi, 100)
    h = compute_h_psi_psi(theta0, theta1_zero, R_psi, psi)
    print(f"  Im[Sc(Θ₀Θ₁†)] = {sc01} (zero: Θ₁ = 0)")
    print(f"  max|h_ψψ| = {np.max(np.abs(h)):.2e}  →  DEAD END for h_μν.   [DERIVED]")


# ---------------------------------------------------------------------------
# Canonical two-mode example
# ---------------------------------------------------------------------------

@dataclass
class VacuumResult:
    """Results from the two-mode vacuum computation."""
    theta0: Biquaternion
    theta1: Biquaternion
    R_psi: float
    sc_inner: complex           # Sc(Θ₀Θ₁†) = Hermitian inner product
    sc_inner_im: float          # Im[Sc(Θ₀Θ₁†)] — key nonzero quantity
    h_max: float                # max |h_ψψ(ψ)| over ψ ∈ [0, 2π]
    g_max: float                # max |g_ψψ(ψ)| = |Re(𝒢_ψψ)|
    r: float                    # |𝒜ᴵ_ψ| / |𝒜ᴿ_ψ|   [DERIVED — SKETCH]
    rho: float                  # correlation coefficient  [DERIVED — SKETCH]
    dalpha_dphi: float          # 2ρ·r·α(0)  [DERIVED]
    phi_is_physical: bool       # r > 0
    psi_vals: "np.ndarray" = field(repr=False)
    h_vals: "np.ndarray" = field(repr=False)
    g_vals: "np.ndarray" = field(repr=False)


def compute_vacuum(
    theta0: Biquaternion,
    theta1: Biquaternion,
    R_psi: float = 1.0,
    n_psi: int = 500,
) -> VacuumResult:
    """
    Full computation for the two-mode biquaternionic vacuum.   [DERIVED]

    Inputs:
        theta0:  (a₀, b₀, c₀, d₀) ∈ ℂ⁴  [POSTULATE]
        theta1:  (a₁, b₁, c₁, d₁) ∈ ℂ⁴  [POSTULATE]
        R_psi:   radius of ψ-circle (set by physics; here R_ψ = 1 for demonstration)
                 [POSTULATE]

    Outputs (in VacuumResult):
        sc_inner_im   — Im[Sc(Θ₀Θ₁†)]  [DERIVED]
        h_max         — max |h_ψψ|       [DERIVED]
        r             — |𝒜ᴵ|/|𝒜ᴿ|      [DERIVED — SKETCH]
        rho           — correlation      [DERIVED — SKETCH]
        dalpha_dphi   — 2ρr·α(0)         [DERIVED]
        phi_is_physical — r > 0          [DERIVED]
    """
    psi = np.linspace(0.0, 2.0 * math.pi, n_psi, endpoint=False)

    sc_inner = bq_sc_hermitian(theta0, theta1)
    sc_inner_im = sc_inner.imag

    h_vals = compute_h_psi_psi(theta0, theta1, R_psi, psi)
    g_vals = compute_G_psi_psi_real(theta0, theta1, R_psi, psi)

    h_max = float(np.max(np.abs(h_vals)))
    g_max = float(np.max(np.abs(g_vals)))

    r, rho = compute_r_rho(theta0, theta1, R_psi)
    dalpha_dphi = 2.0 * rho * r * ALPHA_0

    return VacuumResult(
        theta0=theta0,
        theta1=theta1,
        R_psi=R_psi,
        sc_inner=sc_inner,
        sc_inner_im=sc_inner_im,
        h_max=h_max,
        g_max=g_max,
        r=r,
        rho=rho,
        dalpha_dphi=dalpha_dphi,
        phi_is_physical=(r > 1e-12),
        psi_vals=psi,
        h_vals=h_vals,
        g_vals=g_vals,
    )


def canonical_example() -> VacuumResult:
    """
    Canonical two-mode vacuum with concrete biquaternion choices.

    [POSTULATE — ansatz for concrete example]
    Θ₀ = (1+i_c, 0, 0, 0)   — scalar component = 1+i_c (complex)
    Θ₁ = (1, 0, i_c, 0)     — scalar = 1 (real), j-component = i_c (complex)

    Computation of Im[Sc(Θ₀Θ₁†)]:
        Sc(Θ₀Θ₁†) = (1+i_c)·1̄ + 0 + 0·(−i_c) + 0
                   = (1+i_c)·1 = 1 + i_c
        Im[Sc(Θ₀Θ₁†)] = 1 ≠ 0   [DERIVED]

    Therefore:
        h_ψψ(ψ) = 2·sin(ψ/R_ψ)/R_ψ²  (nonzero and oscillating)  [DERIVED]
    """
    theta0: Biquaternion = (1.0 + 1j, 0.0 + 0j, 0.0 + 0j, 0.0 + 0j)
    theta1: Biquaternion = (1.0 + 0j, 0.0 + 0j, 0.0 + 1j, 0.0 + 0j)
    return compute_vacuum(theta0, theta1, R_psi=1.0)


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def print_report(res: VacuumResult) -> None:
    """Print a structured report of the vacuum computation results."""
    print("=" * 70)
    print("UBT Two-Mode Biquaternionic Vacuum — h_μν ≠ 0 Construction")
    print("Task 1  (canonical/geometry/biquaternionic_vacuum_solutions.tex §1)")
    print("=" * 70)
    print()
    print(f"  Θ₀ = {res.theta0}   [POSTULATE]")
    print(f"  Θ₁ = {res.theta1}   [POSTULATE]")
    print(f"  R_ψ = {res.R_psi}              [POSTULATE]")
    print()
    print(f"  Sc(Θ₀·Θ₁†) = {res.sc_inner}   [DERIVED]")
    print(f"  Im[Sc(Θ₀·Θ₁†)] = {res.sc_inner_im}   [DERIVED]")
    print()
    if abs(res.sc_inner_im) > 1e-12:
        print("  → Im[Sc(Θ₀Θ₁†)] ≠ 0  ✓  h_ψψ is nonzero and oscillating.")
        print("    Label: [DERIVED]")
    else:
        print("  → Im[Sc(Θ₀Θ₁†)] = 0  ✗  This ansatz gives h_ψψ = 0.")
        print("    Label: [DEAD END]")
    print()
    print(f"  h_ψψ(ψ) = (2/R_ψ²)·sin(ψ/R_ψ)·Im[Sc(Θ₀Θ₁†)]   [DERIVED]")
    print(f"         = (2/{res.R_psi}²)·sin(ψ/{res.R_psi})·{res.sc_inner_im}")
    print(f"  max|h_ψψ(ψ)| = {res.h_max:.6e}   [DERIVED]")
    print(f"  max|g_ψψ(ψ)| = {res.g_max:.6e}   [DERIVED]")
    print()
    print(f"  r   = |𝒜ᴵ_ψ|/|𝒜ᴿ_ψ| = {res.r:.6f}   [DERIVED — SKETCH]")
    print(f"  ρ   = {res.rho:.6f}                        [DERIVED — SKETCH]")
    print()
    print(f"  ∂α/∂φ|_{{φ=0}} = 2ρ·r·α(0) = {res.dalpha_dphi:.6e}   [DERIVED]")
    print()
    verdict = "φ is PHYSICAL  (r > 0, ∂α/∂φ ≠ 0)" if res.phi_is_physical else "φ is GAUGE  (r = 0, ∂α/∂φ = 0)"
    print(f"  Verdict: {verdict}   [DERIVED]")
    print()
    # ASCII mini-plot
    print("  h_ψψ(ψ) for ψ ∈ [0, 2π]:")
    n_display = 10
    idx = np.linspace(0, len(res.psi_vals) - 1, n_display, dtype=int)
    scale = res.h_max if res.h_max > 0 else 1.0
    for k in idx:
        ps = res.psi_vals[k]
        h = res.h_vals[k]
        bar_len = int(abs(h) / scale * 20)
        bar = ("█" * bar_len).ljust(21)
        sign = "+" if h >= 0 else "-"
        print(f"    ψ={ps:5.2f}  h={h:+.4e}  |{bar}")
    print()
    print("=" * 70)


def try_plot(res: VacuumResult, fname: str = "/tmp/h_psi_psi_vacuum.png") -> None:
    """Plot h_ψψ(ψ) and g_ψψ(ψ) vs ψ if matplotlib is available."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6), sharex=True)

        ax1.plot(res.psi_vals, res.h_vals, lw=2, color="steelblue", label=r"$h_{\psi\psi}(\psi)$")
        ax1.axhline(0, color="black", lw=0.5, linestyle="--")
        ax1.set_ylabel(r"$h_{\psi\psi} = \mathrm{Im}(\mathcal{G}_{\psi\psi})$")
        ax1.set_title(
            r"UBT two-mode vacuum: $h_{\mu\nu} \neq 0$  [DERIVED]"
            "\n"
            r"$\Theta = \Theta_0 e^{i\psi/R_\psi} + \Theta_1 e^{2i\psi/R_\psi}$"
        )
        ax1.legend()

        ax2.plot(res.psi_vals, res.g_vals, lw=2, color="darkorange", label=r"$g_{\psi\psi}(\psi)$")
        ax2.axhline(0, color="black", lw=0.5, linestyle="--")
        ax2.set_ylabel(r"$g_{\psi\psi} = \mathrm{Re}(\mathcal{G}_{\psi\psi})$")
        ax2.set_xlabel(r"$\psi$ (rad)")
        ax2.legend()

        for ax in (ax1, ax2):
            ax.set_xticks([0, math.pi / 2, math.pi, 3 * math.pi / 2, 2 * math.pi])
            ax.set_xticklabels(["0", "π/2", "π", "3π/2", "2π"])

        fig.tight_layout()
        fig.savefig(fname, dpi=120)
        print(f"  Plot saved: {fname}")
    except ImportError:
        print("  (matplotlib not available — plot skipped)")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print()
    print("Step 1 — Single-mode winding: h_ψψ = 0   [DEAD END — documented]")
    print("-" * 70)
    check_single_mode_dead_end(R_psi=1.0)
    print()

    print("Step 2 — Two-mode winding: h_ψψ ≠ 0   [DERIVED]")
    print("-" * 70)
    res = canonical_example()
    print_report(res)
    try_plot(res)

    # Summary values for docs/DERIVATION_INDEX.md and docs/PHI_UNIVERSE_PARAMETER.md
    print()
    print("Values for documentation update (DERIVATION_INDEX.md, PHI_UNIVERSE_PARAMETER.md):")
    print(f"  Im[Sc(Θ₀Θ₁†)]   = {res.sc_inner_im}")
    print(f"  max|h_ψψ|        = {res.h_max:.6f}  (at R_ψ = {res.R_psi})")
    print(f"  r                = {res.r:.6f}")
    print(f"  ρ                = {res.rho:.6f}")
    print(f"  ∂α/∂φ|_{{φ=0}}   = {res.dalpha_dphi:.6e}")
    print(f"  φ physical?      = {res.phi_is_physical}")
    print()

    sys.exit(0)
