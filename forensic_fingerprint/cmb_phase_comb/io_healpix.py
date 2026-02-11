#!/usr/bin/env python3
"""
HEALPix Map I/O and Spherical Harmonic Analysis
================================================

Load CMB maps in HEALPix format and compute spherical harmonic coefficients a_lm.

Supported formats:
- FITS (via healpy.read_map)
- NumPy binary (.npy)

Dependencies:
- healpy (required)
- astropy (optional, for advanced FITS handling)

License: MIT
Author: UBT Research Team
"""

import numpy as np
from pathlib import Path
from typing import Optional, Tuple
import warnings


def load_healpix_map(map_path: str, 
                     mask_path: Optional[str] = None,
                     field: int = 0,
                     remove_monopole: bool = True,
                     remove_dipole: bool = True) -> Tuple[np.ndarray, Optional[np.ndarray], dict]:
    """
    Load HEALPix CMB map and optional mask.
    
    Parameters
    ----------
    map_path : str
        Path to HEALPix map (FITS or .npy)
    mask_path : str or None
        Path to mask (0/1 values, same resolution as map)
    field : int
        Field index to read from FITS (default: 0 for temperature)
    remove_monopole : bool
        Remove monopole (ℓ=0) before analysis (default: True)
    remove_dipole : bool
        Remove dipole (ℓ=1) before analysis (default: True)
    
    Returns
    -------
    map_data : ndarray
        HEALPix map (masked and monopole/dipole removed if requested)
    mask : ndarray or None
        Mask array (0/1)
    metadata : dict
        Map metadata (nside, npix, etc.)
    """
    try:
        import healpy as hp
    except ImportError:
        raise ImportError(
            "healpy required for HEALPix I/O. Install with: pip install healpy"
        )
    
    map_path = Path(map_path)
    
    if not map_path.exists():
        raise FileNotFoundError(f"Map not found: {map_path}")
    
    # Load map
    print(f"Loading HEALPix map: {map_path}")
    
    if map_path.suffix == '.npy':
        map_data = np.load(map_path)
    else:
        # Assume FITS
        map_data = hp.read_map(str(map_path), field=field, verbose=False)
    
    nside = hp.npix2nside(len(map_data))
    npix = len(map_data)
    
    print(f"  NSIDE = {nside}, NPIX = {npix}")
    
    # Load mask if provided
    mask = None
    if mask_path:
        mask_path = Path(mask_path)
        print(f"Loading mask: {mask_path}")
        
        if not mask_path.exists():
            raise FileNotFoundError(f"Mask not found: {mask_path}")
        
        if mask_path.suffix == '.npy':
            mask = np.load(mask_path)
        else:
            mask = hp.read_map(str(mask_path), field=0, verbose=False)
        
        # Check mask dimensions
        if len(mask) != npix:
            raise ValueError(
                f"Mask size mismatch: map has {npix} pixels, mask has {len(mask)}"
            )
        
        # Check mask values
        unique_vals = np.unique(mask)
        if not np.all(np.isin(unique_vals, [0, 1])):
            # Allow continuous masks, threshold at 0.5
            warnings.warn(
                "Mask contains non-binary values. Thresholding at 0.5"
            )
            mask = (mask > 0.5).astype(float)
        
        # Apply mask
        print(f"  Masked pixels: {np.sum(mask == 0)} / {npix} ({100*np.sum(mask==0)/npix:.1f}%)")
        map_data = map_data * mask
    else:
        print("  No mask provided (using full sky)")
    
    # Remove monopole/dipole
    if remove_monopole or remove_dipole:
        # Use healpy's remove_dipole which handles masked pixels
        if mask is not None:
            # Set masked pixels to UNSEEN
            map_masked = map_data.copy()
            map_masked[mask < 0.5] = hp.UNSEEN
        else:
            map_masked = map_data
        
        if remove_monopole and remove_dipole:
            print("  Removing monopole and dipole...")
            map_data = hp.remove_dipole(map_masked, verbose=False, copy=True)
        elif remove_monopole:
            print("  Removing monopole only...")
            # Remove monopole by subtracting mean of unmasked pixels
            if mask is not None:
                good = mask > 0.5
                mean_val = np.mean(map_data[good])
            else:
                mean_val = np.mean(map_data)
            map_data = map_data - mean_val
    
    # Metadata
    metadata = {
        'nside': nside,
        'npix': npix,
        'map_file': str(map_path),
        'mask_file': str(mask_path) if mask_path else None,
        'masked_pixels': int(np.sum(mask == 0)) if mask is not None else 0,
        'sky_fraction': float(np.sum(mask > 0.5) / npix) if mask is not None else 1.0,
        'monopole_removed': remove_monopole,
        'dipole_removed': remove_dipole,
    }
    
    return map_data, mask, metadata


def compute_alm(map_data: np.ndarray, 
                lmax: int,
                iter: int = 3,
                use_pixel_weights: bool = False) -> np.ndarray:
    """
    Compute spherical harmonic coefficients a_lm from HEALPix map.
    
    Parameters
    ----------
    map_data : ndarray
        HEALPix map (should be masked if needed)
    lmax : int
        Maximum ℓ for spherical harmonic decomposition
    iter : int
        Number of iterations for iterative map2alm (default: 3)
        - 0: Direct transform (fast but less accurate)
        - 3: Standard (good balance)
        - Higher: Better for noisy/masked maps
    use_pixel_weights : bool
        Use pixel weights for improved accuracy (default: False)
        Requires healpy pixel weights data
    
    Returns
    -------
    alm : complex ndarray
        Spherical harmonic coefficients
        Shape: (N_alm,) where N_alm = (lmax+1)*(lmax+2)/2
    """
    try:
        import healpy as hp
    except ImportError:
        raise ImportError("healpy required. Install with: pip install healpy")
    
    nside = hp.npix2nside(len(map_data))
    
    print(f"Computing spherical harmonics up to lmax={lmax}...")
    print(f"  NSIDE={nside}, iter={iter}")
    
    # Check if map contains UNSEEN pixels
    has_unseen = np.any(map_data == hp.UNSEEN)
    if has_unseen:
        print("  Map contains UNSEEN pixels (masked)")
    
    # Compute alm
    if use_pixel_weights:
        print("  Using pixel weights (slower but more accurate)")
        # This requires downloading healpy pixel weights
        try:
            alm = hp.map2alm(map_data, lmax=lmax, iter=iter, use_pixel_weights=True)
        except Exception as e:
            warnings.warn(f"Pixel weights failed ({e}), using standard transform")
            alm = hp.map2alm(map_data, lmax=lmax, iter=iter)
    else:
        alm = hp.map2alm(map_data, lmax=lmax, iter=iter)
    
    print(f"  Computed {len(alm)} coefficients")
    
    # Sanity check: verify reality constraint for m=0
    # a_{ℓ,0} should be real
    n_m0_imaginary = 0
    for ell in range(lmax + 1):
        idx = hp.sphtfunc.Alm.getidx(lmax, ell, 0)
        if abs(alm[idx].imag) > 1e-10 * abs(alm[idx].real):
            n_m0_imaginary += 1
    
    if n_m0_imaginary > 0:
        warnings.warn(
            f"{n_m0_imaginary} m=0 coefficients have significant imaginary parts. "
            "This may indicate numerical issues or non-real map."
        )
    
    return alm


def validate_alm_conjugacy(alm: np.ndarray, lmax: int, 
                          tol: float = 1e-6) -> Tuple[bool, str]:
    """
    Validate reality constraint: a_{ℓ,-m} = (-1)^m conj(a_{ℓ,m})
    
    Note: healpy only stores m≥0, so this checks consistency of m=0 being real.
    
    Parameters
    ----------
    alm : complex ndarray
        Spherical harmonic coefficients
    lmax : int
        Maximum ℓ
    tol : float
        Tolerance for imaginary part of m=0 modes
    
    Returns
    -------
    is_valid : bool
        True if conjugacy constraint satisfied
    message : str
        Diagnostic message
    """
    try:
        import healpy as hp
    except ImportError:
        raise ImportError("healpy required")
    
    violations = []
    
    for ell in range(lmax + 1):
        idx = hp.sphtfunc.Alm.getidx(lmax, ell, 0)
        a_l0 = alm[idx]
        
        # Check if m=0 is real
        imag_frac = abs(a_l0.imag) / (abs(a_l0.real) + 1e-30)
        
        if imag_frac > tol:
            violations.append((ell, imag_frac))
    
    if len(violations) == 0:
        return True, "All m=0 modes are real (within tolerance)"
    else:
        max_viol = max(violations, key=lambda x: x[1])
        return False, (
            f"{len(violations)} m=0 modes violate reality constraint. "
            f"Worst: ℓ={max_viol[0]} with imag/real={max_viol[1]:.2e}"
        )


def get_cl_from_alm(alm: np.ndarray, lmax: int) -> np.ndarray:
    """
    Compute power spectrum C_ℓ from a_lm coefficients.
    
    C_ℓ = (1/(2ℓ+1)) Σ_m |a_ℓm|²
    
    Parameters
    ----------
    alm : complex ndarray
        Spherical harmonic coefficients
    lmax : int
        Maximum ℓ
    
    Returns
    -------
    cl : ndarray
        Power spectrum, shape (lmax+1,)
    """
    try:
        import healpy as hp
    except ImportError:
        raise ImportError("healpy required")
    
    cl = hp.sphtfunc.alm2cl(alm, lmax=lmax)
    return cl
