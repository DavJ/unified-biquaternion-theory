#!/usr/bin/env python3
"""
UBT Forensic Fingerprint - Stress Test #2: Polarization Channels (EE, TE)
==========================================================================

Test whether the candidate structural signal propagates to polarization channels.

This script:
1. Loads Planck EE and TE spectra
2. Runs the CMB comb test independently on each channel
3. Compares results with TT channel
4. Generates joint TT/EE/TE summary table

PASS/FAIL Criteria:
- STRONG PASS: Δℓ ≈ 255 appears in EE and/or TE with p ≤ 10⁻³
- WEAK PASS: Δℓ ≈ 255 appears with reduced amplitude but aligned phase
- FAIL: No structure near 255 in polarization channels

Skeptic One-Liner:
"If the Δℓ = 255 signal were caused by a TT-only instrumental artifact or scalar 
mode contamination, it would NOT appear in polarization channels (EE, TE). Presence 
in polarization would suggest a field-level structural feature. It does or does not."

Note: A real structural/digital fingerprint should propagate to polarization.
Instrumental or scalar TT artifacts generally will NOT.

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


def run_polarization_stress_test(
    tt_obs_file=None, tt_model_file=None,
    ee_obs_file=None, ee_model_file=None,
    te_obs_file=None, te_model_file=None,
    ell_min=30, ell_max=1500,
    output_dir=None, n_mc_trials=5000
):
    """
    Run polarization stress test on Planck data.
    
    Parameters
    ----------
    tt_obs_file : str or Path, optional
        TT observation file (for comparison)
    tt_model_file : str or Path, optional
        TT model file
    ee_obs_file : str or Path, optional
        EE observation file
    ee_model_file : str or Path, optional
        EE model file
    te_obs_file : str or Path, optional
        TE observation file
    te_model_file : str or Path, optional
        TE model file
    ell_min : int
        Minimum multipole
    ell_max : int
        Maximum multipole
    output_dir : str or Path, optional
        Output directory
    n_mc_trials : int
        Number of Monte Carlo trials
    
    Returns
    -------
    dict
        Results for each channel
    """
    # Setup output directory
    if output_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = repo_root / 'forensic_fingerprint' / 'out' / 'stress_tests' / f'polarization_{timestamp}'
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("="*80)
    print("STRESS TEST #2: POLARIZATION CHANNELS (EE, TE)")
    print("="*80)
    print(f"Output directory: {output_dir}")
    print()
    
    results_all = {}
    
    # Test TT (for comparison if provided)
    if tt_obs_file is not None:
        print("="*80)
        print("TESTING TT CHANNEL (for comparison)")
        print("="*80)
        print()
        
        tt_data = planck.load_planck_data(
            obs_file=tt_obs_file,
            model_file=tt_model_file,
            ell_min=ell_min,
            ell_max=ell_max,
            dataset_name="Planck PR3 TT",
            spectrum_type="TT"
        )
        
        tt_results = cmb_comb.run_cmb_comb_test(
            ell=tt_data['ell'],
            C_obs=tt_data['cl_obs'],
            C_model=tt_data['cl_model'] if tt_data['cl_model'] is not None else tt_data['cl_obs'] * 0,
            sigma=tt_data['sigma'],
            cov=tt_data['cov'],
            dataset_name="Planck PR3 TT",
            variant="C",
            n_mc_trials=n_mc_trials,
            random_seed=42,
            whiten_mode='diagonal',
            output_dir=None
        )
        
        results_all['TT'] = tt_results
        
        # Save TT results
        tt_dir = output_dir / 'TT'
        tt_dir.mkdir(exist_ok=True)
        cmb_comb.save_results(tt_results, tt_dir)
        cmb_comb.plot_results(tt_results, tt_dir)
        print()
    
    # Test EE
    if ee_obs_file is not None:
        print("="*80)
        print("TESTING EE CHANNEL")
        print("="*80)
        print()
        
        ee_data = planck.load_planck_data(
            obs_file=ee_obs_file,
            model_file=ee_model_file,
            ell_min=ell_min,
            ell_max=ell_max,
            dataset_name="Planck PR3 EE",
            spectrum_type="EE"
        )
        
        ee_results = cmb_comb.run_cmb_comb_test(
            ell=ee_data['ell'],
            C_obs=ee_data['cl_obs'],
            C_model=ee_data['cl_model'] if ee_data['cl_model'] is not None else ee_data['cl_obs'] * 0,
            sigma=ee_data['sigma'],
            cov=ee_data['cov'],
            dataset_name="Planck PR3 EE",
            variant="C",
            n_mc_trials=n_mc_trials,
            random_seed=42,
            whiten_mode='diagonal',
            output_dir=None
        )
        
        results_all['EE'] = ee_results
        
        # Save EE results
        ee_dir = output_dir / 'EE'
        ee_dir.mkdir(exist_ok=True)
        cmb_comb.save_results(ee_results, ee_dir)
        cmb_comb.plot_results(ee_results, ee_dir)
        print()
    
    # Test TE
    if te_obs_file is not None:
        print("="*80)
        print("TESTING TE CHANNEL")
        print("="*80)
        print()
        
        te_data = planck.load_planck_data(
            obs_file=te_obs_file,
            model_file=te_model_file,
            ell_min=ell_min,
            ell_max=ell_max,
            dataset_name="Planck PR3 TE",
            spectrum_type="TE"
        )
        
        te_results = cmb_comb.run_cmb_comb_test(
            ell=te_data['ell'],
            C_obs=te_data['cl_obs'],
            C_model=te_data['cl_model'] if te_data['cl_model'] is not None else te_data['cl_obs'] * 0,
            sigma=te_data['sigma'],
            cov=te_data['cov'],
            dataset_name="Planck PR3 TE",
            variant="C",
            n_mc_trials=n_mc_trials,
            random_seed=42,
            whiten_mode='diagonal',
            output_dir=None
        )
        
        results_all['TE'] = te_results
        
        # Save TE results
        te_dir = output_dir / 'TE'
        te_dir.mkdir(exist_ok=True)
        cmb_comb.save_results(te_results, te_dir)
        cmb_comb.plot_results(te_results, te_dir)
        print()
    
    # Generate comparison report
    generate_polarization_report(results_all, output_dir)
    
    # Save combined JSON
    save_polarization_json(results_all, output_dir)
    
    return results_all


def generate_polarization_report(results_all, output_dir):
    """Generate markdown comparison report for polarization channels."""
    output_file = output_dir / 'polarization_comparison.md'
    
    with open(output_file, 'w') as f:
        f.write("# Stress Test #2: Polarization Channels (EE, TE)\n\n")
        f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## Objective\n\n")
        f.write("Test whether the candidate structural signal at Δℓ ≈ 255 propagates ")
        f.write("to polarization channels (EE, TE). A real structural/digital fingerprint ")
        f.write("should appear in polarization. Instrumental or scalar TT artifacts generally will NOT.\n\n")
        
        f.write("## Results Summary\n\n")
        f.write("| Channel | Best Δℓ | Amplitude | Phase (rad) | Max Δχ² | p-value | Significance |\n")
        f.write("|---------|---------|-----------|-------------|---------|---------|-------------|\n")
        
        for channel, results in results_all.items():
            f.write(f"| {channel:7s} | {results['best_period']:7d} | "
                   f"{results['amplitude']:9.4f} | {results['phase']:11.4f} | "
                   f"{results['max_delta_chi2']:7.2f} | {results['p_value']:7.2e} | "
                   f"{results['significance']:12s} |\n")
        
        f.write("\n## PASS/FAIL Assessment\n\n")
        
        # Extract results
        ee_present = 'EE' in results_all
        te_present = 'TE' in results_all
        
        if ee_present:
            ee_period_255 = abs(results_all['EE']['best_period'] - 255) <= 2
            ee_significant = results_all['EE']['p_value'] < 0.001
        else:
            ee_period_255 = False
            ee_significant = False
        
        if te_present:
            te_period_255 = abs(results_all['TE']['best_period'] - 255) <= 2
            te_significant = results_all['TE']['p_value'] < 0.001
        else:
            te_period_255 = False
            te_significant = False
        
        # Check phase alignment if TT is present
        phase_aligned_ee = False
        phase_aligned_te = False
        
        if 'TT' in results_all:
            tt_phase = results_all['TT']['phase']
            
            if ee_present:
                ee_phase = results_all['EE']['phase']
                phase_diff_ee = abs(tt_phase - ee_phase)
                phase_diff_ee = min(phase_diff_ee, 2*np.pi - phase_diff_ee)
                phase_aligned_ee = phase_diff_ee < np.pi / 2
            
            if te_present:
                te_phase = results_all['TE']['phase']
                phase_diff_te = abs(tt_phase - te_phase)
                phase_diff_te = min(phase_diff_te, 2*np.pi - phase_diff_te)
                phase_aligned_te = phase_diff_te < np.pi / 2
        
        # Determine verdict
        strong_pass = (ee_period_255 and ee_significant) or (te_period_255 and te_significant)
        weak_pass = ((ee_period_255 and phase_aligned_ee) or 
                    (te_period_255 and phase_aligned_te))
        
        if strong_pass:
            f.write("### ✓ STRONG PASS\n\n")
            f.write("- Δℓ ≈ 255 appears in polarization with p ≤ 10⁻³\n")
            if ee_period_255 and ee_significant:
                f.write(f"  - EE: Δℓ = {results_all['EE']['best_period']}, p = {results_all['EE']['p_value']:.2e}\n")
            if te_period_255 and te_significant:
                f.write(f"  - TE: Δℓ = {results_all['TE']['best_period']}, p = {results_all['TE']['p_value']:.2e}\n")
            f.write("- Signal propagates to polarization channels\n")
            f.write("- Consistent with structural/digital fingerprint hypothesis\n\n")
        elif weak_pass:
            f.write("### ~ WEAK PASS\n\n")
            f.write("- Δℓ ≈ 255 appears in polarization with reduced amplitude but aligned phase\n")
            f.write("- Signal partially propagates to polarization\n")
            f.write("- Warrants further investigation\n\n")
        else:
            f.write("### ✗ FAIL\n\n")
            f.write("- No significant structure near Δℓ = 255 in polarization channels\n")
            f.write("- Signal does NOT propagate to polarization\n")
            f.write("- Suggests TT candidate may be instrumental or scalar artifact\n\n")
        
        f.write("## Interpretation\n\n")
        f.write("The polarization test checks whether the candidate signal is a true ")
        f.write("structural property of the CMB or an artifact specific to temperature measurements. ")
        f.write("A genuine digital/lattice structure should imprint on all CMB observables.\n\n")
        
        if strong_pass or weak_pass:
            f.write("**Result**: The signal shows evidence in polarization channels. ")
            f.write("This increases confidence in the structural hypothesis.\n")
        else:
            f.write("**Result**: The signal does NOT appear in polarization. ")
            f.write("This suggests the TT candidate is likely instrumental or a statistical fluctuation.\n")
    
    print(f"Polarization report saved to: {output_file}")


def save_polarization_json(results_all, output_dir):
    """Save combined polarization results to JSON."""
    # Save EE results
    if 'EE' in results_all:
        ee_json = {
            'best_period': int(results_all['EE']['best_period']),
            'amplitude': float(results_all['EE']['amplitude']),
            'phase': float(results_all['EE']['phase']),
            'max_delta_chi2': float(results_all['EE']['max_delta_chi2']),
            'p_value': float(results_all['EE']['p_value']),
            'significance': results_all['EE']['significance'],
            'n_mc_trials': results_all['EE']['n_mc_trials']
        }
        with open(output_dir / 'planck_EE_results.json', 'w') as f:
            json.dump(ee_json, f, indent=2)
        print(f"EE results saved to: {output_dir / 'planck_EE_results.json'}")
    
    # Save TE results
    if 'TE' in results_all:
        te_json = {
            'best_period': int(results_all['TE']['best_period']),
            'amplitude': float(results_all['TE']['amplitude']),
            'phase': float(results_all['TE']['phase']),
            'max_delta_chi2': float(results_all['TE']['max_delta_chi2']),
            'p_value': float(results_all['TE']['p_value']),
            'significance': results_all['TE']['significance'],
            'n_mc_trials': results_all['TE']['n_mc_trials']
        }
        with open(output_dir / 'planck_TE_results.json', 'w') as f:
            json.dump(te_json, f, indent=2)
        print(f"TE results saved to: {output_dir / 'planck_TE_results.json'}")


def main():
    parser = argparse.ArgumentParser(
        description="Stress Test #2: Polarization Channels (EE, TE)",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--tt_obs', type=str,
                       help='TT observation file (for comparison)')
    parser.add_argument('--tt_model', type=str,
                       help='TT model file')
    parser.add_argument('--ee_obs', type=str,
                       help='EE observation file')
    parser.add_argument('--ee_model', type=str,
                       help='EE model file')
    parser.add_argument('--te_obs', type=str,
                       help='TE observation file')
    parser.add_argument('--te_model', type=str,
                       help='TE model file')
    parser.add_argument('--ell_min', type=int, default=30,
                       help='Minimum multipole (default: 30)')
    parser.add_argument('--ell_max', type=int, default=1500,
                       help='Maximum multipole (default: 1500)')
    parser.add_argument('--output_dir', type=str,
                       help='Output directory (default: auto-generated)')
    parser.add_argument('--mc_trials', type=int, default=5000,
                       help='Number of MC trials (default: 5000)')
    
    args = parser.parse_args()
    
    # Check that at least one polarization file is provided
    if args.ee_obs is None and args.te_obs is None:
        parser.error("Must provide at least one of --ee_obs or --te_obs")
    
    results = run_polarization_stress_test(
        tt_obs_file=args.tt_obs,
        tt_model_file=args.tt_model,
        ee_obs_file=args.ee_obs,
        ee_model_file=args.ee_model,
        te_obs_file=args.te_obs,
        te_model_file=args.te_model,
        ell_min=args.ell_min,
        ell_max=args.ell_max,
        output_dir=args.output_dir,
        n_mc_trials=args.mc_trials
    )
    
    print("\n" + "="*80)
    print("POLARIZATION STRESS TEST COMPLETE")
    print("="*80)
    print("\nSee polarization_comparison.md for detailed results.\n")


if __name__ == '__main__':
    main()
