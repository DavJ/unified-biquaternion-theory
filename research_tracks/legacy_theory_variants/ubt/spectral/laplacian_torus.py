# Copyright (c) 2026 David Jaroš (UBT Framework)
# SPDX-License-Identifier: MIT

"""
Laplacian Spectrum on Torus

Computes eigenvalues and eigenmodes of the Laplacian operator on a d-dimensional torus.
"""

import math
import numpy as np
from scipy.integrate import quad
from typing import Tuple

try:
    import mpmath
except ImportError:  # pragma: no cover - optional runtime dependency
    mpmath = None


def torus_eigenvalues(d: int, k_max: int, L: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute eigenvalues of Laplacian on d-dimensional torus.
    
    For a flat torus T^d with period L, eigenvalues are:
        λ_k = (2π/L)² |k|²
    
    where k ∈ Z^d is the mode number vector.
    
    Args:
        d: Dimension of torus
        k_max: Maximum |k| to include in each direction
        L: Period/radius of torus (default 1.0 for normalized)
        
    Returns:
        eigenvalues: Array of eigenvalues λ_k
        degeneracies: Array of degeneracy for each unique eigenvalue
    """
    # Generate all mode vectors k in [-k_max, k_max]^d
    if d == 1:
        k_vectors = np.arange(-k_max, k_max + 1).reshape(-1, 1)
    elif d == 2:
        k1, k2 = np.meshgrid(range(-k_max, k_max + 1), range(-k_max, k_max + 1))
        k_vectors = np.column_stack([k1.ravel(), k2.ravel()])
    elif d == 3:
        k1 = np.arange(-k_max, k_max + 1)
        k_grid = np.array(np.meshgrid(k1, k1, k1)).T.reshape(-1, 3)
        k_vectors = k_grid
    else:
        # General d dimensions
        ranges = [range(-k_max, k_max + 1) for _ in range(d)]
        grid = np.array(np.meshgrid(*ranges, indexing='ij'))
        k_vectors = grid.reshape(d, -1).T
    
    # Compute eigenvalues: λ_k = (2π/L)² |k|²
    k_squared = np.sum(k_vectors**2, axis=1)
    eigenvalues = (2 * np.pi / L)**2 * k_squared
    
    # Count degeneracies (number of k vectors giving same eigenvalue)
    unique_vals, inverse, counts = np.unique(
        eigenvalues, return_inverse=True, return_counts=True
    )
    
    return unique_vals, counts


def torus_spectrum_generator(d: int, k_max: int, L: float = 1.0):
    """
    Generator yielding (eigenvalue, degeneracy) pairs sorted by eigenvalue.
    
    Args:
        d: Dimension of torus
        k_max: Maximum mode number
        L: Torus period
        
    Yields:
        (lambda_k, degeneracy): Eigenvalue and its degeneracy
    """
    eigenvalues, degeneracies = torus_eigenvalues(d, k_max, L)
    
    # Sort by eigenvalue
    sorted_indices = np.argsort(eigenvalues)
    
    for idx in sorted_indices:
        yield eigenvalues[idx], degeneracies[idx]


def mode_count_below_energy(d: int, Lambda: float, L: float = 1.0) -> int:
    """
    Count number of modes with eigenvalue λ_k ≤ Λ.
    
    This gives the Weyl asymptotic formula for large Λ:
        N(Λ) ~ (L/(2π))^d × V_d × Λ^{d/2}
    
    where V_d is the volume of unit d-sphere.
    
    Args:
        d: Dimension
        Lambda: Energy cutoff
        L: Torus period
        
    Returns:
        Number of modes below Lambda
    """
    # Maximum |k| such that (2π/L)² |k|² ≤ Λ
    k_max_cutoff = int(np.sqrt(Lambda) * L / (2 * np.pi)) + 1
    
    eigenvalues, degeneracies = torus_eigenvalues(d, k_max_cutoff, L)
    
    mask = eigenvalues <= Lambda
    return int(np.sum(degeneracies[mask]))


def get_lowest_nonzero_eigenvalue(d: int, L: float = 1.0) -> float:
    """
    Get the lowest non-zero eigenvalue (spectral gap).
    
    For a torus, this corresponds to k = (±1, 0, ..., 0) or permutations.
    
    Args:
        d: Dimension
        L: Torus period
        
    Returns:
        Lowest non-zero eigenvalue
    """
    return (2 * np.pi / L)**2


def torus_laplacian_spectrum(R: float = 1.0, n_max: int = 10) -> np.ndarray:
    """
    Eigenvalues of -nabla^2 on T^3 = S^1 x S^1 x S^1.
    lambda_{n1,n2,n3} = (n1^2 + n2^2 + n3^2) / R^2
    """
    if R <= 0:
        raise ValueError("R must be positive")
    if n_max < 0:
        raise ValueError("n_max must be >= 0")
    eigs = []
    for n1 in range(-n_max, n_max + 1):
        for n2 in range(-n_max, n_max + 1):
            for n3 in range(-n_max, n_max + 1):
                eigs.append((n1**2 + n2**2 + n3**2) / R**2)
    return np.array(sorted(set(eigs)), dtype=float)


def heat_kernel_torus(t: float, R: float = 1.0, n_max: int = 20) -> float:
    """
    K_{T^3}(t) = [theta3(0|it/piR^2)]^3
    Numerical approximation via truncated sum.
    """
    if t <= 0:
        raise ValueError("t must be positive")
    if R <= 0:
        raise ValueError("R must be positive")
    if n_max < 0:
        raise ValueError("n_max must be >= 0")

    total = 0.0
    for n in range(-n_max, n_max + 1):
        total += math.exp(-t * n**2 / R**2)
    return float(total**3)


def heat_kernel_exact(t: float, R: float = 1.0) -> float:
    """
    K_{T^3}(t) = [theta3(0|it/piR^2)]^3 — exact via Jacobi theta.
    Falls back to high-cutoff numerical approximation when mpmath is unavailable.
    """
    if t <= 0:
        raise ValueError("t must be positive")
    if R <= 0:
        raise ValueError("R must be positive")

    if mpmath is None:
        n_max = max(100, int(30 + 20 / math.sqrt(t)))
        return heat_kernel_torus(t=t, R=R, n_max=n_max)

    mpmath.mp.dps = 30
    tau = mpmath.mpc(0, t / (math.pi * R**2))
    th3 = float(mpmath.re(mpmath.jtheta(3, 0, mpmath.exp(1j * math.pi * tau))))
    return th3**3


def zeta_prime_0_torus(R: float = 1.0, n_max: int = 50) -> float:
    """
    zeta'_{-nabla^2}(0) na T^3 přes Mellin transformaci K_{T^3}(t).
    Numerická aproximace.
    """
    if R <= 0:
        raise ValueError("R must be positive")
    if n_max < 0:
        raise ValueError("n_max must be >= 0")

    def integrand(t: float, s: float) -> float:
        k_t = heat_kernel_exact(t=t, R=R) if mpmath is not None else heat_kernel_torus(t=t, R=R, n_max=n_max)
        return float(t ** (s - 1) * k_t)

    s0 = 0.001
    result_low, _ = quad(lambda t: integrand(t, s0), 0.01, 1.0, limit=200)
    result_high, _ = quad(lambda t: integrand(t, s0), 1.0, 100.0, limit=200)
    return float(-(result_low + result_high))
