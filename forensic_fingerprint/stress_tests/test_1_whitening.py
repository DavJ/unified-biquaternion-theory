#!/usr/bin/env python3
"""
UBT Forensic Fingerprint - Stress Test #1: Whitening / Full Covariance
=======================================================================

Test whether the TT candidate signal survives when using different whitening modes.

This script:
1. Runs the CMB comb test with different whitening modes:
   - none (no whitening)
   - diagonal (default, diagonal uncertainties only)
   - block-diagonal (approximate covariance with local correlations)
   - covariance (full covariance if available)
2. Compares results across modes
3. Generates comparison plots
4. Outputs planck_whitened_results.json

PASS/FAIL Criteria:
- PASS: Peak remains at Δℓ ≈ 255 (±1-2 bins) with p < 10⁻³ across all modes
- FAIL: Peak disappears or shifts arbitrarily after whitening

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


def run_whitening_stress_test(obs_file, model_file, cov_file=None, 
                               ell_min=30, ell_max=1500, 
                               output_dir=None, n_mc_trials=5000):
    """
    Run whitening stress test on Planck TT data.
    
    Parameters
    ----------
    obs_file : str or Path
        Planck observation file
    model_file : str or Path
        Planck model file
    cov_file : str or Path, optional
        Covariance matrix file
    ell_min : int
        Minimum multipole
    ell_max : int
        Maximum multipole
    output_dir : str or Path, optional
        Output directory
    n_mc_trials : int
        Number of Monte Carlo trials
    
    Returns
    -------
    dict
        Results for each whitening mode
    """
    # Setup output directory
    if output_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = repo_root / 'forensic_fingerprint' / 'out' / 'stress_tests' / f'whitening_{timestamp}'
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("="*80)
    print("STRESS TEST #1: WHITENING / FULL COVARIANCE")
    print("="*80)
    print(f"Output directory: {output_dir}")
    print()
    
    # Load data once
    print("Loading Planck TT data...")
    data = planck.load_planck_data(
        obs_file=obs_file,
        model_file=model_file,
        cov_file=cov_file,
        ell_min=ell_min,
        ell_max=ell_max,
        dataset_name="Planck PR3 TT"
    )
    
    print(f"Loaded {data['n_multipoles']} multipoles (ℓ = {data['ell_range'][0]} to {data['ell_range'][1]})")
    print()
    
    # Whitening modes to test
    modes = ['none', 'diagonal', 'block-diagonal']
    if data['cov'] is not None:
        modes.extend(['cov_diag', 'covariance'])
    
    results_all = {}
    
    for mode in modes:
        print("="*80)
        print(f"TESTING WHITENING MODE: {mode.upper()}")
        print("="*80)
        print()
        
        # Run CMB comb test
        results = cmb_comb.run_cmb_comb_test(
            ell=data['ell'],
            C_obs=data['cl_obs'],
            C_model=data['cl_model'] if data['cl_model'] is not None else data['cl_obs'] * 0,
            sigma=data['sigma'],
            cov=data['cov'],
            dataset_name=f"Planck PR3 TT (whiten={mode})",
            variant="C",
            n_mc_trials=n_mc_trials,
            random_seed=42,
            whiten_mode=mode,
            output_dir=None  # Don't auto-save
        )
        
        results_all[mode] = results
        
        # Save individual results
        mode_dir = output_dir / mode
        mode_dir.mkdir(exist_ok=True)
        cmb_comb.save_results(results, mode_dir)
        cmb_comb.plot_results(results, mode_dir)
        
        print()
    
    # Generate comparison report
    generate_comparison_report(results_all, output_dir)
    
    # Save combined results as JSON
    save_combined_json(results_all, output_dir / 'planck_whitened_results.json')
    
    # Generate comparison plots
    generate_comparison_plots(results_all, output_dir)
    
    return results_all


def generate_comparison_report(results_all, output_dir):
    """Generate markdown comparison report."""
    output_file = output_dir / 'whitening_comparison.md'
    
    with open(output_file, 'w') as f:
        f.write("# Stress Test #1: Whitening / Full Covariance\n\n")
        f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## Objective\n\n")
        f.write("Test whether the TT candidate signal at Δℓ ≈ 255 survives when using ")
        f.write("different whitening modes to account for correlated noise.\n\n")
        
        f.write("## Results Summary\n\n")
        f.write("| Whitening Mode | Best Δℓ | Amplitude | Phase (rad) | Max Δχ² | p-value | Significance |\n")
        f.write("|----------------|---------|-----------|-------------|---------|---------|-------------|\n")
        
        for mode, results in results_all.items():
            f.write(f"| {mode:14s} | {results['best_period']:7d} | "
                   f"{results['amplitude']:9.4f} | {results['phase']:11.4f} | "
                   f"{results['max_delta_chi2']:7.2f} | {results['p_value']:7.2e} | "
                   f"{results['significance']:12s} |\n")
        
        f.write("\n## PASS/FAIL Assessment\n\n")
        
        # Check consistency
        periods = [r['best_period'] for r in results_all.values()]
        pvalues = [r['p_value'] for r in results_all.values()]
        
        period_consistent = all(abs(p - 255) <= 2 for p in periods)
        pvalue_threshold = all(p < 0.001 for p in pvalues)
        
        if period_consistent and pvalue_threshold:
            f.write("### ✓ PASS\n\n")
            f.write("- Peak remains at Δℓ ≈ 255 (±1-2 bins) across all whitening modes\n")
            f.write("- All p-values < 10⁻³\n")
            f.write("- Signal survives whitening stress test\n\n")
        else:
            f.write("### ✗ FAIL\n\n")
            if not period_consistent:
                f.write(f"- Peak position varies: {periods}\n")
            if not pvalue_threshold:
                f.write(f"- Some p-values ≥ 10⁻³: {pvalues}\n")
            f.write("- Signal does NOT survive whitening stress test\n\n")
        
        f.write("## Interpretation\n\n")
        f.write("The whitening test checks whether the candidate signal is an artifact ")
        f.write("of ignoring error correlations. A true structural signal should persist ")
        f.write("regardless of the error model used.\n\n")
        
        if period_consistent and pvalue_threshold:
            f.write("**Result**: The signal survives this falsification attempt. ")
            f.write("This increases confidence but does NOT constitute proof.\n")
        else:
            f.write("**Result**: The signal does NOT survive this falsification attempt. ")
            f.write("This suggests the candidate may be an artifact of the error model.\n")
    
    print(f"Comparison report saved to: {output_file}")


def save_combined_json(results_all, output_file):
    """Save combined results to JSON."""
    # Convert to serializable format
    combined = {}
    for mode, results in results_all.items():
        combined[mode] = {
            'best_period': int(results['best_period']),
            'amplitude': float(results['amplitude']),
            'phase': float(results['phase']),
            'max_delta_chi2': float(results['max_delta_chi2']),
            'p_value': float(results['p_value']),
            'significance': results['significance'],
            'whiten_mode': results['whiten_mode'],
            'n_mc_trials': results['n_mc_trials']
        }
    
    with open(output_file, 'w') as f:
        json.dump(combined, f, indent=2)
    
    print(f"Combined JSON saved to: {output_file}")


def generate_comparison_plots(results_all, output_dir):
    """Generate comparison plots."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Matplotlib not available - skipping comparison plots")
        return
    
    # Plot 1: Δχ² comparison across modes
    fig, ax = plt.subplots(figsize=(10, 6))
    
    for mode, results in results_all.items():
        periods = sorted(results['all_periods'].keys())
        delta_chi2_values = [results['all_periods'][p]['delta_chi2'] for p in periods]
        ax.plot(periods, delta_chi2_values, 'o-', label=mode, linewidth=2, markersize=8)
    
    ax.set_xlabel('Period Δℓ', fontsize=12)
    ax.set_ylabel('Δχ²', fontsize=12)
    ax.set_title('Δχ² vs Period: Whitening Mode Comparison', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'whitening_delta_chi2_comparison.png', dpi=150)
    plt.close()
    
    print(f"Comparison plot saved to: {output_dir / 'whitening_delta_chi2_comparison.png'}")


def main():
    parser = argparse.ArgumentParser(
        description="Stress Test #1: Whitening / Full Covariance",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--obs', type=str, required=True,
                       help='Planck observation file')
    parser.add_argument('--model', type=str, required=True,
                       help='Planck model file')
    parser.add_argument('--cov', type=str,
                       help='Covariance file (optional)')
    parser.add_argument('--ell_min', type=int, default=30,
                       help='Minimum multipole (default: 30)')
    parser.add_argument('--ell_max', type=int, default=1500,
                       help='Maximum multipole (default: 1500)')
    parser.add_argument('--output_dir', type=str,
                       help='Output directory (default: auto-generated)')
    parser.add_argument('--mc_trials', type=int, default=5000,
                       help='Number of MC trials (default: 5000)')
    
    args = parser.parse_args()
    
    results = run_whitening_stress_test(
        obs_file=args.obs,
        model_file=args.model,
        cov_file=args.cov,
        ell_min=args.ell_min,
        ell_max=args.ell_max,
        output_dir=args.output_dir,
        n_mc_trials=args.mc_trials
    )
    
    print("\n" + "="*80)
    print("WHITENING STRESS TEST COMPLETE")
    print("="*80)
    print("\nSee whitening_comparison.md for detailed results.\n")


if __name__ == '__main__':
    main()
