#!/usr/bin/env python3
# Copyright (c) 2026 David Jaroš (UBT Framework)
# SPDX-License-Identifier: MIT

"""
Poisson Duality Demonstration

Verifies the Poisson summation / theta function duality:
    Σ_{n∈Z^d} exp(-π|n|²/τ) = τ^{-d/2} Σ_{k∈Z^d} exp(-πτ|k|²)

Shows equivalence between winding (n-space) and spectral (k-space) formulations.
"""

import numpy as np
import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from ubt.spectral.laplacian_torus import torus_eigenvalues


def winding_sum(tau: float, d: int, n_max: int) -> float:
    """
    Winding number sum (position space).
    
    W(τ) = Σ_{n∈Z^d} exp(-π|n|²/τ)
    
    Args:
        tau: Parameter
        d: Dimension
        n_max: Truncation (sum from -n_max to n_max in each direction)
        
    Returns:
        Sum value
    """
    # Generate all n vectors
    if d == 1:
        n_vectors = np.arange(-n_max, n_max + 1).reshape(-1, 1)
    elif d == 2:
        n1, n2 = np.meshgrid(range(-n_max, n_max + 1), range(-n_max, n_max + 1))
        n_vectors = np.column_stack([n1.ravel(), n2.ravel()])
    elif d == 3:
        n1 = np.arange(-n_max, n_max + 1)
        n_grid = np.array(np.meshgrid(n1, n1, n1)).T.reshape(-1, 3)
        n_vectors = n_grid
    else:
        ranges = [range(-n_max, n_max + 1) for _ in range(d)]
        grid = np.array(np.meshgrid(*ranges, indexing='ij'))
        n_vectors = grid.reshape(d, -1).T
    
    # Compute |n|²
    n_squared = np.sum(n_vectors**2, axis=1)
    
    # Sum exp(-π|n|²/τ)
    result = np.sum(np.exp(-np.pi * n_squared / tau))
    
    return result


def spectral_sum(tau: float, d: int, k_max: int) -> float:
    """
    Spectral / momentum sum (k-space).
    
    S(τ) = Σ_{k∈Z^d} exp(-πτ|k|²)
    
    Args:
        tau: Parameter
        d: Dimension
        k_max: Truncation
        
    Returns:
        Sum value (normalized by τ^{-d/2} for duality)
    """
    # Generate all k vectors
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
        ranges = [range(-k_max, k_max + 1) for _ in range(d)]
        grid = np.array(np.meshgrid(*ranges, indexing='ij'))
        k_vectors = grid.reshape(d, -1).T
    
    # Compute |k|²
    k_squared = np.sum(k_vectors**2, axis=1)
    
    # Sum exp(-πτ|k|²)
    raw_sum = np.sum(np.exp(-np.pi * tau * k_squared))
    
    # Apply Poisson prefactor: τ^{-d/2}
    normalized_sum = tau**(-d / 2) * raw_sum
    
    return normalized_sum


def main():
    """Demonstrate Poisson duality."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Poisson duality demonstration')
    parser.add_argument('--dim', type=int, default=2, help='Dimension')
    parser.add_argument('--cutoff', type=int, default=10, help='Cutoff for sums')
    parser.add_argument('--tau-min', type=float, default=0.1, help='Min tau value')
    parser.add_argument('--tau-max', type=float, default=2.0, help='Max tau value')
    parser.add_argument('--n-points', type=int, default=10, help='Number of tau points')
    
    args = parser.parse_args()
    
    print("=" * 80)
    print("POISSON SUMMATION DUALITY DEMONSTRATION")
    print("=" * 80)
    print()
    print(f"Dimension: d = {args.dim}")
    print(f"Cutoff: n_max = k_max = {args.cutoff}")
    print(f"Tau range: [{args.tau_min}, {args.tau_max}]")
    print()
    print("Verifying:")
    print("  Winding sum:  W(τ) = Σ_n exp(-π|n|²/τ)")
    print("  Spectral sum: S(τ) = τ^{-d/2} Σ_k exp(-πτ|k|²)")
    print("  Duality: W(τ) ≈ S(τ) for large cutoffs")
    print()
    
    # Generate tau values
    tau_values = np.linspace(args.tau_min, args.tau_max, args.n_points)
    
    # Table header
    print(f"{'τ':<10} {'Winding W(τ)':<15} {'Spectral S(τ)':<15} {'Ratio W/S':<12} {'Rel. Diff':<12}")
    print("-" * 80)
    
    max_rel_diff = 0.0
    
    for tau in tau_values:
        winding = winding_sum(tau, args.dim, args.cutoff)
        spectral = spectral_sum(tau, args.dim, args.cutoff)
        
        ratio = winding / spectral if spectral > 0 else float('nan')
        rel_diff = abs(winding - spectral) / spectral if spectral > 0 else float('nan')
        
        max_rel_diff = max(max_rel_diff, rel_diff)
        
        print(f"{tau:<10.4f} {winding:<15.6f} {spectral:<15.6f} {ratio:<12.6f} {rel_diff:<12.2e}")
    
    print()
    print(f"Maximum relative difference: {max_rel_diff:.2e}")
    
    if max_rel_diff < 1e-2:
        print("✓ DUALITY VERIFIED (difference < 1%)")
    elif max_rel_diff < 1e-1:
        print("~ DUALITY APPROXIMATELY VERIFIED (difference < 10%)")
    else:
        print("✗ DUALITY NOT VERIFIED (increase cutoff for better convergence)")
    
    print()
    print("Interpretation:")
    print("  Small differences indicate Poisson summation duality holds numerically.")
    print("  Winding (n-space) and spectral (k-space) are dual representations.")


if __name__ == '__main__':
    main()
