#!/usr/bin/env python3
"""
UBT Forensic Fingerprint - One-Command CMB Phase-Comb Test Runner
===================================================================

Court-grade test for periodic phase-locking in CMB spherical harmonics.

This script provides a single-command entrypoint for running the phase-comb
fingerprint test on real Planck (and optionally WMAP) map-level data.

Key Differences from TT Spectrum Comb Test:
-------------------------------------------
- TT spectrum test: Analyzes C_ℓ = ⟨|a_ℓm|²⟩_m (power, phases discarded)
- Phase-comb test: Analyzes φ_ℓm = arg(a_ℓm) (phase coherence between modes)

This test is **complementary** to the TT comb test. A null result in TT
spectrum does NOT preclude a positive result in phase space.

Usage Examples
--------------

Minimal example (Planck map only):
    python run_real_data_cmb_phase_comb.py \\
        --planck_map data/planck_pr3/maps/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits \\
        --planck_mask data/planck_pr3/maps/masks/COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits

With manifest validation (court-grade):
    python run_real_data_cmb_phase_comb.py \\
        --planck_map data/planck_pr3/maps/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits \\
        --planck_mask data/planck_pr3/maps/masks/COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits \\
        --planck_manifest data/planck_pr3/maps/manifests/planck_maps_manifest.json \\
        --mc_samples 10000

High-confidence run (100k surrogates):
    python run_real_data_cmb_phase_comb.py \\
        --planck_map data/planck_pr3/maps/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits \\
        --planck_mask data/planck_pr3/maps/masks/COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits \\
        --mc_samples 100000 --seed 42

Custom periods (enable Bonferroni correction):
    python run_real_data_cmb_phase_comb.py \\
        --planck_map data/planck_pr3/maps/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits \\
        --periods "137,139,255,256,512" \\
        --correction bonferroni

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
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'cmb_phase_comb'))
sys.path.insert(0, str(repo_root / 'tools' / 'data_provenance'))

# Import phase-comb modules
try:
    import phase_comb
    import io_healpix
    import report
    import plots
    import nulls
except ImportError as e:
    print(f"ERROR: Failed to import phase-comb modules: {e}")
    print("Make sure forensic_fingerprint/cmb_phase_comb/ exists")
    sys.exit(1)

# Import data validation
try:
    import validate_manifest
except ImportError:
    print("WARNING: validate_manifest not available, skipping manifest validation")
    validate_manifest = None


# Check for healpy
try:
    import healpy as hp
    HEALPY_AVAILABLE = True
except ImportError:
    HEALPY_AVAILABLE = False


# Pre-registered periods (LOCKED)
DEFAULT_PERIODS = [255, 256, 137, 139]
DEFAULT_MC_SAMPLES = 10000
DEFAULT_SEED = 42


def validate_data_manifest(manifest_path, dataset_type, map_file=None, mask_file=None, base_dir=None):
    """
    Validate dataset against SHA-256 manifest.
    
    Parameters
    ----------
    manifest_path : str or Path or None
        Path to manifest JSON file
    dataset_type : str
        Dataset type: 'planck' or 'wmap'
    map_file : str or Path or None
        Map file path (for error messages)
    mask_file : str or Path or None
        Mask file path (for error messages)
    base_dir : str or Path or None
        Base directory for resolving paths
    
    Returns
    -------
    bool
        True if validation passed, False otherwise
    """
    if manifest_path is None:
        print("WARNING: No manifest provided. Skipping hash validation.")
        print("         For court-grade provenance, manifests are required.\n")
        return True
    
    if validate_manifest is None:
        print("WARNING: validate_manifest module not available")
        return True
    
    if base_dir is None:
        base_dir = repo_root
    else:
        base_dir = Path(base_dir)
    
    manifest_path = Path(manifest_path)
    
    if not manifest_path.exists():
        print(f"ERROR: Manifest not found: {manifest_path}")
        print()
        print("To generate the manifest, run:")
        
        manifest_dir = base_dir / 'data' / (
            'planck_pr3/maps' if dataset_type == 'planck' else 'wmap/maps'
        ) / 'manifests'
        manifest_name = f'{dataset_type}_maps_manifest.json'
        
        file_args = []
        if map_file:
            map_path = Path(map_file)
            if map_path.is_absolute() and map_path.is_relative_to(base_dir):
                rel_map = map_path.relative_to(base_dir)
            else:
                rel_map = map_file
            file_args.append(str(rel_map))
        if mask_file:
            mask_path = Path(mask_file)
            if mask_path.is_absolute() and mask_path.is_relative_to(base_dir):
                rel_mask = mask_path.relative_to(base_dir)
            else:
                rel_mask = mask_file
            file_args.append(str(rel_mask))
        
        print(f"  cd {base_dir}")
        print(f"  mkdir -p {manifest_dir}")
        print(f"  python tools/data_provenance/hash_dataset.py {' '.join(file_args)} > {manifest_dir}/{manifest_name}")
        print()
        
        return False
    
    print(f"Validating manifest: {manifest_path}")
    success = validate_manifest.validate_manifest(manifest_path, base_dir=base_dir)
    
    if not success:
        print()
        return False
    
    print()
    return True


def parse_periods(periods_str):
    """Parse comma-separated period string into list of ints."""
    try:
        return [int(p.strip()) for p in periods_str.split(',')]
    except ValueError as e:
        raise ValueError(f"Invalid periods string '{periods_str}': {e}")


def parse_prime_window(window_str):
    """
    Parse prime window string "min,max" and return list of primes in range.
    
    Returns None if window_str is "0" or empty.
    """
    if not window_str or window_str == "0":
        return None
    
    try:
        parts = window_str.split(',')
        if len(parts) != 2:
            raise ValueError("Prime window must be 'min,max'")
        
        p_min = int(parts[0].strip())
        p_max = int(parts[1].strip())
        
        # Simple prime sieve
        primes = []
        for n in range(p_min, p_max + 1):
            if n < 2:
                continue
            is_prime = True
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(n)
        
        return primes
    
    except Exception as e:
        raise ValueError(f"Invalid prime window '{window_str}': {e}")


def main():
    parser = argparse.ArgumentParser(
        description="One-Command CMB Phase-Comb Test Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Minimal (Planck only):
  python run_real_data_cmb_phase_comb.py \\
      --planck_map data/planck_pr3/maps/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits

  # With mask and manifest (court-grade):
  python run_real_data_cmb_phase_comb.py \\
      --planck_map data/planck_pr3/maps/raw/COM_CMB_IQU-smica_2048_R3.00_full.fits \\
      --planck_mask data/planck_pr3/maps/masks/COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits \\
      --planck_manifest data/planck_pr3/maps/manifests/planck_maps_manifest.json \\
      --mc_samples 10000

See forensic_fingerprint/RUNBOOK_PHASE_COMB.md for complete documentation.
        """
    )
    
    # Planck data
    parser.add_argument('--planck_map', type=str, required=True,
                       help='Planck CMB map (HEALPix FITS or .npy)')
    parser.add_argument('--planck_mask', type=str,
                       help='Planck mask (optional, recommended)')
    parser.add_argument('--planck_manifest', type=str,
                       help='Planck SHA-256 manifest for validation (optional)')
    
    # WMAP data (optional, for replication)
    parser.add_argument('--wmap_map', type=str,
                       help='WMAP CMB map (optional, for replication)')
    parser.add_argument('--wmap_mask', type=str,
                       help='WMAP mask (optional)')
    parser.add_argument('--wmap_manifest', type=str,
                       help='WMAP SHA-256 manifest (optional)')
    
    # Test parameters
    parser.add_argument('--ell_min', type=int, default=30,
                       help='Minimum multipole for test (default: 30)')
    parser.add_argument('--ell_max', type=int, default=1500,
                       help='Maximum multipole for test (default: 1500)')
    parser.add_argument('--alm_lmax', type=int, default=None,
                       help='Maximum lmax for a_lm computation (default: same as ell_max)')
    
    # Periods to test
    parser.add_argument('--periods', type=str, default=None,
                       help='Comma-separated periods to test (default: "255,256,137,139")')
    parser.add_argument('--prime_window', type=str, default="0",
                       help='Add primes in range "min,max" (default: "0" disabled)')
    
    # Monte Carlo
    parser.add_argument('--mc_samples', type=int, default=DEFAULT_MC_SAMPLES,
                       help=f'Number of MC surrogates (default: {DEFAULT_MC_SAMPLES})')
    parser.add_argument('--seed', type=int, default=DEFAULT_SEED,
                       help=f'Random seed (default: {DEFAULT_SEED}, pre-registered)')
    
    # Advanced options
    parser.add_argument('--m_mode', type=str, default='same_m',
                       choices=['same_m'],
                       help='Mode pairing (default: same_m, court-grade)')
    parser.add_argument('--correction', type=str, default='none',
                       choices=['none', 'bonferroni', 'max_statistic'],
                       help='Multiple-testing correction (default: none for pre-registered)')
    parser.add_argument('--remove_monopole', action='store_true', default=True,
                       help='Remove monopole before analysis (default: True)')
    parser.add_argument('--remove_dipole', action='store_true', default=True,
                       help='Remove dipole before analysis (default: True)')
    parser.add_argument('--iter', type=int, default=3,
                       help='Iterations for map2alm (default: 3)')
    
    # Output
    parser.add_argument('--output_dir', type=str,
                       help='Output directory (default: auto-generated with timestamp)')
    
    args = parser.parse_args()
    
    # Check healpy availability
    if not HEALPY_AVAILABLE:
        print()
        print("="*80)
        print("ERROR: healpy not installed")
        print("="*80)
        print()
        print("The phase-comb test requires healpy for spherical harmonic analysis.")
        print()
        print("Install with:")
        print("  pip install healpy")
        print()
        print("Or add to requirements.txt and run:")
        print("  pip install -r requirements.txt")
        print()
        print("="*80)
        sys.exit(1)
    
    # Determine alm_lmax
    alm_lmax = args.alm_lmax if args.alm_lmax else args.ell_max
    
    # Parse periods
    if args.periods:
        periods = parse_periods(args.periods)
    else:
        periods = DEFAULT_PERIODS.copy()
    
    # Add primes if requested
    if args.prime_window and args.prime_window != "0":
        primes = parse_prime_window(args.prime_window)
        if primes:
            print(f"Adding {len(primes)} primes from window {args.prime_window}")
            periods.extend(primes)
            periods = sorted(list(set(periods)))  # Remove duplicates and sort
            
            # Warn about multiple testing
            if args.correction == 'none':
                print()
                print("WARNING: Prime window adds extra periods beyond pre-registered set.")
                print("         Consider using --correction bonferroni or --correction max_statistic")
                print()
    
    # Generate output directory
    if args.output_dir:
        output_dir = Path(args.output_dir)
        if not output_dir.is_absolute():
            output_dir = repo_root / output_dir
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = repo_root / 'forensic_fingerprint' / 'out' / 'real_runs' / f"cmb_phase_comb_{timestamp}"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create figures subdirectory
    figures_dir = output_dir / 'figures'
    figures_dir.mkdir(exist_ok=True)
    
    print("="*80)
    print("UBT FORENSIC FINGERPRINT - CMB PHASE-COMB TEST")
    print("="*80)
    print(f"Output directory: {output_dir}")
    print(f"Periods to test: {periods}")
    print(f"MC samples: {args.mc_samples}")
    print(f"Random seed: {args.seed}")
    print(f"Multiple-testing correction: {args.correction}")
    print()
    
    # Validate manifests if provided
    planck_manifest_validated = None
    wmap_manifest_validated = None
    
    if args.planck_manifest:
        print("Validating Planck manifest...")
        planck_manifest_validated = validate_data_manifest(
            args.planck_manifest, 'planck', 
            args.planck_map, args.planck_mask
        )
        if not planck_manifest_validated:
            print("ERROR: Planck manifest validation failed. Aborting.")
            sys.exit(1)
    
    if args.wmap_manifest:
        print("Validating WMAP manifest...")
        wmap_manifest_validated = validate_data_manifest(
            args.wmap_manifest, 'wmap',
            args.wmap_map, args.wmap_mask
        )
        if not wmap_manifest_validated:
            print("ERROR: WMAP manifest validation failed. Aborting.")
            sys.exit(1)
    
    # Run Planck analysis
    planck_results = None
    if args.planck_map:
        print("="*80)
        print("RUNNING PLANCK PHASE-COMB ANALYSIS")
        print("="*80)
        print()
        
        # Load map
        print("Loading Planck CMB map...")
        map_data, mask, map_metadata = io_healpix.load_healpix_map(
            args.planck_map,
            mask_path=args.planck_mask,
            remove_monopole=args.remove_monopole,
            remove_dipole=args.remove_dipole
        )
        
        # Compute alm
        print()
        alm = io_healpix.compute_alm(map_data, lmax=alm_lmax, iter=args.iter)
        
        # Validate conjugacy
        print("\nValidating reality constraints...")
        is_valid, msg = io_healpix.validate_alm_conjugacy(alm, alm_lmax)
        print(f"  {msg}")
        
        if not is_valid:
            print("  WARNING: Reality constraint violations detected")
            print("           Results may be unreliable")
        
        # Run phase-comb test
        print()
        print("Running phase-comb test...")
        print()
        
        planck_results = phase_comb.run_phase_comb_test(
            alm=alm,
            lmax=alm_lmax,
            ell_min=args.ell_min,
            ell_max=args.ell_max,
            periods=periods,
            n_mc_samples=args.mc_samples,
            seed=args.seed,
            m_mode=args.m_mode,
            correction=args.correction,
            metadata={
                'dataset': 'Planck PR3',
                'map_file': str(args.planck_map),
                'mask_file': str(args.planck_mask) if args.planck_mask else None,
                **map_metadata
            }
        )
        
        # Save results
        print()
        print("Saving Planck results...")
        report.save_results_json(
            planck_results, 
            output_dir / 'planck_phase_results.json'
        )
        
        # Generate verdict
        data_files = {
            'CMB map': args.planck_map,
        }
        if args.planck_mask:
            data_files['Mask'] = args.planck_mask
        
        report.generate_verdict_markdown(
            planck_results,
            output_dir / 'combined_verdict.md',
            dataset_name='Planck PR3',
            manifest_validated=planck_manifest_validated,
            data_files=data_files
        )
        
        # Generate plots
        print()
        print("Generating plots...")
        plots.generate_all_plots(planck_results, figures_dir)
        print()
    
    # Run WMAP analysis (if provided)
    wmap_results = None
    if args.wmap_map:
        print("="*80)
        print("RUNNING WMAP PHASE-COMB ANALYSIS")
        print("="*80)
        print()
        
        # Load map
        print("Loading WMAP CMB map...")
        map_data, mask, map_metadata = io_healpix.load_healpix_map(
            args.wmap_map,
            mask_path=args.wmap_mask,
            remove_monopole=args.remove_monopole,
            remove_dipole=args.remove_dipole
        )
        
        # Compute alm
        print()
        alm = io_healpix.compute_alm(map_data, lmax=alm_lmax, iter=args.iter)
        
        # Validate conjugacy
        print("\nValidating reality constraints...")
        is_valid, msg = io_healpix.validate_alm_conjugacy(alm, alm_lmax)
        print(f"  {msg}")
        
        # Run phase-comb test
        print()
        print("Running phase-comb test...")
        print()
        
        wmap_results = phase_comb.run_phase_comb_test(
            alm=alm,
            lmax=alm_lmax,
            ell_min=args.ell_min,
            ell_max=args.ell_max,
            periods=periods,
            n_mc_samples=args.mc_samples,
            seed=args.seed,
            m_mode=args.m_mode,
            correction=args.correction,
            metadata={
                'dataset': 'WMAP 9yr',
                'map_file': str(args.wmap_map),
                'mask_file': str(args.wmap_mask) if args.wmap_mask else None,
                **map_metadata
            }
        )
        
        # Save results
        print()
        print("Saving WMAP results...")
        report.save_results_json(
            wmap_results,
            output_dir / 'wmap_phase_results.json'
        )
        
        print()
    
    # Final summary
    print("="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    print()
    print(f"All results saved to: {output_dir}")
    print()
    print("Key files:")
    if planck_results:
        print("  - planck_phase_results.json")
    if wmap_results:
        print("  - wmap_phase_results.json")
    print("  - combined_verdict.md (READ THIS FOR PASS/FAIL DECISION)")
    print("  - figures/phase_coherence_curve.png")
    print()
    
    # Quick summary
    if planck_results:
        print("Quick Summary (Planck):")
        print(f"  Best period: P = {planck_results['best_period']}")
        print(f"  P-value: {planck_results['best_p_value']:.6e}")
        print(f"  Significance: {planck_results['significance']}")
        print()
    
    if wmap_results:
        print("Quick Summary (WMAP):")
        print(f"  Best period: P = {wmap_results['best_period']}")
        print(f"  P-value: {wmap_results['best_p_value']:.6e}")
        print(f"  Significance: {wmap_results['significance']}")
        print()
    
    print("See combined_verdict.md for detailed interpretation and next steps.")
    print()


if __name__ == '__main__':
    main()
