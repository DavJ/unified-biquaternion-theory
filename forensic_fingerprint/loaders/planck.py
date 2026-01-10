#!/usr/bin/env python3
"""
Planck Data Loader for CMB Comb Fingerprint Test

Loads Planck PR3 (Release 3) TT power spectrum data with support for:
- Text files (.txt)
- FITS files (.fits)
- Diagonal uncertainties or full covariance
- Multipole range filtering

Returns unified data dictionary compatible with cmb_comb.py

License: MIT
Author: UBT Research Team
"""

import numpy as np
from pathlib import Path
import warnings


def load_planck_data(
    obs_file,
    model_file=None,
    cov_file=None,
    ell_min=None,
    ell_max=None,
    dataset_name="Planck PR3"
):
    """
    Load Planck TT power spectrum data.
    
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
        Dataset identifier for provenance (default: "Planck PR3")
    
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
        ell_obs, cl_obs, sigma_obs = _load_planck_fits(obs_file)
    elif obs_file.suffix.lower() in ['.txt', '.dat']:
        ell_obs, cl_obs, sigma_obs = _load_planck_text(obs_file)
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
                ell_model, cl_model, _ = _load_planck_fits(model_file)
            else:
                ell_model, cl_model, _ = _load_planck_text(model_file)
            
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
            cov = _load_planck_covariance(cov_file)
            
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


def _load_planck_text(filepath):
    """
    Load Planck data from text file.
    
    Expected format (simple 3-column):
    # ell  C_ell  sigma_C_ell
    2      1305.6  30.2
    3      2015.3  28.5
    ...
    
    Also supports PR3 "minimum" model format with multiple columns
    and header line indicating column names.
    
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
    # First, check if file is HTML (indicates wrong URL or 404)
    with open(filepath, 'r') as f:
        first_line = f.readline().strip()
    
    if first_line.startswith('<!DOCTYPE') or first_line.startswith('<html'):
        raise ValueError(
            f"HTML detected in {filepath}. This likely means:\n"
            f"  - Downloaded from wrong URL (got 404 page)\n"
            f"  - File doesn't exist at the specified location\n"
            f"  - Check URL and use correct PR3 cosmoparams directory:\n"
            f"    https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/"
        )
    
    # Detect if this is a PR3 "minimum" model file
    filename = filepath.name if hasattr(filepath, 'name') else str(filepath)
    is_minimum_format = '-minimum_' in filename or 'plikHM' in filename
    
    if is_minimum_format:
        return _load_planck_minimum_format(filepath)
    
    # Standard simple 3-column format
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


def _load_planck_minimum_format(filepath):
    """
    Load Planck PR3 "minimum" model file format.
    
    The PR3 minimum model file has a header line with column names followed by data.
    Format example:
    # L  TT  TE  EE  BB  PP  TP
    2  5.51e+01  -1.18e+01  1.34e-02  ...
    3  2.29e+02  -2.99e+01  6.89e-03  ...
    
    We extract the 'L' (multipole) and 'TT' (TT power spectrum) columns.
    The TT values are typically in Dl units (l(l+1)Cl/2π) and need to be
    converted to Cl for consistency with cmb_comb residuals.
    
    Parameters
    ----------
    filepath : Path
        Path to minimum format file
    
    Returns
    -------
    ell : ndarray
        Multipole moments (integers)
    cl : ndarray
        TT power spectrum in Cl units (μK²)
    sigma : ndarray
        Uncertainties (estimated as 1% since not provided in model file)
    """
    # Read file and find header line
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Find header line (starts with # and contains column names)
    header_idx = None
    header_line = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('#'):
            # Check if it contains expected column names
            if 'TT' in stripped or 'Dl' in stripped or 'Cl' in stripped:
                header_idx = i
                header_line = stripped.lstrip('#').strip()
                break
    
    if header_line is None:
        # No header found, try simple parsing
        warnings.warn(
            f"No header found in {filepath}. "
            f"Attempting to parse as standard format with L in col 0, TT in col 1."
        )
        try:
            data = np.loadtxt(filepath, comments='#')
            if data.shape[1] < 2:
                raise ValueError(f"Expected at least 2 columns, got {data.shape[1]}")
            
            ell = data[:, 0].astype(int)
            cl_or_dl = data[:, 1]
            
            # Convert Dl to Cl if needed (heuristic: if values > 1000, likely Dl)
            if np.median(cl_or_dl[ell > 10]) > 1000:
                # Likely Dl format: Dl = l(l+1)Cl/(2π)
                cl = cl_or_dl * (2.0 * np.pi) / (ell * (ell + 1.0))
                cl[ell == 0] = 0.0  # Handle ell=0 case
            else:
                cl = cl_or_dl
            
            sigma = 0.01 * np.abs(cl)
            return ell, cl, sigma
            
        except Exception as e:
            raise ValueError(f"Failed to parse minimum format file {filepath}: {e}")
    
    # Parse header to find column indices
    columns = header_line.split()
    
    # Find L/ell column
    ell_col = None
    for i, col in enumerate(columns):
        if col.upper() in ['L', 'ELL', 'MULTIPOLE']:
            ell_col = i
            break
    
    if ell_col is None:
        # Assume first column is ell
        ell_col = 0
        warnings.warn(f"Could not find ell column in header, assuming column 0")
    
    # Find TT column (may be Dl_TT, Cl_TT, or just TT)
    tt_col = None
    for i, col in enumerate(columns):
        col_upper = col.upper()
        if col_upper in ['TT', 'DL_TT', 'CL_TT', 'DLTT', 'CLTT']:
            tt_col = i
            break
    
    if tt_col is None:
        raise ValueError(f"Could not find TT column in header: {columns}")
    
    # Load data (skip header and comment lines)
    data_lines = []
    for line in lines[header_idx + 1:]:
        stripped = line.strip()
        if stripped and not stripped.startswith('#'):
            data_lines.append(stripped)
    
    if not data_lines:
        raise ValueError(f"No data found in {filepath}")
    
    # Parse data
    data = []
    for line in data_lines:
        try:
            values = line.split()
            data.append([float(v) for v in values])
        except ValueError:
            continue  # Skip malformed lines
    
    if not data:
        raise ValueError(f"No valid data rows in {filepath}")
    
    data = np.array(data)
    
    # Extract columns
    ell = data[:, ell_col].astype(int)
    cl_or_dl = data[:, tt_col]
    
    # Determine if Dl or Cl format
    # Heuristic: if column name contains 'DL' or values are large (>1000 for ell>10), assume Dl
    is_dl_format = 'DL' in columns[tt_col].upper() or np.median(cl_or_dl[ell > 10]) > 1000
    
    if is_dl_format:
        # Convert Dl to Cl: Cl = Dl * 2π / [l(l+1)]
        with np.errstate(divide='ignore', invalid='ignore'):
            cl = cl_or_dl * (2.0 * np.pi) / (ell * (ell + 1.0))
            cl[ell == 0] = 0.0  # Handle ell=0
            cl[ell == 1] = 0.0  # Handle ell=1
    else:
        cl = cl_or_dl
    
    # Model files typically don't include uncertainties
    # Estimate as 1% of signal
    sigma = 0.01 * np.abs(cl)
    sigma[sigma == 0] = 1e-10  # Avoid exact zeros
    
    return ell, cl, sigma


def _load_planck_fits(filepath):
    """
    Load Planck data from FITS file.
    
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
            
            # Try common column names
            ell_names = ['ell', 'ELL', 'l', 'L', 'MULTIPOLE']
            cl_names = ['TT', 'C_ell', 'C_ELL', 'CL', 'POWER']
            sigma_names = ['TT_error', 'sigma', 'SIGMA', 'ERROR', 'ERR']
            
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


def _load_planck_covariance(filepath):
    """
    Load Planck covariance matrix from file.
    
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
        print("Usage: python planck.py <obs_file> [model_file] [cov_file]")
        print("")
        print("Example:")
        print("  python planck.py data/planck_pr3/raw/spectrum.txt")
        print("  python planck.py spectrum.txt model.txt covariance.dat")
        sys.exit(1)
    
    obs_file = sys.argv[1]
    model_file = sys.argv[2] if len(sys.argv) > 2 else None
    cov_file = sys.argv[3] if len(sys.argv) > 3 else None
    
    print("Loading Planck data...")
    data = load_planck_data(obs_file, model_file, cov_file, ell_min=30, ell_max=1500)
    
    print("\nData loaded successfully:")
    print(f"  Dataset: {data['dataset']}")
    print(f"  Multipole range: {data['ell_range']}")
    print(f"  Number of multipoles: {data['n_multipoles']}")
    print(f"  Has model: {data['cl_model'] is not None}")
    print(f"  Has covariance: {data['cov'] is not None}")
    print(f"  First few ell: {data['ell'][:5]}")
    print(f"  First few C_ell: {data['cl_obs'][:5]}")
