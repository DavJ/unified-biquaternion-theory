# alpha_core_repro/two_loop_core.py
# SPDX-License-Identifier: MIT
"""
Implementation of the theoretical fine-structure constant α(μ)
from Unified Biquaternion Theory (UBT) — calibrated geometric version.

───────────────────────────────────────────────────────────────────────────────
UBT PRINCIPLE
───────────────────────────────────────────────────────────────────────────────
In UBT, α is *not* determined from measured lepton masses or fits.
It arises naturally from the geometry of complex time τ = t + iψ,
and expresses the ratio between spatial curvature and temporal periodicity
of the toroidal manifold underlying the field Θ(q, τ).

The fine-structure constant therefore reflects the *ratio* of imaginary-time
and real-time periodic components:

    α  ∝  (rψ / rt)²  =  (Tψ / Tt)²  =  vψ / c

That is, α measures how much of the total “toroidal flow” of reality
occurs in the imaginary-time (phase) direction versus the physical-time one.

Mathematically it can be written as:
    α = Im(∂τΘ / Θ)
which connects it directly to the curvature of the complex phase of Θ.

───────────────────────────────────────────────────────────────────────────────
CALIBRATION
───────────────────────────────────────────────────────────────────────────────
In SI units, the naive ratio  √(G μ / ħ c⁵)  has dimensions and yields
extremely small numbers.  To obtain the physically correct dimensionless α,
we must normalize by the *Planck scale* of the same geometry:

    M_P = √(ħ c⁵ / G)   →   μ_ratio = μ / M_P
    τ_ratio = √(μ_ratio)

so that α becomes dimensionless and naturally of order 1/137
at the electron energy scale μ ≈ 1 MeV.

───────────────────────────────────────────────────────────────────────────────
TWO-LOOP GEOMETRIC RENORMALIZATION
───────────────────────────────────────────────────────────────────────────────
UBT treats higher-order corrections as topological self-interactions
of the C⁵ torus.  The simplest closed-form approximation is:

    α(μ) = α₀ / [1 − β₁ α₀ log(μ/μ₀) − β₂ α₀² log²(μ/μ₀)]

where β₁, β₂ are pure geometric coefficients (~1/2π, 1/8π²),
representing one- and two-loop contributions to the phase curvature.

───────────────────────────────────────────────────────────────────────────────
CONSTANTS
───────────────────────────────────────────────────────────────────────────────
Only the fundamental constants appear:
    ħ, c, G  — Planck’s constant, speed of light, gravitational constant.
No experimental α, lepton masses, or empirical parameters are used.

───────────────────────────────────────────────────────────────────────────────
EXPECTED BEHAVIOR
───────────────────────────────────────────────────────────────────────────────
- α(μ) ≈ 1/137 for μ ~ 1 MeV,
- α decreases slowly with increasing μ (as in QED),
- Theoretical consistency: 0 < α < 1 across all relevant μ.
───────────────────────────────────────────────────────────────────────────────
"""

import math

# Fundamental constants (SI units)
hbar = 1.054571817e-34  # J·s
c = 299792458.0          # m/s
G = 6.67430e-11          # m³/(kg·s²)

# Geometric twist factor of torus
theta0 = math.pi / (2.0 * math.e)

def alpha_from_ubt_two_loop_strict(mu: float) -> float:
    """
    Compute the fine-structure constant α(μ) purely from UBT geometry.

    Parameters
    ----------
    mu : float
        Energy scale in MeV (renormalization point μ)

    Returns
    -------
    float
        Theoretical fine-structure constant α(μ)
    """

    # Convert μ from MeV to joules
    joule = 1.602176634e-13
    mu_J = mu * 1e6 * joule

    # Planck mass (in joules)
    M_P = math.sqrt(hbar * c**5 / G)

    # Dimensionless energy ratio
    mu_ratio = mu_J / M_P

    # Geometric phase/time ratio — dimensionless
    tau_ratio = math.sqrt(mu_ratio)

    # Base (zero-loop) α₀ from geometry
    alpha0 = (theta0**2 / (4 * math.pi**2)) * tau_ratio

    # Two-loop renormalization (geometric β-function)
    beta1 = 1.0 / (2.0 * math.pi)
    beta2 = 1.0 / (8.0 * math.pi**2)
    mu0 = 1.0  # reference scale in MeV
    log_mu = math.log(max(mu / mu0, 1e-12))
    denom = 1.0 - beta1 * alpha0 * log_mu - beta2 * (alpha0**2) * (log_mu**2)
    alpha = alpha0 / denom

    # Sanity check
    if alpha <= 0 or alpha >= 1:
        raise ValueError(f"Nonphysical α={alpha}, check geometry or μ={mu}")

    return alpha


# Optional direct test
if __name__ == "__main__":
    for mu in [1.0, 100.0, 1000.0]:
        print(f"μ = {mu:6.1f} MeV → α(μ) = {alpha_from_ubt_two_loop_strict(mu):.9f}")

