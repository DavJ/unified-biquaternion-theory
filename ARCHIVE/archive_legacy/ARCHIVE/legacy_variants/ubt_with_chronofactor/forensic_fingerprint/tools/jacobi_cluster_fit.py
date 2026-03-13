#!/usr/bin/env python3
"""
jacobi_cluster_fit.py

Fit Jacobi theta function θ₃ to the measured cluster k=134-143 in CMB TT channel data.

According to UBT, the dispersive imaginary scalar sector Θ̃_S evolves via:
    ∂_τ Θ̃_S = L_disp Θ̃_S

Solutions on the 8D torus are given by Jacobi theta functions θ₃(z,τ).
The composite numbers 141, 142 showing higher amplitude than twin primes 137, 139 in the TT 
channel is interpreted as a measurement of the dispersive parameter τ.

This script:
1. Loads radial FFT spectrum from cmb_fft2d_scan.py output CSV
2. Fits Jacobi theta function θ₃ to the cluster k=134-143
3. Estimates diffusion coefficient D from the fit
4. Generates diagnostic plots

Theoretical Background:
The Jacobi theta function θ₃ is defined as:
    θ₃(z, q) = Σ_{n=-∞}^{∞} q^{n²} exp(2πinz)

For the radial k-spectrum on a toroidal projection, the power spectral density follows:
    P(k) ∝ |θ₃(k/k₀, q)|²

where the nome parameter q = exp(-D·τ) encodes the diffusion coefficient D 
and dispersive evolution parameter τ.

Usage:
    python -m forensic_fingerprint.tools.jacobi_cluster_fit \\
        --input scans/tt_radial_dump.csv \\
        --output results/jacobi_fit_report.txt \\
        --plot results/jacobi_fit.png \\
        --k-min 134 --k-max 143
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import numpy as np


def _ensure_dir_for(path: Optional[str]) -> None:
    """Create directory for file path if needed."""
    if not path:
        return
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)


def jacobi_theta3(z: np.ndarray, q: float, n_terms: int = 100) -> np.ndarray:
    """
    Compute Jacobi theta function θ₃(z, q).
    
    θ₃(z, q) = Σ_{n=-n_terms}^{n_terms} q^{n²} exp(2πinz)
    
    Args:
        z: Complex or real input values
        q: Nome parameter (|q| < 1 for convergence)
        n_terms: Number of terms in the sum (default: 100)
    
    Returns:
        Complex or real values of θ₃(z, q)
    """
    z = np.asarray(z, dtype=complex)
    result = np.zeros_like(z, dtype=complex)
    
    for n in range(-n_terms, n_terms + 1):
        result += (q ** (n * n)) * np.exp(2j * np.pi * n * z)
    
    return result


def jacobi_theta3_power_spectrum(k: np.ndarray, k0: float, D: float, tau: float, 
                                   n_terms: int = 100) -> np.ndarray:
    """
    Power spectrum model based on Jacobi theta function.
    
    P(k) = |θ₃(k/k₀, exp(-D·τ))|²
    
    Args:
        k: Wavenumber array
        k0: Characteristic scale
        D: Diffusion coefficient
        tau: Dispersive evolution parameter
        n_terms: Number of terms in theta function
    
    Returns:
        Power spectrum values
    """
    z = k / k0
    q = np.exp(-D * tau)
    theta = jacobi_theta3(z, q, n_terms)
    return np.abs(theta) ** 2


@dataclass
class JacobiFitResult:
    """Results from Jacobi theta function fit."""
    k_data: np.ndarray
    psd_data: np.ndarray
    k0_fit: float
    D_fit: float
    tau_fit: float
    amplitude_fit: float
    psd_model: np.ndarray
    residuals: np.ndarray
    chi2: float
    chi2_reduced: float
    n_terms: int


def fit_jacobi_cluster(k_data: np.ndarray, psd_data: np.ndarray,
                       k_min: int = 134, k_max: int = 143,
                       initial_k0: float = 137.0,
                       initial_D: float = 0.01,
                       initial_tau: float = 1.0,
                       n_terms: int = 50) -> JacobiFitResult:
    """
    Fit Jacobi theta function to k-cluster data.
    
    Uses simple grid search followed by refinement for robustness.
    
    Args:
        k_data: Full k array
        psd_data: Full PSD array
        k_min: Minimum k for fit range
        k_max: Maximum k for fit range
        initial_k0: Initial guess for k0
        initial_D: Initial guess for D
        initial_tau: Initial guess for τ
        n_terms: Number of terms in theta function
    
    Returns:
        JacobiFitResult with fitted parameters
    """
    # Extract cluster data
    mask = (k_data >= k_min) & (k_data <= k_max)
    k_cluster = k_data[mask]
    psd_cluster = psd_data[mask]
    
    if len(k_cluster) == 0:
        raise ValueError(f"No data points in range k=[{k_min}, {k_max}]")
    
    # Normalize PSD to avoid numerical issues
    psd_max = np.max(psd_cluster)
    psd_norm = psd_cluster / psd_max
    
    # Simple grid search for initial parameters
    best_chi2 = float('inf')
    best_params = (initial_k0, initial_D, initial_tau, 1.0)
    
    # Grid search ranges
    k0_range = np.linspace(135, 140, 11)
    D_range = np.logspace(-3, -1, 11)  # 0.001 to 0.1
    tau_range = np.linspace(0.1, 2.0, 11)
    
    print(f"[jacobi_cluster_fit] Grid search over {len(k0_range)}×{len(D_range)}×{len(tau_range)} parameter combinations...")
    
    for k0 in k0_range:
        for D in D_range:
            for tau in tau_range:
                model = jacobi_theta3_power_spectrum(k_cluster, k0, D, tau, n_terms)
                
                # Fit amplitude
                amp = np.sum(psd_norm * model) / np.sum(model * model) if np.sum(model * model) > 0 else 1.0
                model_scaled = amp * model
                
                # Compute chi-squared
                residuals = psd_norm - model_scaled
                chi2 = np.sum(residuals ** 2)
                
                if chi2 < best_chi2:
                    best_chi2 = chi2
                    best_params = (k0, D, tau, amp * psd_max)
    
    k0_fit, D_fit, tau_fit, amp_fit = best_params
    
    print(f"[jacobi_cluster_fit] Best fit: k0={k0_fit:.2f}, D={D_fit:.6f}, τ={tau_fit:.4f}, amp={amp_fit:.6g}")
    
    # Generate final model
    psd_model = amp_fit * jacobi_theta3_power_spectrum(k_cluster, k0_fit, D_fit, tau_fit, n_terms)
    residuals = psd_cluster - psd_model
    chi2 = np.sum(residuals ** 2)
    
    # Degrees of freedom: n_data - n_params
    dof = len(k_cluster) - 4  # 4 parameters: k0, D, tau, amplitude
    chi2_reduced = chi2 / dof if dof > 0 else float('inf')
    
    return JacobiFitResult(
        k_data=k_cluster,
        psd_data=psd_cluster,
        k0_fit=k0_fit,
        D_fit=D_fit,
        tau_fit=tau_fit,
        amplitude_fit=amp_fit,
        psd_model=psd_model,
        residuals=residuals,
        chi2=chi2,
        chi2_reduced=chi2_reduced,
        n_terms=n_terms
    )


def load_radial_csv(path: str, channel: str = "TT") -> Tuple[np.ndarray, np.ndarray]:
    """
    Load radial spectrum from cmb_fft2d_scan.py dump CSV.
    
    Args:
        path: Path to CSV file
        channel: Channel name to filter (default: "TT")
    
    Returns:
        Tuple of (k_array, psd_array)
    """
    k_list = []
    psd_list = []
    
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['channel'] == channel:
                k = int(row['k'])
                psd = float(row['obs_psd'])
                if not np.isnan(psd):
                    k_list.append(k)
                    psd_list.append(psd)
    
    if not k_list:
        raise ValueError(f"No valid data for channel {channel} in {path}")
    
    return np.array(k_list), np.array(psd_list)


def write_fit_report(result: JacobiFitResult, output_path: str) -> None:
    """Write fit results to text file."""
    _ensure_dir_for(output_path)
    
    with open(output_path, 'w') as f:
        f.write("=" * 70 + "\n")
        f.write("UBT Jacobi Theta Function Cluster Fit Results\n")
        f.write("=" * 70 + "\n\n")
        
        f.write("FITTED PARAMETERS:\n")
        f.write(f"  k₀ (characteristic scale)    = {result.k0_fit:.4f} cycles/map\n")
        f.write(f"  D (diffusion coefficient)    = {result.D_fit:.8f}\n")
        f.write(f"  τ (dispersive parameter)     = {result.tau_fit:.6f}\n")
        f.write(f"  A (amplitude)                = {result.amplitude_fit:.6g}\n")
        f.write(f"  n_terms (theta expansion)    = {result.n_terms}\n\n")
        
        f.write("FIT QUALITY:\n")
        f.write(f"  χ²                           = {result.chi2:.6f}\n")
        f.write(f"  χ²/dof (reduced chi-squared) = {result.chi2_reduced:.6f}\n")
        f.write(f"  Number of data points        = {len(result.k_data)}\n")
        f.write(f"  Degrees of freedom           = {len(result.k_data) - 4}\n\n")
        
        f.write("PHYSICAL INTERPRETATION:\n")
        f.write(f"  Nome parameter q = exp(-D·τ) = {np.exp(-result.D_fit * result.tau_fit):.8f}\n")
        f.write(f"  Diffusion scale D·τ          = {result.D_fit * result.tau_fit:.8f}\n\n")
        
        f.write("DATA vs MODEL:\n")
        f.write(f"  {'k':>4} {'Observed':>12} {'Model':>12} {'Residual':>12} {'Rel.Error':>12}\n")
        f.write("  " + "-" * 56 + "\n")
        
        for i, k in enumerate(result.k_data):
            obs = result.psd_data[i]
            mod = result.psd_model[i]
            res = result.residuals[i]
            rel_err = res / obs if obs != 0 else float('nan')
            f.write(f"  {int(k):4d} {obs:12.6g} {mod:12.6g} {res:12.6g} {rel_err:12.4%}\n")
        
        f.write("\n" + "=" * 70 + "\n")
        f.write("NOTE: According to UBT, the TT channel measures the dispersive\n")
        f.write("imaginary scalar sector Θ̃_S, which evolves as a Jacobi theta\n")
        f.write("function on the 8D toroidal substrate. The fitted diffusion\n")
        f.write("coefficient D characterizes the rate of dispersive evolution\n")
        f.write("in complex time τ = t + iψ.\n")
        f.write("=" * 70 + "\n")


def plot_fit_results(result: JacobiFitResult, output_path: str) -> None:
    """Generate diagnostic plot of fit results."""
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print("[warn] matplotlib not available; skipping plot")
        return
    
    _ensure_dir_for(output_path)
    
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    
    # Top panel: Data and fit
    ax1 = axes[0]
    ax1.plot(result.k_data, result.psd_data, 'o', label='Observed PSD', 
             markersize=8, color='blue', alpha=0.7)
    ax1.plot(result.k_data, result.psd_model, '-', label='Jacobi θ₃ fit',
             linewidth=2, color='red')
    
    # Highlight twin primes
    for k_prime in [137, 139]:
        if k_prime in result.k_data:
            ax1.axvline(k_prime, color='green', linestyle='--', alpha=0.5, linewidth=1)
    
    ax1.set_xlabel('k (cycles per full map)', fontsize=11)
    ax1.set_ylabel('Power Spectral Density', fontsize=11)
    ax1.set_title(f'Jacobi Cluster Fit: k₀={result.k0_fit:.2f}, D={result.D_fit:.6f}, τ={result.tau_fit:.4f}',
                  fontsize=12, fontweight='bold')
    ax1.legend(loc='best', fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # Bottom panel: Residuals
    ax2 = axes[1]
    ax2.plot(result.k_data, result.residuals, 'o-', color='purple', markersize=6)
    ax2.axhline(0, color='black', linestyle='-', linewidth=1, alpha=0.5)
    ax2.set_xlabel('k (cycles per full map)', fontsize=11)
    ax2.set_ylabel('Residuals (Obs - Model)', fontsize=11)
    ax2.set_title(f'Fit Residuals (χ²/dof = {result.chi2_reduced:.4f})', fontsize=11)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close(fig)
    
    print(f"[info] wrote plot: {output_path}")


def main() -> None:
    """Main entry point."""
    ap = argparse.ArgumentParser(description=__doc__, 
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    
    ap.add_argument('--input', required=True, 
                    help='Input CSV from cmb_fft2d_scan.py --dump-radial-csv')
    ap.add_argument('--channel', default='TT',
                    help='Channel to analyze (default: TT)')
    ap.add_argument('--k-min', type=int, default=134,
                    help='Minimum k for fit cluster (default: 134)')
    ap.add_argument('--k-max', type=int, default=143,
                    help='Maximum k for fit cluster (default: 143)')
    ap.add_argument('--n-terms', type=int, default=50,
                    help='Number of terms in Jacobi theta expansion (default: 50)')
    ap.add_argument('--output', default='',
                    help='Output text file for fit report')
    ap.add_argument('--plot', default='',
                    help='Output PNG file for diagnostic plot')
    
    args = ap.parse_args()
    
    print(f"[jacobi_cluster_fit] Loading data from {args.input}...")
    k_data, psd_data = load_radial_csv(args.input, args.channel)
    
    print(f"[jacobi_cluster_fit] Loaded {len(k_data)} data points for channel {args.channel}")
    print(f"[jacobi_cluster_fit] k range: [{np.min(k_data)}, {np.max(k_data)}]")
    
    print(f"\n[jacobi_cluster_fit] Fitting Jacobi theta function to k=[{args.k_min}, {args.k_max}]...")
    result = fit_jacobi_cluster(
        k_data, psd_data,
        k_min=args.k_min,
        k_max=args.k_max,
        n_terms=args.n_terms
    )
    
    print("\n" + "=" * 70)
    print("FIT RESULTS:")
    print("=" * 70)
    print(f"  k₀                    = {result.k0_fit:.4f} cycles/map")
    print(f"  D (diffusion coeff.)  = {result.D_fit:.8f}")
    print(f"  τ (dispersive param.) = {result.tau_fit:.6f}")
    print(f"  amplitude             = {result.amplitude_fit:.6g}")
    print(f"  χ²/dof                = {result.chi2_reduced:.6f}")
    print("=" * 70 + "\n")
    
    if args.output:
        write_fit_report(result, args.output)
        print(f"[info] wrote report: {args.output}")
    
    if args.plot:
        plot_fit_results(result, args.plot)
    
    print("\n[jacobi_cluster_fit] Complete.")


if __name__ == '__main__':
    main()
