#!/usr/bin/env python3
"""
Test Report Generation for Robustness Campaign

This script generates a sample ROBUSTNESS_AND_FALSIFICATION.md report
using mock test results to verify the report generation logic works correctly.
"""

import json
import sys
from pathlib import Path
from datetime import datetime

# Find repository root
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root / 'forensic_fingerprint'))

# Import the report generation function
from run_robustness_campaign import generate_final_report


def create_mock_results(scenario='pass'):
    """
    Create mock test results for different scenarios.
    
    Parameters
    ----------
    scenario : str
        'pass' - Signal survives all tests
        'fail_whitening' - Signal eliminated by whitening
        'fail_lcdm' - Signal appears frequently in ΛCDM
        'fail_ablation' - Signal localized to one range
    
    Returns
    -------
    dict
        Mock campaign results
    """
    if scenario == 'pass':
        # Signal survives scenario
        return {
            'test_1_whitening': {
                'test_name': 'Test #1: Whitening / Full Covariance',
                'success': True,
                'summary': 'Δℓ=255 persists across modes',
                'verdict': 'PASS',
                'output_dir': '/tmp/mock_whitening',
                'stdout': 'Mock whitening test completed'
            },
            'test_4_lcdm_null': {
                'test_name': 'Test #2: Synthetic ΛCDM Null Controls',
                'success': True,
                'summary': 'Δℓ=255 rare in ΛCDM (0.5%)',
                'verdict': 'PASS',
                'output_dir': '/tmp/mock_lcdm',
                'stdout': 'Mock ΛCDM null test completed'
            },
            'test_3_ablation': {
                'test_name': 'Test #3: ℓ-Range Ablation',
                'success': True,
                'summary': 'Δℓ=255 in 3/5 ranges',
                'verdict': 'PASS',
                'output_dir': '/tmp/mock_ablation',
                'stdout': 'Mock ablation test completed'
            }
        }
    elif scenario == 'fail_whitening':
        # Signal eliminated by whitening
        return {
            'test_1_whitening': {
                'test_name': 'Test #1: Whitening / Full Covariance',
                'success': True,
                'summary': 'Signal disappears after whitening',
                'verdict': 'FAIL',
                'output_dir': '/tmp/mock_whitening',
                'stdout': 'Mock whitening test completed'
            },
            'test_4_lcdm_null': {
                'test_name': 'Test #2: Synthetic ΛCDM Null Controls',
                'success': True,
                'summary': 'Not applicable (signal failed whitening)',
                'verdict': 'SKIP',
                'output_dir': '/tmp/mock_lcdm',
                'stdout': 'Mock ΛCDM null test completed'
            },
            'test_3_ablation': {
                'test_name': 'Test #3: ℓ-Range Ablation',
                'success': True,
                'summary': 'Not applicable (signal failed whitening)',
                'verdict': 'SKIP',
                'output_dir': '/tmp/mock_ablation',
                'stdout': 'Mock ablation test completed'
            }
        }
    elif scenario == 'fail_lcdm':
        # Signal appears frequently in ΛCDM
        return {
            'test_1_whitening': {
                'test_name': 'Test #1: Whitening / Full Covariance',
                'success': True,
                'summary': 'Δℓ=255 persists across modes',
                'verdict': 'PASS',
                'output_dir': '/tmp/mock_whitening',
                'stdout': 'Mock whitening test completed'
            },
            'test_4_lcdm_null': {
                'test_name': 'Test #2: Synthetic ΛCDM Null Controls',
                'success': True,
                'summary': 'Δℓ=255 common in ΛCDM (12%)',
                'verdict': 'FAIL',
                'output_dir': '/tmp/mock_lcdm',
                'stdout': 'Mock ΛCDM null test completed'
            },
            'test_3_ablation': {
                'test_name': 'Test #3: ℓ-Range Ablation',
                'success': True,
                'summary': 'Δℓ=255 in 3/5 ranges',
                'verdict': 'PASS',
                'output_dir': '/tmp/mock_ablation',
                'stdout': 'Mock ablation test completed'
            }
        }
    else:  # fail_ablation
        # Signal localized to one range
        return {
            'test_1_whitening': {
                'test_name': 'Test #1: Whitening / Full Covariance',
                'success': True,
                'summary': 'Δℓ=255 persists across modes',
                'verdict': 'PASS',
                'output_dir': '/tmp/mock_whitening',
                'stdout': 'Mock whitening test completed'
            },
            'test_4_lcdm_null': {
                'test_name': 'Test #2: Synthetic ΛCDM Null Controls',
                'success': True,
                'summary': 'Δℓ=255 rare in ΛCDM (0.5%)',
                'verdict': 'PASS',
                'output_dir': '/tmp/mock_lcdm',
                'stdout': 'Mock ΛCDM null test completed'
            },
            'test_3_ablation': {
                'test_name': 'Test #3: ℓ-Range Ablation',
                'success': True,
                'summary': 'Δℓ=255 only in low-ℓ range',
                'verdict': 'FAIL',
                'output_dir': '/tmp/mock_ablation',
                'stdout': 'Mock ablation test completed'
            }
        }


def create_mock_json_results(output_dir, scenario='pass'):
    """Create mock JSON result files for detailed reporting."""
    output_dir = Path(output_dir)
    
    # Mock whitening results
    whitening_dir = output_dir / 'whitening'
    whitening_dir.mkdir(parents=True, exist_ok=True)
    
    if scenario == 'pass':
        whitening_results = {
            'none': {'best_period': 255, 'p_value': 1.5e-4, 'amplitude': 0.045, 'significance': 'candidate'},
            'diagonal': {'best_period': 255, 'p_value': 2.1e-4, 'amplitude': 0.042, 'significance': 'candidate'},
            'block-diagonal': {'best_period': 255, 'p_value': 3.5e-4, 'amplitude': 0.038, 'significance': 'candidate'},
            'covariance': {'best_period': 255, 'p_value': 4.2e-4, 'amplitude': 0.035, 'significance': 'candidate'}
        }
    else:
        whitening_results = {
            'none': {'best_period': 255, 'p_value': 1.5e-4, 'amplitude': 0.045, 'significance': 'candidate'},
            'diagonal': {'best_period': 255, 'p_value': 2.1e-4, 'amplitude': 0.042, 'significance': 'candidate'},
            'block-diagonal': {'best_period': 64, 'p_value': 0.15, 'amplitude': 0.012, 'significance': 'null'},
            'covariance': {'best_period': 128, 'p_value': 0.23, 'amplitude': 0.008, 'significance': 'null'}
        }
    
    with open(whitening_dir / 'planck_whitened_results.json', 'w') as f:
        json.dump(whitening_results, f, indent=2)
    
    # Mock ΛCDM null results
    lcdm_dir = output_dir / 'lcdm_null'
    lcdm_dir.mkdir(parents=True, exist_ok=True)
    
    if scenario == 'fail_lcdm':
        best_periods = [255] * 24 + [64, 128, 255, 32, 255, 8, 255, 16] + [128] * 60 + [64] * 8
    else:
        best_periods = [128] * 45 + [64] * 35 + [255] * 1 + [32] * 12 + [16] * 7
    
    lcdm_results = {
        'best_periods': best_periods,
        'n_realizations': len(best_periods)
    }
    
    with open(lcdm_dir / 'lcdm_null_distribution.json', 'w') as f:
        json.dump(lcdm_results, f, indent=2)
    
    # Mock ablation results
    ablation_dir = output_dir / 'ablation'
    ablation_dir.mkdir(parents=True, exist_ok=True)
    
    if scenario == 'fail_ablation':
        ablation_results = {
            'ell_30_800': {'best_period': 255, 'p_value': 1.2e-3, 'significance': 'candidate'},
            'ell_800_1500': {'best_period': 64, 'p_value': 0.18, 'significance': 'null'},
            'ell_30_500': {'best_period': 128, 'p_value': 0.12, 'significance': 'null'},
            'ell_500_1000': {'best_period': 32, 'p_value': 0.25, 'significance': 'null'},
            'ell_1000_1500': {'best_period': 16, 'p_value': 0.35, 'significance': 'null'}
        }
    else:
        ablation_results = {
            'ell_30_800': {'best_period': 255, 'p_value': 1.2e-3, 'significance': 'candidate'},
            'ell_800_1500': {'best_period': 255, 'p_value': 3.5e-3, 'significance': 'candidate'},
            'ell_30_500': {'best_period': 255, 'p_value': 2.8e-3, 'significance': 'candidate'},
            'ell_500_1000': {'best_period': 128, 'p_value': 0.08, 'significance': 'null'},
            'ell_1000_1500': {'best_period': 64, 'p_value': 0.15, 'significance': 'null'}
        }
    
    with open(ablation_dir / 'ablation_results.json', 'w') as f:
        json.dump(ablation_results, f, indent=2)


def test_report_generation():
    """Test report generation with different scenarios."""
    
    output_dir = repo_root / 'forensic_fingerprint' / 'out' / 'test_reports'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    scenarios = ['pass', 'fail_whitening', 'fail_lcdm', 'fail_ablation']
    
    print("="*80)
    print("TESTING REPORT GENERATION")
    print("="*80)
    print()
    
    class MockArgs:
        pass
    
    args = MockArgs()
    
    for scenario in scenarios:
        print(f"\nScenario: {scenario.upper()}")
        print("-" * 40)
        
        # Create mock results
        campaign_results = create_mock_results(scenario)
        
        # Create output directory for this scenario
        scenario_dir = output_dir / scenario
        scenario_dir.mkdir(exist_ok=True)
        
        # Create mock JSON files
        create_mock_json_results(scenario_dir, scenario)
        
        # Update output dirs in results
        for key in campaign_results:
            if campaign_results[key].get('output_dir'):
                test_type = key.split('_')[-1] if '_' in key else key
                if test_type == '1' or test_type == 'whitening':
                    campaign_results[key]['output_dir'] = str(scenario_dir / 'whitening')
                elif test_type == '4' or test_type == 'lcdm':
                    campaign_results[key]['output_dir'] = str(scenario_dir / 'lcdm_null')
                elif test_type == '3' or test_type == 'ablation':
                    campaign_results[key]['output_dir'] = str(scenario_dir / 'ablation')
        
        # Generate report
        report_file = scenario_dir / 'ROBUSTNESS_AND_FALSIFICATION.md'
        generate_final_report(campaign_results, report_file, args)
        
        print(f"✓ Report generated: {report_file}")
        
        # Read first few lines to verify
        with open(report_file, 'r') as f:
            lines = f.readlines()[:20]
            print("\nFirst few lines:")
            for line in lines:
                print(f"  {line.rstrip()}")
    
    print("\n" + "="*80)
    print("TESTING COMPLETE")
    print("="*80)
    print(f"\nAll reports saved to: {output_dir}")
    print("\nReview the generated reports to verify:")
    print("  - Pass scenario has ✓ SIGNAL SURVIVED verdict")
    print("  - Fail scenarios have ✗ SIGNAL FAILED verdicts")
    print("  - Tables are properly formatted")
    print("  - JSON results are correctly parsed")
    print()


if __name__ == '__main__':
    test_report_generation()
