"""
UBT Core: Entropy and Phase Observables

This module implements the entropy channel S_Θ and phase channel Σ_Θ
derived from the fundamental Θ field.

Key definitions:
- S_Θ(x) = 2 k_B ln |det Θ(x)| (entropy channel)
- Σ_Θ(x) = k_B arg det Θ(x) (phase channel)

NO external chronofactor is used.
"""

import numpy as np
from typing import Optional
from .theta_field import ThetaField, k_B


def entropy_channel(theta: ThetaField, k_boltzmann: Optional[float] = None) -> float:
    """
    Calculate entropy channel S_Θ for a given Θ field configuration.
    
    Definition: S_Θ(x) = 2 k_B ln |det Θ(x)|
    
    Equivalent: S_Θ(x) = k_B ln det(Θ†(x) Θ(x))
    
    Args:
        theta: ThetaField object
        k_boltzmann: Boltzmann constant (default: uses module constant)
    
    Returns:
        Entropy value S_Θ (real, units of J/K)
    """
    if k_boltzmann is None:
        k_boltzmann = k_B
    
    # Compute determinant
    det_theta = theta.determinant()
    det_abs = abs(det_theta)
    
    # Handle zero or very small determinant
    if det_abs < 1e-100:
        # Return very negative entropy (low configuration volume)
        return -np.inf
    
    # S_Θ = 2 k_B ln |det Θ|
    entropy = 2.0 * k_boltzmann * np.log(det_abs)
    
    return entropy


def phase_channel(theta: ThetaField, k_boltzmann: Optional[float] = None) -> float:
    """
    Calculate phase channel Σ_Θ for a given Θ field configuration.
    
    Definition: Σ_Θ(x) = k_B arg det Θ(x)
    
    Args:
        theta: ThetaField object
        k_boltzmann: Boltzmann constant (default: uses module constant)
    
    Returns:
        Phase observable Σ_Θ (real, units of J/K, range [0, 2π k_B))
    """
    if k_boltzmann is None:
        k_boltzmann = k_B
    
    # Compute determinant
    det_theta = theta.determinant()
    
    # Extract argument (phase)
    phase_arg = np.angle(det_theta)  # Range: [-π, π]
    
    # Σ_Θ = k_B arg det Θ
    phase_obs = k_boltzmann * phase_arg
    
    return phase_obs


def entropy_phase_decomposition(theta: ThetaField, 
                                k_boltzmann: Optional[float] = None) -> tuple[float, float]:
    """
    Compute both entropy and phase channels simultaneously.
    
    Args:
        theta: ThetaField object
        k_boltzmann: Boltzmann constant (default: uses module constant)
    
    Returns:
        Tuple (S_Θ, Σ_Θ) of entropy and phase observables
    """
    S_theta = entropy_channel(theta, k_boltzmann)
    Sigma_theta = phase_channel(theta, k_boltzmann)
    
    return (S_theta, Sigma_theta)


def entropy_density(theta: ThetaField, volume_element: float = 1.0) -> float:
    """
    Calculate entropy density s_Θ = S_Θ / V.
    
    Args:
        theta: ThetaField object
        volume_element: Spacetime volume element dV (default: 1.0)
    
    Returns:
        Entropy density (J/K/m³)
    """
    S = entropy_channel(theta)
    return S / volume_element


def phase_gradient_estimate(theta_config: dict, direction: int = 0) -> float:
    """
    Estimate phase gradient ∂_μ Σ_Θ along a direction.
    
    This is a placeholder for holonomy and topological calculations.
    Requires field configuration over spatial region.
    
    Args:
        theta_config: Dictionary of ThetaField at neighboring points
        direction: Spacetime direction (0=t, 1=x, 2=y, 3=z)
    
    Returns:
        Phase gradient estimate (placeholder)
    """
    raise NotImplementedError("Phase gradient requires full field configuration")


def holonomy_integral(theta_path: list[ThetaField]) -> float:
    """
    Calculate phase holonomy around a closed path.
    
    Holonomy = ∮ dΣ_Θ (around closed loop)
    
    This captures topological winding and global phase constraints.
    
    Args:
        theta_path: Ordered list of ThetaField along closed path
    
    Returns:
        Total phase winding (units: J/K)
    """
    if len(theta_path) < 2:
        return 0.0
    
    # Calculate phase differences along path
    total_winding = 0.0
    for i in range(len(theta_path)):
        theta_i = theta_path[i]
        theta_next = theta_path[(i + 1) % len(theta_path)]
        
        phase_i = phase_channel(theta_i)
        phase_next = phase_channel(theta_next)
        
        # Accumulate phase difference (accounting for 2π wrapping)
        delta_phase = phase_next - phase_i
        
        # Wrap to [-π k_B, π k_B]
        while delta_phase > np.pi * k_B:
            delta_phase -= 2 * np.pi * k_B
        while delta_phase < -np.pi * k_B:
            delta_phase += 2 * np.pi * k_B
        
        total_winding += delta_phase
    
    return total_winding


# Physical interpretation helpers

def is_topologically_trivial(winding: float, tolerance: float = 1e-6) -> bool:
    """
    Check if phase winding corresponds to topologically trivial sector.
    
    Args:
        winding: Phase winding from holonomy_integral
        tolerance: Numerical tolerance for zero winding
    
    Returns:
        True if winding is approximately zero (trivial sector)
    """
    return abs(winding) < tolerance * k_B


def winding_number(winding: float) -> int:
    """
    Extract integer winding number from phase holonomy.
    
    Args:
        winding: Phase winding from holonomy_integral
    
    Returns:
        Integer winding number n (where winding ≈ 2πn k_B)
    """
    n = round(winding / (2 * np.pi * k_B))
    return n


# Module metadata
__version__ = '0.1.0'
__author__ = 'UBT Core Team'
__status__ = 'Development - Scaffolding Phase'
