# tests/test_electron_mass.py
# SPDX-License-Identifier: MIT
"""
Electron Mass Tests - Fit-Free, Metrology-Grade
================================================

Validates the electron mass derivation pipeline:
1. α is computed fit-free from UBT two-loop (no mocks)
2. MSbar mass calculation is self-consistent
3. Pole mass matches experiment within target precision

Target: Relative error < 10⁻⁴ (TODO: tighten to 10⁻⁵ with 2-loop QED)
"""
import math
import os
import sys
from pathlib import Path
import pytest

# Add repo root to path
repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

# Ensure strict mode for these tests
os.environ["UBT_ALPHA_STRICT"] = "1"
if "UBT_ALPHA_ALLOW_MOCK" in os.environ:
    del os.environ["UBT_ALPHA_ALLOW_MOCK"]

from alpha_core_repro.alpha_two_loop import (
    compute_two_loop_delta,
    alpha_corrected,
    TwoLoopConfig,
)
from ubt_masses.core import (
    ubt_alpha_msbar,
    compute_lepton_msbar_mass,
    solve_msbar_fixed_point,
)
from ubt_masses.qed import pole_from_msbar_lepton, msbar_from_pole_lepton


# Reference values (PDG 2024)
M_E_POLE_REF = 0.51099895  # MeV, electron pole mass
ALPHA_INV_THOMSON_REF = 137.035999  # α⁻¹ at Thomson limit


def test_alpha_fit_free_identity():
    """
    Critical test: α from mass pipeline must be IDENTICAL to α from alpha_core_repro.
    
    This ensures we're using the fit-free two-loop calculation, not a mock or manual value.
    """
    mu = 0.511  # MeV, approximate electron mass scale
    
    # Direct call to alpha_core_repro (strict mode)
    cfg_direct = TwoLoopConfig(scheme="MSbar", mu=mu, strict=True)
    delta_ct_direct = compute_two_loop_delta(137, cfg_direct)
    alpha_direct = alpha_corrected(137, delta_ct_direct)
    
    # Call through mass pipeline
    alpha_pipeline = ubt_alpha_msbar(mu)
    
    # Must be EXACTLY the same (no tolerance)
    assert alpha_direct == alpha_pipeline, (
        f"α mismatch: direct={alpha_direct:.15e}, pipeline={alpha_pipeline:.15e}. "
        "Mass pipeline must use identical α calculation from alpha_core_repro."
    )


def test_alpha_strict_mode_enforced():
    """
    Verify that mass pipeline rejects mock mode.
    """
    # Temporarily enable mock mode
    os.environ["UBT_ALPHA_ALLOW_MOCK"] = "1"
    
    try:
        with pytest.raises(RuntimeError, match="strict α calculation"):
            ubt_alpha_msbar(0.511)
    finally:
        # Clean up
        if "UBT_ALPHA_ALLOW_MOCK" in os.environ:
            del os.environ["UBT_ALPHA_ALLOW_MOCK"]


def test_alpha_physical_value():
    """
    Sanity check: α(m_e) should be close to 1/137.
    """
    alpha = ubt_alpha_msbar(0.511)  # At electron mass scale
    alpha_inv = 1.0 / alpha
    
    # Should be within 1% of Thomson value
    assert abs(alpha_inv - ALPHA_INV_THOMSON_REF) < 1.5, (
        f"α⁻¹ = {alpha_inv:.6f} is too far from {ALPHA_INV_THOMSON_REF}"
    )


def test_qed_conversion_roundtrip():
    """
    Test MSbar ↔ pole mass conversion consistency.
    """
    m_msbar_input = 0.510  # MeV
    mu = m_msbar_input  # Use μ = m̄ to minimize logs
    alpha_mu = ubt_alpha_msbar(mu)
    
    # MSbar → pole → MSbar
    m_pole = pole_from_msbar_lepton(m_msbar_input, mu, alpha_mu)
    m_msbar_recovered = msbar_from_pole_lepton(m_pole, mu, alpha_mu)
    
    # Should recover original MSbar mass within numerical precision
    rel_error = abs(m_msbar_recovered - m_msbar_input) / m_msbar_input
    assert rel_error < 1e-6, (
        f"QED conversion roundtrip failed: "
        f"m̄_in={m_msbar_input:.9f}, m̄_out={m_msbar_recovered:.9f}, "
        f"rel_error={rel_error:.2e}"
    )


def test_electron_msbar_mass_computed():
    """
    Test that MSbar mass is computed without errors.
    """
    mbar = compute_lepton_msbar_mass("e", mu=None)
    
    # Basic sanity checks
    assert mbar > 0, "MSbar mass must be positive"
    assert 0.4 < mbar < 0.6, (
        f"Electron MSbar mass {mbar:.6f} MeV is out of expected range [0.4, 0.6] MeV"
    )


def test_electron_mass_precision():
    """
    Main precision test: electron pole mass must match experiment within tolerance.
    
    Current target: relative error < 10⁻⁴
    TODO: Tighten to < 10⁻⁵ after implementing 2-loop QED conversion
    """
    # Compute MSbar mass at μ = m̄_e (self-consistent choice)
    mbar = compute_lepton_msbar_mass("e", mu=None)
    
    # Get α at this scale
    alpha_mu = ubt_alpha_msbar(mbar)
    
    # Convert to pole mass using 1-loop QED
    m_pole = pole_from_msbar_lepton(mbar, mu=mbar, alpha_mu=alpha_mu)
    
    # Compare with experimental value
    rel_error = abs(m_pole - M_E_POLE_REF) / M_E_POLE_REF
    
    # Current tolerance: 10⁻⁴ (will be tightened to 10⁻⁵)
    tolerance = 1e-4
    
    assert rel_error < tolerance, (
        f"Electron pole mass precision test failed:\n"
        f"  Computed: m_e = {m_pole:.9f} MeV\n"
        f"  Reference: m_e = {M_E_POLE_REF:.9f} MeV\n"
        f"  Relative error: {rel_error:.2e}\n"
        f"  Tolerance: {tolerance:.2e}\n"
        f"  TODO: Tighten to 10⁻⁵ after 2-loop QED implementation"
    )


def test_electron_mass_precision_target_10minus5():
    """
    Future target test: relative error < 10⁻⁵.
    
    This test is marked as xfail (expected to fail) until we implement 2-loop QED.
    """
    pytest.skip("TODO: Implement 2-loop QED self-energy correction")
    
    # Same calculation as test_electron_mass_precision
    mbar = compute_lepton_msbar_mass("e", mu=None)
    alpha_mu = ubt_alpha_msbar(mbar)
    m_pole = pole_from_msbar_lepton(mbar, mu=mbar, alpha_mu=alpha_mu)
    
    rel_error = abs(m_pole - M_E_POLE_REF) / M_E_POLE_REF
    
    # Tighter tolerance
    tolerance = 1e-5
    
    assert rel_error < tolerance, (
        f"Target precision 10⁻⁵ not yet achieved. "
        f"Current error: {rel_error:.2e}"
    )


def test_fixed_point_convergence():
    """
    Test that fixed-point solver converges to self-consistent solution.
    """
    initial_guess = 0.510  # MeV
    
    mbar_fixed = solve_msbar_fixed_point(initial_guess, lepton="e", tol=1e-10)
    
    # Verify it's a fixed point: μ = m̄(μ)
    alpha_mu = ubt_alpha_msbar(mbar_fixed)
    mbar_check = compute_lepton_msbar_mass("e", mu=mbar_fixed)
    
    rel_diff = abs(mbar_check - mbar_fixed) / mbar_fixed
    assert rel_diff < 1e-9, (
        f"Fixed point not self-consistent: "
        f"m̄={mbar_fixed:.12f}, m̄(μ=m̄)={mbar_check:.12f}, "
        f"rel_diff={rel_diff:.2e}"
    )


def test_muon_and_tau_not_implemented():
    """
    Verify that muon and tau raise NotImplementedError.
    """
    with pytest.raises(NotImplementedError, match="muon"):
        compute_lepton_msbar_mass("mu")
    
    with pytest.raises(NotImplementedError, match="tau"):
        compute_lepton_msbar_mass("tau")


def test_invalid_inputs_rejected():
    """
    Test that invalid inputs are properly rejected.
    """
    # Negative scale
    with pytest.raises(ValueError, match="positive"):
        ubt_alpha_msbar(-1.0)
    
    # Zero scale
    with pytest.raises(ValueError, match="positive"):
        ubt_alpha_msbar(0.0)
    
    # Negative MSbar mass
    with pytest.raises(ValueError, match="positive"):
        pole_from_msbar_lepton(-0.5, 0.5, 1/137)
    
    # Invalid α
    with pytest.raises(ValueError, match="α"):
        pole_from_msbar_lepton(0.5, 0.5, -0.01)
    
    with pytest.raises(ValueError, match="α"):
        pole_from_msbar_lepton(0.5, 0.5, 1.5)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
