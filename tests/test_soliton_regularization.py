# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""Tests for finite-energy soliton regularization scaffold."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ubt.solitons.regularization import (  # noqa: E402
    SolitonRegularizationConfig,
    calculate_soliton_energy,
    energy_density,
)


def test_energy_density_finite_at_zero_radius() -> None:
    cfg = SolitonRegularizationConfig(cutoff_length=1e-3, smoothing_kernel="lorentzian")
    rho0 = energy_density(0.0, core_strength=2.0, config=cfg)
    assert np.isfinite(rho0)


def test_total_energy_finite_with_cutoff_regularization() -> None:
    cfg = SolitonRegularizationConfig(cutoff_length=1e-4, smoothing_kernel="gaussian")
    energy = calculate_soliton_energy(max_radius=1.0, n_samples=2000, core_strength=1.0, config=cfg)
    assert np.isfinite(energy)
    assert energy > 0.0


def test_large_radius_behavior_matches_unregularized_limit() -> None:
    cutoff = 1e-6
    cfg = SolitonRegularizationConfig(cutoff_length=cutoff, smoothing_kernel="lorentzian")
    r_large = 1.0
    rho_regularized = float(energy_density(r_large, core_strength=1.0, config=cfg))
    rho_unregularized = 1.0 / (r_large**2)

    assert abs(rho_regularized - rho_unregularized) / rho_unregularized < 1e-9
