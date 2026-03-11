#!/usr/bin/env python3
"""
Whitening and Covariance Utilities for Court-Grade CMB Analysis
================================================================

This module provides numerically stable functions for:
1. Loading and validating covariance matrices
2. Aligning covariance to target ell ranges
3. Cholesky-based whitening transformations
4. Ridge regularization for ill-conditioned matrices

All functions use Cholesky decomposition and solving (not explicit matrix inversion)
for numerical stability.

License: MIT
Author: UBT Research Team
"""

import numpy as np
from pathlib import Path
import warnings


def load_covariance(cov_path):
    """
    Load covariance matrix from file.
    
    Supports:
    - NumPy .npy files
    - Text files (space/comma-delimited, square matrix)
    - FITS files (TODO: if needed)
    
    Parameters
    ----------
    cov_path : str or Path
        Path to covariance file
    
    Returns
    -------
    ell : ndarray
        Multipole moments (if available in file metadata, else None)
    C : ndarray
        Covariance matrix (N x N)
    
    Raises
    ------
    FileNotFoundError
        If file doesn't exist
    ValueError
        If file format is invalid or matrix is not square
    """
    cov_path = Path(cov_path)
    
    if not cov_path.exists():
        raise FileNotFoundError(f"Covariance file not found: {cov_path}")
    
    # Load based on extension
    if cov_path.suffix == '.npy':
        C = np.load(cov_path)
        ell = None  # Metadata not stored in .npy
    elif cov_path.suffix in ['.txt', '.dat', '.csv']:
        C = np.loadtxt(cov_path)
        ell = None
    else:
        raise ValueError(f"Unsupported covariance file format: {cov_path.suffix}")
    
    # Validate square matrix
    if C.ndim != 2:
        raise ValueError(f"Covariance must be 2D array, got shape {C.shape}")
    
    if C.shape[0] != C.shape[1]:
        raise ValueError(f"Covariance must be square, got shape {C.shape}")
    
    return ell, C


def align_cov_to_ell(C, ell_cov, ell_target):
    """
    Align covariance matrix to target multipole range.
    
    Extracts subset of covariance corresponding to ell_target.
    Assumes ell_cov and ell_target are sorted arrays of multipoles.
    
    Parameters
    ----------
    C : ndarray
        Full covariance matrix (N x N)
    ell_cov : array-like
        Multipoles corresponding to C (length N)
    ell_target : array-like
        Target multipoles to extract (length M ≤ N)
    
    Returns
    -------
    C_aligned : ndarray
        Aligned covariance matrix (M x M)
    
    Raises
    ------
    ValueError
        If target ells are not a subset of cov ells
    """
    if ell_cov is None:
        # If covariance has no ell metadata, assume it matches target
        if C.shape[0] != len(ell_target):
            raise ValueError(
                f"Covariance size {C.shape[0]} doesn't match target ell count {len(ell_target)}. "
                "Provide ell_cov or ensure covariance matches target range."
            )
        return C
    
    ell_cov = np.asarray(ell_cov)
    ell_target = np.asarray(ell_target)
    
    # Find indices in ell_cov that match ell_target
    indices = []
    for ell_t in ell_target:
        idx = np.where(ell_cov == ell_t)[0]
        if len(idx) == 0:
            raise ValueError(
                f"Target ell={ell_t} not found in covariance ells. "
                "Covariance must cover the full target ell range."
            )
        indices.append(idx[0])
    
    indices = np.array(indices)
    
    # Extract submatrix
    C_aligned = C[np.ix_(indices, indices)]
    
    return C_aligned


def validate_and_regularize_covariance(C, ell=None, target_condition=1e8, 
                                       symmetry_tolerance=1e-10, 
                                       auto_symmetrize=True):
    """
    Validate covariance matrix and apply regularization if needed.
    
    Checks:
    - Symmetry (with auto-symmetrization option)
    - Positive definiteness
    - Condition number
    
    Applies ridge regularization if condition number exceeds threshold.
    
    Parameters
    ----------
    C : ndarray
        Covariance matrix (N x N)
    ell : array-like, optional
        Multipole moments (for metadata reporting)
    target_condition : float
        Target condition number for regularization (default: 1e8)
    symmetry_tolerance : float
        Tolerance for symmetry check (default: 1e-10)
    auto_symmetrize : bool
        If True, auto-symmetrize if asymmetry is small (default: True)
    
    Returns
    -------
    C_validated : ndarray
        Validated (and possibly regularized) covariance
    metadata : dict
        Validation and regularization metadata with keys:
        - is_symmetric: bool (before auto-symmetrization)
        - was_symmetrized: bool
        - is_positive_definite: bool (before regularization)
        - min_eigenvalue: float
        - max_eigenvalue: float
        - condition_number: float (before regularization)
        - needs_regularization: bool
        - regularization_applied: bool
        - lambda_ridge: float or None
        - final_condition_number: float
        - ell_range: tuple or None
        - matrix_size: int
    """
    n = C.shape[0]
    metadata = {
        'matrix_size': n,
        'ell_range': (int(ell[0]), int(ell[-1])) if ell is not None else None,
        'was_symmetrized': False,
        'regularization_applied': False,
        'lambda_ridge': None
    }
    
    # Check symmetry
    is_symmetric = np.allclose(C, C.T, rtol=symmetry_tolerance, atol=symmetry_tolerance)
    metadata['is_symmetric'] = is_symmetric
    
    C_work = C.copy()
    
    # Auto-symmetrize if requested and asymmetry is small
    if not is_symmetric and auto_symmetrize:
        asymmetry = np.max(np.abs(C - C.T))
        if asymmetry < 1e-6 * np.max(np.abs(C)):
            C_work = (C + C.T) / 2
            metadata['was_symmetrized'] = True
            warnings.warn(
                f"Covariance was slightly asymmetric (max diff = {asymmetry:.2e}). "
                "Auto-symmetrized. Use auto_symmetrize=False to disable."
            )
        else:
            raise ValueError(
                f"Covariance is significantly asymmetric (max diff = {asymmetry:.2e}). "
                "This likely indicates a data loading error."
            )
    elif not is_symmetric:
        raise ValueError("Covariance matrix is not symmetric.")
    
    # Compute eigenvalues for validation
    eigenvalues = np.linalg.eigvalsh(C_work)
    min_eig = np.min(eigenvalues)
    max_eig = np.max(eigenvalues)
    
    metadata['min_eigenvalue'] = float(min_eig)
    metadata['max_eigenvalue'] = float(max_eig)
    
    # Check positive definiteness
    is_positive_definite = min_eig > 0
    metadata['is_positive_definite'] = is_positive_definite
    
    # Condition number
    if min_eig > 0:
        condition_number = max_eig / min_eig
    else:
        condition_number = np.inf
    
    metadata['condition_number'] = float(condition_number)
    
    # Determine if regularization is needed
    needs_regularization = (not is_positive_definite) or (condition_number > target_condition)
    metadata['needs_regularization'] = needs_regularization
    
    # Apply ridge regularization if needed
    if needs_regularization:
        C_validated, lambda_ridge = _apply_ridge_regularization(
            C_work, target_condition=target_condition
        )
        metadata['regularization_applied'] = True
        metadata['lambda_ridge'] = float(lambda_ridge)
        
        # Compute final condition number
        eigs_final = np.linalg.eigvalsh(C_validated)
        final_cond = np.max(eigs_final) / np.min(eigs_final)
        metadata['final_condition_number'] = float(final_cond)
        
        warnings.warn(
            f"Covariance regularized: added {lambda_ridge:.2e} * I. "
            f"Condition number: {condition_number:.2e} → {final_cond:.2e}"
        )
    else:
        C_validated = C_work
        metadata['final_condition_number'] = float(condition_number)
    
    return C_validated, metadata


def _apply_ridge_regularization(C, target_condition=1e8):
    """
    Internal function: Apply ridge regularization to covariance.
    
    Adds λI to bring condition number to target value.
    
    Parameters
    ----------
    C : ndarray
        Covariance matrix
    target_condition : float
        Target condition number
    
    Returns
    -------
    C_reg : ndarray
        Regularized covariance
    lambda_ridge : float
        Regularization parameter used
    """
    eigenvalues = np.linalg.eigvalsh(C)
    min_eig = np.min(eigenvalues)
    max_eig = np.max(eigenvalues)
    
    if min_eig <= 0:
        # Not positive definite - add offset to make it so
        lambda_ridge = abs(min_eig) + max_eig * 1e-6
    else:
        # Solve for λ to achieve target condition number
        # (max_eig + λ) / (min_eig + λ) = target_condition
        # λ * (target_condition - 1) = max_eig - target_condition * min_eig
        lambda_ridge = (max_eig - target_condition * min_eig) / (target_condition - 1)
        
        # Ensure positive and at least a minimum
        lambda_ridge = max(lambda_ridge, max_eig * 1e-10)
    
    C_reg = C + lambda_ridge * np.eye(C.shape[0])
    
    return C_reg, lambda_ridge


def cholesky_whitener(C):
    """
    Compute Cholesky whitening transformation.
    
    Given covariance C, computes L such that C = L L^T.
    The whitening transformation is W = L^{-1}.
    
    For a random vector r ~ N(0, C), the whitened vector w = W @ r ~ N(0, I).
    
    Parameters
    ----------
    C : ndarray
        Covariance matrix (N x N), must be symmetric positive definite
    
    Returns
    -------
    L : ndarray
        Lower triangular Cholesky factor (N x N)
    
    Raises
    ------
    np.linalg.LinAlgError
        If Cholesky decomposition fails (matrix not positive definite)
    
    Notes
    -----
    This function does NOT return W explicitly. Use whiten_residuals() to apply
    the whitening transformation, which uses Cholesky solving for stability.
    """
    try:
        L = np.linalg.cholesky(C)
        return L
    except np.linalg.LinAlgError as e:
        raise np.linalg.LinAlgError(
            "Cholesky decomposition failed. Covariance is not positive definite. "
            "Try validate_and_regularize_covariance() first."
        ) from e


def whiten_residuals(r, C):
    """
    Whiten residuals using Cholesky solve (numerically stable).
    
    Computes whitened residuals: r_w = L^{-1} r
    where C = L L^T (Cholesky decomposition).
    
    This is equivalent to r_w = C^{-1/2} r but computed via Cholesky solve
    instead of explicit matrix inversion for numerical stability.
    
    Parameters
    ----------
    r : ndarray
        Residuals to whiten (length N)
    C : ndarray
        Covariance matrix (N x N), must be symmetric positive definite
    
    Returns
    -------
    r_w : ndarray
        Whitened residuals (length N)
    
    Raises
    ------
    np.linalg.LinAlgError
        If Cholesky decomposition fails
    
    Notes
    -----
    After whitening, if r ~ N(0, C), then r_w ~ N(0, I).
    Chi-squared statistic: χ² = r^T C^{-1} r = ||r_w||²
    """
    r = np.asarray(r)
    C = np.asarray(C)
    
    if len(r) != C.shape[0]:
        raise ValueError(f"Residual length {len(r)} doesn't match covariance size {C.shape[0]}")
    
    # Compute Cholesky factor: C = L L^T
    L = cholesky_whitener(C)
    
    # Solve L r_w = r for r_w
    # This is equivalent to r_w = L^{-1} r but numerically stable
    r_w = np.linalg.solve(L, r)
    
    return r_w
