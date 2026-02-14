#!/usr/bin/env python3
"""
Simple test for unified_phase_lock_scan.py without pytest.
"""

import numpy as np
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from forensic_fingerprint.tools.unified_phase_lock_scan import (
    compute_phase_lock,
    segment_and_fft,
    _window_2d,
)


def test_perfect_phase_lock():
    """Test that identical signals give PC ≈ 1.0."""
    print("Test 1: Perfect phase lock...")
    
    n_segments = 5
    h, w = 64, 64
    
    # Create identical complex patterns with some structure
    # Use a simple pattern with energy distributed across multiple k values
    fft_segments_tt = []
    fft_segments_bb = []
    
    for i in range(n_segments):
        # Create the same random complex field for all segments
        # This ensures perfect phase lock
        # Reinitialize with same seed to get identical patterns
        rng = np.random.default_rng(42)
        F = rng.standard_normal((h, w)) + 1j * rng.standard_normal((h, w))
        
        fft_segments_tt.append(F)
        fft_segments_bb.append(F.copy())  # Identical copy
    
    coherence, targets = compute_phase_lock(
        fft_segments_tt, 
        fft_segments_bb, 
        targets=[10, 20]
    )
    
    # Check multiple k values
    all_high = all(targets[k] > 0.95 for k in [10, 20])
    
    for k in [10, 20]:
        pc = targets[k]
        print(f"  PC at k={k}: {pc:.6f}")
    
    if all_high:
        print("  ✓ PASS: Perfect coherence achieved")
        return True
    else:
        print(f"  ✗ FAIL: Expected PC≈1.0 for all k")
        return False


def test_random_phase():
    """Test that random phases give low PC."""
    print("\nTest 2: Random phases...")
    
    n_segments = 10
    h, w = 64, 64
    rng = np.random.default_rng(42)
    
    fft_segments_tt = []
    fft_segments_bb = []
    
    for i in range(n_segments):
        F_tt = rng.standard_normal((h, w)) + 1j * rng.standard_normal((h, w))
        F_bb = rng.standard_normal((h, w)) + 1j * rng.standard_normal((h, w))
        fft_segments_tt.append(F_tt)
        fft_segments_bb.append(F_bb)
    
    coherence, targets = compute_phase_lock(
        fft_segments_tt,
        fft_segments_bb,
        targets=[10, 20]
    )
    
    all_pass = True
    for k in [10, 20]:
        pc = targets[k]
        print(f"  PC at k={k}: {pc:.6f}")
        if pc < 0.5:
            print(f"    ✓ Low PC as expected for random phases")
        else:
            print(f"    ✗ FAIL: Expected low PC, got {pc}")
            all_pass = False
    
    if all_pass:
        print("  ✓ PASS: Random phases produce low coherence")
    return all_pass


def test_segmentation():
    """Test segmentation produces correct number of FFTs."""
    print("\nTest 3: Segmentation...")
    
    img = np.random.randn(256, 512)
    window_size = 64
    stride = 32
    
    segments = segment_and_fft(img, window_size, stride, "none")
    
    n_lat = (256 - 64) // 32 + 1  # = 7
    n_lon = (512 - 64) // 32 + 1  # = 15
    expected = n_lat * n_lon  # = 105
    
    print(f"  Expected segments: {expected}")
    print(f"  Actual segments:   {len(segments)}")
    
    if len(segments) == expected:
        print("  ✓ PASS: Correct number of segments")
        return True
    else:
        print(f"  ✗ FAIL: Expected {expected}, got {len(segments)}")
        return False


def test_window_functions():
    """Test window functions."""
    print("\nTest 4: Window functions...")
    
    # Test "none" window
    w_none = _window_2d("none", 32, 32, normalize_rms=False)
    if np.allclose(w_none, 1.0):
        print("  ✓ 'none' window is all ones")
        pass1 = True
    else:
        print("  ✗ 'none' window should be all ones")
        pass1 = False
    
    # Test Hann window
    w_hann = _window_2d("hann", 32, 32, normalize_rms=False)
    if w_hann[0, 0] < w_hann[16, 16] and w_hann[16, 16] > 0.9:
        print("  ✓ Hann window has correct shape")
        pass2 = True
    else:
        print("  ✗ Hann window shape incorrect")
        pass2 = False
    
    # Test normalization
    w_norm = _window_2d("hann", 32, 32, normalize_rms=True)
    rms = np.sqrt(np.mean(w_norm**2))
    if abs(rms - 1.0) < 0.01:
        print(f"  ✓ RMS normalization works (RMS={rms:.4f})")
        pass3 = True
    else:
        print(f"  ✗ RMS normalization failed (RMS={rms:.4f}, expected 1.0)")
        pass3 = False
    
    if pass1 and pass2 and pass3:
        print("  ✓ PASS: All window functions correct")
        return True
    return False


def test_coherence_range():
    """Test that coherence is in [0, 1]."""
    print("\nTest 5: Coherence range validation...")
    
    n_segments = 10
    h, w = 64, 64
    rng = np.random.default_rng(123)
    
    fft_segments_tt = []
    fft_segments_bb = []
    
    for i in range(n_segments):
        F_tt = rng.standard_normal((h, w)) + 1j * rng.standard_normal((h, w))
        F_bb = rng.standard_normal((h, w)) + 1j * rng.standard_normal((h, w))
        fft_segments_tt.append(F_tt)
        fft_segments_bb.append(F_bb)
    
    coherence, _ = compute_phase_lock(fft_segments_tt, fft_segments_bb, targets=[])
    
    min_pc = np.min(coherence)
    max_pc = np.max(coherence)
    
    print(f"  PC range: [{min_pc:.6f}, {max_pc:.6f}]")
    
    if np.all(coherence >= 0.0) and np.all(coherence <= 1.0):
        print("  ✓ PASS: All PC values in valid range [0, 1]")
        return True
    else:
        print("  ✗ FAIL: PC values outside valid range")
        return False


def main():
    """Run all tests."""
    print("=" * 70)
    print("UNIFIED PHASE-LOCK SCAN - BASIC TESTS")
    print("=" * 70)
    
    tests = [
        test_perfect_phase_lock,
        test_random_phase,
        test_segmentation,
        test_window_functions,
        test_coherence_range,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"\n  ✗ ERROR: {e}")
            import traceback
            traceback.print_exc()
            results.append(False)
    
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    
    if all(results):
        print("✓ ALL TESTS PASSED")
        return 0
    else:
        print("✗ SOME TESTS FAILED")
        return 1


if __name__ == '__main__':
    sys.exit(main())
