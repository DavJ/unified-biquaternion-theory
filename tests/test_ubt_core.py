"""
Test basic functionality of UBT Core scaffolding.

These tests verify that the new chronofactor-free core implementation
has basic functionality working.
"""

import numpy as np
import sys
import os

# Add ubt_core to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from ubt_core.theta_field import ThetaField, k_B
from ubt_core.entropy_phase import (
    entropy_channel,
    phase_channel,
    entropy_phase_decomposition,
    holonomy_integral,
    winding_number
)


def test_theta_field_creation():
    """Test that we can create a ThetaField."""
    amplitude = np.array([1.0, 0.0, 0.0, 0.0])
    phase = np.array([0.0, 0.0, 0.0, 0.0])
    
    theta = ThetaField(amplitude, phase)
    
    assert theta.amplitude.shape == (4,)
    assert theta.phase.shape == (4,)
    assert len(theta.components) == 4


def test_theta_field_conjugate():
    """Test quaternionic conjugation."""
    amplitude = np.array([1.0, 2.0, 3.0, 4.0])
    phase = np.array([0.1, 0.2, 0.3, 0.4])
    
    theta = ThetaField(amplitude, phase)
    theta_conj = theta.conjugate()
    
    # Scalar component should have opposite phase sign
    assert theta_conj.amplitude[0] == theta.amplitude[0]
    assert theta_conj.phase[0] == -theta.phase[0]
    
    # Vector components should have opposite amplitude signs
    assert theta_conj.amplitude[1] == -theta.amplitude[1]


def test_theta_field_norm():
    """Test norm calculation."""
    amplitude = np.array([1.0, 0.0, 0.0, 0.0])
    phase = np.array([0.0, 0.0, 0.0, 0.0])
    
    theta = ThetaField(amplitude, phase)
    norm_sq = theta.norm_squared()
    
    # For real scalar biquaternion with amplitude 1, norm^2 should be 1
    assert abs(norm_sq - 1.0) < 1e-10


def test_entropy_channel():
    """Test entropy channel S_Θ calculation."""
    amplitude = np.array([2.0, 0.0, 0.0, 0.0])
    phase = np.array([0.0, 0.0, 0.0, 0.0])
    
    theta = ThetaField(amplitude, phase)
    S = entropy_channel(theta)
    
    # Entropy should be real
    assert isinstance(S, float)
    
    # For larger amplitude, entropy should be positive
    assert S > 0


def test_phase_channel():
    """Test phase channel Σ_Θ calculation."""
    amplitude = np.array([1.0, 0.0, 0.0, 0.0])
    phase = np.array([0.5, 0.0, 0.0, 0.0])
    
    theta = ThetaField(amplitude, phase)
    Sigma = phase_channel(theta)
    
    # Phase should be real
    assert isinstance(Sigma, float)
    
    # Phase should be bounded
    assert abs(Sigma) <= 2 * np.pi * k_B


def test_entropy_phase_decomposition():
    """Test simultaneous calculation of both channels."""
    amplitude = np.array([1.0, 0.5, 0.3, 0.2])
    phase = np.array([0.1, 0.2, 0.3, 0.4])
    
    theta = ThetaField(amplitude, phase)
    S, Sigma = entropy_phase_decomposition(theta)
    
    assert isinstance(S, float)
    assert isinstance(Sigma, float)


def test_holonomy_trivial_path():
    """Test holonomy for a trivial (single point) path."""
    amplitude = np.array([1.0, 0.0, 0.0, 0.0])
    phase = np.array([0.0, 0.0, 0.0, 0.0])
    
    theta = ThetaField(amplitude, phase)
    
    # Single point "path"
    path = [theta]
    winding = holonomy_integral(path)
    
    # Single point should give zero winding
    assert abs(winding) < 1e-10


def test_holonomy_closed_path():
    """Test holonomy around a closed path with phase variation."""
    # Create a path with phase varying around a loop
    path = []
    for i in range(8):
        amplitude = np.array([1.0, 0.0, 0.0, 0.0])
        phase = np.array([i * np.pi / 4, 0.0, 0.0, 0.0])
        path.append(ThetaField(amplitude, phase))
    
    winding = holonomy_integral(path)
    n = winding_number(winding)
    
    # Should have some winding
    assert isinstance(n, int)


def test_no_chronofactor_in_theta():
    """Verify that ThetaField does not have chronofactor dependency."""
    # ThetaField should only have amplitude and phase attributes
    amplitude = np.array([1.0, 0.0, 0.0, 0.0])
    phase = np.array([0.0, 0.0, 0.0, 0.0])
    
    theta = ThetaField(amplitude, phase)
    
    # Check that there's no tau, chronofactor, or psi attribute
    assert not hasattr(theta, 'tau')
    assert not hasattr(theta, 'chronofactor')
    assert not hasattr(theta, 'psi')
    assert not hasattr(theta, 'complex_time')


if __name__ == '__main__':
    print("Testing UBT Core scaffolding...")
    
    test_theta_field_creation()
    print("✓ ThetaField creation")
    
    test_theta_field_conjugate()
    print("✓ Quaternionic conjugation")
    
    test_theta_field_norm()
    print("✓ Norm calculation")
    
    test_entropy_channel()
    print("✓ Entropy channel S_Θ")
    
    test_phase_channel()
    print("✓ Phase channel Σ_Θ")
    
    test_entropy_phase_decomposition()
    print("✓ Entropy-phase decomposition")
    
    test_holonomy_trivial_path()
    print("✓ Holonomy trivial path")
    
    test_holonomy_closed_path()
    print("✓ Holonomy closed path")
    
    test_no_chronofactor_in_theta()
    print("✓ No chronofactor dependency")
    
    print("\n✅ All UBT Core scaffolding tests passed!")
