#!/usr/bin/env python3
"""
test_unified_phase_lock_scan.py

Unit tests for the Unified Phase-Lock Scan tool.

Tests the core phase coherence calculation logic without requiring
actual Planck CMB data.
"""

import numpy as np
import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from unified_phase_lock_scan import (
    compute_phase_lock,
    segment_and_fft,
    _window_2d,
)


class TestPhaseLockCore:
    """Test core phase-lock computation."""
    
    def test_perfect_phase_lock(self):
        """Test that identical signals give PC = 1.0."""
        # Create synthetic FFT segments with identical phase structure
        n_segments = 5
        h, w = 64, 64
        
        # Create a simple pattern: single frequency component
        fft_segments_tt = []
        fft_segments_bb = []
        
        for i in range(n_segments):
            # Create identical complex patterns
            F = np.zeros((h, w), dtype=complex)
            F[h//2 + 10, w//2 + 10] = 100.0 + 0j  # Single mode at k≈14
            fft_segments_tt.append(F)
            fft_segments_bb.append(F)  # Identical
        
        coherence, targets = compute_phase_lock(
            fft_segments_tt, 
            fft_segments_bb, 
            targets=[14]
        )
        
        # Should have perfect coherence at k≈14
        assert targets[14] > 0.99, f"Expected PC≈1.0, got {targets[14]}"
    
    def test_random_phase_lock(self):
        """Test that random phases give low PC."""
        n_segments = 10
        h, w = 64, 64
        rng = np.random.default_rng(42)
        
        fft_segments_tt = []
        fft_segments_bb = []
        
        for i in range(n_segments):
            # Random phases
            F_tt = rng.standard_normal((h, w)) + 1j * rng.standard_normal((h, w))
            F_bb = rng.standard_normal((h, w)) + 1j * rng.standard_normal((h, w))
            
            fft_segments_tt.append(F_tt)
            fft_segments_bb.append(F_bb)
        
        coherence, targets = compute_phase_lock(
            fft_segments_tt,
            fft_segments_bb,
            targets=[10, 20]
        )
        
        # Random phases should give low coherence
        for k in [10, 20]:
            assert targets[k] < 0.5, f"Expected low PC for random, got {targets[k]} at k={k}"
    
    def test_constant_phase_offset(self):
        """Test that constant phase offset gives high PC."""
        n_segments = 5
        h, w = 64, 64
        
        # Fixed phase offset
        phase_offset = np.pi / 4
        
        fft_segments_tt = []
        fft_segments_bb = []
        
        for i in range(n_segments):
            F = np.zeros((h, w), dtype=complex)
            F[h//2 + 10, w//2 + 10] = 100.0 + 0j
            
            fft_segments_tt.append(F)
            # BB has constant phase offset
            fft_segments_bb.append(F * np.exp(1j * phase_offset))
        
        coherence, targets = compute_phase_lock(
            fft_segments_tt,
            fft_segments_bb,
            targets=[14]
        )
        
        # Constant offset should still give high coherence
        assert targets[14] > 0.99, f"Expected high PC with constant offset, got {targets[14]}"
    
    def test_segment_fft_shape(self):
        """Test that segmentation produces correct number of FFTs."""
        # Create synthetic image
        img = np.random.randn(256, 512)
        
        window_size = 64
        stride = 32
        
        segments = segment_and_fft(img, window_size, stride, "none")
        
        # Calculate expected number of segments
        n_lat = (256 - 64) // 32 + 1  # = 7
        n_lon = (512 - 64) // 32 + 1  # = 15
        expected_segments = n_lat * n_lon  # = 105
        
        assert len(segments) == expected_segments, \
            f"Expected {expected_segments} segments, got {len(segments)}"
        
        # Check shape of each segment
        for seg in segments:
            assert seg.shape == (window_size, window_size), \
                f"Expected shape ({window_size}, {window_size}), got {seg.shape}"
    
    def test_window_functions(self):
        """Test different window functions."""
        # Test "none" window (boxcar)
        w_none = _window_2d("none", 32, 32, normalize_rms=False)
        assert np.allclose(w_none, 1.0), "None window should be all ones"
        
        # Test Hann window
        w_hann = _window_2d("hann", 32, 32, normalize_rms=False)
        assert w_hann[0, 0] < w_hann[16, 16], "Hann window should be lower at edges"
        assert w_hann[16, 16] > 0.9, "Hann window center should be near 1.0"
        
        # Test normalization
        w_norm = _window_2d("hann", 32, 32, normalize_rms=True)
        rms = np.sqrt(np.mean(w_norm**2))
        assert abs(rms - 1.0) < 0.01, f"RMS-normalized window should have RMS≈1, got {rms}"
    
    def test_empty_segments(self):
        """Test error handling for empty segment lists."""
        with pytest.raises(ValueError):
            compute_phase_lock([], [], targets=[137])
    
    def test_coherence_range(self):
        """Test that coherence values are in valid range [0, 1]."""
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
        
        # Check all coherence values are in [0, 1]
        assert np.all(coherence >= 0.0), "Coherence values must be >= 0"
        assert np.all(coherence <= 1.0), "Coherence values must be <= 1"


class TestPhaseLockIntegration:
    """Integration tests with synthetic CMB-like data."""
    
    def test_synthetic_phase_locked_cmb(self):
        """
        Test with synthetic CMB-like data where TT and BB are phase-locked
        at specific k values.
        """
        # Create synthetic images with embedded phase-locked frequency
        nlat, nlon = 256, 512
        
        # Build coordinate grids
        y = np.arange(nlat)
        x = np.arange(nlon)
        Y, X = np.meshgrid(y, x, indexing='ij')
        
        # Add a coherent wave at k≈137 (scale to image dimensions)
        k_target = 137
        k_x = k_target * (2 * np.pi / nlon)
        k_y = 0
        
        # TT channel: cos wave
        img_tt = np.cos(k_x * X + k_y * Y)
        
        # BB channel: cos wave with small phase offset
        img_bb = np.cos(k_x * X + k_y * Y + 0.1)
        
        # Add noise
        rng = np.random.default_rng(456)
        img_tt += 0.1 * rng.standard_normal((nlat, nlon))
        img_bb += 0.1 * rng.standard_normal((nlat, nlon))
        
        # Segment and compute FFTs
        window_size = 64
        stride = 32
        
        fft_tt = segment_and_fft(img_tt, window_size, stride, "none")
        fft_bb = segment_and_fft(img_bb, window_size, stride, "none")
        
        # Compute phase coherence
        # Note: k_target in global coordinates needs to be scaled to segment coordinates
        # For W=64 segments, k in segment ≈ k_global * W / map_width
        k_seg = int(k_target * window_size / nlon)
        if k_seg == 0:
            k_seg = 1  # Avoid DC
        
        coherence, targets = compute_phase_lock(fft_tt, fft_bb, targets=[k_seg])
        
        # Should have elevated coherence at the embedded frequency
        # (not perfect due to windowing and noise, but should be > random baseline)
        print(f"Synthetic test: PC at k_seg={k_seg} is {targets[k_seg]:.4f}")
        assert targets[k_seg] > 0.3, \
            f"Expected elevated PC for phase-locked signal, got {targets[k_seg]}"


def run_tests():
    """Run all tests."""
    print("Running Unified Phase-Lock Scan tests...\n")
    
    # Run pytest
    exit_code = pytest.main([__file__, "-v", "-s"])
    
    return exit_code


if __name__ == '__main__':
    sys.exit(run_tests())
