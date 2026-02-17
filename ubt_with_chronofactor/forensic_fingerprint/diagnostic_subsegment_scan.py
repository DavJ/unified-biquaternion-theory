#!/usr/bin/env python3
"""
UBT Forensic Fingerprint - Diagnostic Sub-segment Scan on Planck PR3 Residuals
===============================================================================

This script performs a detailed diagnostic analysis to test whether the detected
period Δℓ = 16 is a sub-harmonic of the predicted period Δℓ = 256 (multiplex scaling).

Analysis includes:
1. Sub-harmonic relationship testing (Δℓ = 16 vs Δℓ = 255/256)
2. ℓ-windowed analysis (increments of 200) to check signal strength variation
3. Phase-drift term analysis to compute χ² improvement

The predicted Δℓ = 256 comes from Reed-Solomon code architecture.
Observed detection of Δℓ = 16 suggests it may be a 1/16th sub-harmonic.

License: MIT
Author: UBT Research Team
Date: January 2026
"""

import numpy as np
import sys
import argparse
from pathlib import Path
from datetime import datetime
import json

# Import existing CMB comb infrastructure
try:
    from cmb_comb.cmb_comb import (
        compute_residuals,
        fit_sinusoid_linear,
        compute_delta_chi2,
        monte_carlo_null_distribution
    )
except ImportError:
    # Try relative import
    sys.path.insert(0, str(Path(__file__).parent))
    from cmb_comb.cmb_comb import (
        compute_residuals,
        fit_sinusoid_linear,
        compute_delta_chi2,
        monte_carlo_null_distribution
    )

# Import Planck data loader
try:
    from loaders.planck import load_planck_data
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from loaders.planck import load_planck_data


# =============================================================================
# Analysis Parameters
# =============================================================================

# Periods to test
PERIOD_PREDICTED = 256  # Predicted RS code period
PERIOD_DETECTED = 16    # Previously detected period
PERIOD_REFERENCE = 255  # Alternative (RS(255,223) code length)

# Windowed analysis parameters
WINDOW_SIZE = 200       # Multipole window size
WINDOW_STEP = 200       # Step size for sliding window (non-overlapping by default)

# Random seed for Monte Carlo
RANDOM_SEED = 42


def test_subharmonic_relationship(period_a, period_b):
    """
    Test if two periods have a sub-harmonic relationship.
    
    A sub-harmonic relationship exists if one period is an integer divisor
    or multiple of the other.
    
    Parameters
    ----------
    period_a : float
        First period
    period_b : float
        Second period
    
    Returns
    -------
    dict
        Dictionary with keys:
        - is_subharmonic: bool, True if sub-harmonic relationship exists
        - harmonic_ratio: float, ratio of periods
        - harmonic_order: int or None, integer harmonic order if exists
        - relationship_desc: str, description of relationship
    """
    ratio = period_a / period_b
    
    # Check if ratio is close to an integer
    harmonic_order = round(ratio)
    is_integer_harmonic = abs(ratio - harmonic_order) < 0.01
    
    # Check inverse ratio too
    inv_ratio = period_b / period_a
    inv_harmonic_order = round(inv_ratio)
    is_inverse_harmonic = abs(inv_ratio - inv_harmonic_order) < 0.01
    
    if is_integer_harmonic:
        relationship_desc = f"{period_a} = {harmonic_order} × {period_b}"
        is_subharmonic = True
        final_order = harmonic_order
    elif is_inverse_harmonic:
        relationship_desc = f"{period_b} = {inv_harmonic_order} × {period_a}"
        is_subharmonic = True
        final_order = inv_harmonic_order
    else:
        relationship_desc = f"No integer harmonic relationship (ratio = {ratio:.3f})"
        is_subharmonic = False
        final_order = None
    
    return {
        'is_subharmonic': is_subharmonic,
        'harmonic_ratio': float(ratio),
        'harmonic_order': final_order,
        'relationship_desc': relationship_desc
    }


def windowed_period_analysis(ell, residuals, period, window_size=WINDOW_SIZE, 
                             window_step=None, min_points=50):
    """
    Perform ℓ-windowed analysis to check if signal strength varies across multipole range.
    
    Divides the multipole range into windows and computes Δχ² for each window.
    This tests whether the periodic signal is uniform or varies with ℓ.
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    residuals : array-like
        Residual values
    period : float
        Period to test
    window_size : int
        Size of each window in multipole units (default: 200)
    window_step : int or None
        Step size between windows. If None, uses window_size (non-overlapping).
    min_points : int
        Minimum number of points required in a window (default: 50)
    
    Returns
    -------
    dict
        Dictionary with keys:
        - windows: list of dicts, each containing:
            - ell_range: tuple (ell_min, ell_max)
            - ell_center: float, center of window
            - n_points: int, number of points in window
            - delta_chi2: float, Δχ² for this window
            - amplitude: float, fitted amplitude
            - phase: float, fitted phase
            - chi2_per_dof: float, χ²/dof after removing sinusoid
        - period: float, period tested
        - window_size: int, window size used
        - window_step: int, step size used
        - n_windows: int, number of windows analyzed
        - signal_strength_variation: float, std dev of delta_chi2 across windows
    """
    if window_step is None:
        window_step = window_size
    
    ell = np.asarray(ell)
    residuals = np.asarray(residuals)
    
    ell_min = ell.min()
    ell_max = ell.max()
    
    windows = []
    
    # Iterate over windows
    current_start = ell_min
    while current_start < ell_max:
        current_end = current_start + window_size
        
        # Select data in this window
        mask = (ell >= current_start) & (ell < current_end)
        ell_window = ell[mask]
        residuals_window = residuals[mask]
        
        # Skip if too few points
        if len(ell_window) < min_points:
            current_start += window_step
            continue
        
        # Compute Δχ² for this window
        delta_chi2, amplitude, phase = compute_delta_chi2(
            ell_window, residuals_window, period
        )
        
        # Compute χ²/dof after removing sinusoid
        _, _, chi2_fit = fit_sinusoid_linear(ell_window, residuals_window, period)
        dof = len(ell_window) - 2  # 2 parameters fitted
        chi2_per_dof = chi2_fit / dof if dof > 0 else np.inf
        
        window_info = {
            'ell_range': (int(current_start), int(current_end)),
            'ell_center': float(current_start + window_size / 2),
            'n_points': int(len(ell_window)),
            'delta_chi2': float(delta_chi2),
            'amplitude': float(amplitude),
            'phase': float(phase),
            'chi2_per_dof': float(chi2_per_dof)
        }
        
        windows.append(window_info)
        
        # Move to next window
        current_start += window_step
    
    # Compute variation in signal strength
    if len(windows) > 1:
        delta_chi2_values = [w['delta_chi2'] for w in windows]
        signal_strength_variation = float(np.std(delta_chi2_values))
    else:
        signal_strength_variation = 0.0
    
    return {
        'windows': windows,
        'period': float(period),
        'window_size': int(window_size),
        'window_step': int(window_step),
        'n_windows': len(windows),
        'signal_strength_variation': signal_strength_variation
    }


def fit_sinusoid_with_phase_drift(ell, residuals, period):
    """
    Fit sinusoid with linear phase drift: r_ℓ ≈ A sin(2πℓ/Δℓ + φ₀ + φ₁·ℓ)
    
    This tests whether the phase of the oscillation drifts linearly with ℓ,
    which could indicate:
    - Non-stationary periodicity
    - Frequency chirp
    - Transition between different period regimes
    
    Parameterize as: r_ℓ = a cos(θ) + b sin(θ) + c ℓ cos(θ) + d ℓ sin(θ)
    where θ = 2πℓ/Δℓ
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    residuals : array-like
        Residual values
    period : float
        Base period Δℓ
    
    Returns
    -------
    dict
        Dictionary with keys:
        - amplitude: float, base amplitude A
        - phase_0: float, initial phase φ₀
        - phase_drift: float, phase drift rate φ₁ (radians per multipole)
        - chi2_fit: float, χ² of fit
        - chi2_improvement: float, improvement over non-drift model
        - params: dict, all fitted parameters (a, b, c, d)
    """
    # Design matrix: [cos(θ), sin(θ), ℓ·cos(θ), ℓ·sin(θ)]
    theta = 2.0 * np.pi * ell / period
    X = np.column_stack([
        np.cos(theta),
        np.sin(theta),
        ell * np.cos(theta),
        ell * np.sin(theta)
    ])
    
    # Least squares fit
    params, _, _, _ = np.linalg.lstsq(X, residuals, rcond=None)
    a, b, c, d = params
    
    # Compute fit
    fit = (a + c * ell) * np.cos(theta) + (b + d * ell) * np.sin(theta)
    chi2_fit = np.sum((residuals - fit)**2)
    
    # Base amplitude and phase (at ℓ=0)
    amplitude_0 = np.sqrt(a**2 + b**2)
    phase_0 = np.arctan2(b, a)
    
    # Phase drift rate (approximate for small drift)
    # φ(ℓ) ≈ φ₀ + φ₁·ℓ where φ₁ comes from c and d
    phase_drift = np.sqrt(c**2 + d**2) / amplitude_0 if amplitude_0 > 0 else 0.0
    
    # Compare with non-drift model
    _, _, chi2_nodrift = fit_sinusoid_linear(ell, residuals, period)
    chi2_improvement = chi2_nodrift - chi2_fit
    
    return {
        'amplitude': float(amplitude_0),
        'phase_0': float(phase_0),
        'phase_drift': float(phase_drift),
        'chi2_fit': float(chi2_fit),
        'chi2_improvement': float(chi2_improvement),
        'params': {
            'a': float(a),
            'b': float(b),
            'c': float(c),
            'd': float(d)
        }
    }


def run_diagnostic_scan(ell, cl_obs, cl_model, sigma, cov=None, 
                       whiten_mode='diagonal', output_dir=None):
    """
    Run complete diagnostic sub-segment scan.
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    cl_obs : array-like
        Observed power spectrum
    cl_model : array-like
        Model power spectrum
    sigma : array-like
        Uncertainties
    cov : array-like, optional
        Covariance matrix
    whiten_mode : str
        Whitening mode ('diagonal', 'covariance', etc.)
    output_dir : str or Path, optional
        Directory to save results
    
    Returns
    -------
    dict
        Complete diagnostic results
    """
    print("=" * 80)
    print("DIAGNOSTIC SUB-SEGMENT SCAN ON PLANCK PR3 RESIDUALS")
    print("=" * 80)
    print()
    
    # Compute residuals
    print("Computing residuals...")
    residuals, res_metadata = compute_residuals(
        ell, cl_obs, cl_model, sigma, cov=cov, whiten_mode=whiten_mode
    )
    print(f"  Whitening mode: {whiten_mode}")
    print(f"  χ²/dof: {res_metadata['chi2_per_dof']:.2f}")
    print()
    
    # Test 1: Sub-harmonic relationship
    print("-" * 80)
    print("TEST 1: SUB-HARMONIC RELATIONSHIP")
    print("-" * 80)
    
    print(f"\nTesting relationship between detected Δℓ={PERIOD_DETECTED} and predicted Δℓ={PERIOD_PREDICTED}...")
    subharmonic_256 = test_subharmonic_relationship(PERIOD_PREDICTED, PERIOD_DETECTED)
    print(f"  {subharmonic_256['relationship_desc']}")
    print(f"  Is sub-harmonic: {subharmonic_256['is_subharmonic']}")
    if subharmonic_256['harmonic_order'] is not None:
        print(f"  Harmonic order: {subharmonic_256['harmonic_order']}")
    
    print(f"\nTesting relationship between detected Δℓ={PERIOD_DETECTED} and alternative Δℓ={PERIOD_REFERENCE}...")
    subharmonic_255 = test_subharmonic_relationship(PERIOD_REFERENCE, PERIOD_DETECTED)
    print(f"  {subharmonic_255['relationship_desc']}")
    print(f"  Is sub-harmonic: {subharmonic_255['is_subharmonic']}")
    if subharmonic_255['harmonic_order'] is not None:
        print(f"  Harmonic order: {subharmonic_255['harmonic_order']}")
    print()
    
    # Test 2: Full multipole range analysis for all periods
    print("-" * 80)
    print("TEST 2: PERIOD STRENGTH COMPARISON (FULL RANGE)")
    print("-" * 80)
    print()
    
    periods_to_test = [PERIOD_DETECTED, PERIOD_REFERENCE, PERIOD_PREDICTED]
    period_results = {}
    
    for period in periods_to_test:
        delta_chi2, amplitude, phase = compute_delta_chi2(ell, residuals, period)
        period_results[period] = {
            'delta_chi2': float(delta_chi2),
            'amplitude': float(amplitude),
            'phase': float(phase)
        }
        print(f"Period Δℓ = {period}:")
        print(f"  Δχ² = {delta_chi2:.2f}")
        print(f"  Amplitude = {amplitude:.4f}")
        print(f"  Phase = {phase:.4f} rad")
        print()
    
    # Test 3: Windowed analysis
    print("-" * 80)
    print("TEST 3: ℓ-WINDOWED ANALYSIS")
    print("-" * 80)
    print(f"\nWindow size: {WINDOW_SIZE} multipoles")
    print(f"Testing period Δℓ = {PERIOD_REFERENCE} in sliding windows...")
    print()
    
    windowed_results = windowed_period_analysis(
        ell, residuals, PERIOD_REFERENCE, 
        window_size=WINDOW_SIZE, window_step=WINDOW_STEP
    )
    
    print(f"Number of windows: {windowed_results['n_windows']}")
    print(f"Signal strength variation (std): {windowed_results['signal_strength_variation']:.2f}")
    print()
    print("Window-by-window results:")
    print(f"{'ℓ-range':<20} {'N pts':<8} {'Δχ²':<12} {'Amplitude':<12} {'χ²/dof':<10}")
    print("-" * 70)
    
    for w in windowed_results['windows']:
        ell_range_str = f"{w['ell_range'][0]}-{w['ell_range'][1]}"
        print(f"{ell_range_str:<20} {w['n_points']:<8} {w['delta_chi2']:<12.2f} "
              f"{w['amplitude']:<12.4f} {w['chi2_per_dof']:<10.2f}")
    print()
    
    # Test 4: Phase drift analysis
    print("-" * 80)
    print("TEST 4: PHASE-DRIFT ANALYSIS")
    print("-" * 80)
    print(f"\nTesting if phase drifts linearly with ℓ for period Δℓ = {PERIOD_REFERENCE}...")
    print()
    
    phase_drift_results = fit_sinusoid_with_phase_drift(ell, residuals, PERIOD_REFERENCE)
    
    print(f"No-drift model:")
    no_drift_result = period_results[PERIOD_REFERENCE]
    _, _, chi2_nodrift = fit_sinusoid_linear(ell, residuals, PERIOD_REFERENCE)
    print(f"  Amplitude: {no_drift_result['amplitude']:.4f}")
    print(f"  Phase: {no_drift_result['phase']:.4f} rad")
    print(f"  χ² = {chi2_nodrift:.2f}")
    print()
    
    print(f"With phase-drift model:")
    print(f"  Base amplitude: {phase_drift_results['amplitude']:.4f}")
    print(f"  Initial phase: {phase_drift_results['phase_0']:.4f} rad")
    print(f"  Phase drift rate: {phase_drift_results['phase_drift']:.6f} rad/multipole")
    print(f"  χ² = {phase_drift_results['chi2_fit']:.2f}")
    print()
    
    print(f"χ² improvement from phase drift: {phase_drift_results['chi2_improvement']:.2f}")
    
    # Compute degrees of freedom
    n_data = len(ell)
    dof_nodrift = n_data - 2  # 2 parameters (amplitude, phase)
    dof_drift = n_data - 4     # 4 parameters (a, b, c, d)
    delta_dof = 2
    
    # F-test for significance of phase drift
    F_stat = (phase_drift_results['chi2_improvement'] / delta_dof) / (phase_drift_results['chi2_fit'] / dof_drift)
    print(f"F-statistic (2, {dof_drift} dof): {F_stat:.2f}")
    
    # Rough significance assessment
    if F_stat > 5.0:
        print("  → Phase drift is SIGNIFICANT (F > 5)")
    elif F_stat > 2.0:
        print("  → Phase drift is MARGINAL (F > 2)")
    else:
        print("  → Phase drift is NOT SIGNIFICANT (F < 2)")
    print()
    
    # Assemble complete results
    results = {
        'timestamp': datetime.now().isoformat(),
        'ell_range': (int(ell.min()), int(ell.max())),
        'n_multipoles': len(ell),
        'whiten_mode': whiten_mode,
        'chi2_per_dof_residuals': res_metadata['chi2_per_dof'],
        'subharmonic_tests': {
            '256_vs_16': subharmonic_256,
            '255_vs_16': subharmonic_255
        },
        'period_comparison': period_results,
        'windowed_analysis': windowed_results,
        'phase_drift_analysis': phase_drift_results,
        'phase_drift_f_stat': float(F_stat)
    }
    
    # Save results if output directory specified
    if output_dir is not None:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = output_dir / f"diagnostic_scan_{timestamp}.json"
        
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print("=" * 80)
        print(f"Results saved to: {output_file}")
        print("=" * 80)
    
    return results


def main():
    """Main entry point for diagnostic scan."""
    parser = argparse.ArgumentParser(
        description='Diagnostic sub-segment scan on Planck PR3 residuals',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument('--planck_obs', type=str, required=True,
                       help='Path to Planck observed spectrum file')
    parser.add_argument('--planck_model', type=str, required=True,
                       help='Path to Planck model spectrum file')
    parser.add_argument('--planck_cov', type=str, default=None,
                       help='Path to Planck covariance matrix (optional)')
    parser.add_argument('--ell_min', type=int, default=30,
                       help='Minimum multipole (default: 30)')
    parser.add_argument('--ell_max', type=int, default=1500,
                       help='Maximum multipole (default: 1500)')
    parser.add_argument('--whiten_mode', type=str, default='diagonal',
                       choices=['none', 'diagonal', 'covariance', 'cov_diag'],
                       help='Whitening mode (default: diagonal)')
    parser.add_argument('--window_size', type=int, default=200,
                       help='Window size for windowed analysis (default: 200)')
    parser.add_argument('--window_step', type=int, default=None,
                       help='Step size for sliding windows (default: same as window_size)')
    parser.add_argument('--output_dir', type=str, default='./diagnostic_results',
                       help='Output directory for results (default: ./diagnostic_results)')
    
    args = parser.parse_args()
    
    # Update global parameters
    global WINDOW_SIZE, WINDOW_STEP
    WINDOW_SIZE = args.window_size
    if args.window_step is not None:
        WINDOW_STEP = args.window_step
    else:
        WINDOW_STEP = WINDOW_SIZE
    
    # Load Planck data
    print("Loading Planck PR3 data...")
    print(f"  Observation: {args.planck_obs}")
    print(f"  Model: {args.planck_model}")
    if args.planck_cov:
        print(f"  Covariance: {args.planck_cov}")
    print()
    
    try:
        data = load_planck_data(
            obs_file=args.planck_obs,
            model_file=args.planck_model,
            cov_file=args.planck_cov,
            ell_min=args.ell_min,
            ell_max=args.ell_max,
            dataset_name="Planck PR3",
            spectrum_type="TT"
        )
    except Exception as e:
        print(f"ERROR: Failed to load Planck data: {e}")
        return 1
    
    print(f"Data loaded successfully:")
    print(f"  Multipole range: {data['ell_range']}")
    print(f"  Number of multipoles: {data['n_multipoles']}")
    print(f"  Has covariance: {data['cov'] is not None}")
    print()
    
    # Run diagnostic scan
    results = run_diagnostic_scan(
        ell=data['ell'],
        cl_obs=data['cl_obs'],
        cl_model=data['cl_model'],
        sigma=data['sigma'],
        cov=data['cov'],
        whiten_mode=args.whiten_mode,
        output_dir=args.output_dir
    )
    
    print()
    print("=" * 80)
    print("DIAGNOSTIC SCAN COMPLETE")
    print("=" * 80)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
