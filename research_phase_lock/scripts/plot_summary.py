#!/usr/bin/env python3
"""
plot_summary.py

Generate summary plots and visualizations from aggregated grid results.

Creates:
1. Phase coherence distributions by target k
2. P-value histograms
3. Parameter sweep plots (PC vs window_size, nside_out, etc.)
4. Volcano plots (effect size vs significance)
5. Twin prime comparison plots

Usage:
    python scripts/plot_summary.py --input results/summary.csv --output results/plots/
    python scripts/plot_summary.py --input results/summary.csv --output results/plots/ --format pdf

Author: UBT Research Team
License: See repository LICENSE.md
"""

import argparse
import csv
import sys
from pathlib import Path
from typing import List, Dict, Any
import numpy as np

# Add parent directory to path
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root))

try:
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("Warning: matplotlib not available, plotting disabled")


def load_summary_csv(csv_path):
    """Load aggregated summary CSV."""
    rows = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def plot_pc_distribution(data, output_dir, fmt='png'):
    """Plot phase coherence distributions by target k."""
    if not HAS_MATPLOTLIB:
        return
    
    # Group by target k
    k_groups = {}
    for row in data:
        k = row.get('k_target', 'unknown')
        try:
            pc = float(row.get('phase_coherence', 0))
            if k not in k_groups:
                k_groups[k] = []
            k_groups[k].append(pc)
        except (ValueError, TypeError):
            pass
    
    if not k_groups:
        print("No phase coherence data found")
        return
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot distributions
    positions = []
    labels = []
    data_to_plot = []
    
    for i, (k, pc_values) in enumerate(sorted(k_groups.items())):
        positions.append(i)
        labels.append(f"k={k}")
        data_to_plot.append(pc_values)
    
    # Box plot
    bp = ax.boxplot(data_to_plot, positions=positions, labels=labels,
                    patch_artist=True, widths=0.6)
    
    # Customize
    for patch in bp['boxes']:
        patch.set_facecolor('lightblue')
        patch.set_alpha(0.7)
    
    ax.set_ylabel('Phase Coherence', fontsize=12)
    ax.set_xlabel('Target k', fontsize=12)
    ax.set_title('Phase Coherence Distribution by Target k', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    ax.axhline(y=0.5, color='red', linestyle='--', alpha=0.5, label='PC = 0.5 threshold')
    ax.legend()
    
    plt.tight_layout()
    output_path = Path(output_dir) / f'pc_distribution.{fmt}'
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Saved: {output_path}")


def plot_pvalue_histogram(data, output_dir, fmt='png'):
    """Plot p-value histogram."""
    if not HAS_MATPLOTLIB:
        return
    
    # Extract p-values
    p_values = []
    for row in data:
        try:
            p = float(row.get('p_value', 1))
            if 0 <= p <= 1:
                p_values.append(p)
        except (ValueError, TypeError):
            pass
    
    if not p_values:
        print("No p-value data found")
        return
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Histogram
    ax.hist(p_values, bins=50, color='steelblue', alpha=0.7, edgecolor='black')
    
    # Add significance thresholds
    ax.axvline(x=0.01, color='red', linestyle='--', linewidth=2, label='p = 0.01')
    ax.axvline(x=0.05, color='orange', linestyle='--', linewidth=2, label='p = 0.05')
    
    ax.set_xlabel('P-value', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title('P-value Distribution (All Runs)', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Add statistics
    n_sig_01 = sum(1 for p in p_values if p <= 0.01)
    n_sig_05 = sum(1 for p in p_values if p <= 0.05)
    textstr = f'N = {len(p_values)}\np ≤ 0.01: {n_sig_01} ({100*n_sig_01/len(p_values):.1f}%)\np ≤ 0.05: {n_sig_05} ({100*n_sig_05/len(p_values):.1f}%)'
    ax.text(0.95, 0.95, textstr, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    output_path = Path(output_dir) / f'pvalue_histogram.{fmt}'
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Saved: {output_path}")


def plot_parameter_sweep(data, param_name, output_dir, fmt='png'):
    """Plot phase coherence vs a parameter."""
    if not HAS_MATPLOTLIB:
        return
    
    # Extract data
    param_key = f'config_{param_name}'
    points = []
    
    for row in data:
        try:
            param_val = row.get(param_key)
            if param_val is None:
                continue
            
            # Try to convert to numeric
            try:
                param_val = float(param_val)
            except:
                pass
            
            pc = float(row.get('phase_coherence', 0))
            p = float(row.get('p_value', 1))
            k = row.get('k_target', 'unknown')
            
            points.append({
                'param': param_val,
                'pc': pc,
                'p': p,
                'k': k
            })
        except (ValueError, TypeError):
            pass
    
    if not points:
        print(f"No data found for parameter: {param_name}")
        return
    
    # Group by k
    k_groups = {}
    for pt in points:
        k = pt['k']
        if k not in k_groups:
            k_groups[k] = []
        k_groups[k].append(pt)
    
    # Create figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    
    # Plot 1: PC vs parameter
    for k, group in sorted(k_groups.items()):
        params = [pt['param'] for pt in group]
        pcs = [pt['pc'] for pt in group]
        
        # Sort by param for line plot
        sorted_pairs = sorted(zip(params, pcs))
        params_sorted, pcs_sorted = zip(*sorted_pairs) if sorted_pairs else ([], [])
        
        ax1.scatter(params, pcs, alpha=0.5, s=50, label=f'k={k}')
        
        # Add trend line if numeric
        if params and isinstance(params[0], (int, float)):
            ax1.plot(params_sorted, pcs_sorted, alpha=0.3, linewidth=1)
    
    ax1.set_xlabel(param_name, fontsize=12)
    ax1.set_ylabel('Phase Coherence', fontsize=12)
    ax1.set_title(f'Phase Coherence vs {param_name}', fontsize=14, fontweight='bold')
    ax1.axhline(y=0.5, color='red', linestyle='--', alpha=0.5)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: P-value vs parameter
    for k, group in sorted(k_groups.items()):
        params = [pt['param'] for pt in group]
        ps = [pt['p'] for pt in group]
        
        ax2.scatter(params, ps, alpha=0.5, s=50, label=f'k={k}')
    
    ax2.set_xlabel(param_name, fontsize=12)
    ax2.set_ylabel('P-value', fontsize=12)
    ax2.set_title(f'P-value vs {param_name}', fontsize=14, fontweight='bold')
    ax2.axhline(y=0.01, color='red', linestyle='--', alpha=0.5)
    ax2.axhline(y=0.05, color='orange', linestyle='--', alpha=0.5)
    ax2.set_yscale('log')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_path = Path(output_dir) / f'sweep_{param_name}.{fmt}'
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Saved: {output_path}")


def plot_twin_prime_comparison(data, output_dir, fmt='png'):
    """Plot comparison between k=137 and k=139 (twin primes)."""
    if not HAS_MATPLOTLIB:
        return
    
    # Extract k=137 and k=139 data
    k137_data = [row for row in data if row.get('k_target') == '137']
    k139_data = [row for row in data if row.get('k_target') == '139']
    
    if not k137_data or not k139_data:
        print("Insufficient twin prime data (need both k=137 and k=139)")
        return
    
    # Create figure
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: PC comparison
    pc137 = [float(row.get('phase_coherence', 0)) for row in k137_data]
    pc139 = [float(row.get('phase_coherence', 0)) for row in k139_data]
    
    axes[0].scatter(pc137, pc139, alpha=0.5, s=50)
    axes[0].plot([0, 1], [0, 1], 'r--', alpha=0.5, label='PC_137 = PC_139')
    axes[0].set_xlabel('PC at k=137', fontsize=12)
    axes[0].set_ylabel('PC at k=139', fontsize=12)
    axes[0].set_title('Twin Prime Phase Coherence Comparison', fontsize=14, fontweight='bold')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    axes[0].set_aspect('equal')
    
    # Plot 2: Delta PC distribution
    min_len = min(len(pc137), len(pc139))
    delta_pc = [abs(pc137[i] - pc139[i]) for i in range(min_len)]
    
    axes[1].hist(delta_pc, bins=30, color='steelblue', alpha=0.7, edgecolor='black')
    axes[1].axvline(x=0.1, color='red', linestyle='--', linewidth=2, label='ΔPC = 0.1 threshold')
    axes[1].set_xlabel('|PC_137 - PC_139|', fontsize=12)
    axes[1].set_ylabel('Frequency', fontsize=12)
    axes[1].set_title('Twin Prime Phase Difference Distribution', fontsize=14, fontweight='bold')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    # Statistics
    mean_delta = np.mean(delta_pc)
    textstr = f'ΔPC mean: {mean_delta:.4f}\nN: {len(delta_pc)}'
    axes[1].text(0.95, 0.95, textstr, transform=axes[1].transAxes, fontsize=10,
                verticalalignment='top', horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    output_path = Path(output_dir) / f'twin_prime_comparison.{fmt}'
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Saved: {output_path}")


def create_summary_plots(input_csv, output_dir, fmt='png'):
    """Create all summary plots."""
    print("=" * 70)
    print("CREATING SUMMARY PLOTS")
    print("=" * 70)
    print(f"Input: {input_csv}")
    print(f"Output: {output_dir}")
    print(f"Format: {fmt}")
    print()
    
    if not HAS_MATPLOTLIB:
        print("ERROR: matplotlib not available, cannot create plots")
        return
    
    # Load data
    data = load_summary_csv(input_csv)
    print(f"Loaded {len(data)} rows")
    
    # Create output directory
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Generate plots
    print("\nGenerating plots...")
    
    plot_pc_distribution(data, output_dir, fmt)
    plot_pvalue_histogram(data, output_dir, fmt)
    plot_twin_prime_comparison(data, output_dir, fmt)
    
    # Parameter sweeps
    for param in ['window_size', 'nside_out', 'mc_samples']:
        plot_parameter_sweep(data, param, output_dir, fmt)
    
    print("\n" + "=" * 70)
    print("✓ All plots generated")
    print("=" * 70)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate Summary Plots from Phase-Lock Results",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--input',
        required=True,
        help='Input summary CSV file'
    )
    
    parser.add_argument(
        '--output',
        required=True,
        help='Output directory for plots'
    )
    
    parser.add_argument(
        '--format',
        default='png',
        choices=['png', 'pdf', 'svg'],
        help='Plot format (default: png)'
    )
    
    args = parser.parse_args()
    
    create_summary_plots(
        input_csv=args.input,
        output_dir=args.output,
        fmt=args.format
    )


if __name__ == '__main__':
    main()
