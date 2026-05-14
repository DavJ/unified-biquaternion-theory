#!/usr/bin/env python3
"""
prime_vs_composite_scan.py

Systematically compare spectral stability of prime numbers vs composite numbers.
Generates ranking tables and plots without privileging any specific mode.

Usage:
    python prime_vs_composite_scan.py --range 100 200
    python prime_vs_composite_scan.py --range 100 200 --output results/

Author: UBT Research Team
License: See repository LICENSE.md
"""

import argparse
import csv
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple

# Import from interference_functional module
from interference_functional import (
    evaluate_range, is_prime, generate_harmonic_spectrum,
    compute_interference_functional
)

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("Warning: matplotlib not available, plots will be skipped")


def generate_prime_list(n_min: int, n_max: int) -> List[int]:
    """
    Generate list of prime numbers in range [n_min, n_max].
    
    Args:
        n_min: Minimum value
        n_max: Maximum value
        
    Returns:
        List of prime numbers
    """
    return [n for n in range(n_min, n_max + 1) if is_prime(n)]


def create_ranking_table(results: Dict[int, Dict[str, float]], 
                         output_file: str = None) -> List[Tuple[int, float, bool]]:
    """
    Create ranking table sorted by I(n).
    
    Args:
        results: Results dictionary from evaluate_range
        output_file: Optional CSV output path
        
    Returns:
        List of (n, I(n), is_prime) tuples sorted by I(n)
    """
    # Sort by I(n)
    ranking = [(n, data['I(n)'], data['is_prime']) 
               for n, data in results.items()]
    ranking.sort(key=lambda x: x[1])  # Sort by I(n)
    
    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Rank', 'n', 'I(n)', 'Type', 'Note'])
            
            for rank, (n, I_n, prime) in enumerate(ranking, 1):
                type_str = 'PRIME' if prime else 'composite'
                note = ''
                if n == 137:
                    note = '← n=137'
                elif n == 139:
                    note = '← n=139'
                writer.writerow([rank, n, f'{I_n:.6f}', type_str, note])
        
        print(f"Ranking table written to {output_path}")
    
    return ranking


def plot_interference_landscape(results: Dict[int, Dict[str, float]],
                                output_file: str = None) -> None:
    """
    Plot I(n) vs n with primes and composites distinguished.
    
    Args:
        results: Results dictionary from evaluate_range
        output_file: Output plot file path
    """
    if not HAS_MATPLOTLIB:
        print("Skipping plot (matplotlib not available)")
        return
    
    # Separate primes and composites
    primes = {n: data for n, data in results.items() if data['is_prime']}
    composites = {n: data for n, data in results.items() if not data['is_prime']}
    
    prime_n = sorted(primes.keys())
    prime_I = [primes[n]['I(n)'] for n in prime_n]
    
    composite_n = sorted(composites.keys())
    composite_I = [composites[n]['I(n)'] for n in composite_n]
    
    # Create plot
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot composites as light gray dots
    ax.scatter(composite_n, composite_I, c='lightgray', s=20, 
               label='Composite', alpha=0.6, marker='o')
    
    # Plot primes as blue dots
    ax.scatter(prime_n, prime_I, c='blue', s=40, 
               label='Prime', alpha=0.7, marker='o')
    
    # Highlight 137 and 139 without special treatment
    if 137 in results:
        ax.scatter([137], [results[137]['I(n)']], c='red', s=100, 
                   marker='s', label='n=137', zorder=5)
        ax.annotate('137', (137, results[137]['I(n)']), 
                    xytext=(5, 5), textcoords='offset points', fontsize=9)
    
    if 139 in results:
        ax.scatter([139], [results[139]['I(n)']], c='orange', s=100, 
                   marker='^', label='n=139', zorder=5)
        ax.annotate('139', (139, results[139]['I(n)']), 
                    xytext=(5, 5), textcoords='offset points', fontsize=9)
    
    ax.set_xlabel('Mode number n', fontsize=12)
    ax.set_ylabel('Interference functional I(n)', fontsize=12)
    ax.set_title('Interference Functional Landscape: Prime vs Composite Modes', 
                 fontsize=14)
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=150)
        print(f"Plot saved to {output_path}")
    else:
        plt.savefig('interference_landscape.png', dpi=150)
        print("Plot saved to interference_landscape.png")
    
    plt.close()


def plot_prime_composite_distributions(results: Dict[int, Dict[str, float]],
                                       output_file: str = None) -> None:
    """
    Plot distributions of I(n) for primes vs composites.
    
    Args:
        results: Results dictionary from evaluate_range
        output_file: Output plot file path
    """
    if not HAS_MATPLOTLIB:
        print("Skipping plot (matplotlib not available)")
        return
    
    # Separate primes and composites
    primes = [data['I(n)'] for data in results.values() if data['is_prime']]
    composites = [data['I(n)'] for data in results.values() if not data['is_prime']]
    
    # Create plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Histogram
    bins = np.linspace(min(min(primes), min(composites)), 
                       max(max(primes), max(composites)), 30)
    ax1.hist(composites, bins=bins, alpha=0.5, label='Composite', color='gray')
    ax1.hist(primes, bins=bins, alpha=0.7, label='Prime', color='blue')
    ax1.set_xlabel('I(n)', fontsize=12)
    ax1.set_ylabel('Count', fontsize=12)
    ax1.set_title('Distribution of I(n): Prime vs Composite', fontsize=13)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Box plot
    ax2.boxplot([composites, primes], labels=['Composite', 'Prime'])
    ax2.set_ylabel('I(n)', fontsize=12)
    ax2.set_title('I(n) Statistics', fontsize=13)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=150)
        print(f"Distribution plot saved to {output_path}")
    else:
        plt.savefig('prime_composite_distributions.png', dpi=150)
        print("Distribution plot saved to prime_composite_distributions.png")
    
    plt.close()


def run_prime_composite_scan(n_min: int = 100, n_max: int = 200,
                             output_dir: str = None) -> None:
    """
    Run full prime vs composite scan.
    
    Args:
        n_min: Minimum mode number
        n_max: Maximum mode number
        output_dir: Output directory for results
    """
    print("=" * 70)
    print("PRIME VS COMPOSITE MODE SCAN")
    print("=" * 70)
    print(f"Range: n ∈ [{n_min}, {n_max}]\n")
    
    # Setup output directory
    if output_dir:
        output_path = Path(output_dir)
    else:
        output_path = Path('results')
    
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Generate prime list
    primes = generate_prime_list(n_min, n_max)
    print(f"Prime numbers in range: {len(primes)}")
    print(f"Prime list (first 10): {primes[:10]}")
    if len(primes) > 10:
        print(f"... (showing {min(10, len(primes))} of {len(primes)} primes)")
    print()
    
    # Evaluate interference functional
    results = evaluate_range(n_min, n_max, 
                            output_file=str(output_path / 'interference_data.csv'))
    
    # Create ranking table
    print("\nCreating ranking table...")
    ranking = create_ranking_table(results, 
                                   output_file=str(output_path / 'ranking.csv'))
    
    # Display top rankings
    print("\n--- Top 20 Most Stable Modes ---")
    for rank, (n, I_n, prime) in enumerate(ranking[:20], 1):
        type_str = 'PRIME' if prime else 'composite'
        note = ''
        if n == 137:
            note = ' ← n=137 (highlighted)'
        elif n == 139:
            note = ' ← n=139 (highlighted)'
        print(f"{rank:3d}. n={n:3d} ({type_str:9s}): I(n)={I_n:.6f}{note}")
    
    # Generate plots
    print("\nGenerating plots...")
    plot_interference_landscape(results, 
                                str(output_path / 'interference_landscape.png'))
    plot_prime_composite_distributions(results,
                                      str(output_path / 'prime_composite_distributions.png'))
    
    # Statistical summary
    primes_data = [data for data in results.values() if data['is_prime']]
    composites_data = [data for data in results.values() if not data['is_prime']]
    
    prime_I = [d['I(n)'] for d in primes_data]
    composite_I = [d['I(n)'] for d in composites_data]
    
    print("\n" + "=" * 70)
    print("STATISTICAL SUMMARY")
    print("=" * 70)
    print(f"\nPrimes ({len(primes_data)} modes):")
    print(f"  Mean I(n): {np.mean(prime_I):.6f}")
    print(f"  Std I(n):  {np.std(prime_I):.6f}")
    print(f"  Min I(n):  {np.min(prime_I):.6f}")
    print(f"  Max I(n):  {np.max(prime_I):.6f}")
    
    print(f"\nComposites ({len(composites_data)} modes):")
    print(f"  Mean I(n): {np.mean(composite_I):.6f}")
    print(f"  Std I(n):  {np.std(composite_I):.6f}")
    print(f"  Min I(n):  {np.min(composite_I):.6f}")
    print(f"  Max I(n):  {np.max(composite_I):.6f}")
    
    print(f"\nDifference (Composite - Prime):")
    print(f"  Mean: {np.mean(composite_I) - np.mean(prime_I):.6f}")
    
    # Effect size (Cohen's d)
    pooled_std = np.sqrt((np.std(prime_I)**2 + np.std(composite_I)**2) / 2)
    cohens_d = (np.mean(composite_I) - np.mean(prime_I)) / pooled_std
    print(f"  Effect size (Cohen's d): {cohens_d:.3f}")
    
    print(f"\nAll results saved to: {output_path}/")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Scan prime vs composite mode stability'
    )
    parser.add_argument('--range', nargs=2, type=int, default=[100, 200],
                        metavar=('MIN', 'MAX'),
                        help='Range of modes to evaluate (default: 100 200)')
    parser.add_argument('--output', type=str, default='results',
                        help='Output directory (default: results)')
    
    args = parser.parse_args()
    
    n_min, n_max = args.range
    
    run_prime_composite_scan(n_min, n_max, output_dir=args.output)


if __name__ == '__main__':
    main()
