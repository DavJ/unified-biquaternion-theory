#!/usr/bin/env python3
"""
Phase Randomization and C_ℓ Preservation Utilities
==================================================

Implements court-grade null model for phase-comb test:
- Randomize phases while preserving amplitudes |a_lm|
- Verify C_ℓ preservation
- Ensure reality constraints for real maps

License: MIT
Author: UBT Research Team
"""

import numpy as np
from typing import Optional, Tuple
import warnings


def randomize_phases_preserve_cl(alm: np.ndarray, lmax: int,
                                 seed: Optional[int] = None,
                                 preserve_m0_real: bool = True) -> np.ndarray:
    """
    Generate phase-randomized a_lm preserving |a_lm| (and thus C_ℓ).
    
    For each (ℓ,m):
        a'_ℓm = |a_ℓm| * exp(i θ_ℓm)
    where θ_ℓm ~ Uniform(0, 2π)
    
    Reality constraints for real maps:
    - a_ℓ,0 is real (phase = 0 or π, preserve sign)
    - a_ℓ,-m = (-1)^m conj(a_ℓm) [healpy handles this internally for m≥0]
    
    Parameters
    ----------
    alm : complex ndarray
        Original spherical harmonic coefficients
    lmax : int
        Maximum ℓ
    seed : int or None
        Random seed for reproducibility
    preserve_m0_real : bool
        Keep m=0 modes real (default: True)
    
    Returns
    -------
    alm_randomized : complex ndarray
        Phase-randomized coefficients with same |a_lm|
    """
    try:
        import healpy as hp
    except ImportError:
        raise ImportError("healpy required. Install with: pip install healpy")
    
    rng = np.random.RandomState(seed)
    
    alm_rand = np.zeros_like(alm)
    
    # Iterate over all (ℓ,m) pairs (healpy stores only m≥0)
    for ell in range(lmax + 1):
        for m in range(0, ell + 1):
            idx = hp.sphtfunc.Alm.getidx(lmax, ell, m)
            
            # Original amplitude
            amplitude = abs(alm[idx])
            
            # Random phase
            if m == 0 and preserve_m0_real:
                # m=0 is real: phase = 0 or π
                # Preserve sign of original
                if alm[idx].real >= 0:
                    phase = 0.0
                else:
                    phase = np.pi
            else:
                # Random phase
                phase = rng.uniform(0, 2 * np.pi)
            
            # Randomized coefficient
            alm_rand[idx] = amplitude * np.exp(1j * phase)
    
    return alm_rand


def validate_cl_preservation(alm_original: np.ndarray, 
                             alm_randomized: np.ndarray,
                             lmax: int,
                             rtol: float = 1e-10) -> Tuple[bool, str, dict]:
    """
    Validate that phase randomization preserved C_ℓ.
    
    Checks:
    1. |a_lm| preserved (per-mode check)
    2. C_ℓ preserved (averaged over m)
    
    Parameters
    ----------
    alm_original : complex ndarray
        Original coefficients
    alm_randomized : complex ndarray
        Phase-randomized coefficients
    lmax : int
        Maximum ℓ
    rtol : float
        Relative tolerance for amplitude preservation
    
    Returns
    -------
    is_valid : bool
        True if C_ℓ preserved within tolerance
    message : str
        Diagnostic message
    stats : dict
        Detailed statistics
    """
    try:
        import healpy as hp
    except ImportError:
        raise ImportError("healpy required")
    
    # Check 1: Per-mode amplitude preservation
    max_amplitude_error = 0.0
    n_violations = 0
    
    for ell in range(lmax + 1):
        for m in range(0, ell + 1):
            idx = hp.sphtfunc.Alm.getidx(lmax, ell, m)
            
            amp_orig = abs(alm_original[idx])
            amp_rand = abs(alm_randomized[idx])
            
            if amp_orig > 0:
                rel_error = abs(amp_rand - amp_orig) / amp_orig
                max_amplitude_error = max(max_amplitude_error, rel_error)
                
                if rel_error > rtol:
                    n_violations += 1
    
    # Check 2: C_ℓ preservation
    cl_orig = hp.sphtfunc.alm2cl(alm_original, lmax=lmax)
    cl_rand = hp.sphtfunc.alm2cl(alm_randomized, lmax=lmax)
    
    # Relative errors in C_ℓ
    # Ignore ℓ < 2 (monopole/dipole may be zero)
    cl_errors = []
    for ell in range(2, lmax + 1):
        if cl_orig[ell] > 0:
            rel_err = abs(cl_rand[ell] - cl_orig[ell]) / cl_orig[ell]
            cl_errors.append(rel_err)
    
    max_cl_error = max(cl_errors) if cl_errors else 0.0
    mean_cl_error = np.mean(cl_errors) if cl_errors else 0.0
    
    # Validation
    is_valid = (max_amplitude_error < rtol and max_cl_error < rtol)
    
    stats = {
        'max_amplitude_error': float(max_amplitude_error),
        'n_amplitude_violations': n_violations,
        'max_cl_error': float(max_cl_error),
        'mean_cl_error': float(mean_cl_error),
        'tolerance': rtol,
    }
    
    if is_valid:
        message = (
            f"C_ℓ preservation: PASS. "
            f"Max amplitude error: {max_amplitude_error:.2e}, "
            f"Max C_ℓ error: {max_cl_error:.2e}"
        )
    else:
        message = (
            f"C_ℓ preservation: FAIL. "
            f"Max amplitude error: {max_amplitude_error:.2e} (tol={rtol:.2e}), "
            f"Max C_ℓ error: {max_cl_error:.2e}, "
            f"Violations: {n_violations}"
        )
    
    return is_valid, message, stats


def sanity_check_surrogates(alm_original: np.ndarray,
                            surrogates: list,
                            lmax: int,
                            n_check: int = 10) -> dict:
    """
    Perform sanity checks on surrogate ensemble.
    
    Checks:
    1. C_ℓ preservation for each surrogate
    2. Phase randomness (variance should be uniform)
    
    Parameters
    ----------
    alm_original : complex ndarray
        Original coefficients
    surrogates : list of ndarray
        List of surrogate alm arrays
    lmax : int
        Maximum ℓ
    n_check : int
        Number of surrogates to check in detail
    
    Returns
    -------
    results : dict
        Sanity check results
    """
    try:
        import healpy as hp
    except ImportError:
        raise ImportError("healpy required")
    
    n_surrogates = len(surrogates)
    n_to_check = min(n_check, n_surrogates)
    
    # Check C_ℓ preservation
    cl_errors = []
    for i in range(n_to_check):
        _, _, stats = validate_cl_preservation(
            alm_original, surrogates[i], lmax
        )
        cl_errors.append(stats['max_cl_error'])
    
    max_cl_error_overall = max(cl_errors)
    mean_cl_error_overall = np.mean(cl_errors)
    
    # Check phase randomness
    # For a few (ℓ,m) modes, compute variance of phases across surrogates
    # Should be close to (2π)²/12 ≈ 3.29 for uniform distribution
    
    phase_variances = []
    
    # Sample some modes
    test_modes = [
        (30, 0), (30, 5), (30, 15),
        (100, 0), (100, 10), (100, 50),
        (500, 0), (500, 50), (500, 250),
    ]
    
    for ell, m in test_modes:
        if ell > lmax or m > ell:
            continue
        
        idx = hp.sphtfunc.Alm.getidx(lmax, ell, m)
        
        phases = []
        for alm_surr in surrogates:
            phase = np.angle(alm_surr[idx])
            phases.append(phase)
        
        # Compute circular variance
        # For uniform phases on [0,2π), variance ≈ π²/3 ≈ 3.29
        phases = np.array(phases)
        
        # Use circular mean and variance
        # R = |mean(exp(i*phase))|
        # Circular variance = 1 - R
        R = abs(np.mean(np.exp(1j * phases)))
        circ_var = 1 - R
        
        phase_variances.append(circ_var)
    
    mean_phase_variance = np.mean(phase_variances) if phase_variances else 0.0
    
    # Expected circular variance for uniform: 1.0 (R=0 for large N)
    phase_variance_ok = (0.8 < mean_phase_variance < 1.0)
    
    results = {
        'n_surrogates_checked': n_to_check,
        'max_cl_error': float(max_cl_error_overall),
        'mean_cl_error': float(mean_cl_error_overall),
        'cl_preservation_ok': max_cl_error_overall < 1e-6,
        'mean_phase_variance': float(mean_phase_variance),
        'expected_phase_variance': 1.0,
        'phase_randomness_ok': phase_variance_ok,
        'overall_pass': (
            max_cl_error_overall < 1e-6 and phase_variance_ok
        ),
    }
    
    return results
