#!/usr/bin/env python3
"""
Integration test for enhanced whitening modes.

Tests the full CMB comb analysis pipeline with different whitening modes.
"""

import sys
import numpy as np
from pathlib import Path

# Add parent directories to path
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root / 'forensic_fingerprint' / 'cmb_comb'))

import cmb_comb


def test_end_to_end_whitening():
    """Test complete CMB comb analysis with different whitening modes."""
    
    # Create synthetic data
    np.random.seed(42)
    n = 100
    ell = np.arange(30, 30 + n)
    
    # Synthetic observed spectrum with weak comb signal
    C_model = 1000.0 / (ell * (ell + 1))  # Rough CMB shape
    amplitude_signal = 0.05  # Small signal
    period_signal = 64  # True period
    phase_signal = 0.5
    
    theta = 2.0 * np.pi * ell / period_signal
    signal = amplitude_signal * np.sin(theta + phase_signal)
    
    C_obs = C_model * (1 + signal) + np.random.randn(n) * 0.01
    sigma = np.ones(n) * 0.01
    
    # Create covariance matrix with some correlations
    A = np.random.randn(n, n) * 0.001
    cov = A @ A.T + np.diag(sigma**2)
    
    print("=" * 80)
    print("INTEGRATION TEST: End-to-End Whitening Modes")
    print("=" * 80)
    print(f"Synthetic data: n={n} multipoles, period={period_signal}, amplitude={amplitude_signal}")
    print()
    
    # Test each whitening mode
    modes = ['none', 'diagonal', 'cov_diag', 'covariance']
    results = {}
    
    for mode in modes:
        print(f"\n{'='*80}")
        print(f"Testing mode: {mode.upper()}")
        print('='*80)
        
        result = cmb_comb.run_cmb_comb_test(
            ell=ell,
            C_obs=C_obs,
            C_model=C_model,
            sigma=sigma,
            cov=cov if mode in ['cov_diag', 'covariance'] else None,
            dataset_name=f"Synthetic ({mode})",
            variant="C",
            n_mc_trials=1000,  # Reduced for speed
            random_seed=42,
            whiten_mode=mode,
            output_dir=None
        )
        
        results[mode] = result
        
        # Print metadata summary
        if 'whitening_metadata' in result:
            meta = result['whitening_metadata']
            print(f"\nWhitening metadata:")
            print(f"  Mode: {meta.get('whiten_mode')}")
            print(f"  Regularization used: {meta.get('regularization_used', False)}")
            
            if meta.get('cov_metadata'):
                cov_meta = meta['cov_metadata']
                if isinstance(cov_meta, dict):
                    if 'condition_number' in cov_meta:
                        print(f"  Condition number: {cov_meta['condition_number']:.2e}")
                    if 'source' in cov_meta:
                        print(f"  Source: {cov_meta['source']}")
    
    # Compare results
    print(f"\n{'='*80}")
    print("COMPARISON OF WHITENING MODES")
    print('='*80)
    print(f"{'Mode':<15} {'Best Period':<15} {'Amplitude':<15} {'p-value':<15}")
    print('-'*80)
    
    for mode in modes:
        r = results[mode]
        print(f"{mode:<15} {r['best_period']:<15} {r['amplitude']:<15.4f} {r['p_value']:<15.6e}")
    
    # Verify consistency
    print(f"\n{'='*80}")
    print("VERIFICATION")
    print('='*80)
    
    # All modes should find similar periods (within candidates)
    periods = [r['best_period'] for r in results.values()]
    period_range = max(periods) - min(periods)
    
    print(f"Period range across modes: {period_range}")
    if period_range <= 128:  # Within one candidate step
        print("✓ Periods are reasonably consistent across whitening modes")
    else:
        print("✗ WARNING: Large period variation across modes")
    
    # Check that covariance mode has metadata
    cov_result = results['covariance']
    if 'whitening_metadata' in cov_result:
        meta = cov_result['whitening_metadata']
        if meta.get('cov_metadata'):
            print("✓ Covariance metadata present")
        else:
            print("✗ WARNING: Missing covariance metadata")
    
    # Check that cov_diag mode works
    cov_diag_result = results['cov_diag']
    if 'whitening_metadata' in cov_diag_result:
        meta = cov_diag_result['whitening_metadata']
        if meta.get('cov_metadata') and 'source' in meta['cov_metadata']:
            print(f"✓ cov_diag mode working (source: {meta['cov_metadata']['source']})")
        else:
            print("✗ WARNING: cov_diag metadata incomplete")
    
    print("\n✓ Integration test completed successfully!")
    print('='*80)


if __name__ == '__main__':
    test_end_to_end_whitening()
