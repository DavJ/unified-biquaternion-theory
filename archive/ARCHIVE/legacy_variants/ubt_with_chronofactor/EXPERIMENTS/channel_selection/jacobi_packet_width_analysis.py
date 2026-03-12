#!/usr/bin/env python3
"""
jacobi_packet_width_analysis.py

Verify whether the Jacobi kernel (Layer 1) generates natural energy packets
around certain modes. Analyzes theta function dispersion and Gaussian envelope widths.

This module numerically simulates theta function behavior without modifying
core UBT theory.

Usage:
    python jacobi_packet_width_analysis.py --center 137 --width 20
    python jacobi_packet_width_analysis.py --config config.yaml

Author: UBT Research Team
License: See repository LICENSE.md
"""

import argparse
import csv
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Optional

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("Warning: matplotlib not available, plots will be skipped")


def jacobi_theta_3(z: complex, q: complex, terms: int = 50) -> complex:
    """
    Compute Jacobi theta function θ₃(z, q).
    
    θ₃(z, q) = 1 + 2∑(n=1 to ∞) qⁿ² cos(2nz)
    
    Args:
        z: Argument
        q: Nome parameter (|q| < 1)
        terms: Number of terms in series
        
    Returns:
        Theta function value
    """
    result = 1.0 + 0.0j
    
    for n in range(1, terms + 1):
        result += 2 * (q ** (n * n)) * np.cos(2 * n * z)
    
    return result


def simulate_theta_dispersion(n_center: int, n_width: int = 20,
                              tau: float = 0.1) -> Tuple[np.ndarray, np.ndarray]:
    """
    Simulate theta function dispersion around a central mode.
    
    Args:
        n_center: Central mode number
        n_width: Width of scan around center
        tau: Imaginary time parameter
        
    Returns:
        (modes, amplitudes) arrays
    """
    # Create mode range
    n_min = max(1, n_center - n_width)
    n_max = n_center + n_width
    modes = np.arange(n_min, n_max + 1)
    
    # Compute theta function amplitude for each mode
    # Using simplified model: amplitude ~ θ₃(πn/n_center, e^(-πτ))
    q = np.exp(-np.pi * tau)
    amplitudes = np.zeros(len(modes))
    
    for i, n in enumerate(modes):
        z = np.pi * n / n_center
        theta_val = jacobi_theta_3(z, q, terms=30)
        amplitudes[i] = abs(theta_val)
    
    return modes, amplitudes


def fit_gaussian_envelope(modes: np.ndarray, amplitudes: np.ndarray) -> Dict[str, float]:
    """
    Fit Gaussian envelope to amplitude distribution.
    
    A(n) ~ A₀ exp(-(n - n₀)² / (2σ²))
    
    Args:
        modes: Array of mode numbers
        amplitudes: Array of amplitudes
        
    Returns:
        Dictionary with fit parameters {A0, n0, sigma}
    """
    # Log of amplitudes for linear fit
    log_amp = np.log(amplitudes + 1e-10)  # Avoid log(0)
    
    # Find peak
    peak_idx = np.argmax(amplitudes)
    n0 = modes[peak_idx]
    A0 = amplitudes[peak_idx]
    
    # Estimate sigma from width at half maximum
    half_max = A0 / 2
    above_half = amplitudes >= half_max
    if np.any(above_half):
        indices = np.where(above_half)[0]
        fwhm = modes[indices[-1]] - modes[indices[0]]
        sigma = fwhm / (2 * np.sqrt(2 * np.log(2)))
    else:
        sigma = 5.0  # Default
    
    return {
        'A0': A0,
        'n0': n0,
        'sigma': sigma,
        'fwhm': 2.35 * sigma  # Full width at half maximum
    }


def analyze_packet_width(n_center: int, n_width: int = 20,
                         output_dir: Optional[str] = None) -> Dict[str, float]:
    """
    Analyze packet width around a central mode.
    
    Args:
        n_center: Central mode number
        n_width: Scan width
        output_dir: Optional output directory
        
    Returns:
        Analysis results dictionary
    """
    print(f"\nAnalyzing packet around n={n_center}...")
    
    # Simulate dispersion
    modes, amplitudes = simulate_theta_dispersion(n_center, n_width)
    
    # Fit Gaussian
    fit_params = fit_gaussian_envelope(modes, amplitudes)
    
    print(f"  Peak amplitude: {fit_params['A0']:.4f}")
    print(f"  Peak position: {fit_params['n0']:.1f}")
    print(f"  Gaussian width σ: {fit_params['sigma']:.2f}")
    print(f"  FWHM: {fit_params['fwhm']:.2f}")
    
    # Save plot if matplotlib available
    if HAS_MATPLOTLIB and output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Plot
        fig, ax = plt.subplots(figsize=(10, 6))
        
        ax.plot(modes, amplitudes, 'o-', label='Simulated θ₃ amplitude')
        
        # Gaussian fit
        n_fine = np.linspace(modes[0], modes[-1], 200)
        gaussian_fit = fit_params['A0'] * np.exp(
            -(n_fine - fit_params['n0'])**2 / (2 * fit_params['sigma']**2)
        )
        ax.plot(n_fine, gaussian_fit, '--', label=f'Gaussian fit (σ={fit_params["sigma"]:.2f})', 
                color='red')
        
        ax.axvline(n_center, color='gray', linestyle=':', label=f'n={n_center}')
        ax.set_xlabel('Mode number n', fontsize=12)
        ax.set_ylabel('Amplitude', fontsize=12)
        ax.set_title(f'Jacobi Theta Packet Width Analysis (n={n_center})', fontsize=13)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plot_path = output_path / f'packet_width_n{n_center}.png'
        plt.savefig(plot_path, dpi=150)
        print(f"  Plot saved to {plot_path}")
        plt.close()
    
    return fit_params


def scan_multiple_centers(centers: List[int], n_width: int = 20,
                          output_dir: Optional[str] = None) -> Dict[int, Dict[str, float]]:
    """
    Scan packet widths for multiple centers.
    
    Args:
        centers: List of central mode numbers
        n_width: Scan width for each center
        output_dir: Optional output directory
        
    Returns:
        Dictionary mapping center to fit parameters
    """
    print("=" * 70)
    print("JACOBI PACKET WIDTH ANALYSIS")
    print("=" * 70)
    
    results = {}
    
    for n_center in centers:
        fit_params = analyze_packet_width(n_center, n_width, output_dir)
        results[n_center] = fit_params
    
    # Save summary
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        csv_path = output_path / 'packet_widths.csv'
        with open(csv_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['n_center', 'A0', 'n0', 'sigma', 'fwhm'])
            for n, params in results.items():
                writer.writerow([n, params['A0'], params['n0'], 
                               params['sigma'], params['fwhm']])
        
        print(f"\nSummary saved to {csv_path}")
    
    # Print summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"{'Center':>8s} {'σ':>10s} {'FWHM':>10s} {'Peak':>10s}")
    print("-" * 70)
    for n, params in results.items():
        print(f"{n:8d} {params['sigma']:10.2f} {params['fwhm']:10.2f} {params['A0']:10.4f}")
    
    return results


def correlate_with_primes(centers: List[int], results: Dict[int, Dict[str, float]]) -> None:
    """
    Check if packet width minima correlate with prime modes.
    
    Args:
        centers: List of analyzed centers
        results: Analysis results
    """
    from interference_functional import is_prime
    
    print("\n" + "=" * 70)
    print("CORRELATION WITH PRIME MODES")
    print("=" * 70)
    
    # Separate primes and composites
    primes = {n: results[n] for n in centers if is_prime(n)}
    composites = {n: results[n] for n in centers if not is_prime(n)}
    
    if primes and composites:
        prime_widths = [params['sigma'] for params in primes.values()]
        composite_widths = [params['sigma'] for params in composites.values()]
        
        print(f"\nPrimes ({len(primes)} modes):")
        print(f"  Mean σ: {np.mean(prime_widths):.2f}")
        print(f"  Std σ:  {np.std(prime_widths):.2f}")
        
        print(f"\nComposites ({len(composites)} modes):")
        print(f"  Mean σ: {np.mean(composite_widths):.2f}")
        print(f"  Std σ:  {np.std(composite_widths):.2f}")
        
        print(f"\nDifference (Composite - Prime): {np.mean(composite_widths) - np.mean(prime_widths):.2f}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Analyze Jacobi theta packet widths'
    )
    parser.add_argument('--center', type=int, default=137,
                        help='Central mode number (default: 137)')
    parser.add_argument('--centers', type=int, nargs='+',
                        help='Multiple centers to analyze')
    parser.add_argument('--width', type=int, default=20,
                        help='Scan width around center (default: 20)')
    parser.add_argument('--output', type=str, default='results/jacobi_packets',
                        help='Output directory')
    
    args = parser.parse_args()
    
    # Determine centers to analyze
    if args.centers:
        centers = args.centers
    else:
        # Default: scan around primes near 137
        centers = [127, 131, 137, 139, 149, 151, 157]
    
    # Run analysis
    results = scan_multiple_centers(centers, args.width, args.output)
    
    # Correlate with primes
    correlate_with_primes(centers, results)


if __name__ == '__main__':
    main()
