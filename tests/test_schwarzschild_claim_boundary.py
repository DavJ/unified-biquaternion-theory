"""Regression guards for the canonical boundary of the legacy Schwarzschild ansatz."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _load_legacy_verifier():
    path = ROOT / "tools" / "verify_schwarzschild_theta.py"
    spec = importlib.util.spec_from_file_location("schwarzschild_legacy", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_legacy_spatial_identity_is_kept_but_bounded():
    verifier = _load_legacy_verifier()
    assert verifier.verify_schwarzschild(
        M=1.0, r_values=[2.0, 5.0, 10.0], tolerance=1e-10
    )
    assert verifier.verify_canonical_boundary(M=1.0)


def test_authoritative_status_keeps_microscopic_schwarzschild_selection_open():
    claims = (ROOT / "CLAIMS.yaml").read_text(encoding="utf-8")
    proved = (ROOT / "WHAT_IS_PROVED.md").read_text(encoding="utf-8")
    correction = (
        ROOT / "canonical" / "geometry" / "schwarzschild_claim_status.yaml"
    ).read_text(encoding="utf-8")
    for text in (claims, proved, correction):
        assert "GAP-U2Theta" in text
        assert "OPEN" in text
    assert "status: CLOSED_CONDITIONALLY_FOR_GR_RECOVERY" in correction
    assert "microscopic_direct_selection_status: OPEN" in correction
    assert "INVALID_AS_CANONICAL_DERIVATION" in correction


def test_paired_gr_paper_correction_exists():
    en = ROOT / "papers" / "UBT_GR_Submission_canonical_correction.en.tex"
    cs = ROOT / "papers" / "UBT_GR_Submission_canonical_correction.cs.tex"
    record = ROOT / "papers" / "UBT_GR_Submission.verification.yaml"
    for path in (en, cs, record):
        assert path.is_file(), path
    for path in (en, cs):
        text = path.read_text(encoding="utf-8")
        assert "GAP-U2Theta" in text
        assert "LEAN-PENDING" in text
        assert r"\partial_\psi\Theta_0=0" in text
        assert r"f'(2M)=\frac54" in text


def test_false_source_is_not_published_as_canonical_html():
    workflow = (ROOT / ".github" / "workflows" / "build_pages.yml").read_text(
        encoding="utf-8"
    )
    wiki_generator = (ROOT / "tools" / "generate_wiki.py").read_text(
        encoding="utf-8"
    )
    path = "canonical/geometry/biquaternionic_vacuum_solutions.tex"
    assert path not in workflow
    assert path not in wiki_generator
