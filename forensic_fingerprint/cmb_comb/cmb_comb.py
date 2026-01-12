#!/usr/bin/env python3
"""
UBT Forensic Fingerprint - CMB Comb Test
=========================================

Test #1: Search for periodic "comb" signatures in CMB power spectrum residuals.

This script implements a pre-registered protocol to test whether CMB residuals
(observed - ΛCDM model) contain sinusoidal oscillations at candidate periods,
which could indicate discrete spacetime architecture.

**IMPORTANT**: This test is ONLY valid under Variant C (Explicit Frame Synchronization).
See forensic_fingerprint/ARCHITECTURE_VARIANTS.md for variant definitions.

Protocol: See ../PROTOCOL.md
Author: UBT Research Team
License: MIT
"""

import numpy as np
import sys
import argparse
from pathlib import Path
from datetime import datetime


# =============================================================================
# Architecture Variant Selection
# =============================================================================

# ARCHITECTURE_VARIANT: Which architectural hypothesis to test
# Valid values: "A", "B", "C", "D"
# See ../ARCHITECTURE_VARIANTS.md for definitions
#
# "A" = No Explicit Synchronization (continuous-time)
# "B" = Implicit Synchronization (discrete states, no sync symbol)
# "C" = Explicit Frame Synchronization (RS with sync overhead)
# "D" = Hierarchical Synchronization (local sync, global async)
#
# CMB comb test is ONLY applicable to Variant C.
# Other variants predict null results (no periodic structure).

ARCHITECTURE_VARIANT = "C"  # DEFAULT: Test Variant C hypothesis

# =============================================================================
# Pre-Registered Parameters (LOCKED)
# =============================================================================

# Fixed random seed for reproducibility (pre-registered)
RANDOM_SEED = 42

# Pre-fixed candidate periods (locked in protocol)
CANDIDATE_PERIODS = [8, 16, 32, 64, 128, 255]

# Monte Carlo parameters
N_MC_TRIALS = 10000

# Significance thresholds (pre-registered)
THRESHOLD_CANDIDATE = 0.01  # p < 0.01 for "candidate signal"
THRESHOLD_STRONG = 2.9e-7   # p < 2.9e-7 for "strong signal" (~5σ)


def create_block_diagonal_covariance(sigma, block_size=10):
    """
    Create block-diagonal approximation to covariance matrix.
    
    This approximates the full covariance by creating blocks where nearby
    multipoles have correlated uncertainties. This is a middle ground between
    diagonal (no correlations) and full covariance.
    
    Parameters
    ----------
    sigma : array-like
        Diagonal uncertainties
    block_size : int
        Size of correlation blocks (default: 10)
    
    Returns
    -------
    cov : ndarray
        Block-diagonal covariance matrix
    """
    n = len(sigma)
    cov = np.zeros((n, n))
    
    # Fill blocks
    for i in range(0, n, block_size):
        # Determine block end
        j_end = min(i + block_size, n)
        block_n = j_end - i
        
        # Create block with exponential decay correlation
        for j in range(block_n):
            for k in range(block_n):
                # Correlation decreases exponentially with distance
                correlation = np.exp(-abs(j - k) / 3.0)
                cov[i + j, i + k] = sigma[i + j] * sigma[i + k] * correlation
    
    return cov


def validate_covariance(cov, ell):
    """
    Validate covariance matrix and compute diagnostics.
    
    Checks:
    - Symmetry
    - Positive definiteness (via eigenvalues)
    - Computes condition number
    - Returns metadata for provenance
    
    Parameters
    ----------
    cov : ndarray
        Covariance matrix (n x n)
    ell : array-like
        Multipole moments (for range reporting)
    
    Returns
    -------
    dict
        Validation metadata with keys:
        - is_symmetric: bool
        - is_positive_definite: bool
        - min_eigenvalue: float
        - max_eigenvalue: float
        - condition_number: float
        - ell_range: tuple (ell_min, ell_max)
        - needs_regularization: bool
    """
    n = cov.shape[0]
    
    # Check symmetry
    is_symmetric = np.allclose(cov, cov.T, rtol=1e-10, atol=1e-12)
    
    # Compute eigenvalues (for positive definiteness and condition number)
    eigenvalues = np.linalg.eigvalsh(cov)
    min_eig = np.min(eigenvalues)
    max_eig = np.max(eigenvalues)
    
    # Check positive definiteness
    is_positive_definite = min_eig > 0
    
    # Condition number (ratio of largest to smallest eigenvalue)
    if min_eig > 0:
        condition_number = max_eig / min_eig
    else:
        condition_number = np.inf
    
    # Determine if regularization is needed
    # Use threshold: condition number > 1e10 or min eigenvalue < 1e-10
    needs_regularization = (not is_positive_definite) or (condition_number > 1e10)
    
    metadata = {
        'is_symmetric': is_symmetric,
        'is_positive_definite': is_positive_definite,
        'min_eigenvalue': float(min_eig),
        'max_eigenvalue': float(max_eig),
        'condition_number': float(condition_number),
        'ell_range': (int(ell[0]), int(ell[-1])),
        'needs_regularization': needs_regularization,
        'matrix_size': n
    }
    
    return metadata


def apply_ridge_regularization(cov, lambda_ridge=None, target_condition=1e8):
    """
    Apply ridge regularization to ill-conditioned covariance matrix.
    
    Adds λI to covariance: Σ_reg = Σ + λI
    
    Parameters
    ----------
    cov : ndarray
        Original covariance matrix
    lambda_ridge : float, optional
        Regularization parameter. If None, automatically determined.
    target_condition : float
        Target condition number after regularization (default: 1e8)
    
    Returns
    -------
    cov_reg : ndarray
        Regularized covariance matrix
    lambda_used : float
        Regularization parameter used
    """
    if lambda_ridge is None:
        # Auto-determine lambda from eigenvalues
        eigenvalues = np.linalg.eigvalsh(cov)
        min_eig = np.min(eigenvalues)
        max_eig = np.max(eigenvalues)
        
        # Set lambda to bring condition number to target_condition
        # After regularization: cond = (max_eig + λ) / (min_eig + λ)
        # Solve for λ: target_condition * (min_eig + λ) = max_eig + λ
        #               λ * (target_condition - 1) = max_eig - target_condition * min_eig
        
        if min_eig <= 0:
            # If not positive definite, add small offset
            lambda_ridge = abs(min_eig) + max_eig * 1e-6
        else:
            lambda_ridge = max(0, (max_eig - target_condition * min_eig) / (target_condition - 1))
            # Ensure at least a small regularization
            lambda_ridge = max(lambda_ridge, max_eig * 1e-10)
    
    # Apply regularization
    cov_reg = cov + lambda_ridge * np.eye(cov.shape[0])
    
    return cov_reg, lambda_ridge


def compute_residuals(ell, C_obs, C_model, sigma, cov=None, whiten_mode='diagonal', 
                     cov_jitter=1e-12, cov_method='cholesky', strict=False):
    """
    Compute normalized residuals with optional whitening.
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    C_obs : array-like
        Observed C_ℓ power spectrum
    C_model : array-like
        ΛCDM model prediction C_ℓ
    sigma : array-like
        Uncertainty (diagonal covariance assumed if cov is None)
    cov : array-like, optional
        Full covariance matrix. If provided and whiten_mode='covariance' or 'cov_diag', 
        residuals are whitened.
    whiten_mode : str
        Whitening mode: 'none', 'diagonal', 'covariance', 'cov_diag', or 'block-diagonal'
    cov_jitter : float
        Regularization jitter for covariance matrix (default: 1e-12)
    cov_method : str
        Covariance factorization method: 'cholesky' or 'eigh' (default: 'cholesky')
    strict : bool
        If True, raises RuntimeError on catastrophic units mismatch (court-grade mode).
        Default False for backward compatibility.
    
    Returns
    -------
    residuals : ndarray
        Normalized residuals. Normalization depends on whiten_mode:
        - 'none': r = C_obs - C_model (no normalization)
        - 'diagonal': r = (C_obs - C_model) / sigma
        - 'covariance': r = L^-1 (C_obs - C_model) where L is Cholesky of cov
        - 'cov_diag': r = (C_obs - C_model) / sqrt(diag(cov))
        - 'block-diagonal': r = L^-1 (C_obs - C_model) where L is Cholesky of block-diagonal cov
    metadata : dict
        Whitening metadata (condition number, regularization, debug stats, etc.)
    """
    diff = C_obs - C_model
    metadata = {
        'whiten_mode': whiten_mode,
        'regularization_used': False,
        'lambda_ridge': None,
        'cov_metadata': None
    }
    
    # Compute debug statistics for diff and sigma
    debug_stats = {
        'std_diff': float(np.std(diff)),
        'std_sigma': float(np.std(sigma)),
        'mean_diff': float(np.mean(diff)),
        'mean_sigma': float(np.mean(sigma)),
    }
    
    if whiten_mode == 'none':
        # No whitening
        residuals = diff
    elif whiten_mode == 'diagonal':
        # Use diagonal uncertainties
        residuals = diff / sigma
    elif whiten_mode == 'cov_diag':
        # Use diagonal extracted from covariance matrix
        if cov is not None:
            # Extract diagonal from covariance
            sigma_from_cov = np.sqrt(np.diag(cov))
            residuals = diff / sigma_from_cov
            metadata['cov_metadata'] = {
                'source': 'diagonal from covariance',
                'matrix_size': cov.shape[0]
            }
            debug_stats['std_sigma_from_cov'] = float(np.std(sigma_from_cov))
        else:
            print("WARNING: Covariance matrix not provided for 'cov_diag' mode. Falling back to 'diagonal'.")
            residuals = diff / sigma
    elif whiten_mode == 'covariance':
        if cov is not None:
            # Validate covariance
            cov_validation = validate_covariance(cov, ell)
            metadata['cov_metadata'] = cov_validation
            
            # Log validation results
            print(f"Covariance validation:")
            print(f"  Symmetric: {cov_validation['is_symmetric']}")
            print(f"  Positive definite: {cov_validation['is_positive_definite']}")
            print(f"  Min eigenvalue: {cov_validation['min_eigenvalue']:.6e}")
            print(f"  Max eigenvalue: {cov_validation['max_eigenvalue']:.6e}")
            print(f"  Condition number: {cov_validation['condition_number']:.6e}")
            print(f"  ℓ-range: {cov_validation['ell_range']}")
            
            # Symmetrize if needed
            if not cov_validation['is_symmetric']:
                print("WARNING: Covariance not symmetric. Symmetrizing: cov = (cov + cov.T) / 2")
                cov = 0.5 * (cov + cov.T)
            
            # Apply regularization if needed OR if jitter is specified
            if cov_validation['needs_regularization'] or cov_jitter > 0:
                if cov_validation['needs_regularization']:
                    print(f"WARNING: Covariance is ill-conditioned (cond={cov_validation['condition_number']:.2e})")
                    print("         Applying ridge regularization...")
                # Apply jitter
                cov_reg = cov + cov_jitter * np.eye(cov.shape[0])
                metadata['regularization_used'] = True
                metadata['lambda_ridge'] = float(cov_jitter)
                print(f"         Ridge parameter λ = {cov_jitter:.6e}")
                
                # Re-validate
                cov_validation_after = validate_covariance(cov_reg, ell)
                print(f"         After regularization:")
                print(f"           Condition number: {cov_validation_after['condition_number']:.6e}")
                print(f"           Min eigenvalue: {cov_validation_after['min_eigenvalue']:.6e}")
                cov = cov_reg
            
            # Whiten using specified method
            try:
                if cov_method == 'cholesky':
                    L = np.linalg.cholesky(cov)
                    residuals = np.linalg.solve(L, diff)
                elif cov_method == 'eigh':
                    eigenvalues, eigenvectors = np.linalg.eigh(cov)
                    sqrt_inv_eigs = 1.0 / np.sqrt(eigenvalues)
                    residuals = (eigenvectors.T @ diff) * sqrt_inv_eigs
                else:
                    raise ValueError(f"Unknown cov_method: {cov_method}")
                metadata['cov_method'] = cov_method
            except np.linalg.LinAlgError as e:
                print(f"ERROR: {cov_method} decomposition failed even after regularization: {e}")
                print("       Falling back to diagonal.")
                residuals = diff / sigma
                metadata['fallback_to_diagonal'] = True
        else:
            print("WARNING: Covariance matrix not provided. Falling back to diagonal.")
            residuals = diff / sigma
    elif whiten_mode == 'block-diagonal':
        # Create block-diagonal approximation
        block_cov = create_block_diagonal_covariance(sigma)
        try:
            L = np.linalg.cholesky(block_cov)
            residuals = np.linalg.solve(L, diff)
        except np.linalg.LinAlgError:
            print("WARNING: Block-diagonal covariance is not positive definite. Falling back to diagonal.")
            residuals = diff / sigma
    else:
        raise ValueError(f"Unknown whitening mode: {whiten_mode}")
    
    # Add residual statistics after whitening
    debug_stats['median_abs_residual_over_sigma'] = float(np.median(np.abs(residuals)))
    debug_stats['max_abs_residual_over_sigma'] = float(np.max(np.abs(residuals)))
    debug_stats['std_residuals'] = float(np.std(residuals))
    debug_stats['mean_residuals'] = float(np.mean(residuals))
    
    metadata['debug_stats'] = debug_stats
    
    # Check for units mismatch (exploding chi2)
    chi2_per_dof = np.sum(residuals**2) / len(residuals)
    median_abs_res = debug_stats['median_abs_residual_over_sigma']
    
    # Court-grade mode: strict sanity checks
    # These thresholds indicate catastrophic units mismatch
    CATASTROPHIC_CHI2_THRESHOLD = 1e6  # chi2/dof >> 1e6
    CATASTROPHIC_MEDIAN_THRESHOLD = 1e4  # median(|diff/sigma|) >> 1e4
    
    is_catastrophic = (chi2_per_dof > CATASTROPHIC_CHI2_THRESHOLD or 
                      median_abs_res > CATASTROPHIC_MEDIAN_THRESHOLD)
    
    if chi2_per_dof > 100.0:  # Warning threshold (less severe)
        print()
        print("=" * 80)
        print("WARNING: POSSIBLE UNITS MISMATCH OR WRONG MODEL")
        print("=" * 80)
        print(f"χ²/dof = {chi2_per_dof:.2e} >> 1")
        print()
        print("This suggests one of the following:")
        print("  1. Observation and model have different units (Cl vs Dl)")
        print("  2. Model file is incorrect (not matching the observation)")
        print("  3. Uncertainties are severely underestimated")
        print()
        print("Debug statistics:")
        print(f"  std(diff) = {debug_stats['std_diff']:.2e}")
        print(f"  std(sigma) = {debug_stats['std_sigma']:.2e}")
        print(f"  median(|diff/sigma|) = {median_abs_res:.2e}")
        print(f"  max(|diff/sigma|) = {debug_stats['max_abs_residual_over_sigma']:.2e}")
        print()
        print("Please verify:")
        print("  - Both files use same units (μK² for Cl, or both converted)")
        print("  - Model corresponds to the correct observation")
        print("  - Uncertainties are correctly loaded")
        print("  - Model file is TT power spectrum, not likelihood/parameter file")
        print("=" * 80)
        print()
        metadata['units_mismatch_warning'] = True
        
        # COURT-GRADE MODE: Fail fast on catastrophic mismatch (only if strict=True)
        if is_catastrophic and strict:
            print()
            print("=" * 80)
            print("ERROR: CATASTROPHIC UNITS MISMATCH DETECTED (STRICT MODE FAILURE)")
            print("=" * 80)
            print()
            print(f"χ²/dof = {chi2_per_dof:.2e} (threshold: {CATASTROPHIC_CHI2_THRESHOLD:.0e})")
            print(f"median(|diff/sigma|) = {median_abs_res:.2e} (threshold: {CATASTROPHIC_MEDIAN_THRESHOLD:.0e})")
            print()
            print("This indicates a CRITICAL ERROR in data loading:")
            print()
            print("MOST LIKELY CAUSES:")
            print("  1. **Model file in wrong units**: Obs is Dl, model is Cl (or vice versa)")
            print("  2. **Wrong model file**: Using likelihood/parameter file instead of spectrum")
            print("  3. **Corrupted data**: File damaged or wrong format")
            print()
            print("REQUIRED ACTIONS:")
            print("  1. Verify observation file format (check header for 'l Dl -dDl +dDl')")
            print("  2. Verify model file is TT power spectrum (NOT 'minimum' or 'plikHM')")
            print("  3. Ensure both files are in compatible units")
            print("  4. Check that ℓ-ranges match")
            print()
            print("Court-grade analysis CANNOT proceed with this data configuration.")
            print("Strict mode is enabled (--strict flag). Set strict=False to continue anyway.")
            print("=" * 80)
            print()
            
            raise RuntimeError(
                f"Units mismatch sanity check failed in strict mode: "
                f"chi2/dof={chi2_per_dof:.2e}, median(|diff/sigma|)={median_abs_res:.2e}. "
                f"Observation and model files are incompatible. "
                f"See output above for diagnostic guidance."
            )
        elif is_catastrophic and not strict:
            # Warn but don't fail if strict=False
            print("⚠ STRICT MODE DISABLED: Continuing despite catastrophic chi2.")
            print("  This run is for DEBUGGING ONLY and results are NOT court-grade.")
            print()
    else:
        metadata['units_mismatch_warning'] = False
    
    metadata['chi2_per_dof'] = float(chi2_per_dof)
    metadata['sanity_checks_passed'] = not is_catastrophic
    metadata['strict_mode'] = strict
    
    return residuals, metadata


def fit_sinusoid_linear(ell, residuals, period):
    """
    Fit sinusoid r_ℓ ≈ A sin(2πℓ/Δℓ + φ) using linear regression.
    
    Parameterize as: r_ℓ = a cos(2πℓ/Δℓ) + b sin(2πℓ/Δℓ)
    Then: A = √(a² + b²), φ = arctan2(a, b)
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    residuals : array-like
        Residual values
    period : float
        Period Δℓ to fit
    
    Returns
    -------
    amplitude : float
        Fitted amplitude A
    phase : float
        Fitted phase φ (radians)
    chi2_fit : float
        χ² of fit (sum of squared residuals after removing sinusoid)
    """
    # Design matrix: [cos(2πℓ/Δℓ), sin(2πℓ/Δℓ)]
    theta = 2.0 * np.pi * ell / period
    X = np.column_stack([np.cos(theta), np.sin(theta)])
    
    # Least squares: solve X^T X β = X^T y
    # Using numpy for numerical stability
    beta, _, _, _ = np.linalg.lstsq(X, residuals, rcond=None)
    a, b = beta
    
    # Convert to amplitude and phase
    amplitude = np.sqrt(a**2 + b**2)
    phase = np.arctan2(a, b)
    
    # Compute χ² of fit
    fit = a * np.cos(theta) + b * np.sin(theta)
    chi2_fit = np.sum((residuals - fit)**2)
    
    return amplitude, phase, chi2_fit


def compute_delta_chi2(ell, residuals, period):
    """
    Compute Δχ² improvement from adding sinusoid.
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    residuals : array-like
        Residual values
    period : float
        Period Δℓ to test
    
    Returns
    -------
    delta_chi2 : float
        Δχ² = χ²(H0) - χ²(H1)
    amplitude : float
        Best-fit amplitude
    phase : float
        Best-fit phase
    """
    # H0: no sinusoid, χ² = sum of squared residuals
    chi2_h0 = np.sum(residuals**2)
    
    # H1: with sinusoid
    amplitude, phase, chi2_h1 = fit_sinusoid_linear(ell, residuals, period)
    
    # Improvement
    delta_chi2 = chi2_h0 - chi2_h1
    
    return delta_chi2, amplitude, phase


def generate_null_residuals(ell, sigma, cov=None, null_type='diagonal_gaussian'):
    """
    Generate null residuals for Monte Carlo simulations.
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    sigma : array-like
        Diagonal uncertainties
    cov : array-like, optional
        Full covariance matrix
    null_type : str
        Type of null to generate:
        - 'diagonal_gaussian': Independent N(0,1) (for diagonal whitening)
        - 'cov_gaussian': Multivariate N(0, Cov) then whiten (for covariance whitening)
    
    Returns
    -------
    null_residuals : ndarray
        Generated null residuals (already normalized/whitened)
    """
    n = len(ell)
    
    if null_type == 'diagonal_gaussian':
        # Independent Gaussian N(0, 1)
        # This is appropriate for diagonal whitening
        return np.random.normal(0, 1, size=n)
    
    elif null_type == 'cov_gaussian':
        # Multivariate Gaussian N(0, Cov), then whiten
        # This calibrates the covariance whitening
        if cov is None:
            # Fall back to diagonal if no covariance
            return np.random.normal(0, 1, size=n)
        
        # Generate multivariate Gaussian x ~ N(0, Cov)
        # using Cholesky: x = L * z where z ~ N(0, I)
        try:
            L = np.linalg.cholesky(cov)
            z = np.random.normal(0, 1, size=n)
            x = L @ z
            
            # Now whiten: r = L^-1 x = L^-1 (L z) = z
            # So the whitened residuals should be ~ N(0, I)
            residuals_whitened = np.linalg.solve(L, x)
            return residuals_whitened
        
        except np.linalg.LinAlgError:
            # If covariance is not positive definite, fall back
            return np.random.normal(0, 1, size=n)
    
    else:
        raise ValueError(f"Unknown null_type: {null_type}")


def monte_carlo_null_distribution(ell, sigma, candidate_periods, n_trials=N_MC_TRIALS, 
                                  random_seed=None, cov=None, null_type='diagonal_gaussian'):
    """
    Generate null distribution of max(Δχ²) under H0.
    
    For each trial:
    1. Generate null residuals (Gaussian, optionally from covariance)
    2. Compute Δχ² for all candidate periods
    3. Record maximum
    
    This implements look-elsewhere correction via max statistic.
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    sigma : array-like
        Uncertainties (same shape as residuals)
    candidate_periods : list
        List of periods to test
    n_trials : int
        Number of Monte Carlo trials
    random_seed : int, optional
        Random seed for reproducibility. If None, uses RANDOM_SEED global.
    cov : array-like, optional
        Full covariance matrix (for cov_gaussian null type)
    null_type : str
        Type of null to generate: 'diagonal_gaussian' or 'cov_gaussian'
    
    Returns
    -------
    max_delta_chi2_null : ndarray
        Distribution of max(Δχ²) under H0 (shape: n_trials)
    """
    if random_seed is None:
        random_seed = RANDOM_SEED
    np.random.seed(random_seed)
    
    max_delta_chi2_null = np.zeros(n_trials)
    
    for i in range(n_trials):
        # Generate null residuals based on null_type
        null_residuals = generate_null_residuals(ell, sigma, cov=cov, null_type=null_type)
        
        # Compute Δχ² for all candidate periods
        delta_chi2_values = []
        for period in candidate_periods:
            delta_chi2, _, _ = compute_delta_chi2(ell, null_residuals, period)
            delta_chi2_values.append(delta_chi2)
        
        # Record maximum
        max_delta_chi2_null[i] = np.max(delta_chi2_values)
    
    return max_delta_chi2_null


def calibrate_whitening(ell, sigma, cov, n_trials=1000, random_seed=None):
    """
    Calibration test for covariance whitening.
    
    Generates samples from N(0, Cov), whitens them, and checks if the
    whitened residuals have unit variance and near-zero correlation.
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    sigma : array-like
        Diagonal uncertainties
    cov : array-like
        Full covariance matrix
    n_trials : int
        Number of calibration trials (default: 1000)
    random_seed : int, optional
        Random seed for reproducibility
    
    Returns
    -------
    dict
        Calibration diagnostics with keys:
        - 'mean_variance': Mean variance of whitened residuals (should be ~1)
        - 'std_variance': Std of variance across trials
        - 'mean_correlation': Mean off-diagonal correlation (should be ~0)
        - 'max_correlation': Max off-diagonal correlation
        - 'calibration_passed': bool, whether calibration criteria are met
    """
    if random_seed is not None:
        np.random.seed(random_seed)
    
    n = len(ell)
    whitened_samples = np.zeros((n_trials, n))
    
    # Generate samples and whiten
    try:
        L = np.linalg.cholesky(cov)
    except np.linalg.LinAlgError:
        return {
            'mean_variance': np.nan,
            'std_variance': np.nan,
            'mean_correlation': np.nan,
            'max_correlation': np.nan,
            'calibration_passed': False,
            'error': 'Covariance not positive definite'
        }
    
    for i in range(n_trials):
        # Generate x ~ N(0, Cov)
        z = np.random.normal(0, 1, size=n)
        x = L @ z
        
        # Whiten
        x_whitened = np.linalg.solve(L, x)
        whitened_samples[i, :] = x_whitened
    
    # Compute statistics
    # Variance per multipole
    variances = np.var(whitened_samples, axis=0)
    mean_variance = np.mean(variances)
    std_variance = np.std(variances)
    
    # Correlation matrix
    corr_matrix = np.corrcoef(whitened_samples.T)
    # Extract off-diagonal elements
    n_ell = corr_matrix.shape[0]
    off_diag_mask = ~np.eye(n_ell, dtype=bool)
    off_diag_corr = corr_matrix[off_diag_mask]
    mean_correlation = np.mean(np.abs(off_diag_corr))
    max_correlation = np.max(np.abs(off_diag_corr))
    
    # Calibration criteria
    # Variance should be close to 1 (within 10%)
    # Correlations should be small (< 0.1)
    variance_ok = abs(mean_variance - 1.0) < 0.1
    correlation_ok = mean_correlation < 0.1
    
    calibration_passed = variance_ok and correlation_ok
    
    diagnostics = {
        'mean_variance': float(mean_variance),
        'std_variance': float(std_variance),
        'mean_correlation': float(mean_correlation),
        'max_correlation': float(max_correlation),
        'calibration_passed': calibration_passed,
        'n_trials': n_trials
    }
    
    return diagnostics


def compute_p_value(observed_max, null_distribution):
    """
    Compute p-value from empirical null distribution.
    
    P-value = fraction of null trials with statistic ≥ observed
    
    Parameters
    ----------
    observed_max : float
        Observed max(Δχ²)
    null_distribution : array-like
        MC null distribution of max(Δχ²)
    
    Returns
    -------
    p_value : float
        Empirical p-value
    """
    n_trials = len(null_distribution)
    n_exceed = np.sum(null_distribution >= observed_max)
    p_value = n_exceed / n_trials
    
    # Ensure p-value is not exactly zero (limited by MC trials)
    if p_value == 0:
        p_value = 1.0 / n_trials  # Upper limit
    
    return p_value


def run_cmb_comb_test(ell, C_obs, C_model, sigma, output_dir=None, cov=None, dataset_name="Unknown",
                      variant="C", n_mc_trials=None, random_seed=None, whiten_mode='diagonal',
                      cov_jitter=1e-12, cov_method='cholesky', strict=True):
    """
    Run full CMB comb test protocol.
    
    Parameters
    ----------
    ell : array-like
        Multipole moments
    C_obs : array-like
        Observed power spectrum
    C_model : array-like
        ΛCDM model prediction
    sigma : array-like
        Uncertainties
    output_dir : str or Path, optional
        Directory to save output files
    cov : array-like, optional
        Full covariance matrix (if available, enables whitening)
    dataset_name : str
        Dataset identifier for provenance
    variant : str, optional
        Architecture variant to test ("A", "B", "C", or "D"). Default: "C"
    n_mc_trials : int, optional
        Number of Monte Carlo trials. If None, uses N_MC_TRIALS global.
    random_seed : int, optional
        Random seed for reproducibility. If None, uses RANDOM_SEED global.
    whiten_mode : str, optional
        Whitening mode: 'none', 'diag', 'diagonal', 'covariance', 'full', or 'block-diagonal'. Default: 'diagonal'
        Note: 'diag' and 'diagonal' are equivalent, as are 'covariance' and 'full'
    cov_jitter : float, optional
        Regularization jitter for covariance matrix (default: 1e-12)
    cov_method : str, optional
        Covariance factorization method: 'cholesky' or 'eigh' (default: 'cholesky')
    strict : bool, optional
        Enable strict mode for court-grade runs. If True, raises RuntimeError on
        catastrophic units mismatch. Default: True for real data.
    
    Returns
    -------
    results : dict
        Dictionary containing:
        - 'best_period': Best-fit period Δℓ
        - 'amplitude': Best-fit amplitude
        - 'phase': Best-fit phase
        - 'max_delta_chi2': Observed max(Δχ²)
        - 'p_value': P-value
        - 'significance': 'null', 'candidate', or 'strong'
        - 'null_distribution': MC null distribution (for plotting)
        - 'whitened': whether covariance whitening was used
        - 'whiten_mode': whitening mode used
        - 'dataset': dataset name
        - 'architecture_variant': variant tested
        - 'variant_valid': whether variant is appropriate for this test
    """
    # Use provided parameters or fall back to globals
    if n_mc_trials is None:
        n_mc_trials = N_MC_TRIALS
    if random_seed is None:
        random_seed = RANDOM_SEED
    
    # Validate variant
    if variant not in ["A", "B", "C", "D"]:
        raise ValueError(f"Invalid variant: {variant}. Must be one of: A, B, C, D")
    
    # Step 1: Compute residuals (with whitening based on mode)
    print(f"Whitening mode: {whiten_mode}")
    
    # Normalize whitening mode names (handle both old and new conventions)
    whiten_mode_normalized = whiten_mode
    if whiten_mode in ['diag', 'diagonal']:
        whiten_mode_normalized = 'diagonal'
    elif whiten_mode in ['full', 'covariance']:
        whiten_mode_normalized = 'covariance'
    
    # Determine if this is effectively whitened
    whitened = (whiten_mode_normalized in ['covariance', 'cov_diag', 'block-diagonal'] and 
                (cov is not None or whiten_mode_normalized == 'block-diagonal'))
    
    # For the new 'full' mode, we need to handle it specially
    if whiten_mode in ['full', 'covariance'] and cov is None:
        raise ValueError(
            f"Whitening mode '{whiten_mode}' requires covariance matrix, but cov=None. "
            f"Provide a covariance matrix or use --whiten diag."
        )
    
    residuals, whiten_metadata = compute_residuals(
        ell, C_obs, C_model, sigma, cov, 
        whiten_mode=whiten_mode_normalized,
        cov_jitter=cov_jitter,
        cov_method=cov_method,
        strict=strict
    )
    
    # Hard validity gate: if sanity checks failed, do NOT compute significance as candidate/strong.
    # Court-grade requirement: invalid scaling cannot produce a "signal".
    if not whiten_metadata.get('sanity_checks_passed', True):
        results = {
            'best_period': None,
            'amplitude': None,
            'phase': None,
            'max_delta_chi2': None,
            'p_value': None,
            'significance': 'invalid',
            'null_distribution': None,
            'residuals': residuals,
            'ell': ell,
            'all_periods': {},
            'whitened': whitened,
            'whiten_mode': whiten_mode,
            'whitening_metadata': whiten_metadata,
            'calibration_diagnostics': calibration_diagnostics,
            'dataset': dataset_name,
            'architecture_variant': variant,
            'variant_valid': (variant == "C"),
            'n_mc_trials': n_mc_trials,
            'random_seed': random_seed
        }
        print("\n" + "="*60)
        print("CMB COMB TEST RESULTS")
        print("="*60)
        print(f"Dataset: {dataset_name}")
        print(f"Whitening mode: {whiten_mode}")
        print("Significance: INVALID")
        print("Result: INVALID RUN (sanity checks failed: units/model mismatch or sigma failure)")
        print("="*60 + "\n")
        return results
    
    # Calibration test for covariance whitening
    calibration_diagnostics = None
    if whiten_mode == 'covariance' and cov is not None:
        print("Running whitening calibration test...")
        calibration_diagnostics = calibrate_whitening(ell, sigma, cov, n_trials=1000, random_seed=random_seed)
        print(f"  Mean variance: {calibration_diagnostics['mean_variance']:.4f} (expected: 1.0)")
        print(f"  Mean |correlation|: {calibration_diagnostics['mean_correlation']:.4f} (expected: ~0)")
        if calibration_diagnostics['calibration_passed']:
            print("  ✓ Calibration PASSED")
        else:
            print("  ⚠ Calibration FAILED - whitening may not be working correctly")
        print()
    
    # Step 2: Test all candidate periods
    results_per_period = {}
    for period in CANDIDATE_PERIODS:
        delta_chi2, amplitude, phase = compute_delta_chi2(ell, residuals, period)
        results_per_period[period] = {
            'delta_chi2': delta_chi2,
            'amplitude': amplitude,
            'phase': phase
        }
    
    # Step 3: Find maximum Δχ²
    best_period = max(results_per_period.keys(), 
                     key=lambda p: results_per_period[p]['delta_chi2'])
    max_delta_chi2 = results_per_period[best_period]['delta_chi2']
    amplitude = results_per_period[best_period]['amplitude']
    phase = results_per_period[best_period]['phase']
    
    # Step 4: Generate null distribution
    # Determine appropriate null type based on whitening mode
    if whiten_mode == 'covariance' and cov is not None:
        null_type = 'cov_gaussian'
        print(f"Generating null distribution ({n_mc_trials} trials using covariance-aware null)...")
    else:
        null_type = 'diagonal_gaussian'
        print(f"Generating null distribution ({n_mc_trials} trials using diagonal Gaussian null)...")
    
    null_distribution = monte_carlo_null_distribution(
        ell, sigma, CANDIDATE_PERIODS, 
        n_trials=n_mc_trials, 
        random_seed=random_seed,
        cov=cov,
        null_type=null_type
    )
    
    # Step 5: Compute p-value
    p_value = compute_p_value(max_delta_chi2, null_distribution)
    
    # Step 6: Assess significance
    if p_value < THRESHOLD_STRONG:
        significance = 'strong'
    elif p_value < THRESHOLD_CANDIDATE:
        significance = 'candidate'
    else:
        significance = 'null'
    
    # Prepare results
    results = {
        'best_period': best_period,
        'amplitude': amplitude,
        'phase': phase,
        'max_delta_chi2': max_delta_chi2,
        'p_value': p_value,
        'significance': significance,
        'null_distribution': null_distribution,
        'residuals': residuals,
        'ell': ell,
        'all_periods': results_per_period,
        'whitened': whitened,
        'whiten_mode': whiten_mode,
        'whitening_metadata': whiten_metadata,
        'calibration_diagnostics': calibration_diagnostics,
        'dataset': dataset_name,
        'architecture_variant': variant,
        'variant_valid': (variant == "C"),
        'n_mc_trials': n_mc_trials,
        'random_seed': random_seed
    }
    
    # Print summary
    print("\n" + "="*60)
    print("CMB COMB TEST RESULTS")
    print("="*60)
    print(f"Dataset: {dataset_name}")
    print(f"Whitening mode: {whiten_mode}")
    print(f"Best period: Δℓ = {best_period}")
    print(f"Amplitude: A = {amplitude:.4f}")
    print(f"Phase: φ = {phase:.4f} rad ({np.degrees(phase):.2f}°)")
    print(f"Max Δχ²: {max_delta_chi2:.2f}")
    print(f"P-value: {p_value:.6e}")
    print(f"Significance: {significance.upper()}")
    print("="*60)
    
    if significance == 'null':
        print("Result: No significant periodic signal detected (H0 not rejected)")
    elif significance == 'candidate':
        print("Result: CANDIDATE signal detected - replication required")
    else:
        print("Result: STRONG signal detected - immediate independent verification needed")
    print("="*60 + "\n")
    
    # Save results if output directory provided
    if output_dir is not None:
        save_results(results, output_dir)
    
    return results


def save_results(results, output_dir):
    """
    Save results to output directory.
    
    Parameters
    ----------
    results : dict
        Results dictionary from run_cmb_comb_test
    output_dir : str or Path
        Output directory
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save summary statistics
    with open(output_dir / 'cmb_comb_results.txt', 'w') as f:
        f.write("CMB COMB TEST RESULTS\n")
        f.write("="*60 + "\n")
        f.write(f"Dataset: {results.get('dataset', 'Unknown')}\n")
        f.write(f"Whitening mode: {results.get('whiten_mode', 'diagonal')}\n")
        
        # Add whitening metadata if available
        if 'whitening_metadata' in results and results['whitening_metadata']:
            meta = results['whitening_metadata']
            f.write("\nWhitening Metadata:\n")
            if 'regularization_used' in meta:
                f.write(f"  Regularization used: {meta['regularization_used']}\n")
            if meta.get('regularization_used') and 'lambda_ridge' in meta:
                f.write(f"  Ridge parameter λ: {meta['lambda_ridge']:.6e}\n")
            if 'cov_metadata' in meta and meta['cov_metadata']:
                cov_meta = meta['cov_metadata']
                if isinstance(cov_meta, dict) and 'condition_number' in cov_meta:
                    f.write(f"  Covariance condition number: {cov_meta['condition_number']:.6e}\n")
                    f.write(f"  Min eigenvalue: {cov_meta['min_eigenvalue']:.6e}\n")
                    f.write(f"  Max eigenvalue: {cov_meta['max_eigenvalue']:.6e}\n")
                    f.write(f"  Symmetric: {cov_meta['is_symmetric']}\n")
                    f.write(f"  Positive definite: {cov_meta['is_positive_definite']}\n")
                    if 'ell_range' in cov_meta:
                        f.write(f"  ℓ-range compatibility: {cov_meta['ell_range']}\n")
        
        f.write(f"\nBest period: Δℓ = {results['best_period']}\n")
        f.write(f"Amplitude: A = {results['amplitude']:.6f}\n")
        f.write(f"Phase: φ = {results['phase']:.6f} rad\n")
        f.write(f"Max Δχ²: {results['max_delta_chi2']:.6f}\n")
        f.write(f"P-value: {results['p_value']:.6e}\n")
        f.write(f"Significance: {results['significance']}\n")
        f.write(f"Random seed: {results.get('random_seed', RANDOM_SEED)}\n")
        f.write(f"MC trials: {results.get('n_mc_trials', N_MC_TRIALS)}\n")
        f.write(f"Architecture variant: {results.get('architecture_variant', 'C')}\n")
        f.write(f"Variant valid: {results.get('variant_valid', True)}\n")
    
    # Save null distribution
    np.savetxt(output_dir / 'null_distribution.txt', results['null_distribution'],
               header='Max Δχ² values under H0 (null hypothesis)')
    
    # Save residuals and fitted sinusoid
    ell = results['ell']
    residuals = results['residuals']
    period = results['best_period']
    amplitude = results['amplitude']
    phase = results['phase']
    
    theta = 2.0 * np.pi * ell / period
    fitted_sinusoid = amplitude * np.sin(theta + phase)
    
    np.savetxt(output_dir / 'residuals_and_fit.txt',
               np.column_stack([ell, residuals, fitted_sinusoid]),
               header='ℓ   residual   fitted_sinusoid')
    
    print(f"Results saved to {output_dir}")


def plot_results(results, output_dir):
    """
    Generate diagnostic plots (requires matplotlib).
    
    Parameters
    ----------
    results : dict
        Results dictionary from run_cmb_comb_test
    output_dir : str or Path
        Output directory
    """
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Matplotlib not available - skipping plots")
        return
    
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Plot 1: Residuals with fitted sinusoid
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ell = results['ell']
    residuals = results['residuals']
    period = results['best_period']
    amplitude = results['amplitude']
    phase = results['phase']
    
    theta = 2.0 * np.pi * ell / period
    fitted_sinusoid = amplitude * np.sin(theta + phase)
    
    ax.scatter(ell, residuals, s=10, alpha=0.5, label='Residuals')
    ax.plot(ell, fitted_sinusoid, 'r-', linewidth=2, 
            label=f'Best fit (Δℓ={period}, A={amplitude:.3f})')
    ax.axhline(0, color='k', linestyle='--', alpha=0.3)
    ax.set_xlabel('Multipole ℓ')
    ax.set_ylabel('Normalized Residual')
    ax.set_title('CMB Power Spectrum Residuals with Fitted Comb')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'residuals_with_fit.png', dpi=150)
    plt.close()
    
    # Plot 2: Null distribution histogram
    fig, ax = plt.subplots(figsize=(10, 6))
    
    null_dist = results['null_distribution']
    max_delta_chi2 = results['max_delta_chi2']
    p_value = results['p_value']
    
    ax.hist(null_dist, bins=50, alpha=0.7, edgecolor='black', label='H0 null distribution')
    ax.axvline(max_delta_chi2, color='r', linestyle='--', linewidth=2,
               label=f'Observed (p={p_value:.4e})')
    ax.set_xlabel('max(Δχ²)')
    ax.set_ylabel('Frequency')
    ax.set_title('Monte Carlo Null Distribution of max(Δχ²)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'null_distribution.png', dpi=150)
    plt.close()
    
    print(f"Plots saved to {output_dir}")


def load_data(obs_file, model_file, cov_file=None):
    """
    Load CMB data from files.
    
    Expected format: Text files with columns [ell, C_ell, sigma_ell]
    
    Parameters
    ----------
    obs_file : str or Path
        Observed power spectrum file
    model_file : str or Path
        Model prediction file
    cov_file : str or Path, optional
        Covariance file (if None, use diagonal sigma)
    
    Returns
    -------
    ell : ndarray
        Multipole moments
    C_obs : ndarray
        Observed power spectrum
    C_model : ndarray
        Model prediction
    sigma : ndarray
        Uncertainties
    """
    # Load observed data
    obs_data = np.loadtxt(obs_file)
    ell_obs = obs_data[:, 0].astype(int)
    C_obs = obs_data[:, 1]
    sigma_obs = obs_data[:, 2] if obs_data.shape[1] > 2 else None
    
    # Load model data
    model_data = np.loadtxt(model_file)
    ell_model = model_data[:, 0].astype(int)
    C_model = model_data[:, 1]
    
    # Ensure ell arrays match
    if not np.array_equal(ell_obs, ell_model):
        raise ValueError("Multipole ranges in obs and model files don't match")
    
    ell = ell_obs
    
    # Handle uncertainties
    if sigma_obs is not None:
        sigma = sigma_obs
    elif cov_file is not None:
        # Load covariance and extract diagonal
        cov = np.loadtxt(cov_file)
        sigma = np.sqrt(np.diag(cov))
    else:
        raise ValueError("Must provide sigma in obs file or covariance file")
    
    return ell, C_obs, C_model, sigma


def check_input_file_exists(filepath, file_description="Input file"):
    """
    Check if an input file exists and provide helpful error message if not.
    
    Parameters
    ----------
    filepath : str or Path
        Path to file to check
    file_description : str
        Description of the file (e.g., "Observation file")
    
    Raises
    ------
    SystemExit
        If file doesn't exist (exits with helpful error message)
    """
    if filepath is None:
        return  # Optional file not provided
    
    filepath = Path(filepath)
    
    if not filepath.exists():
        print("=" * 80)
        print(f"ERROR: {file_description} not found!")
        print("=" * 80)
        print(f"Looking for: {filepath}")
        print(f"Absolute path: {filepath.resolve()}")
        print("")
        print(f"Current working directory: {Path.cwd()}")
        print("")
        
        # Try to find similar files in the expected directory
        if filepath.parent.exists():
            print(f"Files in {filepath.parent}:")
            try:
                # List files matching PowerSpect and TT patterns (for Planck data)
                parent_files = list(filepath.parent.iterdir())
                matching_files = [f for f in parent_files 
                                if f.is_file() and 
                                   ('PowerSpect' in f.name or 'TT' in f.name or 
                                    'spectrum' in f.name.lower() or 'model' in f.name.lower())]
                
                if matching_files:
                    print("  Found potentially relevant files:")
                    for f in sorted(matching_files):
                        print(f"    - {f.name}")
                else:
                    print("  No matching PowerSpect/TT/spectrum files found.")
                    print(f"  Total files in directory: {len([f for f in parent_files if f.is_file()])}")
            except Exception as e:
                print(f"  (Unable to list files: {e})")
        else:
            print(f"Directory does not exist: {filepath.parent}")
        
        print("")
        print("=" * 80)
        print("SUGGESTIONS:")
        print("=" * 80)
        print("")
        print("1. Download the required data files:")
        print("   bash tools/data_download/download_planck_pr3_cosmoparams.sh")
        print("")
        print("2. Verify the filename matches the downloaded file:")
        print("   Expected Planck PR3 files:")
        print("   - COM_PowerSpect_CMB-TT-full_R3.01.txt  (observation)")
        print("   - COM_PowerSpect_CMB-TT-model_R3.01.txt (model)")
        print("")
        print("3. Check the path is correct relative to your current directory")
        print("")
        print("4. See forensic_fingerprint/RUNBOOK_REAL_DATA.md for complete instructions")
        print("")
        print("=" * 80)
        sys.exit(1)


def main():
    """
    Main function for command-line usage with enhanced dataset support.
    """
    # =============================================================================
    # COMMAND LINE ARGUMENT PARSING
    # =============================================================================
    
    parser = argparse.ArgumentParser(
        description="UBT Forensic Fingerprint - CMB Comb Test",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Legacy mode (synthetic data):
  python cmb_comb.py obs.txt model.txt output/
  
  # Real data mode (Planck PR3):
  python cmb_comb.py --dataset planck_pr3 \\
      --input_obs data/planck_pr3/raw/spectrum.txt \\
      --input_model data/planck_pr3/raw/model.txt \\
      --ell_min 30 --ell_max 1500
  
  # Real data mode (WMAP):
  python cmb_comb.py --dataset wmap \\
      --input_obs data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt \\
      --ell_min 30 --ell_max 800

See forensic_fingerprint/RUNBOOK_REAL_DATA.md for complete instructions.
        """
    )
    
    # Dataset selection
    parser.add_argument(
        '--dataset',
        type=str,
        choices=['planck_pr3', 'wmap', 'custom'],
        help='Dataset to use (planck_pr3, wmap, or custom for legacy mode)'
    )
    
    # Input files
    parser.add_argument(
        '--input_obs',
        type=str,
        help='Path to observed power spectrum file'
    )
    
    parser.add_argument(
        '--input_model',
        type=str,
        help='Path to theoretical model file'
    )
    
    parser.add_argument(
        '--input_cov',
        type=str,
        help='Path to covariance matrix file (optional, enables whitening)'
    )
    
    # Multipole range
    parser.add_argument(
        '--ell_min',
        type=int,
        help='Minimum multipole to include in analysis'
    )
    
    parser.add_argument(
        '--ell_max',
        type=int,
        help='Maximum multipole to include in analysis'
    )
    
    # Output
    parser.add_argument(
        '--output_dir',
        type=str,
        help='Output directory for results (default: auto-generated)'
    )
    
    # Whitening mode
    parser.add_argument(
        '--whiten',
        type=str,
        choices=['none', 'diagonal', 'covariance', 'cov_diag', 'block-diagonal'],
        default='diagonal',
        help='Whitening mode: none (no whitening), diagonal (default, use diagonal uncertainties), '
             'covariance (full covariance matrix), cov_diag (diagonal from covariance matrix), '
             'block-diagonal (approximate covariance)'
    )
    
    # Legacy positional arguments for backward compatibility
    parser.add_argument(
        'obs_file',
        nargs='?',
        help='[LEGACY] Observed spectrum file'
    )
    
    parser.add_argument(
        'model_file',
        nargs='?',
        help='[LEGACY] Model spectrum file'
    )
    
    parser.add_argument(
        'legacy_output_dir',
        nargs='?',
        help='[LEGACY] Output directory'
    )
    
    args = parser.parse_args()
    
    # =============================================================================
    # VARIANT VALIDATION
    # =============================================================================
    
    print("=" * 80)
    print("UBT Forensic Fingerprint - CMB Comb Test")
    print("=" * 80)
    print(f"Architecture Variant: {ARCHITECTURE_VARIANT}")
    print("")
    
    # Validate variant selection
    if ARCHITECTURE_VARIANT not in ["A", "B", "C", "D"]:
        raise ValueError(
            f"Invalid ARCHITECTURE_VARIANT: {ARCHITECTURE_VARIANT}\n"
            "Must be one of: 'A', 'B', 'C', 'D'\n"
            "See ../ARCHITECTURE_VARIANTS.md for definitions"
        )
    
    # Warn if not Variant C
    if ARCHITECTURE_VARIANT != "C":
        print("WARNING: CMB comb test is ONLY valid under Variant C assumptions")
        print("         (Explicit Frame Synchronization with RS code structure)")
        print("")
        print(f"Variant {ARCHITECTURE_VARIANT} predicts:")
        
        if ARCHITECTURE_VARIANT == "A":
            print("  - No periodic structure (continuous-time)")
            print("  - Expected result: NULL (p > 0.05)")
        elif ARCHITECTURE_VARIANT == "B":
            print("  - Broad-band cutoff but NO periodicity")
            print("  - Expected result: NULL for comb test (p > 0.05)")
        elif ARCHITECTURE_VARIANT == "D":
            print("  - Scale-dependent decoherence of periodicity")
            print("  - Expected result: Depends on scale (requires binning)")
        
        print("")
        print("Proceeding with test for validation/null-hypothesis purposes only.")
        print("Results will be labeled as 'VARIANT MISMATCH' if signal found.")
        print("")
    else:
        print("Variant C: Explicit Frame Synchronization")
        print("Hypothesis: CMB residuals contain periodic comb structure")
        print("           at periods tied to RS code length (255 or divisors)")
        print("")
    
    print("=" * 80)
    print("")
    
    # =============================================================================
    # DETERMINE MODE: REAL DATA vs LEGACY
    # =============================================================================
    
    # Check if using new dataset mode or legacy mode
    if args.dataset is not None:
        # New dataset mode
        mode = 'real_data'
        
        if args.input_obs is None:
            parser.error("--input_obs is required when using --dataset")
        
        # Check input files exist before attempting to load
        check_input_file_exists(args.input_obs, "Observation file")
        check_input_file_exists(args.input_model, "Model file")
        check_input_file_exists(args.input_cov, "Covariance file")
        
        # Load data using appropriate loader
        print(f"Loading {args.dataset.upper()} data...")
        
        # Import loaders
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'loaders'))
        
        if args.dataset == 'planck_pr3':
            from planck import load_planck_data
            data = load_planck_data(
                obs_file=args.input_obs,
                model_file=args.input_model,
                cov_file=args.input_cov,
                ell_min=args.ell_min,
                ell_max=args.ell_max,
                dataset_name="Planck PR3"
            )
        elif args.dataset == 'wmap':
            from wmap import load_wmap_data
            data = load_wmap_data(
                obs_file=args.input_obs,
                model_file=args.input_model,
                cov_file=args.input_cov,
                ell_min=args.ell_min,
                ell_max=args.ell_max,
                dataset_name="WMAP 9yr"
            )
        else:  # custom
            # For custom datasets, try planck loader first
            from planck import load_planck_data
            data = load_planck_data(
                obs_file=args.input_obs,
                model_file=args.input_model,
                cov_file=args.input_cov,
                ell_min=args.ell_min,
                ell_max=args.ell_max,
                dataset_name="Custom"
            )
        
        print(f"Loaded {data['n_multipoles']} multipoles from ℓ = {data['ell_range'][0]} to {data['ell_range'][1]}")
        
        ell = data['ell']
        C_obs = data['cl_obs']
        C_model = data['cl_model'] if data['cl_model'] is not None else C_obs * 0  # Dummy if no model
        sigma = data['sigma']
        cov = data['cov']
        dataset_name = data['dataset']
        
        if C_model is None or np.all(C_model == 0):
            print("WARNING: No model provided. Using zero residuals (test will be NULL).")
        
        # Generate output directory with timestamp
        if args.output_dir:
            output_dir = Path(args.output_dir)
        else:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_dir = Path(__file__).parent.parent / 'out' / 'cmb_comb' / f"{args.dataset}_{timestamp}"
        
    else:
        # Legacy mode (backward compatibility)
        mode = 'legacy'
        
        if args.obs_file is None or args.model_file is None:
            print("ERROR: Must provide either --dataset mode or legacy positional arguments")
            print("")
            parser.print_help()
            sys.exit(1)
        
        print("Using LEGACY mode (synthetic/test data)")
        print("")
        
        obs_file = args.obs_file
        model_file = args.model_file
        output_dir = args.legacy_output_dir if args.legacy_output_dir else Path(__file__).parent.parent / 'out'
        
        # Check input files exist before attempting to load
        check_input_file_exists(obs_file, "Observation file")
        check_input_file_exists(model_file, "Model file")
        
        # Load data using legacy function
        print(f"Loading data from {obs_file} and {model_file}...")
        ell, C_obs, C_model, sigma = load_data(obs_file, model_file)
        cov = None
        dataset_name = "Legacy"
        
        print(f"Loaded {len(ell)} multipoles (ℓ = {ell[0]} to {ell[-1]})")
    
    # =============================================================================
    # RUN CMB COMB TEST
    # =============================================================================
    
    # Determine whitening mode based on flags
    whiten_mode = args.whiten if hasattr(args, 'whiten') else 'diagonal'
    
    # Run test
    results = run_cmb_comb_test(
        ell, C_obs, C_model, sigma,
        output_dir=output_dir,
        cov=cov,
        dataset_name=dataset_name,
        whiten_mode=whiten_mode
    )
    
    # Add variant metadata to results
    results['architecture_variant'] = ARCHITECTURE_VARIANT
    results['variant_valid'] = (ARCHITECTURE_VARIANT == "C")
    results['mode'] = mode
    
    # Interpretation with variant awareness
    print("")
    print("=" * 80)
    print("INTERPRETATION")
    print("=" * 80)
    if results['variant_valid']:
        print(f"Variant C test: {results['significance']}")
    else:
        print(f"Variant {ARCHITECTURE_VARIANT} test (NULL expected):")
        print(f"  Result: {results['significance']}")
        if results['p_value'] < THRESHOLD_CANDIDATE:
            print("  ⚠ UNEXPECTED: Signal found in variant that predicts NULL")
            print("               Requires investigation or variant re-evaluation")
    print("=" * 80)
    
    # Generate plots if matplotlib available
    plot_results(results, output_dir)
    
    return results


if __name__ == '__main__':
    main()
