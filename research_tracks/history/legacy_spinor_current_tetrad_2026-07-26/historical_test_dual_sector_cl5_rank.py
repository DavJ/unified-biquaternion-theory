from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.verify_dual_sector_cl5_rank import (
    EXPECTED_DUAL_E_DET,
    EXPECTED_DUAL_MINOR_DET,
    EXPECTED_SINGLE_E_DET,
    EXPECTED_SINGLE_MINOR_DET,
    cl5_two_branch_checks,
    exact_dual_witness,
    exact_single_witness,
)


def test_cl5_two_branch_faithful_representation() -> None:
    checks = cl5_two_branch_checks()
    assert checks["clifford_residual"] < 1e-12
    assert checks["monomial_count"] == 32
    assert checks["faithful_complex_span_rank"] == 32
    assert checks["projector_plus_rank"] == 4
    assert checks["projector_minus_rank"] == 4


def test_single_sector_exact_rank_ten_witness() -> None:
    checks = exact_single_witness()
    assert checks["tetrad_det"] == EXPECTED_SINGLE_E_DET
    assert checks["selected_10x10_minor_det"] == EXPECTED_SINGLE_MINOR_DET
    assert checks["selected_minor_rank"] == 10


def test_dual_sector_exact_rank_ten_witness() -> None:
    checks = exact_dual_witness()
    assert checks["tetrad_det"] == EXPECTED_DUAL_E_DET
    assert checks["selected_10x10_minor_det"] == EXPECTED_DUAL_MINOR_DET
    assert checks["selected_minor_rank"] == 10
