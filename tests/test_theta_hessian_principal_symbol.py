# UBT-AI-PROVENANCE-BEGIN
# schema: ubt-ai-provenance/v1
# tier: B_machine_verified
# ai_assistance: disclosed
# human_review: machine-verification
# editorial_responsibility: Ing. David Jaroš
# policy: ../AI_PROVENANCE.md
# notice: Machine-verified against named sources or verifiers; individual attestation is not claimed.
# UBT-AI-PROVENANCE-END
"""Regression gates for the Theta-Hessian principal-symbol decision."""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "verify_theta_hessian_principal_symbol.py"
NOTE = ROOT / "canonical" / "gr_closure" / "gap_10d_theta_hessian_principal_symbol.tex"
ENDGAME = ROOT / "canonical" / "gr_closure" / "gap_10d_induced_gravity_endgame.tex"
README = ROOT / "canonical" / "gr_closure" / "README.md"


def _load():
    spec = importlib.util.spec_from_file_location("theta_hessian_symbol", TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_theta_hessian_principal_symbol_verifier_is_green() -> None:
    assert all(_load().all_checks().values())


def test_note_keeps_fixed_and_composite_claims_separate() -> None:
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "GAP-10D-HESS-FIXED",
        "GAP-10D-RES-PRINCIPAL",
        "GAP-10D-HESS-COMP",
        "fixed-background",
        "not conic",
        "full composite",
        "does not derive",
    ]
    for token in required:
        assert token in text
    assert "GAP-10D: CLOSED UNCONDITIONALLY" not in text
    assert "Newton constant is predicted" not in text


def test_authoritative_b_tier_files_reference_the_decision() -> None:
    for path in (ENDGAME, README):
        text = path.read_text(encoding="utf-8")
        assert ("gap_10d_theta_hessian_principal_symbol" in text or r"gap\_10d\_theta\_hessian\_principal\_symbol" in text)
        assert "GAP-10D-HESS-FIXED" in text
        assert "GAP-10D-RES-PRINCIPAL" in text
        assert "GAP-10D-HESS-COMP" in text


def test_new_pdf_root_has_visible_provenance_contract() -> None:
    text = NOTE.read_text(encoding="utf-8")
    assert r"\usepackage{ubtprovenance}" in text
    assert r"\UBTTier{B}" in text
    assert r"\UBTProvenanceNotice" in text
