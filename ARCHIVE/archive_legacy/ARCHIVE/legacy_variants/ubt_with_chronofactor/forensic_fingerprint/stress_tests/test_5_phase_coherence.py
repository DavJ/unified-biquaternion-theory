#!/usr/bin/env python3
"""
UBT Forensic Fingerprint - Stress Test #5: Phase Coherence
===========================================================

Test whether the phase of the Δℓ = 255 signal is stable across:
- Different datasets (Planck vs WMAP)
- Different preprocessing (raw vs whitened)

This script:
1. Extracts phase φ from multiple datasets and preprocessing modes
2. Computes phase dispersion across conditions
3. Calculates cross-dataset phase differences
4. Tests whether phase is random or coherent

PASS/FAIL Criteria:
- PASS: Phase remains stable within a few degrees across datasets/preprocessing
- FAIL: Phase is random or unstable (varies > 30° between conditions)

Skeptic One-Liner:
"If the Δℓ = 255 signal were caused by random noise or uncorrelated instrumental 
artifacts, phase would be random across datasets. Coherent phase across Planck 
and WMAP, both raw and whitened, would suggest a physical or systematic origin."

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
import wmap
import cmb_comb


def extract_phase_from_dataset(
    obs_file, model_file, cov_file=None, 
    dataset_name="Unknown",
    ell_min=30, ell_max=1500,
    whiten_modes=['diagonal', 'covariance'],
    target_period=255,
    n_mc_trials=1000
):
    """
    Extract phase φ for target period from a dataset with multiple whitening modes.
    
    Parameters
    ----------
    obs_file : str or Path
        Observation file
    model_file : str or Path
        Model file
    cov_file : str or Path, optional
        Covariance file
    dataset_name : str
        Dataset identifier
    ell_min, ell_max : int
        Multipole range
    whiten_modes : list
        Whitening modes to test
    target_period : int
        Period to extract phase for (default: 255)
    n_mc_trials : int
        Number of MC trials for significance
    
    Returns
    -------
    dict
        Results for each whitening mode with phase information
    """
    print(f"\nProcessing {dataset_name}...")
    print(f"  Observation file: {obs_file}")
    print(f"  Model file: {model_file}")
    print(f"  Covariance file: {cov_file if cov_file else 'None (diagonal only)'}")
    
    # Determine which loader to use based on dataset name
    if 'planck' in dataset_name.lower():
        loader = planck.load_planck_data
    elif 'wmap' in dataset_name.lower():
        loader = wmap.load_wmap_data
    else:
        # Default to planck loader for custom datasets
        loader = planck.load_planck_data
    
    # Load data
    data = loader(
        obs_file=obs_file,
        model_file=model_file,
        cov_file=cov_file,
        ell_min=ell_min,
        ell_max=ell_max,
        dataset_name=dataset_name
    )
    
    print(f"  Loaded {data['n_multipoles']} multipoles (ℓ = {data['ell_range'][0]} to {data['ell_range'][1]})")
    
    results = {}
    
    for whiten_mode in whiten_modes:
        print(f"\n  Whitening mode: {whiten_mode}")
        
        # Skip covariance mode if no covariance available
        if whiten_mode == 'covariance' and cov_file is None:
            print(f"    Skipping (no covariance file)")
            continue
        
        # Run comb test
        test_results = cmb_comb.run_cmb_comb_test(
            ell=data['ell'],
            C_obs=data['cl_obs'],
            C_model=data['cl_model'] if data['cl_model'] is not None else data['cl_obs'] * 0,
            sigma=data['sigma'],
            cov=data['cov'] if whiten_mode == 'covariance' else None,
            dataset_name=f"{dataset_name} ({whiten_mode})",
            whiten_mode=whiten_mode,
            n_mc_trials=n_mc_trials,
            output_dir=None  # Don't save intermediate results
        )
        
        # Extract phase for target period
        if target_period in test_results['all_periods']:
            period_data = test_results['all_periods'][target_period]
            phase_rad = period_data['phase']
            phase_deg = np.degrees(phase_rad)
            amplitude = period_data['amplitude']
            delta_chi2 = period_data['delta_chi2']
        else:
            # If target period not in candidate list, compute it
            delta_chi2, amplitude, phase_rad = cmb_comb.compute_delta_chi2(
                data['ell'], test_results['residuals'], target_period
            )
            phase_deg = np.degrees(phase_rad)
        
        # Store results
        results[whiten_mode] = {
            'phase_rad': float(phase_rad),
            'phase_deg': float(phase_deg),
            'amplitude': float(amplitude),
            'delta_chi2': float(delta_chi2),
            'best_period': int(test_results['best_period']),
            'p_value': float(test_results['p_value'])
        }
        
        print(f"    Phase at Δℓ={target_period}: φ = {phase_deg:.2f}° ({phase_rad:.4f} rad)")
        print(f"    Amplitude: A = {amplitude:.4f}")
        print(f"    Best period: Δℓ = {test_results['best_period']} (p = {test_results['p_value']:.2e})")
    
    return results


def compute_phase_statistics(phase_results):
    """
    Compute phase coherence statistics across datasets and modes.
    
    Parameters
    ----------
    phase_results : dict
        Nested dict: {dataset: {mode: {phase_deg, ...}}}
    
    Returns
    -------
    dict
        Statistics including:
        - phase_dispersion: circular standard deviation
        - phase_range: max - min phase
        - pairwise_differences: all pairwise phase differences
        - coherence_score: measure of phase alignment (0-1)
    """
    # Collect all phases (in radians for circular statistics)
    all_phases_rad = []
    all_phases_deg = []
    phase_list = []  # For tracking (dataset, mode, phase)
    
    for dataset, modes in phase_results.items():
        for mode, data in modes.items():
            phase_rad = data['phase_rad']
            phase_deg = data['phase_deg']
            all_phases_rad.append(phase_rad)
            all_phases_deg.append(phase_deg)
            phase_list.append((dataset, mode, phase_deg))
    
    # Convert to numpy arrays
    all_phases_rad = np.array(all_phases_rad)
    all_phases_deg = np.array(all_phases_deg)
    
    # Circular mean (using complex exponential)
    z = np.mean(np.exp(1j * all_phases_rad))
    circular_mean_rad = np.angle(z)
    circular_mean_deg = np.degrees(circular_mean_rad)
    
    # Circular dispersion (1 - |mean resultant length|)
    mean_resultant_length = np.abs(z)
    circular_dispersion = 1.0 - mean_resultant_length
    
    # Circular standard deviation (approximation)
    if mean_resultant_length > 0:
        circular_std_rad = np.sqrt(-2 * np.log(mean_resultant_length))
        circular_std_deg = np.degrees(circular_std_rad)
    else:
        circular_std_rad = np.pi
        circular_std_deg = 180.0
    
    # Phase range (careful with wraparound)
    # Normalize all phases to [-180, 180]
    phases_normalized = np.array([(p + 180) % 360 - 180 for p in all_phases_deg])
    phase_range = np.max(phases_normalized) - np.min(phases_normalized)
    
    # Compute all pairwise differences
    pairwise_diffs = []
    for i, (ds1, mode1, p1) in enumerate(phase_list):
        for j, (ds2, mode2, p2) in enumerate(phase_list):
            if i < j:  # Avoid duplicates
                # Angular difference (minimum angle between two angles)
                diff = abs(p1 - p2)
                if diff > 180:
                    diff = 360 - diff
                pairwise_diffs.append({
                    'dataset1': ds1,
                    'mode1': mode1,
                    'dataset2': ds2,
                    'mode2': mode2,
                    'phase_diff_deg': float(diff)
                })
    
    # Coherence score: 0 (random) to 1 (perfect alignment)
    # Based on mean resultant length
    coherence_score = mean_resultant_length
    
    stats = {
        'circular_mean_deg': float(circular_mean_deg),
        'circular_std_deg': float(circular_std_deg),
        'circular_dispersion': float(circular_dispersion),
        'phase_range_deg': float(phase_range),
        'mean_resultant_length': float(mean_resultant_length),
        'coherence_score': float(coherence_score),
        'n_measurements': len(all_phases_rad),
        'pairwise_differences': pairwise_diffs,
        'all_phases': phase_list
    }
    
    return stats


def assess_phase_coherence(stats, threshold_coherence=0.9, threshold_std_deg=15.0):
    """
    Assess whether phase is coherent based on statistics.
    
    Parameters
    ----------
    stats : dict
        Phase statistics from compute_phase_statistics
    threshold_coherence : float
        Minimum coherence score for PASS (default: 0.9)
    threshold_std_deg : float
        Maximum circular std dev for PASS (default: 15°)
    
    Returns
    -------
    str
        'PASS' or 'FAIL'
    dict
        Detailed verdict
    """
    coherence = stats['coherence_score']
    std_deg = stats['circular_std_deg']
    
    # Check criteria
    coherence_pass = coherence >= threshold_coherence
    std_pass = std_deg <= threshold_std_deg
    
    # Overall verdict
    if coherence_pass and std_pass:
        verdict = 'PASS'
        interpretation = (
            f"Phase is COHERENT across datasets and preprocessing modes. "
            f"Coherence score = {coherence:.3f} (≥ {threshold_coherence}), "
            f"circular std = {std_deg:.1f}° (≤ {threshold_std_deg}°). "
            f"This suggests the signal has a consistent structural origin."
        )
    else:
        verdict = 'FAIL'
        reasons = []
        if not coherence_pass:
            reasons.append(f"coherence = {coherence:.3f} < {threshold_coherence}")
        if not std_pass:
            reasons.append(f"circular std = {std_deg:.1f}° > {threshold_std_deg}°")
        
        interpretation = (
            f"Phase is INCOHERENT ({', '.join(reasons)}). "
            f"Random or varying phase suggests noise or uncorrelated artifacts."
        )
    
    verdict_detail = {
        'verdict': verdict,
        'coherence_pass': coherence_pass,
        'std_pass': std_pass,
        'interpretation': interpretation,
        'coherence_score': coherence,
        'circular_std_deg': std_deg,
        'threshold_coherence': threshold_coherence,
        'threshold_std_deg': threshold_std_deg
    }
    
    return verdict, verdict_detail


def generate_phase_stability_report(phase_results, stats, verdict_detail, output_dir):
    """
    Generate phase_stability_report.md with detailed analysis.
    
    Parameters
    ----------
    phase_results : dict
        Phase extraction results
    stats : dict
        Phase statistics
    verdict_detail : dict
        Verdict information
    output_dir : Path
        Output directory
    """
    output_file = output_dir / 'phase_stability_report.md'
    
    with open(output_file, 'w') as f:
        f.write("# Phase Coherence Test - Stability Report\n\n")
        f.write("**Test**: Stress Test #5 - Phase Coherence  \n")
        f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n")
        f.write("**Objective**: Test whether the Δℓ = 255 signal phase is stable across datasets and preprocessing  \n\n")
        
        f.write("---\n\n")
        
        # Skeptic one-liner
        f.write("## Skeptic Statement\n\n")
        f.write("> **If the Δℓ = 255 signal were caused by random noise or uncorrelated "
                "instrumental artifacts, phase would be random across datasets. "
                "Coherent phase across Planck and WMAP, both raw and whitened, would "
                "suggest a physical or systematic origin.**\n\n")
        
        f.write("---\n\n")
        
        # Overall verdict
        f.write("## Verdict\n\n")
        f.write(f"**Result**: {verdict_detail['verdict']}  \n")
        f.write(f"**Coherence Score**: {verdict_detail['coherence_score']:.3f} "
                f"({'≥' if verdict_detail['coherence_pass'] else '<'} {verdict_detail['threshold_coherence']})  \n")
        f.write(f"**Circular Std Dev**: {verdict_detail['circular_std_deg']:.1f}° "
                f"({'≤' if verdict_detail['std_pass'] else '>'} {verdict_detail['threshold_std_deg']}°)  \n\n")
        f.write(f"**Interpretation**: {verdict_detail['interpretation']}\n\n")
        
        f.write("---\n\n")
        
        # Phase measurements table
        f.write("## Phase Measurements (Δℓ = 255)\n\n")
        f.write("| Dataset | Whitening Mode | Phase (deg) | Phase (rad) | Amplitude | Best Period | p-value |\n")
        f.write("|---------|----------------|-------------|-------------|-----------|-------------|----------|\n")
        
        for dataset, modes in phase_results.items():
            for mode, data in modes.items():
                f.write(f"| {dataset} | {mode} | {data['phase_deg']:7.2f} | "
                       f"{data['phase_rad']:6.4f} | {data['amplitude']:6.4f} | "
                       f"{data['best_period']:3d} | {data['p_value']:8.2e} |\n")
        
        f.write("\n---\n\n")
        
        # Statistics
        f.write("## Phase Coherence Statistics\n\n")
        f.write(f"- **Circular Mean**: {stats['circular_mean_deg']:.2f}°\n")
        f.write(f"- **Circular Std Dev**: {stats['circular_std_deg']:.2f}°\n")
        f.write(f"- **Phase Range**: {stats['phase_range_deg']:.2f}°\n")
        f.write(f"- **Mean Resultant Length**: {stats['mean_resultant_length']:.3f}\n")
        f.write(f"- **Coherence Score**: {stats['coherence_score']:.3f}\n")
        f.write(f"- **Number of Measurements**: {stats['n_measurements']}\n\n")
        
        f.write("### Interpretation Guide\n\n")
        f.write("- **Coherence Score**: 0 (random phases) to 1 (perfect alignment)\n")
        f.write("- **Circular Std Dev**: Lower is better (< 15° suggests coherent signal)\n")
        f.write("- **Phase Range**: Total spread in phase measurements\n\n")
        
        f.write("---\n\n")
        
        # Pairwise differences
        f.write("## Pairwise Phase Differences\n\n")
        f.write("| Dataset 1 | Mode 1 | Dataset 2 | Mode 2 | Δφ (deg) |\n")
        f.write("|-----------|--------|-----------|--------|----------|\n")
        
        for diff in stats['pairwise_differences']:
            f.write(f"| {diff['dataset1']} | {diff['mode1']} | "
                   f"{diff['dataset2']} | {diff['mode2']} | "
                   f"{diff['phase_diff_deg']:6.2f} |\n")
        
        # Summary of differences
        if stats['pairwise_differences']:
            diff_values = [d['phase_diff_deg'] for d in stats['pairwise_differences']]
            f.write(f"\n**Mean pairwise difference**: {np.mean(diff_values):.2f}°  \n")
            f.write(f"**Max pairwise difference**: {np.max(diff_values):.2f}°  \n")
            f.write(f"**Min pairwise difference**: {np.min(diff_values):.2f}°  \n\n")
        
        f.write("---\n\n")
        
        # PASS/FAIL criteria
        f.write("## PASS/FAIL Criteria\n\n")
        f.write("### PASS Conditions\n")
        f.write(f"- Coherence score ≥ {verdict_detail['threshold_coherence']} ✓ " if verdict_detail['coherence_pass'] else f"- Coherence score ≥ {verdict_detail['threshold_coherence']} ✗ ")
        f.write(f"({verdict_detail['coherence_score']:.3f})\n")
        f.write(f"- Circular std dev ≤ {verdict_detail['threshold_std_deg']}° ✓ " if verdict_detail['std_pass'] else f"- Circular std dev ≤ {verdict_detail['threshold_std_deg']}° ✗ ")
        f.write(f"({verdict_detail['circular_std_deg']:.1f}°)\n\n")
        
        f.write("### FAIL Conditions\n")
        f.write("- Phase is random or varies > 30° between datasets\n")
        f.write("- No consistent phase alignment across preprocessing modes\n\n")
        
        f.write("---\n\n")
        
        # Conclusion
        f.write("## Conclusion\n\n")
        if verdict_detail['verdict'] == 'PASS':
            f.write("The Δℓ = 255 signal exhibits **coherent phase** across multiple datasets "
                   "and preprocessing modes. This consistency suggests the signal has a "
                   "structural origin rather than being random noise.\n\n")
            f.write("**Next Steps**:\n")
            f.write("- Independent replication with additional datasets\n")
            f.write("- Physical interpretation (if warranted)\n")
            f.write("- Cross-check with polarization channels\n")
        else:
            f.write("The Δℓ = 255 signal does **NOT** exhibit coherent phase. Phase varies "
                   "significantly across datasets or preprocessing modes, suggesting the "
                   "signal may be noise or uncorrelated artifacts.\n\n")
            f.write("**Interpretation**: This test **FAILED** to support the hypothesis of "
                   "a coherent structural signal.\n")
        
        f.write("\n---\n\n")
        f.write("*This report was generated automatically by test_5_phase_coherence.py*\n")
    
    print(f"\nPhase stability report saved to: {output_file}")


def run_phase_coherence_test(
    planck_obs, planck_model, planck_cov=None,
    wmap_obs=None, wmap_model=None, wmap_cov=None,
    ell_min=30, ell_max=800,
    output_dir=None,
    n_mc_trials=1000,
    target_period=255
):
    """
    Run phase coherence stress test.
    
    Parameters
    ----------
    planck_obs, planck_model : str or Path
        Planck observation and model files (required)
    planck_cov : str or Path, optional
        Planck covariance file
    wmap_obs, wmap_model : str or Path, optional
        WMAP observation and model files
    wmap_cov : str or Path, optional
        WMAP covariance file
    ell_min, ell_max : int
        Multipole range (should be compatible with both datasets)
    output_dir : str or Path, optional
        Output directory
    n_mc_trials : int
        Number of MC trials (reduced for speed)
    target_period : int
        Period to extract phase for (default: 255)
    
    Returns
    -------
    dict
        Complete test results
    """
    # Setup output directory
    if output_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = repo_root / 'forensic_fingerprint' / 'out' / 'stress_tests' / f'phase_coherence_{timestamp}'
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("="*80)
    print("STRESS TEST #5: PHASE COHERENCE")
    print("="*80)
    print(f"Target period: Δℓ = {target_period}")
    print(f"Multipole range: ℓ = {ell_min} to {ell_max}")
    print(f"Output directory: {output_dir}")
    print("="*80)
    
    phase_results = {}
    
    # Process Planck dataset
    print("\n" + "="*80)
    print("PLANCK PR3 DATASET")
    print("="*80)
    
    whiten_modes_planck = ['diagonal']
    if planck_cov is not None:
        whiten_modes_planck.append('covariance')
    
    phase_results['Planck'] = extract_phase_from_dataset(
        obs_file=planck_obs,
        model_file=planck_model,
        cov_file=planck_cov,
        dataset_name="Planck PR3",
        ell_min=ell_min,
        ell_max=ell_max,
        whiten_modes=whiten_modes_planck,
        target_period=target_period,
        n_mc_trials=n_mc_trials
    )
    
    # Process WMAP dataset if provided
    if wmap_obs is not None and wmap_model is not None:
        print("\n" + "="*80)
        print("WMAP DATASET")
        print("="*80)
        
        whiten_modes_wmap = ['diagonal']
        if wmap_cov is not None:
            whiten_modes_wmap.append('covariance')
        
        phase_results['WMAP'] = extract_phase_from_dataset(
            obs_file=wmap_obs,
            model_file=wmap_model,
            cov_file=wmap_cov,
            dataset_name="WMAP 9yr",
            ell_min=ell_min,
            ell_max=ell_max,
            whiten_modes=whiten_modes_wmap,
            target_period=target_period,
            n_mc_trials=n_mc_trials
        )
    else:
        print("\n" + "="*80)
        print("WMAP dataset not provided - skipping cross-dataset comparison")
        print("="*80)
    
    # Compute phase statistics
    print("\n" + "="*80)
    print("PHASE COHERENCE ANALYSIS")
    print("="*80)
    
    stats = compute_phase_statistics(phase_results)
    
    print(f"\nCircular mean: {stats['circular_mean_deg']:.2f}°")
    print(f"Circular std dev: {stats['circular_std_deg']:.2f}°")
    print(f"Phase range: {stats['phase_range_deg']:.2f}°")
    print(f"Coherence score: {stats['coherence_score']:.3f}")
    
    # Assess coherence
    verdict, verdict_detail = assess_phase_coherence(stats)
    
    print(f"\n{'='*80}")
    print(f"VERDICT: {verdict}")
    print(f"{'='*80}")
    print(verdict_detail['interpretation'])
    print(f"{'='*80}")
    
    # Generate report
    generate_phase_stability_report(phase_results, stats, verdict_detail, output_dir)
    
    # Save JSON results
    results = {
        'test_name': 'Phase Coherence Test',
        'test_number': 5,
        'target_period': target_period,
        'ell_range': [ell_min, ell_max],
        'phase_results': phase_results,
        'statistics': stats,
        'verdict': verdict_detail,
        'timestamp': datetime.now().isoformat()
    }
    
    with open(output_dir / 'phase_coherence_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nJSON results saved to: {output_dir / 'phase_coherence_results.json'}")
    
    return results


def main():
    """
    Main function for command-line usage.
    """
    parser = argparse.ArgumentParser(
        description="UBT Forensic Fingerprint - Phase Coherence Test",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Planck only (raw and whitened):
  python test_5_phase_coherence.py \\
      --planck_obs data/planck_pr3/raw/TT_spectrum.txt \\
      --planck_model data/planck_pr3/raw/TT_model.txt \\
      --planck_cov data/planck_pr3/raw/TT_covariance.txt
  
  # Planck + WMAP cross-dataset:
  python test_5_phase_coherence.py \\
      --planck_obs data/planck_pr3/raw/TT_spectrum.txt \\
      --planck_model data/planck_pr3/raw/TT_model.txt \\
      --wmap_obs data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \\
      --wmap_model data/wmap/raw/wmap_tt_model_9yr_v5.txt \\
      --ell_min 30 --ell_max 800
        """
    )
    
    # Planck files
    parser.add_argument('--planck_obs', type=str, required=True,
                       help='Planck observation file (required)')
    parser.add_argument('--planck_model', type=str, required=True,
                       help='Planck model file (required)')
    parser.add_argument('--planck_cov', type=str,
                       help='Planck covariance file (optional)')
    
    # WMAP files
    parser.add_argument('--wmap_obs', type=str,
                       help='WMAP observation file (optional)')
    parser.add_argument('--wmap_model', type=str,
                       help='WMAP model file (optional)')
    parser.add_argument('--wmap_cov', type=str,
                       help='WMAP covariance file (optional)')
    
    # Analysis parameters
    parser.add_argument('--ell_min', type=int, default=30,
                       help='Minimum multipole (default: 30)')
    parser.add_argument('--ell_max', type=int, default=800,
                       help='Maximum multipole (default: 800, for WMAP compatibility)')
    parser.add_argument('--target_period', type=int, default=255,
                       help='Target period to extract phase (default: 255)')
    parser.add_argument('--mc_trials', type=int, default=1000,
                       help='Monte Carlo trials per dataset (default: 1000)')
    
    # Output
    parser.add_argument('--output_dir', type=str,
                       help='Output directory (default: auto-generated)')
    
    args = parser.parse_args()
    
    # Run test
    results = run_phase_coherence_test(
        planck_obs=args.planck_obs,
        planck_model=args.planck_model,
        planck_cov=args.planck_cov,
        wmap_obs=args.wmap_obs,
        wmap_model=args.wmap_model,
        wmap_cov=args.wmap_cov,
        ell_min=args.ell_min,
        ell_max=args.ell_max,
        output_dir=args.output_dir,
        n_mc_trials=args.mc_trials,
        target_period=args.target_period
    )
    
    return results


if __name__ == '__main__':
    main()
