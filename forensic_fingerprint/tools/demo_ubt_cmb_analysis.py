#!/usr/bin/env python3
"""
demo_ubt_cmb_analysis.py

Demonstration workflow for UBT CMB spectral forensic analysis using synthetic data.

This script demonstrates the complete analysis pipeline:
1. Generate synthetic CMB-like data with UBT signatures
2. Run Jacobi theta function fitting on TT cluster
3. Analyze cross-channel phase coherence
4. Generate reports and visualizations

Usage:
    python demo_ubt_cmb_analysis.py --output-dir demo_results/
"""

from __future__ import annotations

import argparse
import csv
import os
from typing import Tuple

import numpy as np

# Import our analysis tools
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from forensic_fingerprint.tools.jacobi_cluster_fit import (
    jacobi_theta3_power_spectrum,
    fit_jacobi_cluster,
    write_fit_report,
    plot_fit_results,
)

from forensic_fingerprint.tools.cross_channel_phase_coherence import (
    compute_phase_coherence,
)


def generate_synthetic_spectrum(
    k_min: int = 100,
    k_max: int = 200,
    k0_tt: float = 137.0,
    D: float = 0.012,
    tau: float = 1.5,
    k_bb: int = 139,
    noise_level: float = 0.05,
    seed: int = 42
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Generate synthetic radial power spectrum with UBT signatures.
    
    Returns:
        k_array: Wavenumber array
        psd_tt: TT channel power spectrum (Jacobi cluster)
        psd_bb: BB channel power spectrum (sharp peak at k=139)
    """
    rng = np.random.default_rng(seed)
    
    k_array = np.arange(k_min, k_max + 1, dtype=float)
    
    # TT channel: Jacobi theta function cluster
    psd_tt_signal = 1000.0 * jacobi_theta3_power_spectrum(k_array, k0_tt, D, tau, n_terms=50)
    
    # Add smooth background
    psd_tt_bg = 500.0 * np.exp(-((k_array - 137.0) / 50.0) ** 2)
    
    # Add noise
    psd_tt_noise = rng.normal(0, noise_level * np.max(psd_tt_signal), size=len(k_array))
    psd_tt = psd_tt_signal + psd_tt_bg + np.abs(psd_tt_noise)
    
    # BB channel: Sharp Lorentzian peak at k=139
    gamma = 2.0  # width
    psd_bb_signal = 2000.0 / (1.0 + ((k_array - k_bb) / gamma) ** 2)
    
    # Add smooth background
    psd_bb_bg = 200.0 * np.exp(-((k_array - 139.0) / 60.0) ** 2)
    
    # Add noise
    psd_bb_noise = rng.normal(0, noise_level * np.max(psd_bb_signal), size=len(k_array))
    psd_bb = psd_bb_signal + psd_bb_bg + np.abs(psd_bb_noise)
    
    return k_array, psd_tt, psd_bb


def generate_synthetic_phases(
    n_modes: int = 50,
    coherence: float = 0.85,
    phase_offset: float = 0.3,
    seed: int = 42
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate synthetic phases with controlled coherence.
    
    Args:
        n_modes: Number of modes
        coherence: Target coherence (0=random, 1=perfect lock)
        phase_offset: Mean phase difference in radians
        seed: Random seed
    
    Returns:
        phases_tt: TT channel phases
        phases_bb: BB channel phases
    """
    rng = np.random.default_rng(seed)
    
    # Generate base phases
    base_phases = rng.uniform(-np.pi, np.pi, n_modes)
    
    # TT phases: base + small noise
    phases_tt = base_phases + rng.normal(0, 0.1, n_modes)
    
    # BB phases: coherent component + random component
    coherent_component = base_phases + phase_offset
    random_component = rng.uniform(-np.pi, np.pi, n_modes)
    
    # Mix based on target coherence
    phases_bb = coherence * coherent_component + (1 - coherence) * random_component
    
    return phases_tt, phases_bb


def write_synthetic_csv(path: str, k_array: np.ndarray, psd: np.ndarray, channel: str) -> None:
    """Write synthetic spectrum to CSV in cmb_fft2d_scan format."""
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else '.', exist_ok=True)
    
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'channel', 'nside_out', 'nlat', 'nlon', 'lat_cut_deg', 'field', 
            'window2d', 'radial', 'null', 'mc', 'seed', 'k', 'obs_psd',
            'mc_mean', 'mc_std', 'z', 'p_tail'
        ])
        
        for k, p in zip(k_array, psd):
            writer.writerow([
                channel, 256, 512, 1024, 0.0, 'value', 'none', 'True', '', 0, 0,
                int(k), float(p), '', '', '', ''
            ])


def main() -> None:
    """Main demonstration workflow."""
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--output-dir', default='demo_results/',
                    help='Output directory for results (default: demo_results/)')
    ap.add_argument('--seed', type=int, default=42,
                    help='Random seed (default: 42)')
    
    args = ap.parse_args()
    
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)
    
    print("=" * 70)
    print("UBT CMB Spectral Forensic Analysis - Demo Workflow")
    print("=" * 70)
    print()
    
    # Step 1: Generate synthetic data
    print("[1/4] Generating synthetic CMB-like spectra with UBT signatures...")
    k_array, psd_tt, psd_bb = generate_synthetic_spectrum(seed=args.seed)
    
    # Save synthetic spectra
    tt_csv = os.path.join(output_dir, 'synthetic_tt_spectrum.csv')
    bb_csv = os.path.join(output_dir, 'synthetic_bb_spectrum.csv')
    write_synthetic_csv(tt_csv, k_array, psd_tt, 'TT')
    write_synthetic_csv(bb_csv, k_array, psd_bb, 'BB')
    
    print(f"  ✓ Generated TT spectrum: {len(k_array)} k-modes")
    print(f"  ✓ Generated BB spectrum: {len(k_array)} k-modes")
    print(f"  ✓ Saved to {output_dir}")
    print()
    
    # Step 2: Fit Jacobi theta function to TT cluster
    print("[2/4] Fitting Jacobi theta function to TT cluster (k=134-143)...")
    fit_result = fit_jacobi_cluster(
        k_data=k_array,
        psd_data=psd_tt,
        k_min=134,
        k_max=143,
        n_terms=50
    )
    
    # Write fit report
    fit_report = os.path.join(output_dir, 'jacobi_fit_report.txt')
    fit_plot = os.path.join(output_dir, 'jacobi_fit.png')
    write_fit_report(fit_result, fit_report)
    plot_fit_results(fit_result, fit_plot)
    
    print(f"  ✓ Fitted parameters:")
    print(f"     k₀ = {fit_result.k0_fit:.4f} cycles/map")
    print(f"     D  = {fit_result.D_fit:.8f}")
    print(f"     τ  = {fit_result.tau_fit:.6f}")
    print(f"     χ²/dof = {fit_result.chi2_reduced:.6f}")
    print(f"  ✓ Report: {fit_report}")
    print(f"  ✓ Plot: {fit_plot}")
    print()
    
    # Step 3: Analyze phase coherence
    print("[3/4] Analyzing cross-channel phase coherence...")
    phases_tt, phases_bb = generate_synthetic_phases(
        n_modes=50,
        coherence=0.85,
        phase_offset=0.3,
        seed=args.seed
    )
    
    coherence_obs, mean_diff, concentration = compute_phase_coherence(phases_tt, phases_bb)
    
    # Write phase coherence report
    phase_report = os.path.join(output_dir, 'phase_coherence_report.txt')
    with open(phase_report, 'w') as f:
        f.write("=" * 70 + "\n")
        f.write("UBT Cross-Channel Phase Coherence Analysis (Synthetic Data)\n")
        f.write("=" * 70 + "\n\n")
        f.write("COHERENCE METRICS:\n")
        f.write(f"  Observed coherence Γ         = {coherence_obs:.8f}\n")
        f.write(f"  Mean phase difference ⟨Δφ⟩   = {mean_diff:.6f} rad")
        f.write(f" ({np.degrees(mean_diff):.2f}°)\n")
        f.write(f"  Phase concentration κ        = {concentration:.6f}\n\n")
        f.write("INTERPRETATION:\n")
        f.write(f"A coherence of {coherence_obs:.4f} indicates ")
        if coherence_obs > 0.7:
            f.write("STRONG phase lock between channels.\n")
        elif coherence_obs > 0.3:
            f.write("MODERATE phase correlation between channels.\n")
        else:
            f.write("WEAK or NO phase correlation between channels.\n")
        f.write("\nThis supports the UBT hypothesis that TT and BB channels\n")
        f.write("are projections of a unified biquaternion field.\n")
        f.write("=" * 70 + "\n")
    
    print(f"  ✓ Coherence Γ = {coherence_obs:.6f}")
    print(f"  ✓ Mean phase diff = {mean_diff:.4f} rad ({np.degrees(mean_diff):.2f}°)")
    print(f"  ✓ Concentration κ = {concentration:.4f}")
    print(f"  ✓ Report: {phase_report}")
    print()
    
    # Step 4: Summary
    print("[4/4] Summary:")
    print(f"  All results saved to: {os.path.abspath(output_dir)}")
    print()
    print("  Key findings (synthetic data):")
    print(f"    • TT cluster fitted with Jacobi θ₃: D={fit_result.D_fit:.6f}, τ={fit_result.tau_fit:.4f}")
    print(f"    • Cross-channel coherence: Γ={coherence_obs:.4f}")
    print(f"    • Phase lock detected: {'YES' if coherence_obs > 0.7 else 'MODERATE' if coherence_obs > 0.3 else 'NO'}")
    print()
    print("=" * 70)
    print("Demo complete! Check the output directory for detailed reports and plots.")
    print("=" * 70)


if __name__ == '__main__':
    main()
