#!/usr/bin/env python3
# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
compute_dalpha_dphi.py — Plot α(φ) for the UBT vacuum solution.

GAP 3: Is φ physical or gauge?  Compute ∂α/∂φ.

From canonical/geometry/phi_gauge_vs_physical.tex [DERIVED]:

    α(φ) = α(0) · [cos²(φ) + 2ρ·r·cos(φ)sin(φ) + r²·sin²(φ)]

    ∂α/∂φ|_{φ=0} = 2ρ·r·α(0)

where:
    r   = |𝒜ᴵ_μ| / |𝒜ᴿ_μ|    (imaginary-to-real amplitude ratio)
    ρ   = correlation coefficient between 𝒜ᴿ and 𝒜ᴵ

Decision:
    r = 0  →  ∂α/∂φ = 0  →  φ is pure gauge   (flat vacuum)
    r ≠ 0  →  ∂α/∂φ ≠ 0  →  φ is physical     (biquaternionic vacuum)

Layer: [L1] — biquaternionic geometry
Classification: [DERIVED] — see canonical/geometry/phi_gauge_vs_physical.tex
"""

from __future__ import annotations

import math
import sys
from typing import Tuple

import numpy as np


ALPHA_0 = 1.0 / 137.035999177  # CODATA 2022 fine structure constant


# ---------------------------------------------------------------------------
# Core formula  [DERIVED]
# ---------------------------------------------------------------------------

def alpha_of_phi(
    phi: "np.ndarray",
    alpha_0: float = ALPHA_0,
    r: float = 0.0,
    rho: float = 0.0,
) -> "np.ndarray":
    """
    Compute α(φ) for the UBT vacuum.

    Formula [DERIVED — canonical/geometry/phi_gauge_vs_physical.tex eq.(9)]:

        α(φ) = α(0) · [cos²φ + 2ρ·r·cosφ·sinφ + r²·sin²φ]

    Args:
        phi:    Array of phase angles φ ∈ [0, 2π).
        alpha_0: α(0) — fine structure constant at φ=0.
        r:      Imaginary-to-real amplitude ratio |𝒜ᴵ|/|𝒜ᴿ|.
        rho:    Correlation coefficient ρ ∈ [-1, 1].

    Returns:
        α(φ) array.

    Classification: [DERIVED]
    """
    phi = np.asarray(phi, dtype=float)
    c = np.cos(phi)
    s = np.sin(phi)
    return alpha_0 * (c**2 + 2.0 * rho * r * c * s + r**2 * s**2)


def dalpha_dphi_at_zero(
    alpha_0: float = ALPHA_0,
    r: float = 0.0,
    rho: float = 0.0,
) -> float:
    """
    Compute ∂α/∂φ|_{φ=0}.

    Formula [DERIVED — canonical/geometry/phi_gauge_vs_physical.tex eq.(10)]:

        ∂α/∂φ|_{φ=0} = 2ρ·r·α(0)

    Returns:
        Scalar ∂α/∂φ at φ=0.  Zero if r=0 (φ is pure gauge).
    """
    return 2.0 * rho * r * alpha_0


def phi_status(r: float, rho: float) -> str:
    """
    Return the status of φ: 'pure gauge' or 'physical (moduli)'.

    Classification: [DERIVED]
    """
    if abs(r) < 1e-12:
        return "pure gauge  (∂α/∂φ = 0)"
    else:
        return f"physical  (∂α/∂φ|_{{φ=0}} = {dalpha_dphi_at_zero(r=r, rho=rho):.4e})"


# ---------------------------------------------------------------------------
# UBT vacuum parameter extraction
# ---------------------------------------------------------------------------

def ubt_flat_vacuum_params() -> Tuple[float, float]:
    """
    Parameters for the UBT flat (Minkowski) vacuum.

    𝒰_μν = η_μν  (real, no imaginary component h_μν = 0)
    → r = 0, ρ = 0.

    Returns:
        (r, rho)   [DERIVED]
    """
    return 0.0, 0.0


def ubt_biquaternionic_vacuum_params(h_over_g: float = 0.1) -> Tuple[float, float]:
    """
    Parameters for a generic biquaternionic vacuum with h_μν ≠ 0.

    For simplicity, assume:
        𝒜ᴿ and 𝒜ᴵ are proportional: ρ = 1 (maximal correlation).
        r = |h_μν| / |g_μν| ≈ h_over_g.

    Args:
        h_over_g:  Ratio |h_μν|/|g_μν| (imaginary-to-real metric component ratio).

    Returns:
        (r, rho)   [CONJECTURE — full computation requires explicit vacuum solution]
    """
    return h_over_g, 1.0  # ρ=1 conservative upper bound; [CONJECTURE]


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------

def analyse_phi_parameter(
    r: float = 0.0,
    rho: float = 0.0,
    alpha_0: float = ALPHA_0,
    n_points: int = 1000,
    verbose: bool = True,
    save_plot: bool = False,
    plot_path: str = "/tmp/alpha_vs_phi.png",
) -> dict:
    """
    Compute and optionally plot α(φ) for given UBT vacuum parameters.

    Args:
        r:          Imaginary-to-real amplitude ratio.
        rho:        Correlation coefficient.
        alpha_0:    α at φ=0.
        n_points:   Number of φ values.
        verbose:    Print results.
        save_plot:  Save plot to file.
        plot_path:  Output file path.

    Returns:
        dict with analysis results.
    """
    phi_vals = np.linspace(0, 2 * math.pi, n_points, endpoint=False)
    alpha_vals = alpha_of_phi(phi_vals, alpha_0=alpha_0, r=r, rho=rho)
    deriv = dalpha_dphi_at_zero(alpha_0=alpha_0, r=r, rho=rho)
    status = phi_status(r, rho)

    # Evaluate at φ₁₃₇ = 2π/137
    phi_137 = 2.0 * math.pi / 137
    alpha_137 = float(alpha_of_phi(np.array([phi_137]), alpha_0=alpha_0, r=r, rho=rho)[0])
    alpha_inv_137 = 1.0 / alpha_137 if alpha_137 != 0 else float("inf")

    result = {
        "r": r,
        "rho": rho,
        "alpha_0": alpha_0,
        "alpha_inv_0": 1.0 / alpha_0,
        "dalpha_dphi_at_0": deriv,
        "phi_status": status,
        "phi_137_rad": phi_137,
        "alpha_at_phi_137": alpha_137,
        "alpha_inv_at_phi_137": alpha_inv_137,
        "alpha_max": float(np.max(alpha_vals)),
        "alpha_min": float(np.min(alpha_vals)),
        "alpha_variation": float(np.max(alpha_vals) - np.min(alpha_vals)),
    }

    if verbose:
        alpha_inv_0 = result["alpha_inv_0"]
        alpha_inv_at_phi_137 = result["alpha_inv_at_phi_137"]
        print("=" * 65)
        print("∂α/∂φ Computation — UBT Gap 3")
        print("=" * 65)
        print(f"Input parameters:")
        print(f"  r   = {r}    (imaginary-to-real amplitude ratio)")
        print(f"  ρ   = {rho}   (correlation coefficient)")
        print(f"  α(0) = 1/{alpha_inv_0:.6f}  (CODATA 2022)")
        print()
        print(f"Result [DERIVED]:")
        print(f"  ∂α/∂φ|_{{φ=0}} = {deriv:.4e}")
        print(f"  φ status: {status}")
        print()
        print(f"α(φ₁₃₇) at φ₁₃₇ = 2π/137:")
        print(f"  α(φ₁₃₇) = 1/{alpha_inv_at_phi_137:.6f}")
        print(f"  Experimental: 1/137.035999177")
        print()
        if abs(r) < 1e-12:
            print("  → φ is PURE GAUGE: ∂α/∂φ|_{φ=0} = 0 (no first-order variation).  [DERIVED]")
            print("  (α(φ)=α(0)·cos²φ varies globally, but the linearised gauge invariant vanishes.)")
        else:
            print(f"  → φ is PHYSICAL: α varies with φ.  [DERIVED]")
            print(f"  α variation: {result['alpha_variation']:.4e}")
        print("=" * 65)

    if save_plot:
        try:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt

            fig, axes = plt.subplots(1, 2, figsize=(12, 5))

            ax1 = axes[0]
            ax1.plot(phi_vals, 1.0 / alpha_vals, "b-", linewidth=1.5)
            ax1.axvline(phi_137, color="red", linestyle="--",
                        label=r"$\varphi_{137} = 2\pi/137$")
            ax1.axhline(137.035999177, color="gray", linestyle=":",
                        label=r"Experimental $\alpha^{-1}$")
            ax1.set_xlabel(r"$\varphi$ (rad)")
            ax1.set_ylabel(r"$\alpha^{-1}(\varphi)$")
            ax1.set_title(fr"$\alpha^{{-1}}(\varphi)$ — UBT vacuum (r={r}, ρ={rho})")
            ax1.legend()
            ax1.grid(True, alpha=0.3)

            ax2 = axes[1]
            ax2.plot(phi_vals, alpha_vals, "g-", linewidth=1.5)
            ax2.axvline(phi_137, color="red", linestyle="--",
                        label=r"$\varphi_{137} = 2\pi/137$")
            ax2.set_xlabel(r"$\varphi$ (rad)")
            ax2.set_ylabel(r"$\alpha(\varphi)$")
            flat_label = "flat (φ gauge)" if abs(r) < 1e-12 else "varies (φ physical)"
            ax2.set_title(fr"$\alpha(\varphi)$ — {flat_label}")
            ax2.legend()
            ax2.grid(True, alpha=0.3)

            plt.tight_layout()
            plt.savefig(plot_path, dpi=150, bbox_inches="tight")
            print(f"Plot saved to {plot_path}")
            plt.close(fig)
        except ImportError:
            print("matplotlib not available; skipping plot.")

    return result


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Compute ∂α/∂φ for UBT vacuum — GAP 3.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python compute_dalpha_dphi.py              # flat vacuum (r=0): φ is gauge
  python compute_dalpha_dphi.py --r 0.1     # biquaternionic vacuum: φ is physical
  python compute_dalpha_dphi.py --r 0.1 --rho 0.5 --plot
""",
    )
    parser.add_argument("--r", type=float, default=0.0,
                        help="Imaginary-to-real amplitude ratio r=|𝒜ᴵ|/|𝒜ᴿ| (default: 0)")
    parser.add_argument("--rho", type=float, default=0.0,
                        help="Correlation coefficient ρ ∈ [-1,1] (default: 0)")
    parser.add_argument("--alpha0", type=float, default=ALPHA_0,
                        help="α(0) value (default: CODATA 2022)")
    parser.add_argument("--plot", action="store_true",
                        help="Save α(φ) plot to /tmp/alpha_vs_phi.png")
    parser.add_argument("--plot-path", type=str, default="/tmp/alpha_vs_phi.png",
                        help="Output plot path")
    parser.add_argument("--quiet", action="store_true",
                        help="Suppress verbose output")
    parser.add_argument("--biquat-vacuum", type=float, default=None, metavar="H_OVER_G",
                        help="Use biquaternionic vacuum with h/g ratio (sets r=H_OVER_G, rho=1)")
    args = parser.parse_args()

    if args.biquat_vacuum is not None:
        r, rho = ubt_biquaternionic_vacuum_params(args.biquat_vacuum)
    else:
        r, rho = args.r, args.rho

    result = analyse_phi_parameter(
        r=r,
        rho=rho,
        alpha_0=args.alpha0,
        verbose=not args.quiet,
        save_plot=args.plot,
        plot_path=args.plot_path,
    )

    # Exit code: 0 if φ is pure gauge (r=0), 1 if physical (r≠0)
    raise SystemExit(0 if abs(result["dalpha_dphi_at_0"]) < 1e-15 else 1)


if __name__ == "__main__":
    main()
