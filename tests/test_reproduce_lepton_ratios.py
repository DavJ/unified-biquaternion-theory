"""
Tests for the lepton mass ratio reproduction script (Appendix W forensic audit).

These tests verify that:
  1. The script tools/reproduce_lepton_ratios.py exists and all variants run.
  2. The canonical eigenvalue formula produces the exact locked reference values.
  3. The canonical formula gives a MISMATCH (exit code 1) — documented expected result.
  4. candidate_integer exits 1 (NOT_A_PREDICTION — uses 3 calibrations).
  5. candidate_hopf exits 1 (MISMATCH — p=3/2 gives ~2.83, not 207).
  6. --variant all exits 1 (no variant reproduces ratios under 1-calibration rule).

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
    "E_01_R":               1.11803399,
    "E_02_R":               2.06155281,
    "E_10_R":               1.50000000,
    "E_11_R":               1.80277564,
    "ratio_mu_e_formula":   1.84390889,
    "ratio_tau_mu_formula": 0.72760688,
}

EXP_MU_OVER_E   = 206.768283
EXP_TAU_OVER_MU = 16.817029

TOLERANCE_LOCK = 1e-6   # tolerance for locked formula values
TOLERANCE_PCT  = 0.01   # 1% tolerance for "reproduced" verdict


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def eigenvalue(n: int, m: int, delta: float = DELTA, dp: float = DELTA_PRIME) -> float:
    return math.sqrt((n + delta) ** 2 + (m + dp) ** 2)


def run_script(*extra_args) -> subprocess.CompletedProcess:
    """Run the reproduction script and return completed process."""
    return subprocess.run(
        [sys.executable, str(SCRIPT)] + list(extra_args),
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )


# ---------------------------------------------------------------------------
# Tests: script exists
# ---------------------------------------------------------------------------

class TestScriptExists:
    def test_script_file_exists(self):
        assert SCRIPT.exists(), f"Script not found: {SCRIPT}"

    def test_script_is_python(self):
        assert SCRIPT.suffix == ".py"


# ---------------------------------------------------------------------------
# Tests: canonical formula values (locked)
# ---------------------------------------------------------------------------

class TestCanonicalFormulaValues:
    """Verify the eigenvalue formula produces the locked reference values."""

    def test_E_01(self):
        assert abs(eigenvalue(0, 1) - LOCKED["E_01_R"]) < TOLERANCE_LOCK

    def test_E_02(self):
        assert abs(eigenvalue(0, 2) - LOCKED["E_02_R"]) < TOLERANCE_LOCK

    def test_E_10(self):
        assert abs(eigenvalue(1, 0) - LOCKED["E_10_R"]) < TOLERANCE_LOCK

    def test_E_11(self):
        assert abs(eigenvalue(1, 1) - LOCKED["E_11_R"]) < TOLERANCE_LOCK

    def test_ratio_mu_e(self):
        ratio = eigenvalue(0, 2) / eigenvalue(0, 1)
        assert abs(ratio - LOCKED["ratio_mu_e_formula"]) < TOLERANCE_LOCK

    def test_ratio_tau_mu(self):
        ratio = eigenvalue(1, 0) / eigenvalue(0, 2)
        assert abs(ratio - LOCKED["ratio_tau_mu_formula"]) < TOLERANCE_LOCK


# ---------------------------------------------------------------------------
# Tests: canonical mismatch is the documented expected result
# ---------------------------------------------------------------------------

class TestCanonicalMismatchDocumented:
    """Lock in that the canonical formula does NOT reproduce experiment."""

    def test_mu_e_large_mismatch(self):
        ratio = eigenvalue(0, 2) / eigenvalue(0, 1)
        rel_err = abs(ratio - EXP_MU_OVER_E) / EXP_MU_OVER_E
        assert rel_err > 0.90, (
            f"Canonical m_μ/m_e = {ratio:.4f} unexpectedly close to exp {EXP_MU_OVER_E}"
        )

    def test_tau_mu_wrong_direction(self):
        """E_(1,0) < E_(0,2): mode hierarchy contradicts mass hierarchy."""
        assert eigenvalue(1, 0) < eigenvalue(0, 2), (
            "Expected E_(1,0) < E_(0,2) (documented wrong-direction problem)"
        )

    def test_tau_mu_large_mismatch(self):
        ratio = eigenvalue(1, 0) / eigenvalue(0, 2)
        rel_err = abs(ratio - EXP_TAU_OVER_MU) / EXP_TAU_OVER_MU
        assert rel_err > 0.90


# ---------------------------------------------------------------------------
# Tests: script --variant canonical
# ---------------------------------------------------------------------------

class TestScriptCanonical:
    def test_exits_with_mismatch(self):
        result = run_script()   # default = canonical
        assert result.returncode == 1, (
            f"Expected exit 1 (mismatch); got {result.returncode}\n{result.stdout}"
        )

    def test_canonical_variant_explicit(self):
        result = run_script("--variant", "canonical")
        assert result.returncode == 1

    def test_output_contains_mismatch(self):
        result = run_script("--variant", "canonical")
        assert "MISMATCH" in result.stdout

    def test_output_contains_missing_factor(self):
        result = run_script("--variant", "canonical")
        assert "Missing factor" in result.stdout

    def test_output_contains_eigenvalues(self):
        result = run_script("--variant", "canonical")
        assert "E_(0,1)" in result.stdout
        assert "E_(0,2)" in result.stdout


# ---------------------------------------------------------------------------
# Tests: script --variant candidate_integer
# ---------------------------------------------------------------------------

class TestScriptCandidateInteger:
    def test_exits_1_not_a_prediction(self):
        result = run_script("--variant", "candidate_integer")
        assert result.returncode == 1, (
            "candidate_integer should exit 1 (NOT_A_PREDICTION)"
        )

    def test_output_labels_not_a_prediction(self):
        result = run_script("--variant", "candidate_integer")
        assert "NOT_A_PREDICTION" in result.stdout or "NOT derived" in result.stdout

    def test_output_names_extra_calibrations(self):
        result = run_script("--variant", "candidate_integer")
        # n_mu and n_tau must be flagged as calibration parameters
        assert "n_mu" in result.stdout and "n_tau" in result.stdout

    def test_integer_ratios_numerically_close(self):
        """n_mu=207, n_tau=3477 give <1% error vs experiment — but that's by construction."""
        n_mu, n_tau = 207, 3477
        err_mu  = abs(n_mu               - EXP_MU_OVER_E)   / EXP_MU_OVER_E
        err_tau = abs(n_tau / n_mu        - EXP_TAU_OVER_MU) / EXP_TAU_OVER_MU
        assert err_mu  < TOLERANCE_PCT, "n_mu=207 numerically close to exp (expected)"
        assert err_tau < TOLERANCE_PCT, "n_tau/n_mu numerically close to exp (expected)"


# ---------------------------------------------------------------------------
# Tests: script --variant candidate_hopf
# ---------------------------------------------------------------------------

class TestScriptCandidateHopf:
    def test_exits_1_mismatch(self):
        result = run_script("--variant", "candidate_hopf")
        assert result.returncode == 1, (
            "candidate_hopf should exit 1 (MISMATCH)"
        )

    def test_output_contains_mismatch(self):
        result = run_script("--variant", "candidate_hopf")
        assert "MISMATCH" in result.stdout

    def test_hopf_p15_gives_small_ratio(self):
        """With p=1.5 the formula gives m_μ/m_e = 2^1.5 ≈ 2.83, not 207."""
        ratio_mu_e = 2 ** 1.5
        assert abs(ratio_mu_e - 2.828427) < 1e-5
        # Must be very far from experiment
        rel_err = abs(ratio_mu_e - EXP_MU_OVER_E) / EXP_MU_OVER_E
        assert rel_err > 0.98

    def test_no_single_p_fits_both(self):
        """log(207)/log(2) ≠ log(16.8)/log(3/2): no single p works."""
        p_mu  = math.log(EXP_MU_OVER_E)   / math.log(2)
        p_tau = math.log(EXP_TAU_OVER_MU) / math.log(1.5)
        assert abs(p_mu - p_tau) > 0.5, (
            f"p_mu={p_mu:.3f}, p_tau={p_tau:.3f} — should be inconsistent"
        )


# ---------------------------------------------------------------------------
# Tests: --variant all
# ---------------------------------------------------------------------------

class TestScriptVariantAll:
    def test_exits_1_no_variant_works(self):
        result = run_script("--variant", "all")
        assert result.returncode == 1, (
            "Expected exit 1: no variant reproduces ratios under 1-calibration rule"
        )

    def test_overall_message_present(self):
        result = run_script("--variant", "all")
        assert "OVERALL" in result.stdout

    def test_all_three_variants_run(self):
        result = run_script("--variant", "all")
        assert "VARIANT: canonical" in result.stdout
        assert "VARIANT: candidate_integer" in result.stdout
        assert "VARIANT: candidate_hopf" in result.stdout

