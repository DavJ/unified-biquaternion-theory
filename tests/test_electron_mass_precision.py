# tests/test_electron_mass_precision.py
# SPDX-License-Identifier: MIT
"""
Test: Electron Mass Precision
==============================

Verifies that the computed electron pole mass matches the experimental
value within specified tolerance.

Current tolerance: 1e-4 (0.01%)
Future target: 1e-5 (0.001%) after implementing 2-loop QED conversion
"""
import math
import sys
from pathlib import Path

# Ensure imports work
repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

# Experimental electron pole mass (PDG 2024)
M_E_REF = 0.51099895  # MeV

# Precision tolerance
# Current: 1e-4 (will be tightened to 1e-5 after 2-loop QED implementation)
TOL = 1e-4


def test_electron_mass_precision():
    """
    Test that computed electron pole mass matches experiment within tolerance.
    
    This test uses derived_mode=False (legacy validation mode) to validate
    against PDG reference. For theory-derived tests, see test_me_alpha_no_pdg.py
    
    Current tolerance: 1e-4 (0.01%)
    TODO: Tighten to 1e-5 after implementing full 2-loop QED MSbar→pole conversion
    """
    from ubt_masses.core import compute_lepton_msbar_mass, ubt_alpha_msbar
    from ubt_masses.qed import pole_from_msbar_lepton
    
    # Compute MSbar mass at μ = m̄_e (self-consistent choice)
    # Use legacy mode for PDG validation
    mbar = compute_lepton_msbar_mass("e", mu=None, derived_mode=False)
    
    # Get alpha at the mass scale
    alpha_mu = ubt_alpha_msbar(mbar)
    
    # Convert MSbar to pole mass using QED
    m_pole = pole_from_msbar_lepton(mbar, mu=mbar, alpha_mu=alpha_mu)
    
    # Compute relative error
    rel_err = abs(m_pole - M_E_REF) / M_E_REF
    
    assert rel_err < TOL, (
        f"Electron mass precision not met:\n"
        f"  Experimental: {M_E_REF:.12f} MeV\n"
        f"  Computed: {m_pole:.12f} MeV\n"
        f"  Relative error: {rel_err:.2e}\n"
        f"  Tolerance: {TOL:.2e}\n"
        f"TODO: Implement full 2-loop QED conversion to reach 1e-5 precision"
    )
    
    print(f"✓ Electron mass precision test passed:")
    print(f"  Experimental: {M_E_REF:.12f} MeV")
    print(f"  Computed: {m_pole:.12f} MeV")
    print(f"  Relative error: {rel_err:.2e} (< {TOL:.2e})")
    print(f"  MSbar mass: {mbar:.12f} MeV at μ = {mbar:.6f} MeV")
    print(f"  Alpha: {alpha_mu:.12e} at μ = {mbar:.6f} MeV")


def test_electron_mass_precision_target_10minus5():
    """
    Future precision target: 1e-5 (0.001%).
    
    This test is currently SKIPPED. It will pass once we implement
    the full 2-loop QED MSbar→pole conversion.
    Uses legacy mode for PDG validation.
    """
    import pytest
    pytest.skip("TODO: Implement 2-loop QED conversion to reach 1e-5 precision")
    
    # After 2-loop implementation, this should pass:
    from ubt_masses.core import compute_lepton_msbar_mass, ubt_alpha_msbar
    from ubt_masses.qed import pole_from_msbar_lepton
    
    mbar = compute_lepton_msbar_mass("e", mu=None, derived_mode=False)
    alpha_mu = ubt_alpha_msbar(mbar)
    m_pole = pole_from_msbar_lepton(mbar, mu=mbar, alpha_mu=alpha_mu)
    
    rel_err = abs(m_pole - M_E_REF) / M_E_REF
    
    assert rel_err < 1e-5, (
        f"Target 1e-5 precision not met: {rel_err:.2e}"
    )


if __name__ == "__main__":
    test_electron_mass_precision()
    print("✓ Electron mass precision verified")
