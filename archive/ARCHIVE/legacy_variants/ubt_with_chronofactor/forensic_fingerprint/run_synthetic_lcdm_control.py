#!/usr/bin/env python3
"""
UBT Forensic Fingerprint - Synthetic ΛCDM Control Test
=======================================================

End-to-end null hypothesis test: Generate synthetic ΛCDM power spectrum 
with realistic noise and run the CMB comb test to measure false positive rate.

This script:
1. Generates synthetic TT power spectrum using theoretical ΛCDM model
2. Adds realistic Gaussian noise (from sigma or covariance)
3. Runs CMB comb test with same protocol as real data
4. Repeats N times to estimate false positive rate at p < 0.01 threshold

Expected result under null: ~1% false positive rate at p < 0.01

Usage Examples
--------------

Generate 100 synthetic ΛCDM realizations and test:
    python run_synthetic_lcdm_control.py \\
        --model_file data/planck_pr3/raw/model.txt \\
        --sigma_file data/planck_pr3/raw/spectrum.txt \\
        --n_realizations 100 \\
        --ell_min 30 --ell_max 1500

With full covariance:
    python run_synthetic_lcdm_control.py \\
        --model_file data/planck_pr3/raw/model.txt \\
        --sigma_file data/planck_pr3/raw/spectrum.txt \\
        --cov_file data/planck_pr3/covariance.txt \\
        --whiten_mode covariance \\
        --n_realizations 100

License: MIT
Author: UBT Research Team
"""

import sys
import argparse
import json
from pathlib import Path
from datetime import datetime
import numpy as np


def find_repo_root(start_path=None):
    """
    Find repository root by walking upward from start_path.
    
    Looks for markers like .git, README.md, or pyproject.toml.
    
    Parameters
    ----------
    start_path : Path or None
        Starting directory (default: directory containing this file)
    
    Returns
    -------
    Path
        Repository root directory
    
    Raises
    ------
    FileNotFoundError
        If no repository markers found
    """
    if start_path is None:
        start_path = Path(__file__).resolve().parent
    else:
        start_path = Path(start_path).resolve()
    
    current = start_path
    markers = ['.git', 'pyproject.toml', 'pytest.ini']
    
    while current != current.parent:
        for marker in markers:
            if (current / marker).exists():
                return current
        current = current.parent
    
    for marker in markers:
        if (current / marker).exists():
            return current
    
    raise FileNotFoundError(
        f"Could not find repository root. Searched from {start_path} upward. "
        f"Looking for markers: {', '.join(markers)}"
    )


# Find repository root
repo_root = find_repo_root()

# Add modules to path
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'loaders'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'cmb_comb'))

import planck
import cmb_comb


# Default parameters
DEFAULT_N_REALIZATIONS = 100
DEFAULT_MC_SAMPLES = 5000  # For each realization
DEFAULT_SEED = 12345  # Different from main protocol seed
SIGNIFICANCE_THRESHOLD = 0.01  # p < 0.01 for "detection"


def load_lcdm_model_and_uncertainties(model_file, sigma_file, cov_file=None, 
                                      ell_min=None, ell_max=None):
    """
    Load ΛCDM model spectrum and uncertainties.
    
    Parameters
    ----------
    model_file : str or Path
        Theoretical ΛCDM model file
    sigma_file : str or Path
        File containing sigma values (can be observation file)
    cov_file : str or Path, optional
        Covariance matrix file
    ell_min : int, optional
        Minimum multipole
    ell_max : int, optional
        Maximum multipole
    
    Returns
    -------
    dict
        Dictionary with ell, cl_model, sigma, cov
    """
    # Load using planck loader
    data = planck.load_planck_data(
        obs_file=sigma_file,  # Just for sigma extraction
        model_file=model_file,
        cov_file=cov_file,
        ell_min=ell_min,
        ell_max=ell_max,
        dataset_name="LCDM Model"
    )
    
    return {
        'ell': data['ell'],
        'cl_model': data['cl_model'],
        'sigma': data['sigma'],
        'cov': data['cov']
    }


def generate_synthetic_realization(cl_model, sigma, cov=None, random_state=None):
    """
    Generate synthetic power spectrum realization.
    
    C_obs = C_model + noise
    
    where noise ~ N(0, sigma²) (diagonal) or N(0, Cov) (full covariance)
    
    Parameters
    ----------
    cl_model : array-like
        Theoretical ΛCDM model
    sigma : array-like
        Diagonal uncertainties
    cov : array-like, optional
        Full covariance matrix
    random_state : np.random.RandomState or int, optional
        Random state for reproducibility
    
    Returns
    -------
    cl_obs : ndarray
        Synthetic observed power spectrum
    """
    if random_state is None:
        rng = np.random
    elif isinstance(random_state, int):
        rng = np.random.RandomState(random_state)
    else:
        rng = random_state
    
    n = len(cl_model)
    
    if cov is not None:
        # Generate correlated noise using covariance
        try:
            L = np.linalg.cholesky(cov)
            z = rng.normal(0, 1, size=n)
            noise = L @ z
        except np.linalg.LinAlgError:
            # Fall back to diagonal
            noise = rng.normal(0, sigma)
    else:
        # Generate uncorrelated noise
        noise = rng.normal(0, sigma)
    
    cl_obs = cl_model + noise
    
    return cl_obs


def run_lcdm_control_test(model_file, sigma_file, cov_file=None,
                          ell_min=30, ell_max=1500,
                          n_realizations=DEFAULT_N_REALIZATIONS,
                          mc_samples=DEFAULT_MC_SAMPLES,
                          whiten_mode='diagonal',
                          output_dir=None,
                          random_seed=DEFAULT_SEED):
    """
    Run synthetic ΛCDM control test.
    
    Parameters
    ----------
    model_file : str or Path
        ΛCDM model file
    sigma_file : str or Path
        File with sigma values
    cov_file : str or Path, optional
        Covariance file
    ell_min : int
        Minimum multipole
    ell_max : int
        Maximum multipole
    n_realizations : int
        Number of synthetic realizations to generate
    mc_samples : int
        MC samples per realization
    whiten_mode : str
        Whitening mode
    output_dir : str or Path, optional
        Output directory
    random_seed : int
        Random seed
    
    Returns
    -------
    dict
        Control test results
    """
    # Setup output directory
    if output_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = repo_root / 'forensic_fingerprint' / 'out' / 'lcdm_control' / f'control_{timestamp}'
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("="*80)
    print("SYNTHETIC ΛCDM CONTROL TEST")
    print("="*80)
    print(f"Output directory: {output_dir}")
    print(f"N realizations: {n_realizations}")
    print(f"MC samples per realization: {mc_samples}")
    print(f"Whitening mode: {whiten_mode}")
    print()
    
    # Load model and uncertainties
    print("Loading ΛCDM model and uncertainties...")
    model_data = load_lcdm_model_and_uncertainties(
        model_file, sigma_file, cov_file, ell_min, ell_max
    )
    
    ell = model_data['ell']
    cl_model = model_data['cl_model']
    sigma = model_data['sigma']
    cov = model_data['cov']
    
    print(f"Loaded {len(ell)} multipoles (ℓ = {ell[0]} to {ell[-1]})")
    print()
    
    # Initialize random state
    rng = np.random.RandomState(random_seed)
    
    # Track results
    p_values = []
    best_periods = []
    detections = []  # p < 0.01
    
    print(f"Generating {n_realizations} synthetic realizations...")
    print()
    
    for i in range(n_realizations):
        print(f"Realization {i+1}/{n_realizations}")
        print("-" * 60)
        
        # Generate synthetic realization
        cl_obs_synthetic = generate_synthetic_realization(
            cl_model, sigma, cov, random_state=rng
        )
        
        # Run CMB comb test
        # Use a different seed for each realization's MC
        realization_seed = random_seed + i + 1
        
        results = cmb_comb.run_cmb_comb_test(
            ell=ell,
            C_obs=cl_obs_synthetic,
            C_model=cl_model,
            sigma=sigma,
            cov=cov,
            dataset_name=f"Synthetic LCDM #{i+1}",
            variant="C",  # Test under Variant C hypothesis
            n_mc_trials=mc_samples,
            random_seed=realization_seed,
            whiten_mode=whiten_mode,
            output_dir=None  # Don't save individual results
        )
        
        # Record results
        p_values.append(results['p_value'])
        best_periods.append(results['best_period'])
        
        is_detection = results['p_value'] < SIGNIFICANCE_THRESHOLD
        detections.append(is_detection)
        
        if is_detection:
            print(f"  ⚠ FALSE POSITIVE: p = {results['p_value']:.6e}, Δℓ = {results['best_period']}")
        else:
            print(f"  ✓ Null (as expected): p = {results['p_value']:.6e}")
        
        print()
    
    # Compute false positive rate
    false_positive_rate = np.sum(detections) / n_realizations
    
    # Expected false positive rate at p < 0.01 is 0.01
    expected_fpr = SIGNIFICANCE_THRESHOLD
    
    # Binomial confidence interval (Wilson score interval)
    # For p=0.01, n=100: 95% CI is approximately [0.002, 0.055]
    n = n_realizations
    p_hat = false_positive_rate
    z = 1.96  # 95% confidence
    
    if p_hat == 0:
        ci_lower = 0
    else:
        ci_lower = max(0, (p_hat + z**2/(2*n) - z*np.sqrt(p_hat*(1-p_hat)/n + z**2/(4*n**2))) / (1 + z**2/n))
    
    if p_hat == 1:
        ci_upper = 1
    else:
        ci_upper = min(1, (p_hat + z**2/(2*n) + z*np.sqrt(p_hat*(1-p_hat)/n + z**2/(4*n**2))) / (1 + z**2/n))
    
    # Summary
    print("="*80)
    print("CONTROL TEST SUMMARY")
    print("="*80)
    print(f"Total realizations: {n_realizations}")
    print(f"False positives (p < {SIGNIFICANCE_THRESHOLD}): {np.sum(detections)}")
    print(f"False positive rate: {false_positive_rate:.4f} ({false_positive_rate*100:.2f}%)")
    print(f"95% CI: [{ci_lower:.4f}, {ci_upper:.4f}]")
    print(f"Expected rate: {expected_fpr:.4f}")
    print()
    
    if false_positive_rate > ci_upper or false_positive_rate < ci_lower:
        # Outside expected range
        if false_positive_rate > expected_fpr * 2:
            print("⚠ WARNING: False positive rate HIGHER than expected")
            print("           Possible systematic bias or MC undersampling")
        elif false_positive_rate < expected_fpr * 0.5:
            print("✓ False positive rate LOWER than expected (conservative)")
        else:
            print("✓ False positive rate within expected range")
    else:
        print("✓ False positive rate consistent with null hypothesis")
    
    print("="*80)
    print()
    
    # Prepare results
    control_results = {
        'n_realizations': n_realizations,
        'mc_samples': mc_samples,
        'whiten_mode': whiten_mode,
        'ell_range': (int(ell[0]), int(ell[-1])),
        'p_values': [float(p) for p in p_values],
        'best_periods': [int(bp) for bp in best_periods],
        'detections': [bool(d) for d in detections],
        'false_positive_rate': float(false_positive_rate),
        'expected_fpr': float(expected_fpr),
        'ci_lower': float(ci_lower),
        'ci_upper': float(ci_upper),
        'random_seed': random_seed,
        'threshold': SIGNIFICANCE_THRESHOLD
    }
    
    # Save results
    with open(output_dir / 'lcdm_control_results.json', 'w') as f:
        json.dump(control_results, f, indent=2)
    
    print(f"Results saved to: {output_dir / 'lcdm_control_results.json'}")
    
    # Save p-value histogram data
    np.savetxt(output_dir / 'p_values.txt', p_values,
               header=f'P-values from {n_realizations} synthetic ΛCDM realizations')
    
    # Generate plots if matplotlib available
    try:
        import matplotlib.pyplot as plt
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # P-value histogram
        ax1.hist(p_values, bins=20, alpha=0.7, edgecolor='black')
        ax1.axvline(SIGNIFICANCE_THRESHOLD, color='r', linestyle='--', linewidth=2,
                   label=f'p = {SIGNIFICANCE_THRESHOLD} threshold')
        ax1.set_xlabel('P-value')
        ax1.set_ylabel('Frequency')
        ax1.set_title(f'P-value Distribution ({n_realizations} synthetic ΛCDM realizations)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Period frequency
        period_counts = {p: best_periods.count(p) for p in cmb_comb.CANDIDATE_PERIODS}
        ax2.bar(period_counts.keys(), period_counts.values(), alpha=0.7, edgecolor='black')
        ax2.set_xlabel('Best-fit Δℓ')
        ax2.set_ylabel('Frequency')
        ax2.set_title('Best-fit Period Distribution')
        ax2.grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        plt.savefig(output_dir / 'lcdm_control_plots.png', dpi=150)
        plt.close()
        
        print(f"Plots saved to: {output_dir / 'lcdm_control_plots.png'}")
    except ImportError:
        print("Matplotlib not available - skipping plots")
    
    return control_results


def main():
    parser = argparse.ArgumentParser(
        description="Synthetic ΛCDM Control Test - Measure False Positive Rate",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic test (100 realizations, diagonal):
  python run_synthetic_lcdm_control.py \\
      --model_file data/planck_pr3/raw/model.txt \\
      --sigma_file data/planck_pr3/raw/spectrum.txt \\
      --n_realizations 100
  
  # With full covariance:
  python run_synthetic_lcdm_control.py \\
      --model_file data/planck_pr3/raw/model.txt \\
      --sigma_file data/planck_pr3/raw/spectrum.txt \\
      --cov_file data/planck_pr3/covariance.txt \\
      --whiten_mode covariance \\
      --n_realizations 100

See forensic_fingerprint/RUNBOOK_REAL_DATA.md for documentation.
        """
    )
    
    # Input files
    parser.add_argument('--model_file', type=str, required=True,
                       help='ΛCDM model file (theoretical spectrum)')
    parser.add_argument('--sigma_file', type=str, required=True,
                       help='File with sigma values (can be observation file)')
    parser.add_argument('--cov_file', type=str,
                       help='Covariance matrix file (optional)')
    
    # Multipole range
    parser.add_argument('--ell_min', type=int, default=30,
                       help='Minimum multipole (default: 30)')
    parser.add_argument('--ell_max', type=int, default=1500,
                       help='Maximum multipole (default: 1500)')
    
    # Test parameters
    parser.add_argument('--n_realizations', type=int, default=DEFAULT_N_REALIZATIONS,
                       help=f'Number of synthetic realizations (default: {DEFAULT_N_REALIZATIONS})')
    parser.add_argument('--mc_samples', type=int, default=DEFAULT_MC_SAMPLES,
                       help=f'MC samples per realization (default: {DEFAULT_MC_SAMPLES})')
    parser.add_argument('--whiten_mode', type=str,
                       choices=['none', 'diagonal', 'cov_diag', 'covariance'],
                       default='diagonal',
                       help='Whitening mode (default: diagonal)')
    parser.add_argument('--seed', type=int, default=DEFAULT_SEED,
                       help=f'Random seed (default: {DEFAULT_SEED})')
    
    # Output
    parser.add_argument('--output_dir', type=str,
                       help='Output directory (default: auto-generated with timestamp)')
    
    args = parser.parse_args()
    
    # Run control test
    run_lcdm_control_test(
        model_file=args.model_file,
        sigma_file=args.sigma_file,
        cov_file=args.cov_file,
        ell_min=args.ell_min,
        ell_max=args.ell_max,
        n_realizations=args.n_realizations,
        mc_samples=args.mc_samples,
        whiten_mode=args.whiten_mode,
        output_dir=args.output_dir,
        random_seed=args.seed
    )


if __name__ == '__main__':
    main()
