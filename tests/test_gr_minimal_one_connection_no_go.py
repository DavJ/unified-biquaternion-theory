from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load_verifier():
    path = ROOT / "tools" / "verify_minimal_one_connection_gr_no_go.py"
    spec = importlib.util.spec_from_file_location("gr_one_connection_no_go", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_metric_compatible_contortion_torsion_map_is_invertible():
    module = _load_verifier()
    matrix = module.contortion_to_torsion_matrix()
    assert matrix.shape == (24, 24)
    assert matrix.rank() == 24


def test_architecture_no_go_is_propagated_to_authoritative_ledgers():
    required = [
        ROOT / "CLAIMS.yaml",
        ROOT / "CLAIMS_MATRIX.md",
        ROOT / "STATUS.md",
        ROOT / "STATUS_OF_UBT.md",
        ROOT / "WHAT_IS_PROVED.md",
        ROOT / "papers" / "UBT_GR_Submission.tex",
    ]
    token = "GAP-10T-MINIMAL-ONE-CONNECTION-GR"
    for path in required:
        assert token in path.read_text(), path


def test_completion_is_not_overclaimed():
    claims = (ROOT / "CLAIMS.yaml").read_text()
    assert "GAP-10T-JET-KIN: CLOSED LOCALLY" in claims
    assert "GAP-10T-JET-DYN: OPEN" in claims
    assert "GAP-10D: NARROWED" in claims
    paper = (ROOT / "papers" / "UBT_GR_Submission.tex").read_text()
    assert r"does not select $E[\Theta]$" in paper
    assert "derive the completion from the action" in paper
