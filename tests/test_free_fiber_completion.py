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

def test_completion_note_keeps_conditional_status_and_open_bridges() -> None:
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    note = (
        root
        / "research_tracks/T1_GR/free_fiber_completion/"
        "gap_10r_free_fiber_embedding_completion.tex"
    ).read_text(encoding="utf-8").lower()
    assert "conditional local vacuum equivalence" in note
    assert "flat ambient profile connection" in note
    assert "canonical pointwise spin-lift" in note
    assert "fourteen-mode sector" in note
    assert "not yet a" in note
    assert "derivation from the older ubt master" in note

