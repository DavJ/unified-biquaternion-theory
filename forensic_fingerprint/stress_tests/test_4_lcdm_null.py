#!/usr/bin/env python3
"""
UBT Forensic Fingerprint - Stress Test #4: Synthetic ΛCDM Null Controls
========================================================================

Test whether ΛCDM realizations generically produce Δℓ = 255.

This script:
1. Generates ≥100 synthetic TT spectra from ΛCDM
2. Uses same ℓ range and noise model as real data
3. Applies identical comb test pipeline to each realization
4. Counts how often Δℓ ≈ 255 appears as best-fit

PASS/FAIL Criteria:
- PASS: Δℓ ≈ 255 appears in ≤1% of ΛCDM realizations
- FAIL: Δℓ ≈ 255 appears frequently in pure ΛCDM

Note: This validates that the candidate signal is not a generic feature of ΛCDM.

License: MIT
Author: UBT Research Team
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
import numpy as np

# Add parent directories to path
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'loaders'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'cmb_comb'))

import planck
import cmb_comb


def generate_synthetic_lcdm_spectrum(ell, cl_theory, sigma, random_seed=None):
    """
    Generate synthetic ΛCDM realization.
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    cl_theory : array-like
        Theoretical ΛCDM C_ell
    sigma : array-like
        Observational uncertainties
    random_seed : int, optional
        Random seed
    
    Returns
    -------
    cl_synthetic : ndarray
        Synthetic observed C_ell
    """
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate Gaussian realizations around theory
    # C_ell^obs = C_ell^theory + N(0, sigma^2)
    noise = np.random.normal(0, sigma, size=len(ell))
    cl_synthetic = cl_theory + noise
    
    return cl_synthetic


def run_lcdm_null_stress_test(
    model_file, obs_file=None,
    ell_min=30, ell_max=1500,
    n_realizations=100,
    output_dir=None, n_mc_trials=1000
):
    """
    Run ΛCDM null control stress test.
    
    Parameters
    ----------
    model_file : str or Path
        ΛCDM model file (used as theory)
    obs_file : str or Path, optional
        Real observation file (used to get sigma if available)
    ell_min : int
        Minimum multipole
    ell_max : int
        Maximum multipole
    n_realizations : int
        Number of synthetic ΛCDM realizations to generate
    output_dir : str or Path, optional
        Output directory
    n_mc_trials : int
        Number of Monte Carlo trials per realization (reduced for speed)
    
    Returns
    -------
    dict
        Results summary
    """
    # Setup output directory
    if output_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = repo_root / 'forensic_fingerprint' / 'out' / 'stress_tests' / f'lcdm_null_{timestamp}'
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("="*80)
    print("STRESS TEST #4: SYNTHETIC ΛCDM NULL CONTROLS")
    print("="*80)
    print(f"Output directory: {output_dir}")
    print(f"Number of realizations: {n_realizations}")
    print()
    
    # Load ΛCDM theory spectrum
    print("Loading ΛCDM theory spectrum...")
    theory_data = planck.load_planck_data(
        obs_file=model_file,
        model_file=None,
        ell_min=ell_min,
        ell_max=ell_max,
        dataset_name="ΛCDM Theory"
    )
    
    ell = theory_data['ell']
    cl_theory = theory_data['cl_obs']
    
    # Get sigma from observations if available, otherwise use fraction of theory
    if obs_file is not None:
        print("Loading observation file for sigma...")
        obs_data = planck.load_planck_data(
            obs_file=obs_file,
            model_file=None,
            ell_min=ell_min,
            ell_max=ell_max,
            dataset_name="Observations"
        )
        sigma = obs_data['sigma']
    else:
        print("No observation file provided. Using 1% of theory as sigma...")
        sigma = 0.01 * np.abs(cl_theory)
    
    print(f"Multipole range: ℓ = {ell[0]} to {ell[-1]} ({len(ell)} multipoles)")
    print()
    
    # Generate and test synthetic realizations
    best_periods = []
    p_values = []
    significances = []
    
    for i in range(n_realizations):
        if (i + 1) % 10 == 0:
            print(f"Processing realization {i+1}/{n_realizations}...")
        
        # Generate synthetic spectrum
        cl_synthetic = generate_synthetic_lcdm_spectrum(
            ell, cl_theory, sigma, random_seed=42 + i
        )
        
        # Run comb test
        results = cmb_comb.run_cmb_comb_test(
            ell=ell,
            C_obs=cl_synthetic,
            C_model=cl_theory,
            sigma=sigma,
            cov=None,
            dataset_name=f"ΛCDM Realization {i+1}",
            variant="C",
            n_mc_trials=n_mc_trials,
            random_seed=42 + i + 1000,  # Different seed for MC
            whiten_mode='diagonal',
            output_dir=None
        )
        
        best_periods.append(results['best_period'])
        p_values.append(results['p_value'])
        significances.append(results['significance'])
    
    print(f"\nCompleted {n_realizations} realizations.")
    print()
    
    # Analyze results
    results_summary = {
        'n_realizations': n_realizations,
        'best_periods': best_periods,
        'p_values': p_values,
        'significances': significances,
        'ell_range': (int(ell[0]), int(ell[-1])),
        'n_mc_trials': n_mc_trials
    }
    
    # Generate report
    generate_lcdm_report(results_summary, output_dir)
    
    # Save JSON
    save_lcdm_json(results_summary, output_dir)
    
    # Generate histogram
    generate_lcdm_histogram(results_summary, output_dir)
    
    return results_summary


def generate_lcdm_report(results_summary, output_dir):
    """Generate markdown report for ΛCDM null controls."""
    output_file = output_dir / 'lcdm_null_comparison.md'
    
    best_periods = results_summary['best_periods']
    p_values = results_summary['p_values']
    n_realizations = results_summary['n_realizations']
    
    # Count occurrences of Δℓ ≈ 255
    n_near_255 = sum(1 for p in best_periods if abs(p - 255) <= 2)
    frac_near_255 = n_near_255 / n_realizations
    
    # Count significant detections at p < 0.01
    n_significant = sum(1 for p in p_values if p < 0.01)
    frac_significant = n_significant / n_realizations
    
    with open(output_file, 'w') as f:
        f.write("# Stress Test #4: Synthetic ΛCDM Null Controls\n\n")
        f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## Objective\n\n")
        f.write("Test whether ΛCDM realizations generically produce Δℓ = 255 as best-fit. ")
        f.write("This validates that the candidate signal is not a common feature of ")
        f.write("pure ΛCDM models.\n\n")
        
        f.write("## Parameters\n\n")
        f.write(f"- Number of realizations: {n_realizations}\n")
        f.write(f"- ℓ range: [{results_summary['ell_range'][0]}, {results_summary['ell_range'][1]}]\n")
        f.write(f"- MC trials per realization: {results_summary['n_mc_trials']}\n\n")
        
        f.write("## Results Summary\n\n")
        f.write(f"- Realizations with Δℓ ≈ 255 (±2): {n_near_255}/{n_realizations} ({frac_near_255*100:.1f}%)\n")
        f.write(f"- Realizations with p < 0.01: {n_significant}/{n_realizations} ({frac_significant*100:.1f}%)\n")
        f.write(f"- Both (Δℓ ≈ 255 AND p < 0.01): {sum(1 for p, pv in zip(best_periods, p_values) if abs(p-255)<=2 and pv<0.01)}/{n_realizations}\n\n")
        
        f.write("### Distribution of Best-fit Periods\n\n")
        
        # Create histogram bins
        period_counts = {}
        for p in best_periods:
            period_counts[p] = period_counts.get(p, 0) + 1
        
        f.write("| Period Δℓ | Count | Fraction |\n")
        f.write("|-----------|-------|----------|\n")
        
        for period in sorted(period_counts.keys()):
            count = period_counts[period]
            frac = count / n_realizations
            marker = " ← **255**" if abs(period - 255) <= 2 else ""
            f.write(f"| {period:9d} | {count:5d} | {frac:8.1%}{marker} |\n")
        
        f.write("\n## PASS/FAIL Assessment\n\n")
        
        # Check pass/fail criterion
        if frac_near_255 <= 0.01:
            f.write("### ✓ PASS\n\n")
            f.write(f"- Δℓ ≈ 255 appears in only {frac_near_255*100:.1f}% of realizations (≤1% threshold)\n")
            f.write("- The candidate signal is NOT a generic feature of ΛCDM\n")
            f.write("- This supports the hypothesis that the real-data signal is distinct\n\n")
        elif frac_near_255 <= 0.05:
            f.write("### ~ MARGINAL\n\n")
            f.write(f"- Δℓ ≈ 255 appears in {frac_near_255*100:.1f}% of realizations (slightly above 1%)\n")
            f.write("- Borderline result - warrants investigation\n")
            f.write("- May need larger n_realizations for definitive test\n\n")
        else:
            f.write("### ✗ FAIL\n\n")
            f.write(f"- Δℓ ≈ 255 appears in {frac_near_255*100:.1f}% of realizations (>>1%)\n")
            f.write("- The candidate period is a COMMON feature in ΛCDM simulations\n")
            f.write("- This suggests the real-data signal is NOT anomalous\n\n")
        
        f.write("## Interpretation\n\n")
        f.write("The ΛCDM null control test checks whether the candidate Δℓ = 255 ")
        f.write("appears frequently in pure ΛCDM realizations. If yes, the real-data ")
        f.write("signal is not special. If no, it suggests genuine anomaly.\n\n")
        
        if frac_near_255 <= 0.01:
            f.write("**Result**: Δℓ = 255 is RARE in ΛCDM simulations. ")
            f.write("This strengthens the case for a structural anomaly in real data.\n")
        else:
            f.write("**Result**: Δℓ = 255 is COMMON in ΛCDM simulations. ")
            f.write("This undermines the hypothesis that the real-data signal is anomalous.\n")
    
    print(f"ΛCDM report saved to: {output_file}")


def save_lcdm_json(results_summary, output_dir):
    """Save ΛCDM null results to JSON."""
    output_data = {
        'n_realizations': results_summary['n_realizations'],
        'ell_range': results_summary['ell_range'],
        'n_mc_trials': results_summary['n_mc_trials'],
        'best_periods': results_summary['best_periods'],
        'p_values': results_summary['p_values'],
        'significances': results_summary['significances'],
        'statistics': {
            'n_near_255': sum(1 for p in results_summary['best_periods'] if abs(p - 255) <= 2),
            'fraction_near_255': sum(1 for p in results_summary['best_periods'] if abs(p - 255) <= 2) / results_summary['n_realizations'],
            'n_significant': sum(1 for p in results_summary['p_values'] if p < 0.01),
            'fraction_significant': sum(1 for p in results_summary['p_values'] if p < 0.01) / results_summary['n_realizations']
        }
    }
    
    output_file = output_dir / 'lcdm_null_distribution.json'
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"ΛCDM JSON saved to: {output_file}")


def generate_lcdm_histogram(results_summary, output_dir):
    """Generate histogram of best-fit periods from ΛCDM realizations."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Matplotlib not available - skipping histogram")
        return
    
    best_periods = results_summary['best_periods']
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Histogram
    ax.hist(best_periods, bins=range(0, max(best_periods) + 10, 8), 
            alpha=0.7, edgecolor='black', label='ΛCDM Realizations')
    
    # Mark 255
    ax.axvline(255, color='red', linestyle='--', linewidth=2, label='Δℓ = 255')
    ax.axvline(253, color='red', linestyle=':', linewidth=1, alpha=0.5)
    ax.axvline(257, color='red', linestyle=':', linewidth=1, alpha=0.5)
    
    ax.set_xlabel('Best-fit Period Δℓ', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title(f'Distribution of Best-fit Δℓ in {results_summary["n_realizations"]} ΛCDM Realizations', 
                fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig(output_dir / 'lcdm_null_histogram.png', dpi=150)
    plt.close()
    
    print(f"ΛCDM histogram saved to: {output_dir / 'lcdm_null_histogram.png'}")


def main():
    parser = argparse.ArgumentParser(
        description="Stress Test #4: Synthetic ΛCDM Null Controls",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--model', type=str, required=True,
                       help='ΛCDM model file (used as theory)')
    parser.add_argument('--obs', type=str,
                       help='Observation file (for sigma extraction, optional)')
    parser.add_argument('--ell_min', type=int, default=30,
                       help='Minimum multipole (default: 30)')
    parser.add_argument('--ell_max', type=int, default=1500,
                       help='Maximum multipole (default: 1500)')
    parser.add_argument('--n_realizations', type=int, default=100,
                       help='Number of synthetic realizations (default: 100)')
    parser.add_argument('--mc_trials', type=int, default=1000,
                       help='MC trials per realization (default: 1000, reduced for speed)')
    parser.add_argument('--output_dir', type=str,
                       help='Output directory (default: auto-generated)')
    
    args = parser.parse_args()
    
    results = run_lcdm_null_stress_test(
        model_file=args.model,
        obs_file=args.obs,
        ell_min=args.ell_min,
        ell_max=args.ell_max,
        n_realizations=args.n_realizations,
        output_dir=args.output_dir,
        n_mc_trials=args.mc_trials
    )
    
    print("\n" + "="*80)
    print("ΛCDM NULL CONTROL STRESS TEST COMPLETE")
    print("="*80)
    print("\nSee lcdm_null_comparison.md for detailed results.\n")


if __name__ == '__main__':
    main()
