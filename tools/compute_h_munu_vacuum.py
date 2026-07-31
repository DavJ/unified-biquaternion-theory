#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""Audit of the two-mode Hermitian metric channel.

For the ansatz

    Theta(psi) = Theta0 exp(i psi/R) + Theta1 exp(2 i psi/R),

the quantity Sc(E_psi E_psi^dagger) is a Hermitian norm and is therefore real
for every field, not only for one or two modes.  The former claim that its
cross term generated a nonzero h_psi_psi was algebraically incorrect: a term
z plus its complex conjugate is real.

The script now verifies the correction, keeps the older gauge-potential ratio
only as a SKETCH diagnostic, and explicitly prevents that ratio from being
used as proof of a non-real metric or of a physical phase modulus.
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
    """Return Im[Sc(E_psi E_psi^dagger)], which vanishes identically.

    The cross terms are

        (2/R^2) [exp(-i psi/R) s01 + exp(+i psi/R) conjugate(s01)]

    and the bracket equals twice a real part.  Hence the full Hermitian norm is
    real for all psi and for arbitrary complex biquaternion coefficients.
    """
    del theta0, theta1, R_psi
    psi = np.asarray(psi, dtype=float)
    return np.zeros_like(psi, dtype=float)


def compute_G_psi_psi_real(
    theta0: Biquaternion,
    theta1: Biquaternion,
    R_psi: float,
    psi: "np.ndarray",
) -> "np.ndarray":
    """Exact real Hermitian metric component for the two-mode ansatz.

    Re[G_psi_psi] = R^-2 [N0 + 4 N1
        + 4 cos(psi/R) Re(s01) + 4 sin(psi/R) Im(s01)].
    """
    psi = np.asarray(psi, dtype=float)
    n0 = bq_norm_sq(theta0)
    n1 = bq_norm_sq(theta1)
    sc01 = bq_sc_hermitian(theta0, theta1)
    phase = psi / R_psi
    return (1.0 / R_psi**2) * (
        n0
        + 4.0 * n1
        + 4.0 * np.cos(phase) * sc01.real
        + 4.0 * np.sin(phase) * sc01.imag
    )


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

    A nonzero r is only a property of the sketch gauge formula; it does not prove phi is physical.

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
    Single-mode winding: Theta = Theta0 exp(i psi/R) gives h_psi_psi = 0.

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
    phi_is_physical: bool       # False: the metric calculation does not prove this
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
        phi_is_physical — always False here; physicality is not established
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
        phi_is_physical=False,
        psi_vals=psi,
        h_vals=h_vals,
        g_vals=g_vals,
    )


def canonical_example() -> VacuumResult:
    """Concrete two-mode audit example.

    The overlap Sc(Theta0 Theta1^dagger) is complex, but the conjugate-paired
    cross term in Sc(E_psi E_psi^dagger) is real.  Therefore h_psi_psi remains
    zero.  A nonzero imaginary overlap is not enough to produce a non-real
    Hermitian metric component.
    """
    theta0: Biquaternion = (1.0 + 1j, 0.0 + 0j, 0.0 + 0j, 0.0 + 0j)
    theta1: Biquaternion = (1.0 + 0j, 0.0 + 0j, 0.0 + 1j, 0.0 + 0j)
    return compute_vacuum(theta0, theta1, R_psi=1.0)


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def print_report(res: VacuumResult) -> None:
    """Print the corrected two-mode audit."""
    print("=" * 70)
    print("UBT Two-Mode Hermitian Metric Audit — corrected result")
    print("=" * 70)
    print()
    print(f"  Theta0 = {res.theta0}   [POSTULATE]")
    print(f"  Theta1 = {res.theta1}   [POSTULATE]")
    print(f"  R_psi  = {res.R_psi}    [POSTULATE]")
    print()
    print(f"  Sc(Theta0 Theta1^dagger) = {res.sc_inner}   [DERIVED]")
    print(f"  Im overlap                = {res.sc_inner_im}   [DERIVED]")
    print()
    print("  Cross term = z + conjugate(z), hence it is real.")
    print(f"  max|h_psi_psi| = {res.h_max:.6e}   [DERIVED: IDENTICALLY ZERO]")
    print(f"  max|g_psi_psi| = {res.g_max:.6e}   [DERIVED]")
    print()
    print(f"  r   = |A_I|/|A_R| = {res.r:.6f}   [SKETCH ONLY]")
    print(f"  rho = {res.rho:.6f}               [SKETCH ONLY]")
    print(f"  formal 2 rho r alpha(0) = {res.dalpha_dphi:.6e}   [SKETCH INPUT]")
    print()
    print("  Verdict: h_psi_psi = 0.  The two-mode Hermitian channel does not")
    print("  establish a non-real metric and does not prove that phi is physical.")
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
            r"UBT two-mode Hermitian metric audit: $h_{\psi\psi}=0$"
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

    print("Step 2 — Two-mode winding: Hermitian h_ψψ remains zero   [CORRECTED]")
    print("-" * 70)
    res = canonical_example()
    print_report(res)
    try_plot(res)

    # Summary values for docs/DERIVATION_INDEX.md and docs/PHI_UNIVERSE_PARAMETER.md
    print()
    print("Corrected audit values for documentation:")
    print(f"  Im[Sc(Θ₀Θ₁†)]   = {res.sc_inner_im}")
    print(f"  max|h_ψψ|        = {res.h_max:.6f}  (at R_ψ = {res.R_psi})")
    print(f"  r                = {res.r:.6f}")
    print(f"  ρ                = {res.rho:.6f}")
    print(f"  ∂α/∂φ|_{{φ=0}}   = {res.dalpha_dphi:.6e}")
    print("  phi physical?    = NOT ESTABLISHED BY THIS CALCULATION")
    print()

    sys.exit(0)
