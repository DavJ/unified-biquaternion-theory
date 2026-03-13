"""
Forensic Fingerprint Data Loaders

This module provides loaders for real CMB datasets (Planck, WMAP)
with unified interface for the CMB comb fingerprint test.

All loaders return standardized data dictionaries with:
- ell: array of multipole moments
- cl_obs: observed power spectrum
- cl_model: theoretical model (if available)
- sigma: diagonal uncertainties (1-D array)
- cov: full covariance matrix (2-D array, optional)
- dataset: dataset name for provenance

License: MIT
Author: UBT Research Team
"""

__version__ = "1.0.0"

from .planck import load_planck_data
from .wmap import load_wmap_data

__all__ = [
    'load_planck_data',
    'load_wmap_data',
]
