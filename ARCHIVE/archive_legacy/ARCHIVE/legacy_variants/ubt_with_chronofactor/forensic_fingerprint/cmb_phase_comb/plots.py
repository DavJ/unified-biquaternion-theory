#!/usr/bin/env python3
"""
Visualization for CMB Phase-Comb Test Results
==============================================

Generate diagnostic plots:
- R(P) vs period curve
- Surrogate distributions
- P-value visualizations

License: MIT
Author: UBT Research Team
"""

import numpy as np
from pathlib import Path
from typing import Dict, Optional

try:
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False


def plot_phase_coherence_curve(results: Dict, output_dir: str,
                               filename: str = 'phase_coherence_curve.png') -> None:
    """
    Plot R(P) vs period with error bars from surrogates.
    
    Parameters
    ----------
    results : dict
        Results from run_phase_comb_test
    output_dir : str
        Output directory for plot
    filename : str
        Output filename (default: 'phase_coherence_curve.png')
    """
    if not MATPLOTLIB_AVAILABLE:
        print("WARNING: matplotlib not available, skipping plot")
        return
    
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    periods = results['periods']
    R_obs = [results['R_observed'][p] for p in periods]
    
    # Surrogate statistics
    surr_means = [results['surrogate_stats'][p]['mean'] for p in periods]
    surr_stds = [results['surrogate_stats'][p]['std'] for p in periods]
    surr_q95 = [results['surrogate_stats'][p]['q95'] for p in periods]
    surr_q99 = [results['surrogate_stats'][p]['q99'] for p in periods]
    
    # P-values
    p_values = [results['p_values'][p] for p in periods]
    
    # Create figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    # Top panel: R(P) curve
    ax1.plot(periods, R_obs, 'o-', color='red', linewidth=2, markersize=8, 
             label='Observed', zorder=10)
    ax1.plot(periods, surr_means, 's--', color='gray', linewidth=1, markersize=6,
             label='Surrogate mean')
    
    # Error bars (surrogate std)
    ax1.fill_between(periods, 
                     np.array(surr_means) - np.array(surr_stds),
                     np.array(surr_means) + np.array(surr_stds),
                     alpha=0.3, color='gray', label='Surrogate ±1σ')
    
    # 95% and 99% quantiles
    ax1.plot(periods, surr_q95, ':', color='orange', linewidth=1, label='Surrogate 95%')
    ax1.plot(periods, surr_q99, ':', color='red', linewidth=1, label='Surrogate 99%')
    
    ax1.set_ylabel('Phase Coherence R(P)', fontsize=12)
    ax1.set_title('CMB Phase-Comb Test Results', fontsize=14, fontweight='bold')
    ax1.legend(loc='best', fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(bottom=0)
    
    # Bottom panel: P-values
    ax2.semilogy(periods, p_values, 'o-', color='blue', linewidth=2, markersize=8)
    ax2.axhline(0.01, color='orange', linestyle='--', linewidth=1, label='p = 0.01 (candidate)')
    ax2.axhline(2.9e-7, color='red', linestyle='--', linewidth=1, label='p = 2.9e-7 (5σ)')
    
    # Highlight significant periods
    for i, period in enumerate(periods):
        if p_values[i] < 0.01:
            ax2.plot(period, p_values[i], 'o', color='red', markersize=12, 
                    markeredgecolor='darkred', markeredgewidth=2, zorder=20)
    
    ax2.set_xlabel('Period P', fontsize=12)
    ax2.set_ylabel('P-value', fontsize=12)
    ax2.legend(loc='best', fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(1e-8, 1)
    
    plt.tight_layout()
    
    output_path = output_dir / filename
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"Plot saved to: {output_path}")


def plot_surrogate_distributions(results: Dict, output_dir: str,
                                 filename: str = 'surrogate_distributions.png') -> None:
    """
    Plot histograms of R(P) from surrogates for each period.
    
    Parameters
    ----------
    results : dict
        Results from run_phase_comb_test (must include R_surrogates if available)
    output_dir : str
        Output directory
    filename : str
        Output filename
    """
    if not MATPLOTLIB_AVAILABLE:
        print("WARNING: matplotlib not available, skipping plot")
        return
    
    # This plot requires the full surrogate distributions
    # which are commented out in phase_comb.py to save space
    # For now, we'll skip this or implement a simplified version
    
    print("INFO: Surrogate distribution plot requires full R_surrogates data")
    print("      Enable by uncommenting 'R_surrogates' in phase_comb.py results")


def generate_all_plots(results: Dict, output_dir: str) -> None:
    """
    Generate all standard plots for phase-comb test.
    
    Parameters
    ----------
    results : dict
        Results from run_phase_comb_test
    output_dir : str
        Output directory for all plots
    """
    if not MATPLOTLIB_AVAILABLE:
        print("WARNING: matplotlib not available, skipping all plots")
        return
    
    print("Generating phase-comb diagnostic plots...")
    
    plot_phase_coherence_curve(results, output_dir)
    # plot_surrogate_distributions(results, output_dir)  # Requires full data
    
    print("Plot generation complete.")
