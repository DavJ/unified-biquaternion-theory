# Copyright (c) 2025 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""
test_involutions_triplet_space.py
==================================
Golden test asserting algebraic facts about the Z2×Z2×Z2 involution
decomposition of ℬ = ℂ⊗ℍ and the carrier space Vc.

These tests verify fixed mathematical truths:
  - All three involutions satisfy Pk² = id.
  - All three pairs commute.
  - The P2=-1 eigenspace (Vc) has complex dimension 3 with real basis {I,J,K,iI,iJ,iK}.
  - Vc = span_ℂ{I,J,K} under the convention that iI, iJ, iK are i times I, J, K.
  - S3=(+,+,-) is provably empty.
  - The tool's --json-out output is stable across runs.
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
TOOL = REPO_ROOT / "tools" / "involutions_triplet_projectors.py"


def _get_data() -> dict:
    """Run the tool with --json-out and return the parsed JSON."""
    import tempfile
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        tmp = Path(f.name)
    result = subprocess.run(
        [sys.executable, str(TOOL), "--json-out", str(tmp)],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
    )
    assert result.returncode == 0, (
        f"Tool failed (rc={result.returncode}):\n{result.stdout}\n{result.stderr}"
    )
    return json.loads(tmp.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def data():
    return _get_data()


# ---------------------------------------------------------------------------
# Involution verification
# ---------------------------------------------------------------------------

class TestInvolutionProperties:
    """Algebraic properties: Pk² = id, [Pi, Pj] = 0."""

    def test_p1_is_involution(self, data):
        assert data["involution_verification"]["p1_involution"] is True

    def test_p2_is_involution(self, data):
        assert data["involution_verification"]["p2_involution"] is True

    def test_p3_is_involution(self, data):
        assert data["involution_verification"]["p3_involution"] is True

    def test_p1_p2_commute(self, data):
        assert data["involution_verification"]["p1_p2_commute"] is True

    def test_p1_p3_commute(self, data):
        assert data["involution_verification"]["p1_p3_commute"] is True

    def test_p2_p3_commute(self, data):
        assert data["involution_verification"]["p2_p3_commute"] is True


# ---------------------------------------------------------------------------
# Carrier space Vc golden assertions
# ---------------------------------------------------------------------------

class TestCarrierSpaceVc:
    """Golden test: Vc = span_ℂ{I,J,K} is the P2=-1 eigenspace."""

    def test_vc_complex_dimension_is_3(self, data):
        """Vc must be 3-dimensional over ℂ."""
        assert data["carrier_space"]["Vc_complex_dim"] == 3

    def test_vc_real_basis_spans_i_j_k(self, data):
        """The real basis of Vc must be {I, J, K, iI, iJ, iK} (the P2=-1 eigenspace)."""
        expected = {"I", "J", "K", "iI", "iJ", "iK"}
        actual = set(data["carrier_space"]["Vc_real_basis"])
        assert actual == expected, (
            f"Vc real basis mismatch.\n"
            f"  Expected: {sorted(expected)}\n"
            f"  Got:      {sorted(actual)}"
        )

    def test_s3_sector_is_empty(self, data):
        """S3=(+,+,-) must be provably empty under the given involution definitions."""
        assert data["carrier_space"]["S3_empty"] is True, (
            "S3=(+,+,-) sector should be empty — see mathematical note in "
            "tools/involutions_triplet_projectors.py"
        )
        assert data["carrier_space"]["S3_members"] == [], (
            f"S3_members should be empty, got: {data['carrier_space']['S3_members']}"
        )


# ---------------------------------------------------------------------------
# Basis element signature golden values
# ---------------------------------------------------------------------------

# Expected eigenvalue signatures derived from the involution definitions.
# These are fixed mathematical facts and must not change between runs.
GOLDEN_SIGNATURES = {
    "1":  ( 1,  1,  1),
    "I":  ( 1, -1,  1),
    "J":  ( 1, -1, -1),
    "K":  ( 1, -1, -1),
    "i":  (-1,  1,  1),
    "iI": (-1, -1,  1),
    "iJ": (-1, -1, -1),
    "iK": (-1, -1, -1),
}


class TestBasisSignaturesGolden:
    """Each basis element must have the expected (P1, P2, P3) eigenvalue signature."""

    def test_all_elements_present(self, data):
        elements = {r["element"] for r in data["basis_signatures"]}
        assert elements == set(GOLDEN_SIGNATURES.keys())

    @pytest.mark.parametrize("element,expected", GOLDEN_SIGNATURES.items())
    def test_signature(self, data, element, expected):
        row = next(r for r in data["basis_signatures"] if r["element"] == element)
        actual = (row["s1"], row["s2"], row["s3"])
        assert actual == expected, (
            f"Signature mismatch for basis element '{element}'.\n"
            f"  Expected (P1,P2,P3) = {expected}\n"
            f"  Got      (P1,P2,P3) = {actual}"
        )
