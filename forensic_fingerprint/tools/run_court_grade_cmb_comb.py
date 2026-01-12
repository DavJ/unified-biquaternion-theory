#!/usr/bin/env python3
"""
Court-Grade CMB Comb Pipeline - One-Command Reproducible Execution
===================================================================

This script provides a complete, deterministic pipeline for running the court-grade
CMB comb fingerprint test from data download to final verdict generation.

Features:
- Verifies repository structure
- Downloads Planck PR3 and WMAP data (idempotent)
- Validates downloaded files (HTML detection)
- Generates derived Planck model (deterministic Dl→Cl conversion)
- Creates and validates SHA-256 manifests
- Runs CMB comb test with exact court-grade parameters
- Prints output directory and verdict location

Usage:
    python run_court_grade_cmb_comb.py
    python run_court_grade_cmb_comb.py --mc_samples 100000
    python run_court_grade_cmb_comb.py --seed 123 --dry-run

License: MIT
Author: UBT Research Team
"""

import sys
import argparse
import subprocess
from pathlib import Path
import json

# Lazy load numpy only when needed (not for --dry-run or --help)
np = None


def find_repo_root():
    """Find repository root by looking for tools/data_provenance/hash_dataset.py."""
    current = Path(__file__).resolve().parent
    
    # Walk up directory tree
    while current != current.parent:
        marker = current / 'tools' / 'data_provenance' / 'hash_dataset.py'
        if marker.exists():
            return current
        current = current.parent
    
    raise FileNotFoundError(
        "Could not find repository root. "
        "Looking for tools/data_provenance/hash_dataset.py"
    )


def detect_html(filepath):
    """
    Check if file is an HTML error page (404/redirect).
    
    Parameters
    ----------
    filepath : Path
        File to check
    
    Returns
    -------
    bool
        True if file contains HTML markers, False otherwise
    """
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            first_kb = f.read(1024)
            lower = first_kb.lower()
            return '<html' in lower or '<!doctype' in lower
    except Exception:
        return False


def ensure_directory(path, description=""):
    """Ensure directory exists, creating if needed."""
    path = Path(path)
    if not path.exists():
        print(f"Creating directory: {path}")
        path.mkdir(parents=True, exist_ok=True)
    else:
        print(f"✓ Directory exists: {path}")


def run_command(cmd, description="", check=True, cwd=None):
    """
    Run a shell command with error handling.
    
    Parameters
    ----------
    cmd : list of str
        Command and arguments
    description : str
        Human-readable description
    check : bool
        If True, raise on non-zero exit code
    cwd : Path or None
        Working directory
    
    Returns
    -------
    subprocess.CompletedProcess
        Result object
    """
    if description:
        print(f"\n→ {description}")
    
    print(f"  Command: {' '.join(str(c) for c in cmd)}")
    
    try:
        result = subprocess.run(
            cmd,
            check=check,
            capture_output=True,
            text=True,
            cwd=cwd
        )
        if result.stdout:
            print(result.stdout)
        if result.returncode == 0:
            print(f"  ✓ Success")
        return result
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Failed (exit code {e.returncode})")
        if e.stdout:
            print(f"  STDOUT: {e.stdout}")
        if e.stderr:
            print(f"  STDERR: {e.stderr}")
        raise


def download_data(repo_root, force_download=False):
    """
    Download Planck and WMAP data (idempotent).
    
    Parameters
    ----------
    repo_root : Path
        Repository root directory
    force_download : bool
        If True, download even if files exist
    """
    print("="*80)
    print("STEP 1: Download CMB datasets")
    print("="*80)
    
    # Check if download scripts exist
    planck_script = repo_root / 'tools' / 'data_download' / 'download_planck_pr3_cosmoparams.sh'
    wmap_script = repo_root / 'tools' / 'data_download' / 'download_wmap_tt.sh'
    
    # Planck download
    if planck_script.exists():
        print("\n→ Running Planck PR3 download script")
        try:
            run_command(
                ['bash', str(planck_script)],
                cwd=repo_root,
                check=False  # Don't fail if already downloaded
            )
        except Exception as e:
            print(f"  Warning: Planck download script failed: {e}")
            print(f"  Continuing (files may already exist)...")
    else:
        print(f"\n⚠ Planck download script not found: {planck_script}")
        print(f"  Manual download required or files must already exist")
    
    # WMAP download
    if wmap_script.exists():
        print("\n→ Running WMAP download script")
        try:
            run_command(
                ['bash', str(wmap_script)],
                cwd=repo_root,
                check=False
            )
        except Exception as e:
            print(f"  Warning: WMAP download script failed: {e}")
            print(f"  Continuing (files may already exist)...")
    else:
        print(f"\n⚠ WMAP download script not found: {wmap_script}")
        print(f"  Manual download required or files must already exist")


def validate_file(filepath, min_lines=50, description="file"):
    """
    Validate that a file exists, is not HTML, and has enough lines.
    
    Parameters
    ----------
    filepath : Path
        File to validate
    min_lines : int
        Minimum expected line count
    description : str
        Human-readable description
    
    Returns
    -------
    bool
        True if valid, raises exception otherwise
    """
    print(f"\nValidating {description}:")
    print(f"  Path: {filepath}")
    
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    # Check for HTML
    if detect_html(filepath):
        raise ValueError(
            f"{description} is an HTML error page\n"
            f"  Path: {filepath}\n"
            f"  This usually means download failed or returned 404/redirect.\n"
            f"  Delete the file and re-download."
        )
    
    # Count lines
    with open(filepath, 'r') as f:
        lines = sum(1 for _ in f)
    
    print(f"  Lines: {lines}")
    
    if lines < min_lines:
        raise ValueError(
            f"{description} has too few lines\n"
            f"  Path: {filepath}\n"
            f"  Lines: {lines} (expected >= {min_lines})\n"
            f"  File may be incomplete or corrupted."
        )
    
    # Show first data line (skip comments)
    with open(filepath, 'r') as f:
        for line in f:
            stripped = line.strip()
            if stripped and not stripped.startswith('#'):
                print(f"  First data: {stripped}")
                break
    
    # Show file size
    size = filepath.stat().st_size
    print(f"  Size: {size} bytes")
    
    print(f"  ✓ Valid")
    return True


def generate_derived_model(repo_root, source_file, output_file):
    """
    Generate derived Planck TT model file from minimum-theory file.
    
    Extracts TT column and converts Dl → Cl.
    
    Parameters
    ----------
    repo_root : Path
        Repository root
    source_file : Path
        Source minimum-theory file (multi-column, Dl format)
    output_file : Path
        Output model file (2-column, Cl format)
    """
    global np
    if np is None:
        import numpy as _np
        np = _np
    
    print("="*80)
    print("STEP 3: Generate derived Planck model")
    print("="*80)
    
    print(f"\nInput: {source_file}")
    print(f"Output: {output_file}")
    
    if not source_file.exists():
        raise FileNotFoundError(f"Source file not found: {source_file}")
    
    # Load data
    print("\nLoading source file...")
    data = []
    with open(source_file, 'r') as f:
        for line in f:
            stripped = line.strip()
            # Skip empty lines and comments
            if not stripped or stripped.startswith('#'):
                continue
            # Parse numeric row
            parts = stripped.split()
            if len(parts) >= 2:
                try:
                    ell = float(parts[0])
                    tt_dl = float(parts[1])  # TT column in Dl format
                    data.append((ell, tt_dl))
                except ValueError:
                    continue
    
    if len(data) < 100:
        raise ValueError(f"Too few rows loaded from source: {len(data)}")
    
    print(f"  Loaded {len(data)} rows")
    
    # Convert Dl → Cl
    print("\nConverting Dl → Cl (Cl = Dl × 2π / [l(l+1)])...")
    ell_array = np.array([row[0] for row in data])
    dl_array = np.array([row[1] for row in data])
    
    # Cl = Dl × 2π / [l(l+1)]
    cl_array = dl_array * (2 * np.pi) / (ell_array * (ell_array + 1))
    
    # Sanity checks
    if not np.all(np.isfinite(cl_array)):
        raise ValueError("Non-finite values in converted Cl array")
    
    if not np.all(cl_array > 0):
        # Allow some zeros at very high ell
        n_nonpositive = np.sum(cl_array <= 0)
        if n_nonpositive > 10:
            raise ValueError(f"Too many non-positive Cl values: {n_nonpositive}")
    
    # Check L range includes analysis window
    if ell_array.min() > 30:
        raise ValueError(f"L range starts at {ell_array.min()} > 30")
    
    if ell_array.max() < 1500:
        raise ValueError(f"L range ends at {ell_array.max()} < 1500")
    
    print(f"  ℓ range: {int(ell_array.min())} to {int(ell_array.max())}")
    print(f"  Median Cl: {np.median(cl_array):.2e} μK²")
    
    # Write output in minimal format
    print(f"\nWriting output file: {output_file}")
    
    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w') as f:
        # Header: exactly "#    L    TT" (no other # lines above it!)
        f.write("#    L    TT\n")
        
        # Data rows: L and TT (where TT is Cl)
        for ell, cl in zip(ell_array, cl_array):
            f.write(f"{int(ell):5d}  {cl:.6e}\n")
    
    print(f"  Wrote {len(ell_array)} rows")
    
    # Validate output
    print("\nValidating output file...")
    with open(output_file, 'r') as f:
        first_line = f.readline().strip()
        if first_line != "#    L    TT":
            raise ValueError(f"Output header incorrect: '{first_line}'")
    
    validate_file(output_file, min_lines=2000, description="derived model")
    
    print("  ✓ Derived model generation complete")


def generate_manifest(repo_root, files, output_file, description=""):
    """
    Generate SHA-256 manifest for files.
    
    Parameters
    ----------
    repo_root : Path
        Repository root (for relative paths)
    files : list of Path
        Files to hash
    output_file : Path
        Output manifest JSON file
    description : str
        Human-readable description
    """
    print(f"\n→ Generating manifest{': ' + description if description else ''}")
    
    # Build command
    cmd = [
        'python',
        str(repo_root / 'tools' / 'data_provenance' / 'hash_dataset.py')
    ]
    
    # Add file paths (relative to repo root)
    for f in files:
        if f.is_absolute():
            try:
                rel = f.relative_to(repo_root)
                cmd.append(str(rel))
            except ValueError:
                cmd.append(str(f))
        else:
            cmd.append(str(f))
    
    print(f"  Output: {output_file}")
    print(f"  Files: {len(files)}")
    for f in files:
        print(f"    - {f.name}")
    
    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Run hash_dataset.py
    result = subprocess.run(
        cmd,
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True
    )
    
    # Write output to manifest file
    with open(output_file, 'w') as f:
        f.write(result.stdout)
    
    print(f"  ✓ Manifest generated: {output_file}")


def validate_manifest(repo_root, manifest_file, description=""):
    """
    Validate manifest using validate_manifest.py.
    
    Parameters
    ----------
    repo_root : Path
        Repository root
    manifest_file : Path
        Manifest JSON file
    description : str
        Human-readable description
    """
    print(f"\n→ Validating manifest{': ' + description if description else ''}")
    
    cmd = [
        'python',
        str(repo_root / 'tools' / 'data_provenance' / 'validate_manifest.py'),
        str(manifest_file),
        '--base_dir', str(repo_root)
    ]
    
    run_command(cmd, cwd=repo_root)


def run_cmb_comb_pipeline(repo_root, args):
    """
    Run the CMB comb pipeline with specified parameters.
    
    Parameters
    ----------
    repo_root : Path
        Repository root
    args : Namespace
        Command-line arguments
    
    Returns
    -------
    Path
        Output directory path
    """
    print("="*80)
    print("STEP 5: Run CMB comb pipeline")
    print("="*80)
    
    # Build command
    cmd = [
        'python',
        str(repo_root / 'forensic_fingerprint' / 'run_real_data_cmb_comb.py'),
        '--planck_obs', str(repo_root / 'data' / 'planck_pr3' / 'raw' / 'COM_PowerSpect_CMB-TT-full_R3.01.txt'),
        '--planck_model', str(repo_root / 'data' / 'planck_pr3' / 'derived' / 'planck_pr3_tt_model_extracted_minfmt.txt'),
        '--planck_manifest', str(repo_root / 'data' / 'planck_pr3' / 'manifests' / 'planck_pr3_tt_full_plus_extracted_minfmt_manifest.json'),
        '--wmap_obs', str(repo_root / 'data' / 'wmap' / 'raw' / 'wmap_tt_spectrum_9yr_v5.txt'),
        '--wmap_manifest', str(repo_root / 'data' / 'wmap' / 'manifests' / 'wmap_tt_manifest.json'),
        '--ell_min_planck', str(args.ell_min_planck),
        '--ell_max_planck', str(args.ell_max_planck),
        '--ell_min_wmap', str(args.ell_min_wmap),
        '--ell_max_wmap', str(args.ell_max_wmap),
        '--variant', args.variant,
        '--mc_samples', str(args.mc_samples),
        '--whiten', args.whiten,
        '--seed', str(args.seed)
    ]
    
    print(f"\nRunning: {' '.join(cmd)}\n")
    
    result = run_command(cmd, cwd=repo_root)
    
    # Parse output to find output directory
    # Look for line like "Output directory: ..."
    output_dir = None
    for line in result.stdout.split('\n'):
        if 'Output directory:' in line:
            # Extract path
            parts = line.split(':', 1)
            if len(parts) == 2:
                output_dir = Path(parts[1].strip())
                break
    
    if output_dir is None:
        # Try to find latest run
        runs_dir = repo_root / 'forensic_fingerprint' / 'out' / 'real_runs'
        if runs_dir.exists():
            subdirs = sorted([d for d in runs_dir.iterdir() if d.is_dir()], key=lambda x: x.stat().st_mtime, reverse=True)
            if subdirs:
                output_dir = subdirs[0]
    
    return output_dir


def main():
    parser = argparse.ArgumentParser(
        description="Court-Grade CMB Comb Pipeline - One-Command Execution",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Basic run (default parameters)
    python run_court_grade_cmb_comb.py
    
    # High-confidence run (100k MC samples)
    python run_court_grade_cmb_comb.py --mc_samples 100000
    
    # Custom seed for reproducibility
    python run_court_grade_cmb_comb.py --seed 123
    
    # Dry run (show what would be done)
    python run_court_grade_cmb_comb.py --dry-run

Court-Grade Defaults:
    --variant C
    --mc_samples 10000
    --whiten diag
    --seed 42
    --ell_min_planck 30
    --ell_max_planck 1500
    --ell_min_wmap 30
    --ell_max_wmap 800
        """
    )
    
    # Pipeline control
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be done without executing')
    parser.add_argument('--skip-download', action='store_true',
                       help='Skip data download step (assume files exist)')
    parser.add_argument('--skip-validation', action='store_true',
                       help='Skip manifest validation (not recommended)')
    
    # Test parameters (court-grade defaults)
    parser.add_argument('--variant', type=str, default='C',
                       choices=['A', 'B', 'C', 'D'],
                       help='Architecture variant (default: C)')
    parser.add_argument('--mc_samples', type=int, default=10000,
                       help='Monte Carlo samples (default: 10000 for court-grade)')
    parser.add_argument('--seed', type=int, default=42,
                       help='Random seed for reproducibility (default: 42, pre-registered)')
    parser.add_argument('--whiten', type=str, default='diag',
                       choices=['none', 'diag', 'full'],
                       help='Whitening mode (default: diag)')
    
    # Multipole ranges
    parser.add_argument('--ell_min_planck', type=int, default=30,
                       help='Planck minimum multipole (default: 30)')
    parser.add_argument('--ell_max_planck', type=int, default=1500,
                       help='Planck maximum multipole (default: 1500)')
    parser.add_argument('--ell_min_wmap', type=int, default=30,
                       help='WMAP minimum multipole (default: 30)')
    parser.add_argument('--ell_max_wmap', type=int, default=800,
                       help='WMAP maximum multipole (default: 800)')
    
    args = parser.parse_args()
    
    if args.dry_run:
        print("="*80)
        print("DRY RUN MODE - No changes will be made")
        print("="*80)
    
    try:
        # Step 0: Find repository root
        print("="*80)
        print("COURT-GRADE CMB COMB PIPELINE")
        print("="*80)
        
        repo_root = find_repo_root()
        print(f"\nRepository root: {repo_root}\n")
        
        if args.dry_run:
            print("Would execute the following steps:")
            print("1. Ensure required directories exist")
            print("2. Download Planck PR3 and WMAP data (if missing)")
            print("3. Validate downloaded files (HTML detection, line counts)")
            print("4. Generate derived Planck model (Dl → Cl conversion)")
            print("5. Generate SHA-256 manifests")
            print("6. Validate manifests")
            print("7. Run CMB comb test")
            print("8. Print output directory and verdict location")
            print("\nNo actual changes will be made in dry-run mode.")
            return 0
        
        # Step 1: Ensure directories exist
        print("="*80)
        print("STEP 0: Ensure required directories exist")
        print("="*80)
        
        ensure_directory(repo_root / 'data' / 'planck_pr3' / 'raw')
        ensure_directory(repo_root / 'data' / 'planck_pr3' / 'derived')
        ensure_directory(repo_root / 'data' / 'planck_pr3' / 'manifests')
        ensure_directory(repo_root / 'data' / 'wmap' / 'raw')
        ensure_directory(repo_root / 'data' / 'wmap' / 'manifests')
        
        # Step 2: Download data
        if not args.skip_download:
            download_data(repo_root)
        else:
            print("\n→ Skipping download (--skip-download)")
        
        # Step 2.5: Validate files
        print("\n" + "="*80)
        print("STEP 2: Validate downloaded files")
        print("="*80)
        
        planck_obs = repo_root / 'data' / 'planck_pr3' / 'raw' / 'COM_PowerSpect_CMB-TT-full_R3.01.txt'
        planck_source = repo_root / 'data' / 'planck_pr3' / 'raw' / 'COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt'
        wmap_obs = repo_root / 'data' / 'wmap' / 'raw' / 'wmap_tt_spectrum_9yr_v5.txt'
        
        validate_file(planck_obs, min_lines=500, description="Planck TT-full observation")
        validate_file(planck_source, min_lines=50, description="Planck minimum-theory source")
        validate_file(wmap_obs, min_lines=200, description="WMAP observation")
        
        # Step 3: Generate derived model
        planck_model = repo_root / 'data' / 'planck_pr3' / 'derived' / 'planck_pr3_tt_model_extracted_minfmt.txt'
        
        # Only regenerate if missing
        if not planck_model.exists():
            generate_derived_model(repo_root, planck_source, planck_model)
        else:
            print("\n" + "="*80)
            print("STEP 3: Derived model exists (skipping generation)")
            print("="*80)
            print(f"\n✓ Using existing: {planck_model}")
            validate_file(planck_model, min_lines=2000, description="derived Planck model")
        
        # Step 4: Generate manifests
        print("\n" + "="*80)
        print("STEP 4: Generate and validate manifests")
        print("="*80)
        
        # Planck manifest (obs + derived model)
        planck_manifest = repo_root / 'data' / 'planck_pr3' / 'manifests' / 'planck_pr3_tt_full_plus_extracted_minfmt_manifest.json'
        
        if not planck_manifest.exists():
            generate_manifest(
                repo_root,
                [planck_obs, planck_model],
                planck_manifest,
                description="Planck OBS + DERIVED MODEL"
            )
        else:
            print(f"\n✓ Planck manifest exists: {planck_manifest}")
        
        # WMAP manifest
        wmap_manifest = repo_root / 'data' / 'wmap' / 'manifests' / 'wmap_tt_manifest.json'
        
        if not wmap_manifest.exists():
            generate_manifest(
                repo_root,
                [wmap_obs],
                wmap_manifest,
                description="WMAP"
            )
        else:
            print(f"\n✓ WMAP manifest exists: {wmap_manifest}")
        
        # Validate manifests
        if not args.skip_validation:
            validate_manifest(repo_root, planck_manifest, description="Planck")
            validate_manifest(repo_root, wmap_manifest, description="WMAP")
        else:
            print("\n→ Skipping manifest validation (--skip-validation)")
        
        # Step 5: Run CMB comb pipeline
        output_dir = run_cmb_comb_pipeline(repo_root, args)
        
        # Step 6: Print results
        print("\n" + "="*80)
        print("PIPELINE COMPLETE")
        print("="*80)
        
        if output_dir:
            print(f"\nOutput directory: {output_dir}")
            
            verdict_file = output_dir / 'combined_verdict.md'
            if verdict_file.exists():
                print(f"Verdict file: {verdict_file}")
                print("\n→ Reading first 50 lines of verdict...\n")
                print("-" * 80)
                with open(verdict_file, 'r') as f:
                    for i, line in enumerate(f):
                        if i >= 50:
                            print("\n[... truncated, see full file ...]")
                            break
                        print(line, end='')
                print("-" * 80)
            else:
                print(f"\n⚠ Verdict file not found: {verdict_file}")
        else:
            print("\n⚠ Could not determine output directory")
        
        print("\n✓ All steps completed successfully\n")
        return 0
        
    except Exception as e:
        print(f"\n✗ ERROR: {e}\n", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
