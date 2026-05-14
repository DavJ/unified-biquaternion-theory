#!/usr/bin/env python3
"""
example_phase_lock_analysis.py

Example script demonstrating the Unified Phase-Lock Scan with Monte Carlo validation.

This script shows how to use the unified_phase_lock_scan tool to verify
UBT predictions about phase-lock between TT and BB channels at k=137/139.

Requirements:
- Planck CMB maps (SMICA or other component-separated products)
- Python packages: numpy, healpy, matplotlib

Usage:
    python example_phase_lock_analysis.py
"""

import os
import subprocess
import sys

# Configuration - Update these paths to your Planck data
DATA_DIR = "data/planck_pr3"  # Directory containing Planck FITS files

# Planck SMICA component-separated maps (example filenames)
TT_MAP = os.path.join(DATA_DIR, "COM_CMB_IQU-smica_2048_R3.00_full.fits")
Q_MAP = os.path.join(DATA_DIR, "COM_CMB_IQU-smica_2048_R3.00_full.fits")  # Field 1
U_MAP = os.path.join(DATA_DIR, "COM_CMB_IQU-smica_2048_R3.00_full.fits")  # Field 2

# Output directory
OUTPUT_DIR = "results/phase_lock_analysis"

# Analysis parameters
TARGETS = "137,139"  # UBT-predicted Jacobi cluster twin primes
WINDOW_SIZE = 128    # Segment size (W×W)
WINDOW_FUNC = "none"  # No windowing (UBT requirement)
NSIDE_OUT = 256      # Map degradation for faster processing
MC_SAMPLES = 1000    # Monte Carlo samples for p-value estimation


def check_data_files():
    """Check if Planck data files exist."""
    print("=" * 70)
    print("DATA FILE CHECK")
    print("=" * 70)
    
    files = {
        "TT map": TT_MAP,
        "Q map": Q_MAP,
        "U map": U_MAP,
    }
    
    all_exist = True
    for name, path in files.items():
        if os.path.exists(path):
            print(f"✓ {name}: {path}")
        else:
            print(f"✗ {name}: NOT FOUND - {path}")
            all_exist = False
    
    print()
    
    if not all_exist:
        print("ERROR: Some data files are missing.")
        print("\nTo run this example, you need Planck CMB maps.")
        print("See Planck archive documentation for download instructions.")
        print("\nRecommended products:")
        print("  - COM_CMB_IQU-smica_2048_R3.00_full.fits (SMICA)")
        print("  - COM_CMB_IQU-nilc_2048_R3.00_full.fits (NILC)")
        print("  - COM_CMB_IQU-sevem_2048_R3.00_full.fits (SEVEM)")
        print()
        return False
    
    return True


def run_analysis():
    """Run the unified phase-lock scan analysis."""
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Build command as list for subprocess
    cmd = [
        sys.executable, "-m", "forensic_fingerprint.tools.unified_phase_lock_scan",
        "--tt-map", TT_MAP,
        "--q-map", Q_MAP,
        "--u-map", U_MAP,
        "--targets", TARGETS,
        "--nside-out", str(NSIDE_OUT),
        "--window-size", str(WINDOW_SIZE),
        "--window", WINDOW_FUNC,
        "--projection", "torus",
        "--mc", str(MC_SAMPLES),
        "--null", "phase-shuffle",
        "--seed", "42",
        "--report-csv", f"{OUTPUT_DIR}/phase_lock_targets.csv",
        "--dump-full-csv", f"{OUTPUT_DIR}/phase_lock_full_spectrum.csv",
        "--plot", f"{OUTPUT_DIR}/phase_lock_diagnostic.png",
    ]
    
    print("=" * 70)
    print("RUNNING UNIFIED PHASE-LOCK SCAN")
    print("=" * 70)
    print("\nCommand:")
    print(" \\\n  ".join(cmd))
    print("\n" + "=" * 70 + "\n")
    
    # Execute with subprocess.run
    try:
        result = subprocess.run(cmd, check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"\nError running analysis: {e}")
        return False


def show_results():
    """Display analysis results."""
    import csv
    
    results_file = os.path.join(OUTPUT_DIR, "phase_lock_targets.csv")
    
    if not os.path.exists(results_file):
        print(f"Results file not found: {results_file}")
        return
    
    print("\n" + "=" * 70)
    print("ANALYSIS RESULTS")
    print("=" * 70)
    
    with open(results_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            k = row['k_target']
            pc = float(row['phase_coherence'])
            p = float(row['p_value'])
            z = float(row['z_score'])
            
            print(f"\nk = {k}:")
            print(f"  Phase Coherence (PC) = {pc:.6f}")
            print(f"  Z-score              = {z:.4f}")
            print(f"  p-value              = {p:.6g}")
            
            # Interpretation
            if p < 0.001:
                sig = "*** HIGHLY SIGNIFICANT ***"
            elif p < 0.01:
                sig = "** SIGNIFICANT **"
            elif p < 0.05:
                sig = "* MARGINALLY SIGNIFICANT *"
            else:
                sig = "NOT SIGNIFICANT"
            
            print(f"  Significance         = {sig}")
    
    print("\n" + "=" * 70)
    print("OUTPUT FILES")
    print("=" * 70)
    print(f"  Target results:  {results_file}")
    print(f"  Full spectrum:   {OUTPUT_DIR}/phase_lock_full_spectrum.csv")
    print(f"  Diagnostic plot: {OUTPUT_DIR}/phase_lock_diagnostic.png")
    print("=" * 70 + "\n")
    
    print("INTERPRETATION GUIDELINES:")
    print("-" * 70)
    print("This analysis tests whether TT and BB channels show non-random")
    print("phase relationships at the UBT-predicted frequencies k=137/139.")
    print()
    print("When evaluating results:")
    print("  • Compare observed PC against null distribution (MC samples)")
    print("  • Use maxstat or FDR correction to account for multiple testing")
    print("  • Inspect full PC spectrum, not just target frequencies")
    print("  • Consider physical interpretation alongside statistical tests")
    print()
    print("Statistical significance does NOT automatically confirm UBT.")
    print("Results must be interpreted in context of:")
    print("  - Systematic effects (foregrounds, instrument noise, etc.)")
    print("  - Alternative explanations for phase coherence")
    print("  - Consistency across different datasets and methods")
    print("=" * 70 + "\n")


def main():
    """Main entry point."""
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║         UNIFIED PHASE-LOCK SCAN - EXAMPLE ANALYSIS                  ║
║                                                                      ║
║  Verifying UBT predictions for phase synchronization between        ║
║  TT (scalar) and BB (spinor) channels in Planck CMB data            ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    
    # Check if data files exist
    if not check_data_files():
        print("\n⚠ Cannot proceed without Planck data files.")
        print("Update the DATA_DIR and file paths in this script,")
        print("or consult Planck archive documentation for data access.\n")
        return 1
    
    # Run analysis
    print(f"\nProcessing with {MC_SAMPLES} Monte Carlo samples...")
    print("This may take several minutes depending on your system.\n")
    
    success = run_analysis()
    
    if not success:
        print("\n✗ Analysis failed. Check error messages above.")
        return 1
    
    # Show results
    show_results()
    
    print("✓ Analysis complete!")
    print(f"\nResults saved to: {OUTPUT_DIR}/")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
