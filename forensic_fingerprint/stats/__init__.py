"""
Statistical utilities for forensic fingerprint analysis.

This module provides statistical tools for analyzing CMB data including:
- Covariance matrix loading and alignment
- Whitening transformations (Cholesky-based)
- Regularization for ill-conditioned matrices
"""

from .whitening import (
    load_covariance,
    align_cov_to_ell,
    cholesky_whitener,
    whiten_residuals,
    validate_and_regularize_covariance
)

__all__ = [
    'load_covariance',
    'align_cov_to_ell',
    'cholesky_whitener',
    'whiten_residuals',
    'validate_and_regularize_covariance'
]
