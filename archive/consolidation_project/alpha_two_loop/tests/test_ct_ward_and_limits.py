"""
Test Ward identity and Thomson limit using REAL computations (no stubs).

This test suite uses the actual symbolic/numeric implementations from
ct_two_loop_eval.py to verify:
1. Ward identity Z1 = Z2
2. Thomson limit R_UBT → 1
3. Baseline theorem R_UBT = 1 under A1-A3

NO PLACEHOLDER RETURNS - all tests use computational results.
"""

import numpy as np
import pytest
import sys
from pathlib import Path

# Add symbolics to path
test_dir = Path(__file__).parent
symbolics_dir = test_dir.parent / "symbolics"
sys.path.insert(0, str(symbolics_dir))

from ct_two_loop_eval import (
    CTVacuumPolarization,
    ward_identity_ok,
    R_UBT_value,
)


@pytest.fixture
def calculator():
    """Provide CT vacuum polarization calculator."""
    return CTVacuumPolarization()


@pytest.mark.parametrize("xi", [0.0, 0.5, 1.0, 2.0])
def test_ward_identity_Z1_eq_Z2(xi, calculator):
    """
    Test Ward identity Z1 = Z2 at various gauge parameter values.
    
    Uses real Ward identity computation from ct_two_loop_eval.py.
    """
    # Use actual Ward identity check (not stub)
    ward_holds, details = calculator.verify_ward_identity(mu_val=1.0, xi_val=xi)
    
    assert ward_holds, \
        f"Ward identity Z1=Z2 violated at ξ={xi}: {details}"


def test_qed_limit_R_UBT_to_one(calculator):
    """
    Test that R_UBT → 1 in the QED limit (ψ → 0).
    
    Uses real numeric computation from ct_two_loop_eval.py.
    """
    for psi in [0.0, 1e-12, 1e-9]:
        R_UBT = calculator.compute_R_UBT_numeric(psi=psi, mu=1.0)
        
        assert abs(R_UBT - 1.0) < 1e-12, \
            f"QED limit: |R_UBT - 1| = {abs(R_UBT - 1.0)} > 1e-12 at ψ={psi}"


def test_R_UBT_baseline_equals_one(calculator):
    """
    Test CT baseline theorem: R_UBT = 1 at two loops under A1-A3.
    
    Uses real Thomson limit computation from ct_two_loop_eval.py.
    """
    for psi in [0.0, 0.1, 0.5, 1.0]:
        # Numeric computation
        R_UBT_num = calculator.compute_R_UBT_numeric(psi=psi, mu=1.0)
        
        assert abs(R_UBT_num - 1.0) < 1e-12, \
            f"Baseline: |R_UBT - 1| = {abs(R_UBT_num - 1.0)} > 1e-12 at ψ={psi}"


def test_symbolic_R_UBT_equals_one(calculator):
    """
    Test symbolic computation of R_UBT = 1.
    
    This verifies the symbolic derivation, not just numeric evaluation.
    """
    R_UBT_sym = calculator.thomson_limit_R_UBT(mu_val=1.0, xi_val=1.0)
    
    # Should be exactly 1 (symbolic integer)
    assert R_UBT_sym == 1, \
        f"Symbolic R_UBT = {R_UBT_sym} ≠ 1"


def test_module_level_functions():
    """Test module-level convenience functions."""
    # Test ward_identity_ok
    assert ward_identity_ok(mu_symbol=1.0, gauge_xi=1.0), \
        "Module-level ward_identity_ok failed"
    
    # Test R_UBT_value
    R_UBT = R_UBT_value(mu_symbol=1.0, gauge_xi=1.0)
    assert R_UBT == 1, \
        f"Module-level R_UBT_value = {R_UBT} ≠ 1"


# Keep original stub functions for backward compatibility with test_no_placeholders
def compute_R_UBT_stub(psi: float, mu: float) -> float:
    """
    Backward-compatible stub that calls real computation.
    
    This allows test_no_placeholders_and_ct_logic.py to continue working
    while actually using real computations underneath.
    """
    calc = CTVacuumPolarization()
    return calc.compute_R_UBT_numeric(psi=psi, mu=mu)
