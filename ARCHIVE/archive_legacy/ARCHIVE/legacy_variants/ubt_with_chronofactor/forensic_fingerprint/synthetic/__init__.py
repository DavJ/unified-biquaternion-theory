"""
Synthetic data generation for forensic fingerprint testing.

This module provides tools for generating synthetic CMB data for:
- ΛCDM null hypothesis testing
- False positive rate validation
- Injection studies for detection power
"""

from .lcdm import (
    generate_lcdm_spectrum,
    generate_mock_observation
)

__all__ = [
    'generate_lcdm_spectrum',
    'generate_mock_observation'
]
