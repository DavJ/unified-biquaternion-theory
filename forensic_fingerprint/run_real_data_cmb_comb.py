#!/usr/bin/env python3
"""
UBT Forensic Fingerprint - One-Command Real Data CMB Comb Test Runner
=====================================================================

Single entrypoint for running court-grade CMB comb fingerprint test on real data
(Planck PR3 and WMAP TT) with full provenance tracking and automated verdict generation.

This script:
1. Validates dataset manifests (SHA-256 hashes)
2. Loads Planck and WMAP data
3. Runs CMB comb test on both datasets
4. Generates combined PASS/FAIL verdict report
5. Saves all results with timestamps

Usage Examples
--------------

Minimal example (Planck only, Variant C):
    python run_real_data_cmb_comb.py \
        --planck_obs data/planck_pr3/raw/spectrum.txt \
        --planck_model data/planck_pr3/raw/model.txt

Full example (Planck + WMAP, with manifests):
    python run_real_data_cmb_comb.py \
        --planck_obs data/planck_pr3/raw/spectrum.txt \
        --planck_model data/planck_pr3/raw/model.txt \
        --planck_manifest data/planck_pr3/manifests/sha256.json \
        --wmap_obs data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
        --wmap_manifest data/wmap/manifests/sha256.json \
        --ell_min_planck 30 --ell_max_planck 1500 \
        --ell_min_wmap 30 --ell_max_wmap 800 \
        --variant C --mc_samples 10000

High-confidence run (100k MC samples):
    python run_real_data_cmb_comb.py \
        --planck_obs data/planck_pr3/raw/spectrum.txt \
        --planck_model data/planck_pr3/raw/model.txt \
        --wmap_obs data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
        --mc_samples 100000 --variant C

License: MIT
Author: UBT Research Team
"""

import sys
import argparse
import json
from pathlib import Path
from datetime import datetime
import numpy as np

# Add loaders and cmb_comb to path
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).parent / 'loaders'))
sys.path.insert(0, str(Path(__file__).parent / 'cmb_comb'))
sys.path.insert(0, str(repo_root / 'tools' / 'data_provenance'))

import planck
import wmap
import cmb_comb
import validate_manifest


# PROTOCOL-LOCKED CANDIDATE PERIODS (do not modify)
CANDIDATE_PERIODS = [8, 16, 32, 64, 128, 255]

# Default parameters
DEFAULT_VARIANT = "C"
DEFAULT_MC_SAMPLES = 5000  # Candidate-grade
DEFAULT_SEED = 42  # Pre-registered


def validate_data_manifest(manifest_path):
    """
    Validate dataset against SHA-256 manifest.
    
    Parameters
    ----------
    manifest_path : str or Path
        Path to manifest JSON file
    
    Returns
    -------
    bool
        True if validation passed, False otherwise
    """
    if manifest_path is None:
        print("WARNING: No manifest provided. Skipping hash validation.")
        print("         For court-grade provenance, manifests are required.\n")
        return True
    
    manifest_path = Path(manifest_path)
    if not manifest_path.exists():
        print(f"ERROR: Manifest not found: {manifest_path}")
        return False
    
    print(f"Validating manifest: {manifest_path}")
    success = validate_manifest.validate_manifest(manifest_path)
    print()
    
    return success


def save_results_json(results, output_file):
    """
    Save results to JSON file (converting numpy arrays to lists).
    
    Parameters
    ----------
    results : dict
        Results dictionary from run_cmb_comb_test
    output_file : Path
        Output JSON file path
    """
    # Create serializable copy (convert numpy arrays to lists)
    results_copy = {}
    for key, value in results.items():
        if isinstance(value, np.ndarray):
            results_copy[key] = value.tolist()
        elif isinstance(value, (np.integer, np.floating)):
            results_copy[key] = float(value)
        elif isinstance(value, dict):
            # Handle nested dicts (like all_periods)
            results_copy[key] = {
                str(k): {sk: float(sv) if isinstance(sv, (np.integer, np.floating)) else sv 
                        for sk, sv in v.items()}
                for k, v in value.items()
            }
        else:
            results_copy[key] = value
    
    with open(output_file, 'w') as f:
        json.dump(results_copy, f, indent=2)
    
    print(f"Results saved to: {output_file}")


def generate_combined_verdict(planck_results, wmap_results, output_file, variant):
    """
    Generate court-grade combined verdict markdown report.
    
    Parameters
    ----------
    planck_results : dict or None
        Results from Planck analysis
    wmap_results : dict or None
        Results from WMAP analysis
    output_file : Path
        Output markdown file path
    variant : str
        Architecture variant tested
    """
    with open(output_file, 'w') as f:
        f.write("# CMB Comb Fingerprint Test - Combined Verdict\n\n")
        f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
        f.write(f"**Protocol Version**: v1.0\n")
        f.write(f"**Architecture Variant**: {variant}\n\n")
        
        f.write("## Pre-Registered Candidate Periods\n\n")
        f.write("Δℓ ∈ {" + ", ".join(map(str, CANDIDATE_PERIODS)) + "} (LOCKED)\n\n")
        
        f.write("**IMPORTANT**: These candidate periods were pre-registered before data analysis. ")
        f.write("No modifications are permitted based on results.\n\n")
        
        f.write("---\n\n")
        
        # Planck results
        if planck_results is not None:
            f.write("## Planck PR3 Results\n\n")
            f.write(f"- **Dataset**: {planck_results.get('dataset', 'Planck PR3')}\n")
            f.write(f"- **Multipole range**: ℓ = {planck_results['ell'][0]} to {planck_results['ell'][-1]}\n")
            f.write(f"- **Whitening**: {'YES (full covariance)' if planck_results.get('whitened', False) else 'NO (diagonal uncertainties only)'}\n")
            f.write(f"- **MC trials**: {planck_results.get('n_mc_trials', 'N/A')}\n\n")
            
            f.write("### Statistical Results\n\n")
            f.write(f"- **Best-fit period**: Δℓ = {planck_results['best_period']}\n")
            f.write(f"- **Amplitude**: A = {planck_results['amplitude']:.6f}\n")
            f.write(f"- **Phase**: φ = {planck_results['phase']:.6f} rad ({np.degrees(planck_results['phase']):.2f}°)\n")
            f.write(f"- **Max Δχ²**: {planck_results['max_delta_chi2']:.6f}\n")
            f.write(f"- **P-value**: {planck_results['p_value']:.6e}\n")
            f.write(f"- **Significance**: **{planck_results['significance'].upper()}**\n\n")
        else:
            f.write("## Planck PR3 Results\n\n")
            f.write("*Not run*\n\n")
        
        f.write("---\n\n")
        
        # WMAP results
        if wmap_results is not None:
            f.write("## WMAP 9yr Results\n\n")
            f.write(f"- **Dataset**: {wmap_results.get('dataset', 'WMAP 9yr')}\n")
            f.write(f"- **Multipole range**: ℓ = {wmap_results['ell'][0]} to {wmap_results['ell'][-1]}\n")
            f.write(f"- **Whitening**: {'YES (full covariance)' if wmap_results.get('whitened', False) else 'NO (diagonal uncertainties only)'}\n")
            f.write(f"- **MC trials**: {wmap_results.get('n_mc_trials', 'N/A')}\n\n")
            
            f.write("### Statistical Results\n\n")
            f.write(f"- **Best-fit period**: Δℓ = {wmap_results['best_period']}\n")
            f.write(f"- **Amplitude**: A = {wmap_results['amplitude']:.6f}\n")
            f.write(f"- **Phase**: φ = {wmap_results['phase']:.6f} rad ({np.degrees(wmap_results['phase']):.2f}°)\n")
            f.write(f"- **Max Δχ²**: {wmap_results['max_delta_chi2']:.6f}\n")
            f.write(f"- **P-value**: {wmap_results['p_value']:.6e}\n")
            f.write(f"- **Significance**: **{wmap_results['significance'].upper()}**\n\n")
        else:
            f.write("## WMAP 9yr Results\n\n")
            f.write("*Not run*\n\n")
        
        f.write("---\n\n")
        
        # PASS/FAIL decision
        f.write("## PASS/FAIL Decision\n\n")
        f.write("### Decision Rules (from PROTOCOL.md)\n\n")
        f.write("A signal **PASSES** if ALL of the following hold:\n\n")
        f.write("1. Planck p-value < 0.01 (candidate or strong)\n")
        f.write("2. WMAP p-value < 0.05 (replication threshold)\n")
        f.write("3. Same period in Planck and WMAP (best-fit Δℓ matches)\n")
        f.write("4. Consistent phase (within π/2 radians)\n")
        f.write("5. Variant C is the active hypothesis\n\n")
        
        # Evaluate criteria
        if planck_results is not None and wmap_results is not None:
            criterion_1 = planck_results['p_value'] < 0.01
            criterion_2 = wmap_results['p_value'] < 0.05
            criterion_3 = planck_results['best_period'] == wmap_results['best_period']
            phase_diff = abs(planck_results['phase'] - wmap_results['phase'])
            phase_diff = min(phase_diff, 2*np.pi - phase_diff)  # Handle wrapping
            criterion_4 = phase_diff < np.pi / 2
            criterion_5 = variant == "C"
            
            f.write("### Criterion Evaluation\n\n")
            f.write(f"1. Planck p < 0.01: **{'✓ PASS' if criterion_1 else '✗ FAIL'}** (p = {planck_results['p_value']:.6e})\n")
            f.write(f"2. WMAP p < 0.05: **{'✓ PASS' if criterion_2 else '✗ FAIL'}** (p = {wmap_results['p_value']:.6e})\n")
            f.write(f"3. Same period: **{'✓ PASS' if criterion_3 else '✗ FAIL'}** (Planck: {planck_results['best_period']}, WMAP: {wmap_results['best_period']})\n")
            f.write(f"4. Consistent phase: **{'✓ PASS' if criterion_4 else '✗ FAIL'}** (Δφ = {phase_diff:.3f} rad)\n")
            f.write(f"5. Variant C: **{'✓ PASS' if criterion_5 else '✗ FAIL'}** (tested: {variant})\n\n")
            
            all_pass = criterion_1 and criterion_2 and criterion_3 and criterion_4 and criterion_5
            
            f.write("### Final Verdict\n\n")
            if all_pass:
                f.write("## ✓ **PASS**\n\n")
                f.write("All criteria satisfied. Candidate signal detected in both Planck and WMAP.\n\n")
                f.write("**Next steps**:\n")
                f.write("- Prepare manuscript for peer review\n")
                f.write("- Seek independent verification with third dataset\n")
                f.write("- Archive full results for reproducibility\n\n")
            else:
                f.write("## ✗ **FAIL** (Null Result)\n\n")
                f.write("One or more criteria not satisfied. No significant periodic signal detected.\n\n")
                f.write("**Interpretation**: The data do not support the hypothesis of periodic comb structure ")
                f.write("in CMB residuals at the tested candidate periods.\n\n")
        elif planck_results is not None:
            f.write("### Verdict: INCOMPLETE\n\n")
            f.write("Only Planck data analyzed. WMAP replication required for PASS/FAIL decision.\n\n")
            if planck_results['p_value'] < 0.01:
                f.write("**Planck result**: CANDIDATE signal detected. Requires WMAP confirmation.\n\n")
            else:
                f.write("**Planck result**: NULL. No significant signal in Planck data.\n\n")
        else:
            f.write("### Verdict: NO DATA\n\n")
            f.write("No analysis performed.\n\n")
        
        f.write("---\n\n")
        
        # Variant conditional statement
        f.write("## Conditional Statement\n\n")
        f.write(f"**This result is conditional on Variant {variant} assumptions.**\n\n")
        
        if variant == "C":
            f.write("Variant C (Explicit Frame Synchronization) predicts periodic comb structure ")
            f.write("in CMB residuals tied to Reed-Solomon code synchronization overhead.\n\n")
            f.write("If signal is detected, it supports the discrete spacetime architecture hypothesis. ")
            f.write("If null, Variant C is falsified in this form.\n")
        elif variant == "A":
            f.write("Variant A (No Explicit Synchronization) predicts **NO** periodic structure. ")
            f.write("This analysis serves as a null-hypothesis validation.\n")
        elif variant == "B":
            f.write("Variant B (Implicit Synchronization) predicts broad-band cutoff but **NO** periodicity. ")
            f.write("This CMB comb test is not the appropriate test for Variant B.\n")
        elif variant == "D":
            f.write("Variant D (Hierarchical Synchronization) predicts scale-dependent behavior. ")
            f.write("Results may vary by multipole range. Requires binned analysis.\n")
        
        f.write("\n---\n\n")
        
        # Court-grade mode warnings
        f.write("## Data Quality and Limitations\n\n")
        
        if planck_results is not None:
            if not planck_results.get('whitened', False):
                f.write("**WARNING (Planck)**: Diagonal uncertainties only. ")
                f.write("Full covariance matrix not provided. This is **candidate-grade only**. ")
                f.write("Court-grade analysis requires full covariance for proper error correlation.\n\n")
        
        if wmap_results is not None:
            if not wmap_results.get('whitened', False):
                f.write("**WARNING (WMAP)**: Diagonal uncertainties only. ")
                f.write("Full covariance matrix not provided. This is **candidate-grade only**. ")
                f.write("Court-grade analysis requires full covariance for proper error correlation.\n\n")
        
        f.write("---\n\n")
        f.write("**End of Report**\n")
    
    print(f"Combined verdict saved to: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="One-Command Real Data CMB Comb Test Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Minimal (Planck only):
  python run_real_data_cmb_comb.py \\
      --planck_obs data/planck_pr3/raw/spectrum.txt \\
      --planck_model data/planck_pr3/raw/model.txt

  # Full (Planck + WMAP with manifests):
  python run_real_data_cmb_comb.py \\
      --planck_obs data/planck_pr3/raw/spectrum.txt \\
      --planck_model data/planck_pr3/raw/model.txt \\
      --planck_manifest data/planck_pr3/manifests/sha256.json \\
      --wmap_obs data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \\
      --wmap_manifest data/wmap/manifests/sha256.json \\
      --variant C --mc_samples 10000

See forensic_fingerprint/RUNBOOK_REAL_DATA.md for complete documentation.
        """
    )
    
    # Planck data
    parser.add_argument('--planck_obs', type=str, help='Planck observed spectrum file')
    parser.add_argument('--planck_model', type=str, help='Planck model spectrum file (optional)')
    parser.add_argument('--planck_cov', type=str, help='Planck covariance file (optional, enables whitening)')
    parser.add_argument('--planck_manifest', type=str, help='Planck SHA-256 manifest for validation (optional)')
    parser.add_argument('--ell_min_planck', type=int, default=30, help='Planck min multipole (default: 30)')
    parser.add_argument('--ell_max_planck', type=int, default=1500, help='Planck max multipole (default: 1500)')
    
    # WMAP data
    parser.add_argument('--wmap_obs', type=str, help='WMAP observed spectrum file (optional)')
    parser.add_argument('--wmap_model', type=str, help='WMAP model spectrum file (optional)')
    parser.add_argument('--wmap_cov', type=str, help='WMAP covariance file (optional)')
    parser.add_argument('--wmap_manifest', type=str, help='WMAP SHA-256 manifest for validation (optional)')
    parser.add_argument('--ell_min_wmap', type=int, default=30, help='WMAP min multipole (default: 30)')
    parser.add_argument('--ell_max_wmap', type=int, default=800, help='WMAP max multipole (default: 800)')
    
    # Test parameters
    parser.add_argument('--variant', type=str, choices=['A', 'B', 'C', 'D'], default=DEFAULT_VARIANT,
                       help=f'Architecture variant to test (default: {DEFAULT_VARIANT})')
    parser.add_argument('--mc_samples', type=int, default=DEFAULT_MC_SAMPLES,
                       help=f'Number of Monte Carlo samples (default: {DEFAULT_MC_SAMPLES} for candidate-grade, 100000 for strong)')
    parser.add_argument('--seed', type=int, default=DEFAULT_SEED,
                       help=f'Random seed for reproducibility (default: {DEFAULT_SEED}, pre-registered)')
    
    # Output
    parser.add_argument('--output_dir', type=str, help='Output directory (default: auto-generated with timestamp)')
    
    args = parser.parse_args()
    
    # Validate inputs
    if args.planck_obs is None:
        parser.error("--planck_obs is required")
    
    # Generate output directory with timestamp
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = Path(__file__).parent / 'out' / 'real_runs' / f"cmb_comb_{timestamp}"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create figures subdirectory
    figures_dir = output_dir / 'figures'
    figures_dir.mkdir(exist_ok=True)
    
    print("="*80)
    print("UBT FORENSIC FINGERPRINT - ONE-COMMAND CMB COMB TEST")
    print("="*80)
    print(f"Output directory: {output_dir}")
    print(f"Variant: {args.variant}")
    print(f"MC samples: {args.mc_samples}")
    print(f"Random seed: {args.seed}")
    print()
    
    # Validate manifests if provided
    if args.planck_manifest:
        print("Validating Planck manifest...")
        if not validate_data_manifest(args.planck_manifest):
            print("ERROR: Planck manifest validation failed. Aborting.")
            sys.exit(1)
    
    if args.wmap_manifest:
        print("Validating WMAP manifest...")
        if not validate_data_manifest(args.wmap_manifest):
            print("ERROR: WMAP manifest validation failed. Aborting.")
            sys.exit(1)
    
    # Run Planck analysis
    planck_results = None
    if args.planck_obs:
        print("="*80)
        print("RUNNING PLANCK PR3 ANALYSIS")
        print("="*80)
        print()
        
        # Load Planck data
        print("Loading Planck data...")
        planck_data = planck.load_planck_data(
            obs_file=args.planck_obs,
            model_file=args.planck_model,
            cov_file=args.planck_cov,
            ell_min=args.ell_min_planck,
            ell_max=args.ell_max_planck,
            dataset_name="Planck PR3"
        )
        
        print(f"Loaded {planck_data['n_multipoles']} multipoles (ℓ = {planck_data['ell_range'][0]} to {planck_data['ell_range'][1]})")
        print()
        
        # Run CMB comb test
        planck_results = cmb_comb.run_cmb_comb_test(
            ell=planck_data['ell'],
            C_obs=planck_data['cl_obs'],
            C_model=planck_data['cl_model'] if planck_data['cl_model'] is not None else planck_data['cl_obs'] * 0,
            sigma=planck_data['sigma'],
            cov=planck_data['cov'],
            dataset_name=planck_data['dataset'],
            variant=args.variant,
            n_mc_trials=args.mc_samples,
            random_seed=args.seed,
            output_dir=None  # Don't auto-save, we'll do it manually
        )
        
        # Save results
        save_results_json(planck_results, output_dir / 'planck_results.json')
        
        # Generate plots
        print("Generating Planck plots...")
        cmb_comb.plot_results(planck_results, figures_dir)
        print()
    
    # Run WMAP analysis
    wmap_results = None
    if args.wmap_obs:
        print("="*80)
        print("RUNNING WMAP 9YR ANALYSIS")
        print("="*80)
        print()
        
        # Load WMAP data
        print("Loading WMAP data...")
        wmap_data = wmap.load_wmap_data(
            obs_file=args.wmap_obs,
            model_file=args.wmap_model,
            cov_file=args.wmap_cov,
            ell_min=args.ell_min_wmap,
            ell_max=args.ell_max_wmap,
            dataset_name="WMAP 9yr"
        )
        
        print(f"Loaded {wmap_data['n_multipoles']} multipoles (ℓ = {wmap_data['ell_range'][0]} to {wmap_data['ell_range'][1]})")
        print()
        
        # Run CMB comb test
        wmap_results = cmb_comb.run_cmb_comb_test(
            ell=wmap_data['ell'],
            C_obs=wmap_data['cl_obs'],
            C_model=wmap_data['cl_model'] if wmap_data['cl_model'] is not None else wmap_data['cl_obs'] * 0,
            sigma=wmap_data['sigma'],
            cov=wmap_data['cov'],
            dataset_name=wmap_data['dataset'],
            variant=args.variant,
            n_mc_trials=args.mc_samples,
            random_seed=args.seed,
            output_dir=None  # Don't auto-save, we'll do it manually
        )
        
        # Save results
        save_results_json(wmap_results, output_dir / 'wmap_results.json')
        
        # Generate plots
        print("Generating WMAP plots...")
        cmb_comb.plot_results(wmap_results, figures_dir)
        print()
    
    # Generate combined verdict
    print("="*80)
    print("GENERATING COMBINED VERDICT")
    print("="*80)
    print()
    
    generate_combined_verdict(
        planck_results,
        wmap_results,
        output_dir / 'combined_verdict.md',
        args.variant
    )
    
    print()
    print("="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    print(f"\nAll results saved to: {output_dir}")
    print(f"\nKey files:")
    if planck_results:
        print(f"  - planck_results.json")
    if wmap_results:
        print(f"  - wmap_results.json")
    print(f"  - combined_verdict.md (READ THIS FOR PASS/FAIL DECISION)")
    print(f"  - figures/*.png\n")
    
    # Print quick summary
    if planck_results and wmap_results:
        print("Quick Summary:")
        print(f"  Planck: p = {planck_results['p_value']:.6e}, period = {planck_results['best_period']}, sig = {planck_results['significance']}")
        print(f"  WMAP:   p = {wmap_results['p_value']:.6e}, period = {wmap_results['best_period']}, sig = {wmap_results['significance']}")
        print(f"\nSee combined_verdict.md for detailed PASS/FAIL evaluation.\n")


if __name__ == '__main__':
    main()
