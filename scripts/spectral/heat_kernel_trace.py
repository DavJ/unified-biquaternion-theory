#!/usr/bin/env python3
# Copyright (c) 2026 David Jaroš (UBT Framework)
# SPDX-License-Identifier: MIT

"""
Heat Kernel Trace Calculator

Computes Tr exp(-τΔ) using spectral decomposition on a torus.
"""

import numpy as np
import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from ubt.spectral.laplacian_torus import torus_eigenvalues


def heat_kernel_trace_spectral(tau: float, d: int, k_max: int, L: float = 1.0) -> float:
    """
    Compute heat kernel trace using spectral decomposition.
    
    K(τ) = Tr exp(-τΔ) = Σ_{k} exp(-τλ_k)
    
    where the sum includes degeneracy.
    
    Args:
        tau: Heat kernel time parameter
        d: Dimension of torus
        k_max: Maximum mode number for truncation
        L: Torus period
        
    Returns:
        Heat kernel trace value
    """
    eigenvalues, degeneracies = torus_eigenvalues(d, k_max, L)
    
    # K(τ) = Σ g_k exp(-τλ_k) where g_k is degeneracy
    trace = np.sum(degeneracies * np.exp(-tau * eigenvalues))
    
    return trace


def heat_kernel_trace_exact_1d(tau: float, L: float = 1.0) -> float:
    """
    Exact heat kernel trace for 1D torus (infinite sum).
    
    K(τ) = Σ_{n=-∞}^{∞} exp(-τ(2πn/L)²)
          = θ₃(0, q) where q = exp(-τ(2π/L)²)
    
    For L=1, this is the Jacobi theta function θ₃(0, exp(-4π²τ)).
    
    Args:
        tau: Heat kernel time
        L: Period
        
    Returns:
        Exact trace value
    """
    q = np.exp(-tau * (2 * np.pi / L)**2)
    
    # Compute theta_3(0, q) = 1 + 2 Σ_{n=1}^∞ q^{n²}
    # Truncate at reasonable n
    if 0 < q < 1:
        # Estimate n_max from exponential decay
        log_q = np.log(q)
        n_max = max(10, int(np.sqrt(-np.log(1e-15) / abs(log_q))) + 1)
    else:
        n_max = 100
    
    theta = 1.0
    for n in range(1, n_max + 1):
        term = 2 * q**(n**2)
        theta += term
        if abs(term) < 1e-15:
            break
    
    return theta


def main():
    """Demonstrate heat kernel trace calculation."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Heat kernel trace calculator')
    parser.add_argument('--tau', type=float, default=0.1, help='Heat kernel time')
    parser.add_argument('--dim', type=int, default=2, help='Torus dimension')
    parser.add_argument('--kmax', type=int, default=10, help='Maximum mode number')
    parser.add_argument('--L', type=float, default=1.0, help='Torus period')
    
    args = parser.parse_args()
    
    print(f"Heat Kernel Trace on {args.dim}D Torus")
    print(f"=" * 50)
    print(f"Parameters:")
    print(f"  τ = {args.tau}")
    print(f"  d = {args.dim}")
    print(f"  k_max = {args.kmax}")
    print(f"  L = {args.L}")
    print()
    
    # Compute trace
    trace = heat_kernel_trace_spectral(args.tau, args.dim, args.kmax, args.L)
    print(f"K(τ) = Tr exp(-τΔ) = {trace:.6f}")
    print()
    
    # For 1D, compare to exact
    if args.dim == 1:
        exact = heat_kernel_trace_exact_1d(args.tau, args.L)
        print(f"Exact (theta function): {exact:.6f}")
        print(f"Relative error: {abs(trace - exact) / exact:.2e}")
    
    # Show convergence
    if args.kmax >= 5:
        print(f"\nConvergence check (varying k_max):")
        print(f"{'k_max':<10} {'K(τ)':<15} {'Relative change':<15}")
        print("-" * 40)
        
        prev_trace = None
        for k in [args.kmax // 2, 3 * args.kmax // 4, args.kmax]:
            trace_k = heat_kernel_trace_spectral(args.tau, args.dim, k, args.L)
            
            if prev_trace is not None:
                rel_change = abs(trace_k - prev_trace) / prev_trace
                print(f"{k:<10} {trace_k:<15.6f} {rel_change:<15.2e}")
            else:
                print(f"{k:<10} {trace_k:<15.6f} {'—':<15}")
            
            prev_trace = trace_k


if __name__ == '__main__':
    main()
