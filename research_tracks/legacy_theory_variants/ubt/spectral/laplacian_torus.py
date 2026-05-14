# Copyright (c) 2026 David Jaroš (UBT Framework)
# SPDX-License-Identifier: MIT

"""
Laplacian Spectrum on Torus

Computes eigenvalues and eigenmodes of the Laplacian operator on a d-dimensional torus.
"""

import numpy as np
from typing import List, Tuple, Optional


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
