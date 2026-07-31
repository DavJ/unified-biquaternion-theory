"""Regression tests for the corrected two-mode Hermitian metric channel."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np


MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "compute_h_munu_vacuum.py"
SPEC = importlib.util.spec_from_file_location("compute_h_munu_vacuum", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MOD = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MOD
SPEC.loader.exec_module(MOD)


def _direct_metric(theta0, theta1, radius: float, psi: np.ndarray) -> np.ndarray:
    """Compute sum_a |E_psi^a|^2 directly from the four complex coefficients."""
    theta0_arr = np.asarray(theta0, dtype=complex)
    theta1_arr = np.asarray(theta1, dtype=complex)
    phase0 = np.exp(1j * psi / radius)
    phase1 = np.exp(2j * psi / radius)
    e = (
        (1j / radius) * theta0_arr[:, None] * phase0[None, :]
        + (2j / radius) * theta1_arr[:, None] * phase1[None, :]
    )
    return np.sum(e * np.conjugate(e), axis=0)


def test_two_mode_h_is_identically_zero() -> None:
    result = MOD.canonical_example()
    assert np.array_equal(result.h_vals, np.zeros_like(result.h_vals))
    assert result.h_max == 0.0
    assert result.phi_is_physical is False


def test_closed_formula_matches_direct_hermitian_norm() -> None:
    theta0 = (1 + 2j, -0.3 + 0.7j, 0.2 - 0.9j, 1.1 + 0.4j)
    theta1 = (-0.4 + 1.3j, 0.6 - 0.1j, 0.8 + 0.2j, -0.5 - 0.7j)
    radius = 1.7
    psi = np.linspace(0.0, 2.0 * np.pi * radius, 257, endpoint=False)

    direct = _direct_metric(theta0, theta1, radius, psi)
    formula = MOD.compute_G_psi_psi_real(theta0, theta1, radius, psi)

    assert np.max(np.abs(direct.imag)) < 1e-12
    assert np.allclose(formula, direct.real, rtol=1e-12, atol=1e-12)


def test_cross_sum_is_real_for_arbitrary_complex_overlap() -> None:
    overlap = 0.37 - 1.91j
    phases = np.linspace(-3.0, 3.0, 101)
    cross = np.exp(-1j * phases) * overlap + np.exp(1j * phases) * overlap.conjugate()
    assert np.max(np.abs(cross.imag)) < 1e-14
