#!/usr/bin/env python3
"""
Exploratory Phase Coherence Scan for CMB Maps
==============================================

EXPLORATORY TEST - NOT CONFIRMATORY

This script implements the phase-coherence scan (Test Family A) as an
EXPLORATORY analysis. Results are labeled as candidates only, not detections.

Usage:
    python run_exploratory_phase_scan.py \\
        --alm_file data/cmb_maps/planck_pr3_temperature_alm.fits \\
        --lmax 2048 \\
        --output_dir forensic_fingerprint/out/exploratory_phase_scan

Pre-registered periods: [255, 256, 137, 139]
Optional: Scan additional primes in [100, 300] with --scan_primes flag

License: MIT
Author: UBT Research Team
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np

# Import phase coherence module
sys.path.insert(0, str(Path(__file__).parent))
from cmb_phase_comb import phase_comb, nulls


def parse_args():
    parser = argparse.ArgumentParser(
        description="Exploratory phase coherence scan (NOT confirmatory)"
    )
    
    # Input data
    parser.add_argument(
        "--alm_file", 
        type=str, 
        required=True,
        help="Path to FITS file containing spherical harmonic coefficients a_lm"
    )
    parser.add_argument(
        "--lmax", 
        type=int, 
        required=True,
        help="Maximum multipole ℓ in alm array"
    )
    
    # Test configuration
    parser.add_argument(
        "--ell_min", 
        type=int, 
        default=30,
        help="Minimum ℓ for phase coherence test (default: 30)"
    )
    parser.add_argument(
        "--ell_max", 
        type=int, 
        default=1500,
        help="Maximum ℓ for phase coherence test (default: 1500)"
    )
    parser.add_argument(
        "--periods", 
        type=int, 
        nargs='+',
        default=[255, 256, 137, 139],
        help="Periods to test (default: [255, 256, 137, 139] - pre-registered)"
    )
    parser.add_argument(
        "--scan_primes", 
        action='store_true',
        help="Additionally scan prime numbers in [100, 300]"
    )
    
    # Monte Carlo
    parser.add_argument(
        "--n_surrogates", 
        type=int, 
        default=10000,
        help="Number of phase-randomized surrogates (default: 10000)"
    )
    parser.add_argument(
        "--seed", 
        type=int, 
        default=42,
        help="Random seed for reproducibility (default: 42)"
    )
    
    # Output
    parser.add_argument(
        "--output_dir", 
        type=str, 
        required=True,
        help="Directory for output files"
    )
    parser.add_argument(
        "--label", 
        type=str, 
        default="exploratory",
        help="Label for this scan (default: exploratory)"
    )
    
    return parser.parse_args()


def load_alm(alm_file: str, lmax: int) -> np.ndarray:
    """
    Load spherical harmonic coefficients from FITS file.
    
    Parameters
    ----------
    alm_file : str
        Path to FITS file containing alm
    lmax : int
        Maximum multipole
    
    Returns
    -------
    alm : complex ndarray
        Spherical harmonic coefficients
    """
    try:
        import healpy as hp
    except ImportError:
        raise ImportError(
            "healpy required for loading alm. Install with: pip install healpy"
        )
    
    print(f"Loading alm from {alm_file}...")
    alm = hp.read_alm(alm_file)
    
    # Validate shape
    expected_size = hp.Alm.getsize(lmax)
    if len(alm) != expected_size:
        raise ValueError(
            f"alm size mismatch: got {len(alm)}, expected {expected_size} "
            f"for lmax={lmax}"
        )
    
    print(f"Loaded {len(alm)} complex coefficients (lmax={lmax})")
    return alm


def get_prime_numbers(min_val: int, max_val: int) -> List[int]:
    """Generate list of prime numbers in range [min_val, max_val]."""
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(np.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    return [n for n in range(min_val, max_val + 1) if is_prime(n)]


def run_exploratory_scan(args):
    """
    Run exploratory phase coherence scan.
    
    Parameters
    ----------
    args : argparse.Namespace
        Command-line arguments
    
    Returns
    -------
    results : dict
        Complete results dictionary
    """
    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Build period list
    periods = args.periods.copy()
    
    if args.scan_primes:
        print("Adding prime numbers in [100, 300] to scan list...")
        primes = get_prime_numbers(100, 300)
        print(f"Found {len(primes)} primes in range")
        periods.extend([p for p in primes if p not in periods])
    
    periods = sorted(periods)
    print(f"\nTotal periods to test: {len(periods)}")
    print(f"Periods: {periods}")
    
    # Load alm
    alm = load_alm(args.alm_file, args.lmax)
    
    # Run phase coherence test
    print("\n" + "="*70)
    print("EXPLORATORY PHASE COHERENCE SCAN")
    print("="*70)
    print("\nWARNING: This is an EXPLORATORY analysis.")
    print("Results are CANDIDATES, not confirmatory detections.")
    print("Any interesting signals require pre-registered confirmation.\n")
    
    results = phase_comb.run_phase_comb_test(
        alm=alm,
        lmax=args.lmax,
        ell_min=args.ell_min,
        ell_max=args.ell_max,
        periods=periods,
        n_mc_samples=args.n_surrogates,
        seed=args.seed,
        m_mode='same_m',
        correction='none',  # No correction for pre-registered periods
        metadata={
            'alm_file': str(args.alm_file),
            'label': args.label,
            'scan_type': 'exploratory',
            'timestamp': datetime.utcnow().isoformat() + 'Z',
        }
    )
    
    # Save JSON results
    json_file = output_dir / f"results_{args.label}.json"
    print(f"\nSaving results to {json_file}")
    
    with open(json_file, 'w') as f:
        # Convert numpy types for JSON serialization
        json_results = {}
        for key, val in results.items():
            if isinstance(val, dict):
                json_results[key] = {
                    str(k): float(v) if isinstance(v, (np.floating, np.integer)) else v
                    for k, v in val.items()
                }
            elif isinstance(val, list):
                json_results[key] = [
                    int(x) if isinstance(x, (np.integer,)) else x for x in val
                ]
            elif isinstance(val, (np.floating, np.integer)):
                json_results[key] = float(val)
            else:
                json_results[key] = val
        
        json.dump(json_results, f, indent=2)
    
    # Generate Markdown report
    generate_exploratory_report(results, args, output_dir)
    
    return results


def generate_exploratory_report(results: Dict, args, output_dir: Path):
    """
    Generate exploratory report in Markdown format.
    
    Parameters
    ----------
    results : dict
        Results from phase_comb.run_phase_comb_test
    args : argparse.Namespace
        Command-line arguments
    output_dir : Path
        Output directory
    """
    report_file = output_dir / f"EXPLORATORY_PHASE_SCAN.md"
    
    print(f"Generating exploratory report: {report_file}")
    
    with open(report_file, 'w') as f:
        f.write("# Exploratory Phase Coherence Scan\n\n")
        f.write("**EXPLORATORY — NOT A CONFIRMATORY TEST**\n\n")
        f.write("---\n\n")
        
        # Metadata
        f.write("## Scan Metadata\n\n")
        f.write(f"- **Timestamp**: {results['metadata']['timestamp']}\n")
        f.write(f"- **Label**: {args.label}\n")
        f.write(f"- **Input File**: `{args.alm_file}`\n")
        f.write(f"- **ℓ Range**: [{args.ell_min}, {args.ell_max}]\n")
        f.write(f"- **lmax**: {args.lmax}\n")
        f.write(f"- **Random Seed**: {args.seed}\n")
        f.write(f"- **Surrogates**: {args.n_surrogates:,}\n\n")
        
        # Disclaimer
        f.write("## ⚠️ Exploratory Analysis Disclaimer\n\n")
        f.write("**This is an EXPLORATORY scan, not a confirmatory test.**\n\n")
        f.write("**Interpretation guidelines**:\n")
        f.write("- p < 0.01 → **CANDIDATE** (interesting, requires confirmation)\n")
        f.write("- p < 0.001 → **STRONG CANDIDATE** (high priority for confirmation)\n")
        f.write("- p ≥ 0.01 → **NULL** (no further action)\n\n")
        f.write("**Do NOT use language like**:\n")
        f.write("- ❌ \"Detection\"\n")
        f.write("- ❌ \"Evidence for\"\n")
        f.write("- ❌ \"Confirmation\"\n\n")
        f.write("**Use language like**:\n")
        f.write("- ✅ \"Candidate signal\"\n")
        f.write("- ✅ \"Requires replication\"\n")
        f.write("- ✅ \"Exploratory indication\"\n\n")
        f.write("---\n\n")
        
        # Results table
        f.write("## Results\n\n")
        f.write("| Period | R(P) | Mean_surr | Std_surr | p-value | Status |\n")
        f.write("|--------|------|-----------|----------|---------|--------|\n")
        
        periods = results['periods']
        R_obs = results['R_observed']
        p_vals = results['p_values']
        surr_stats = results['surrogate_stats']
        
        for period in periods:
            R = R_obs[period]
            p = p_vals[period]
            mean_s = surr_stats[period]['mean']
            std_s = surr_stats[period]['std']
            
            # Status
            if p < 0.001:
                status = "**STRONG CANDIDATE** 🔴"
            elif p < 0.01:
                status = "**CANDIDATE** 🟡"
            else:
                status = "NULL ⚪"
            
            f.write(
                f"| {period:3d} | {R:.6f} | {mean_s:.6f} | {std_s:.6f} | "
                f"{p:.6e} | {status} |\n"
            )
        
        f.write("\n---\n\n")
        
        # Best candidate
        f.write("## Best Candidate\n\n")
        best_period = results['best_period']
        best_p = results['best_p_value']
        best_R = R_obs[best_period]
        
        f.write(f"- **Period**: Δℓ = {best_period}\n")
        f.write(f"- **R(P)**: {best_R:.6f}\n")
        f.write(f"- **p-value**: {best_p:.6e}\n")
        
        if best_p < 0.001:
            f.write(f"- **Status**: **STRONG CANDIDATE** — High priority for confirmation\n\n")
        elif best_p < 0.01:
            f.write(f"- **Status**: **CANDIDATE** — Interesting, worth confirmation\n\n")
        else:
            f.write(f"- **Status**: **NULL** — No significant signal\n\n")
        
        # Significance interpretation
        f.write("## Significance Interpretation\n\n")
        f.write("**Phase coherence statistic R(P)**:\n")
        f.write("- R(P) = 0 → Random phases (no structure)\n")
        f.write("- R(P) > 0 → Phase alignment (potential structure)\n\n")
        f.write("**Null model**: Phase-randomized surrogates preserving |a_ℓm|\n")
        f.write("- Randomize phases uniformly in [0, 2π)\n")
        f.write("- Preserve amplitude spectrum (and thus C_ℓ)\n")
        f.write("- Enforce reality constraints: a_ℓ,-m = (-1)^m conj(a_ℓm)\n\n")
        f.write("**p-value**: Fraction of surrogates with R ≥ R_observed\n\n")
        
        # Next steps
        f.write("---\n\n")
        f.write("## Next Steps\n\n")
        
        has_candidate = any(p_vals[p] < 0.01 for p in periods)
        
        if has_candidate:
            f.write("**CANDIDATE SIGNAL(S) DETECTED**\n\n")
            f.write("### Required Actions:\n\n")
            f.write("1. **Pre-register confirmatory test**:\n")
            f.write("   - Create `pre_registration/PHASE_TEST_v1.json`\n")
            f.write("   - Lock dataset, periods, ℓ-range, statistic, null model\n")
            f.write("   - Set significance threshold (α = 0.01 or α = 2.9×10⁻⁷)\n\n")
            f.write("2. **Run confirmatory test**:\n")
            f.write("   - Use `run_real_data_cmb_phase_confirm.py`\n")
            f.write("   - Require pre-registration file\n")
            f.write("   - Validate data with SHA-256 manifests\n\n")
            f.write("3. **Replication**:\n")
            f.write("   - Test on E-mode polarization maps\n")
            f.write("   - Test on different component separations (SMICA/NILC/SEVEM)\n")
            f.write("   - Require consistency across ≥2 independent realizations\n\n")
            f.write("4. **Only after confirmation**:\n")
            f.write("   - Write interpretation document\n")
            f.write("   - Connect to theoretical framework\n\n")
        else:
            f.write("**NO CANDIDATE SIGNALS DETECTED**\n\n")
            f.write("All tested periods show p ≥ 0.01 (NULL).\n\n")
            f.write("**Interpretation**: No evidence for phase-locking at tested periods.\n\n")
            f.write("**Recommended actions**:\n")
            f.write("- Test additional periods (if theoretically motivated)\n")
            f.write("- Try different ℓ-ranges\n")
            f.write("- Test polarization maps (E-mode, B-mode)\n")
            f.write("- Consider alternative observables (bispectrum, etc.)\n\n")
        
        f.write("---\n\n")
        f.write("**Report generated**: {}\n".format(datetime.utcnow().isoformat() + 'Z'))
        f.write("\n**This is an exploratory analysis. Do not claim detection without confirmation.**\n")
    
    print(f"Report saved to {report_file}")


def main():
    args = parse_args()
    
    print("="*70)
    print("EXPLORATORY PHASE COHERENCE SCAN")
    print("="*70)
    print()
    print("⚠️  WARNING: This is an EXPLORATORY analysis")
    print("⚠️  Results are CANDIDATES, not confirmatory detections")
    print()
    
    results = run_exploratory_scan(args)
    
    print("\n" + "="*70)
    print("EXPLORATORY SCAN COMPLETE")
    print("="*70)
    print(f"\nResults saved to: {args.output_dir}")
    print(f"Review: {args.output_dir}/EXPLORATORY_PHASE_SCAN.md")
    
    # Summary
    best_p = results['best_p_value']
    best_period = results['best_period']
    
    if best_p < 0.001:
        print(f"\n🔴 STRONG CANDIDATE detected at period {best_period} (p = {best_p:.2e})")
        print("   → HIGH PRIORITY for confirmatory testing")
    elif best_p < 0.01:
        print(f"\n🟡 CANDIDATE detected at period {best_period} (p = {best_p:.2e})")
        print("   → Interesting, worth confirmation")
    else:
        print(f"\n⚪ NULL result (best p = {best_p:.2e})")
        print("   → No significant signal detected")


if __name__ == "__main__":
    main()
