#!/usr/bin/env python3
"""
interference_functional.py

Defines interference functional I(n) for discrete mode n to measure:
- Aliasing effects
- Harmonic overlaps
- Spectral redundancy

This module implements the core mathematical framework for evaluating
mode stability without modifying core UBT theory.

Usage:
    python interference_functional.py --range 100 200
    python interference_functional.py --range 100 200 --output results/interference.csv

Author: UBT Research Team
License: See repository LICENSE.md
"""

import argparse
import csv
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple


def is_prime(n: int) -> bool:
    """
    Check if n is prime using trial division.
    
    Args:
        n: Integer to test
        
    Returns:
        True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def generate_harmonic_spectrum(n_max: int = 300, fundamental: float = 1.0) -> np.ndarray:
    """
    Generate a synthetic harmonic spectrum for testing.
    
    In UBT, this would come from the biquaternionic field structure,
    but here we use a generic harmonic series for validation.
    
    Args:
        n_max: Maximum mode number
        fundamental: Fundamental frequency
        
    Returns:
        Array of spectral amplitudes
    """
    spectrum = np.zeros(n_max + 1)
    
    # Generic harmonic decay
    for n in range(1, n_max + 1):
        # Amplitude decays as 1/n with some oscillation
        spectrum[n] = (1.0 / n) * (1 + 0.1 * np.sin(n / 10))
    
    return spectrum


def compute_aliasing_metric(n: int, spectrum: np.ndarray, n_max: int = None) -> float:
    """
    Compute aliasing metric for mode n.
    
    Aliasing occurs when:
    - Mode n interferes with its harmonics (2n, 3n, ...)
    - Mode n interferes with its sub-harmonics (n/2, n/3, ...)
    
    Args:
        n: Mode number to evaluate
        spectrum: Spectral amplitude array
        n_max: Maximum mode to consider (default: len(spectrum)-1)
        
    Returns:
        Aliasing metric (higher = more aliasing/interference)
    """
    if n_max is None:
        n_max = len(spectrum) - 1
    
    aliasing = 0.0
    
    # Harmonic interference (n with 2n, 3n, ...)
    for k in range(2, 11):  # Check first 10 harmonics
        harmonic = k * n
        if harmonic <= n_max:
            # Interference proportional to product of amplitudes
            aliasing += spectrum[n] * spectrum[harmonic] / k
    
    # Sub-harmonic interference (n with n/2, n/3, ...)
    for k in range(2, 11):
        if n % k == 0:
            subharmonic = n // k
            if subharmonic > 0:
                aliasing += spectrum[n] * spectrum[subharmonic] / k
    
    return aliasing


def compute_harmonic_overlap(n: int, spectrum: np.ndarray = None) -> float:
    """
    Compute harmonic overlap metric for mode n.
    
    This measures how many divisors mode n has (composite numbers
    have more divisors, leading to more overlaps).
    
    Args:
        n: Mode number to evaluate
        spectrum: Spectral amplitude array (optional, for weighting)
        
    Returns:
        Harmonic overlap metric (higher = more overlaps)
    """
    if n < 2:
        return 0.0
    
    # Count divisors
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    
    # Harmonic overlap increases with number of divisors
    # Prime numbers have only 2 divisors (1 and n)
    overlap = len(divisors) - 2  # Subtract 1 and n
    
    # Weight by inverse of divisor values (smaller divisors = stronger overlap)
    if overlap > 0:
        overlap += sum(1.0 / d for d in divisors if d > 1 and d < n)
    
    return overlap


def compute_interference_functional(n: int, spectrum: np.ndarray, 
                                    alpha: float = 1.0, beta: float = 1.0) -> float:
    """
    Compute total interference functional I(n).
    
    I(n) = α·aliasing(n) + β·overlap(n)
    
    Lower values indicate more stable modes with less interference.
    
    Args:
        n: Mode number to evaluate
        spectrum: Spectral amplitude array
        alpha: Weight for aliasing metric
        beta: Weight for harmonic overlap
        
    Returns:
        Total interference functional I(n)
    """
    aliasing = compute_aliasing_metric(n, spectrum)
    overlap = compute_harmonic_overlap(n, spectrum)
    
    return alpha * aliasing + beta * overlap


def evaluate_range(n_min: int = 100, n_max: int = 200, 
                   output_file: str = None) -> Dict[int, Dict[str, float]]:
    """
    Evaluate interference functional over a range of modes.
    
    Args:
        n_min: Minimum mode number
        n_max: Maximum mode number
        output_file: Optional CSV output file path
        
    Returns:
        Dictionary mapping mode n to metrics
    """
    print(f"Evaluating interference functional for n ∈ [{n_min}, {n_max}]")
    
    # Generate spectrum
    spectrum = generate_harmonic_spectrum(n_max + 50)
    
    results = {}
    
    for n in range(n_min, n_max + 1):
        aliasing = compute_aliasing_metric(n, spectrum)
        overlap = compute_harmonic_overlap(n, spectrum)
        I_n = compute_interference_functional(n, spectrum)
        prime = is_prime(n)
        
        results[n] = {
            'n': n,
            'aliasing': aliasing,
            'overlap': overlap,
            'I(n)': I_n,
            'is_prime': prime
        }
    
    # Write to CSV if requested
    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', newline='') as f:
            fieldnames = ['n', 'aliasing', 'overlap', 'I(n)', 'is_prime']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for data in results.values():
                writer.writerow(data)
        
        print(f"Results written to {output_path}")
    
    return results


def print_summary(results: Dict[int, Dict[str, float]]) -> None:
    """
    Print summary statistics of results.
    
    Args:
        results: Dictionary of results from evaluate_range
    """
    print("\n" + "=" * 70)
    print("INTERFERENCE FUNCTIONAL SUMMARY")
    print("=" * 70)
    
    # Separate primes and composites
    primes = {n: data for n, data in results.items() if data['is_prime']}
    composites = {n: data for n, data in results.items() if not data['is_prime']}
    
    print(f"\nTotal modes evaluated: {len(results)}")
    print(f"Primes: {len(primes)}")
    print(f"Composites: {len(composites)}")
    
    # Find modes with lowest I(n)
    sorted_results = sorted(results.items(), key=lambda x: x[1]['I(n)'])
    
    print("\n--- Top 10 Most Stable Modes (Lowest I(n)) ---")
    for i, (n, data) in enumerate(sorted_results[:10]):
        prime_str = "PRIME" if data['is_prime'] else "composite"
        print(f"{i+1}. n={n:3d} ({prime_str:9s}): I(n)={data['I(n)']:.6f}, "
              f"aliasing={data['aliasing']:.6f}, overlap={data['overlap']:.2f}")
    
    # Statistics for primes vs composites
    if primes and composites:
        prime_I = [data['I(n)'] for data in primes.values()]
        composite_I = [data['I(n)'] for data in composites.values()]
        
        print(f"\n--- Prime vs Composite Statistics ---")
        print(f"Primes - Mean I(n): {np.mean(prime_I):.6f}, Std: {np.std(prime_I):.6f}")
        print(f"Composites - Mean I(n): {np.mean(composite_I):.6f}, Std: {np.std(composite_I):.6f}")
        print(f"Difference (Composite - Prime): {np.mean(composite_I) - np.mean(prime_I):.6f}")
        
        # Check if 137 and 139 are in range
        if 137 in results:
            print(f"\n--- Special Case: n=137 ---")
            data_137 = results[137]
            print(f"n=137 (PRIME): I(n)={data_137['I(n)']:.6f}")
            rank_137 = next(i for i, (n, _) in enumerate(sorted_results) if n == 137) + 1
            print(f"Rank: {rank_137} out of {len(results)}")
            
        if 139 in results:
            print(f"\n--- Special Case: n=139 ---")
            data_139 = results[139]
            print(f"n=139 (PRIME): I(n)={data_139['I(n)']:.6f}")
            rank_139 = next(i for i, (n, _) in enumerate(sorted_results) if n == 139) + 1
            print(f"Rank: {rank_139} out of {len(results)}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Evaluate interference functional for mode selection'
    )
    parser.add_argument('--range', nargs=2, type=int, default=[100, 200],
                        metavar=('MIN', 'MAX'),
                        help='Range of modes to evaluate (default: 100 200)')
    parser.add_argument('--output', type=str, default=None,
                        help='Output CSV file path')
    
    args = parser.parse_args()
    
    n_min, n_max = args.range
    
    # Evaluate
    results = evaluate_range(n_min, n_max, output_file=args.output)
    
    # Print summary
    print_summary(results)


if __name__ == '__main__':
    main()
