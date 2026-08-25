"""Regression tests for the graded prime-Fock Möbius bridge verifier."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL_PATH = ROOT / "tools" / "verify_graded_mobius_bridge.py"


def load_tool():
    spec = importlib.util.spec_from_file_location("verify_graded_mobius_bridge", TOOL_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


TOOL = load_tool()


def test_exact_graded_coefficients() -> None:
    TOOL.check_exact_coefficients([2, 3, 5, 7, 11])


def test_repeated_prime_factors_have_zero_mobius_weight() -> None:
    assert TOOL.mobius(1) == 1
    assert TOOL.mobius(2 * 3 * 5) == -1
    assert TOOL.mobius(2 * 3) == 1
    assert TOOL.mobius(2 * 2 * 3) == 0


def test_finite_bosonic_graded_dirichlet_inverse() -> None:
    TOOL.check_dirichlet_inverse([2, 3, 5, 7], 500)


def test_partition_function_inverse() -> None:
    TOOL.check_partition_functions([2, 3, 5, 7, 11, 13], 2e-13)


def test_zeta2_benchmark() -> None:
    TOOL.check_zeta2_benchmark(5000, 5e-5)

