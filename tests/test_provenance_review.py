"""Regression tests for orthogonal UBT review profiles."""
from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TOOL_PATH = ROOT / "tools" / "verify_provenance_review.py"
REGISTRY = ROOT / "PROVENANCE_REVIEW.yaml"
HESSIAN = "canonical/gr_closure/gap_10d_theta_hessian_principal_symbol.tex"


def load_tool():
    spec = importlib.util.spec_from_file_location("ubt_review_tool", TOOL_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


TOOL = load_tool()


def test_review_registry_is_valid_and_source_blocks_match() -> None:
    assert TOOL.verify(REGISTRY) == []


def test_review_verifier_cli_is_green() -> None:
    proc = subprocess.run(
        [sys.executable, str(TOOL_PATH)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout
    assert "Verified 1 orthogonal review profile" in proc.stdout


def test_hessian_profile_records_exactly_scoped_human_review() -> None:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    profile = data["profiles"][HESSIAN]
    assert profile["machine_verification"]["status"] == "comprehensive_for_named_claims"
    assert profile["human_review"]["status"] == "selected_claims"
    assert profile["editorial_approval"]["status"] == "approved"
    assert len(profile["human_review"]["claims"]) >= 3
    assert "full line-by-line human review of the document" in profile["human_review"]["not_claimed"]
    assert "a demonstrated transition mechanism between UBT sectors" in profile["human_review"]["not_claimed"]


def test_hessian_tex_declares_visible_review_profile() -> None:
    text = (ROOT / HESSIAN).read_text(encoding="utf-8")
    assert "UBT-REVIEW-PROFILE-BEGIN" in text
    assert "machine_verification: comprehensive_for_named_claims" in text
    assert "human_review: selected_claims" in text
    assert "editorial_approval: approved" in text
    assert "\\UBTReviewProfile" in text
    assert "comprehensive for named claims" in text
    assert "selected principal claims" in text
    assert "author approved" in text


def test_latex_package_supports_orthogonal_profile_without_replacing_tier() -> None:
    text = (ROOT / "tex" / "ubtprovenance.sty").read_text(encoding="utf-8")
    assert "\\newcommand{\\UBTReviewProfile}[3]" in text
    assert "Review profile" in text
    assert "PROVENANCE\\_REVIEW.yaml" in text
    assert "provenance tier \\UBT@tier" in text
