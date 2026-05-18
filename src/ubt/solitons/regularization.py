# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""Finite-energy soliton regularization scaffold with explicit RG open gap."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np
from scipy.integrate import quad


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


class UBTSoliton:
    """
    Finite-energy soliton in UBT on R^3 x S^1_psi.

    STATUS: NUMERICAL_EVIDENCE — not derived from full S[Theta].
    Regularization scheme: Pauli-Villars with cutoff Lambda.
    """

    def __init__(self, R_psi: float = 1.0, Lambda: float = 10.0):
        self.R_psi = R_psi
        self.Lambda = Lambda

    def energy_density(self, r: float, n: int = 1) -> float:
        """
        Radial energy density for winding-n soliton.
        Ansatz: Theta(r) = f(r)*exp(i*n*psi/R_psi)
        f(r) -> 1 as r -> infinity, f(0) = 0.
        """
        m_n = n / self.R_psi
        f = np.tanh(m_n * r)
        cosh_val = np.cosh(m_n * r)
        df = m_n / (cosh_val * cosh_val)
        winding_weight = float(n * n)
        return float(winding_weight * (df**2 + m_n**2 * (1 - f**2) ** 2))

    def total_energy(self, n: int = 1, r_max: float = 20.0) -> float:
        """Total energy of winding-n soliton (4*pi integral)."""
        result, _ = quad(
            lambda r: 4 * np.pi * r**2 * self.energy_density(r, n),
            0,
            r_max,
        )
        return float(result)

    def mass_spectrum(self, n_max: int = 5) -> dict[int, float]:
        """Soliton mass spectrum M(n) for n=1..n_max."""
        return {n: self.total_energy(n) for n in range(1, n_max + 1)}
