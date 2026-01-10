#!/usr/bin/env python3
"""
WMAP Data Loader for CMB Comb Fingerprint Test

Loads WMAP 9-year TT power spectrum data for independent replication.
Supports text and FITS formats.

Returns unified data dictionary compatible with cmb_comb.py

License: MIT
Author: UBT Research Team
"""

import numpy as np
from pathlib import Path
import warnings


def load_wmap_data(
    obs_file,
    model_file=None,
    cov_file=None,
    ell_min=None,
    ell_max=None,
    dataset_name="WMAP 9yr"
):
    """
    Load WMAP TT power spectrum data.
    
    Parameters
    ----------
    obs_file : str or Path
        Path to observed power spectrum file (.txt or .fits)
    model_file : str or Path, optional
        Path to theoretical model file. If None, cl_model will be None.
    cov_file : str or Path, optional
        Path to covariance matrix file. If None, uses diagonal from obs_file.
    ell_min : int, optional
        Minimum multipole to include (default: use all)
    ell_max : int, optional
        Maximum multipole to include (default: use all)
    dataset_name : str
        Dataset identifier for provenance (default: "WMAP 9yr")
    
    Returns
    -------
    dict
        Data dictionary with keys:
        - ell: ndarray, multipole moments
        - cl_obs: ndarray, observed power spectrum (μK²)
        - cl_model: ndarray or None, theoretical model
        - sigma: ndarray, diagonal uncertainties
        - cov: ndarray or None, full covariance matrix
        - dataset: str, dataset name
        - ell_range: tuple, (ell_min, ell_max) applied
    
    Raises
    ------
    FileNotFoundError
        If obs_file doesn't exist
    ValueError
        If file format is unsupported or data is invalid
    """
    obs_file = Path(obs_file)
    
    if not obs_file.exists():
        raise FileNotFoundError(f"Observation file not found: {obs_file}")
    
    # Detect format from extension
    if obs_file.suffix.lower() == '.fits':
        ell_obs, cl_obs, sigma_obs = _load_wmap_fits(obs_file)
    elif obs_file.suffix.lower() in ['.txt', '.dat']:
        ell_obs, cl_obs, sigma_obs = _load_wmap_text(obs_file)
    else:
        raise ValueError(f"Unsupported file format: {obs_file.suffix}")
    
    # Load model if provided
    cl_model = None
    if model_file is not None:
        model_file = Path(model_file)
        if not model_file.exists():
            warnings.warn(f"Model file not found: {model_file}. Proceeding without model.")
        else:
            if model_file.suffix.lower() == '.fits':
                ell_model, cl_model, _ = _load_wmap_fits(model_file)
            else:
                ell_model, cl_model, _ = _load_wmap_text(model_file)
            
            # Ensure ell arrays match
            if not np.array_equal(ell_obs, ell_model):
                warnings.warn("Multipole ranges in obs and model don't match. Interpolating model.")
                cl_model = np.interp(ell_obs, ell_model, cl_model)
    
    # Load covariance if provided
    cov = None
    if cov_file is not None:
        cov_file = Path(cov_file)
        if not cov_file.exists():
            warnings.warn(f"Covariance file not found: {cov_file}. Using diagonal uncertainties.")
        else:
            cov = _load_wmap_covariance(cov_file)
            
            # Ensure covariance shape matches data
            if cov.shape[0] != len(ell_obs):
                warnings.warn(
                    f"Covariance matrix size ({cov.shape[0]}) doesn't match "
                    f"data size ({len(ell_obs)}). Using diagonal."
                )
                cov = None
    
    # Apply multipole range filter
    ell = ell_obs
    if ell_min is not None or ell_max is not None:
        ell_min = ell_min if ell_min is not None else ell[0]
        ell_max = ell_max if ell_max is not None else ell[-1]
        
        mask = (ell >= ell_min) & (ell <= ell_max)
        
        ell = ell[mask]
        cl_obs = cl_obs[mask]
        sigma_obs = sigma_obs[mask]
        
        if cl_model is not None:
            cl_model = cl_model[mask]
        
        if cov is not None:
            cov = cov[np.ix_(mask, mask)]
    else:
        ell_min = ell[0]
        ell_max = ell[-1]
    
    # Assemble data dictionary
    data = {
        'ell': ell,
        'cl_obs': cl_obs,
        'cl_model': cl_model,
        'sigma': sigma_obs,
        'cov': cov,
        'dataset': dataset_name,
        'ell_range': (int(ell_min), int(ell_max)),
        'n_multipoles': len(ell)
    }
    
    return data


def _load_wmap_text(filepath):
    """
    Load WMAP data from text file.
    
    Expected format (WMAP standard):
    # ell  C_ell  sigma_C_ell
    2      1100.2  50.1
    3      1850.3  45.2
    ...
    
    Parameters
    ----------
    filepath : Path
        Path to text file
    
    Returns
    -------
    ell : ndarray
        Multipole moments (integers)
    cl : ndarray
        Power spectrum values
    sigma : ndarray
        Uncertainties (1-sigma)
    """
    try:
        data = np.loadtxt(filepath, comments='#')
    except Exception as e:
        raise ValueError(f"Failed to load text file {filepath}: {e}")
    
    if data.ndim != 2:
        raise ValueError(f"Expected 2D array from {filepath}, got shape {data.shape}")
    
    if data.shape[1] < 2:
        raise ValueError(f"Expected at least 2 columns in {filepath}, got {data.shape[1]}")
    
    ell = data[:, 0].astype(int)
    cl = data[:, 1]
    
    # Sigma may or may not be present
    if data.shape[1] >= 3:
        sigma = data[:, 2]
    else:
        # If no sigma provided, estimate from scatter (not ideal)
        warnings.warn(f"No uncertainties in {filepath}. Estimating from 1% of signal.")
        sigma = 0.01 * np.abs(cl)
    
    return ell, cl, sigma


def _load_wmap_fits(filepath):
    """
    Load WMAP data from FITS file.
    
    Parameters
    ----------
    filepath : Path
        Path to FITS file
    
    Returns
    -------
    ell : ndarray
        Multipole moments
    cl : ndarray
        Power spectrum values
    sigma : ndarray
        Uncertainties
    """
    try:
        from astropy.io import fits
    except ImportError:
        raise ImportError(
            "astropy is required to load FITS files. Install with: pip install astropy"
        )
    
    try:
        with fits.open(filepath) as hdul:
            # Typically data is in first extension
            data = hdul[1].data
            
            # Try common WMAP column names
            ell_names = ['ell', 'ELL', 'l', 'L', 'MULTIPOLE']
            cl_names = ['TT', 'C_l', 'C_ell', 'CL', 'POWER', 'TEMPERATURE']
            sigma_names = ['TT_error', 'sigma', 'SIGMA', 'ERROR', 'ERR', 'C_l_ERR']
            
            ell = None
            for name in ell_names:
                if name in data.names:
                    ell = data[name]
                    break
            
            if ell is None:
                raise ValueError(f"No ell column found in {filepath}")
            
            cl = None
            for name in cl_names:
                if name in data.names:
                    cl = data[name]
                    break
            
            if cl is None:
                raise ValueError(f"No power spectrum column found in {filepath}")
            
            sigma = None
            for name in sigma_names:
                if name in data.names:
                    sigma = data[name]
                    break
            
            if sigma is None:
                warnings.warn(f"No uncertainty column found in {filepath}. Estimating from 1% of signal.")
                sigma = 0.01 * np.abs(cl)
            
            return np.array(ell, dtype=int), np.array(cl), np.array(sigma)
    
    except Exception as e:
        raise ValueError(f"Failed to load FITS file {filepath}: {e}")


def _load_wmap_covariance(filepath):
    """
    Load WMAP covariance matrix from file.
    
    Parameters
    ----------
    filepath : Path
        Path to covariance file (.dat or .txt)
    
    Returns
    -------
    cov : ndarray
        Covariance matrix (2D array)
    """
    try:
        cov = np.loadtxt(filepath)
    except Exception as e:
        raise ValueError(f"Failed to load covariance file {filepath}: {e}")
    
    if cov.ndim != 2 or cov.shape[0] != cov.shape[1]:
        raise ValueError(f"Covariance must be square 2D array, got shape {cov.shape}")
    
    # Verify covariance is symmetric (within tolerance)
    if not np.allclose(cov, cov.T, rtol=1e-5):
        warnings.warn("Covariance matrix is not symmetric. Symmetrizing.")
        cov = 0.5 * (cov + cov.T)
    
    return cov


if __name__ == '__main__':
    # Example usage
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python wmap.py <obs_file> [model_file] [cov_file]")
        print("")
        print("Example:")
        print("  python wmap.py data/wmap/raw/wmap_tt_spectrum_9yr_v5.txt")
        print("  python wmap.py spectrum.txt model.txt covariance.dat")
        sys.exit(1)
    
    obs_file = sys.argv[1]
    model_file = sys.argv[2] if len(sys.argv) > 2 else None
    cov_file = sys.argv[3] if len(sys.argv) > 3 else None
    
    print("Loading WMAP data...")
    data = load_wmap_data(obs_file, model_file, cov_file, ell_min=30, ell_max=800)
    
    print("\nData loaded successfully:")
    print(f"  Dataset: {data['dataset']}")
    print(f"  Multipole range: {data['ell_range']}")
    print(f"  Number of multipoles: {data['n_multipoles']}")
    print(f"  Has model: {data['cl_model'] is not None}")
    print(f"  Has covariance: {data['cov'] is not None}")
    print(f"  First few ell: {data['ell'][:5]}")
    print(f"  First few C_ell: {data['cl_obs'][:5]}")
