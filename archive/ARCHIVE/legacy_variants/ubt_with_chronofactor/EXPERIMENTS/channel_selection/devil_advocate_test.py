#!/usr/bin/env python3
"""
devil_advocate_test.py

Attempt to FALSIFY the hypothesis about privileged status of n=137.

This module implements rigorous statistical tests to determine if 137's
apparent stability could emerge by chance. Uses randomization, permutation
tests, and Monte Carlo simulation.

Usage:
    python devil_advocate_test.py --trials 1000
    python devil_advocate_test.py --trials 1000 --range 100 200 --output results/

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


def randomize_spectrum(spectrum: np.ndarray, seed: Optional[int] = None) -> np.ndarray:
    """
    Randomize spectral data while preserving statistical properties.
    
    Args:
        spectrum: Original spectrum
        seed: Random seed for reproducibility
        
    Returns:
        Randomized spectrum
    """
    if seed is not None:
        np.random.seed(seed)
    
    # Shuffle amplitudes
    randomized = spectrum.copy()
    np.random.shuffle(randomized)
    
    return randomized


def permutation_test(results: Dict[int, Dict[str, float]], 
                    target_n: int = 137,
                    n_permutations: int = 1000) -> Tuple[float, List[int]]:
    """
    Permutation test to assess if target mode's ranking is significant.
    
    Null hypothesis: The ranking of mode n is random.
    
    Args:
        results: Results dictionary
        target_n: Target mode number to test
        n_permutations: Number of permutations
        
    Returns:
        (p_value, permuted_ranks)
    """
    # Original rank of target
    sorted_results = sorted(results.items(), key=lambda x: x[1]['I(n)'])
    original_rank = next(i for i, (n, _) in enumerate(sorted_results) if n == target_n) + 1
    
    # Permutation test
    I_values = [data['I(n)'] for data in results.values()]
    permuted_ranks = []
    
    for i in range(n_permutations):
        # Shuffle I(n) values
        shuffled_I = I_values.copy()
        np.random.shuffle(shuffled_I)
        
        # Reassign to modes
        shuffled_results = {n: shuffled_I[j] for j, n in enumerate(results.keys())}
        
        # Find target's rank in shuffled data
        shuffled_sorted = sorted(shuffled_results.items(), key=lambda x: x[1])
        shuffled_rank = next(i for i, (n, _) in enumerate(shuffled_sorted) if n == target_n) + 1
        permuted_ranks.append(shuffled_rank)
    
    # P-value: fraction of permutations where rank is as good or better
    p_value = np.mean([r <= original_rank for r in permuted_ranks])
    
    return p_value, permuted_ranks


def monte_carlo_simulation(n_min: int, n_max: int, 
                           target_n: int = 137,
                           n_trials: int = 1000) -> Tuple[float, List[int]]:
    """
    Monte Carlo simulation with randomized spectra.
    
    Test if target mode consistently ranks high across different
    random spectral configurations.
    
    Args:
        n_min: Minimum mode number
        n_max: Maximum mode number
        target_n: Target mode to track
        n_trials: Number of Monte Carlo trials
        
    Returns:
        (mean_rank, ranks_list)
    """
    print(f"\nRunning Monte Carlo simulation ({n_trials} trials)...")
    
    ranks = []
    
    for trial in range(n_trials):
        if (trial + 1) % 100 == 0:
            print(f"  Trial {trial + 1}/{n_trials}")
        
        # Generate random spectrum
        spectrum = randomize_spectrum(
            generate_harmonic_spectrum(n_max + 50), 
            seed=trial
        )
        
        # Compute I(n) for all modes
        trial_results = {}
        for n in range(n_min, n_max + 1):
            I_n = compute_interference_functional(n, spectrum)
            trial_results[n] = I_n
        
        # Find target's rank
        sorted_trial = sorted(trial_results.items(), key=lambda x: x[1])
        rank = next(i for i, (n, _) in enumerate(sorted_trial) if n == target_n) + 1
        ranks.append(rank)
    
    mean_rank = np.mean(ranks)
    
    return mean_rank, ranks


def bootstrap_confidence_interval(results: Dict[int, Dict[str, float]],
                                  target_n: int = 137,
                                  n_bootstrap: int = 1000,
                                  confidence: float = 0.95) -> Tuple[int, int]:
    """
    Bootstrap confidence interval for target mode's rank.
    
    Args:
        results: Results dictionary
        target_n: Target mode
        n_bootstrap: Number of bootstrap samples
        confidence: Confidence level (e.g., 0.95 for 95%)
        
    Returns:
        (lower_bound, upper_bound) for rank
    """
    n_modes = len(results)
    ranks = []
    
    for _ in range(n_bootstrap):
        # Resample with replacement
        sample_indices = np.random.choice(n_modes, size=n_modes, replace=True)
        sample_results = {list(results.keys())[i]: results[list(results.keys())[i]] 
                         for i in sample_indices}
        
        # Compute rank
        sorted_sample = sorted(sample_results.items(), key=lambda x: x[1]['I(n)'])
        if target_n in sample_results:
            rank = next((i for i, (n, _) in enumerate(sorted_sample) if n == target_n), n_modes) + 1
            ranks.append(rank)
    
    # Confidence interval
    alpha = 1 - confidence
    lower = np.percentile(ranks, 100 * alpha / 2)
    upper = np.percentile(ranks, 100 * (1 - alpha / 2))
    
    return int(lower), int(upper)


def compute_falsification_score(p_permutation: float, 
                                mean_mc_rank: float,
                                total_modes: int,
                                actual_rank: int) -> Dict[str, float]:
    """
    Compute falsification score.
    
    Higher score = more evidence that 137 is NOT special.
    Lower score = 137 appears genuinely special.
    
    Args:
        p_permutation: P-value from permutation test
        mean_mc_rank: Mean rank from Monte Carlo
        total_modes: Total number of modes
        actual_rank: Actual rank in original data
        
    Returns:
        Dictionary with falsification metrics
    """
    # Normalized rank (0 = best, 1 = worst)
    norm_actual = actual_rank / total_modes
    norm_mc = mean_mc_rank / total_modes
    
    # Falsification score components:
    # 1. P-value (high = likely random)
    # 2. Rank stability (high MC rank = unstable under randomization)
    # 3. Rank difference (large difference = sensitive to spectrum details)
    
    falsification_score = (
        0.4 * p_permutation +  # Weight permutation p-value
        0.3 * norm_mc +         # Weight MC rank
        0.3 * abs(norm_mc - norm_actual)  # Weight rank instability
    )
    
    return {
        'falsification_score': falsification_score,
        'p_permutation': p_permutation,
        'normalized_actual_rank': norm_actual,
        'normalized_mc_rank': norm_mc,
        'rank_instability': abs(norm_mc - norm_actual)
    }


def run_devil_advocate_test(n_min: int = 100, n_max: int = 200,
                            target_n: int = 137,
                            n_trials: int = 1000,
                            output_dir: Optional[str] = None) -> Dict[str, any]:
    """
    Run complete devil's advocate falsification test.
    
    Args:
        n_min: Minimum mode number
        n_max: Maximum mode number
        target_n: Target mode to test
        n_trials: Number of randomization trials
        output_dir: Optional output directory
        
    Returns:
        Dictionary with test results
    """
    print("=" * 70)
    print("DEVIL'S ADVOCATE TEST")
    print("=" * 70)
    print(f"Target mode: n={target_n}")
    print(f"Range: n ∈ [{n_min}, {n_max}]")
    print(f"Trials: {n_trials}\n")
    
    # 1. Original analysis
    print("Step 1: Computing original interference functional...")
    results = evaluate_range(n_min, n_max)
    
    sorted_results = sorted(results.items(), key=lambda x: x[1]['I(n)'])
    original_rank = next(i for i, (n, _) in enumerate(sorted_results) if n == target_n) + 1
    
    print(f"  Original rank of n={target_n}: {original_rank} out of {len(results)}")
    print(f"  I({target_n}) = {results[target_n]['I(n)']:.6f}")
    
    # 2. Permutation test
    print("\nStep 2: Running permutation test...")
    p_perm, perm_ranks = permutation_test(results, target_n, n_permutations=n_trials)
    print(f"  P-value (permutation): {p_perm:.4f}")
    print(f"  Mean permuted rank: {np.mean(perm_ranks):.1f}")
    print(f"  Std permuted rank: {np.std(perm_ranks):.1f}")
    
    # 3. Monte Carlo simulation
    print("\nStep 3: Running Monte Carlo simulation...")
    mean_mc_rank, mc_ranks = monte_carlo_simulation(n_min, n_max, target_n, n_trials)
    print(f"  Mean MC rank: {mean_mc_rank:.1f}")
    print(f"  Std MC rank: {np.std(mc_ranks):.1f}")
    
    # 4. Bootstrap CI
    print("\nStep 4: Computing bootstrap confidence interval...")
    ci_lower, ci_upper = bootstrap_confidence_interval(results, target_n, 
                                                       n_bootstrap=n_trials)
    print(f"  95% CI for rank: [{ci_lower}, {ci_upper}]")
    
    # 5. Falsification score
    print("\nStep 5: Computing falsification score...")
    falsification = compute_falsification_score(p_perm, mean_mc_rank, 
                                                len(results), original_rank)
    
    # Compile results
    test_results = {
        'target_n': target_n,
        'original_rank': original_rank,
        'total_modes': len(results),
        'p_permutation': p_perm,
        'mean_mc_rank': mean_mc_rank,
        'std_mc_rank': np.std(mc_ranks),
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'falsification_score': falsification['falsification_score'],
        'perm_ranks': perm_ranks,
        'mc_ranks': mc_ranks
    }
    
    # Save results
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Save summary
        summary_path = output_path / f'falsification_test_n{target_n}.csv'
        with open(summary_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Metric', 'Value'])
            writer.writerow(['Target mode', target_n])
            writer.writerow(['Original rank', original_rank])
            writer.writerow(['Total modes', len(results)])
            writer.writerow(['P-value (permutation)', f'{p_perm:.4f}'])
            writer.writerow(['Mean MC rank', f'{mean_mc_rank:.2f}'])
            writer.writerow(['Std MC rank', f'{np.std(mc_ranks):.2f}'])
            writer.writerow(['95% CI lower', ci_lower])
            writer.writerow(['95% CI upper', ci_upper])
            writer.writerow(['Falsification score', f'{falsification["falsification_score"]:.4f}'])
        
        print(f"\nResults saved to {summary_path}")
        
        # Plot distributions
        if HAS_MATPLOTLIB:
            plot_falsification_results(test_results, output_path)
    
    return test_results


def plot_falsification_results(test_results: Dict[str, any], 
                               output_dir: Path) -> None:
    """
    Plot falsification test results.
    
    Args:
        test_results: Results dictionary
        output_dir: Output directory
    """
    if not HAS_MATPLOTLIB:
        return
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Plot 1: Permutation test ranks
    ax1.hist(test_results['perm_ranks'], bins=30, alpha=0.7, color='blue', 
             edgecolor='black')
    ax1.axvline(test_results['original_rank'], color='red', linestyle='--', 
                linewidth=2, label=f'Original rank = {test_results["original_rank"]}')
    ax1.set_xlabel('Rank', fontsize=12)
    ax1.set_ylabel('Frequency', fontsize=12)
    ax1.set_title(f'Permutation Test (n={test_results["target_n"]})\n'
                  f'P-value = {test_results["p_permutation"]:.4f}', fontsize=13)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Monte Carlo ranks
    ax2.hist(test_results['mc_ranks'], bins=30, alpha=0.7, color='green', 
             edgecolor='black')
    ax2.axvline(test_results['original_rank'], color='red', linestyle='--', 
                linewidth=2, label=f'Original rank = {test_results["original_rank"]}')
    ax2.axvline(test_results['mean_mc_rank'], color='orange', linestyle=':', 
                linewidth=2, label=f'Mean MC rank = {test_results["mean_mc_rank"]:.1f}')
    ax2.set_xlabel('Rank', fontsize=12)
    ax2.set_ylabel('Frequency', fontsize=12)
    ax2.set_title(f'Monte Carlo Simulation (n={test_results["target_n"]})', fontsize=13)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    plot_path = output_dir / f'falsification_distributions_n{test_results["target_n"]}.png'
    plt.savefig(plot_path, dpi=150)
    print(f"Distributions plot saved to {plot_path}")
    plt.close()


def print_verdict(test_results: Dict[str, any]) -> None:
    """
    Print verdict on whether hypothesis is falsified.
    
    Args:
        test_results: Test results dictionary
    """
    print("\n" + "=" * 70)
    print("VERDICT")
    print("=" * 70)
    
    target_n = test_results['target_n']
    p_val = test_results['p_permutation']
    falsification_score = test_results['falsification_score']
    
    print(f"\nTarget mode: n={target_n}")
    print(f"Falsification score: {falsification_score:.4f}")
    print(f"  (0.0 = definitely special, 1.0 = definitely random)")
    
    # Interpret p-value
    print(f"\nPermutation test p-value: {p_val:.4f}")
    if p_val < 0.01:
        print("  → STRONG evidence that n={target_n} is NOT random (p < 0.01)")
    elif p_val < 0.05:
        print("  → Moderate evidence that n={target_n} is NOT random (p < 0.05)")
    elif p_val < 0.10:
        print("  → Weak evidence that n={target_n} is NOT random (p < 0.10)")
    else:
        print("  → No significant evidence (p ≥ 0.10)")
        print(f"  → n={target_n} ranking appears CONSISTENT with random chance")
    
    # Overall verdict
    print("\n" + "-" * 70)
    if falsification_score < 0.2:
        print("VERDICT: Hypothesis NOT falsified.")
        print(f"         n={target_n} appears GENUINELY SPECIAL.")
    elif falsification_score < 0.4:
        print("VERDICT: Weak evidence against hypothesis.")
        print(f"         n={target_n} shows some special properties.")
    elif falsification_score < 0.6:
        print("VERDICT: Insufficient evidence either way.")
        print(f"         n={target_n} status is AMBIGUOUS.")
    else:
        print("VERDICT: Hypothesis FALSIFIED.")
        print(f"         n={target_n} does NOT appear special.")
        print("         Observed ranking likely due to CHANCE.")
    print("-" * 70)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Devil's advocate test for mode 137 hypothesis"
    )
    parser.add_argument('--target', type=int, default=137,
                        help='Target mode to test (default: 137)')
    parser.add_argument('--range', nargs=2, type=int, default=[100, 200],
                        metavar=('MIN', 'MAX'),
                        help='Range of modes (default: 100 200)')
    parser.add_argument('--trials', type=int, default=1000,
                        help='Number of randomization trials (default: 1000)')
    parser.add_argument('--output', type=str, default='results/devil_advocate',
                        help='Output directory')
    
    args = parser.parse_args()
    
    n_min, n_max = args.range
    
    # Run test
    test_results = run_devil_advocate_test(n_min, n_max, args.target, 
                                          args.trials, output_dir=args.output)
    
    # Print verdict
    print_verdict(test_results)
    
    # Also test 139 if it's in range
    if args.target == 137 and 139 <= n_max:
        print("\n\n" + "=" * 70)
        print("BONUS: Testing n=139")
        print("=" * 70)
        test_results_139 = run_devil_advocate_test(n_min, n_max, 139, 
                                                   args.trials, output_dir=args.output)
        print_verdict(test_results_139)


if __name__ == '__main__':
    main()
