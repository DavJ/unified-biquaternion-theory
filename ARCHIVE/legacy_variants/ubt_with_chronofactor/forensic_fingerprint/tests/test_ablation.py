#!/usr/bin/env python3
"""
Unit Tests for ablation.py Module
==================================

Tests ablation range definitions and result summarization.

License: MIT
Author: UBT Research Team
"""

import pytest
import numpy as np
from pathlib import Path
import sys

# Add modules to path
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root / 'forensic_fingerprint'))

from ablation import (
    get_ablation_ranges,
    validate_ablation_range,
    create_sliding_windows,
    summarize_ablation_results,
    ABLATION_RANGES_PLANCK,
    ABLATION_RANGES_WMAP
)


class TestAblationRanges:
    """Test ablation range retrieval."""
    
    def test_get_planck_ranges(self):
        """Test getting Planck ablation ranges."""
        ranges = get_ablation_ranges('planck')
        
        assert len(ranges) == 5
        assert ranges == ABLATION_RANGES_PLANCK
        
        # Check structure
        for name, ell_min, ell_max in ranges:
            assert isinstance(name, str)
            assert isinstance(ell_min, int)
            assert isinstance(ell_max, int)
            assert ell_min < ell_max
    
    def test_get_wmap_ranges(self):
        """Test getting WMAP ablation ranges."""
        ranges = get_ablation_ranges('wmap')
        
        assert len(ranges) == 3
        assert ranges == ABLATION_RANGES_WMAP
    
    def test_get_custom_ranges(self):
        """Test using custom ranges."""
        custom = [
            ('test1', 10, 50),
            ('test2', 51, 100)
        ]
        
        ranges = get_ablation_ranges('planck', custom_ranges=custom)
        assert ranges == custom
    
    def test_get_unknown_dataset(self):
        """Test error for unknown dataset."""
        with pytest.raises(ValueError, match="Unknown dataset"):
            get_ablation_ranges('unknown')


class TestRangeValidation:
    """Test ablation range validation."""
    
    def test_validate_sufficient_points(self):
        """Test validation with sufficient data points."""
        ell_data = np.arange(30, 1501)  # Planck-like range
        
        is_valid, n_points, reason = validate_ablation_range(
            ell_min=30,
            ell_max=250,
            ell_data=ell_data,
            min_points=50
        )
        
        assert is_valid is True
        assert n_points == 221  # 30 to 250 inclusive
        assert reason is None
    
    def test_validate_insufficient_points(self):
        """Test validation with too few points."""
        ell_data = np.arange(30, 100)  # Small range
        
        is_valid, n_points, reason = validate_ablation_range(
            ell_min=30,
            ell_max=200,
            ell_data=ell_data,
            min_points=100
        )
        
        assert is_valid is False
        assert n_points == 70
        assert 'Insufficient data points' in reason
    
    def test_validate_no_points(self):
        """Test validation with no points in range."""
        ell_data = np.arange(30, 100)
        
        is_valid, n_points, reason = validate_ablation_range(
            ell_min=200,
            ell_max=300,
            ell_data=ell_data,
            min_points=50
        )
        
        assert is_valid is False
        assert n_points == 0
        assert reason is not None  # Just check reason exists
    
    def test_validate_custom_threshold(self):
        """Test validation with custom minimum points."""
        ell_data = np.arange(30, 200)
        
        # Should pass with min_points=50
        is_valid1, _, _ = validate_ablation_range(
            30, 200, ell_data, min_points=50
        )
        assert is_valid1 is True
        
        # Should fail with min_points=200
        is_valid2, _, _ = validate_ablation_range(
            30, 200, ell_data, min_points=200
        )
        assert is_valid2 is False


class TestSlidingWindows:
    """Test sliding window generation."""
    
    def test_create_windows_default(self):
        """Test creating sliding windows with defaults."""
        ell_data = np.arange(30, 1501)  # Planck range
        
        windows = create_sliding_windows(
            ell_data,
            window_size=300,
            step=100,
            min_points=50
        )
        
        # Should create multiple windows
        assert len(windows) > 5
        
        # Check structure
        for name, ell_min, ell_max in windows:
            assert 'window_' in name
            assert ell_max - ell_min == 300
    
    def test_create_windows_custom(self):
        """Test creating windows with custom parameters."""
        ell_data = np.arange(30, 601)
        
        windows = create_sliding_windows(
            ell_data,
            window_size=200,
            step=50,
            min_points=100
        )
        
        # Check first window
        assert windows[0][1] == 30  # First ell_min
        assert windows[0][2] == 230  # First ell_max (30 + 200)
        
        # Check step
        if len(windows) > 1:
            assert windows[1][1] == 80  # Second ell_min (30 + 50)
    
    def test_create_windows_skip_invalid(self):
        """Test that invalid windows are skipped."""
        ell_data = np.arange(30, 200)  # Small range
        
        windows = create_sliding_windows(
            ell_data,
            window_size=300,
            step=100,
            min_points=50
        )
        
        # Can't fit 300-wide window in 170-point range
        assert len(windows) == 0


class TestResultSummarization:
    """Test ablation result summarization."""
    
    def test_summarize_empty_results(self):
        """Test summarization with no results."""
        summary = summarize_ablation_results({})
        
        assert summary['n_ranges'] == 0
        assert summary['n_skipped'] == 0
        assert summary['periods'] == {}
        assert summary['mean_p_value'] is None
    
    def test_summarize_valid_results(self):
        """Test summarization with valid results."""
        results = {
            'low': {
                'best_period': 255,
                'p_value': 0.001,
                'phase': 1.5,
                'amplitude': 0.05,
                'skipped': False
            },
            'mid': {
                'best_period': 255,
                'p_value': 0.005,
                'phase': 1.6,
                'amplitude': 0.04,
                'skipped': False
            },
            'high': {
                'best_period': 128,
                'p_value': 0.02,
                'phase': 0.8,
                'amplitude': 0.03,
                'skipped': False
            }
        }
        
        summary = summarize_ablation_results(results)
        
        assert summary['n_ranges'] == 3
        assert summary['n_valid'] == 3
        assert summary['n_skipped'] == 0
        assert summary['periods'][255] == 2
        assert summary['periods'][128] == 1
        assert np.isclose(summary['mean_p_value'], 0.00867, atol=0.0001)
        assert summary['median_p_value'] == 0.005
    
    def test_summarize_with_skipped(self):
        """Test summarization with some skipped ranges."""
        results = {
            'low': {
                'best_period': 255,
                'p_value': 0.001,
                'skipped': False
            },
            'mid': {
                'skipped': True,
                'skip_reason': 'Insufficient points'
            },
            'high': {
                'best_period': 255,
                'p_value': 0.002,
                'skipped': False
            }
        }
        
        summary = summarize_ablation_results(results)
        
        assert summary['n_ranges'] == 3
        assert summary['n_valid'] == 2
        assert summary['n_skipped'] == 1
        assert summary['periods'][255] == 2
    
    def test_summarize_phase_consistency(self):
        """Test phase consistency calculation."""
        results = {
            'range1': {
                'best_period': 255,
                'p_value': 0.001,
                'phase': 1.5,
                'skipped': False
            },
            'range2': {
                'best_period': 255,
                'p_value': 0.002,
                'phase': 1.6,  # Within π/2 of 1.5
                'skipped': False
            },
            'range3': {
                'best_period': 255,
                'p_value': 0.003,
                'phase': 1.55,  # Also close
                'skipped': False
            }
        }
        
        summary = summarize_ablation_results(results)
        
        assert summary['phase_consistency'] is not None
        assert summary['phase_consistency']['consistent_within_pi_2'] is True
        assert summary['phase_consistency']['max_phase_diff'] < np.pi / 2
    
    def test_summarize_phase_inconsistent(self):
        """Test detection of phase inconsistency."""
        results = {
            'range1': {
                'best_period': 255,
                'p_value': 0.001,
                'phase': 0.0,
                'skipped': False
            },
            'range2': {
                'best_period': 255,
                'p_value': 0.002,
                'phase': np.pi,  # Opposite phase
                'skipped': False
            }
        }
        
        summary = summarize_ablation_results(results)
        
        assert summary['phase_consistency'] is not None
        assert summary['phase_consistency']['max_phase_diff'] > np.pi / 2
        assert summary['phase_consistency']['consistent_within_pi_2'] is False
    
    def test_summarize_p_value_stats(self):
        """Test p-value statistics calculation."""
        results = {
            f'range{i}': {
                'best_period': 255,
                'p_value': 0.001 * (i + 1),
                'skipped': False
            }
            for i in range(10)
        }
        
        summary = summarize_ablation_results(results)
        
        assert summary['min_p_value'] == 0.001
        assert summary['max_p_value'] == 0.010
        assert 'mean_p_value' in summary
        assert 'median_p_value' in summary


class TestIntegration:
    """Integration tests combining multiple functions."""
    
    def test_full_ablation_workflow(self):
        """Test complete ablation workflow."""
        # Get ranges
        ranges = get_ablation_ranges('planck')
        
        # Simulate data
        ell_data = np.arange(30, 1501)
        
        # Validate each range
        valid_ranges = []
        for name, ell_min, ell_max in ranges:
            is_valid, n_points, reason = validate_ablation_range(
                ell_min, ell_max, ell_data, min_points=50
            )
            if is_valid:
                valid_ranges.append((name, ell_min, ell_max))
        
        assert len(valid_ranges) == 5  # All Planck ranges should be valid
        
        # Simulate results
        results = {}
        for name, ell_min, ell_max in valid_ranges:
            results[name] = {
                'best_period': 255,
                'p_value': np.random.uniform(0.001, 0.01),
                'phase': np.random.uniform(1.4, 1.6),
                'amplitude': 0.05,
                'skipped': False
            }
        
        # Summarize
        summary = summarize_ablation_results(results)
        
        assert summary['n_valid'] == 5
        assert summary['periods'][255] == 5
        assert summary['phase_consistency']['consistent_within_pi_2'] is True


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
