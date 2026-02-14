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
    
    def test_synthetic_exact_fft_bin(self):
        """
        Test with exact FFT bin injection for reliable synthetic signal.
        
        Creates synthetic data by directly placing a coherent signal in specific
        FFT bins, ensuring the test is deterministic and maps correctly to k values.
        """
        # Parameters
        window_size = 64
        n_segments = 10
        k_target = 10  # Target frequency bin (must be < window_size/2)
        
        # Create segments with exact frequency injection
        fft_segments_tt = []
        fft_segments_bb = []
        phase_offset = 0.1  # Small constant phase offset between channels
        
        rng = np.random.default_rng(789)
        
        for i in range(n_segments):
            # Create FFT array (in frequency domain)
            F_tt = np.zeros((window_size, window_size), dtype=complex)
            F_bb = np.zeros((window_size, window_size), dtype=complex)
            
            # Inject signal at exact FFT bin (k_target, 0) and (0, k_target)
            # These correspond to horizontal and vertical modes at k=k_target
            amplitude = 100.0
            
            # Horizontal mode: F[0, k_target]
            F_tt[0, k_target] = amplitude * np.exp(1j * 0)  # TT: phase = 0
            F_bb[0, k_target] = amplitude * np.exp(1j * phase_offset)  # BB: phase = phase_offset
            
            # Vertical mode: F[k_target, 0]
            F_tt[k_target, 0] = amplitude * np.exp(1j * 0)
            F_bb[k_target, 0] = amplitude * np.exp(1j * phase_offset)
            
            # Add small random noise in frequency domain
            noise_level = 1.0
            F_tt += noise_level * (rng.standard_normal((window_size, window_size)) + 
                                   1j * rng.standard_normal((window_size, window_size)))
            F_bb += noise_level * (rng.standard_normal((window_size, window_size)) + 
                                   1j * rng.standard_normal((window_size, window_size)))
            
            fft_segments_tt.append(F_tt)
            fft_segments_bb.append(F_bb)
        
        # Compute phase coherence
        coherence, targets = compute_phase_lock(
            fft_segments_tt,
            fft_segments_bb,
            targets=[k_target]
        )
        
        # With exact FFT bin injection and constant phase offset,
        # we should get very high coherence at k_target
        print(f"Exact FFT bin test: PC at k={k_target} is {targets[k_target]:.6f}")
        assert targets[k_target] > 0.95, \
            f"Expected high PC (>0.95) with exact bin injection, got {targets[k_target]:.6f}"
    
    def test_synthetic_phase_locked_cmb(self):
        """
        Test with synthetic CMB-like spatial data where TT and BB are phase-locked.
        
        This generates spatial waves and checks that the phase coherence is detected,
        though the mapping to k is approximate due to windowing.
        """
        # Create synthetic images with embedded phase-locked frequency
        nlat, nlon = 256, 512
        
        # Build coordinate grids
        y = np.arange(nlat)
        x = np.arange(nlon)
        Y, X = np.meshgrid(y, x, indexing='ij')
        
        # Inject wave with integer number of periods that fits window_size
        window_size = 64
        n_periods = 8  # 8 complete periods in window
        wavelength = window_size / n_periods
        k_spatial = 2 * np.pi / wavelength  # Spatial frequency
        
        # TT channel: cos wave
        img_tt = np.cos(k_spatial * X)
        
        # BB channel: cos wave with small constant phase offset
        phase_offset = 0.1
        img_bb = np.cos(k_spatial * X + phase_offset)
        
        # Add noise
        rng = np.random.default_rng(456)
        noise_level = 0.1
        img_tt += noise_level * rng.standard_normal((nlat, nlon))
        img_bb += noise_level * rng.standard_normal((nlat, nlon))
        
        # Segment and compute FFTs
        stride = window_size // 2  # 50% overlap
        
        fft_tt = segment_and_fft(img_tt, window_size, stride, "none")
        fft_bb = segment_and_fft(img_bb, window_size, stride, "none")
        
        # The k value in FFT corresponds to n_periods
        k_fft = n_periods
        
        coherence, targets = compute_phase_lock(fft_tt, fft_bb, targets=[k_fft])
        
        # Should have elevated coherence at the embedded frequency
        print(f"Spatial wave test: PC at k={k_fft} is {targets[k_fft]:.4f}")
        assert targets[k_fft] > 0.5, \
            f"Expected elevated PC (>0.5) for phase-locked spatial wave, got {targets[k_fft]:.4f}"


class TestMaxstatPvalue:
    """Test maxstat p-value computation."""
    
    def test_maxstat_identical_channels(self):
        """
        When TT=BB (identical), maxstat p-value should be extremely small.
        
        With identical channels, observed PC should be 1.0 at all k,
        while null samples will have lower max PC, giving p-value ~ 0.
        """
        # Import the maxstat function
        from unified_phase_lock_scan import compute_maxstat_pvalues
        
        # Create observed coherence (perfect lock everywhere)
        n_k = 50
        obs_coherence = np.ones(n_k)  # PC = 1.0 at all k
        
        # Create MC null samples (random, much lower coherence)
        rng = np.random.default_rng(999)
        n_mc = 100
        mc_samples = []
        for i in range(n_mc):
            # Random coherence typically ~0.1-0.3
            mc_spec = rng.uniform(0.0, 0.4, size=n_k)
            mc_samples.append(mc_spec)
        
        # Compute maxstat p-values for middle range
        k_range = (10, 40)
        targets = [15, 20, 25]
        
        p_values = compute_maxstat_pvalues(obs_coherence, mc_samples, k_range, targets)
        
        # With perfect observed coherence and random null,
        # p-values should be very small (none of the MC max values exceed 1.0)
        print(f"Maxstat test (identical): p-values = {p_values}")
        for k in targets:
            assert p_values[k] < 0.01, \
                f"Expected p-value << 1 for perfect coherence, got {p_values[k]:.4f} at k={k}"
    
    def test_maxstat_independent_channels(self):
        """
        When channels are independent random, maxstat p-value should be ~ uniform.
        
        Both observed and null samples are random, so observed PC should not
        systematically exceed null max PC.
        """
        from unified_phase_lock_scan import compute_maxstat_pvalues
        
        # Create observed and null samples all from same random distribution
        rng = np.random.default_rng(888)
        n_k = 50
        n_mc = 100
        
        # Observed: random coherence
        obs_coherence = rng.uniform(0.0, 0.4, size=n_k)
        
        # MC samples: also random
        mc_samples = []
        for i in range(n_mc):
            mc_spec = rng.uniform(0.0, 0.4, size=n_k)
            mc_samples.append(mc_spec)
        
        # Compute maxstat p-values
        k_range = (10, 40)
        targets = [15, 20, 25, 30, 35]
        
        p_values = compute_maxstat_pvalues(obs_coherence, mc_samples, k_range, targets)
        
        # P-values should be distributed roughly uniformly in [0, 1]
        # Not all should be near 0 or near 1
        print(f"Maxstat test (independent): p-values = {p_values}")
        p_vals_list = [p_values[k] for k in targets]
        
        # Check that we get a range of p-values (not all extreme)
        assert min(p_vals_list) < 0.5, "Should have some p-values < 0.5"
        assert max(p_vals_list) > 0.1, "Should have some p-values > 0.1"
        
        # Mean p-value should be around 0.5 for uniform distribution
        mean_p = np.mean(p_vals_list)
        assert 0.2 < mean_p < 0.8, \
            f"Mean p-value should be ~0.5 for independent samples, got {mean_p:.2f}"


def run_tests():
    """Run all tests."""
    print("Running Unified Phase-Lock Scan tests...\n")
    
    # Run pytest
    exit_code = pytest.main([__file__, "-v", "-s"])
    
    return exit_code


if __name__ == '__main__':
    sys.exit(run_tests())
