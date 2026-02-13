#!/usr/bin/env python3
"""
Tests for Layer2 Fingerprint - Rarity Bits Calculation
=======================================================

Tests the information-theoretic rarity metric used in rigidity analysis.

License: MIT
Copyright (c) 2025 Ing. David Jaroš
"""

import pytest
import math
from forensic_fingerprint.layer2.metrics import compute_rarity_bits


def test_rarity_bits_zero_hit_rate():
    """Test that zero hit-rate gives infinite rarity."""
    rarity = compute_rarity_bits(0.0)
    assert rarity == float('inf'), "Zero hit-rate should give infinite rarity"


def test_rarity_bits_half_hit_rate():
    """Test that 50% hit-rate gives 1 bit of rarity."""
    rarity = compute_rarity_bits(0.5)
    expected = -math.log2(0.5)
    assert abs(rarity - expected) < 1e-10, f"Expected {expected}, got {rarity}"
    assert abs(rarity - 1.0) < 1e-10, "50% hit-rate should give exactly 1 bit"


def test_rarity_bits_one_percent():
    """Test rarity for 1% hit-rate."""
    rarity = compute_rarity_bits(0.01)
    expected = -math.log2(0.01)
    assert abs(rarity - expected) < 1e-10, f"Expected {expected}, got {rarity}"
    assert abs(rarity - 6.643856) < 0.001, "1% hit-rate should give ~6.64 bits"


def test_rarity_bits_point_one_percent():
    """Test rarity for 0.1% hit-rate."""
    rarity = compute_rarity_bits(0.001)
    expected = -math.log2(0.001)
    assert abs(rarity - expected) < 1e-10, f"Expected {expected}, got {rarity}"
    assert abs(rarity - 9.965784) < 0.001, "0.1% hit-rate should give ~9.97 bits"


def test_rarity_bits_full_hit_rate():
    """Test that 100% hit-rate gives 0 bits (no rarity)."""
    rarity = compute_rarity_bits(1.0)
    assert abs(rarity - 0.0) < 1e-10, "100% hit-rate should give 0 bits"


def test_rarity_bits_invalid_negative():
    """Test that negative hit-rate raises ValueError."""
    with pytest.raises(ValueError, match="hit_rate must be in"):
        compute_rarity_bits(-0.1)


def test_rarity_bits_invalid_greater_than_one():
    """Test that hit-rate > 1 raises ValueError."""
    with pytest.raises(ValueError, match="hit_rate must be in"):
        compute_rarity_bits(1.5)


def test_rarity_bits_monotonic_decrease():
    """Test that rarity decreases monotonically with increasing hit-rate."""
    rates = [0.001, 0.01, 0.1, 0.5, 0.9]
    rarities = [compute_rarity_bits(r) for r in rates]
    
    for i in range(len(rarities) - 1):
        assert rarities[i] > rarities[i+1], \
            f"Rarity should decrease: {rarities[i]} > {rarities[i+1]}"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
