#!/usr/bin/env python3
"""
UBT Forensic Fingerprint - Court-Grade Audit Suite Runner
==========================================================

Single unified entrypoint for running all court-grade audit tests:
1. Baseline TT with diagonal uncertainties
2. Whitened TT with full covariance
3. Polarization channels (EE, TE) if requested
4. ℓ-range ablations across pre-defined splits
5. Synthetic ΛCDM null hypothesis testing

All tests use the same locked candidate periods and pre-registered protocol.

Usage Examples
--------------

Minimal audit (TT + whitening + ablation):
    python run_audit_suite.py \\
        --planck_obs data/planck_pr3/raw/spectrum.txt \\
        --planck_model data/planck_pr3/raw/model.txt \\
        --planck_cov data/planck_pr3/raw/covariance.npy \\
        --run_ablation

Full audit (all modes):
    python run_audit_suite.py \\
        --planck_obs data/planck_pr3/raw/spectrum_tt.txt \\
        --planck_model data/planck_pr3/raw/model_tt.txt \\
        --planck_cov data/planck_pr3/raw/cov_tt.npy \\
        --planck_obs_ee data/planck_pr3/raw/spectrum_ee.txt \\
        --planck_model_ee data/planck_pr3/raw/model_ee.txt \\
        --planck_obs_te data/planck_pr3/raw/spectrum_te.txt \\
        --planck_model_te data/planck_pr3/raw/model_te.txt \\
        --wmap_obs data/wmap/raw/wmap_tt.txt \\
        --run_ablation --run_synth_null --synth_trials 200 \\
        --mc_samples 10000

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
    """Find repository root by walking upward."""
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
        f"Could not find repository root. Searched from {start_path} upward."
    )


# Find repository root
repo_root = find_repo_root()

# Add modules to path
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'loaders'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'cmb_comb'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'stats'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'synthetic'))
sys.path.insert(0, str(repo_root / 'tools' / 'data_provenance'))

import planck
import wmap
import cmb_comb
import ablation
from synthetic import lcdm
try:
    import validate_manifest
    MANIFEST_VALIDATION_AVAILABLE = True
except ImportError:
    MANIFEST_VALIDATION_AVAILABLE = False
    print("WARNING: validate_manifest not available. Skipping manifest validation.")


# PROTOCOL-LOCKED CANDIDATE PERIODS (do not modify)
CANDIDATE_PERIODS = [8, 16, 32, 64, 128, 255]

# Default parameters
DEFAULT_VARIANT = "C"
DEFAULT_MC_SAMPLES = 5000
DEFAULT_SYNTH_TRIALS = 200
DEFAULT_SEED = 42


def validate_manifest_if_provided(manifest_path, dataset_type, files_used):
    """
    Validate manifest if provided.
    
    Parameters
    ----------
    manifest_path : str or Path or None
        Path to manifest file
    dataset_type : str
        'planck' or 'wmap'
    files_used : list of str
        List of file paths used in this run
    
    Returns
    -------
    bool
        True if validation passed or no manifest provided
    """
    if manifest_path is None:
        print(f"  No {dataset_type} manifest provided (skipping validation)")
        return True
    
    if not MANIFEST_VALIDATION_AVAILABLE:
        print(f"  Manifest validation not available (skipping)")
        return True
    
    manifest_path = Path(manifest_path)
    if not manifest_path.exists():
        print(f"  ERROR: Manifest not found: {manifest_path}")
        return False
    
    # Validate hashes
    print(f"  Validating {dataset_type} manifest: {manifest_path}")
    success = validate_manifest.validate_manifest(manifest_path, base_dir=repo_root)
    
    if not success:
        return False
    
    # Check manifest contains all used files
    with open(manifest_path, 'r') as f:
        manifest = json.load(f)
    
    manifest_files = {f['filename'] for f in manifest.get('files', [])}
    
    for file_path in files_used:
        if file_path is None:
            continue
        filename = Path(file_path).name
        if filename not in manifest_files:
            print(f"  WARNING: File {filename} not in manifest")
    
    print(f"  ✓ Manifest validated")
    return True


def run_baseline_analysis(dataset_name, data_loader, loader_args, mc_samples, seed, variant, whiten_mode):
    """
    Run baseline analysis (TT with diagonal or covariance).
    
    Returns
    -------
    dict
        Analysis results
    """
    print(f"\n{'='*80}")
    print(f"BASELINE ANALYSIS: {dataset_name}")
    print(f"{'='*80}")
    
    # Load data
    print(f"Loading data...")
    data = data_loader(**loader_args)
    
    print(f"  Loaded {data['n_multipoles']} multipoles (ℓ = {data['ell_range'][0]} to {data['ell_range'][1]})")
    print(f"  Whitening mode: {whiten_mode}")
    
    # Run comb test
    results = cmb_comb.run_cmb_comb_test(
        ell=data['ell'],
        C_obs=data['cl_obs'],
        C_model=data['cl_model'] if data['cl_model'] is not None else data['cl_obs'] * 0,
        sigma=data['sigma'],
        cov=data['cov'],
        dataset_name=dataset_name,
        variant=variant,
        n_mc_trials=mc_samples,
        random_seed=seed,
        whiten_mode=whiten_mode,
        output_dir=None
    )
    
    print(f"  Best period: Δℓ = {results['best_period']}")
    print(f"  P-value: {results['p_value']:.6e}")
    print(f"  Significance: {results['significance']}")
    
    return results


def run_polarization_analysis(dataset_name, channel, obs_file, model_file, cov_file,
                              ell_min, ell_max, mc_samples, seed, variant, whiten_mode):
    """
    Run analysis on single polarization channel.
    
    Returns
    -------
    dict
        Analysis results
    """
    print(f"\n{'='*80}")
    print(f"POLARIZATION ANALYSIS: {dataset_name} {channel}")
    print(f"{'='*80}")
    
    # Load data
    print(f"Loading {channel} data...")
    data = planck.load_planck_data(
        obs_file=obs_file,
        model_file=model_file,
        cov_file=cov_file,
        ell_min=ell_min,
        ell_max=ell_max,
        dataset_name=f"{dataset_name} {channel}",
        spectrum_type=channel
    )
    
    print(f"  Loaded {data['n_multipoles']} multipoles (ℓ = {data['ell_range'][0]} to {data['ell_range'][1]})")
    
    # Run comb test
    results = cmb_comb.run_cmb_comb_test(
        ell=data['ell'],
        C_obs=data['cl_obs'],
        C_model=data['cl_model'] if data['cl_model'] is not None else data['cl_obs'] * 0,
        sigma=data['sigma'],
        cov=data['cov'],
        dataset_name=f"{dataset_name} {channel}",
        variant=variant,
        n_mc_trials=mc_samples,
        random_seed=seed,
        whiten_mode=whiten_mode,
        output_dir=None
    )
    
    print(f"  Best period: Δℓ = {results['best_period']}")
    print(f"  P-value: {results['p_value']:.6e}")
    
    return results


def run_ablation_suite(dataset_name, data_loader, loader_args, dataset_type,
                       mc_samples, seed, variant, whiten_mode):
    """
    Run ablation tests across pre-defined ℓ ranges.
    
    Returns
    -------
    dict
        Ablation results for each range
    """
    print(f"\n{'='*80}")
    print(f"ABLATION SUITE: {dataset_name}")
    print(f"{'='*80}")
    
    # Get ablation ranges for this dataset
    ranges = ablation.get_ablation_ranges(dataset=dataset_type)
    
    print(f"Testing {len(ranges)} ablation ranges...")
    
    ablation_results = {}
    
    for range_name, ell_min, ell_max in ranges:
        print(f"\n  Range: {range_name} (ℓ = {ell_min} to {ell_max})")
        
        # Load data for this range
        loader_args_range = loader_args.copy()
        loader_args_range['ell_min'] = ell_min
        loader_args_range['ell_max'] = ell_max
        
        try:
            data = data_loader(**loader_args_range)
            
            # Validate range has sufficient points
            is_valid, n_points, skip_reason = ablation.validate_ablation_range(
                ell_min, ell_max, data['ell'], min_points=50
            )
            
            if not is_valid:
                print(f"    SKIPPED: {skip_reason}")
                ablation_results[range_name] = {
                    'skipped': True,
                    'skip_reason': skip_reason,
                    'ell_range': (ell_min, ell_max)
                }
                continue
            
            # Run comb test
            results = cmb_comb.run_cmb_comb_test(
                ell=data['ell'],
                C_obs=data['cl_obs'],
                C_model=data['cl_model'] if data['cl_model'] is not None else data['cl_obs'] * 0,
                sigma=data['sigma'],
                cov=data['cov'],
                dataset_name=f"{dataset_name} {range_name}",
                variant=variant,
                n_mc_trials=mc_samples,
                random_seed=seed,
                whiten_mode=whiten_mode,
                output_dir=None
            )
            
            print(f"    Period: Δℓ = {results['best_period']}, p = {results['p_value']:.4e}")
            
            ablation_results[range_name] = results
            ablation_results[range_name]['skipped'] = False
            ablation_results[range_name]['ell_range'] = (ell_min, ell_max)
            
        except Exception as e:
            print(f"    ERROR: {str(e)}")
            ablation_results[range_name] = {
                'skipped': True,
                'skip_reason': f"Error: {str(e)}",
                'ell_range': (ell_min, ell_max)
            }
    
    # Summarize
    summary = ablation.summarize_ablation_results(ablation_results)
    print(f"\nAblation summary:")
    print(f"  Valid ranges: {summary['n_valid']}/{summary['n_ranges']}")
    if summary['periods']:
        print(f"  Period counts: {summary['periods']}")
    if summary['phase_consistency']:
        print(f"  Phase consistency: {summary['phase_consistency']}")
    
    return {'results_by_range': ablation_results, 'summary': summary}


def run_synth_null_suite(dataset_name, model_file, ell_min, ell_max, sigma_or_cov,
                        n_trials, mc_samples, seed, variant, whiten_mode):
    """
    Run synthetic ΛCDM null hypothesis tests.
    
    Returns
    -------
    dict
        Synthetic null results
    """
    print(f"\n{'='*80}")
    print(f"SYNTHETIC ΛCDM NULL: {dataset_name}")
    print(f"{'='*80}")
    
    print(f"Generating {n_trials} synthetic ΛCDM realizations...")
    
    # Load ΛCDM model
    ell, Cl_theory = lcdm.load_lcdm_model_from_file(
        model_file, ell_min=ell_min, ell_max=ell_max
    )
    
    # Extract sigma
    if isinstance(sigma_or_cov, dict) and 'sigma' in sigma_or_cov:
        sigma = sigma_or_cov['sigma']
        cov = sigma_or_cov.get('cov')
    elif isinstance(sigma_or_cov, np.ndarray) and sigma_or_cov.ndim == 1:
        sigma = sigma_or_cov
        cov = None
    elif isinstance(sigma_or_cov, np.ndarray) and sigma_or_cov.ndim == 2:
        # Covariance matrix provided, extract diagonal for sigma
        sigma = np.sqrt(np.diag(sigma_or_cov))
        cov = sigma_or_cov
    else:
        raise ValueError("sigma_or_cov must be array or dict with 'sigma' key")
    
    # Run trials
    trial_results = []
    period_counts = {p: 0 for p in CANDIDATE_PERIODS}
    p_values = []
    
    for trial_idx in range(n_trials):
        # Generate synthetic observation
        trial_seed = seed + trial_idx  # Deterministic but unique per trial
        Cl_obs_synth = lcdm.generate_mock_observation(
            ell=ell,
            Cl_theory=Cl_theory,
            noise_model={'sigma': sigma},
            cov=cov,
            seed=trial_seed
        )
        
        # Run comb test
        result = cmb_comb.run_cmb_comb_test(
            ell=ell,
            C_obs=Cl_obs_synth,
            C_model=Cl_theory,
            sigma=sigma,
            cov=cov,
            dataset_name=f"Synth trial {trial_idx}",
            variant=variant,
            n_mc_trials=mc_samples,
            random_seed=trial_seed,
            whiten_mode=whiten_mode,
            output_dir=None
        )
        
        trial_results.append({
            'trial_idx': trial_idx,
            'best_period': result['best_period'],
            'p_value': result['p_value'],
            'amplitude': result['amplitude'],
            'phase': result['phase']
        })
        
        period_counts[result['best_period']] += 1
        p_values.append(result['p_value'])
        
        if (trial_idx + 1) % 50 == 0:
            print(f"  Completed {trial_idx + 1}/{n_trials} trials")
    
    # Compute summary statistics
    p_values = np.array(p_values)
    false_positive_rate = np.mean(p_values < 0.01)
    
    print(f"\nSynthetic null summary:")
    print(f"  False positive rate (p < 0.01): {false_positive_rate:.4f}")
    print(f"  Period 255 frequency: {period_counts[255]}/{n_trials} ({period_counts[255]/n_trials:.4f})")
    print(f"  Mean p-value: {np.mean(p_values):.4e}")
    print(f"  Median p-value: {np.median(p_values):.4e}")
    
    return {
        'n_trials': n_trials,
        'trial_results': trial_results,
        'period_counts': period_counts,
        'false_positive_rate': float(false_positive_rate),
        'p_value_stats': {
            'mean': float(np.mean(p_values)),
            'median': float(np.median(p_values)),
            'min': float(np.min(p_values)),
            'max': float(np.max(p_values))
        }
    }


def save_json_results(data, output_file):
    """Save results to JSON, converting numpy types."""
    def convert(obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, (np.integer, np.floating)):
            return float(obj)
        elif isinstance(obj, dict):
            return {str(k): convert(v) for k, v in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [convert(item) for item in obj]
        else:
            return obj
    
    with open(output_file, 'w') as f:
        json.dump(convert(data), f, indent=2)
    
    print(f"  Saved: {output_file}")


def generate_audit_report(baseline_results, pol_results, ablation_results, synth_results,
                         output_file, args):
    """Generate human-readable audit report."""
    
    with open(output_file, 'w') as f:
        f.write("# CMB Forensic Fingerprint - Court-Grade Audit Report\n\n")
        f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
        f.write(f"**Protocol Version**: v2.0 (Court-Grade)\n")
        f.write(f"**Variant**: {args.variant}\n")
        f.write(f"**Random Seed**: {args.seed}\n\n")
        
        f.write("## Overview\n\n")
        f.write("This report consolidates results from multiple audit modes:\n\n")
        f.write("1. **Baseline**: Standard TT analysis with diagonal/covariance uncertainties\n")
        f.write("2. **Polarization**: Independent tests on EE/TE channels (if available)\n")
        f.write("3. **Ablation**: Tests across multiple ℓ-ranges to detect localized artifacts\n")
        f.write("4. **Synthetic Null**: ΛCDM false positive rate validation\n\n")
        
        f.write("---\n\n")
        
        # Baseline Results
        f.write("## Baseline Results\n\n")
        
        for dataset_name, results in baseline_results.items():
            f.write(f"### {dataset_name}\n\n")
            if results:
                f.write(f"- **ℓ range**: {results['ell'][0]} to {results['ell'][-1]}\n")
                f.write(f"- **Whitening**: {results.get('whiten_mode', 'diagonal')}\n")
                f.write(f"- **Best period**: Δℓ = {results['best_period']}\n")
                f.write(f"- **Amplitude**: A = {results['amplitude']:.6f}\n")
                f.write(f"- **Phase**: φ = {results['phase']:.6f} rad\n")
                f.write(f"- **P-value**: {results['p_value']:.6e}\n")
                f.write(f"- **Significance**: **{results['significance'].upper()}**\n\n")
            else:
                f.write("*Not run*\n\n")
        
        f.write("---\n\n")
        
        # Polarization Results
        if pol_results:
            f.write("## Polarization Results\n\n")
            
            for key, results in pol_results.items():
                f.write(f"### {key}\n\n")
                f.write(f"- **Best period**: Δℓ = {results['best_period']}\n")
                f.write(f"- **P-value**: {results['p_value']:.6e}\n")
                f.write(f"- **Phase**: φ = {results['phase']:.6f} rad\n\n")
            
            f.write("---\n\n")
        
        # Ablation Results
        if ablation_results:
            f.write("## Ablation Results\n\n")
            
            for dataset_name, abl_data in ablation_results.items():
                f.write(f"### {dataset_name}\n\n")
                
                summary = abl_data['summary']
                f.write(f"**Summary**: {summary['n_valid']}/{summary['n_ranges']} valid ranges\n\n")
                
                if summary['periods']:
                    f.write("**Period counts across ranges**:\n\n")
                    for period, count in sorted(summary['periods'].items()):
                        f.write(f"- Δℓ = {period}: {count} range(s)\n")
                    f.write("\n")
                
                if summary['phase_consistency']:
                    pc = summary['phase_consistency']
                    f.write(f"**Phase consistency**: Max diff = {pc['max_phase_diff']:.3f} rad")
                    if pc['consistent_within_pi_2']:
                        f.write(" ✓ (within π/2)\n\n")
                    else:
                        f.write(" ✗ (exceeds π/2)\n\n")
                
                f.write("**Per-range results**:\n\n")
                f.write("| Range | ℓ min | ℓ max | Best Period | P-value | Status |\n")
                f.write("|-------|-------|-------|-------------|---------|--------|\n")
                
                for range_name, result in abl_data['results_by_range'].items():
                    ell_min, ell_max = result['ell_range']
                    if result.get('skipped'):
                        f.write(f"| {range_name} | {ell_min} | {ell_max} | - | - | SKIPPED |\n")
                    else:
                        period = result['best_period']
                        p_val = result['p_value']
                        f.write(f"| {range_name} | {ell_min} | {ell_max} | {period} | {p_val:.4e} | OK |\n")
                
                f.write("\n")
            
            f.write("---\n\n")
        
        # Synthetic Null Results
        if synth_results:
            f.write("## Synthetic ΛCDM Null Results\n\n")
            
            for dataset_name, synth_data in synth_results.items():
                f.write(f"### {dataset_name}\n\n")
                f.write(f"- **Trials**: {synth_data['n_trials']}\n")
                f.write(f"- **False positive rate** (p < 0.01): {synth_data['false_positive_rate']:.4f}\n")
                f.write(f"- **Mean p-value**: {synth_data['p_value_stats']['mean']:.4e}\n")
                f.write(f"- **Δℓ=255 frequency**: {synth_data['period_counts'][255]}/{synth_data['n_trials']}\n\n")
                
                f.write("**Interpretation**: ")
                if synth_data['false_positive_rate'] < 0.01:
                    f.write("✓ False positive rate is low. Signal unlikely to be ΛCDM artifact.\n\n")
                elif synth_data['false_positive_rate'] < 0.05:
                    f.write("⚠ Borderline false positive rate. Requires further investigation.\n\n")
                else:
                    f.write("✗ High false positive rate. Signal may be ΛCDM artifact.\n\n")
            
            f.write("---\n\n")
        
        # Interpretation
        f.write("## Interpretation Guidelines\n\n")
        f.write("### Signal Robustness Indicators\n\n")
        f.write("A **robust** candidate signal should exhibit:\n\n")
        f.write("1. **Baseline**: p < 0.01 in primary TT channel\n")
        f.write("2. **Whitening**: Signal persists with full covariance whitening\n")
        f.write("3. **Polarization**: Appears in EE/TE with consistent phase\n")
        f.write("4. **Ablation**: Appears in ≥2 independent ℓ-ranges\n")
        f.write("5. **Synthetic Null**: Δℓ=255 appears in <1% of ΛCDM realizations\n\n")
        
        f.write("### Potential Artifacts\n\n")
        f.write("Signal **disappears** after whitening → likely covariance artifact\n")
        f.write("Signal **absent** in polarization → likely TT-specific systematic\n")
        f.write("Signal **restricted** to one ℓ-range → likely localized artifact\n")
        f.write("Signal **frequent** in ΛCDM null → likely generic statistical fluctuation\n\n")
        
        f.write("---\n\n")
        f.write("**End of Audit Report**\n")
    
    print(f"Audit report saved: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Court-Grade CMB Audit Suite",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Planck TT
    parser.add_argument('--planck_obs', type=str, help='Planck TT observation file')
    parser.add_argument('--planck_model', type=str, help='Planck TT model file')
    parser.add_argument('--planck_cov', type=str, help='Planck TT covariance file')
    parser.add_argument('--planck_manifest', type=str, help='Planck manifest for validation')
    
    # Planck EE
    parser.add_argument('--planck_obs_ee', type=str, help='Planck EE observation file')
    parser.add_argument('--planck_model_ee', type=str, help='Planck EE model file')
    parser.add_argument('--planck_cov_ee', type=str, help='Planck EE covariance file')
    
    # Planck TE
    parser.add_argument('--planck_obs_te', type=str, help='Planck TE observation file')
    parser.add_argument('--planck_model_te', type=str, help='Planck TE model file')
    parser.add_argument('--planck_cov_te', type=str, help='Planck TE covariance file')
    
    # WMAP
    parser.add_argument('--wmap_obs', type=str, help='WMAP TT observation file')
    parser.add_argument('--wmap_model', type=str, help='WMAP TT model file')
    parser.add_argument('--wmap_cov', type=str, help='WMAP TT covariance file')
    parser.add_argument('--wmap_manifest', type=str, help='WMAP manifest for validation')
    
    # Multipole ranges
    parser.add_argument('--ell_min_planck', type=int, default=30)
    parser.add_argument('--ell_max_planck', type=int, default=1500)
    parser.add_argument('--ell_min_wmap', type=int, default=30)
    parser.add_argument('--ell_max_wmap', type=int, default=800)
    
    # Audit options
    parser.add_argument('--run_ablation', action='store_true', help='Run ℓ-range ablation tests')
    parser.add_argument('--run_synth_null', action='store_true', help='Run synthetic ΛCDM null tests')
    parser.add_argument('--synth_trials', type=int, default=DEFAULT_SYNTH_TRIALS,
                       help=f'Number of synthetic trials (default: {DEFAULT_SYNTH_TRIALS})')
    
    # Test parameters
    parser.add_argument('--variant', type=str, choices=['A', 'B', 'C', 'D'], default=DEFAULT_VARIANT)
    parser.add_argument('--mc_samples', type=int, default=DEFAULT_MC_SAMPLES)
    parser.add_argument('--seed', type=int, default=DEFAULT_SEED)
    parser.add_argument('--whiten_mode', type=str, 
                       choices=['none', 'diagonal', 'cov_diag', 'covariance'],
                       default='covariance',
                       help='Whitening mode (default: covariance if cov file provided, else diagonal)')
    
    # Output
    parser.add_argument('--output_dir', type=str, help='Output directory')
    
    args = parser.parse_args()
    
    # Setup output directory
    if args.output_dir:
        output_dir = Path(args.output_dir)
        if not output_dir.is_absolute():
            output_dir = repo_root / output_dir
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = repo_root / 'forensic_fingerprint' / 'out' / 'audit_runs' / f"audit_{timestamp}"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create subdirectories
    (output_dir / 'baseline').mkdir(exist_ok=True)
    (output_dir / 'polarization').mkdir(exist_ok=True)
    (output_dir / 'ablations').mkdir(exist_ok=True)
    (output_dir / 'synth').mkdir(exist_ok=True)
    (output_dir / 'figures').mkdir(exist_ok=True)
    
    print("="*80)
    print("CMB FORENSIC FINGERPRINT - COURT-GRADE AUDIT SUITE")
    print("="*80)
    print(f"Output: {output_dir}")
    print(f"Variant: {args.variant}")
    print(f"MC samples: {args.mc_samples}")
    print(f"Seed: {args.seed}")
    print()
    
    # Validate manifests
    print("="*80)
    print("MANIFEST VALIDATION")
    print("="*80)
    
    planck_files = [args.planck_obs, args.planck_model, args.planck_cov,
                   args.planck_obs_ee, args.planck_model_ee, args.planck_cov_ee,
                   args.planck_obs_te, args.planck_model_te, args.planck_cov_te]
    planck_files = [f for f in planck_files if f is not None]
    
    if planck_files:
        validate_manifest_if_provided(args.planck_manifest, 'planck', planck_files)
    
    wmap_files = [args.wmap_obs, args.wmap_model, args.wmap_cov]
    wmap_files = [f for f in wmap_files if f is not None]
    
    if wmap_files:
        validate_manifest_if_provided(args.wmap_manifest, 'wmap', wmap_files)
    
    # Auto-adjust whiten_mode based on availability
    actual_whiten_mode = args.whiten_mode
    if args.whiten_mode == 'covariance' and not (args.planck_cov or args.wmap_cov):
        actual_whiten_mode = 'diagonal'
        print("\nNOTE: No covariance files provided. Using diagonal whitening.")
    
    # 1. Baseline analyses
    baseline_results = {}
    
    if args.planck_obs:
        planck_loader_args = {
            'obs_file': args.planck_obs,
            'model_file': args.planck_model,
            'cov_file': args.planck_cov,
            'ell_min': args.ell_min_planck,
            'ell_max': args.ell_max_planck,
            'dataset_name': 'Planck PR3 TT'
        }
        
        baseline_results['Planck TT'] = run_baseline_analysis(
            'Planck PR3 TT',
            planck.load_planck_data,
            planck_loader_args,
            args.mc_samples,
            args.seed,
            args.variant,
            actual_whiten_mode
        )
        
        save_json_results(baseline_results['Planck TT'], output_dir / 'baseline' / 'planck_tt.json')
    
    if args.wmap_obs:
        wmap_loader_args = {
            'obs_file': args.wmap_obs,
            'model_file': args.wmap_model,
            'cov_file': args.wmap_cov,
            'ell_min': args.ell_min_wmap,
            'ell_max': args.ell_max_wmap,
            'dataset_name': 'WMAP 9yr TT'
        }
        
        baseline_results['WMAP TT'] = run_baseline_analysis(
            'WMAP 9yr TT',
            wmap.load_wmap_data,
            wmap_loader_args,
            args.mc_samples,
            args.seed,
            args.variant,
            'diagonal' if not args.wmap_cov else actual_whiten_mode
        )
        
        save_json_results(baseline_results['WMAP TT'], output_dir / 'baseline' / 'wmap_tt.json')
    
    # 2. Polarization analyses
    pol_results = {}
    
    if args.planck_obs_ee:
        pol_results['Planck EE'] = run_polarization_analysis(
            'Planck PR3', 'EE',
            args.planck_obs_ee,
            args.planck_model_ee,
            args.planck_cov_ee,
            args.ell_min_planck,
            args.ell_max_planck,
            args.mc_samples,
            args.seed,
            args.variant,
            'diagonal' if not args.planck_cov_ee else actual_whiten_mode
        )
        save_json_results(pol_results['Planck EE'], output_dir / 'polarization' / 'planck_ee.json')
    
    if args.planck_obs_te:
        pol_results['Planck TE'] = run_polarization_analysis(
            'Planck PR3', 'TE',
            args.planck_obs_te,
            args.planck_model_te,
            args.planck_cov_te,
            args.ell_min_planck,
            args.ell_max_planck,
            args.mc_samples,
            args.seed,
            args.variant,
            'diagonal' if not args.planck_cov_te else actual_whiten_mode
        )
        save_json_results(pol_results['Planck TE'], output_dir / 'polarization' / 'planck_te.json')
    
    # 3. Ablation tests
    ablation_results = {}
    
    if args.run_ablation:
        if args.planck_obs:
            ablation_results['Planck TT'] = run_ablation_suite(
                'Planck PR3 TT',
                planck.load_planck_data,
                planck_loader_args,
                'planck',
                args.mc_samples,
                args.seed,
                args.variant,
                actual_whiten_mode
            )
            save_json_results(ablation_results['Planck TT'], output_dir / 'ablations' / 'planck_tt.json')
        
        if args.wmap_obs:
            ablation_results['WMAP TT'] = run_ablation_suite(
                'WMAP 9yr TT',
                wmap.load_wmap_data,
                wmap_loader_args,
                'wmap',
                args.mc_samples,
                args.seed,
                args.variant,
                'diagonal' if not args.wmap_cov else actual_whiten_mode
            )
            save_json_results(ablation_results['WMAP TT'], output_dir / 'ablations' / 'wmap_tt.json')
    
    # 4. Synthetic null tests
    synth_results = {}
    
    if args.run_synth_null:
        if args.planck_obs and args.planck_model:
            # Need to load data to get sigma/cov
            data = planck.load_planck_data(
                obs_file=args.planck_obs,
                model_file=args.planck_model,
                cov_file=args.planck_cov,
                ell_min=args.ell_min_planck,
                ell_max=args.ell_max_planck
            )
            
            synth_results['Planck TT'] = run_synth_null_suite(
                'Planck PR3 TT',
                args.planck_model,
                args.ell_min_planck,
                args.ell_max_planck,
                {'sigma': data['sigma'], 'cov': data['cov']},
                args.synth_trials,
                args.mc_samples,
                args.seed + 10000,  # Offset seed for synth
                args.variant,
                actual_whiten_mode
            )
            save_json_results(synth_results['Planck TT'], output_dir / 'synth' / 'planck_tt.json')
    
    # 5. Generate consolidated audit report
    print("\n" + "="*80)
    print("GENERATING AUDIT REPORT")
    print("="*80)
    
    generate_audit_report(
        baseline_results,
        pol_results,
        ablation_results,
        synth_results,
        output_dir / 'AUDIT_REPORT.md',
        args
    )
    
    print("\n" + "="*80)
    print("AUDIT SUITE COMPLETE")
    print("="*80)
    print(f"\nAll results in: {output_dir}")
    print(f"\nRead AUDIT_REPORT.md for consolidated analysis.\n")


if __name__ == '__main__':
    main()
