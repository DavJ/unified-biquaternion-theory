# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""Tests for quantum evolution scaffold reproducibility and deterministic limits."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ubt.quantum.quantum_scaffold import (  # noqa: E402
    PHENOMENOLOGICAL_NOISE_LABEL,
    ThetaState,
    evolve_theta,
)


def _rhs_linear(state: ThetaState) -> np.ndarray:
    return np.full_like(state.field, 0.25)


def test_deterministic_mode_recovered_with_zero_noise() -> None:
    state = ThetaState(field=np.array([1.0, 2.0, 3.0]))
    next_a = evolve_theta(state, dt=0.2, deterministic_rhs=_rhs_linear, noise_amplitude=0.0, seed=1)
    next_b = evolve_theta(state, dt=0.2, deterministic_rhs=_rhs_linear, noise_amplitude=0.0, seed=999)
    expected = state.field + 0.2 * _rhs_linear(state)

    assert np.allclose(next_a.field, expected)
    assert np.allclose(next_b.field, expected)
    assert np.allclose(next_a.field, next_b.field)


def test_stochastic_mode_reproducible_for_fixed_seed() -> None:
    state = ThetaState(field=np.array([1.0 + 0.0j, 2.0 + 1.0j]))
    next_a = evolve_theta(state, dt=0.1, deterministic_rhs=_rhs_linear, noise_amplitude=0.05, seed=42)
    next_b = evolve_theta(state, dt=0.1, deterministic_rhs=_rhs_linear, noise_amplitude=0.05, seed=42)
    next_c = evolve_theta(state, dt=0.1, deterministic_rhs=_rhs_linear, noise_amplitude=0.05, seed=43)

    assert np.allclose(next_a.field, next_b.field)
    assert not np.allclose(next_a.field, next_c.field)


def test_noise_label_is_explicitly_phenomenological() -> None:
    assert "phenomenological quantum-noise proxy" in PHENOMENOLOGICAL_NOISE_LABEL
    assert "pending derivation from UBT action" in PHENOMENOLOGICAL_NOISE_LABEL
