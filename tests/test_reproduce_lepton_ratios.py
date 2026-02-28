"""
Tests for the lepton mass ratio reproduction script (Appendix W forensic audit).

These tests verify that:
  1. The script tools/reproduce_lepton_ratios.py exists and is importable.
  2. The eigenvalue formula produces the exact values locked in the canonical derivation.
  3. The formula gives a MISMATCH with the Appendix W claims (exit code 1),
     which is the documented and expected behaviour.

Run from the repository root:
    pytest tests/test_reproduce_lepton_ratios.py -v

License: MIT
Copyright (c) 2025 Ing. David Jaroš
"""

import math
import subprocess
import sys
from pathlib import Path

import pytest


# ---------------------------------------------------------------------------
# Repo-root detection (consistent with other test files in this directory)
# ---------------------------------------------------------------------------

def find_repo_root() -> Path:
    """Find repository root by walking up from this file."""
    current = Path(__file__).resolve().parent
    while current != current.parent:
        if (current / "pytest.ini").exists():
            return current
        current = current.parent
    raise FileNotFoundError("Could not find repo root (no pytest.ini found)")


REPO_ROOT = find_repo_root()
SCRIPT = REPO_ROOT / "tools" / "reproduce_lepton_ratios.py"


# ---------------------------------------------------------------------------
# Locked reference values from canonical_derivation.md
# Any formula change must justify a change to these constants.
# ---------------------------------------------------------------------------

DELTA = 0.5
DELTA_PRIME = 0.0

LOCKED = {
    "E_01_R":              1.11803399,
    "E_02_R":              2.06155281,
    "E_10_R":              1.50000000,
    "E_11_R":              1.80277564,
    "ratio_mu_e_formula":  1.84390889,
    "ratio_tau_mu_formula": 0.72760688,
}

CLAIMED_MU_OVER_E   = 207.3
CLAIMED_TAU_OVER_MU = 16.9

TOLERANCE = 1e-6   # for locked formula values


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def eigenvalue(n: int, m: int, delta: float = DELTA, dp: float = DELTA_PRIME) -> float:
    return math.sqrt((n + delta) ** 2 + (m + dp) ** 2)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestScriptExists:
    def test_script_file_exists(self):
        assert SCRIPT.exists(), f"Script not found: {SCRIPT}"

    def test_script_is_python(self):
        assert SCRIPT.suffix == ".py"


class TestFormulaValues:
    """Verify the eigenvalue formula produces the locked reference values."""

    def test_E_01(self):
        val = eigenvalue(0, 1)
        assert abs(val - LOCKED["E_01_R"]) < TOLERANCE, (
            f"E_(0,1)·R = {val}, expected {LOCKED['E_01_R']}"
        )

    def test_E_02(self):
        val = eigenvalue(0, 2)
        assert abs(val - LOCKED["E_02_R"]) < TOLERANCE

    def test_E_10(self):
        val = eigenvalue(1, 0)
        assert abs(val - LOCKED["E_10_R"]) < TOLERANCE

    def test_E_11(self):
        val = eigenvalue(1, 1)
        assert abs(val - LOCKED["E_11_R"]) < TOLERANCE

    def test_ratio_mu_e(self):
        ratio = eigenvalue(0, 2) / eigenvalue(0, 1)
        assert abs(ratio - LOCKED["ratio_mu_e_formula"]) < TOLERANCE

    def test_ratio_tau_mu(self):
        ratio = eigenvalue(1, 0) / eigenvalue(0, 2)
        assert abs(ratio - LOCKED["ratio_tau_mu_formula"]) < TOLERANCE


class TestMismatchDocumented:
    """
    The formula does NOT reproduce the claimed 207.3 / 16.9.
    These tests lock in that the mismatch IS the documented result.
    """

    def test_mu_e_does_not_match_claim(self):
        ratio = eigenvalue(0, 2) / eigenvalue(0, 1)
        rel_err = abs(ratio - CLAIMED_MU_OVER_E) / CLAIMED_MU_OVER_E
        assert rel_err > 0.90, (
            f"Unexpectedly, m_μ/m_e formula ratio {ratio:.4f} matches the claim "
            f"{CLAIMED_MU_OVER_E} within 10 % — mismatch should be ~99 %."
        )

    def test_tau_mu_does_not_match_claim(self):
        ratio = eigenvalue(1, 0) / eigenvalue(0, 2)
        rel_err = abs(ratio - CLAIMED_TAU_OVER_MU) / CLAIMED_TAU_OVER_MU
        assert rel_err > 0.90, (
            f"Unexpectedly, m_τ/m_μ formula ratio {ratio:.4f} matches the claim "
            f"{CLAIMED_TAU_OVER_MU} within 10 % — mismatch should be ~96 %."
        )

    def test_mode_ordering_wrong(self):
        """E_(1,0) < E_(0,2): the 'tau' mode is lighter than the 'muon' mode."""
        assert eigenvalue(1, 0) < eigenvalue(0, 2), (
            "Expected E_(1,0) < E_(0,2) (wrong-direction problem documented in audit)"
        )


class TestScriptExitCode:
    """Run the script and verify it exits with code 1 (mismatch documented)."""

    def test_script_exits_with_mismatch(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
        )
        # Exit code 1 means mismatch — which is the expected/documented outcome
        assert result.returncode == 1, (
            f"Expected exit code 1 (mismatch documented), got {result.returncode}.\n"
            f"stdout: {result.stdout}\nstderr: {result.stderr}"
        )

    def test_script_outputs_mismatch_message(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
        )
        assert "MISMATCH" in result.stdout, (
            "Expected 'MISMATCH' in script output"
        )

    def test_script_outputs_missing_factor(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
        )
        assert "Missing factor" in result.stdout or "missing" in result.stdout.lower(), (
            "Expected missing-factor explanation in output"
        )
