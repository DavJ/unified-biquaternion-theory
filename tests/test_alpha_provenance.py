# tests/test_alpha_provenance.py
# SPDX-License-Identifier: MIT
"""
Test: Alpha Provenance
======================

Ensures that the mass pipeline uses α from the fit-free UBT two-loop
calculation, with NO mocks or fallback values.

This verifies the data provenance chain: UBT two-loop → α → masses
"""
import math
import sys
from pathlib import Path

# Ensure imports work
repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))


def test_alpha_fit_free_identity():
    """
    Verify that mass pipeline uses strict UBT alpha (no mock/fallback).
    
    The α value used for mass calculations must come from the two-loop
    UBT calculation in strict mode, ensuring complete data provenance.
    """
    from alpha_core_repro.alpha_two_loop import (
        compute_two_loop_delta,
        alpha_corrected,
        TwoLoopConfig,
    )
    from ubt_masses.core import ubt_alpha_msbar
    
    # Reference scale (electron mass scale)
    mu = 0.511  # MeV
    
    # Compute α using the strict two-loop calculation
    cfg = TwoLoopConfig(scheme="MSbar", mu=mu, strict=True)
    p = 137  # Reference sector
    delta_ct = compute_two_loop_delta(p, cfg)
    alpha_ref = alpha_corrected(p, delta_ct)
    
    # Get α from the mass pipeline provider
    alpha_mass = ubt_alpha_msbar(mu)
    
    # These must be EXACTLY equal (same code path)
    # Using exact equality (not isclose) to ensure no mock/fallback path
    assert alpha_ref == alpha_mass, (
        f"Mass pipeline α provider must use strict UBT two-loop calculation.\n"
        f"  Reference: α({mu} MeV) = {alpha_ref}\n"
        f"  Mass pipeline: α({mu} MeV) = {alpha_mass}\n"
        f"  Difference: {abs(alpha_ref - alpha_mass)}\n"
        f"This indicates a mock or fallback value is being used."
    )


def test_alpha_strict_mode_required():
    """
    Verify that UBT_ALPHA_ALLOW_MOCK environment variable breaks mass calculations.
    
    The mass pipeline must enforce strict mode - setting the mock environment
    variable should cause an error.
    """
    import os
    from ubt_masses.core import ubt_alpha_msbar
    
    # Save current state
    original_value = os.environ.get("UBT_ALPHA_ALLOW_MOCK")
    
    try:
        # Set mock mode
        os.environ["UBT_ALPHA_ALLOW_MOCK"] = "1"
        
        # This should raise an error
        try:
            alpha = ubt_alpha_msbar(0.511)
            # If we get here, the strict mode is not enforced
            assert False, (
                "Mass pipeline allowed mock mode! "
                "ubt_alpha_msbar() must enforce strict=True and reject UBT_ALPHA_ALLOW_MOCK=1"
            )
        except RuntimeError as e:
            # Expected error - strict mode is enforced
            assert "strict" in str(e).lower() or "mock" in str(e).lower(), (
                f"Expected error about strict mode, got: {e}"
            )
    finally:
        # Restore original state
        if original_value is None:
            os.environ.pop("UBT_ALPHA_ALLOW_MOCK", None)
        else:
            os.environ["UBT_ALPHA_ALLOW_MOCK"] = original_value


if __name__ == "__main__":
    test_alpha_fit_free_identity()
    print("✓ Alpha provenance verified: mass pipeline uses strict UBT two-loop")
    test_alpha_strict_mode_required()
    print("✓ Strict mode enforcement verified")
