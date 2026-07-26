from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.verify_canonical_relation_dirac_lift import (
    exact_lorentz_and_clifford_checks,
    exact_principal_symbol_checks,
    exact_psi_normal_form_checks,
    exact_constraint_projection_checks,
    exact_rank_checks,
)


def test_canonical_metric_and_clifford_lift_are_exact() -> None:
    checks = exact_lorentz_and_clifford_checks()
    assert all(value == 0 for value in checks.values())


def test_tetrad_metric_rank_and_lorentz_kernel_are_exact() -> None:
    checks = exact_rank_checks()
    assert checks["metric_jacobian_rank"] == 10
    assert checks["metric_jacobian_nullity"] == 6
    assert checks["lorentz_kernel_rank"] == 6
    assert checks["lorentz_condition_residual_rank"] == 0
    assert checks["jacobian_on_lorentz_kernel_residual_rank"] == 0
    assert checks["right_inverse_residual_rank"] == 0


def test_principal_symbols_have_exact_metric_factorisation() -> None:
    checks = exact_principal_symbol_checks()
    assert all(value == 0 for value in checks.values())


def test_fifth_channel_gives_exact_psi_normal_form() -> None:
    checks = exact_psi_normal_form_checks()
    assert all(value == 0 for value in checks.values())


def test_constraint_projection_criterion_and_rank_budget_are_exact() -> None:
    checks = exact_constraint_projection_checks()
    assert checks["auxiliary_constraint_rank"] == 8
    assert checks["auxiliary_block_rank"] == 8
    assert checks["lifted_tangent_rank"] == 16
    assert checks["constraint_on_lift_residual_rank"] == 0
    assert checks["metric_rank_on_lift"] == 10
    assert checks["tetrad_only_constraint_rank"] == 8
    assert checks["tetrad_only_tangent_rank"] == 8
    assert checks["tetrad_only_residual_rank"] == 0
    assert checks["tetrad_only_metric_rank"] <= 8
