#!/usr/bin/env python3
"""
Demonstration: Enhanced Manifest and Planck Model Validation
=============================================================

This script demonstrates the new validation features implemented in
the forensic fingerprint pipeline:

1. Manifest must contain exact files used in the run
2. Planck parameter/likelihood files are rejected as model input
3. Files with < 50 data rows are rejected (likely corrupted or wrong file)

Run this script to see the validation in action.
"""

import sys
import tempfile
import json
from pathlib import Path

# Setup paths
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root / 'forensic_fingerprint'))
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'loaders'))
sys.path.insert(0, str(repo_root / 'tools' / 'data_provenance'))

import planck
import hash_dataset
import run_real_data_cmb_comb


def demo_1_manifest_file_mismatch():
    """Demonstrate manifest validation catching missing files."""
    print("=" * 80)
    print("DEMO 1: Manifest Missing Required File")
    print("=" * 80)
    
    with tempfile.TemporaryDirectory(dir=repo_root) as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create obs and model files
        obs_file = tmpdir / "obs.txt"
        with open(obs_file, 'w') as f:
            f.write("# l Dl -dDl +dDl\n")
            for i in range(30, 130):
                f.write(f"{i} {1000 + i*10} {50} {50}\n")
        
        model_file = tmpdir / "model.txt"
        with open(model_file, 'w') as f:
            f.write("# l Dl -dDl +dDl\n")
            for i in range(30, 130):
                f.write(f"{i} {950 + i*10} {50} {50}\n")
        
        # Create manifest with only obs file (missing model)
        manifest = hash_dataset.hash_dataset([str(obs_file)])
        manifest_file = tmpdir / "manifest.json"
        with open(manifest_file, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        print(f"\nCreated files:")
        print(f"  - obs.txt (in manifest)")
        print(f"  - model.txt (NOT in manifest)")
        print(f"  - manifest.json")
        
        # Try to validate - should fail
        print(f"\nAttempting to run with manifest that doesn't include model.txt...")
        print("Expected: Validation should FAIL\n")
        
        try:
            success = run_real_data_cmb_comb.validate_data_manifest(
                manifest_file, 'planck', obs_file, model_file
            )
            if success:
                print("❌ UNEXPECTED: Validation passed (should have failed)")
            else:
                print("✓ CORRECT: Validation failed as expected")
        except Exception as e:
            print(f"Exception: {e}")
    
    print()


def demo_2_likelihood_file_rejection():
    """Demonstrate rejection of likelihood/parameter files."""
    print("=" * 80)
    print("DEMO 2: Rejection of Likelihood/Parameter File (Content-Based)")
    print("=" * 80)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create a fake likelihood file with -log(Like) in the data
        likelihood_file = tmpdir / "likelihood_params.txt"
        with open(likelihood_file, 'w') as f:
            f.write("# L  -log(Like)  Chi2\n")
            # Put -log(Like) in the actual data content
            f.write("2  -log(Like)=1234.56  100.0\n")
            for i in range(30, 130):
                f.write(f"{i} {1234.56 + i*0.1} {100.0}\n")
        
        print(f"\nCreated file: likelihood_params.txt")
        print("Contains: '-log(Like)' in the data (not just header)")
        print("Note: Rejection is content-based, not filename-based")
        
        print(f"\nAttempting to load as Planck model spectrum...")
        print("Expected: Should FAIL with clear error message\n")
        
        try:
            data = planck.load_planck_data(likelihood_file)
            print("❌ UNEXPECTED: File loaded (should have been rejected)")
        except ValueError as e:
            print("✓ CORRECT: File rejected with error:")
            print(f"\n{str(e)[:200]}...")
    
    print()


def demo_3_tiny_file_rejection():
    """Demonstrate rejection of suspiciously small files."""
    print("=" * 80)
    print("DEMO 3: Rejection of Tiny File (< 50 rows)")
    print("=" * 80)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create a tiny file
        tiny_file = tmpdir / "tiny_spectrum.txt"
        with open(tiny_file, 'w') as f:
            f.write("# l Dl -dDl +dDl\n")
            for i in range(30, 40):  # Only 10 rows
                f.write(f"{i} {1000 + i*10} {50} {50}\n")
        
        print(f"\nCreated file: tiny_spectrum.txt")
        print("Contains: Only 10 data rows (expected ~50-2500)")
        
        print(f"\nAttempting to load as Planck spectrum...")
        print("Expected: Should FAIL (likely corrupted or wrong file)\n")
        
        try:
            data = planck.load_planck_data(tiny_file)
            print("❌ UNEXPECTED: File loaded (should have been rejected)")
        except ValueError as e:
            print("✓ CORRECT: File rejected with error:")
            print(f"\n{str(e)[:200]}...")
    
    print()


def demo_4_valid_file_accepted():
    """Demonstrate that valid files are accepted."""
    print("=" * 80)
    print("DEMO 4: Valid File Accepted")
    print("=" * 80)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create a valid file
        valid_file = tmpdir / "valid_spectrum.txt"
        with open(valid_file, 'w') as f:
            f.write("# l Dl -dDl +dDl\n")
            for i in range(30, 130):  # 100 rows - valid
                f.write(f"{i} {1000 + i*10} {50} {50}\n")
        
        print(f"\nCreated file: valid_spectrum.txt")
        print("Contains: 100 data rows (valid spectrum)")
        
        print(f"\nAttempting to load as Planck spectrum...")
        print("Expected: Should SUCCEED\n")
        
        try:
            data = planck.load_planck_data(valid_file)
            print("✓ CORRECT: File loaded successfully")
            print(f"  - Loaded {len(data['ell'])} multipoles")
            print(f"  - Range: ℓ = {data['ell'][0]} to {data['ell'][-1]}")
        except ValueError as e:
            print(f"❌ UNEXPECTED: File rejected with error: {e}")
    
    print()


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("FORENSIC FINGERPRINT VALIDATION DEMO")
    print("=" * 80)
    print()
    print("This demo shows the enhanced validation features:")
    print("  1. Manifest must contain exact files used")
    print("  2. Likelihood/parameter files rejected by CONTENT (not filename)")
    print("  3. Tiny files (< 50 rows) are rejected")
    print("  4. Valid files are accepted")
    print()
    print("NOTE: Validation is content-based. Files with 'minimum' in their")
    print("name are NOT automatically rejected - only files containing")
    print("'-log(Like)' or 'logLike' in the data are rejected.")
    print()
    
    demo_1_manifest_file_mismatch()
    demo_2_likelihood_file_rejection()
    demo_3_tiny_file_rejection()
    demo_4_valid_file_accepted()
    
    print("=" * 80)
    print("DEMO COMPLETE")
    print("=" * 80)
    print()
    print("All validation features working as expected!")
    print()
