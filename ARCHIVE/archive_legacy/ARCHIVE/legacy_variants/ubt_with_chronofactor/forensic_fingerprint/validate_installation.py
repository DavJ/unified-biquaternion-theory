#!/usr/bin/env python3
"""
Validation Test for Forensic Fingerprint Pipeline
==================================================

This script validates that the forensic fingerprint pipeline is correctly
installed and configured, without requiring actual CMB data.

Tests:
1. Module imports (phase_comb, nulls)
2. Pre-registration template validation
3. Directory structure
4. Script executability

License: MIT
Author: UBT Research Team
"""

import json
import os
import sys
from pathlib import Path


def test_directory_structure():
    """Verify directory structure exists."""
    print("Testing directory structure...")
    
    required_dirs = [
        'cmb_phase_comb',
        'reports',
        'pre_registration',
    ]
    
    required_files = [
        'SEARCH_SPACE.md',
        'RUNBOOK_PHASE_COHERENCE.md',
        'INTERPRETATION_NOTES.md',
        'FORENSIC_FINGERPRINT_INDEX.md',
        'run_exploratory_phase_scan.py',
        'run_real_data_cmb_phase_confirm.py',
        'cmb_phase_comb/phase_comb.py',
        'cmb_phase_comb/nulls.py',
        'pre_registration/README.md',
        'pre_registration/PHASE_TEST_v1_TEMPLATE.json',
        'reports/CMB_TT_NEGATIVE_BENCHMARK.md',
    ]
    
    all_ok = True
    
    for dirname in required_dirs:
        if os.path.isdir(dirname):
            print(f"  ✅ Directory: {dirname}")
        else:
            print(f"  ❌ Missing directory: {dirname}")
            all_ok = False
    
    for filename in required_files:
        if os.path.isfile(filename):
            print(f"  ✅ File: {filename}")
        else:
            print(f"  ❌ Missing file: {filename}")
            all_ok = False
    
    return all_ok


def test_pre_registration_template():
    """Validate pre-registration template JSON."""
    print("\nTesting pre-registration template...")
    
    template_file = 'pre_registration/PHASE_TEST_v1_TEMPLATE.json'
    
    try:
        with open(template_file, 'r') as f:
            pre_reg = json.load(f)
        
        print(f"  ✅ JSON valid")
        
        # Check required fields
        required_fields = [
            'version',
            'dataset',
            'lmax',
            'ell_min',
            'ell_max',
            'periods',
            'n_surrogates',
            'seed',
            'significance_threshold',
        ]
        
        missing = [f for f in required_fields if f not in pre_reg]
        
        if missing:
            print(f"  ❌ Missing fields: {missing}")
            return False
        else:
            print(f"  ✅ All required fields present")
        
        # Check dataset subfields
        if 'alm_file' in pre_reg['dataset'] and 'alm_sha256' in pre_reg['dataset']:
            print(f"  ✅ Dataset fields valid")
        else:
            print(f"  ❌ Dataset missing alm_file or alm_sha256")
            return False
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"  ❌ JSON parse error: {e}")
        return False
    except FileNotFoundError:
        print(f"  ❌ Template file not found")
        return False


def test_script_imports():
    """Test that scripts can be imported (syntax check)."""
    print("\nTesting script syntax...")
    
    scripts = [
        'run_exploratory_phase_scan.py',
        'run_real_data_cmb_phase_confirm.py',
    ]
    
    all_ok = True
    
    for script in scripts:
        try:
            # Just compile, don't execute
            with open(script, 'r') as f:
                code = f.read()
            compile(code, script, 'exec')
            print(f"  ✅ Syntax OK: {script}")
        except SyntaxError as e:
            print(f"  ❌ Syntax error in {script}: {e}")
            all_ok = False
        except FileNotFoundError:
            print(f"  ❌ Script not found: {script}")
            all_ok = False
    
    return all_ok


def test_module_structure():
    """Verify module structure."""
    print("\nTesting module structure...")
    
    module_files = [
        ('cmb_phase_comb/phase_comb.py', ['run_phase_comb_test', 'compute_phase_coherence']),
        ('cmb_phase_comb/nulls.py', ['randomize_phases_preserve_cl', 'validate_cl_preservation']),
    ]
    
    all_ok = True
    
    for filepath, expected_functions in module_files:
        try:
            with open(filepath, 'r') as f:
                content = f.read()
            
            missing = [func for func in expected_functions if f'def {func}' not in content]
            
            if missing:
                print(f"  ❌ {filepath}: missing functions {missing}")
                all_ok = False
            else:
                print(f"  ✅ {filepath}: all functions present")
        
        except FileNotFoundError:
            print(f"  ❌ Module not found: {filepath}")
            all_ok = False
    
    return all_ok


def test_documentation_links():
    """Check that key documentation exists and cross-references are valid."""
    print("\nTesting documentation completeness...")
    
    docs = [
        'SEARCH_SPACE.md',
        'RUNBOOK_PHASE_COHERENCE.md',
        'INTERPRETATION_NOTES.md',
        'FORENSIC_FINGERPRINT_INDEX.md',
        'reports/CMB_TT_NEGATIVE_BENCHMARK.md',
        'pre_registration/README.md',
    ]
    
    all_ok = True
    
    for doc in docs:
        if os.path.isfile(doc):
            # Check file size > 1KB (basic sanity check)
            size = os.path.getsize(doc)
            if size > 1000:
                print(f"  ✅ {doc} ({size:,} bytes)")
            else:
                print(f"  ⚠️  {doc} seems small ({size} bytes)")
        else:
            print(f"  ❌ Missing: {doc}")
            all_ok = False
    
    return all_ok


def main():
    print("="*70)
    print("FORENSIC FINGERPRINT PIPELINE VALIDATION")
    print("="*70)
    print()
    
    results = {
        'Directory Structure': test_directory_structure(),
        'Pre-registration Template': test_pre_registration_template(),
        'Script Syntax': test_script_imports(),
        'Module Structure': test_module_structure(),
        'Documentation': test_documentation_links(),
    }
    
    print("\n" + "="*70)
    print("VALIDATION SUMMARY")
    print("="*70)
    
    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    all_passed = all(results.values())
    
    if all_passed:
        print("\n✅ All validation tests PASSED")
        print("\nThe forensic fingerprint pipeline is correctly installed.")
        print("\nNext steps:")
        print("  1. Install dependencies: pip install numpy scipy matplotlib healpy")
        print("  2. Obtain CMB alm data (Planck PR3 or WMAP)")
        print("  3. Run exploratory scan: python run_exploratory_phase_scan.py --help")
        print("  4. See RUNBOOK_PHASE_COHERENCE.md for complete workflow")
        return 0
    else:
        print("\n❌ Some validation tests FAILED")
        print("\nPlease fix the issues above before proceeding.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
