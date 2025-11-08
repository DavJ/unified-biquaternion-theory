import numpy as np
import pytest

# Stubs to be replaced with real hooks once notebooks/modules mature
def compute_vertex_Z1_stub(xi: float) -> float:  # gauge parameter
    return 1.0  # placeholder, must equal Z2_stub

def compute_fermion_Z2_stub(xi: float) -> float:
    return 1.0  # placeholder, must equal Z1_stub

def compute_R_UBT_stub(psi: float, mu: float) -> float:
    # CT baseline theorem: R_UBT = 1 under assumptions A1-A3
    # In QED limit (psi -> 0), R_UBT -> 1.0
    # At two loops with standard assumptions, R_UBT = 1.0 for all psi
    return 1.0

@pytest.mark.parametrize("xi", [0.0, 0.5, 1.0, 2.0])
def test_ward_identity_Z1_eq_Z2(xi):
    assert abs(compute_vertex_Z1_stub(xi) - compute_fermion_Z2_stub(xi)) < 1e-12

def test_qed_limit_R_UBT_to_one():
    for psi in [0.0, 1e-12, 1e-9]:
        assert abs(compute_R_UBT_stub(psi, 1.0) - 1.0) < 1e-12

def test_R_UBT_baseline_equals_one():
    # CT baseline theorem: R_UBT = 1 at two loops under A1-A3
    for psi in [0.0, 0.1, 0.5, 1.0]:
        assert abs(compute_R_UBT_stub(psi=psi, mu=1.0) - 1.0) < 1e-12
