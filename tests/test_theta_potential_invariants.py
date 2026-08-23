"""Regression gates for the exact local Theta-potential classification."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_verifier(name: str) -> str:
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / name)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def test_exact_invariant_space_classification() -> None:
    output = run_verifier("verify_theta_potential_invariants.py")
    assert "quadratic invariant space dimension = 1" in output
    assert "quartic invariant space dimension = 2" in output
    assert "NOT TESTED" in output
    assert "LEAN-PENDING" in output


def test_independent_finite_transformation_checks() -> None:
    output = run_verifier("verify_theta_potential_invariants_independent.py")
    assert "preserve H and |det X|^2" in output
    assert "257/16" in output
    assert "NOT TESTED" in output
