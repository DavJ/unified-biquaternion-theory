import sympy as sp

from tools.verify_free_fiber_completion import (
    ambient_metric,
    gauss_checks,
    profile_metric_and_rank,
)


def test_profile_block_has_signature_13_1() -> None:
    _, _, _, gram14 = profile_metric_and_rank()
    assert gram14 == ambient_metric()


def test_free_profile_jet_has_full_ranks() -> None:
    metric, closure_rank, osculating_rank, _ = profile_metric_and_rank()
    assert metric == sp.diag(-1, 1, 1, 1)
    assert closure_rank == 10
    assert osculating_rank == 14


def test_gauss_scalar_and_riemann_symmetries() -> None:
    scalar_riemann, scalar_b, anti, exchange, bianchi = gauss_checks()
    assert scalar_riemann == scalar_b
    assert anti
    assert exchange
    assert bianchi
