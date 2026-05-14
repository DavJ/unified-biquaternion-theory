# Copyright (c) 2026 David Jaroš (UBT Framework)
# SPDX-License-Identifier: MIT

"""
Alpha Stability Scan: Test if n=137 is a Derived Selection or Arbitrary Choice

This script performs a systematic scan over candidate winding numbers n
to determine whether n=137 emerges as a stability maximum or is simply
an arbitrary Layer-2 channel selection.

Usage:
    python -m analysis.alpha_stability_scan --range 101 199 --seed 0
    python -m analysis.alpha_stability_scan --range 101 199 --primes-only --seed 0
    python -m analysis.alpha_stability_scan --help

Output:
    - CSV file with stability metrics for all candidates
    - JSON summary with top-K candidates and whether 137 is a local maximum
    - Console summary table
"""

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import List, Dict, Tuple, Optional

import numpy as np

from analysis.stability_metrics import (
    compute_all_metrics,
    is_prime,
    is_twin_prime
)


def scan_range(n_min: int, n_max: int, 
               filter_primes: bool = False,
               filter_twin_primes: bool = False,
               seed: Optional[int] = None) -> List[Dict]:
    """
    Scan stability metrics over a range of winding numbers.
    
    Args:
        n_min: Minimum winding number
        n_max: Maximum winding number (inclusive)
        filter_primes: If True, only scan prime numbers
        filter_twin_primes: If True, only scan twin primes
        seed: Random seed for reproducibility
        
    Returns:
        List of dictionaries with metrics for each candidate
    """
    candidates = []
    
    for n in range(n_min, n_max + 1):
        # Apply filters
        if filter_twin_primes and not is_twin_prime(n):
            continue
        elif filter_primes and not is_prime(n):
            continue
            
        # Compute all metrics
        metrics = compute_all_metrics(n, seed=seed)
        candidates.append(metrics)
    
    return candidates


def rank_candidates(candidates: List[Dict], 
                    metric_key: str = 'combined') -> List[Dict]:
    """
    Rank candidates by a specified metric (descending order).
    
    Args:
        candidates: List of candidate dictionaries with metrics
        metric_key: Key to use for ranking ('spectral_gap', 'robustness', 'combined')
        
    Returns:
        Sorted list of candidates with rank added
    """
    # Sort by metric (descending)
    sorted_candidates = sorted(candidates, 
                               key=lambda x: x[metric_key], 
                               reverse=True)
    
    # Add rank
    for rank, candidate in enumerate(sorted_candidates, start=1):
        candidate['rank'] = rank
    
    return sorted_candidates


def find_local_maximum(candidates: List[Dict], 
                       target_n: int = 137,
                       window: int = 5,
                       metric_key: str = 'combined') -> Dict:
    """
    Check if target_n is a local maximum within a window.
    
    Args:
        candidates: List of candidates with metrics
        target_n: Target winding number to check (default 137)
        window: Size of neighborhood to check (±window)
        metric_key: Metric to use for comparison
        
    Returns:
        Dictionary with analysis results
    """
    # Find target in candidates
    target_candidate = None
    for c in candidates:
        if c['n'] == target_n:
            target_candidate = c
            break
    
    if target_candidate is None:
        return {
            'target_n': target_n,
            'found': False,
            'is_local_max': False,
            'message': f'n={target_n} not found in scan range'
        }
    
    target_value = target_candidate[metric_key]
    
    # Check neighborhood
    neighbors_higher = []
    neighbors_same = []
    neighbors_lower = []
    
    for c in candidates:
        n_diff = abs(c['n'] - target_n)
        if n_diff == 0:
            continue
        if n_diff <= window:
            if c[metric_key] > target_value:
                neighbors_higher.append((c['n'], c[metric_key]))
            elif c[metric_key] == target_value:
                neighbors_same.append((c['n'], c[metric_key]))
            else:
                neighbors_lower.append((c['n'], c[metric_key]))
    
    is_local_max = (len(neighbors_higher) == 0)
    is_strict_local_max = (len(neighbors_higher) == 0 and len(neighbors_same) == 0)
    
    return {
        'target_n': target_n,
        'found': True,
        'target_value': target_value,
        'rank': target_candidate.get('rank', None),
        'is_local_max': is_local_max,
        'is_strict_local_max': is_strict_local_max,
        'neighbors_higher': len(neighbors_higher),
        'neighbors_same': len(neighbors_same),
        'neighbors_lower': len(neighbors_lower),
        'higher_neighbors': neighbors_higher[:3] if neighbors_higher else [],
        'window': window
    }


def save_results(candidates: List[Dict], 
                 output_path: Path,
                 format: str = 'csv') -> None:
    """
    Save scan results to file.
    
    Args:
        candidates: List of candidates with metrics and ranks
        output_path: Output file path
        format: Output format ('csv' or 'json')
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    if format == 'csv':
        fieldnames = ['n', 'is_prime', 'is_twin_prime', 'spectral_gap', 
                      'robustness', 'combined', 'rank']
        
        with open(output_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(candidates)
            
        print(f"✓ Saved CSV results to: {output_path}")
        
    elif format == 'json':
        with open(output_path, 'w') as f:
            json.dump(candidates, f, indent=2)
            
        print(f"✓ Saved JSON results to: {output_path}")


def print_summary(candidates: List[Dict], 
                  local_max_analysis: Dict,
                  top_k: int = 10) -> None:
    """
    Print summary of scan results to console.
    
    Args:
        candidates: Ranked list of candidates
        local_max_analysis: Results from find_local_maximum
        top_k: Number of top candidates to show
    """
    print("\n" + "="*80)
    print("ALPHA STABILITY SCAN RESULTS")
    print("="*80)
    
    print(f"\nTotal candidates scanned: {len(candidates)}")
    
    # Top K candidates
    print(f"\nTop {top_k} candidates by combined stability metric:")
    print("-" * 80)
    print(f"{'Rank':<6} {'n':<6} {'Prime':<7} {'TwinP':<7} {'Spectral':<12} {'Robust':<12} {'Combined':<12}")
    print("-" * 80)
    
    for candidate in candidates[:top_k]:
        rank = candidate['rank']
        n = candidate['n']
        is_p = '✓' if candidate['is_prime'] else ''
        is_tp = '✓' if candidate['is_twin_prime'] else ''
        s1 = candidate['spectral_gap']
        s2 = candidate['robustness']
        comb = candidate['combined']
        
        # Highlight n=137 if present
        marker = ' ← TARGET' if n == 137 else ''
        
        print(f"{rank:<6} {n:<6} {is_p:<7} {is_tp:<7} {s1:<12.4f} {s2:<12.4f} {comb:<12.4f}{marker}")
    
    # Local maximum analysis
    print("\n" + "="*80)
    print("LOCAL MAXIMUM ANALYSIS FOR n=137")
    print("="*80)
    
    if not local_max_analysis['found']:
        print(f"✗ {local_max_analysis['message']}")
    else:
        print(f"Target value: {local_max_analysis['target_value']:.4f}")
        print(f"Rank: {local_max_analysis['rank']}/{len(candidates)}")
        print(f"Window: ±{local_max_analysis['window']}")
        print(f"Neighbors with higher value: {local_max_analysis['neighbors_higher']}")
        print(f"Neighbors with same value: {local_max_analysis['neighbors_same']}")
        print(f"Neighbors with lower value: {local_max_analysis['neighbors_lower']}")
        
        if local_max_analysis['is_strict_local_max']:
            print("\n✓ RESULT: n=137 IS a strict local maximum")
            print("  → Supports derivation from stability principle (Layer 1)")
        elif local_max_analysis['is_local_max']:
            print("\n~ RESULT: n=137 IS a local maximum (with ties)")
            print("  → Weakly supports stability principle")
        else:
            print("\n✗ RESULT: n=137 is NOT a local maximum")
            print(f"  → Better candidates exist: {local_max_analysis['higher_neighbors'][:3]}")
            print("  → Currently interpreted as Layer 2 channel selection")


def main():
    """Main entry point for alpha stability scan."""
    parser = argparse.ArgumentParser(
        description='Alpha Stability Scan: Test if n=137 is derived or chosen',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--range', nargs=2, type=int, metavar=('MIN', 'MAX'),
                        default=[101, 199],
                        help='Scan range for winding numbers (default: 101 199)')
    
    parser.add_argument('--primes-only', action='store_true',
                        help='Only scan prime numbers')
    
    parser.add_argument('--twin-primes-only', action='store_true',
                        help='Only scan twin prime numbers')
    
    parser.add_argument('--seed', type=int, default=0,
                        help='Random seed for reproducibility (default: 0)')
    
    parser.add_argument('--out', type=str, 
                        default='scans/alpha_stability_scan.csv',
                        help='Output CSV file path')
    
    parser.add_argument('--json', type=str,
                        help='Optional JSON output file path')
    
    parser.add_argument('--top-k', type=int, default=10,
                        help='Number of top candidates to display (default: 10)')
    
    parser.add_argument('--target', type=int, default=137,
                        help='Target n to check for local maximum (default: 137)')
    
    parser.add_argument('--window', type=int, default=5,
                        help='Window size for local maximum check (default: 5)')
    
    args = parser.parse_args()
    
    # Run scan
    print(f"Scanning range: {args.range[0]} to {args.range[1]}")
    print(f"Filter: {'twin primes only' if args.twin_primes_only else 'primes only' if args.primes_only else 'all integers'}")
    print(f"Random seed: {args.seed}")
    print()
    
    candidates = scan_range(
        args.range[0], args.range[1],
        filter_primes=args.primes_only,
        filter_twin_primes=args.twin_primes_only,
        seed=args.seed
    )
    
    if not candidates:
        print("✗ No candidates found in range with specified filters")
        return 1
    
    # Rank candidates
    ranked_candidates = rank_candidates(candidates, metric_key='combined')
    
    # Check local maximum
    local_max_analysis = find_local_maximum(
        ranked_candidates,
        target_n=args.target,
        window=args.window,
        metric_key='combined'
    )
    
    # Save results
    save_results(ranked_candidates, Path(args.out), format='csv')
    
    if args.json:
        save_results(ranked_candidates, Path(args.json), format='json')
    
    # Save summary JSON
    summary_path = Path(args.out).parent / 'alpha_stability_summary.json'
    summary = {
        'scan_range': args.range,
        'filter': 'twin_primes' if args.twin_primes_only else 'primes' if args.primes_only else 'all',
        'seed': args.seed,
        'total_candidates': len(candidates),
        'target_n': args.target,
        'local_max_analysis': local_max_analysis,
        'top_10': ranked_candidates[:10]
    }
    
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"✓ Saved summary to: {summary_path}")
    
    # Print summary
    print_summary(ranked_candidates, local_max_analysis, top_k=args.top_k)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
