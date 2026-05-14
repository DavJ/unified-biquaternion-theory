# tests/test_me_alpha_truth.py
# SPDX-License-Identifier: MIT
"""
Strict tests to enforce UBT m_e → alpha claim testability and honesty.

These tests ensure:
1. No unconditional "return 137" in selector (must be from evaluation)
2. No empirical calibrations in derived_mode (no magic constants like 0.0372)
3. alpha_from_me either inverts or raises NotImplementedError (no silent ubt_alpha_msbar call)
4. All constraints are enforced and tests fail if violated

Part of: ubt_me_alpha_truth_fixpack_v1
"""
import inspect
import math
import os
import re
import sys
from pathlib import Path

# Add repo root to path
repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

# Ensure strict mode
os.environ["UBT_ALPHA_STRICT"] = "1"
if "UBT_ALPHA_ALLOW_MOCK" in os.environ:
    del os.environ["UBT_ALPHA_ALLOW_MOCK"]

from ubt_masses.core import (
    ubt_alpha_msbar,
    ubt_mass_operator_electron_msbar,
    ubt_select_sector_p,
    alpha_from_me,
)


def test_no_return_137_literal_in_selector():
    """
    Verify that ubt_select_sector_p does NOT contain unconditional "return 137".
    
    The selector must evaluate candidates and compute scores, not just return 137.
    For CT baseline, 137 should WIN the selection, not be hardcoded.
    """
    source = inspect.getsource(ubt_select_sector_p)
    
    # Look for "return 137" as a standalone statement (not in comments/strings)
    lines = source.split('\n')
    
    # Check each line for unconditional "return 137"
    for line in lines:
        # Remove comments and strings
        code_part = line.split('#')[0].strip()
        
        # Check if this is an unconditional return 137
        if re.match(r'^\s*return\s+137\s*$', code_part):
            # This is a bare "return 137" statement
            # Check if it's inside a conditional or loop context
            # For simplicity, we'll just flag it and require justification
            raise AssertionError(
                "Found unconditional 'return 137' in ubt_select_sector_p. "
                "Selector must evaluate candidates, not hardcode 137. "
                f"Line: {line.strip()}"
            )
    
    # Verify that the function actually evaluates candidates
    assert "candidates" in source, "Selector must accept and use candidates"
    assert "score" in source.lower() or "select" in source.lower(), (
        "Selector must compute scores or perform selection logic"
    )


def test_alpha_requires_sector_or_selector():
    """
    Verify that ubt_alpha_msbar requires explicit sector_p or selector.
    
    When sector_p=None, it must call ubt_select_sector_p, not default to 137.
    """
    source = inspect.getsource(ubt_alpha_msbar)
    
    # Check that sector_p defaults to None
    assert "sector_p: int | None = None" in source or "sector_p=None" in source, (
        "ubt_alpha_msbar must default sector_p to None, not 137"
    )
    
    # Check that it calls ubt_select_sector_p when sector_p is None
    assert "ubt_select_sector_p" in source, (
        "ubt_alpha_msbar must call ubt_select_sector_p when sector_p is None"
    )
    
    # Runtime test: calling with sector_p=None should work (via selector)
    alpha = ubt_alpha_msbar(mu=1.0, sector_p=None)
    assert isinstance(alpha, (int, float)), "Alpha must be numeric"
    assert 1/140 < alpha < 1/130, "Alpha should be near 1/137"


def test_derived_me_no_pdg_no_empirical_literals():
    """
    Verify that derived mode in ubt_mass_operator_electron_msbar contains:
    - NO PDG/CODATA constants (0.51099895, etc.)
    - NO empirical calibration literals (0.0372, etc.)
    
    These may appear in "calibrated" or "legacy" modes, but NOT in "derived".
    """
    source = inspect.getsource(ubt_mass_operator_electron_msbar)
    
    # Split into mode branches
    lines = source.split('\n')
    
    # Find the "derived" mode section
    in_derived = False
    derived_section = []
    
    for line in lines:
        if 'mode == "derived"' in line or "mode == 'derived'" in line:
            in_derived = True
        elif in_derived:
            if 'mode ==' in line:  # Start of another mode
                break
            derived_section.append(line)
    
    derived_code = '\n'.join(derived_section)
    
    # Forbidden literals in derived mode
    forbidden_literals = [
        "0.0372",    # Empirical calibration
        "0.51099895", # PDG pole mass
        "0.511",     # PDG mass (rounded)
        "PDG",       # PDG reference
        "CODATA",    # CODATA reference
    ]
    
    for literal in forbidden_literals:
        # Check if it appears in code (not just comments)
        for line in derived_section:
            code_part = line.split('#')[0]  # Remove comments
            if literal in code_part:
                raise AssertionError(
                    f"Found forbidden literal '{literal}' in derived mode. "
                    f"Line: {line.strip()}\n"
                    "Derived mode must contain ZERO empirical calibrations."
                )
    
    # Verify derived mode has required components
    assert "alpha_mu" in derived_code, "Derived mode must compute alpha"
    assert "sector_p" in derived_code, "Derived mode must use sector_p"
    
    print(f"✓ Derived mode is clean: no PDG, no empirical literals")


def test_alpha_from_me_not_calling_alpha_msbar():
    """
    Verify that alpha_from_me does NOT call ubt_alpha_msbar.
    
    It must either:
    1. Implement a real toy inversion, OR
    2. Raise NotImplementedError with clear missing ingredient
    
    It must NOT silently call ubt_alpha_msbar (circular reasoning).
    """
    source = inspect.getsource(alpha_from_me)
    
    # Check that ubt_alpha_msbar is NOT called
    assert "ubt_alpha_msbar" not in source, (
        "alpha_from_me must NOT call ubt_alpha_msbar. "
        "This would be circular reasoning. "
        "Either implement real inversion or raise NotImplementedError."
    )
    
    # Verify that it either inverts or raises
    assert "raise NotImplementedError" in source or "return" in source, (
        "alpha_from_me must either return a value or raise NotImplementedError"
    )
    
    # Test that non-toy model raises NotImplementedError
    try:
        alpha = alpha_from_me(mu=1.0, me_msbar=0.5, sector_p=137, model="full")
        raise AssertionError(
            "alpha_from_me with model='full' should raise NotImplementedError"
        )
    except NotImplementedError as e:
        # Check that error mentions the missing ingredient
        error_msg = str(e).lower()
        assert "k_gauge" in error_msg or "gauge kinetic" in error_msg, (
            "NotImplementedError must mention missing K_gauge (gauge kinetic normalization)"
        )
    
    print("✓ alpha_from_me does not call ubt_alpha_msbar")


def test_calibrated_mode_is_opt_in():
    """
    Verify that calibrated mode is opt-in, not default.
    
    Default mode must be "derived" (theory-only).
    Calibrated mode must be explicitly requested.
    """
    source = inspect.getsource(ubt_mass_operator_electron_msbar)
    
    # Check that default mode is "derived"
    assert 'mode: str = "derived"' in source, (
        'Default mode must be "derived", not "calibrated"'
    )
    
    # Runtime test: default should be derived
    m_default = ubt_mass_operator_electron_msbar(mu=1.0)
    m_derived = ubt_mass_operator_electron_msbar(mu=1.0, mode="derived")
    
    assert m_default == m_derived, (
        "Default mode must behave as derived mode"
    )
    
    # Calibrated mode must be explicitly requested
    m_calibrated = ubt_mass_operator_electron_msbar(mu=1.0, mode="calibrated")
    
    # They should be different (calibrated uses empirical constant)
    rel_diff = abs(m_calibrated - m_derived) / m_calibrated
    assert rel_diff > 0.01, (
        "Calibrated and derived modes should give significantly different results"
    )
    
    print("✓ Calibrated mode is opt-in, derived is default")


def test_selector_evaluates_candidates():
    """
    Verify that ubt_select_sector_p actually evaluates multiple candidates.
    
    For CT baseline, 137 should win, but other candidates should be evaluated.
    """
    source = inspect.getsource(ubt_select_sector_p)
    
    # Check for evaluation logic
    assert "for" in source or "score" in source.lower(), (
        "Selector must iterate through candidates or compute scores"
    )
    
    # Runtime test: selector with custom candidates
    # Should still return 137 for CT baseline
    candidates_with_137 = [131, 137, 139]
    p1 = ubt_select_sector_p(candidates=candidates_with_137)
    assert p1 == 137, "Selector should pick 137 from candidates for CT baseline"
    
    # If we exclude 137, it should pick the nearest
    candidates_without_137 = [131, 139]
    p2 = ubt_select_sector_p(candidates=candidates_without_137)
    assert p2 in [131, 139], "Selector should pick from available candidates"
    
    print(f"✓ Selector evaluates candidates: picked {p1} from {candidates_with_137}, {p2} from {candidates_without_137}")


def test_derived_mode_produces_reasonable_value():
    """
    Test that derived mode produces a value that could plausibly be m_e.
    
    It may be wrong numerically, but should be in the right ballpark.
    """
    m_e = ubt_mass_operator_electron_msbar(mu=1.0, mode="derived")
    
    # Should be positive and finite
    assert m_e > 0, "Mass must be positive"
    assert math.isfinite(m_e), "Mass must be finite"
    
    # Should be within a few orders of magnitude of actual m_e
    # (Actual m_e ≈ 0.511 MeV)
    assert 0.001 < m_e < 100.0, (
        f"Derived m_e = {m_e} MeV is outside reasonable range (0.001 - 100 MeV)"
    )
    
    print(f"✓ Derived mode produces m_e = {m_e:.6f} MeV (reasonable range)")


def test_calibrated_mode_matches_pdg():
    """
    Test that calibrated mode produces value close to PDG.
    
    This validates that the spectral formula structure is correct,
    just needs proper normalization.
    """
    m_calibrated = ubt_mass_operator_electron_msbar(mu=1.0, mode="calibrated")
    
    # Should be close to PDG electron mass (0.511 MeV)
    assert 0.4 < m_calibrated < 0.6, (
        f"Calibrated m_e = {m_calibrated} MeV should be near PDG value 0.511 MeV"
    )
    
    print(f"✓ Calibrated mode produces m_e = {m_calibrated:.6f} MeV (near PDG)")


def test_no_hidden_empirical_in_derived():
    """
    Verify that derived mode does not use ANY empirical scaling factors.
    
    Check the source code for sqrt(sector_p) multipliers or other scaling.
    """
    source = inspect.getsource(ubt_mass_operator_electron_msbar)
    
    # Extract derived mode section
    lines = source.split('\n')
    in_derived = False
    derived_lines = []
    
    for line in lines:
        if 'mode == "derived"' in line:
            in_derived = True
        elif in_derived:
            if 'mode ==' in line:
                break
            derived_lines.append(line)
    
    derived_code = '\n'.join(derived_lines)
    
    # Check for forbidden patterns in derived mode
    # We allow sqrt(sector_p) as it's a theory quantity
    # But NOT things like "0.0372 * sqrt(sector_p)"
    
    # Pattern: numeric constant * sqrt(sector_p)
    pattern = r'\d+\.\d+\s*\*\s*.*sqrt.*sector_p'
    
    for line in derived_lines:
        if re.search(pattern, line):
            # Check if it's in a comment
            if '#' in line:
                code_part = line.split('#')[0]
                if not re.search(pattern, code_part):
                    continue  # It's only in comment, OK
            
            raise AssertionError(
                f"Found empirical scaling in derived mode: {line.strip()}\n"
                "Derived mode must not contain numeric constants multiplied by theory quantities."
            )
    
    print("✓ No hidden empirical scaling in derived mode")


if __name__ == "__main__":
    # Run all tests
    tests = [
        test_no_return_137_literal_in_selector,
        test_alpha_requires_sector_or_selector,
        test_derived_me_no_pdg_no_empirical_literals,
        test_alpha_from_me_not_calling_alpha_msbar,
        test_calibrated_mode_is_opt_in,
        test_selector_evaluates_candidates,
        test_derived_mode_produces_reasonable_value,
        test_calibrated_mode_matches_pdg,
        test_no_hidden_empirical_in_derived,
    ]
    
    print("=" * 60)
    print("STRICT TESTS: UBT m_e → alpha Truth Fixpack v1")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            print(f"\nRunning {test.__name__}...")
            test()
            print(f"✓ PASSED")
            passed += 1
        except AssertionError as e:
            print(f"✗ FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ ERROR: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    if failed > 0:
        sys.exit(1)
    else:
        print("\n✓ ALL STRICT TESTS PASSED!")
