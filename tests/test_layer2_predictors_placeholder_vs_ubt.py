#!/usr/bin/env python3
"""
Tests for Layer2 Fingerprint - Predictors (Placeholder vs UBT)
===============================================================

Tests that predictors work correctly in both placeholder and ubt modes.

License: MIT
Copyright (c) 2025 Ing. David Jaroš
"""

import pytest
from forensic_fingerprint.layer2.config_space import Layer2Config
from forensic_fingerprint.layer2.predictors import predict_constants


def test_placeholder_returns_values():
    """Test that placeholder mode returns predicted values."""
    cfg = Layer2Config(
        rs_n=255,
        rs_k=200,
        ofdm_channels=16,
        winding_number=137,
        prime_gate_pattern=0,
        quantization_grid=255
    )
    
    # Placeholder should work without error
    predictions = predict_constants(cfg, mapping='placeholder')
    
    assert isinstance(predictions, dict), "Should return dictionary"
    assert 'alpha_inv' in predictions, "Should predict alpha_inv"
    assert 'electron_mass' in predictions, "Should predict electron_mass"
    
    # Values should be numeric
    assert isinstance(predictions['alpha_inv'], (int, float)), "alpha_inv should be numeric"
    assert isinstance(predictions['electron_mass'], (int, float)), "electron_mass should be numeric"
    
    # Values should be reasonable (not NaN, not infinite)
    assert not any(x != x for x in predictions.values()), "No NaN values"
    assert not any(x == float('inf') for x in predictions.values()), "No infinite values"


def test_placeholder_with_targets():
    """Test that placeholder mode respects targets parameter."""
    cfg = Layer2Config(
        rs_n=255,
        rs_k=200,
        ofdm_channels=16,
        winding_number=137,
        prime_gate_pattern=0,
        quantization_grid=255
    )
    
    # Request only alpha_inv
    predictions = predict_constants(cfg, mapping='placeholder', targets=['alpha_inv'])
    assert 'alpha_inv' in predictions
    assert len(predictions) == 1
    
    # Request only electron_mass
    predictions = predict_constants(cfg, mapping='placeholder', targets=['electron_mass'])
    assert 'electron_mass' in predictions
    assert len(predictions) == 1


def test_ubt_mode_exists():
    """Test that UBT mode can be called (may raise RuntimeError if not fully implemented)."""
    cfg = Layer2Config(
        rs_n=255,
        rs_k=200,
        ofdm_channels=16,
        winding_number=137,
        prime_gate_pattern=0,
        quantization_grid=255
    )
    
    # UBT mode should either work or raise RuntimeError with descriptive message
    try:
        predictions = predict_constants(cfg, mapping='ubt')
        
        # If it works, check structure
        assert isinstance(predictions, dict), "Should return dictionary"
        assert 'alpha_inv' in predictions or 'electron_mass' in predictions, \
            "Should predict at least one observable"
        
        # Values should be numeric
        for key, value in predictions.items():
            assert isinstance(value, (int, float)), f"{key} should be numeric"
            assert value == value, f"{key} should not be NaN"
            assert value != float('inf'), f"{key} should not be infinite"
        
    except RuntimeError as e:
        # If not implemented, error message should be descriptive
        error_msg = str(e).lower()
        assert any(keyword in error_msg for keyword in ['ubt', 'adapter', 'not', 'fail']), \
            f"RuntimeError should mention UBT/adapter: {e}"


def test_invalid_mapping_raises_error():
    """Test that invalid mapping mode raises ValueError."""
    cfg = Layer2Config(
        rs_n=255,
        rs_k=200,
        ofdm_channels=16,
        winding_number=137,
        prime_gate_pattern=0,
        quantization_grid=255
    )
    
    with pytest.raises(ValueError, match="Unknown.*mapping"):
        predict_constants(cfg, mapping='invalid_mode')


def test_placeholder_different_configs():
    """Test that placeholder gives different predictions for different configs."""
    cfg1 = Layer2Config(
        rs_n=200,
        rs_k=150,
        ofdm_channels=8,
        winding_number=100,
        prime_gate_pattern=0,
        quantization_grid=128
    )
    
    cfg2 = Layer2Config(
        rs_n=300,
        rs_k=250,
        ofdm_channels=32,
        winding_number=200,
        prime_gate_pattern=5,
        quantization_grid=512
    )
    
    pred1 = predict_constants(cfg1, mapping='placeholder')
    pred2 = predict_constants(cfg2, mapping='placeholder')
    
    # Predictions should be different for different configs
    assert pred1['alpha_inv'] != pred2['alpha_inv'], \
        "Different configs should give different predictions"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
