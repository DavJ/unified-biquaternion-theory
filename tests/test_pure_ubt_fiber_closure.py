from tools.verify_pure_ubt_fiber_closure import (
    corank_one_adjugate,
    fiber_completed_closure_matrix,
    induced_metric_at_origin,
    single_section_closure_matrix,
    verify_local_normalization,
)

import sympy as sp


def test_single_section_rank_obstruction() -> None:
    closure = single_section_closure_matrix()
    assert closure.rank() == 4
    assert len(closure.nullspace()) == 6


def test_fiber_completed_rank_ten() -> None:
    closure = fiber_completed_closure_matrix()
    assert closure.rank() == 10
    assert closure.nullspace() == []


def test_lorentzian_tangent_gram_matrix() -> None:
    assert induced_metric_at_origin() == sp.diag(-1, 1, 1, 1)


def test_local_normalization_freezes_lapse() -> None:
    assert verify_local_normalization() == -1


def test_corank_one_adjugate_is_rank_one() -> None:
    matrix_rank, adjugate_rank, adjugate = corank_one_adjugate()
    assert matrix_rank == 9
    assert adjugate_rank == 1
    assert adjugate == sp.diag(*([0] * 9), 1)
