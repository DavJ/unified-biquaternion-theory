#!/usr/bin/env python3
"""
test_configs_load.py

Test that all configuration files load correctly and contain required fields.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sys
from pathlib import Path

# Add parent directory to path
repo_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo_root))

from research_phase_lock.utils.io import load_yaml


def test_grid_yaml_loads():
    """Test that grid.yaml loads successfully."""
    config_path = repo_root / 'research_phase_lock' / 'configs' / 'grid.yaml'
    config = load_yaml(config_path)
    
    assert config is not None, "Failed to load grid.yaml"
    assert 'global' in config, "Missing 'global' section in grid.yaml"
    assert 'data' in config, "Missing 'data' section in grid.yaml"
    assert 'grid' in config, "Missing 'grid' section in grid.yaml"
    
    print("✓ grid.yaml loads correctly")


def test_controls_yaml_loads():
    """Test that controls.yaml loads successfully."""
    config_path = repo_root / 'research_phase_lock' / 'configs' / 'controls.yaml'
    config = load_yaml(config_path)
    
    assert config is not None, "Failed to load controls.yaml"
    assert 'global' in config, "Missing 'global' section in controls.yaml"
    assert 'negative_controls' in config, "Missing 'negative_controls' section"
    assert 'positive_controls' in config, "Missing 'positive_controls' section"
    
    print("✓ controls.yaml loads correctly")


def test_grid_yaml_structure():
    """Test that grid.yaml has correct structure."""
    config_path = repo_root / 'research_phase_lock' / 'configs' / 'grid.yaml'
    config = load_yaml(config_path)
    
    # Check global section
    global_config = config['global']
    assert 'output_root' in global_config, "Missing output_root in global"
    assert 'seed' in global_config, "Missing seed in global"
    
    # Check data section
    data_config = config['data']
    assert 'mode' in data_config, "Missing mode in data"
    assert data_config['mode'] in ['synthetic', 'planck'], "Invalid data mode"
    
    # Check grid section
    grid_config = config['grid']
    required_grid_params = ['targets', 'projection', 'window_size', 'nside_out']
    for param in required_grid_params:
        assert param in grid_config, f"Missing {param} in grid"
        assert isinstance(grid_config[param], list), f"{param} should be a list"
    
    print("✓ grid.yaml structure is valid")


def test_controls_yaml_structure():
    """Test that controls.yaml has correct structure."""
    config_path = repo_root / 'research_phase_lock' / 'configs' / 'controls.yaml'
    config = load_yaml(config_path)
    
    # Check negative controls
    neg_controls = config['negative_controls']
    assert len(neg_controls) > 0, "No negative controls defined"
    
    for name, ctrl in neg_controls.items():
        if isinstance(ctrl, dict) and ctrl.get('enabled', True):
            assert 'description' in ctrl, f"Missing description in {name}"
            assert 'params' in ctrl, f"Missing params in {name}"
            assert 'grid' in ctrl, f"Missing grid in {name}"
    
    # Check positive controls
    pos_controls = config['positive_controls']
    assert len(pos_controls) > 0, "No positive controls defined"
    
    for name, ctrl in pos_controls.items():
        if isinstance(ctrl, dict) and ctrl.get('enabled', True):
            assert 'description' in ctrl, f"Missing description in {name}"
            assert 'params' in ctrl, f"Missing params in {name}"
            assert 'grid' in ctrl, f"Missing grid in {name}"
    
    print("✓ controls.yaml structure is valid")


def test_success_thresholds_defined():
    """Test that success thresholds are defined in grid.yaml."""
    config_path = repo_root / 'research_phase_lock' / 'configs' / 'grid.yaml'
    config = load_yaml(config_path)
    
    assert 'success_thresholds' in config, "Missing success_thresholds section"
    
    thresholds = config['success_thresholds']
    required = ['p_threshold', 'q_threshold', 'pc_min', 'delta_pc_max']
    
    for key in required:
        assert key in thresholds, f"Missing threshold: {key}"
        assert isinstance(thresholds[key], (int, float)), f"{key} should be numeric"
    
    print("✓ Success thresholds are defined")


def run_all_tests():
    """Run all configuration tests."""
    print("=" * 70)
    print("CONFIGURATION LOADING TESTS")
    print("=" * 70)
    print()
    
    tests = [
        test_grid_yaml_loads,
        test_controls_yaml_loads,
        test_grid_yaml_structure,
        test_controls_yaml_structure,
        test_success_thresholds_defined,
    ]
    
    passed = 0
    failed = 0
    
    for test_func in tests:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test_func.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test_func.__name__}: Unexpected error: {e}")
            failed += 1
    
    print()
    print("=" * 70)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 70)
    
    return failed == 0


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
