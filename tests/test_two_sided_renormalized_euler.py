"""Regression tests for the two-sided renormalized Euler verifier."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL_PATH = ROOT / "tools" / "verify_two_sided_renormalized_euler.py"


def load_tool():
    spec = importlib.util.spec_from_file_location(
        "verify_two_sided_renormalized_euler", TOOL_PATH
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


TOOL = load_tool()


def test_finite_maclaurin_factorization() -> None:
    TOOL.check_finite_maclaurin_factorization()


def test_remainder_convergence_signatures() -> None:
    TOOL.check_remainder_convergence_signatures()


def test_two_sided_reflection() -> None:
    TOOL.check_two_sided_reflection()


def test_first_layer_operator_norm() -> None:
    TOOL.check_first_layer_operator_norm()


def test_higher_layer_norm_bound() -> None:
    TOOL.check_higher_layer_norm_bound()


def test_prime_power_log_derivative() -> None:
    TOOL.check_prime_power_log_derivative()
