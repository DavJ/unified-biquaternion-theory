# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""Quantum scaffold for UBT with explicit open derivation gaps."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Protocol

import numpy as np


PHENOMENOLOGICAL_NOISE_LABEL = (
    "phenomenological quantum-noise proxy pending derivation from UBT action."
)


# TODO(ubt-quantum-gap): Derive canonical commutation relations from the UBT action.
# TODO(ubt-quantum-gap): Derive the Born rule directly from UBT variables.
# TODO(ubt-quantum-gap): Derive a Hilbert-space inner product from UBT structure.
# TODO(ubt-quantum-gap): Derive the path-integral measure in UBT coordinates.
# TODO(ubt-quantum-gap): Derive the map from Theta energy density to probability amplitude.


@dataclass(frozen=True)
class ThetaState:
    """Numerical Theta-state container for scaffold-level evolution experiments."""

    field: np.ndarray
    time: float = 0.0


@dataclass(frozen=True)
class QuantumAmplitude:
    """Placeholder amplitude container pending rigorous UBT derivation."""

    value: complex | None
    status: str = "OPEN_GAP"
    note: str = "Amplitude interpretation pending UBT derivation."


@dataclass(frozen=True)
class ProbabilityDensity:
    """Placeholder probability-density container pending Born-rule derivation."""

    value: float | None
    status: str = "OPEN_GAP"
    note: str = "Probability interpretation pending Born-rule derivation."


class StochasticEvolutionKernel(Protocol):
    """Interface for reproducible stochastic evolution kernels."""

    def __call__(
        self,
        state: ThetaState,
        dt: float,
        deterministic_increment: np.ndarray,
        noise_amplitude: float,
        rng: np.random.Generator,
    ) -> ThetaState:
        """Return next state from a deterministic increment plus optional stochastic term."""


class PathIntegralKernel(Protocol):
    """Interface placeholder for future UBT path-integral weighting."""

    def weight(self, path: list[ThetaState]) -> complex:
        """Return a path weight once UBT path-integral measure is derived."""


class NotDerivedPathIntegralKernel:
    """Explicit placeholder kernel for unresolved UBT path-integral measure."""

    def weight(self, path: list[ThetaState]) -> complex:
        raise NotImplementedError(
            "Path-integral measure in UBT coordinates is OPEN_GAP;"
            " no derived weighting is implemented."
        )


class AdditiveGaussianStochasticKernel:
    """Conservative numerical kernel with optional additive Gaussian perturbation."""

    def __call__(
        self,
        state: ThetaState,
        dt: float,
        deterministic_increment: np.ndarray,
        noise_amplitude: float,
        rng: np.random.Generator,
    ) -> ThetaState:
        if noise_amplitude < 0:
            raise ValueError("noise_amplitude must be non-negative")

        field = np.asarray(state.field)
        increment = np.asarray(deterministic_increment)
        if increment.shape != field.shape:
            raise ValueError("deterministic_increment must match state.field shape")

        next_field = field + dt * increment
        if noise_amplitude > 0.0:
            if np.iscomplexobj(next_field):
                noise = (
                    rng.normal(loc=0.0, scale=noise_amplitude, size=next_field.shape)
                    + 1j * rng.normal(loc=0.0, scale=noise_amplitude, size=next_field.shape)
                )
            else:
                noise = rng.normal(loc=0.0, scale=noise_amplitude, size=next_field.shape)
            next_field = next_field + noise

        return ThetaState(field=np.asarray(next_field), time=state.time + dt)


def evolve_theta(
    state: ThetaState,
    dt: float,
    deterministic_rhs: Callable[[ThetaState], np.ndarray],
    noise_amplitude: float = 0.0,
    seed: int | None = None,
    kernel: StochasticEvolutionKernel | None = None,
) -> ThetaState:
    """Evolve a ThetaState with deterministic update plus optional noise proxy."""
    if dt <= 0:
        raise ValueError("dt must be positive")

    increment = np.asarray(deterministic_rhs(state))
    use_kernel = kernel if kernel is not None else AdditiveGaussianStochasticKernel()
    rng = np.random.default_rng(seed)
    return use_kernel(
        state=state,
        dt=dt,
        deterministic_increment=increment,
        noise_amplitude=noise_amplitude,
        rng=rng,
    )
