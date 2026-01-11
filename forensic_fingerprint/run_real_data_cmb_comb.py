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
        --planck_manifest data/planck_pr3/manifests/planck_pr3_tt_manifest.json \
        --wmap_obs data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \
        --wmap_manifest data/wmap/manifests/wmap_tt_manifest.json \
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
    # Prioritize .git as the most reliable marker
    markers = ['.git', 'pyproject.toml', 'pytest.ini']
    
    # Walk up directory tree
    while current != current.parent:
        # Check if any marker exists in current directory
        for marker in markers:
            if (current / marker).exists():
                return current
        current = current.parent
    
    # Check root directory too
    for marker in markers:
        if (current / marker).exists():
            return current
    
    raise FileNotFoundError(
        f"Could not find repository root. Searched from {start_path} upward. "
        f"Looking for markers: {', '.join(markers)}"
    )


# Find repository root (works regardless of CWD)
repo_root = find_repo_root()

# Add loaders and cmb_comb to path
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'loaders'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'cmb_comb'))
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


def resolve_manifest_path(manifest_path, dataset_type):
    """
    Resolve manifest path with fallback candidates.
    
    Uses repo_root for resolving relative paths, so this works regardless of CWD.
    
    If the specified manifest path does not exist, tries fallback candidates in order:
    - For Planck: planck_pr3_tt_manifest.json, sha256.json, manifest.json
    - For WMAP: wmap_tt_manifest.json, sha256.json, manifest.json
    
    Parameters
    ----------
    manifest_path : str, Path, or None
        User-specified manifest path (may not exist)
    dataset_type : str
        Dataset type: 'planck' or 'wmap'
    
    Returns
    -------
    Path or None
        Resolved manifest path if found, None otherwise
    str or None
        Description of which fallback was used, None if no fallback needed
    """
    if manifest_path is None:
        return None, None
    
    manifest_path = Path(manifest_path)
    
    # If path is relative, try resolving relative to repo_root first
    if not manifest_path.is_absolute():
        resolved_from_root = repo_root / manifest_path
        if resolved_from_root.exists():
            return resolved_from_root, None
    
    # If specified path exists (absolute or relative to CWD), use it
    if manifest_path.exists():
        return manifest_path, None
    
    # Define fallback candidates based on dataset type (using repo_root)
    if dataset_type == 'planck':
        fallback_candidates = [
            repo_root / 'data' / 'planck_pr3' / 'manifests' / 'planck_pr3_tt_manifest.json',
            repo_root / 'data' / 'planck_pr3' / 'manifests' / 'sha256.json',
            repo_root / 'data' / 'planck_pr3' / 'manifests' / 'manifest.json',
        ]
    elif dataset_type == 'wmap':
        fallback_candidates = [
            repo_root / 'data' / 'wmap' / 'manifests' / 'wmap_tt_manifest.json',
            repo_root / 'data' / 'wmap' / 'manifests' / 'sha256.json',
            repo_root / 'data' / 'wmap' / 'manifests' / 'manifest.json',
        ]
    else:
        return None, None
    
    # Try each fallback candidate
    for candidate in fallback_candidates:
        if candidate.exists():
            fallback_desc = f"Using fallback manifest: {candidate}"
            return candidate, fallback_desc
    
    # No fallback found
    return None, None


def validate_data_manifest(manifest_path, dataset_type, obs_file=None, model_file=None):
    """
    Validate dataset against SHA-256 manifest.
    
    After basic hash validation, also verify that the manifest contains hashes
    for the exact files being used in this run.
    
    Parameters
    ----------
    manifest_path : str or Path or None
        Path to manifest JSON file
    dataset_type : str
        Dataset type: 'planck' or 'wmap'
    obs_file : str or Path or None
        Observation file path (for error message generation command)
    model_file : str or Path or None
        Model file path (for error message generation command)
    
    Returns
    -------
    bool
        True if validation passed, False otherwise
    """
    if manifest_path is None:
        print("WARNING: No manifest provided. Skipping hash validation.")
        print("         For court-grade provenance, manifests are required.\n")
        return True
    
    # Resolve manifest path with fallback logic
    resolved_path, fallback_desc = resolve_manifest_path(manifest_path, dataset_type)
    
    if resolved_path is None:
        # Build list of attempted paths for error message
        attempted_paths = [str(manifest_path)]
        
        if dataset_type == 'planck':
            attempted_paths.extend([
                str(repo_root / 'data' / 'planck_pr3' / 'manifests' / 'planck_pr3_tt_manifest.json'),
                str(repo_root / 'data' / 'planck_pr3' / 'manifests' / 'sha256.json'),
                str(repo_root / 'data' / 'planck_pr3' / 'manifests' / 'manifest.json'),
            ])
        elif dataset_type == 'wmap':
            attempted_paths.extend([
                str(repo_root / 'data' / 'wmap' / 'manifests' / 'wmap_tt_manifest.json'),
                str(repo_root / 'data' / 'wmap' / 'manifests' / 'sha256.json'),
                str(repo_root / 'data' / 'wmap' / 'manifests' / 'manifest.json'),
            ])
        
        print(f"ERROR: Manifest not found for {dataset_type} dataset.")
        print(f"\nAttempted paths:")
        for path in attempted_paths:
            print(f"  - {path}")
        
        # Provide helpful generation command
        if obs_file:
            print(f"\nTo generate the expected manifest, run:")
            manifest_dir = repo_root / 'data' / (
                'planck_pr3' if dataset_type == 'planck' else 'wmap'
            ) / 'manifests'
            manifest_name = 'planck_pr3_tt_manifest.json' if dataset_type == 'planck' else 'wmap_tt_manifest.json'
            
            obs_path = Path(obs_file)
            data_dir = obs_path.parent
            
            print(f"  cd {data_dir}")
            
            if model_file:
                print(f"  python {repo_root}/tools/data_provenance/hash_dataset.py {obs_path.name} {Path(model_file).name} --relative-to {repo_root} > {manifest_dir}/{manifest_name}")
            else:
                print(f"  python {repo_root}/tools/data_provenance/hash_dataset.py {obs_path.name} --relative-to {repo_root} > {manifest_dir}/{manifest_name}")
        
        print()
        return False
    
    # Print warning if using fallback
    if fallback_desc:
        print(f"WARNING: Specified manifest not found: {manifest_path}")
        print(f"         {fallback_desc}\n")
    
    print(f"Validating manifest: {resolved_path}")
    success = validate_manifest.validate_manifest(resolved_path, base_dir=repo_root)
    
    if not success:
        print()
        return False
    
    # PART A.1: After validation succeeds, verify manifest contains exact files used
    print("Checking manifest contains exact files used in this run...")
    
    # Load manifest JSON
    with open(resolved_path, 'r') as f:
        manifest = json.load(f)
    
    # Extract filenames and paths from manifest
    # We'll check both filename and path (if available) for more robust matching
    manifest_entries = {}
    for file_info in manifest.get('files', []):
        filename = file_info['filename']
        path = file_info.get('path', filename)  # Use path if available, else just filename
        manifest_entries[filename] = path
    
    # Collect files that should be in manifest
    required_files = {}
    if obs_file:
        obs_path = Path(obs_file)
        # Try to get relative path from repo root if file is absolute
        if obs_path.is_absolute() and obs_path.is_relative_to(repo_root):
            rel_path = str(obs_path.relative_to(repo_root))
        else:
            rel_path = str(obs_file)
        required_files[obs_path.name] = rel_path
    
    if model_file:
        model_path = Path(model_file)
        # Try to get relative path from repo root if file is absolute
        if model_path.is_absolute() and model_path.is_relative_to(repo_root):
            rel_path = str(model_path.relative_to(repo_root))
        else:
            rel_path = str(model_file)
        required_files[model_path.name] = rel_path
    
    # Check each required file is in manifest
    # First check by path (if available), then fall back to filename only
    missing_files = []
    for req_filename, req_path in required_files.items():
        # Check if this file is in the manifest
        if req_filename not in manifest_entries:
            # Filename not in manifest at all
            missing_files.append(req_filename)
        else:
            # Filename exists, but check if path also matches (when manifest has path info)
            manifest_path = manifest_entries[req_filename]
            # If manifest has a path (not just filename), verify it matches
            if '/' in manifest_path or '\\' in manifest_path:
                # Normalize paths for comparison
                manifest_path_normalized = str(Path(manifest_path))
                req_path_normalized = str(Path(req_path))
                if manifest_path_normalized != req_path_normalized:
                    # Path mismatch - this could be a different file with same name
                    missing_files.append(f"{req_filename} (path mismatch: expected {req_path}, found {manifest_path})")
    
    if missing_files:
        print()
        print("=" * 80)
        print("ERROR: Manifest validation succeeded but does not include files used by this run")
        print("=" * 80)
        print(f"Manifest: {resolved_path}")
        print(f"Missing files:")
        for mf in missing_files:
            print(f"  - {mf}")
        print()
        print("The manifest is valid but does not contain hashes for the exact files")
        print("you are trying to use. This could indicate:")
        print("  1. Wrong manifest file for this dataset")
        print("  2. Manifest needs to be regenerated with the current files")
        print()
        print("To regenerate the manifest with the correct files, run:")
        
        manifest_dir = repo_root / 'data' / (
            'planck_pr3' if dataset_type == 'planck' else 'wmap'
        ) / 'manifests'
        manifest_name = 'planck_pr3_tt_manifest.json' if dataset_type == 'planck' else 'wmap_tt_manifest.json'
        
        if obs_file:
            obs_path = Path(obs_file)
            data_dir = obs_path.parent if obs_path.is_absolute() else repo_root / obs_path.parent
            
            print(f"  cd {repo_root}")
            
            file_args = []
            if obs_file:
                # Use relative path from repo root
                rel_obs = Path(obs_file).relative_to(repo_root) if Path(obs_file).is_absolute() and Path(obs_file).is_relative_to(repo_root) else obs_file
                file_args.append(str(rel_obs))
            if model_file:
                rel_model = Path(model_file).relative_to(repo_root) if Path(model_file).is_absolute() and Path(model_file).is_relative_to(repo_root) else model_file
                file_args.append(str(rel_model))
            
            print(f"  python tools/data_provenance/hash_dataset.py {' '.join(file_args)} > {manifest_dir}/{manifest_name}")
        
        print()
        print("=" * 80)
        return False
    
    print(f"✓ Manifest contains all {len(required_files)} required file(s)")
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


def generate_combined_verdict(planck_results, wmap_results, output_file, variant, 
                             planck_manifest_validated=None, wmap_manifest_validated=None,
                             planck_obs_file=None, planck_model_file=None,
                             wmap_obs_file=None):
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
    planck_manifest_validated : bool or None
        Whether Planck manifest was validated (None if no manifest)
    wmap_manifest_validated : bool or None
        Whether WMAP manifest was validated (None if no manifest)
    planck_obs_file : str or None
        Path to Planck observation file
    planck_model_file : str or None
        Path to Planck model file
    wmap_obs_file : str or None
        Path to WMAP observation file
    """
    with open(output_file, 'w') as f:
        f.write("# CMB Comb Fingerprint Test - Combined Verdict\n\n")
        f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
        f.write(f"**Protocol Version**: v1.0\n")
        f.write(f"**Architecture Variant**: {variant}\n\n")
        
        f.write("**See**: `FORENSIC_VERDICT_CRITERIA.md` for pre-registered pass/fail criteria.\n\n")
        
        # Data Provenance Section
        f.write("## Data Provenance\n\n")
        
        if planck_obs_file or wmap_obs_file:
            f.write("### Dataset Files\n\n")
            
            if planck_obs_file:
                f.write(f"**Planck PR3**:\n")
                f.write(f"- Observation: `{planck_obs_file}`\n")
                if planck_model_file:
                    f.write(f"- Model: `{planck_model_file}`\n")
                if planck_manifest_validated is not None:
                    status = "✓ VALIDATED" if planck_manifest_validated else "✗ VALIDATION FAILED"
                    f.write(f"- SHA-256 Manifest: **{status}**\n")
                else:
                    f.write(f"- SHA-256 Manifest: **NOT PROVIDED** (candidate-grade only)\n")
                f.write("\n")
            
            if wmap_obs_file:
                f.write(f"**WMAP 9yr**:\n")
                f.write(f"- Observation: `{wmap_obs_file}`\n")
                if wmap_manifest_validated is not None:
                    status = "✓ VALIDATED" if wmap_manifest_validated else "✗ VALIDATION FAILED"
                    f.write(f"- SHA-256 Manifest: **{status}**\n")
                else:
                    f.write(f"- SHA-256 Manifest: **NOT PROVIDED** (candidate-grade only)\n")
                f.write("\n")
        
        f.write("---\n\n")
        
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
      --planck_manifest data/planck_pr3/manifests/planck_pr3_tt_manifest.json \\
      --wmap_obs data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \\
      --wmap_manifest data/wmap/manifests/wmap_tt_manifest.json \\
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
    
    # PART A.2: Content-based rejection of likelihood/parameter files
    # Check file content for likelihood markers (not filename, as some valid model files may contain "minimum")
    if args.planck_model:
        model_file = Path(args.planck_model)
        if model_file.exists():
            # Content check: look for likelihood markers in data
            try:
                with open(model_file, 'r') as f:
                    for line in f:
                        stripped = line.strip()
                        # Skip empty lines and comments
                        if not stripped or stripped.startswith('#'):
                            continue
                        # Check first non-comment line for likelihood markers
                        if '-log(like)' in stripped.lower() or 'loglike' in stripped.lower():
                            print()
                            print("=" * 80)
                            print("ERROR: Invalid Planck model file")
                            print("=" * 80)
                            print(f"File: {args.planck_model}")
                            print()
                            print("This file contains '-log(Like)' or 'logLike' in the data,")
                            print("indicating it is a likelihood/parameter file, not a power spectrum.")
                            print()
                            print("For the CMB comb test, you need a TT power spectrum model file.")
                            print()
                            print("Recommended files:")
                            print("  1. Theoretical ΛCDM spectrum from CAMB/CLASS")
                            print("  2. Planck 'minimum-theory' spectrum files")
                            print("  3. TT-full observation file as both obs and model (for residual=0)")
                            print()
                            print("See forensic_fingerprint/RUNBOOK_REAL_DATA.md for guidance.")
                            print("=" * 80)
                            sys.exit(1)
                        # Only check first data line
                        break
            except Exception:
                # If we can't read the file, let the loader handle it
                pass
    
    # Generate output directory with timestamp
    if args.output_dir:
        output_dir = Path(args.output_dir)
        if not output_dir.is_absolute():
            # Make relative paths relative to repo_root
            output_dir = repo_root / output_dir
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = repo_root / 'forensic_fingerprint' / 'out' / 'real_runs' / f"cmb_comb_{timestamp}"
    
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
    
    # Validate manifests if provided and track validation status
    planck_manifest_validated = None
    wmap_manifest_validated = None
    
    if args.planck_manifest:
        print("Validating Planck manifest...")
        planck_manifest_validated = validate_data_manifest(args.planck_manifest, 'planck', args.planck_obs, args.planck_model)
        if not planck_manifest_validated:
            print("ERROR: Planck manifest validation failed. Aborting.")
            sys.exit(1)
    
    if args.wmap_manifest:
        print("Validating WMAP manifest...")
        wmap_manifest_validated = validate_data_manifest(args.wmap_manifest, 'wmap', args.wmap_obs, args.wmap_model)
        if not wmap_manifest_validated:
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
        args.variant,
        planck_manifest_validated=planck_manifest_validated,
        wmap_manifest_validated=wmap_manifest_validated,
        planck_obs_file=args.planck_obs,
        planck_model_file=args.planck_model,
        wmap_obs_file=args.wmap_obs
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
