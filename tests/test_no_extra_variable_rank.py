from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.verify_no_extra_variable_rank import (
    exact_constraint_geometry_checks,
    exact_zero_order_block_checks,
)


def test_exact_constrained_metric_rank_formula() -> None:
    checks = exact_constraint_geometry_checks()
    assert checks["metric_rank"] == 10
    assert checks["lorentz_kernel_rank"] == 6
    assert checks["right_inverse_residual_rank"] == 0
    assert checks["frame_basis_rank"] == 16
    assert checks["gauge_only_restricted_metric_rank"] == 10
    assert checks["gauge_only_formula_rank"] == 10
    assert checks["eight_no_absorption_metric_rank"] == 8
    assert checks["eight_no_absorption_formula_rank"] == 8
    assert checks["field_absorption_graph_residual_rank"] == 0
    assert checks["field_absorption_projection_rank"] == 16
    assert checks["field_absorption_metric_rank"] == 10
    assert checks["field_absorption_formula_rank"] == 10


def test_dirac_zero_order_blocks_are_exactly_invertible_off_their_zero_set() -> None:
    checks = exact_zero_order_block_checks()
    assert checks["scalar_inverse_residual_rank"] == 0
    assert checks["mixed_product_residual_rank"] == 0
    assert checks["mixed_inverse_residual_rank"] == 0
