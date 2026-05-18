# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""Finite-energy soliton regularization scaffold with explicit RG open gap."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np


REGULARIZATION_STATUS_LABEL = "regularized finite-energy soliton model; full RG derivation open."


@dataclass(frozen=True)
class SolitonRegularizationConfig:
    """Configuration for finite-energy soliton numerical regularization."""

    cutoff_length: float = 1.616255e-35
    smoothing_kernel: Literal["hard_cutoff", "lorentzian", "gaussian"] = "lorentzian"
    renormalization_scheme: str = "numerical_cutoff_placeholder"


def _regularized_radius(radius: np.ndarray, config: SolitonRegularizationConfig) -> np.ndarray:
    """Return kernel-specific effective radius that avoids direct r=0 division."""
    r = np.asarray(radius, dtype=float)
    if np.any(r < 0):
        raise ValueError("radius must be non-negative")
    if config.cutoff_length <= 0:
        raise ValueError("cutoff_length must be positive")

    eps = config.cutoff_length
    if config.smoothing_kernel == "hard_cutoff":
        return np.maximum(r, eps)
    if config.smoothing_kernel == "lorentzian":
        return np.sqrt(r * r + eps * eps)
    if config.smoothing_kernel == "gaussian":
        return np.sqrt(r * r + 2.0 * eps * eps)
    raise ValueError(f"Unknown smoothing_kernel: {config.smoothing_kernel}")


def energy_density(
    radius: float | np.ndarray,
    core_strength: float = 1.0,
    config: SolitonRegularizationConfig | None = None,
) -> np.ndarray:
    """Regularized soliton energy density with finite r→0 behavior."""
    cfg = config or SolitonRegularizationConfig()
    r_eff = _regularized_radius(np.asarray(radius, dtype=float), cfg)
    return core_strength / (r_eff * r_eff)


def calculate_soliton_energy(
    max_radius: float,
    n_samples: int = 5000,
    core_strength: float = 1.0,
    config: SolitonRegularizationConfig | None = None,
) -> float:
    """Numerically integrate regularized total energy inside a radial cutoff."""
    if max_radius <= 0:
        raise ValueError("max_radius must be positive")
    if n_samples < 8:
        raise ValueError("n_samples must be >= 8")

    r = np.linspace(0.0, max_radius, n_samples)
    rho = energy_density(r, core_strength=core_strength, config=config)
    integrand = 4.0 * np.pi * r * r * rho
    return float(np.trapezoid(integrand, r))
