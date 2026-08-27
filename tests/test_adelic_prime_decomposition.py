"""Regression tests for the adelic prime-decomposition verifier."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL_PATH = ROOT / "tools" / "verify_adelic_prime_decomposition.py"


def load_tool():
    spec = importlib.util.spec_from_file_location(
        "verify_adelic_prime_decomposition", TOOL_PATH
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


TOOL = load_tool()


def test_valuation_fock_bijection() -> None:
    TOOL.check_valuation_fock_bijection()


def test_local_radial_trace() -> None:
    TOOL.check_local_radial_trace()


def test_finite_tensor_trace() -> None:
    TOOL.check_finite_tensor_trace()


def test_self_adjoint_core_truncation() -> None:
    TOOL.check_self_adjoint_core_truncation()


def test_crt_projectors() -> None:
    TOOL.check_crt_projectors()


def test_revival_phase_factorization() -> None:
    TOOL.check_revival_phase_factorization()


def test_archimedean_mellin_completion() -> None:
    TOOL.check_archimedean_mellin_completion()


def test_factorization_output_gate() -> None:
    TOOL.check_factorization_output_gate()
