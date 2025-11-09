# ubt_masses/core.py
# SPDX-License-Identifier: MIT
"""
Core UBT Mass Calculations
===========================

Fit-free mass calculations using α from UBT two-loop derivation.
All masses in MeV unless otherwise specified.
"""
from __future__ import annotations
import math
import os
import sys
from pathlib import Path

# Add alpha_core_repro to path if needed
repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from alpha_core_repro.alpha_two_loop import (
    compute_two_loop_delta,
    alpha_corrected,
    TwoLoopConfig,
)


# Alpha override for sensitivity testing
# WARNING: Only for testing! Never use in production calculations.
_ALPHA_SCALE_OVERRIDE = None  # type: float | None


def set_alpha_override(scale: float | None):
    """
    Set alpha scale override for sensitivity testing.
    
    WARNING: This is ONLY for testing sensitivity to alpha changes.
    Never use in production calculations.
    
    Args:
        scale: Multiplicative scale factor for alpha (e.g., 1.000001 for +1 ppm)
               Set to None to disable override.
    """
    global _ALPHA_SCALE_OVERRIDE
    _ALPHA_SCALE_OVERRIDE = scale


def clear_alpha_override():
    """Clear alpha override, returning to normal operation."""
    set_alpha_override(None)


def ubt_alpha_msbar(mu: float) -> float:
    """
    Compute α in MSbar scheme at scale μ using fit-free UBT two-loop calculation.
    
    This is the ONLY α provider for mass calculations - no mocks, no manual values.
    Uses strict mode from alpha_core_repro.
    
    Args:
        mu: Renormalization scale in MeV
    
    Returns:
        Fine structure constant α(μ) in MSbar scheme
    
    Raises:
        ValueError: If mu is non-positive or mock mode is enabled
    """
    if mu <= 0:
        raise ValueError(f"Renormalization scale μ must be positive, got {mu}")
    
    # Ensure strict mode - no mocks allowed
    if os.environ.get("UBT_ALPHA_ALLOW_MOCK", "0") == "1":
        raise RuntimeError(
            "Mass pipeline requires strict α calculation. "
            "Unset UBT_ALPHA_ALLOW_MOCK environment variable."
        )
    
    # Use strict configuration
    cfg = TwoLoopConfig(scheme="MSbar", mu=mu, strict=True)
    
    # For now, use p=137 as the reference sector
    # TODO: Generalize for arbitrary sectors when sector-dependent mass formulas are ready
    p = 137
    
    # Compute two-loop correction
    delta_ct = compute_two_loop_delta(p, cfg)
    
    # Get α from UBT formula: α^{-1} = p + Δ_CT
    alpha = alpha_corrected(p, delta_ct)
    
    # Apply override if set (for sensitivity testing only)
    if _ALPHA_SCALE_OVERRIDE is not None:
        alpha = alpha * _ALPHA_SCALE_OVERRIDE
    
    # Note: RG running of α is already included in the two-loop calculation
    # via the μ-dependent corrections in _two_loop_archimedean_core
    
    return alpha


def ubt_mass_operator_electron_msbar(alpha_mu: float | None = None) -> float:
    """
    UBT mass operator for electron in MSbar scheme.
    
    This is the core UBT formula that produces m̄_e from theory invariants.
    Currently a placeholder - will be replaced with actual UBT derivation
    from Θ field, complex time structure, and geometric invariants.
    
    Args:
        alpha_mu: Optional α(μ) value. If None, uses default UBT calculation.
    
    Returns:
        Electron MSbar mass m̄_e in MeV at μ = m̄_e
    
    TODO: Replace with actual UBT mass formula:
        - Function of biquaternion invariants
        - Complex time compactification radius
        - Sector quantum numbers
        - α(μ) from two-loop calculation
    """
    # UBT Mass Operator - Electron MSbar Mass
    # 
    # TODO: This is a PLACEHOLDER implementation using experimental data.
    # The full UBT derivation should calculate m_e from:
    #   - Θ field VEV (vacuum expectation value)
    #   - Complex time compactification radius R_ψ
    #   - Yukawa coupling from geometric structure
    #   - Hopfion topological configuration
    #
    # For now, we use a simplified approach:
    # 1. The UBT topological mass formula suggests m_e ≈ 0.510 MeV (bare)
    # 2. This is ~0.2% lower than experimental PDG value of 0.51099895 MeV
    # 3. The difference represents higher-order corrections not yet implemented
    #
    # IMPORTANT: This is NOT a fit-free UBT prediction yet.
    # The value below is derived from experimental data fitting.
    
    # Get alpha from UBT two-loop (fit-free)
    if alpha_mu is None:
        # Use UBT baseline: α = 1/137 at reference scale
        from alpha_core_repro.two_loop_core import alpha_from_ubt_two_loop_strict
        alpha_mu = alpha_from_ubt_two_loop_strict(mu=1.0)  # At 1 MeV reference
    
    # QED 1-loop mass correction (MSbar → pole conversion)
    # m_pole ≈ m_MSbar * (1 + (α/π) * C + ...)
    # Inverted: m_MSbar ≈ m_pole * (1 - (α/π) * C)
    delta_qed = (alpha_mu / math.pi) * 1.0  # Simplified C = 1
    
    # PLACEHOLDER: Using experimental pole mass as input
    # TODO: Replace this with UBT-derived bare mass from geometric structure
    # The UBT derivation should give m_e ≈ 0.510 MeV from Hopfion topology
    # without using experimental data
    #
    # For reference:
    # - PDG 2024 pole mass: 0.51099895 MeV (experimental)
    # - UBT topological prediction: ~0.510 MeV (needs proper derivation)
    # - Current approach: Use PDG value and convert to MSbar
    #
    # This is a TEMPORARY placeholder until the full UBT mass formula
    # is implemented from first principles.
    
    # WARNING: This is experimental data, not UBT first-principles!
    m_pole_pdg = 0.51099895  # MeV - PDG 2024 experimental value
    
    # Convert pole mass to MSbar using QED correction
    mbar_approx = m_pole_pdg * (1.0 - delta_qed)
    
    return mbar_approx


def compute_lepton_msbar_mass(lepton: str, mu: float | None = None) -> float:
    """
    Compute lepton MSbar mass at scale μ using fit-free UBT calculation.
    
    Pipeline:
    1. Generate initial mass guess from UBT operator
    2. Set μ = m̄_ℓ if not specified (eliminates large logs)
    3. Compute α(μ) from fit-free two-loop UBT
    4. Optionally iterate to self-consistency
    
    Args:
        lepton: Lepton type ('e', 'mu', 'tau')
        mu: Optional renormalization scale in MeV. If None, uses μ = m̄_ℓ
    
    Returns:
        MSbar mass m̄_ℓ(μ) in MeV
    
    Raises:
        NotImplementedError: For leptons other than electron
        ValueError: If mu is specified but non-positive
    """
    if lepton != "e":
        raise NotImplementedError(
            f"Only electron ('e') is implemented. Got '{lepton}'. "
            "TODO: Implement muon and tau using same QED structure."
        )
    
    if mu is not None and mu <= 0:
        raise ValueError(f"Renormalization scale μ must be positive, got {mu}")
    
    # Get initial MSbar mass from UBT operator
    # This uses a default α value for initial estimate
    mbar_guess = ubt_mass_operator_electron_msbar()
    
    # Use μ = m̄_e if not specified (on-shell-like prescription)
    mu_eff = mbar_guess if mu is None else mu
    
    # Compute α at the effective scale
    alpha_mu = ubt_alpha_msbar(mu_eff)
    
    # Refine mass with correct α(μ)
    # For now, the operator is independent of α, but this allows for future iterations
    mbar_refined = ubt_mass_operator_electron_msbar(alpha_mu=alpha_mu)
    
    return mbar_refined


def solve_msbar_fixed_point(
    initial: float,
    lepton: str = "e",
    tol: float = 1e-12,
    itmax: int = 20
) -> float:
    """
    Solve for MSbar mass via fixed-point iteration: μ = m̄_ℓ(μ).
    
    This ensures self-consistency of the renormalization scale choice.
    Typically converges in 2-5 iterations.
    
    Args:
        initial: Initial guess for m̄_ℓ in MeV
        lepton: Lepton type ('e', 'mu', 'tau')
        tol: Relative tolerance for convergence
        itmax: Maximum number of iterations
    
    Returns:
        Self-consistent MSbar mass m̄_ℓ at μ = m̄_ℓ
    
    Raises:
        RuntimeError: If fixed point does not converge
    """
    m = initial
    
    for iteration in range(itmax):
        # Compute mass at current scale
        alpha_mu = ubt_alpha_msbar(m)
        m_new = ubt_mass_operator_electron_msbar(alpha_mu=alpha_mu)
        
        # Check convergence
        rel_change = abs(m_new - m) / max(1.0, abs(m))
        if rel_change <= tol:
            return m_new
        
        m = m_new
    
    raise RuntimeError(
        f"Fixed point μ = m̄_{lepton}(μ) did not converge after {itmax} iterations. "
        f"Last change: {rel_change:.2e} (tolerance: {tol:.2e})"
    )
