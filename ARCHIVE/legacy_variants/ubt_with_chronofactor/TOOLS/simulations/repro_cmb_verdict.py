#!/usr/bin/env python3
"""
CMB Verdict Reproducibility Script
===================================

Single-command script to reproduce CMB comb analysis with full provenance tracking.
Downloads data (if needed), generates/validates manifests, runs pipeline, and prints verdict.

This script is designed to be deterministic, noisy on failures, and safe (no silent fallbacks).

Usage:
    python scripts/repro_cmb_verdict.py --mode theory
    python scripts/repro_cmb_verdict.py --mode obs-as-model --dry-run
    python scripts/repro_cmb_verdict.py --planck-obs custom/path.txt --no-download

License: MIT
Author: UBT Research Team
"""

import argparse
import subprocess
import sys
from pathlib import Path
from datetime import datetime


def ensure_repo_root():
    """
    Find repository root by looking for markers.
    
    Returns
    -------
    Path
        Repository root directory
    
    Raises
    ------
    SystemExit
        If repository root cannot be found
    """
    # Start from script location
    current = Path(__file__).resolve().parent
    
    # Markers that indicate repo root
    markers = ['.git', 'pyproject.toml', 'pytest.ini', 'forensic_fingerprint']
    
    # Search upward
    while current != current.parent:
        for marker in markers:
            if (current / marker).exists():
                return current
        current = current.parent
    
    # Check filesystem root
    for marker in markers:
        if (current / marker).exists():
            return current
    
    print("=" * 80)
    print("ERROR: Could not find repository root")
    print("=" * 80)
    print("")
    print("Searched upward from:", Path(__file__).resolve().parent)
    print("")
    print("Looking for one of these markers:")
    for marker in markers:
        print(f"  - {marker}")
    print("")
    print("Make sure you are running this script from within the repository.")
    print("=" * 80)
    sys.exit(1)


def run_cmd(cmd, description, dry_run=False, check=True, capture_output=False):
    """
    Run a command with error handling.
    
    Parameters
    ----------
    cmd : list of str
        Command and arguments
    description : str
        Human-readable description of what command does
    dry_run : bool
        If True, only print command without running
    check : bool
        If True, raise error on non-zero exit
    capture_output : bool
        If True, capture and return stdout/stderr
    
    Returns
    -------
    subprocess.CompletedProcess or None
        Result if not dry_run, None otherwise
    """
    print(f"→ {description}")
    print(f"  Command: {' '.join(str(c) for c in cmd)}")
    
    if dry_run:
        print("  [DRY RUN] Skipping execution")
        return None
    
    try:
        result = subprocess.run(
            cmd,
            check=check,
            capture_output=capture_output,
            text=True
        )
        if capture_output:
            return result
        print("  ✓ Success")
        return result
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Failed with exit code {e.returncode}")
        if capture_output and e.stdout:
            print("\n--- STDOUT ---")
            print(e.stdout[-2000:] if len(e.stdout) > 2000 else e.stdout)
        if capture_output and e.stderr:
            print("\n--- STDERR ---")
            print(e.stderr[-2000:] if len(e.stderr) > 2000 else e.stderr)
        raise
    except FileNotFoundError:
        print(f"  ✗ Command not found: {cmd[0]}")
        raise


def count_lines(filepath):
    """
    Count lines in a file.
    
    Parameters
    ----------
    filepath : Path
        File to count
    
    Returns
    -------
    int
        Number of lines
    """
    with open(filepath, 'r') as f:
        return sum(1 for _ in f)


def first_data_line(filepath, max_lines=50):
    """
    Get first non-comment data line from file.
    
    Parameters
    ----------
    filepath : Path
        File to read
    max_lines : int
        Maximum lines to read
    
    Returns
    -------
    str
        First data line, or empty string if not found
    """
    with open(filepath, 'r') as f:
        for i, line in enumerate(f):
            if i >= max_lines:
                break
            stripped = line.strip()
            if stripped and not stripped.startswith('#'):
                return stripped
    return ""


def is_html_file(filepath):
    """
    Check if file appears to be HTML (error page).
    
    Parameters
    ----------
    filepath : Path
        File to check
    
    Returns
    -------
    bool
        True if file contains HTML markers
    """
    with open(filepath, 'r', errors='ignore') as f:
        for i, line in enumerate(f):
            if i >= 50:  # Check first 50 lines
                break
            lower = line.lower()
            if '<html' in lower or '<!doctype' in lower:
                return True
    return False


def newest_run_dir(runs_dir):
    """
    Find newest run directory by modification time.
    
    Parameters
    ----------
    runs_dir : Path
        Directory containing run directories
    
    Returns
    -------
    Path or None
        Newest directory matching pattern, or None if not found
    """
    pattern = "cmb_comb_*"
    candidates = list(runs_dir.glob(pattern))
    
    if not candidates:
        return None
    
    # Sort by modification time, newest first
    candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0]


def main():
    parser = argparse.ArgumentParser(
        description="One-command CMB verdict reproduction with full provenance",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Theory mode (default): Use Planck TT-full + theory model + WMAP
  python scripts/repro_cmb_verdict.py --mode theory

  # Obs-as-model mode: Use Planck obs as model too (baseline residual=0)
  python scripts/repro_cmb_verdict.py --mode obs-as-model

  # Dry run (print actions without executing)
  python scripts/repro_cmb_verdict.py --dry-run

  # Custom paths
  python scripts/repro_cmb_verdict.py --planck-obs custom/obs.txt --no-download

See forensic_fingerprint/RUNBOOK_REAL_DATA.md for details.
        """
    )
    
    # Mode selection
    parser.add_argument('--mode', choices=['theory', 'obs-as-model'], default='theory',
                       help='Analysis mode: theory (Planck obs + model) or obs-as-model (baseline)')
    
    # Data paths
    parser.add_argument('--planck-obs', type=str,
                       default='data/planck_pr3/raw/COM_PowerSpect_CMB-TT-full_R3.01.txt',
                       help='Planck observation file')
    parser.add_argument('--planck-model', type=str,
                       default='data/planck_pr3/raw/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt',
                       help='Planck model file (ignored in obs-as-model mode)')
    parser.add_argument('--wmap-obs', type=str,
                       default='data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt',
                       help='WMAP observation file')
    
    # Manifest paths
    parser.add_argument('--planck-manifest-out', type=str,
                       default='data/planck_pr3/manifests/planck_pr3_tt_manifest.json',
                       help='Output path for Planck manifest')
    parser.add_argument('--wmap-manifest-out', type=str,
                       default='data/wmap/manifests/wmap_tt_manifest.json',
                       help='Output path for WMAP manifest')
    
    # Pipeline parameters
    parser.add_argument('--ell-min-planck', type=int, default=30,
                       help='Planck minimum multipole')
    parser.add_argument('--ell-max-planck', type=int, default=1500,
                       help='Planck maximum multipole')
    parser.add_argument('--ell-min-wmap', type=int, default=30,
                       help='WMAP minimum multipole')
    parser.add_argument('--ell-max-wmap', type=int, default=800,
                       help='WMAP maximum multipole')
    parser.add_argument('--variant', type=str, default='C',
                       help='Architecture variant')
    parser.add_argument('--mc-samples', type=int, default=10000,
                       help='Monte Carlo samples')
    parser.add_argument('--seed', type=int, default=42,
                       help='Random seed')
    
    # Safety flags
    parser.add_argument('--no-download', action='store_true',
                       help='Skip download scripts entirely')
    parser.add_argument('--download', action='store_true',
                       help='Force download attempt (default: auto-detect)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Print actions without executing')
    
    # Output
    parser.add_argument('--latest-file', type=str,
                       default='forensic_fingerprint/out/real_runs/LATEST_RUN.txt',
                       help='Path to write latest run directory')
    parser.add_argument('--print-verdict-lines', type=int, default=140,
                       help='Number of verdict lines to print')
    
    args = parser.parse_args()
    
    # Find repo root
    repo_root = ensure_repo_root()
    print(f"Repository root: {repo_root}")
    print("")
    
    # Resolve all paths relative to repo root
    planck_obs = repo_root / args.planck_obs
    planck_model = repo_root / args.planck_model
    wmap_obs = repo_root / args.wmap_obs
    planck_manifest_out = repo_root / args.planck_manifest_out
    wmap_manifest_out = repo_root / args.wmap_manifest_out
    latest_file = repo_root / args.latest_file
    
    # Adjust for obs-as-model mode
    if args.mode == 'obs-as-model':
        print("Mode: obs-as-model (Planck obs used as model too)")
        planck_model = planck_obs
    else:
        print("Mode: theory (Planck obs + separate model)")
    print("")
    
    # ==========================================
    # STEP 1: Download data (if requested)
    # ==========================================
    
    if not args.no_download:
        print("=" * 80)
        print("STEP 1: Download CMB datasets")
        print("=" * 80)
        print("")
        
        download_dir = repo_root / 'tools' / 'data_download'
        
        # Find download scripts
        planck_scripts = sorted(download_dir.glob('download_planck_pr3*.sh'))
        wmap_scripts = sorted(download_dir.glob('download_wmap*.sh'))
        
        scripts_to_run = planck_scripts + wmap_scripts
        
        if not scripts_to_run:
            print("No download scripts found in tools/data_download/")
            print("Skipping download step")
        else:
            for script in scripts_to_run:
                try:
                    run_cmd(
                        ['bash', str(script)],
                        f"Running {script.name}",
                        dry_run=args.dry_run,
                        check=True
                    )
                except subprocess.CalledProcessError:
                    print(f"WARNING: Download script {script.name} failed")
                    if not args.dry_run:
                        print("Continuing with existing files (if present)...")
                except FileNotFoundError:
                    print(f"ERROR: bash not found, cannot run {script.name}")
                    sys.exit(1)
        print("")
    else:
        print("Skipping download step (--no-download)")
        print("")
    
    # ==========================================
    # STEP 2: Sanity check files
    # ==========================================
    
    print("=" * 80)
    print("STEP 2: Sanity check data files")
    print("=" * 80)
    print("")
    
    files_to_check = [
        (planck_obs, "Planck observation", 500),
        (wmap_obs, "WMAP observation", 200),
    ]
    
    # Only check model if different from obs
    if args.mode == 'theory' and planck_model != planck_obs:
        files_to_check.append((planck_model, "Planck model", 50))
    
    for filepath, desc, min_lines in files_to_check:
        print(f"Checking: {desc}")
        print(f"  Path: {filepath}")
        
        if args.dry_run:
            print(f"  [DRY RUN] Skipping file checks")
            print("")
            continue
        
        # Check existence
        if not filepath.exists():
            print(f"  ✗ File not found")
            print("")
            print("=" * 80)
            print(f"ERROR: Required file missing: {desc}")
            print("=" * 80)
            print(f"Path: {filepath}")
            print("")
            print("Suggestions:")
            print("  1. Run download scripts: python scripts/repro_cmb_verdict.py --download")
            print("  2. Check path spelling")
            print("  3. Provide custom path: --planck-obs <path> or --wmap-obs <path>")
            print("=" * 80)
            sys.exit(1)
        
        # Check for HTML error page
        if is_html_file(filepath):
            print(f"  ✗ File appears to be HTML (error page)")
            print("")
            print("=" * 80)
            print(f"ERROR: {desc} is an HTML error page")
            print("=" * 80)
            print(f"Path: {filepath}")
            print("")
            print("This usually means the download failed or returned an error page.")
            print("Delete the file and re-run with --download to fetch correct data.")
            print("=" * 80)
            sys.exit(1)
        
        # Check line count
        lines = count_lines(filepath)
        print(f"  Lines: {lines}")
        
        if lines < min_lines:
            print(f"  ✗ Too few lines (expected >= {min_lines})")
            print("")
            print("=" * 80)
            print(f"ERROR: {desc} has too few lines")
            print("=" * 80)
            print(f"Path: {filepath}")
            print(f"Lines: {lines} (expected >= {min_lines})")
            print("")
            print("This file may be incomplete or corrupted.")
            print("Delete and re-download: python scripts/repro_cmb_verdict.py --download")
            print("=" * 80)
            sys.exit(1)
        
        # Print first data line
        first_line = first_data_line(filepath)
        if first_line:
            print(f"  First data: {first_line[:80]}")
        
        print(f"  Size: {filepath.stat().st_size} bytes")
        print(f"  ✓ Valid")
        print("")
    
    # ==========================================
    # STEP 3: Generate manifests
    # ==========================================
    
    print("=" * 80)
    print("STEP 3: Generate SHA-256 manifests")
    print("=" * 80)
    print("")
    
    hash_script = repo_root / 'tools' / 'data_provenance' / 'hash_dataset.py'
    
    if not hash_script.exists():
        print(f"ERROR: hash_dataset.py not found at {hash_script}")
        sys.exit(1)
    
    # Create manifest directories
    if not args.dry_run:
        planck_manifest_out.parent.mkdir(parents=True, exist_ok=True)
        wmap_manifest_out.parent.mkdir(parents=True, exist_ok=True)
    
    # Generate Planck manifest
    print("Generating Planck manifest...")
    planck_files = [str(planck_obs)]
    if args.mode == 'theory' and planck_model != planck_obs:
        planck_files.append(str(planck_model))
    
    if not args.dry_run:
        result = run_cmd(
            ['python', str(hash_script)] + planck_files,
            f"Hash {len(planck_files)} Planck file(s)",
            dry_run=False,
            check=True,
            capture_output=True
        )
        with open(planck_manifest_out, 'w') as f:
            f.write(result.stdout)
        print(f"  Saved to: {planck_manifest_out}")
    else:
        run_cmd(
            ['python', str(hash_script)] + planck_files,
            f"Hash {len(planck_files)} Planck file(s)",
            dry_run=True
        )
    print("")
    
    # Generate WMAP manifest
    print("Generating WMAP manifest...")
    if not args.dry_run:
        result = run_cmd(
            ['python', str(hash_script), str(wmap_obs)],
            "Hash WMAP file",
            dry_run=False,
            check=True,
            capture_output=True
        )
        with open(wmap_manifest_out, 'w') as f:
            f.write(result.stdout)
        print(f"  Saved to: {wmap_manifest_out}")
    else:
        run_cmd(
            ['python', str(hash_script), str(wmap_obs)],
            "Hash WMAP file",
            dry_run=True
        )
    print("")
    
    # ==========================================
    # STEP 4: Validate manifests
    # ==========================================
    
    print("=" * 80)
    print("STEP 4: Validate manifests")
    print("=" * 80)
    print("")
    
    validate_script = repo_root / 'tools' / 'data_provenance' / 'validate_manifest.py'
    
    if not validate_script.exists():
        print(f"ERROR: validate_manifest.py not found at {validate_script}")
        sys.exit(1)
    
    for manifest_path, desc in [(planck_manifest_out, "Planck"), (wmap_manifest_out, "WMAP")]:
        print(f"Validating {desc} manifest...")
        
        if not args.dry_run:
            try:
                run_cmd(
                    ['python', str(validate_script), str(manifest_path)],
                    f"Validate {desc} manifest",
                    dry_run=False,
                    check=True
                )
            except subprocess.CalledProcessError:
                print("")
                print("=" * 80)
                print(f"ERROR: {desc} manifest validation failed")
                print("=" * 80)
                print(f"Manifest: {manifest_path}")
                print("")
                print("This indicates the files don't match their expected hashes.")
                print("This could mean:")
                print("  1. Files were modified after manifest generation")
                print("  2. Wrong files are being validated")
                print("  3. Data corruption occurred")
                print("")
                print("Fix: Re-download and regenerate manifests")
                print("=" * 80)
                sys.exit(1)
        else:
            run_cmd(
                ['python', str(validate_script), str(manifest_path)],
                f"Validate {desc} manifest",
                dry_run=True
            )
        print("")
    
    # ==========================================
    # STEP 5: Run CMB comb pipeline
    # ==========================================
    
    print("=" * 80)
    print("STEP 5: Run CMB comb pipeline")
    print("=" * 80)
    print("")
    
    pipeline_script = repo_root / 'forensic_fingerprint' / 'run_real_data_cmb_comb.py'
    
    if not pipeline_script.exists():
        print(f"ERROR: run_real_data_cmb_comb.py not found at {pipeline_script}")
        sys.exit(1)
    
    # Build pipeline command
    pipeline_cmd = [
        'python', str(pipeline_script),
        '--planck_obs', str(planck_obs),
        '--planck_model', str(planck_model),
        '--planck_manifest', str(planck_manifest_out),
        '--wmap_obs', str(wmap_obs),
        '--wmap_manifest', str(wmap_manifest_out),
        '--ell_min_planck', str(args.ell_min_planck),
        '--ell_max_planck', str(args.ell_max_planck),
        '--ell_min_wmap', str(args.ell_min_wmap),
        '--ell_max_wmap', str(args.ell_max_wmap),
        '--variant', args.variant,
        '--mc_samples', str(args.mc_samples),
        '--seed', str(args.seed),
    ]
    
    print("Running CMB comb analysis with:")
    print(f"  Planck obs: {planck_obs.name}")
    print(f"  Planck model: {planck_model.name}")
    print(f"  WMAP obs: {wmap_obs.name}")
    print(f"  Variant: {args.variant}")
    print(f"  MC samples: {args.mc_samples}")
    print("")
    
    if not args.dry_run:
        try:
            run_cmd(
                pipeline_cmd,
                "Execute CMB comb pipeline",
                dry_run=False,
                check=True
            )
        except subprocess.CalledProcessError as e:
            print("")
            print("=" * 80)
            print("ERROR: Pipeline execution failed")
            print("=" * 80)
            print("")
            print("The CMB comb pipeline returned an error.")
            print("Check the output above for details.")
            print("")
            print("Command was:")
            print(f"  {' '.join(pipeline_cmd)}")
            print("=" * 80)
            sys.exit(1)
    else:
        run_cmd(
            pipeline_cmd,
            "Execute CMB comb pipeline",
            dry_run=True
        )
    print("")
    
    # ==========================================
    # STEP 6: Locate and display verdict
    # ==========================================
    
    print("=" * 80)
    print("STEP 6: Locate latest run and display verdict")
    print("=" * 80)
    print("")
    
    runs_dir = repo_root / 'forensic_fingerprint' / 'out' / 'real_runs'
    
    if not args.dry_run:
        if not runs_dir.exists():
            print(f"ERROR: Runs directory not found: {runs_dir}")
            sys.exit(1)
        
        latest_run = newest_run_dir(runs_dir)
        
        if latest_run is None:
            print("ERROR: No run directories found")
            print(f"Looking in: {runs_dir}")
            sys.exit(1)
        
        print(f"Latest run: {latest_run}")
        
        # Check for verdict file
        verdict_file = latest_run / 'combined_verdict.md'
        
        if not verdict_file.exists():
            print("")
            print("=" * 80)
            print("ERROR: Verdict file not found")
            print("=" * 80)
            print(f"Run directory: {latest_run}")
            print(f"Expected file: combined_verdict.md")
            print("")
            print("The pipeline may have failed to generate the verdict.")
            print("Check the run directory for error logs.")
            print("=" * 80)
            sys.exit(1)
        
        # Write latest run path
        latest_file.parent.mkdir(parents=True, exist_ok=True)
        with open(latest_file, 'w') as f:
            f.write(str(latest_run) + '\n')
        print(f"Latest run path saved to: {latest_file}")
        print("")
        
        # Print verdict
        print("=" * 80)
        print("COMBINED VERDICT")
        print("=" * 80)
        print("")
        
        with open(verdict_file, 'r') as f:
            lines = f.readlines()
        
        n_lines = min(len(lines), args.print_verdict_lines)
        for line in lines[:n_lines]:
            print(line, end='')
        
        if len(lines) > n_lines:
            print(f"\n... ({len(lines) - n_lines} more lines)")
            print(f"\nFull verdict: {verdict_file}")
        
        print("")
        print("=" * 80)
        print("REPRODUCIBILITY RUN COMPLETE")
        print("=" * 80)
        print(f"Run directory: {latest_run}")
        print(f"Verdict file: {verdict_file}")
        print("")
        
    else:
        print("[DRY RUN] Would locate newest run in:")
        print(f"  {runs_dir}")
        print("[DRY RUN] Would print verdict from: <run_dir>/combined_verdict.md")
        print("")
    
    print("✓ All steps completed successfully")
    sys.exit(0)


if __name__ == '__main__':
    main()
