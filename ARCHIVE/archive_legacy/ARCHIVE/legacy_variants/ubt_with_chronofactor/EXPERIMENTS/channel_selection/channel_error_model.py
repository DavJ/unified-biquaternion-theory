#!/usr/bin/env python3
"""
channel_error_model.py

Model Layer 2 as an information channel with mode-dependent error rate.
Simulates Reed-Solomon style redundancy and evaluates stability regions.

Usage:
    python channel_error_model.py --lambda 0.5 --range 100 200
    python channel_error_model.py --lambda 0.5 --output results/channel_model/

Author: UBT Research Team
License: See repository LICENSE.md
"""

import argparse
import csv
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Optional

from interference_functional import (
    evaluate_range, is_prime, compute_interference_functional,
    generate_harmonic_spectrum
)

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("Warning: matplotlib not available, plots will be skipped")


def compute_error_rate(n: int, spectrum: np.ndarray, 
                       base_error: float = 0.01) -> float:
    """
    Compute error rate for mode n based on aliasing.
    
    Error rate increases with aliasing/interference, as modes with
    more overlaps are harder to distinguish.
    
    Args:
        n: Mode number
        spectrum: Spectral amplitude array
        base_error: Baseline error rate
        
    Returns:
        Error rate ∈ [0, 1]
    """
    from interference_functional import compute_aliasing_metric
    
    # Error rate proportional to aliasing
    aliasing = compute_aliasing_metric(n, spectrum)
    
    # Normalize to [0, 1] range
    # Use logistic function to map aliasing to error rate
    error_rate = base_error + (1 - base_error) / (1 + np.exp(-10 * (aliasing - 0.01)))
    
    return min(error_rate, 0.99)  # Cap at 99%


def compute_redundancy_cost(n: int, error_rate: float, 
                            target_reliability: float = 0.999) -> float:
    """
    Compute redundancy cost for achieving target reliability.
    
    Uses simplified Reed-Solomon coding model:
    k/n = R (code rate) where k = message symbols, n = total symbols
    
    Args:
        n: Mode number
        error_rate: Channel error rate
        target_reliability: Target reliability (e.g., 0.999 = 99.9%)
        
    Returns:
        Redundancy overhead (higher = more costly)
    """
    if error_rate >= 1.0:
        return float('inf')
    
    # Number of redundant symbols needed
    # Approximate: need t correction symbols where (1-p)^t >= target_reliability
    if error_rate > 0:
        t = int(np.ceil(np.log(1 - target_reliability) / np.log(error_rate)))
    else:
        t = 0
    
    # Redundancy overhead as fraction
    redundancy = t / max(n, 1)
    
    return redundancy


def compute_cost_functional(n: int, spectrum: np.ndarray, 
                            lambda_param: float = 0.5,
                            alpha: float = 1.0, beta: float = 1.0) -> float:
    """
    Compute total cost functional F(n).
    
    F(n) = interference(n) + λ·error_rate(n)
    
    Lower values indicate better modes (stable with low error).
    
    Args:
        n: Mode number
        spectrum: Spectral amplitude array
        lambda_param: Weight for error rate term
        alpha: Weight for aliasing in interference
        beta: Weight for overlap in interference
        
    Returns:
        Total cost F(n)
    """
    # Interference term
    I_n = compute_interference_functional(n, spectrum, alpha, beta)
    
    # Error rate term
    error = compute_error_rate(n, spectrum)
    
    # Total cost
    F_n = I_n + lambda_param * error
    
    return F_n


def evaluate_channel_model(n_min: int = 100, n_max: int = 200,
                          lambda_param: float = 0.5,
                          output_dir: Optional[str] = None) -> Dict[int, Dict[str, float]]:
    """
    Evaluate channel error model over mode range.
    
    Args:
        n_min: Minimum mode number
        n_max: Maximum mode number
        lambda_param: Weight for error rate in cost functional
        output_dir: Optional output directory
        
    Returns:
        Dictionary of results
    """
    print("=" * 70)
    print("CHANNEL ERROR MODEL ANALYSIS")
    print("=" * 70)
    print(f"Range: n ∈ [{n_min}, {n_max}]")
    print(f"Lambda parameter: {lambda_param}\n")
    
    # Generate spectrum
    spectrum = generate_harmonic_spectrum(n_max + 50)
    
    results = {}
    
    for n in range(n_min, n_max + 1):
        # Compute metrics
        I_n = compute_interference_functional(n, spectrum)
        error = compute_error_rate(n, spectrum)
        redundancy = compute_redundancy_cost(n, error)
        F_n = compute_cost_functional(n, spectrum, lambda_param)
        prime = is_prime(n)
        
        results[n] = {
            'n': n,
            'I(n)': I_n,
            'error_rate': error,
            'redundancy': redundancy,
            'F(n)': F_n,
            'is_prime': prime
        }
    
    # Save results
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        csv_path = output_path / f'channel_model_lambda{lambda_param:.2f}.csv'
        with open(csv_path, 'w', newline='') as f:
            fieldnames = ['n', 'I(n)', 'error_rate', 'redundancy', 'F(n)', 'is_prime']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for data in results.values():
                writer.writerow(data)
        
        print(f"Results saved to {csv_path}")
    
    return results


def find_stability_regions(results: Dict[int, Dict[str, float]], 
                           threshold_percentile: float = 25) -> List[Tuple[int, float]]:
    """
    Identify stability regions (local minima of F(n)).
    
    Args:
        results: Results dictionary
        threshold_percentile: Percentile threshold for defining stable regions
        
    Returns:
        List of (n, F(n)) for stable modes
    """
    # Extract F(n) values
    F_values = [(n, data['F(n)']) for n, data in results.items()]
    F_values.sort(key=lambda x: x[1])
    
    # Threshold for stability
    threshold = np.percentile([f for _, f in F_values], threshold_percentile)
    
    stable_modes = [(n, f) for n, f in F_values if f <= threshold]
    
    return stable_modes


def plot_cost_functional(results: Dict[int, Dict[str, float]],
                         lambda_param: float,
                         output_file: Optional[str] = None) -> None:
    """
    Plot cost functional F(n) landscape.
    
    Args:
        results: Results dictionary
        lambda_param: Lambda parameter value
        output_file: Output plot path
    """
    if not HAS_MATPLOTLIB:
        print("Skipping plot (matplotlib not available)")
        return
    
    # Separate primes and composites
    primes = {n: data for n, data in results.items() if data['is_prime']}
    composites = {n: data for n, data in results.items() if not data['is_prime']}
    
    prime_n = sorted(primes.keys())
    prime_F = [primes[n]['F(n)'] for n in prime_n]
    
    composite_n = sorted(composites.keys())
    composite_F = [composites[n]['F(n)'] for n in composite_n]
    
    # Create plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Plot 1: F(n) landscape
    ax1.scatter(composite_n, composite_F, c='lightgray', s=20, 
                label='Composite', alpha=0.6)
    ax1.scatter(prime_n, prime_F, c='blue', s=40, 
                label='Prime', alpha=0.7)
    
    # Highlight 137 and 139
    if 137 in results:
        ax1.scatter([137], [results[137]['F(n)']], c='red', s=100, 
                    marker='s', label='n=137', zorder=5)
        ax1.annotate('137', (137, results[137]['F(n)']), 
                     xytext=(5, 5), textcoords='offset points')
    
    if 139 in results:
        ax1.scatter([139], [results[139]['F(n)']], c='orange', s=100, 
                    marker='^', label='n=139', zorder=5)
        ax1.annotate('139', (139, results[139]['F(n)']), 
                     xytext=(5, 5), textcoords='offset points')
    
    ax1.set_xlabel('Mode number n', fontsize=12)
    ax1.set_ylabel(f'Cost functional F(n) (λ={lambda_param})', fontsize=12)
    ax1.set_title('Channel Error Model: Cost Functional Landscape', fontsize=13)
    ax1.legend(loc='best')
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Error rate vs n
    all_n = sorted(results.keys())
    error_rates = [results[n]['error_rate'] for n in all_n]
    
    ax2.plot(all_n, error_rates, 'o-', markersize=3, alpha=0.6)
    ax2.set_xlabel('Mode number n', fontsize=12)
    ax2.set_ylabel('Error rate', fontsize=12)
    ax2.set_title('Channel Error Rate vs Mode Number', fontsize=13)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=150)
        print(f"Plot saved to {output_path}")
    else:
        plt.savefig(f'cost_functional_lambda{lambda_param:.2f}.png', dpi=150)
    
    plt.close()


def print_analysis_summary(results: Dict[int, Dict[str, float]], 
                          lambda_param: float) -> None:
    """
    Print summary of channel model analysis.
    
    Args:
        results: Results dictionary
        lambda_param: Lambda parameter
    """
    print("\n" + "=" * 70)
    print("CHANNEL MODEL SUMMARY")
    print("=" * 70)
    
    # Find best modes
    sorted_results = sorted(results.items(), key=lambda x: x[1]['F(n)'])
    
    print(f"\n--- Top 15 Most Stable Modes (Lowest F(n), λ={lambda_param}) ---")
    for i, (n, data) in enumerate(sorted_results[:15]):
        prime_str = "PRIME" if data['is_prime'] else "composite"
        print(f"{i+1:2d}. n={n:3d} ({prime_str:9s}): F(n)={data['F(n)']:.6f}, "
              f"error={data['error_rate']:.4f}, redundancy={data['redundancy']:.3f}")
    
    # Find stability regions
    stable_modes = find_stability_regions(results, threshold_percentile=25)
    print(f"\n--- Stability Region (top 25th percentile) ---")
    print(f"Number of stable modes: {len(stable_modes)}")
    
    stable_primes = [n for n, _ in stable_modes if results[n]['is_prime']]
    print(f"Primes in stability region: {len(stable_primes)}")
    print(f"First 10 stable modes: {[n for n, _ in stable_modes[:10]]}")
    
    # Check 137 and 139
    if 137 in results:
        rank_137 = next(i for i, (n, _) in enumerate(sorted_results) if n == 137) + 1
        print(f"\n--- n=137 Analysis ---")
        print(f"Rank: {rank_137} out of {len(results)}")
        print(f"F(137) = {results[137]['F(n)']:.6f}")
        print(f"Error rate: {results[137]['error_rate']:.4f}")
        print(f"In stability region: {'YES' if 137 in [n for n, _ in stable_modes] else 'NO'}")
    
    if 139 in results:
        rank_139 = next(i for i, (n, _) in enumerate(sorted_results) if n == 139) + 1
        print(f"\n--- n=139 Analysis ---")
        print(f"Rank: {rank_139} out of {len(results)}")
        print(f"F(139) = {results[139]['F(n)']:.6f}")
        print(f"Error rate: {results[139]['error_rate']:.4f}")
        print(f"In stability region: {'YES' if 139 in [n for n, _ in stable_modes] else 'NO'}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Channel error model analysis'
    )
    parser.add_argument('--lambda', dest='lambda_param', type=float, default=0.5,
                        help='Lambda parameter for cost functional (default: 0.5)')
    parser.add_argument('--range', nargs=2, type=int, default=[100, 200],
                        metavar=('MIN', 'MAX'),
                        help='Range of modes (default: 100 200)')
    parser.add_argument('--output', type=str, default='results/channel_model',
                        help='Output directory')
    
    args = parser.parse_args()
    
    n_min, n_max = args.range
    
    # Run analysis
    results = evaluate_channel_model(n_min, n_max, args.lambda_param, 
                                     output_dir=args.output)
    
    # Generate plots
    plot_cost_functional(results, args.lambda_param,
                        output_file=Path(args.output) / f'cost_functional_lambda{args.lambda_param:.2f}.png')
    
    # Print summary
    print_analysis_summary(results, args.lambda_param)


if __name__ == '__main__':
    main()
