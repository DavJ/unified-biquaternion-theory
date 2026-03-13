#!/usr/bin/env python3
"""
Test script for cross_channel_phase_coherence.py

Tests the core phase coherence computation without requiring full CMB maps.
"""

import numpy as np
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from forensic_fingerprint.tools.cross_channel_phase_coherence import (
    compute_phase_coherence,
)


def test_phase_coherence_perfect_lock():
    """Test phase coherence with perfect phase lock."""
    print("[test] Testing perfect phase lock...")
    
    # Create phases with perfect lock (all same phase)
    phases_a = np.array([0.5, 0.5, 0.5, 0.5])
    phases_b = np.array([0.5, 0.5, 0.5, 0.5])
    
    coherence, mean_diff, concentration = compute_phase_coherence(phases_a, phases_b)
    
    print(f"  Coherence: {coherence:.6f}")
    print(f"  Mean phase diff: {mean_diff:.6f}")
    print(f"  Concentration: {concentration:.6f}")
    
    assert coherence > 0.99, "Perfect lock should give coherence ≈ 1"
    assert abs(mean_diff) < 0.01, "Perfect lock should give mean diff ≈ 0"
    
    print("  ✓ Perfect phase lock detected correctly")
    print("[test] Perfect lock test PASSED\n")


def test_phase_coherence_random():
    """Test phase coherence with random phases."""
    print("[test] Testing random phases...")
    
    rng = np.random.default_rng(42)
    
    # Create random phases
    phases_a = rng.uniform(-np.pi, np.pi, 100)
    phases_b = rng.uniform(-np.pi, np.pi, 100)
    
    coherence, mean_diff, concentration = compute_phase_coherence(phases_a, phases_b)
    
    print(f"  Coherence: {coherence:.6f}")
    print(f"  Mean phase diff: {mean_diff:.6f}")
    print(f"  Concentration: {concentration:.6f}")
    
    assert coherence < 0.3, f"Random phases should give low coherence, got {coherence:.4f}"
    
    print("  ✓ Random phases give low coherence")
    print("[test] Random phases test PASSED\n")


def test_phase_coherence_partial_lock():
    """Test phase coherence with partial phase lock."""
    print("[test] Testing partial phase lock...")
    
    rng = np.random.default_rng(123)
    
    # Create phases with a bias (partial lock)
    base_phase = 1.0
    phases_a = base_phase + rng.normal(0, 0.3, 50)
    phases_b = base_phase + rng.normal(0, 0.3, 50)
    
    coherence, mean_diff, concentration = compute_phase_coherence(phases_a, phases_b)
    
    print(f"  Coherence: {coherence:.6f}")
    print(f"  Mean phase diff: {mean_diff:.6f}")
    print(f"  Concentration: {concentration:.6f}")
    
    assert 0.3 < coherence < 0.99, f"Partial lock should give intermediate coherence, got {coherence:.4f}"
    assert abs(mean_diff) < 0.5, "Partial lock should have small mean difference"
    
    print("  ✓ Partial phase lock detected")
    print("[test] Partial lock test PASSED\n")


def test_phase_coherence_constant_offset():
    """Test phase coherence with constant offset."""
    print("[test] Testing constant phase offset...")
    
    # Create phases with constant offset
    # Use same phases repeated to ensure pairwise differences are all equal
    offset = np.pi / 3
    n = 5
    phases_a = np.full(n, 1.0)  # All same phase
    phases_b = np.full(n, 1.0 + offset)  # All same phase + offset
    
    coherence, mean_diff, concentration = compute_phase_coherence(phases_a, phases_b)
    
    print(f"  Coherence: {coherence:.6f}")
    print(f"  Mean phase diff: {mean_diff:.6f} (expected: {-offset:.6f})")
    print(f"  Concentration: {concentration:.6f}")
    
    assert coherence > 0.99, f"Constant offset should give high coherence, got {coherence:.4f}"
    assert abs(mean_diff - (-offset)) < 0.01, f"Mean diff should be -{offset:.4f}"
    
    print("  ✓ Constant offset detected correctly")
    print("[test] Constant offset test PASSED\n")


def test_phase_coherence_monte_carlo():
    """Test that Monte Carlo permutation gives lower coherence."""
    print("[test] Testing Monte Carlo permutation effect...")
    
    rng = np.random.default_rng(456)
    
    # Create correlated phases
    base = rng.uniform(-np.pi, np.pi, 30)
    phases_a = base + rng.normal(0, 0.1, 30)
    phases_b = base + rng.normal(0, 0.1, 30)
    
    coherence_obs, _, _ = compute_phase_coherence(phases_a, phases_b)
    
    # Permute and recompute (should destroy correlation)
    phases_b_perm = rng.permutation(phases_b)
    coherence_null, _, _ = compute_phase_coherence(phases_a, phases_b_perm)
    
    print(f"  Observed coherence: {coherence_obs:.6f}")
    print(f"  Null coherence: {coherence_null:.6f}")
    
    assert coherence_obs > coherence_null, "Permutation should reduce coherence"
    
    print("  ✓ Monte Carlo permutation reduces coherence")
    print("[test] Monte Carlo test PASSED\n")


def main():
    """Run all tests."""
    print("=" * 70)
    print("Testing cross_channel_phase_coherence.py")
    print("=" * 70 + "\n")
    
    try:
        test_phase_coherence_perfect_lock()
        test_phase_coherence_random()
        test_phase_coherence_partial_lock()
        test_phase_coherence_constant_offset()
        test_phase_coherence_monte_carlo()
        
        print("=" * 70)
        print("ALL TESTS PASSED ✓")
        print("=" * 70)
        return 0
        
    except AssertionError as e:
        print(f"\n[ERROR] Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
