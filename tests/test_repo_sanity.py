"""
Tests for the UBT repository sanity guard (verify_repo_sanity.py).

These tests enforce:
  1. The guard script exists and is runnable.
  2. The guard currently reports 0 violations (sweep is complete).
  3. The guard correctly detects a synthetic collision when injected.
  4. The guard does NOT flag legitimate metric uses.

Run from the repository root:
    pytest tests/test_repo_sanity.py -v

License: MIT
Copyright (c) 2025 Ing. David Jaroš
"""

import subprocess
import sys
import textwrap
from pathlib import Path

import pytest


# ---------------------------------------------------------------------------
# Repo-root detection
# ---------------------------------------------------------------------------

def find_repo_root() -> Path:
    """Walk up from this file until we find the repo root (has pytest.ini)."""
    current = Path(__file__).resolve().parent
    while current != current.parent:
        if (current / "pytest.ini").exists():
            return current
        current = current.parent
    raise FileNotFoundError("Could not find repo root (no pytest.ini found)")


REPO_ROOT = find_repo_root()
GUARD_SCRIPT = REPO_ROOT / "tools" / "verify_repo_sanity.py"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def run_guard(*extra_args) -> subprocess.CompletedProcess:
    """Run verify_repo_sanity.py and return the completed process."""
    return subprocess.run(
        [sys.executable, str(GUARD_SCRIPT)] + list(extra_args),
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )


# ---------------------------------------------------------------------------
# Tests: script exists
# ---------------------------------------------------------------------------

class TestGuardExists:
    def test_script_file_exists(self):
        assert GUARD_SCRIPT.exists(), f"Guard script not found: {GUARD_SCRIPT}"

    def test_script_is_python(self):
        assert GUARD_SCRIPT.suffix == ".py"


# ---------------------------------------------------------------------------
# Tests: clean repo passes guard
# ---------------------------------------------------------------------------

class TestCleanRepoPasses:
    """After the symbol sweep, no violations should remain in guarded files."""

    def test_guard_exits_zero(self):
        result = run_guard()
        assert result.returncode == 0, (
            f"verify_repo_sanity.py found violations (exit {result.returncode}):\n"
            f"{result.stdout}"
        )

    def test_guard_verbose_exits_zero(self):
        result = run_guard("--verbose")
        assert result.returncode == 0, (
            f"verify_repo_sanity.py --verbose found violations:\n{result.stdout}"
        )

    def test_guard_reports_ok(self):
        result = run_guard("--verbose")
        assert "OK" in result.stdout or result.returncode == 0


# ---------------------------------------------------------------------------
# Tests: synthetic collision is detected
# ---------------------------------------------------------------------------

class TestSyntheticCollisionDetected:
    """
    Write a temporary file in a guarded location, inject a known collision,
    verify the guard catches it, then restore the file.

    We use a temp file inside the guarded canonical/geometry/ directory
    so the glob pattern picks it up.
    """

    TEMP_FILE = REPO_ROOT / "canonical" / "geometry" / "_test_sanity_tmp.tex"

    # LaTeX snippets that MUST trigger a violation
    COLLISION_SNIPPETS = [
        # P1: field equation
        r"\mathcal{G}_{\mu\nu} = \kappa \mathcal{T}_{\mu\nu}",
        # P4: Re projection of Einstein tensor
        r"G_{\mu\nu} = \text{Re}(\mathcal{G}_{\mu\nu})",
        # P1: with 8\pi
        r"\mathcal{G}_{\mu\nu} = 8\pi G T_{\mu\nu}",
    ]

    # Snippets that must NOT trigger a violation (metric uses)
    SAFE_SNIPPETS = [
        # lowercase g = metric
        r"g_{\mu\nu} := \text{Re}(\mathcal{G}_{\mu\nu})",
        # inverse metric
        r"\mathcal{G}^{\mu\nu} \mathcal{R}_{\mu\nu}",
        # imaginary metric (dark sector)
        r"\text{Im}(\mathcal{G}_{\mu\nu}) \neq 0",
        # cosmological constant with metric
        r"\mathcal{E}_{\mu\nu} + \Lambda \mathcal{G}_{\mu\nu} = \kappa \mathcal{T}_{\mu\nu}",
    ]

    def _write_tex(self, content: str) -> None:
        self.TEMP_FILE.write_text(
            "% temporary test file — auto-deleted\n"
            "\\documentclass{article}\n"
            "\\begin{document}\n"
            + content + "\n"
            "\\end{document}\n",
            encoding="utf-8",
        )

    def teardown_method(self, _method):
        """Always clean up the temp file."""
        if self.TEMP_FILE.exists():
            self.TEMP_FILE.unlink()

    @pytest.mark.parametrize("snippet", COLLISION_SNIPPETS)
    def test_collision_snippet_is_caught(self, snippet):
        self._write_tex(snippet)
        result = run_guard()
        assert result.returncode == 1, (
            f"Guard should have caught collision in snippet:\n  {snippet}\n"
            f"stdout: {result.stdout}"
        )
        assert "_test_sanity_tmp.tex" in result.stdout

    @pytest.mark.parametrize("snippet", SAFE_SNIPPETS)
    def test_safe_snippet_is_not_flagged(self, snippet):
        self._write_tex(snippet)
        result = run_guard()
        assert result.returncode == 0, (
            f"Guard incorrectly flagged a safe (metric) snippet:\n  {snippet}\n"
            f"stdout: {result.stdout}"
        )


# ---------------------------------------------------------------------------
# Tests: \mathcal{E}_{\mu\nu} not confused with metric
# ---------------------------------------------------------------------------

class TestEinsteinSymbolCorrect:
    """Verify that correctly-used \\mathcal{E}_{\\mu\\nu} does not trigger violations."""

    TEMP_FILE = REPO_ROOT / "canonical" / "geometry" / "_test_sanity_tmp.tex"

    def _write_tex(self, content: str) -> None:
        self.TEMP_FILE.write_text(
            "% temporary test file — auto-deleted\n"
            + content + "\n",
            encoding="utf-8",
        )

    def teardown_method(self, _method):
        if self.TEMP_FILE.exists():
            self.TEMP_FILE.unlink()

    def test_correct_field_equation_no_violation(self):
        snippet = r"\mathcal{E}_{\mu\nu} = \kappa \mathcal{T}_{\mu\nu}"
        self._write_tex(snippet)
        result = run_guard()
        assert result.returncode == 0, (
            f"Correct Einstein symbol triggered false positive:\n{result.stdout}"
        )

    def test_correct_einstein_def_no_violation(self):
        snippet = (
            r"\mathcal{E}_{\mu\nu} = \mathcal{R}_{\mu\nu} "
            r"- \frac{1}{2}\mathcal{G}_{\mu\nu}\mathcal{R}"
        )
        self._write_tex(snippet)
        result = run_guard()
        assert result.returncode == 0, (
            f"Correct Einstein definition triggered false positive:\n{result.stdout}"
        )
