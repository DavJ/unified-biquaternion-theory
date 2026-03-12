"""
Layer 2 Fingerprint - Configuration Space Rigidity Testing

This package provides tools for quantifying the rigidity of UBT Layer 2 parameters
by sweeping through configuration space and evaluating match rates against
observed physical constants.

Modules:
--------
- config_space: Layer 2 configuration definitions and sampling
- predictors: Observable prediction from Layer 2 configs (placeholder and UBT modes)
- metrics: Statistical metrics (hit-rate, rarity bits)
- report: Output generation (CSV, JSON, Markdown)

License: MIT
Copyright (c) 2025 Ing. David Jaroš
"""

__version__ = "0.2.0-prototype"
__author__ = "Ing. David Jaroš"

from .config_space import Layer2Config, ConfigurationSpace
from .metrics import compute_hit_rate, compute_rarity_bits

__all__ = [
    'Layer2Config',
    'ConfigurationSpace',
    'compute_hit_rate',
    'compute_rarity_bits',
]
