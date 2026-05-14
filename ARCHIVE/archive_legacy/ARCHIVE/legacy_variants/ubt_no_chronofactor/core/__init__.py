"""
UBT Core: Chronofactor-Free Unified Biquaternion Theory

This package implements the core formulation of UBT without external chronofactor.

Key components:
- theta_field: Biquaternionic field Θ(q) object model
- entropy_phase: Observable channels S_Θ and Σ_Θ

See README.md for detailed documentation.
"""

from .theta_field import ThetaField, k_B
from .entropy_phase import (
    entropy_channel,
    phase_channel,
    entropy_phase_decomposition,
    holonomy_integral,
    winding_number,
    is_topologically_trivial
)

__version__ = '0.1.0'
__author__ = 'UBT Core Team'

__all__ = [
    'ThetaField',
    'k_B',
    'entropy_channel',
    'phase_channel',
    'entropy_phase_decomposition',
    'holonomy_integral',
    'winding_number',
    'is_topologically_trivial',
]
