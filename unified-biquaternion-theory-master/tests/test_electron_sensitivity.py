# tests/test_electron_sensitivity.py
# SPDX-License-Identifier: MIT
"""
Test: Electron Mass Sensitivity to Alpha
=========================================

Verifies that the electron mass CHANGES when alpha changes.
This detects hard-coded mass values: if m_e doesn't respond to
alpha perturbations, it's likely hard-coded rather than computed.
"""
import sys
from pathlib import Path

# Ensure imports work
repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))


def test_electron_mass_moves_with_alpha():
    """
    Test that electron mass responds to alpha changes.
    
    A +1 ppm change in alpha must cause a measurable change in m_e.
    If m_e doesn't change, it's likely hard-coded.
    """
    from ubt_masses.core import (
        compute_lepton_msbar_mass,
        set_alpha_override,
        clear_alpha_override,
    )
    
    # Compute baseline mass with normal alpha
    clear_alpha_override()
    m0 = compute_lepton_msbar_mass("e")
    
    # Perturb alpha by +1 ppm (parts per million)
    set_alpha_override(1.0 + 1e-6)
    m1 = compute_lepton_msbar_mass("e")
    
    # Clean up
    clear_alpha_override()
    
    # Mass must change with alpha
    delta_m = abs(m1 - m0)
    
    assert delta_m > 0.0, (
        f"Electron mass must change with alpha!\n"
        f"  m_e(α): {m0:.12f} MeV\n"
        f"  m_e(α × 1.000001): {m1:.12f} MeV\n"
        f"  Change: {delta_m:.12e} MeV\n"
        f"This suggests m_e is hard-coded rather than computed from alpha."
    )
    
    # The change should be proportional to the alpha change
    # For QED corrections: m ∝ α, so Δm/m ~ Δα/α
    # We perturbed alpha by 1e-6, so we expect Δm/m ~ 1e-6 or larger
    # (could be larger due to nonlinear corrections)
    
    rel_change = delta_m / m0
    
    # Require at least some sensitivity
    # Even a weak dependence should give > 1e-9 relative change
    assert rel_change > 1e-9, (
        f"Electron mass shows insufficient sensitivity to alpha:\n"
        f"  Relative change: {rel_change:.2e}\n"
        f"  Expected: > 1e-9\n"
        f"This suggests m_e may be hard-coded or weakly dependent on alpha."
    )
    
    print(f"✓ Electron mass sensitivity verified:")
    print(f"  m_e(α): {m0:.12f} MeV")
    print(f"  m_e(α × 1.000001): {m1:.12f} MeV")
    print(f"  Δm: {delta_m:.12e} MeV ({rel_change:.2e} relative)")


def test_alpha_override_cleanup():
    """
    Verify that alpha override is properly cleared and doesn't persist.
    """
    from ubt_masses.core import (
        ubt_alpha_msbar,
        set_alpha_override,
        clear_alpha_override,
    )
    
    mu = 0.511
    
    # Get baseline alpha
    alpha_baseline = ubt_alpha_msbar(mu)
    
    # Set override
    set_alpha_override(1.5)
    alpha_override = ubt_alpha_msbar(mu)
    
    # Clear override
    clear_alpha_override()
    alpha_after_clear = ubt_alpha_msbar(mu)
    
    # Override should have effect
    assert abs(alpha_override - alpha_baseline * 1.5) < 1e-15, (
        "Alpha override not working correctly"
    )
    
    # After clearing, should return to baseline
    assert alpha_after_clear == alpha_baseline, (
        "Alpha override not properly cleared"
    )


if __name__ == "__main__":
    test_electron_mass_moves_with_alpha()
    test_alpha_override_cleanup()
    print("✓ All sensitivity tests passed")
