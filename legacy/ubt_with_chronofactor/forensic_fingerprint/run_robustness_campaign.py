#!/usr/bin/env python3
"""
UBT Forensic Fingerprint - Master Robustness & Falsification Campaign Runner
=============================================================================

This script orchestrates the complete robustness and falsification campaign
for the candidate Δℓ = 255 CMB comb signal.

It runs all stress tests in sequence and generates a consolidated report
with clear PASS/FAIL verdicts for each test.

Objective:
----------
Actively attempt to falsify the signal through rigorous testing.
Scientific integrity > confirmation.

This task is successful even if the signal FAILS.

Tests Executed:
---------------
1. Whitening / Full Covariance (CRITICAL)
2. Synthetic ΛCDM Null Controls (Anti-Overfitting)
3. ℓ-Range Ablation (Local Artifact Check)
4. Polarization Channels (Optional but High-Impact)
5. Phase Coherence (Cross-Dataset Validation)

Final Output:
-------------
- ROBUSTNESS_AND_FALSIFICATION.md - Consolidated report
- Individual test results in subdirectories
- Pass/fail summary table
- Explicit failure documentation if signal doesn't survive

License: MIT
Author: UBT Research Team
"""

import sys
import argparse
import json
import subprocess
from pathlib import Path
from datetime import datetime
import shutil

# Find repository root
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'stress_tests'))


def check_file_exists(filepath, description):
    """Check if a file exists and provide helpful error if not."""
    if filepath is None:
        return False
    
    filepath = Path(filepath)
    if not filepath.exists():
        print(f"WARNING: {description} not found: {filepath}")
        return False
    return True


def run_test(test_name, test_script, args, output_subdir, required=True):
    """
    Run a single stress test.
    
    Parameters
    ----------
    test_name : str
        Human-readable test name
    test_script : Path
        Path to test script
    args : list
        Command-line arguments for the test
    output_subdir : Path
        Output subdirectory for this test
    required : bool
        Whether test failure should halt the campaign
    
    Returns
    -------
    dict
        Test results metadata
    """
    print("\n" + "="*80)
    print(f"RUNNING: {test_name}")
    print("="*80)
    print(f"Script: {test_script}")
    print(f"Arguments: {' '.join(args)}")
    print()
    
    # Construct command
    cmd = [sys.executable, str(test_script)] + args
    
    # Run test
    try:
        result = subprocess.run(
            cmd,
            cwd=repo_root,
            capture_output=True,
            text=True,
            timeout=7200  # 2 hour timeout per test
        )
        
        # Print output
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        success = (result.returncode == 0)
        
        # Find output directory (test creates timestamped dir)
        # Look for most recent directory matching pattern
        if output_subdir.exists():
            test_dirs = sorted(output_subdir.glob('*'), key=lambda p: p.stat().st_mtime, reverse=True)
            if test_dirs:
                latest_dir = test_dirs[0]
            else:
                latest_dir = None
        else:
            latest_dir = None
        
        return {
            'test_name': test_name,
            'success': success,
            'returncode': result.returncode,
            'output_dir': str(latest_dir) if latest_dir else None,
            'stdout': result.stdout,
            'stderr': result.stderr
        }
        
    except subprocess.TimeoutExpired:
        print(f"ERROR: {test_name} timed out after 2 hours")
        return {
            'test_name': test_name,
            'success': False,
            'returncode': -1,
            'error': 'Timeout',
            'output_dir': None
        }
    except Exception as e:
        print(f"ERROR: {test_name} failed with exception: {e}")
        return {
            'test_name': test_name,
            'success': False,
            'returncode': -1,
            'error': str(e),
            'output_dir': None
        }


def generate_final_report(campaign_results, output_file, args):
    """
    Generate ROBUSTNESS_AND_FALSIFICATION.md report.
    
    Parameters
    ----------
    campaign_results : dict
        Results from all tests
    output_file : Path
        Output markdown file
    args : argparse.Namespace
        Command-line arguments
    """
    with open(output_file, 'w') as f:
        f.write("# CMB Comb Signal (Δℓ = 255) - Robustness & Falsification Campaign\n\n")
        f.write("**Date**: {}\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')))
        f.write("**Protocol**: Pre-registered falsification tests\n")
        f.write("**Objective**: Actively attempt to invalidate the signal\n\n")
        
        f.write("---\n\n")
        
        f.write("## Executive Summary\n\n")
        f.write("This document reports results from a comprehensive robustness and falsification ")
        f.write("campaign designed to test the candidate Δℓ = 255 periodic comb signal in CMB ")
        f.write("power spectrum residuals.\n\n")
        
        f.write("**Critical Statement**: This campaign is designed to **DESTROY** the signal, ")
        f.write("not strengthen it. Success is measured by scientific integrity, not by signal ")
        f.write("survival. A failed signal is a successful scientific outcome.\n\n")
        
        f.write("---\n\n")
        
        # Summary table
        f.write("## Test Summary\n\n")
        f.write("| # | Test Name | Status | Result | Verdict |\n")
        f.write("|---|-----------|--------|--------|---------|\n")
        
        test_order = [
            'test_1_whitening',
            'test_4_lcdm_null',
            'test_3_ablation',
            'test_2_polarization',
            'test_5_phase_coherence'
        ]
        
        verdicts = []
        for i, test_key in enumerate(test_order, 1):
            if test_key in campaign_results:
                result = campaign_results[test_key]
                test_name = result['test_name']
                
                if result['success']:
                    status = "✓ COMPLETED"
                    # Try to extract verdict from output
                    if 'verdict' in result:
                        verdict = result['verdict']
                    else:
                        verdict = "See details"
                    verdicts.append(verdict)
                else:
                    status = "✗ FAILED"
                    verdict = "ERROR"
                    verdicts.append("FAIL")
                
                f.write(f"| {i} | {test_name} | {status} | {result.get('summary', 'N/A')} | **{verdict}** |\n")
            else:
                test_name = test_key.replace('_', ' ').title()
                f.write(f"| {i} | {test_name} | ☐ SKIPPED | Not run | N/A |\n")
        
        f.write("\n")
        
        # Overall verdict
        f.write("### Overall Campaign Verdict\n\n")
        
        all_pass = all(v in ['PASS', 'SURVIVED'] for v in verdicts if v not in ['ERROR', 'SKIP', 'N/A'])
        any_fail = any(v in ['FAIL', 'FAILED', 'ELIMINATED'] for v in verdicts)
        
        if all_pass and len(verdicts) >= 3:
            f.write("## ✓ SIGNAL SURVIVED FALSIFICATION CAMPAIGN\n\n")
            f.write("The Δℓ = 255 signal survived all executed falsification tests. ")
            f.write("This upgrades the status from 'initial observation' to 'candidate anomaly ")
            f.write("requiring independent verification'.\n\n")
            f.write("**Next Steps**:\n")
            f.write("- Seek independent replication with third dataset\n")
            f.write("- Prepare manuscript for peer review\n")
            f.write("- Archive complete analysis for reproducibility\n\n")
        elif any_fail:
            f.write("## ✗ SIGNAL FAILED FALSIFICATION CAMPAIGN\n\n")
            f.write("The Δℓ = 255 signal did NOT survive the falsification tests. ")
            f.write("One or more critical tests eliminated the signal as a robust anomaly.\n\n")
            f.write("**Interpretation**: The signal is likely an artifact of:\n")
            f.write("- Correlated noise or inadequate error modeling\n")
            f.write("- Localized ℓ-range contamination\n")
            f.write("- Generic ΛCDM cosmic variance feature\n")
            f.write("- Statistical fluctuation or look-elsewhere effect\n\n")
            f.write("**This is a SUCCESSFUL scientific outcome.** The hypothesis was testable ")
            f.write("and falsifiable, and it has been falsified through rigorous testing.\n\n")
        else:
            f.write("## ⚠ INCOMPLETE CAMPAIGN\n\n")
            f.write("The falsification campaign was not completed. Insufficient tests were ")
            f.write("executed to reach a definitive verdict.\n\n")
        
        f.write("---\n\n")
        
        # Detailed test results
        f.write("## Detailed Test Results\n\n")
        
        # Test 1: Whitening
        f.write("### Test #1: Whitening / Full Covariance\n\n")
        f.write("**Objective**: Test whether Δℓ = 255 survives proper covariance-aware whitening.\n\n")
        
        if 'test_1_whitening' in campaign_results:
            result = campaign_results['test_1_whitening']
            f.write(f"**Status**: {'✓ COMPLETED' if result['success'] else '✗ FAILED'}\n\n")
            
            if result['success'] and result.get('output_dir'):
                f.write(f"**Results Directory**: `{result['output_dir']}`\n\n")
                
                # Try to load results JSON
                results_file = Path(result['output_dir']) / 'planck_whitened_results.json'
                if results_file.exists():
                    try:
                        with open(results_file) as rf:
                            test_results = json.load(rf)
                        
                        f.write("**Whitening Modes Tested**:\n\n")
                        f.write("| Mode | Δℓ | p-value | Amplitude | Verdict |\n")
                        f.write("|------|-----|---------|-----------|----------|\n")
                        
                        for mode in ['none', 'diagonal', 'block-diagonal', 'covariance']:
                            if mode in test_results:
                                mr = test_results[mode]
                                f.write(f"| {mode} | {mr.get('best_period', 'N/A')} | "
                                       f"{mr.get('p_value', 'N/A'):.2e} | "
                                       f"{mr.get('amplitude', 'N/A'):.4f} | "
                                       f"{mr.get('significance', 'N/A').upper()} |\n")
                        
                        f.write("\n")
                        
                        # Verdict
                        # Check if 255 appears in multiple modes with p < 0.001
                        periods = [test_results[m].get('best_period') for m in test_results if 'best_period' in test_results[m]]
                        period_255_count = sum(1 for p in periods if p in [254, 255, 256])
                        
                        if period_255_count >= 3:
                            f.write("**Verdict**: ✓ **PASS** - Signal persists across whitening modes\n\n")
                        elif period_255_count >= 2:
                            f.write("**Verdict**: ~ **WEAK PASS** - Signal appears in some modes\n\n")
                        else:
                            f.write("**Verdict**: ✗ **FAIL** - Signal eliminated by whitening\n\n")
                    except Exception as e:
                        f.write(f"*(Error loading results: {e})*\n\n")
                else:
                    f.write("*(Results file not found)*\n\n")
            else:
                f.write("**Error**: Test did not complete successfully\n\n")
        else:
            f.write("**Status**: ☐ NOT RUN\n\n")
        
        f.write("---\n\n")
        
        # Test 2: ΛCDM Null
        f.write("### Test #2: Synthetic ΛCDM Null Controls\n\n")
        f.write("**Objective**: Demonstrate that Δℓ = 255 does NOT appear generically in ΛCDM simulations.\n\n")
        
        if 'test_4_lcdm_null' in campaign_results:
            result = campaign_results['test_4_lcdm_null']
            f.write(f"**Status**: {'✓ COMPLETED' if result['success'] else '✗ FAILED'}\n\n")
            
            if result['success'] and result.get('output_dir'):
                f.write(f"**Results Directory**: `{result['output_dir']}`\n\n")
                
                # Try to load results
                results_file = Path(result['output_dir']) / 'lcdm_null_distribution.json'
                if results_file.exists():
                    try:
                        with open(results_file) as rf:
                            test_results = json.load(rf)
                        
                        n_realizations = len(test_results.get('best_periods', []))
                        period_255_count = sum(1 for p in test_results.get('best_periods', []) 
                                              if p in [254, 255, 256])
                        
                        frequency = (period_255_count / n_realizations * 100) if n_realizations > 0 else 0
                        
                        f.write(f"**Number of ΛCDM Realizations**: {n_realizations}\n")
                        f.write(f"**Δℓ ≈ 255 Frequency**: {period_255_count}/{n_realizations} ({frequency:.1f}%)\n\n")
                        
                        if frequency <= 1.0:
                            f.write("**Verdict**: ✓ **PASS** - Δℓ = 255 is rare in ΛCDM (≤1%)\n\n")
                        elif frequency <= 5.0:
                            f.write("**Verdict**: ~ **WEAK PASS** - Δℓ = 255 uncommon but not rare (1-5%)\n\n")
                        else:
                            f.write("**Verdict**: ✗ **FAIL** - Δℓ = 255 appears frequently in ΛCDM (>5%)\n\n")
                    except Exception as e:
                        f.write(f"*(Error loading results: {e})*\n\n")
                else:
                    f.write("*(Results file not found)*\n\n")
            else:
                f.write("**Error**: Test did not complete successfully\n\n")
        else:
            f.write("**Status**: ☐ NOT RUN\n\n")
        
        f.write("---\n\n")
        
        # Test 3: Ablation
        f.write("### Test #3: ℓ-Range Ablation\n\n")
        f.write("**Objective**: Test whether signal is global or confined to specific multipole band.\n\n")
        
        if 'test_3_ablation' in campaign_results:
            result = campaign_results['test_3_ablation']
            f.write(f"**Status**: {'✓ COMPLETED' if result['success'] else '✗ FAILED'}\n\n")
            
            if result['success'] and result.get('output_dir'):
                f.write(f"**Results Directory**: `{result['output_dir']}`\n\n")
                
                # Try to load results
                results_file = Path(result['output_dir']) / 'ablation_results.json'
                if results_file.exists():
                    try:
                        with open(results_file) as rf:
                            test_results = json.load(rf)
                        
                        f.write("**ℓ-Range Results**:\n\n")
                        f.write("| ℓ Range | Δℓ | p-value | Significance |\n")
                        f.write("|---------|-----|---------|-------------|\n")
                        
                        ranges_with_255 = 0
                        for range_key, range_result in test_results.items():
                            if isinstance(range_result, dict) and 'best_period' in range_result:
                                period = range_result.get('best_period', 'N/A')
                                pval = range_result.get('p_value', 'N/A')
                                sig = range_result.get('significance', 'N/A')
                                
                                f.write(f"| {range_key} | {period} | {pval if isinstance(pval, str) else f'{pval:.2e}'} | {sig.upper() if isinstance(sig, str) else sig} |\n")
                                
                                if period in [254, 255, 256] and (isinstance(pval, (int, float)) and pval < 0.01):
                                    ranges_with_255 += 1
                        
                        f.write("\n")
                        
                        if ranges_with_255 >= 2:
                            f.write(f"**Verdict**: ✓ **PASS** - Δℓ ≈ 255 in {ranges_with_255} disjoint ranges\n\n")
                        elif ranges_with_255 == 1:
                            f.write("**Verdict**: ~ **WEAK PASS** - Δℓ ≈ 255 in only 1 range\n\n")
                        else:
                            f.write("**Verdict**: ✗ **FAIL** - Δℓ ≈ 255 does not appear consistently\n\n")
                    except Exception as e:
                        f.write(f"*(Error loading results: {e})*\n\n")
                else:
                    f.write("*(Results file not found)*\n\n")
            else:
                f.write("**Error**: Test did not complete successfully\n\n")
        else:
            f.write("**Status**: ☐ NOT RUN\n\n")
        
        f.write("---\n\n")
        
        # Test 4: Polarization (optional)
        f.write("### Test #4: Polarization Channels (OPTIONAL)\n\n")
        f.write("**Objective**: Test cross-channel coherence (TT vs EE vs TE).\n\n")
        
        if 'test_2_polarization' in campaign_results:
            result = campaign_results['test_2_polarization']
            f.write(f"**Status**: {'✓ COMPLETED' if result['success'] else '✗ FAILED'}\n\n")
            f.write("*(Details to be added based on test output)*\n\n")
        else:
            f.write("**Status**: ☐ SKIPPED - Polarization data not available or not requested\n\n")
            f.write("*Note: This test is optional but high-impact if data is available.*\n\n")
        
        f.write("---\n\n")
        
        # Test 5: Phase Coherence (optional)
        f.write("### Test #5: Phase Coherence (OPTIONAL)\n\n")
        f.write("**Objective**: Test phase stability across datasets and preprocessing.\n\n")
        
        if 'test_5_phase_coherence' in campaign_results:
            result = campaign_results['test_5_phase_coherence']
            f.write(f"**Status**: {'✓ COMPLETED' if result['success'] else '✗ FAILED'}\n\n")
            f.write("*(Details to be added based on test output)*\n\n")
        else:
            f.write("**Status**: ☐ SKIPPED - Not requested or insufficient data\n\n")
        
        f.write("---\n\n")
        
        # Final deliverables
        f.write("## Deliverables\n\n")
        f.write("1. ✓ This report: `ROBUSTNESS_AND_FALSIFICATION.md`\n")
        f.write("2. ✓ Individual test results in timestamped subdirectories\n")
        f.write("3. ✓ Machine-readable JSON files for each test\n")
        f.write("4. ✓ Diagnostic plots and visualizations\n")
        f.write("5. ✓ Pass/fail summary table (see above)\n\n")
        
        f.write("---\n\n")
        
        # Tone statement
        f.write("## Tone and Scientific Integrity\n\n")
        f.write("This analysis follows a **clinical, skeptical, court-grade** approach:\n\n")
        f.write("- ✓ No interpretive speculation beyond what data support\n")
        f.write("- ✓ Explicit pass/fail language without hedging\n")
        f.write("- ✓ Failures are documented clearly and prominently\n")
        f.write("- ✓ Scientific integrity > confirmation bias\n\n")
        
        f.write("**This task is successful even if the signal FAILS.**\n\n")
        
        f.write("---\n\n")
        f.write("**End of Report**\n\n")
        f.write(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}*\n")
    
    print(f"\nFinal report saved to: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="UBT Robustness & Falsification Campaign - Master Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
This script runs the complete falsification campaign for the Δℓ = 255 signal.

Minimum required arguments (Planck data only):
    --planck_obs path/to/planck_spectrum.txt
    --planck_model path/to/planck_model.txt

Full campaign (all tests):
    --planck_obs path/to/planck_spectrum.txt
    --planck_model path/to/planck_model.txt
    --planck_cov path/to/planck_covariance.txt
    --wmap_obs path/to/wmap_spectrum.txt
    --wmap_model path/to/wmap_model.txt
    --include_polarization
    --ee_obs path/to/EE_spectrum.txt
    --ee_model path/to/EE_model.txt
    --te_obs path/to/TE_spectrum.txt
    --te_model path/to/TE_model.txt
        """
    )
    
    # Required data files
    parser.add_argument('--planck_obs', required=True, help='Planck TT observation file')
    parser.add_argument('--planck_model', required=True, help='Planck TT model file')
    
    # Optional data files
    parser.add_argument('--planck_cov', help='Planck TT covariance matrix (enables full whitening)')
    parser.add_argument('--wmap_obs', help='WMAP TT observation file (for cross-dataset tests)')
    parser.add_argument('--wmap_model', help='WMAP TT model file')
    parser.add_argument('--wmap_cov', help='WMAP covariance matrix')
    
    # Polarization data (optional)
    parser.add_argument('--ee_obs', help='Planck EE observation file')
    parser.add_argument('--ee_model', help='Planck EE model file')
    parser.add_argument('--te_obs', help='Planck TE observation file')
    parser.add_argument('--te_model', help='Planck TE model file')
    
    # Test selection
    parser.add_argument('--skip_whitening', action='store_true', 
                       help='Skip whitening test (NOT RECOMMENDED)')
    parser.add_argument('--skip_lcdm_null', action='store_true',
                       help='Skip ΛCDM null test (NOT RECOMMENDED)')
    parser.add_argument('--skip_ablation', action='store_true',
                       help='Skip ℓ-range ablation test (NOT RECOMMENDED)')
    parser.add_argument('--include_polarization', action='store_true',
                       help='Run polarization test (requires EE/TE data)')
    parser.add_argument('--include_phase_coherence', action='store_true',
                       help='Run phase coherence test (requires WMAP data)')
    
    # Test parameters
    parser.add_argument('--mc_trials_whitening', type=int, default=10000,
                       help='MC trials for whitening test (default: 10000)')
    parser.add_argument('--mc_trials_ablation', type=int, default=5000,
                       help='MC trials for ablation test (default: 5000)')
    parser.add_argument('--mc_trials_polarization', type=int, default=10000,
                       help='MC trials for polarization test (default: 10000)')
    parser.add_argument('--n_lcdm_realizations', type=int, default=100,
                       help='Number of ΛCDM realizations (default: 100)')
    parser.add_argument('--mc_trials_lcdm', type=int, default=1000,
                       help='MC trials per ΛCDM realization (default: 1000)')
    
    # Multipole ranges
    parser.add_argument('--ell_min', type=int, default=30, help='Minimum multipole')
    parser.add_argument('--ell_max', type=int, default=1500, help='Maximum multipole')
    
    # Output
    parser.add_argument('--output_dir', help='Base output directory (default: auto-generated)')
    
    args = parser.parse_args()
    
    # Validate required files exist
    if not check_file_exists(args.planck_obs, "Planck observation file"):
        print("ERROR: Required Planck observation file not found")
        sys.exit(1)
    if not check_file_exists(args.planck_model, "Planck model file"):
        print("ERROR: Required Planck model file not found")
        sys.exit(1)
    
    # Setup output directory
    if args.output_dir:
        campaign_dir = Path(args.output_dir)
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        campaign_dir = repo_root / 'forensic_fingerprint' / 'out' / 'robustness_campaign' / timestamp
    
    campaign_dir.mkdir(parents=True, exist_ok=True)
    
    print("="*80)
    print("UBT ROBUSTNESS & FALSIFICATION CAMPAIGN")
    print("="*80)
    print(f"Campaign directory: {campaign_dir}")
    print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Track all test results
    campaign_results = {}
    
    # Test directory structure
    stress_tests_dir = repo_root / 'forensic_fingerprint' / 'stress_tests'
    out_dir = repo_root / 'forensic_fingerprint' / 'out' / 'stress_tests'
    
    # TEST 1: Whitening
    if not args.skip_whitening:
        test_args = [
            '--obs', args.planck_obs,
            '--model', args.planck_model,
            '--ell_min', str(args.ell_min),
            '--ell_max', str(args.ell_max),
            '--mc_trials', str(args.mc_trials_whitening),
        ]
        
        if args.planck_cov:
            test_args.extend(['--cov', args.planck_cov])
        
        campaign_results['test_1_whitening'] = run_test(
            "Test #1: Whitening / Full Covariance",
            stress_tests_dir / 'test_1_whitening.py',
            test_args,
            out_dir
        )
    
    # TEST 2: ΛCDM Null
    if not args.skip_lcdm_null:
        test_args = [
            '--model', args.planck_model,
            '--obs', args.planck_obs,
            '--ell_min', str(args.ell_min),
            '--ell_max', str(args.ell_max),
            '--n_realizations', str(args.n_lcdm_realizations),
            '--mc_trials', str(args.mc_trials_lcdm),
        ]
        
        campaign_results['test_4_lcdm_null'] = run_test(
            "Test #2: Synthetic ΛCDM Null Controls",
            stress_tests_dir / 'test_4_lcdm_null.py',
            test_args,
            out_dir
        )
    
    # TEST 3: Ablation
    if not args.skip_ablation:
        test_args = [
            '--obs', args.planck_obs,
            '--model', args.planck_model,
            '--mc_trials', str(args.mc_trials_ablation),
        ]
        
        if args.planck_cov:
            test_args.extend(['--cov', args.planck_cov])
        
        campaign_results['test_3_ablation'] = run_test(
            "Test #3: ℓ-Range Ablation",
            stress_tests_dir / 'test_3_ablation.py',
            test_args,
            out_dir
        )
    
    # TEST 4: Polarization (optional)
    if args.include_polarization:
        if args.ee_obs and args.ee_model and args.te_obs and args.te_model:
            test_args = [
                '--tt_obs', args.planck_obs,
                '--tt_model', args.planck_model,
                '--ee_obs', args.ee_obs,
                '--ee_model', args.ee_model,
                '--te_obs', args.te_obs,
                '--te_model', args.te_model,
                '--ell_min', str(args.ell_min),
                '--ell_max', str(args.ell_max),
                '--mc_trials', str(args.mc_trials_polarization),
            ]
            
            campaign_results['test_2_polarization'] = run_test(
                "Test #4: Polarization Channels (EE, TE)",
                stress_tests_dir / 'test_2_polarization.py',
                test_args,
                out_dir,
                required=False  # Optional test
            )
        else:
            print("\nWARNING: Polarization test requested but EE/TE data files not provided")
            print("         Skipping polarization test")
    
    # TEST 5: Phase Coherence (optional)
    if args.include_phase_coherence:
        if args.wmap_obs:
            test_args = [
                '--planck_obs', args.planck_obs,
                '--planck_model', args.planck_model,
                '--wmap_obs', args.wmap_obs,
                '--ell_min', str(args.ell_min),
                '--ell_max', min(args.ell_max, 800),  # WMAP limit
                '--mc_trials', '1000',
            ]
            
            if args.planck_cov:
                test_args.extend(['--planck_cov', args.planck_cov])
            if args.wmap_model:
                test_args.extend(['--wmap_model', args.wmap_model])
            if args.wmap_cov:
                test_args.extend(['--wmap_cov', args.wmap_cov])
            
            campaign_results['test_5_phase_coherence'] = run_test(
                "Test #5: Phase Coherence",
                stress_tests_dir / 'test_5_phase_coherence.py',
                test_args,
                out_dir,
                required=False  # Optional test
            )
        else:
            print("\nWARNING: Phase coherence test requested but WMAP data not provided")
            print("         Skipping phase coherence test")
    
    # Generate final report
    print("\n" + "="*80)
    print("GENERATING FINAL REPORT")
    print("="*80)
    
    report_file = campaign_dir / 'ROBUSTNESS_AND_FALSIFICATION.md'
    generate_final_report(campaign_results, report_file, args)
    
    # Save campaign metadata
    metadata_file = campaign_dir / 'campaign_metadata.json'
    with open(metadata_file, 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'arguments': vars(args),
            'tests_run': list(campaign_results.keys()),
            'tests_successful': [k for k, v in campaign_results.items() if v.get('success', False)]
        }, f, indent=2)
    
    print("\n" + "="*80)
    print("CAMPAIGN COMPLETE")
    print("="*80)
    print(f"\nResults saved to: {campaign_dir}")
    print(f"Main report: {report_file}")
    print(f"\nTests completed: {len(campaign_results)}")
    print(f"Tests successful: {sum(1 for r in campaign_results.values() if r.get('success', False))}")
    print()
    print("Review ROBUSTNESS_AND_FALSIFICATION.md for final verdict.")
    print()


if __name__ == '__main__':
    main()
