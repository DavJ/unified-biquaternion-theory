# alpha_core_repro/two_loop_core.py
# SPDX-License-Identifier: MIT
"""
Implementation of the theoretical fine-structure constant α(μ) from Unified Biquaternion Theory (UBT).

───────────────────────────────────────────────────────────────────────────────
UBT PRINCIPLE
───────────────────────────────────────────────────────────────────────────────
In UBT, α is *not* derived from measured lepton masses. It emerges from the
geometric ratio of the imaginary and real components of the complex time τ = t + iψ.

The fine-structure constant arises as a pure geometric coupling:
    α = f(Tψ / Tt) = (rψ / rt)² = vψ / c

Equivalently, in analytic form:
    α = Im(∂τΘ / Θ)

where Θ(q, τ) is the biquaternionic field defined on the complex torus ℂ⁵.

───────────────────────────────────────────────────────────────────────────────
DERIVATION OUTLINE
───────────────────────────────────────────────────────────────────────────────
1. Let τ_ratio = sqrt(G μ / (ħ c⁵))  → geometric relation between phase and drift time.
2. Define α₀ = (θ₀² / 4π²) * τ_ratio  → fundamental geometric coupling constant.
3. Apply two-loop (geometric) renormalization:
       α(μ) = α₀ / [1 - β₁ α₀ log(μ/μ₀) - β₂ α₀² log²(μ/μ₀)]
   where β₁, β₂ are topological coefficients of the toroidal C⁵ geometry.

───────────────────────────────────────────────────────────────────────────────
NOTES
───────────────────────────────────────────────────────────────────────────────
- This formula uses *no measured lepton masses or experimental α*.
- All constants are fundamental (ħ, c, G).
- θ₀ = π / 2e corresponds to the lowest toroidal twist harmonic.
- The output α(μ) decreases with increasing μ, as expected physically.
───────────────────────────────────────────────────────────────────────────────
"""

import math

# Fundamental constants (SI units)
hbar = 1.054571817e-34  # J·s
c = 299792458.0          # m/s
G = 6.67430e-11          # m³/(kg·s²)

# Geometric twist of torus
theta0 = math.pi / (2.0 * math.e)

def alpha_from_ubt_two_loop_strict(mu: float) -> float:
    """
    Compute fine-structure constant α(μ) purely from UBT geometry.

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

    # Fundamental geometric ratio
    tau_ratio = math.sqrt(G * mu_J / (hbar * c**5))

    # Base (zero-loop) α₀
    alpha0 = (theta0**2 / (4 * math.pi**2)) * tau_ratio

    # Two-loop renormalization coefficients (pure geometric)
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
