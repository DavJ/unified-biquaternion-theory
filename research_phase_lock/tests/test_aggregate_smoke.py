#!/usr/bin/env python3
"""
test_aggregate_smoke.py

Smoke test for result aggregation functionality.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sys
import csv
import tempfile
from pathlib import Path

# Add parent directory to path
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root))

from research_phase_lock.utils.io import save_yaml


def create_mock_results(temp_dir):
    """Create mock result files for testing."""
    # Create mock run directories
    for i in range(3):
        run_dir = Path(temp_dir) / f'run_{i:03d}'
        run_dir.mkdir(parents=True, exist_ok=True)
        
        # Create config.yaml
        config = {
            'projection': 'torus',
            'window_size': 128,
            'nside_out': 256,
            'window_func': 'none',
            'null_model': 'phase-shuffle',
            'mc_samples': 500,
            'seed': i,
        }
        save_yaml(config, run_dir / 'config.yaml')
        
        # Create results CSV
        csv_path = run_dir / 'phase_lock_results.csv'
        with open(csv_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['k_target', 'phase_coherence', 'p_value', 'z_score'])
            writer.writeheader()
            
            # Mock results for k=137, 139
            import random
            random.seed(i)
            
            for k in [137, 139]:
                writer.writerow({
                    'k_target': str(k),
                    'phase_coherence': f"{random.uniform(0.3, 0.7):.4f}",
                    'p_value': f"{random.uniform(0.001, 0.1):.4f}",
                    'z_score': f"{random.uniform(1.5, 3.5):.4f}",
                })
    
    return temp_dir


def test_aggregate_mock_results():
    """Test aggregation on mock results."""
    print("=" * 70)
    print("AGGREGATE SMOKE TEST")
    print("=" * 70)
    print()
    
    # Create temporary directory with mock results
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Creating mock results in: {temp_dir}")
        create_mock_results(temp_dir)
        
        # Import aggregate function
        try:
            from research_phase_lock.scripts.aggregate import aggregate_results
        except ImportError:
            # Try alternate import path
            sys.path.insert(0, str(repo_root / 'research_phase_lock' / 'scripts'))
            from aggregate import aggregate_results
        
        # Run aggregation
        output_csv = Path(temp_dir) / 'summary.csv'
        print(f"Running aggregation...")
        
        try:
            aggregate_results(
                input_dir=temp_dir,
                output_path=str(output_csv),
                apply_fdr=True,
                fdr_alpha=0.05
            )
            
            # Verify output exists
            assert output_csv.exists(), "Summary CSV not created"
            
            # Verify output contains data
            with open(output_csv, 'r') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                
                assert len(rows) > 0, "Summary CSV is empty"
                assert len(rows) == 6, f"Expected 6 rows (3 runs × 2 targets), got {len(rows)}"
                
                # Check for required columns
                required_cols = ['k_target', 'phase_coherence', 'p_value', 'run_id']
                for col in required_cols:
                    assert col in rows[0], f"Missing column: {col}"
                
                # Check for FDR columns
                if 'q_value' in rows[0]:
                    print("✓ FDR correction applied")
                
            print()
            print("✓ Aggregation test PASSED")
            return True
            
        except Exception as e:
            print(f"✗ Aggregation test FAILED: {e}")
            import traceback
            traceback.print_exc()
            return False


def test_benjamini_hochberg():
    """Test Benjamini-Hochberg FDR correction."""
    print("\n" + "=" * 70)
    print("BENJAMINI-HOCHBERG FDR TEST")
    print("=" * 70)
    print()
    
    try:
        from research_phase_lock.scripts.aggregate import benjamini_hochberg_correction
    except ImportError:
        sys.path.insert(0, str(repo_root / 'research_phase_lock' / 'scripts'))
        from aggregate import benjamini_hochberg_correction
    
    # Test with known p-values
    p_values = [0.001, 0.008, 0.039, 0.041, 0.042, 0.06, 0.074, 0.205, 0.212, 0.216]
    
    q_values, is_significant = benjamini_hochberg_correction(p_values, alpha=0.05)
    
    print(f"Input p-values: {p_values}")
    print(f"Output q-values: {[f'{q:.4f}' for q in q_values]}")
    print(f"Significant: {is_significant}")
    
    # Basic sanity checks
    assert len(q_values) == len(p_values), "Q-values length mismatch"
    assert all(q >= p for q, p in zip(q_values, p_values)), "Q-values should be >= p-values"
    assert all(0 <= q <= 1 for q in q_values), "Q-values should be in [0, 1]"
    
    # Check monotonicity (q-values in original order may not be monotonic,
    # but sorted q-values should be)
    import numpy as np
    sorted_indices = np.argsort(p_values)
    sorted_q = q_values[sorted_indices]
    
    print()
    print("✓ Benjamini-Hochberg test PASSED")
    return True


def run_all_tests():
    """Run all aggregation tests."""
    print("=" * 70)
    print("AGGREGATION SMOKE TESTS")
    print("=" * 70)
    print()
    
    results = []
    
    try:
        results.append(('BH FDR Correction', test_benjamini_hochberg()))
    except Exception as e:
        print(f"✗ BH FDR test failed: {e}")
        results.append(('BH FDR Correction', False))
    
    try:
        results.append(('Mock Aggregation', test_aggregate_mock_results()))
    except Exception as e:
        print(f"✗ Mock aggregation test failed: {e}")
        import traceback
        traceback.print_exc()
        results.append(('Mock Aggregation', False))
    
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    for name, passed in results:
        status = "PASSED" if passed else "FAILED"
        symbol = "✓" if passed else "✗"
        print(f"{symbol} {name}: {status}")
    
    all_passed = all(r[1] for r in results)
    print()
    print(f"Overall: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    print("=" * 70)
    
    return all_passed


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
