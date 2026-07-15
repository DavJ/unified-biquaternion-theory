"""Regression guards for the July 2026 covariant-tetrad GR reframe."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def test_canonical_metric_is_central_anticommutator() -> None:
    text = read("canonical/THEORY/canonical/canonical_metric_definition.tex")
    assert "E_\\mu^\\sharp E_\\nu+E_\\nu^\\sharp E_\\mu" in text
    assert "g_{\\mu\\nu}\\mathbf1" in text
    assert "no trace" in text.lower()
    assert "rank ten" in text


def test_axiom_rejects_projection_and_fiber_average() -> None:
    text = read("canonical/AXIOMS.md")
    assert "No projection rule" in text
    assert "compact-$\\psi$ average" in text
    assert "central anticommutator" in text
    assert "GAP-10I" in text


def test_main_paper_uses_covariant_tetrad() -> None:
    text = read("papers/UBT_GR_Submission.tex")
    assert "E_\\mu:=\\mathcal N_0^{-1/2}D_\\mu\\Theta" in text
    assert "Projection-Free Metric" in text
    assert "rank ten" in text
    assert "fiber-average constructions are" in text
    assert "not used as a canonical derivation" in text
    assert r"generic Maxwell or $U(1)_\psi$ field does not generate" in text


def test_claim_ledger_contains_covariant_tetrad_gaps() -> None:
    claims = read("CLAIMS.yaml")
    for gap in (
        "GAP-10K",
        "GAP-10Omega",
        "GAP-10L",
        "GAP-10I",
        "GAP-10D",
        "GAP-10psi",
        "GAP-U2Theta",
        "GAP-B-MASTER",
    ):
        assert gap in claims
    assert "compact-psi fiber average is the canonical UBT metric" in claims


def test_fiber_files_are_explicitly_exploratory() -> None:
    for rel in (
        "canonical/gr_closure/pure_ubt_fiber_closure.tex",
        "canonical/gr_closure/linearised_fiber_closure.tex",
    ):
        text = read(rel)
        assert text.startswith("% STATUS NOTICE (2026-07-15): EXPLORATORY")
