#!/usr/bin/env python3
"""
UBT Forensic Fingerprint - Stress Test #3: ℓ-Range Ablation
============================================================

Test whether the candidate signal depends on a single narrow ℓ window.

This script:
1. Runs the CMB comb test on multiple disjoint ℓ ranges
2. Tests ranges: [30,800], [800,1500], [30,500], [500,1000], [1000,1500]
3. Recomputes null distribution for each range
4. Generates heatmap of p-value vs ℓ-range

PASS/FAIL Criteria:
- PASS: Δℓ ≈ 255 appears in multiple disjoint ℓ ranges
- FAIL: Signal exists only in one narrow window

Skeptic One-Liner:
"If the Δℓ = 255 signal were caused by a narrow-range artifact (foreground, beam 
window, or systematic error localized in ℓ), it would disappear when that range 
is excluded. Persistence across multiple disjoint ranges suggests a global 
structural feature. It does or does not."

Note: A genuine structural signal should not depend on a single ℓ window.

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


# Pre-defined ablation ranges
ABLATION_RANGES = [
    (30, 800),    # Low-ℓ only
    (800, 1500),  # High-ℓ only
    (30, 500),    # Very low-ℓ
    (500, 1000),  # Mid-ℓ
    (1000, 1500), # Very high-ℓ
]


def run_ablation_stress_test(
    obs_file, model_file, cov_file=None,
    custom_ranges=None,
    output_dir=None, n_mc_trials=5000
):
    """
    Run ℓ-range ablation stress test on Planck TT data.
    
    Parameters
    ----------
    obs_file : str or Path
        Planck observation file
    model_file : str or Path
        Planck model file
    cov_file : str or Path, optional
        Covariance matrix file
    custom_ranges : list of tuples, optional
        Custom (ell_min, ell_max) ranges to test. If None, uses ABLATION_RANGES.
    output_dir : str or Path, optional
        Output directory
    n_mc_trials : int
        Number of Monte Carlo trials
    
    Returns
    -------
    dict
        Results for each ℓ range
    """
    # Setup output directory
    if output_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = repo_root / 'forensic_fingerprint' / 'out' / 'stress_tests' / f'ablation_{timestamp}'
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("="*80)
    print("STRESS TEST #3: ℓ-RANGE ABLATION")
    print("="*80)
    print(f"Output directory: {output_dir}")
    print()
    
    # Use custom ranges if provided, otherwise use defaults
    ranges = custom_ranges if custom_ranges is not None else ABLATION_RANGES
    
    print(f"Testing {len(ranges)} ℓ ranges:")
    for ell_min, ell_max in ranges:
        print(f"  - ℓ ∈ [{ell_min}, {ell_max}]")
    print()
    
    results_all = {}
    
    for ell_min, ell_max in ranges:
        range_name = f"ell_{ell_min}_{ell_max}"
        
        print("="*80)
        print(f"TESTING ℓ RANGE: [{ell_min}, {ell_max}]")
        print("="*80)
        print()
        
        # Load data for this range
        data = planck.load_planck_data(
            obs_file=obs_file,
            model_file=model_file,
            cov_file=cov_file,
            ell_min=ell_min,
            ell_max=ell_max,
            dataset_name=f"Planck PR3 TT (ℓ={ell_min}-{ell_max})"
        )
        
        print(f"Loaded {data['n_multipoles']} multipoles")
        
        # Run CMB comb test
        results = cmb_comb.run_cmb_comb_test(
            ell=data['ell'],
            C_obs=data['cl_obs'],
            C_model=data['cl_model'] if data['cl_model'] is not None else data['cl_obs'] * 0,
            sigma=data['sigma'],
            cov=data['cov'],
            dataset_name=data['dataset'],
            variant="C",
            n_mc_trials=n_mc_trials,
            random_seed=42,
            whiten_mode='diagonal',
            output_dir=None
        )
        
        # Add range info to results
        results['ell_range_tested'] = (ell_min, ell_max)
        results_all[range_name] = results
        
        # Save individual results
        range_dir = output_dir / range_name
        range_dir.mkdir(exist_ok=True)
        cmb_comb.save_results(results, range_dir)
        cmb_comb.plot_results(results, range_dir)
        
        print()
    
    # Generate comparison report
    generate_ablation_report(results_all, output_dir)
    
    # Save combined JSON
    save_ablation_json(results_all, output_dir)
    
    # Generate heatmap
    generate_ablation_heatmap(results_all, output_dir)
    
    return results_all


def generate_ablation_report(results_all, output_dir):
    """Generate markdown comparison report for ℓ-range ablation."""
    output_file = output_dir / 'ablation_comparison.md'
    
    with open(output_file, 'w') as f:
        f.write("# Stress Test #3: ℓ-Range Ablation\n\n")
        f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## Objective\n\n")
        f.write("Test whether the candidate signal at Δℓ ≈ 255 appears in multiple ")
        f.write("disjoint ℓ ranges. A genuine structural signal should not depend ")
        f.write("on a single narrow multipole window.\n\n")
        
        f.write("## Results Summary\n\n")
        f.write("| ℓ Range | n_ell | Best Δℓ | Amplitude | Phase (rad) | Max Δχ² | p-value | Significance |\n")
        f.write("|---------|-------|---------|-----------|-------------|---------|---------|-------------|\n")
        
        # Sort by ell_min for readability
        sorted_results = sorted(
            results_all.items(),
            key=lambda x: x[1]['ell_range_tested'][0]
        )
        
        for range_name, results in sorted_results:
            ell_min, ell_max = results['ell_range_tested']
            n_ell = results['n_multipoles']
            f.write(f"| [{ell_min:4d}, {ell_max:4d}] | {n_ell:5d} | "
                   f"{results['best_period']:7d} | {results['amplitude']:9.4f} | "
                   f"{results['phase']:11.4f} | {results['max_delta_chi2']:7.2f} | "
                   f"{results['p_value']:7.2e} | {results['significance']:12s} |\n")
        
        f.write("\n## PASS/FAIL Assessment\n\n")
        
        # Count how many ranges show Δℓ ≈ 255 with p < 0.01
        ranges_with_255 = []
        for range_name, results in sorted_results:
            ell_min, ell_max = results['ell_range_tested']
            if abs(results['best_period'] - 255) <= 2 and results['p_value'] < 0.01:
                ranges_with_255.append((ell_min, ell_max))
        
        n_ranges_total = len(sorted_results)
        n_ranges_with_255 = len(ranges_with_255)
        
        if n_ranges_with_255 >= 2:
            f.write("### ✓ PASS\n\n")
            f.write(f"- Δℓ ≈ 255 appears in {n_ranges_with_255}/{n_ranges_total} ranges with p < 0.01:\n")
            for ell_min, ell_max in ranges_with_255:
                f.write(f"  - ℓ ∈ [{ell_min}, {ell_max}]\n")
            f.write("- Signal is NOT confined to a single narrow window\n")
            f.write("- Consistent with broad structural signature\n\n")
        elif n_ranges_with_255 == 1:
            f.write("### ~ MARGINAL\n\n")
            f.write(f"- Δℓ ≈ 255 appears in only 1/{n_ranges_total} ranges:\n")
            for ell_min, ell_max in ranges_with_255:
                f.write(f"  - ℓ ∈ [{ell_min}, {ell_max}]\n")
            f.write("- Signal may be confined to specific ℓ window\n")
            f.write("- Warrants investigation of window-specific systematics\n\n")
        else:
            f.write("### ✗ FAIL\n\n")
            f.write(f"- Δℓ ≈ 255 does NOT appear consistently across ranges\n")
            f.write("- Signal is ℓ-window dependent\n")
            f.write("- Suggests signal may be an artifact or statistical fluctuation\n\n")
        
        f.write("## Detailed Analysis\n\n")
        
        # Check for systematic trends
        f.write("### Period vs ℓ Range\n\n")
        f.write("| ℓ_min | ℓ_max | Best Δℓ | Δℓ from 255 | p-value |\n")
        f.write("|-------|-------|---------|-------------|-------|\n")
        
        for range_name, results in sorted_results:
            ell_min, ell_max = results['ell_range_tested']
            delta_from_255 = results['best_period'] - 255
            f.write(f"| {ell_min:5d} | {ell_max:5d} | {results['best_period']:7d} | "
                   f"{delta_from_255:+11d} | {results['p_value']:7.2e} |\n")
        
        f.write("\n## Interpretation\n\n")
        f.write("The ℓ-range ablation test checks whether the candidate signal is ")
        f.write("robust across different multipole scales or confined to a specific window. ")
        f.write("A true structural signal should manifest broadly.\n\n")
        
        if n_ranges_with_255 >= 2:
            f.write("**Result**: The signal appears in multiple disjoint ranges. ")
            f.write("This increases confidence in the structural hypothesis.\n")
        elif n_ranges_with_255 == 1:
            f.write("**Result**: The signal appears in only one range. ")
            f.write("This suggests potential ℓ-dependent systematics. Further investigation needed.\n")
        else:
            f.write("**Result**: The signal does NOT appear consistently. ")
            f.write("This suggests the candidate is ℓ-window dependent and likely spurious.\n")
    
    print(f"Ablation report saved to: {output_file}")


def save_ablation_json(results_all, output_dir):
    """Save combined ablation results to JSON."""
    combined = {}
    
    for range_name, results in results_all.items():
        ell_min, ell_max = results['ell_range_tested']
        combined[range_name] = {
            'ell_range': [int(ell_min), int(ell_max)],
            'n_multipoles': results['n_multipoles'],
            'best_period': int(results['best_period']),
            'amplitude': float(results['amplitude']),
            'phase': float(results['phase']),
            'max_delta_chi2': float(results['max_delta_chi2']),
            'p_value': float(results['p_value']),
            'significance': results['significance'],
            'n_mc_trials': results['n_mc_trials']
        }
    
    output_file = output_dir / 'ablation_results.json'
    with open(output_file, 'w') as f:
        json.dump(combined, f, indent=2)
    
    print(f"Ablation JSON saved to: {output_file}")


def generate_ablation_heatmap(results_all, output_dir):
    """Generate heatmap of p-value vs ℓ-range."""
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as patches
    except ImportError:
        print("Matplotlib not available - skipping heatmap")
        return
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Sort results by ell_min
    sorted_results = sorted(
        results_all.items(),
        key=lambda x: x[1]['ell_range_tested'][0]
    )
    
    # Extract data
    ranges = [r[1]['ell_range_tested'] for r in sorted_results]
    periods = [r[1]['best_period'] for r in sorted_results]
    pvalues = [r[1]['p_value'] for r in sorted_results]
    
    # Plot 1: Best period vs ℓ range
    range_labels = [f"[{r[0]},{r[1]}]" for r in ranges]
    colors_period = ['green' if abs(p - 255) <= 2 else 'red' for p in periods]
    
    ax1.barh(range_labels, periods, color=colors_period, alpha=0.7, edgecolor='black')
    ax1.axvline(255, color='blue', linestyle='--', linewidth=2, label='Δℓ = 255')
    ax1.axvline(253, color='blue', linestyle=':', linewidth=1, alpha=0.5)
    ax1.axvline(257, color='blue', linestyle=':', linewidth=1, alpha=0.5)
    ax1.set_xlabel('Best-fit Period Δℓ', fontsize=12)
    ax1.set_ylabel('ℓ Range', fontsize=12)
    ax1.set_title('Best-fit Period vs ℓ Range', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3, axis='x')
    
    # Plot 2: p-value vs ℓ range (log scale)
    colors_pval = ['green' if p < 0.01 else 'orange' if p < 0.05 else 'red' for p in pvalues]
    
    ax2.barh(range_labels, pvalues, color=colors_pval, alpha=0.7, edgecolor='black')
    ax2.axvline(0.01, color='blue', linestyle='--', linewidth=2, label='p = 0.01')
    ax2.axvline(0.001, color='darkblue', linestyle='--', linewidth=2, label='p = 0.001')
    ax2.set_xlabel('p-value', fontsize=12)
    ax2.set_ylabel('ℓ Range', fontsize=12)
    ax2.set_title('p-value vs ℓ Range', fontsize=14, fontweight='bold')
    ax2.set_xscale('log')
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig(output_dir / 'ablation_heatmap.png', dpi=150)
    plt.close()
    
    print(f"Ablation heatmap saved to: {output_dir / 'ablation_heatmap.png'}")


def main():
    parser = argparse.ArgumentParser(
        description="Stress Test #3: ℓ-Range Ablation",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--obs', type=str, required=True,
                       help='Planck observation file')
    parser.add_argument('--model', type=str, required=True,
                       help='Planck model file')
    parser.add_argument('--cov', type=str,
                       help='Covariance file (optional)')
    parser.add_argument('--output_dir', type=str,
                       help='Output directory (default: auto-generated)')
    parser.add_argument('--mc_trials', type=int, default=5000,
                       help='Number of MC trials (default: 5000)')
    parser.add_argument('--custom_ranges', type=str,
                       help='Custom ℓ ranges as JSON string, e.g., "[[30,500],[500,1000]]"')
    
    args = parser.parse_args()
    
    # Parse custom ranges if provided
    custom_ranges = None
    if args.custom_ranges:
        import json as json_lib
        custom_ranges = json_lib.loads(args.custom_ranges)
        # Convert to list of tuples
        custom_ranges = [tuple(r) for r in custom_ranges]
    
    results = run_ablation_stress_test(
        obs_file=args.obs,
        model_file=args.model,
        cov_file=args.cov,
        custom_ranges=custom_ranges,
        output_dir=args.output_dir,
        n_mc_trials=args.mc_trials
    )
    
    print("\n" + "="*80)
    print("ℓ-RANGE ABLATION STRESS TEST COMPLETE")
    print("="*80)
    print("\nSee ablation_comparison.md for detailed results.\n")


if __name__ == '__main__':
    main()
