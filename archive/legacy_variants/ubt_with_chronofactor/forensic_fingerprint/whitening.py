#!/usr/bin/env python3
"""
Whitening Transformations for Court-Grade CMB Analysis
=======================================================

This module provides numerically stable whitening transformations for CMB residuals
with full covariance support. It implements both Cholesky and eigenvalue-based methods.

**Key Concepts**:

1. **Whitening**: Transform correlated residuals r ~ N(0, Cov) into uncorrelated w ~ N(0, I)
2. **Methods**:
   - Cholesky: Fast, numerically stable for well-conditioned matrices
   - Eigenvalue: More robust for ill-conditioned matrices
3. **Monte Carlo**: Null samples must be generated and whitened consistently

**Important**: Both observed residuals AND Monte Carlo samples must be whitened
identically to ensure valid p-value computation.

License: MIT
Author: UBT Research Team
"""

import numpy as np
import warnings


def build_whitener(cov, method='cholesky', jitter=1e-12):
    """
    Build whitening transformation function.
    
    This returns a function that whitens residuals by transforming
    r ~ N(0, Cov) → w ~ N(0, I).
    
    Parameters
    ----------
    cov : ndarray
        Covariance matrix (N x N), must be symmetric positive definite
    method : str
        Whitening method: 'cholesky' or 'eigh'
        - 'cholesky': L @ L.T = Cov, whiten(r) = solve(L, r)
        - 'eigh': Cov = V @ diag(λ) @ V.T, whiten(r) = V.T @ r / sqrt(λ)
    jitter : float
        Regularization added to diagonal before factorization (default: 1e-12)
    
    Returns
    -------
    whiten : callable
        Function that whitens residuals: whiten(r) -> r_whitened
    metadata : dict
        Whitening metadata with keys:
        - method: str
        - jitter: float
        - condition_number_before: float
        - condition_number_after: float
        - min_eigenvalue_before: float
        - min_eigenvalue_after: float
    
    Raises
    ------
    ValueError
        If covariance is invalid or factorization fails
    """
    cov = np.asarray(cov)
    
    if cov.ndim != 2 or cov.shape[0] != cov.shape[1]:
        raise ValueError(f"Covariance must be square 2D array, got shape {cov.shape}")
    
    # Check symmetry
    if not np.allclose(cov, cov.T, rtol=1e-10, atol=1e-12):
        raise ValueError("Covariance matrix must be symmetric")
    
    # Compute eigenvalues for diagnostics
    eigs_before = np.linalg.eigvalsh(cov)
    min_eig_before = np.min(eigs_before)
    max_eig_before = np.max(eigs_before)
    cond_before = max_eig_before / max(min_eig_before, 1e-20)
    
    # Apply jitter regularization
    cov_reg = cov + jitter * np.eye(cov.shape[0])
    
    eigs_after = np.linalg.eigvalsh(cov_reg)
    min_eig_after = np.min(eigs_after)
    max_eig_after = np.max(eigs_after)
    cond_after = max_eig_after / min_eig_after
    
    metadata = {
        'method': method,
        'jitter': float(jitter),
        'condition_number_before': float(cond_before),
        'condition_number_after': float(cond_after),
        'min_eigenvalue_before': float(min_eig_before),
        'min_eigenvalue_after': float(min_eig_after),
        'max_eigenvalue': float(max_eig_after)
    }
    
    if method == 'cholesky':
        # Cholesky factorization: Cov = L @ L.T
        try:
            L = np.linalg.cholesky(cov_reg)
        except np.linalg.LinAlgError as e:
            raise ValueError(
                f"Cholesky decomposition failed even after jitter={jitter:.2e}\n"
                f"Min eigenvalue: {min_eig_after:.6e}\n"
                f"Condition number: {cond_after:.6e}\n\n"
                f"Try:\n"
                f"  1. Increase --cov_jitter (current: {jitter:.2e})\n"
                f"  2. Use --cov_method eigh instead\n"
                f"  3. Verify covariance matrix is valid"
            ) from e
        
        def whiten(r):
            """Whiten residuals using Cholesky solve: w = L^{-1} r"""
            r = np.asarray(r)
            if len(r) != L.shape[0]:
                raise ValueError(f"Residual length {len(r)} doesn't match covariance size {L.shape[0]}")
            return np.linalg.solve(L, r)
        
        metadata['factorization'] = 'cholesky'
        
    elif method == 'eigh':
        # Eigenvalue decomposition: Cov = V @ diag(λ) @ V.T
        eigenvalues, eigenvectors = np.linalg.eigh(cov_reg)
        
        # Whitening: w = V.T @ r / sqrt(λ)
        sqrt_inv_eigs = 1.0 / np.sqrt(eigenvalues)
        
        def whiten(r):
            """Whiten residuals using eigenvalue decomposition"""
            r = np.asarray(r)
            if len(r) != eigenvectors.shape[0]:
                raise ValueError(f"Residual length {len(r)} doesn't match covariance size {eigenvectors.shape[0]}")
            # w = V.T @ r / sqrt(λ)
            return (eigenvectors.T @ r) * sqrt_inv_eigs
        
        metadata['factorization'] = 'eigh'
        metadata['smallest_eigenvalue'] = float(np.min(eigenvalues))
        
    else:
        raise ValueError(f"Unknown whitening method: {method}. Use 'cholesky' or 'eigh'.")
    
    return whiten, metadata


def whiten_residuals(residual, cov=None, sigma=None, mode='diag'):
    """
    Whiten residuals using specified mode.
    
    This is the main entry point for whitening in the CMB pipeline.
    
    Parameters
    ----------
    residual : array-like
        Residual vector r = obs - model (length N)
    cov : ndarray, optional
        Full covariance matrix (N x N). Required for mode='full'.
    sigma : array-like, optional
        Diagonal uncertainties (length N). Required for mode='diag'.
    mode : str
        Whitening mode:
        - 'none': return residual unchanged
        - 'diag': return residual / sigma (diagonal whitening)
        - 'full': return whiten(residual) using full covariance
    
    Returns
    -------
    whitened : ndarray
        Whitened residuals (length N)
    
    Raises
    ------
    ValueError
        If required inputs are missing or mode is invalid
    
    Notes
    -----
    After whitening, if residual ~ N(0, Cov), then whitened ~ N(0, I).
    Chi-squared: χ² = residual.T @ Cov^{-1} @ residual = ||whitened||²
    """
    residual = np.asarray(residual)
    
    if mode == 'none':
        return residual
    
    elif mode == 'diag':
        if sigma is None:
            raise ValueError("sigma is required for mode='diag'")
        sigma = np.asarray(sigma)
        if len(sigma) != len(residual):
            raise ValueError(f"sigma length {len(sigma)} doesn't match residual length {len(residual)}")
        # Check for zero sigma (would cause division by zero)
        if np.any(sigma <= 0):
            raise ValueError("sigma must be > 0 for diagonal whitening")
        return residual / sigma
    
    elif mode == 'full':
        if cov is None:
            raise ValueError("cov is required for mode='full'")
        cov = np.asarray(cov)
        if cov.shape[0] != len(residual):
            raise ValueError(
                f"Covariance size {cov.shape[0]} doesn't match residual length {len(residual)}"
            )
        
        # Build whitener using Cholesky (default)
        whiten_func, _ = build_whitener(cov, method='cholesky', jitter=1e-12)
        return whiten_func(residual)
    
    else:
        raise ValueError(f"Unknown whitening mode: {mode}. Use 'none', 'diag', or 'full'.")


def generate_mc_null_sample(cov=None, sigma=None, mode='diag', random_state=None):
    """
    Generate Monte Carlo null sample under appropriate null hypothesis.
    
    **CRITICAL**: The null sample generation must match the whitening mode:
    - mode='diag': Generate z ~ N(0, I), return z (already whitened)
    - mode='full': Generate z ~ N(0, I), return z (equivalent to generating
                   x ~ N(0, Cov) and then whitening)
    
    The key insight: For full covariance whitening, we DON'T need to generate
    x ~ N(0, Cov) and then whiten it. We can directly generate z ~ N(0, I)
    because:
        1. True process: x ~ N(0, Cov)
        2. After whitening: w = L^{-1} x ~ N(0, I)
        3. We compare in whitened space, so just generate z ~ N(0, I)
    
    Parameters
    ----------
    cov : ndarray, optional
        Covariance matrix (N x N). Required if mode='full' (but not used directly).
    sigma : array-like, optional
        Diagonal uncertainties (length N). Required if mode='diag'.
    mode : str
        Must match the mode used for observed residuals: 'diag' or 'full'
    random_state : np.random.RandomState, optional
        Random state for reproducibility
    
    Returns
    -------
    null_sample : ndarray
        Null sample in whitened space (length N)
    
    Notes
    -----
    This generates samples that are ALREADY in whitened space, so they can be
    directly compared to whitened observed residuals.
    """
    if random_state is None:
        random_state = np.random.RandomState()
    
    if mode == 'diag':
        if sigma is None:
            raise ValueError("sigma is required for mode='diag'")
        sigma = np.asarray(sigma)
        n = len(sigma)
        # Generate z ~ N(0, I) - already in whitened space
        return random_state.randn(n)
    
    elif mode == 'full':
        if cov is None:
            raise ValueError("cov is required for mode='full'")
        cov = np.asarray(cov)
        n = cov.shape[0]
        # Generate z ~ N(0, I) - this is equivalent to generating N(0, Cov) and whitening
        # because we're comparing in whitened space
        return random_state.randn(n)
    
    else:
        raise ValueError(f"Unknown mode: {mode}. Use 'diag' or 'full'.")


def verify_whitening(cov, n_samples=1000, method='cholesky', jitter=1e-12, random_seed=None):
    """
    Verify whitening transformation produces N(0, I) from N(0, Cov).
    
    This is a diagnostic function to validate the whitening implementation.
    
    Parameters
    ----------
    cov : ndarray
        Covariance matrix to test (N x N)
    n_samples : int
        Number of Monte Carlo samples for verification
    method : str
        Whitening method: 'cholesky' or 'eigh'
    jitter : float
        Regularization parameter
    random_seed : int, optional
        Random seed for reproducibility
    
    Returns
    -------
    results : dict
        Verification results with keys:
        - mean_deviation: Mean of whitened samples (should be ~0)
        - cov_deviation: Deviation of whitened covariance from identity
        - max_off_diagonal: Maximum off-diagonal element in whitened cov
        - mean_variance: Mean variance of whitened samples (should be ~1)
        - passed: bool, True if all checks pass
    """
    rng = np.random.RandomState(random_seed)
    
    # Build whitener
    whiten_func, metadata = build_whitener(cov, method=method, jitter=jitter)
    
    n = cov.shape[0]
    
    # Generate samples from N(0, Cov)
    L_true = np.linalg.cholesky(cov + jitter * np.eye(n))
    samples = []
    whitened_samples = []
    
    for _ in range(n_samples):
        z = rng.randn(n)
        x = L_true @ z  # x ~ N(0, Cov)
        w = whiten_func(x)  # w should be ~ N(0, I)
        samples.append(x)
        whitened_samples.append(w)
    
    samples = np.array(samples)
    whitened_samples = np.array(whitened_samples)
    
    # Check whitened samples
    mean_whitened = np.mean(whitened_samples, axis=0)
    cov_whitened = np.cov(whitened_samples.T)
    
    # Compute deviations
    mean_deviation = np.max(np.abs(mean_whitened))
    cov_deviation = np.max(np.abs(cov_whitened - np.eye(n)))
    
    # Off-diagonal check
    off_diag_mask = ~np.eye(n, dtype=bool)
    max_off_diagonal = np.max(np.abs(cov_whitened[off_diag_mask]))
    
    # Variance check
    variances = np.diag(cov_whitened)
    mean_variance = np.mean(variances)
    
    # Pass criteria (relaxed for finite samples)
    # These thresholds are appropriate for ~1000 samples
    passed = (
        mean_deviation < 0.1 and
        max_off_diagonal < 0.1 and
        0.9 < mean_variance < 1.1
    )
    
    results = {
        'mean_deviation': float(mean_deviation),
        'cov_deviation': float(cov_deviation),
        'max_off_diagonal': float(max_off_diagonal),
        'mean_variance': float(mean_variance),
        'n_samples': n_samples,
        'method': method,
        'jitter': jitter,
        'passed': passed
    }
    
    return results


if __name__ == '__main__':
    """Demonstration and self-test of whitening module."""
    
    print("="*80)
    print("Whitening Module Self-Test")
    print("="*80)
    print()
    
    # Test 1: Identity covariance (should be no-op)
    print("Test 1: Identity covariance (whitening should be no-op)")
    n = 10
    cov_identity = np.eye(n)
    residual = np.random.randn(n)
    
    whitened_chol = whiten_residuals(residual, cov=cov_identity, mode='full')
    
    print(f"  Original residual norm: {np.linalg.norm(residual):.6f}")
    print(f"  Whitened residual norm: {np.linalg.norm(whitened_chol):.6f}")
    print(f"  Difference: {np.linalg.norm(residual - whitened_chol):.6e}")
    
    if np.allclose(residual, whitened_chol, rtol=1e-10):
        print("  ✓ PASS: Identity covariance → no-op")
    else:
        print("  ✗ FAIL: Whitening changed residuals unexpectedly")
    print()
    
    # Test 2: Known covariance
    print("Test 2: Known covariance (verify whitening produces N(0,I))")
    n = 20
    # Create random positive definite covariance
    A = np.random.randn(n, n)
    cov_test = A @ A.T + 0.1 * np.eye(n)  # Ensure PD
    
    results = verify_whitening(cov_test, n_samples=1000, random_seed=42)
    
    print(f"  Mean deviation: {results['mean_deviation']:.6f} (should be ~0)")
    print(f"  Max off-diagonal correlation: {results['max_off_diagonal']:.6f} (should be ~0)")
    print(f"  Mean variance: {results['mean_variance']:.6f} (should be ~1)")
    
    if results['passed']:
        print("  ✓ PASS: Whitening produces N(0,I)")
    else:
        print("  ✗ FAIL: Whitening does not produce N(0,I)")
    print()
    
    # Test 3: Diagonal vs full equivalence for diagonal covariance
    print("Test 3: Diagonal covariance (full whitening should match diagonal)")
    n = 15
    sigma = np.random.uniform(0.5, 2.0, n)
    cov_diag = np.diag(sigma**2)
    residual = np.random.randn(n)
    
    whitened_diag = whiten_residuals(residual, sigma=sigma, mode='diag')
    whitened_full = whiten_residuals(residual, cov=cov_diag, mode='full')
    
    print(f"  Diagonal whitening norm: {np.linalg.norm(whitened_diag):.6f}")
    print(f"  Full whitening norm: {np.linalg.norm(whitened_full):.6f}")
    print(f"  Difference: {np.linalg.norm(whitened_diag - whitened_full):.6e}")
    
    if np.allclose(whitened_diag, whitened_full, rtol=1e-6):
        print("  ✓ PASS: Diagonal and full whitening agree for diagonal cov")
    else:
        print("  ✗ FAIL: Methods disagree")
    print()
    
    # Test 4: MC null generation
    print("Test 4: Monte Carlo null generation")
    n = 25
    sigma = np.ones(n)
    cov = np.eye(n)
    
    rng = np.random.RandomState(42)
    samples_diag = [generate_mc_null_sample(sigma=sigma, mode='diag', random_state=rng) for _ in range(1000)]
    samples_full = [generate_mc_null_sample(cov=cov, mode='full', random_state=rng) for _ in range(1000)]
    
    samples_diag = np.array(samples_diag)
    samples_full = np.array(samples_full)
    
    mean_diag = np.mean(samples_diag)
    std_diag = np.std(samples_diag)
    mean_full = np.mean(samples_full)
    std_full = np.std(samples_full)
    
    print(f"  Diag mode: mean={mean_diag:.4f}, std={std_diag:.4f}")
    print(f"  Full mode: mean={mean_full:.4f}, std={std_full:.4f}")
    
    if abs(mean_diag) < 0.1 and abs(std_diag - 1.0) < 0.1:
        print("  ✓ PASS: MC null samples have correct statistics")
    else:
        print("  ✗ FAIL: MC null samples have wrong statistics")
    print()
    
    print("="*80)
    print("Self-test complete")
    print("="*80)
