#!/usr/bin/env python3
"""
test_smoke_synthetic.py

Smoke test for Phase-Lock grid runner using synthetic data.

This test verifies that the complete research harness works end-to-end
without requiring Planck data. It:

1. Creates a minimal grid configuration (2-4 runs)
2. Runs the grid with synthetic data
3. Verifies outputs are generated correctly
4. Checks result aggregation

Author: UBT Research Team
License: See repository LICENSE.md
"""

import os
import pytest
import tempfile
import shutil
from pathlib import Path

# Add parent to path
import sys
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root))

from research_phase_lock.run_grid import expand_grid, run_grid
from research_phase_lock.utils.io import save_yaml, load_yaml
from research_phase_lock.analysis.summarize import aggregate_results


class TestSmokeTestSynthetic:
    """Smoke tests using synthetic data."""
    
    def test_grid_expansion(self):
        """Test that grid expansion works correctly."""
        grid_params = {
            'projection': ['torus', 'lonlat'],
            'window': ['none'],
            'window_size': [64, 128]
        }
        
        combos = expand_grid(grid_params)
        
        # Should get 2 * 1 * 2 = 4 combinations
        assert len(combos) == 4
        
        # Check that all combinations are present
        projections = [c['projection'] for c in combos]
        assert projections.count('torus') == 2
        assert projections.count('lonlat') == 2
    
    def test_single_value_expansion(self):
        """Test grid expansion with single values."""
        grid_params = {
            'projection': 'torus',  # Single value, not list
            'window': ['none', 'hann']
        }
        
        combos = expand_grid(grid_params)
        
        # Should get 1 * 2 = 2 combinations
        assert len(combos) == 2
        
        # All should have 'torus' projection
        for c in combos:
            assert c['projection'] == 'torus'
    
    @pytest.mark.slow
    def test_minimal_grid_synthetic(self, tmp_path):
        """
        End-to-end test with minimal synthetic grid.
        
        This is a SLOW test that actually runs the phase lock scan.
        It uses synthetic data so no Planck maps are needed.
        """
        # Create minimal test config
        config = {
            'global': {
                'output_root': str(tmp_path / 'results'),
                'seed': 42,
                'max_runs': 2  # Limit to 2 runs for speed
            },
            'data': {
                'mode': 'synthetic',
                'synthetic': {
                    'nlat': 128,
                    'nlon': 256,
                    'locked_targets': [137, 139],
                    'noise_sigma': 0.1,
                    'phase_offset_rad': 0.1
                }
            },
            'grid': {
                'projection': ['torus'],
                'window': ['none'],
                'window_size': [64],
                'nside_out': [64],
                'nlat': [256],
                'nlon': [512],
                'null': ['phase-shuffle'],
                'mc': [50],  # Minimal MC for speed
                'targets': ['137,139']
            }
        }
        
        # Save config
        config_path = tmp_path / 'test_config.yaml'
        save_yaml(config, str(config_path))
        
        # Run grid
        try:
            run_grid(str(config_path), resume=False, dry_run=False)
        except Exception as e:
            # Print detailed error for debugging
            import traceback
            traceback.print_exc()
            pytest.fail(f"Grid run failed: {e}")
        
        # Verify outputs
        results_dir = tmp_path / 'results'
        assert results_dir.exists(), "Results directory not created"
        
        # Check that run directories were created
        run_dirs = [d for d in results_dir.iterdir() if d.is_dir() and d.name.startswith('run_')]
        assert len(run_dirs) > 0, "No run directories created"
        assert len(run_dirs) <= 2, f"Too many runs created: {len(run_dirs)}"
        
        # Check that each run has expected outputs
        for run_dir in run_dirs:
            # Check config saved
            config_file = run_dir / 'config.yaml'
            assert config_file.exists(), f"Config not saved for {run_dir.name}"
            
            # Check results CSV
            results_csv = run_dir / 'phase_lock_results.csv'
            assert results_csv.exists(), f"Results CSV not created for {run_dir.name}"
            
            # Check that results CSV has content
            with open(results_csv) as f:
                lines = f.readlines()
                assert len(lines) >= 2, "Results CSV is empty or has only header"
        
        # Check that summary was created
        summary_csv = results_dir / 'grid_summary.csv'
        assert summary_csv.exists(), "Grid summary not created"
        
        # Verify aggregation works
        results = aggregate_results(str(results_dir))
        assert len(results) > 0, "No results aggregated"
    
    def test_config_yaml_validation(self):
        """Test that example config is valid YAML."""
        config_path = repo_root / 'research_phase_lock' / 'configs' / 'grid_v1.yaml'
        
        if not config_path.exists():
            pytest.skip("Config file not found")
        
        # Should load without error
        config = load_yaml(str(config_path))
        
        # Check expected sections
        assert 'global' in config
        assert 'data' in config
        assert 'grid' in config
        
        # Check data mode
        assert 'mode' in config['data']
        assert config['data']['mode'] in ['synthetic', 'planck']


class TestUtilities:
    """Test utility functions."""
    
    def test_hashing_deterministic(self):
        """Test that config hashing is deterministic."""
        from research_phase_lock.utils.hashing import config_to_hash, generate_run_id
        
        config1 = {'a': 1, 'b': 2, 'c': 3}
        config2 = {'c': 3, 'a': 1, 'b': 2}  # Same, different order
        
        # Hashes should be identical despite different key ordering
        hash1 = config_to_hash(config1)
        hash2 = config_to_hash(config2)
        assert hash1 == hash2
        
        # Run IDs should be identical
        run_id1 = generate_run_id(config1)
        run_id2 = generate_run_id(config2)
        assert run_id1 == run_id2
    
    def test_hashing_different_configs(self):
        """Test that different configs produce different hashes."""
        from research_phase_lock.utils.hashing import config_to_hash
        
        config1 = {'a': 1, 'b': 2}
        config2 = {'a': 1, 'b': 3}  # Different value
        
        hash1 = config_to_hash(config1)
        hash2 = config_to_hash(config2)
        assert hash1 != hash2


if __name__ == '__main__':
    # Run tests
    pytest.main([__file__, '-v'])
