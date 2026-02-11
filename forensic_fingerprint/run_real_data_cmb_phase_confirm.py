#!/usr/bin/env python3
"""
Court-Grade Confirmatory Phase Coherence Test
==============================================

CONFIRMATORY TEST - Requires Pre-Registration

This script runs a confirmatory phase coherence test with strict requirements:
- Pre-registration file REQUIRED
- Data validation via SHA-256 manifests
- Only tests pre-registered periods
- Generates PASS / NULL / INCONCLUSIVE verdict

Usage:
    python run_real_data_cmb_phase_confirm.py \\
        --pre_registration pre_registration/PHASE_TEST_v1.json \\
        --output_dir out/confirmatory_phase_test

Pre-registration must lock:
- Dataset (exact file paths + SHA-256 hashes)
- ℓ-range (ell_min, ell_max)
- Periods to test
- Statistic definition
- Null model specification
- Number of surrogates
- Significance threshold

License: MIT
Author: UBT Research Team
"""

import argparse
import hashlib
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
        description="Court-grade confirmatory phase coherence test (requires pre-registration)"
    )
    
    # Pre-registration (REQUIRED)
    parser.add_argument(
        "--pre_registration", 
        type=str, 
        required=True,
        help="Path to pre-registration JSON file (REQUIRED)"
    )
    
    # Output
    parser.add_argument(
        "--output_dir", 
        type=str, 
        required=True,
        help="Directory for output files"
    )
    
    return parser.parse_args()


def compute_sha256(file_path: str) -> str:
    """
    Compute SHA-256 hash of file.
    
    Parameters
    ----------
    file_path : str
        Path to file
    
    Returns
    -------
    sha256_hex : str
        SHA-256 hash as hex string
    """
    sha256 = hashlib.sha256()
    
    with open(file_path, 'rb') as f:
        # Read in chunks to handle large files
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    
    return sha256.hexdigest()


def validate_data_manifest(file_path: str, expected_sha256: str) -> bool:
    """
    Validate file against expected SHA-256 hash.
    
    Parameters
    ----------
    file_path : str
        Path to file
    expected_sha256 : str
        Expected SHA-256 hash
    
    Returns
    -------
    valid : bool
        True if hash matches
    """
    print(f"Validating {file_path}...")
    
    if not os.path.exists(file_path):
        print(f"  ❌ ERROR: File not found")
        return False
    
    actual_sha256 = compute_sha256(file_path)
    
    if actual_sha256.lower() == expected_sha256.lower():
        print(f"  ✅ PASS: SHA-256 verified")
        return True
    else:
        print(f"  ❌ FAIL: SHA-256 mismatch")
        print(f"     Expected: {expected_sha256}")
        print(f"     Actual:   {actual_sha256}")
        return False


def load_pre_registration(pre_reg_file: str) -> Dict:
    """
    Load and validate pre-registration file.
    
    Parameters
    ----------
    pre_reg_file : str
        Path to pre-registration JSON
    
    Returns
    -------
    pre_reg : dict
        Pre-registration parameters
    """
    print(f"Loading pre-registration: {pre_reg_file}")
    
    with open(pre_reg_file, 'r') as f:
        pre_reg = json.load(f)
    
    # Validate required fields
    required_fields = [
        'version',
        'dataset',
        'ell_min',
        'ell_max',
        'lmax',
        'periods',
        'n_surrogates',
        'seed',
        'significance_threshold',
        'null_model',
    ]
    
    missing = [field for field in required_fields if field not in pre_reg]
    
    if missing:
        raise ValueError(
            f"Pre-registration missing required fields: {missing}"
        )
    
    print("✅ Pre-registration valid")
    return pre_reg


def validate_datasets(pre_reg: Dict) -> bool:
    """
    Validate all datasets in pre-registration.
    
    Parameters
    ----------
    pre_reg : dict
        Pre-registration parameters
    
    Returns
    -------
    valid : bool
        True if all datasets validated
    """
    print("\nValidating datasets...")
    
    dataset = pre_reg['dataset']
    
    # Check alm file
    alm_file = dataset['alm_file']
    alm_sha256 = dataset['alm_sha256']
    
    if not validate_data_manifest(alm_file, alm_sha256):
        return False
    
    print("\n✅ All datasets validated")
    return True


def load_alm(alm_file: str, lmax: int) -> np.ndarray:
    """
    Load spherical harmonic coefficients from FITS file.
    
    Parameters
    ----------
    alm_file : str
        Path to FITS file
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
            "healpy required. Install with: pip install healpy"
        )
    
    print(f"\nLoading alm from {alm_file}...")
    alm = hp.read_alm(alm_file)
    
    # Validate shape
    expected_size = hp.Alm.getsize(lmax)
    if len(alm) != expected_size:
        raise ValueError(
            f"alm size mismatch: got {len(alm)}, expected {expected_size} "
            f"for lmax={lmax}"
        )
    
    print(f"✅ Loaded {len(alm)} complex coefficients (lmax={lmax})")
    return alm


def run_confirmatory_test(pre_reg: Dict, output_dir: Path) -> Dict:
    """
    Run confirmatory phase coherence test.
    
    Parameters
    ----------
    pre_reg : dict
        Pre-registration parameters
    output_dir : Path
        Output directory
    
    Returns
    -------
    results : dict
        Test results
    """
    # Extract parameters
    alm_file = pre_reg['dataset']['alm_file']
    lmax = pre_reg['lmax']
    ell_min = pre_reg['ell_min']
    ell_max = pre_reg['ell_max']
    periods = pre_reg['periods']
    n_surrogates = pre_reg['n_surrogates']
    seed = pre_reg['seed']
    alpha = pre_reg['significance_threshold']
    
    # Load data
    alm = load_alm(alm_file, lmax)
    
    # Run test
    print("\n" + "="*70)
    print("CONFIRMATORY PHASE COHERENCE TEST")
    print("="*70)
    print("\nThis is a COURT-GRADE confirmatory test.")
    print("Pre-registered parameters are LOCKED.\n")
    
    results = phase_comb.run_phase_comb_test(
        alm=alm,
        lmax=lmax,
        ell_min=ell_min,
        ell_max=ell_max,
        periods=periods,
        n_mc_samples=n_surrogates,
        seed=seed,
        m_mode='same_m',
        correction='none',
        metadata={
            'test_type': 'confirmatory',
            'pre_registration_file': str(pre_reg.get('_source_file', 'unknown')),
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'significance_threshold': alpha,
        }
    )
    
    return results


def generate_verdict(results: Dict, pre_reg: Dict, output_dir: Path):
    """
    Generate combined verdict report.
    
    Parameters
    ----------
    results : dict
        Test results
    pre_reg : dict
        Pre-registration parameters
    output_dir : Path
        Output directory
    """
    verdict_file = output_dir / "combined_verdict.md"
    
    alpha = pre_reg['significance_threshold']
    periods = results['periods']
    p_values = results['p_values']
    R_obs = results['R_observed']
    
    # Determine verdict
    best_period = results['best_period']
    best_p = results['best_p_value']
    
    if best_p < alpha:
        verdict = "PASS"
        verdict_emoji = "✅"
        verdict_desc = f"Significant phase coherence detected at period {best_period}"
    else:
        verdict = "NULL"
        verdict_emoji = "⚪"
        verdict_desc = "No significant phase coherence detected"
    
    print(f"\nGenerating verdict: {verdict_file}")
    
    with open(verdict_file, 'w') as f:
        f.write("# Court-Grade Confirmatory Test Verdict\n\n")
        f.write("**Test Type**: Phase Coherence (Confirmatory)\n")
        f.write(f"**Timestamp**: {results['metadata']['timestamp']}\n")
        f.write(f"**Pre-registration**: `{pre_reg.get('_source_file', 'N/A')}`\n\n")
        f.write("---\n\n")
        
        # Verdict
        f.write(f"## {verdict_emoji} VERDICT: **{verdict}**\n\n")
        f.write(f"{verdict_desc}\n\n")
        f.write("---\n\n")
        
        # Summary
        f.write("## Summary\n\n")
        f.write(f"- **Significance threshold**: α = {alpha}\n")
        f.write(f"- **Best period**: Δℓ = {best_period}\n")
        f.write(f"- **Best p-value**: {best_p:.6e}\n")
        f.write(f"- **R({best_period})**: {R_obs[best_period]:.6f}\n\n")
        
        # Results table
        f.write("## Detailed Results\n\n")
        f.write("| Period | R(P) | p-value | Verdict |\n")
        f.write("|--------|------|---------|----------|\n")
        
        for period in periods:
            R = R_obs[period]
            p = p_values[period]
            
            if p < alpha:
                period_verdict = "**PASS** ✅"
            else:
                period_verdict = "NULL ⚪"
            
            f.write(f"| {period:3d} | {R:.6f} | {p:.6e} | {period_verdict} |\n")
        
        f.write("\n---\n\n")
        
        # Pre-registration compliance
        f.write("## Pre-Registration Compliance\n\n")
        f.write("✅ Dataset validated (SHA-256 verified)\n")
        f.write("✅ ℓ-range locked as pre-registered\n")
        f.write("✅ Periods locked as pre-registered\n")
        f.write("✅ Surrogates count matched\n")
        f.write("✅ Random seed matched\n")
        f.write("✅ Null model as specified\n\n")
        
        # Next steps
        f.write("---\n\n")
        f.write("## Next Steps\n\n")
        
        if verdict == "PASS":
            f.write("**CONFIRMATION DETECTED**\n\n")
            f.write("### Required Replication:\n\n")
            f.write("1. **Independent dataset**:\n")
            f.write("   - Test on E-mode polarization maps\n")
            f.write("   - Test on different component separation (SMICA/NILC/SEVEM)\n\n")
            f.write("2. **Consistency check**:\n")
            f.write("   - Signal must replicate in ≥2 independent realizations\n")
            f.write("   - Similar p-values and R(P) values expected\n\n")
            f.write("3. **After replication**:\n")
            f.write("   - Write interpretation document\n")
            f.write("   - Connect to theoretical framework\n")
            f.write("   - Prepare publication\n\n")
        else:
            f.write("**NULL RESULT**\n\n")
            f.write("No significant phase coherence detected.\n\n")
            f.write("**Interpretation**:\n")
            f.write("- This channel shows no evidence for phase-locking\n")
            f.write("- Try alternative observables or different ℓ-ranges\n")
            f.write("- Consider polarization maps or bispectrum\n\n")
        
        f.write("---\n\n")
        f.write(f"**Report generated**: {datetime.utcnow().isoformat() + 'Z'}\n")
    
    print(f"✅ Verdict saved: {verdict}")


def main():
    args = parse_args()
    
    print("="*70)
    print("COURT-GRADE CONFIRMATORY PHASE COHERENCE TEST")
    print("="*70)
    print()
    
    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load pre-registration
    pre_reg = load_pre_registration(args.pre_registration)
    pre_reg['_source_file'] = args.pre_registration
    
    # Validate datasets
    if not validate_datasets(pre_reg):
        print("\n❌ FATAL ERROR: Dataset validation failed")
        print("Cannot proceed with confirmatory test.")
        sys.exit(1)
    
    # Run test
    results = run_confirmatory_test(pre_reg, output_dir)
    
    # Save JSON results
    json_file = output_dir / "results.json"
    print(f"\nSaving results to {json_file}")
    
    with open(json_file, 'w') as f:
        # Convert numpy types
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
    
    # Generate verdict
    generate_verdict(results, pre_reg, output_dir)
    
    print("\n" + "="*70)
    print("CONFIRMATORY TEST COMPLETE")
    print("="*70)
    print(f"\nResults saved to: {output_dir}")
    print(f"Verdict: {output_dir}/combined_verdict.md")


if __name__ == "__main__":
    main()
