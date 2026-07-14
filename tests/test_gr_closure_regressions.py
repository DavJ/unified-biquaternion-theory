"""Regression guards for the July 2026 pure-Theta GR closure revision."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def test_canonical_metric_uses_compact_fiber_and_constant_normalization() -> None:
    text = read("canonical/THEORY/canonical/canonical_metric_definition.tex")
    assert "\\int_0^{2\\pi R_\\psi}" in text
    assert "\\mathcal N_0" in text
    assert "Local normalization no-go" in text


def test_main_paper_does_not_use_local_denominator_as_definition() -> None:
    text = read("papers/UBT_GR_Submission.tex")
    assert "\\label{eq:fiber_metric}" in text
    assert "would give $g_{00}=-1$ identically" in text
    # The obsolete denominator may be mentioned only as a rejected prescription.
    assert r"\calN &:= \left|\langle \partial_0\Theta" not in text


def test_corrected_abelian_current_places_i_inside_real_trace() -> None:
    text = read("research_tracks/gap_u2/derive_connection_equation.tex")
    assert "q\\operatorname{ReTr}\\!\\left[" in text
    assert "i\\left(\\Theta^\\dagger D^\\mu\\Theta" in text
    assert "i q\\,\\operatorname{Re}" not in text


def test_claim_ledger_contains_residual_gaps() -> None:
    claims = read("CLAIMS.yaml")
    for gap in ("GAP-10K", "GAP-10S", "GAP-10J", "GAP-10R", "GAP-10G", "GAP-U2Theta"):
        assert gap in claims
    assert "Maxwell field generates vacuum Schwarzschild" in claims


def test_pure_theta_theorem_contains_holomorphic_construction() -> None:
    text = read("canonical/gr_closure/pure_ubt_fiber_closure.tex")
    assert "Existence of holomorphic periodic fiber-free UBT jets" in text
    assert "no independent polynomial in" in text
    assert "Uniqueness of the compact-fiber zero-mode projection" in text
    assert "Finite-mode genericity of fiber-freeness" in text
    assert "GAP-10R" in text
