from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load():
    path = ROOT / "tools" / "verify_gr_endgame_completion.py"
    spec = importlib.util.spec_from_file_location("gr_endgame", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_endgame_verifier_is_green():
    assert all(_load().all_checks().values())


def test_new_gap_statuses_propagated():
    required = [
        ROOT / "CLAIMS.yaml",
        ROOT / "CLAIMS_MATRIX.md",
        ROOT / "STATUS.md",
        ROOT / "STATUS_OF_UBT.md",
        ROOT / "WHAT_IS_PROVED.md",
        ROOT / "DERIVATION_INDEX.md",
        ROOT / "papers" / "UBT_GR_Submission.tex",
    ]
    tokens = [
        "GAP-10T-JET-AUX",
        "GAP-10T-JET-CONSTRAINT-SELECTION",
        "GAP-10D-UNDERDETERMINATION",
        "GAP-10D-A2-FORM",
        "GAP-10D-SPECTRAL-IR",
    ]
    for path in required:
        text = path.read_text(errors="ignore")
        for token in tokens:
            assert token in text, (path, token)


def test_unconditional_gr_is_not_overclaimed():
    import yaml

    payload = yaml.safe_load((ROOT / "CLAIMS.yaml").read_text(errors="ignore"))
    gr = payload["claims"]["gr_chain"]
    assumptions = "\n".join(gr["assumptions"])
    assert "GAP-10D: NARROWED" in assumptions
    assert "GAP-10T-JET-DYN: NARROWED" in assumptions
    assert "complete conditional effective GR branch" in assumptions
    forbidden = set(gr["forbidden_wording"])
    assert "GR is derived unconditionally from UBT" in forbidden
    assert "Newton constant is predicted without assumptions" in forbidden
    assert "GAP-10D: CLOSED UNCONDITIONALLY" not in assumptions


def test_old_5d_spectral_note_is_marked_superseded_for_gr():
    path = ROOT / "research_tracks" / "T3_ALPHA" / "seeley_dewitt_coefficients.tex"
    text = path.read_text(errors="ignore")
    assert "SUPERSEDED FOR THE GR COEFFICIENT" in text
    assert r"gap\_10d\_induced\_gravity\_endgame.tex" in text
