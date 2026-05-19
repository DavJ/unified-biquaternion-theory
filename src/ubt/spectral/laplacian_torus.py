# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
"""Laplacian eigenmodes and heat-kernel scaffold for torus sectors in UBT."""

from __future__ import annotations

import math
from itertools import product
from typing import Generator

import numpy as np
from scipy.integrate import quad

try:
    import mpmath
except ImportError:  # pragma: no cover - optional runtime dependency
    mpmath = None


def _validate_positive(value: float, name: str) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def torus_eigenvalues(d: int, k_max: int, L: float = 1.0) -> tuple[np.ndarray, np.ndarray]:
    """Eigenvalues and degeneracies of -Δ on T^d with period L."""
    if d < 1:
        raise ValueError("d must be >= 1")
    if k_max < 0:
        raise ValueError("k_max must be >= 0")
    _validate_positive(L, "L")

    ranges = [range(-k_max, k_max + 1) for _ in range(d)]
    k_vectors = np.array(list(product(*ranges)), dtype=int)
    k_squared = np.sum(k_vectors**2, axis=1, dtype=np.int64)
    eigenvalues = (2.0 * np.pi / L) ** 2 * k_squared
    unique_vals, counts = np.unique(eigenvalues, return_counts=True)
    return unique_vals, counts


def torus_spectrum_generator(d: int, k_max: int, L: float = 1.0) -> Generator[tuple[float, int], None, None]:
    """Yield sorted (eigenvalue, degeneracy) pairs for T^d."""
    eigenvalues, degeneracies = torus_eigenvalues(d=d, k_max=k_max, L=L)
    for eigenvalue, degeneracy in zip(eigenvalues, degeneracies):
        yield float(eigenvalue), int(degeneracy)


def mode_count_below_energy(d: int, Lambda: float, L: float = 1.0) -> int:
    """Count torus modes with eigenvalue <= Lambda."""
    if Lambda < 0:
        raise ValueError("Lambda must be non-negative")
    _validate_positive(L, "L")
    k_max_cutoff = int(np.sqrt(Lambda) * L / (2.0 * np.pi)) + 1
    eigenvalues, degeneracies = torus_eigenvalues(d=d, k_max=k_max_cutoff, L=L)
    return int(np.sum(degeneracies[eigenvalues <= Lambda]))


def get_lowest_nonzero_eigenvalue(d: int, L: float = 1.0) -> float:
    """Return the spectral gap on T^d."""
    if d < 1:
        raise ValueError("d must be >= 1")
    _validate_positive(L, "L")
    return float((2.0 * np.pi / L) ** 2)


def torus_laplacian_spectrum(R: float = 1.0, n_max: int = 10) -> np.ndarray:
    """
    Eigenvalues of -nabla^2 on T^3 = S^1 x S^1 x S^1.
    lambda_{n1,n2,n3} = (n1^2 + n2^2 + n3^2) / R^2
    """
    _validate_positive(R, "R")
    if n_max < 0:
        raise ValueError("n_max must be >= 0")
    eigs: set[float] = set()
    for n1 in range(-n_max, n_max + 1):
        for n2 in range(-n_max, n_max + 1):
            for n3 in range(-n_max, n_max + 1):
                eigs.add((n1**2 + n2**2 + n3**2) / (R**2))
    return np.array(sorted(eigs), dtype=float)


def heat_kernel_torus(t: float, R: float = 1.0, n_max: int = 20) -> float:
    """
    K_{T^3}(t) = [theta3(0|it/piR^2)]^3
    Numerical approximation via truncated sum.
    """
    _validate_positive(t, "t")
    _validate_positive(R, "R")
    if n_max < 0:
        raise ValueError("n_max must be >= 0")
    total = 0.0
    for n in range(-n_max, n_max + 1):
        total += math.exp(-t * (n**2) / (R**2))
    return float(total**3)


def heat_kernel_exact(t: float, R: float = 1.0) -> float:
    """
    K_{T^3}(t) = [theta3(0|it/piR^2)]^3 — exact via Jacobi theta.
    Falls back to a high-cutoff numerical sum if mpmath is unavailable.
    """
    _validate_positive(t, "t")
    _validate_positive(R, "R")
    if mpmath is None:
        n_max = max(100, int(30 + 20 / math.sqrt(t)))
        return heat_kernel_torus(t=t, R=R, n_max=n_max)

    mpmath.mp.dps = 30
    tau = mpmath.mpc(0, t / (math.pi * R**2))
    q = mpmath.exp(1j * math.pi * tau)
    th3 = float(mpmath.re(mpmath.jtheta(3, 0, q)))
    return th3**3


def zeta_prime_0_torus(R: float = 1.0, n_max: int = 50) -> float:
    """
    zeta'_{-nabla^2}(0) na T^3 přes Mellin transformaci K_{T^3}(t).
    Numerická aproximace.
    """
    _validate_positive(R, "R")
    if n_max < 0:
        raise ValueError("n_max must be >= 0")

    def integrand(t: float, s: float) -> float:
        k_t = heat_kernel_exact(t=t, R=R) if mpmath is not None else heat_kernel_torus(t=t, R=R, n_max=n_max)
        return float((t ** (s - 1)) * k_t)

    s0 = 0.001
    result_low, _ = quad(lambda t: integrand(t, s0), 0.01, 1.0, limit=200)
    result_high, _ = quad(lambda t: integrand(t, s0), 1.0, 100.0, limit=200)
    return float(-(result_low + result_high))
