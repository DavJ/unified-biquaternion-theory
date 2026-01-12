#!/usr/bin/env python3
"""
Planck Data Loader for CMB Comb Fingerprint Test

Loads Planck PR3 (Release 3) power spectrum data with support for:
- TT, EE, TE, BB spectra (polarization and temperature)
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
import sys

# Import covariance loader and utilities
try:
    from . import covariance as cov_loader
    from . import utils
except ImportError:
    # For direct execution
    import covariance as cov_loader
    import utils


# Constants for data parsing and validation
# Threshold for distinguishing Dl from Cl format:
# If median power spectrum value > this threshold, assume Dl format
# Rationale: CMB Cl values at ell > 10 are typically < 1000 μK²,
# while Dl values are typically > 1000 μK² (Dl ≈ ell(ell+1)Cl/2π)
DL_CL_THRESHOLD = 1000.0

# Default uncertainty estimate when not provided in file
# Used for model files which typically don't include errors
DEFAULT_SIGMA_FRACTION = 0.01  # 1% of signal


def load_planck_data(
    obs_file,
    model_file=None,
    cov_file=None,
    ell_min=None,
    ell_max=None,
    dataset_name="Planck PR3",
    spectrum_type="TT",
    _skip_size_validation=False
):
    """
    Load Planck power spectrum data.
    
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
    spectrum_type : str
        Type of spectrum: "TT", "EE", "TE", or "BB" (default: "TT")
    _skip_size_validation : bool, optional
        Internal parameter for testing. If True, skips file size validation.
        Default False. Do not use in production code.
    
    Returns
    -------
    dict
        Data dictionary with keys:
        - ell: ndarray, multipole moments
        - cl_obs: ndarray, observed power spectrum (Cl units, μK²)
        - cl_model: ndarray or None, theoretical model (Cl units, μK²)
        - sigma: ndarray, diagonal uncertainties (Cl units, μK²)
        - cov: ndarray or None, full covariance matrix
        - cov_source: str or None, covariance file path/description
        - cov_metadata: dict or None, validation metadata from covariance loader
        - whitening_mode_supported: list of str, supported whitening modes
        - dataset: str, dataset name
        - spectrum_type: str, spectrum type (TT/EE/TE/BB)
        - ell_range: tuple, (ell_min, ell_max) applied
        - n_multipoles: int, number of multipoles
        - obs_units: str, original units of observation file ("Dl" or "Cl")
        - model_units_original: str or None, original units of model file
        - model_units_used: str, final units used ("Cl")
        - sigma_method: str, method used to compute sigma
    
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
    
    # Detect format from extension and load observation data
    if obs_file.suffix.lower() == '.fits':
        ell_obs, cl_obs, sigma_obs, obs_units = _load_planck_fits(obs_file, spectrum_type=spectrum_type)
    elif obs_file.suffix.lower() in ['.txt', '.dat']:
        ell_obs, cl_obs, sigma_obs, obs_units = _load_planck_text(obs_file, spectrum_type=spectrum_type, _skip_size_validation=_skip_size_validation)
    else:
        raise ValueError(f"Unsupported file format: {obs_file.suffix}")
    
    # Log units detected
    print(f"Observation file units detected: {obs_units}")
    if obs_units == "Dl":
        print(f"  → Converted from Dl to Cl using: Cl = Dl × 2π / [l(l+1)]")
    
    # Load model if provided
    cl_model = None
    model_units_original = None
    if model_file is not None:
        model_file = Path(model_file)
        if not model_file.exists():
            warnings.warn(f"Model file not found: {model_file}. Proceeding without model.")
        else:
            if model_file.suffix.lower() == '.fits':
                ell_model, cl_model, _, model_units_original = _load_planck_fits(model_file, spectrum_type=spectrum_type)
            else:
                ell_model, cl_model, _, model_units_original = _load_planck_text(model_file, spectrum_type=spectrum_type, _skip_size_validation=_skip_size_validation)
            
            print(f"Model file units detected: {model_units_original}")
            if model_units_original == "Dl":
                print(f"  → Converted from Dl to Cl using: Cl = Dl × 2π / [l(l+1)]")
            
            # Ensure ell arrays match
            if not np.array_equal(ell_obs, ell_model):
                warnings.warn("Multipole ranges in obs and model don't match. Interpolating model.")
                cl_model = np.interp(ell_obs, ell_model, cl_model)
    
    # Load covariance if provided (using new covariance loader)
    cov = None
    cov_source = None
    cov_metadata = None
    
    if cov_file is not None:
        cov_file = Path(cov_file)
        if not cov_file.exists():
            warnings.warn(f"Covariance file not found: {cov_file}. Using diagonal uncertainties.")
        else:
            try:
                # Use new covariance loader with strict validation
                cov, cov_metadata = cov_loader.load_covariance_matrix(cov_file)
                cov_source = str(cov_file)
                
                # Ensure covariance shape matches data BEFORE filtering
                if cov.shape[0] != len(ell_obs):
                    warnings.warn(
                        f"Covariance matrix size ({cov.shape[0]}) doesn't match "
                        f"data size ({len(ell_obs)}). Using diagonal."
                    )
                    cov = None
                    cov_source = None
                    cov_metadata = None
            except Exception as e:
                warnings.warn(f"Failed to load covariance from {cov_file}: {e}\n"
                            f"Using diagonal uncertainties.")
                cov = None
                cov_source = None
                cov_metadata = None
    
    # Validate sigma is reasonable
    if np.any(sigma_obs <= 0):
        n_invalid = np.sum(sigma_obs <= 0)
        raise ValueError(
            f"Invalid uncertainties detected: {n_invalid} sigma values are <= 0.\n"
            f"All uncertainties must be positive. Check observation file format."
        )
    
    if np.any(sigma_obs < 1e-10):
        n_tiny = np.sum(sigma_obs < 1e-10)
        warnings.warn(
            f"{n_tiny} uncertainty values are suspiciously small (< 1e-10). "
            f"This may indicate units mismatch or incorrect file format."
        )
    
    # Check for reasonable sigma-to-signal ratio
    if len(cl_obs) > 0:
        sigma_to_signal = np.median(sigma_obs / np.abs(cl_obs))
        if sigma_to_signal < 1e-6:
            warnings.warn(
                f"Uncertainty-to-signal ratio is very small ({sigma_to_signal:.2e}). "
                f"This may indicate units mismatch: sigma in Cl units but cl_obs in Dl units or vice versa."
            )
        elif sigma_to_signal > 10.0:
            warnings.warn(
                f"Uncertainty-to-signal ratio is very large ({sigma_to_signal:.2e}). "
                f"This may indicate units mismatch or very poor signal quality."
            )
    
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
    
    # Determine supported whitening modes
    if cov is not None:
        whitening_mode_supported = ['none', 'diag', 'full']
    else:
        whitening_mode_supported = ['none', 'diag']
    
    # Determine sigma method
    sigma_method = "from_file"  # Default
    
    # Assemble data dictionary with units metadata
    data = {
        'ell': ell,
        'cl_obs': cl_obs,
        'cl_model': cl_model,
        'sigma': sigma_obs,
        'cov': cov,
        'cov_source': cov_source,
        'cov_metadata': cov_metadata,
        'whitening_mode_supported': whitening_mode_supported,
        'dataset': dataset_name,
        'spectrum_type': spectrum_type,
        'ell_range': (int(ell_min), int(ell_max)),
        'n_multipoles': len(ell),
        # Units metadata (NEW)
        'obs_units': obs_units,
        'model_units_original': model_units_original,
        'model_units_used': 'Cl',  # Both obs and model converted to Cl
        'sigma_method': sigma_method
    }
    
    return data


def detect_units_from_header_or_magnitude(header_lines, ell, values):
    """
    Detect whether data is in Dl or Cl units.
    
    Uses a two-stage approach:
    1. Header-based detection: Look for "Dl" or "Cl" keywords in header
    2. Magnitude-based detection: If median value > DL_CL_THRESHOLD for ell > 10, likely Dl
    
    Parameters
    ----------
    header_lines : list of str
        Comment lines from the file (lines starting with #)
    ell : ndarray
        Multipole moments
    values : ndarray
        Power spectrum values
    
    Returns
    -------
    str
        "Dl" or "Cl"
    """
    # Stage 1: Header-based detection
    for line in header_lines:
        line_upper = line.upper()
        # Look for explicit Dl or Cl markers
        # Common patterns: "Dl", "D_l", "D(l)", "C_l", "Cl", "C(l)"
        if any(pattern in line_upper for pattern in ['DL', 'D_L', 'D(L)', 'D L']):
            # Check it's not part of "dDl" (error column)
            if not any(pattern in line_upper for pattern in ['DDL', '-DL', '+DL']):
                return "Dl"
        if any(pattern in line_upper for pattern in ['CL', 'C_L', 'C(L)', 'C L']) and 'DL' not in line_upper:
            return "Cl"
    
    # Stage 2: Magnitude-based detection
    # Heuristic: if median value > DL_CL_THRESHOLD for ell > 10, likely Dl format
    if len(ell) > 0 and np.any(ell > 10):
        median_val = np.median(values[ell > 10]) if np.any(ell > 10) else np.median(values)
        if median_val > DL_CL_THRESHOLD:
            return "Dl"
    
    # Default: assume Cl
    return "Cl"


def _load_planck_text(filepath, spectrum_type="TT", _skip_size_validation=False):
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
    spectrum_type : str
        Type of spectrum to extract: "TT", "EE", "TE", or "BB"
    _skip_size_validation : bool, optional
        Internal parameter for testing. If True, skips file size validation.
        Default False.
    
    Returns
    -------
    ell : ndarray
        Multipole moments (integers)
    cl : ndarray
        Power spectrum values (Cl units, μK²)
    sigma : ndarray
        Uncertainties (1-sigma, Cl units, μK²)
    units : str
        Units detected/used: "Dl" or "Cl" (before conversion to Cl)
    """
    # First, check if file is HTML (indicates wrong URL or 404)
    # Use the common utility function for consistent detection
    if utils.detect_html(filepath):
        raise ValueError(
            f"HTML detected in {filepath}. This likely means:\n"
            f"  - Downloaded from wrong URL (got 404 page)\n"
            f"  - File doesn't exist at the specified location\n"
            f"  - Check URL and use correct PR3 cosmoparams directory:\n"
            f"    https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/"
        )
    
    # Read file and scan through comment lines to find the header with column names
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # PART B.1: Preflight sanity check - detect likelihood/parameter files
    # Read first non-comment line and count data rows
    first_data_line = None
    data_row_count = 0
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        # Found a data line
        if first_data_line is None:
            first_data_line = stripped
        data_row_count += 1
    
    # Check if first data line contains likelihood markers
    if first_data_line:
        if '-log(like)' in first_data_line.lower() or 'loglike' in first_data_line.lower():
            raise ValueError(
                f"Invalid spectrum file: {filepath}\n\n"
                f"This file appears to be a Planck likelihood/parameter table, not a power spectrum.\n"
                f"The data contains '-log(Like)' or 'logLike' values.\n\n"
                f"For CMB analysis, you need a TT power spectrum file, not cosmological parameters.\n\n"
                f"Recommended actions:\n"
                f"  1. Use COM_PowerSpect_CMB-TT-full_R3.01.txt (observed spectrum)\n"
                f"  2. For model, use a theoretical ΛCDM spectrum from CAMB/CLASS\n"
                f"  3. Do NOT use files with 'minimum' or 'plikHM' in the name as model input\n\n"
                f"See RUNBOOK_REAL_DATA.md for correct file selection."
            )
    
    # Check if file is suspiciously small (likely not a spectrum)
    # Typical TT spectra have hundreds to thousands of multipoles
    # A file with < 50 data rows is likely a parameter table or corrupted
    # Skip this check for unit tests with synthetic data
    if not _skip_size_validation and data_row_count < 50:
        filename = filepath.name if hasattr(filepath, 'name') else str(filepath)
        raise ValueError(
            f"Invalid spectrum file: {filepath}\n\n"
            f"File has only {data_row_count} data rows (expected ~50-2500 for TT spectrum).\n"
            f"This is likely NOT a power spectrum file.\n\n"
            f"Possible causes:\n"
            f"  1. Wrong file (cosmological parameter table instead of spectrum)\n"
            f"  2. Corrupted or truncated download\n"
            f"  3. Downloaded HTML error page instead of actual data\n\n"
            f"Recommended actions:\n"
            f"  - Re-download COM_PowerSpect_CMB-TT-full_R3.01.txt (~167 KB, ~2479 rows)\n"
            f"  - Verify file size matches expected: ~167 KB for TT-full\n"
            f"  - If using model file, ensure it's a power spectrum (not 'minimum' file)\n\n"
            f"See RUNBOOK_REAL_DATA.md for correct file selection."
        )
    
    # Detect if this is a PR3 "minimum" model file or TT-full spectrum file
    # Check both filename and file content (scan comment lines for header)
    filename = filepath.name if hasattr(filepath, 'name') else str(filepath)
    is_minimum_by_name = '-minimum_' in filename or '-minimum-theory' in filename or 'plikHM' in filename
    
    # Scan through comment lines to find the header with column names
    is_minimum_by_content = False
    is_tt_full_format = False
    
    # First pass: Look for TT-full format header (this is very specific)
    for line in lines[:10]:  # Check first 10 lines for header
        stripped = line.strip()
        if not stripped.startswith('#'):
            continue
            
        header_cols = stripped.lstrip('#').strip().split()
        
        # Skip lines with too few words
        if len(header_cols) < 2:
            continue
        
        # Check for TT-full format: exactly ['l','Dl','-dDl','+dDl'] or ['ell','Dl','-dDl','+dDl']
        if len(header_cols) == 4:
            col0 = header_cols[0].lower()
            col1 = header_cols[1]
            col2 = header_cols[2]
            col3 = header_cols[3]
            
            if ((col0 in ['l', 'ell']) and 
                (col1 in ['Dl', 'DL', 'dl']) and
                (col2 in ['-dDl', '-dDL', '-ddl', '-Dl', '-DL', '-dl']) and
                (col3 in ['+dDl', '+dDL', '+ddl', '+Dl', '+DL', '+dl'])):
                is_tt_full_format = True
                break
    
    # Second pass: If not TT-full, look for minimum format indicators
    if not is_tt_full_format:
        for line in lines[:10]:
            stripped = line.strip()
            if not stripped.startswith('#'):
                continue
                
            header_cols = stripped.lstrip('#').strip().split()
            
            if len(header_cols) < 2:
                continue
            
            # Check for specific column names indicating multiple spectra
            if any(col.upper() in ['TT', 'TE', 'EE', 'BB', 'DL_TT', 'CL_TT', 'DLTT', 'CLTT'] for col in header_cols):
                is_minimum_by_content = True
                break
    
    # Route to minimum format loader only if explicitly identified
    if is_minimum_by_name or is_minimum_by_content:
        return _load_planck_minimum_format(filepath, spectrum_type=spectrum_type)
    
    # Handle TT-full format (4 columns: ell, Dl, -dDl, +dDl)
    # Note: This format typically only applies to TT spectra
    if is_tt_full_format:
        if spectrum_type != "TT":
            warnings.warn(f"TT-full format detected but {spectrum_type} requested. This may not work as expected.")
        return _load_planck_tt_full_format(filepath)
    
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
    
    # Collect header lines for units detection
    header_lines = [line for line in lines if line.strip().startswith('#')]
    
    # Detect units using improved two-stage detection
    units_detected = detect_units_from_header_or_magnitude(header_lines, ell, cl)
    
    # Convert from Dl to Cl if needed
    if units_detected == "Dl":
        # Convert from Dl to Cl: Cl = Dl * 2π / [l(l+1)]
        with np.errstate(divide='ignore', invalid='ignore'):
            cl = cl * (2.0 * np.pi) / (ell * (ell + 1.0))
            cl[ell == 0] = 0.0
            cl[ell == 1] = 0.0
    
    # Sigma may or may not be present
    if data.shape[1] >= 3:
        sigma = data[:, 2]
        
        # If sigma looks like it's also in Dl units (for consistency with converted cl)
        # Check if it's large and needs conversion
        if units_detected == "Dl":
            # Convert sigma from Dl units to Cl units
            with np.errstate(divide='ignore', invalid='ignore'):
                sigma = sigma * (2.0 * np.pi) / (ell * (ell + 1.0))
                sigma[ell == 0] = 0.0
                sigma[ell == 1] = 0.0
    else:
        # If no sigma provided, estimate from scatter (not ideal)
        warnings.warn(f"No uncertainties in {filepath}. Estimating from {DEFAULT_SIGMA_FRACTION*100}% of signal.")
        sigma = DEFAULT_SIGMA_FRACTION * np.abs(cl)
    
    return ell, cl, sigma, units_detected


def _load_planck_tt_full_format(filepath):
    """
    Load Planck PR3 TT-full spectrum format.
    
    Expected format (4 columns with asymmetric error bars):
    # l  Dl  -dDl  +dDl
    30  1000  -10  10
    31  990   -11  9
    ...
    
    The file contains:
    - Column 0: multipole moment (ell)
    - Column 1: Dl values (power spectrum in Dl units)
    - Column 2: negative error bar (-dDl, typically negative value)
    - Column 3: positive error bar (+dDl, typically positive value)
    
    We convert Dl to Cl and compute symmetric sigma as the average of the 
    absolute values of the two error bars: sigma = 0.5 * (|+dDl| + |-dDl|)
    
    Parameters
    ----------
    filepath : Path
        Path to TT-full format file
    
    Returns
    -------
    ell : ndarray
        Multipole moments (integers)
    cl : ndarray
        Power spectrum values in Cl units (converted from Dl)
    sigma : ndarray
        Uncertainties (1-sigma, symmetric average from asymmetric error bars)
    units : str
        Units detected: "Dl" (always for TT-full format)
    """
    try:
        data = np.loadtxt(filepath, comments='#')
    except Exception as e:
        raise ValueError(f"Failed to load TT-full format file {filepath}: {e}")
    
    # Handle single-row case (numpy returns 1D array for single row)
    if data.ndim == 1:
        data = data.reshape(1, -1)
    
    if data.ndim != 2:
        raise ValueError(f"Expected 2D array from {filepath}, got shape {data.shape}")
    
    if data.shape[1] != 4:
        raise ValueError(
            f"TT-full format expects exactly 4 columns (l, Dl, -dDl, +dDl), "
            f"got {data.shape[1]} columns in {filepath}"
        )
    
    ell = data[:, 0].astype(int)
    dl = data[:, 1]
    minus_ddl = data[:, 2]  # Negative error bar
    plus_ddl = data[:, 3]   # Positive error bar
    
    # Convert Dl to Cl: Cl = Dl * 2π / [l(l+1)]
    # Handle ell=0 and ell=1 cases to avoid division by zero
    with np.errstate(divide='ignore', invalid='ignore'):
        cl = dl * (2.0 * np.pi) / (ell * (ell + 1.0))
        cl[ell == 0] = 0.0
        cl[ell == 1] = 0.0
    
    # For sigma, compute symmetric average of asymmetric error bars
    # sigma = 0.5 * (|+dDl| + |-dDl|)
    sigma_dl = 0.5 * (np.abs(plus_ddl) + np.abs(minus_ddl))
    
    # Convert sigma from Dl units to Cl units using the same conversion factor
    with np.errstate(divide='ignore', invalid='ignore'):
        sigma = sigma_dl * (2.0 * np.pi) / (ell * (ell + 1.0))
        sigma[ell == 0] = 0.0
        sigma[ell == 1] = 0.0
    
    # Ensure no zeros in sigma (for numerical stability)
    sigma[sigma == 0] = 1e-10
    
    return ell, cl, sigma, "Dl"


def _load_planck_minimum_format(filepath, spectrum_type="TT"):
    """
    Load Planck PR3 "minimum" model file format.
    
    The PR3 minimum model file has a header line with column names followed by data.
    Format example:
    # L  TT  TE  EE  BB  PP  TP
    2  5.51e+01  -1.18e+01  1.34e-02  ...
    3  2.29e+02  -2.99e+01  6.89e-03  ...
    
    We extract the 'L' (multipole) and the requested spectrum column (TT/EE/TE/BB).
    The values are typically in Dl units (l(l+1)Cl/2π) and need to be
    converted to Cl for consistency with cmb_comb residuals.
    
    Parameters
    ----------
    filepath : Path
        Path to minimum format file
    spectrum_type : str
        Type of spectrum to extract: "TT", "EE", "TE", or "BB"
    
    Returns
    -------
    ell : ndarray
        Multipole moments (integers)
    cl : ndarray
        Power spectrum in Cl units (μK²)
    sigma : ndarray
        Uncertainties (estimated as 1% since not provided in model file)
    units : str
        Units detected/used: "Dl" or "Cl"
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
            # Check if it contains expected column names for minimum format
            # Look for spectrum indicators: TT, TE, EE, BB, or Dl/Cl
            if any(keyword in stripped for keyword in ['TT', 'TE', 'EE', 'BB', 'Dl', 'Cl', 'DL', 'CL']):
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
            
            # Handle single-row case
            if data.ndim == 1:
                data = data.reshape(1, -1)
            
            if data.shape[1] < 2:
                raise ValueError(f"Expected at least 2 columns, got {data.shape[1]}")
            
            ell = data[:, 0].astype(int)
            cl_or_dl = data[:, 1]
            
            # Collect header lines for units detection
            header_lines = [line for line in lines if line.strip().startswith('#')]
            
            # Detect units using improved detection
            units_detected = detect_units_from_header_or_magnitude(header_lines, ell, cl_or_dl)
            
            if units_detected == "Dl":
                # Convert Dl to Cl: Dl = l(l+1)Cl/(2π)
                cl = cl_or_dl * (2.0 * np.pi) / (ell * (ell + 1.0))
                cl[ell == 0] = 0.0  # Handle ell=0 case
            else:
                cl = cl_or_dl
            
            sigma = DEFAULT_SIGMA_FRACTION * np.abs(cl)
            return ell, cl, sigma, units_detected
            
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
    
    # Find spectrum column (may be Dl_XX, Cl_XX, or just XX where XX is TT/EE/TE/BB)
    spectrum_col = None
    spectrum_upper = spectrum_type.upper()
    for i, col in enumerate(columns):
        col_upper = col.upper()
        if col_upper in [spectrum_upper, f'DL_{spectrum_upper}', f'CL_{spectrum_upper}', 
                         f'DL{spectrum_upper}', f'CL{spectrum_upper}']:
            spectrum_col = i
            break
    
    if spectrum_col is None:
        # Check if this looks like a TT-full spectrum file
        filename = filepath.name if hasattr(filepath, 'name') else str(filepath)
        if len(columns) == 4:
            col0 = columns[0].lower()
            col1 = columns[1]
            if col0 in ['l', 'ell'] and col1 in ['Dl', 'DL', 'dl']:
                raise ValueError(
                    f"Could not find {spectrum_type} column in header: {columns}\n"
                    f"This file ({filename}) looks like a TT-full spectrum with header "
                    f"'l Dl -dDl +dDl' or similar.\n"
                    f"This format should be handled by the simple loader, not the minimum format loader.\n"
                    f"Please report this as a bug - the file detection logic may need adjustment."
                )
        raise ValueError(f"Could not find {spectrum_type} column in header: {columns}")
    
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
    cl_or_dl = data[:, spectrum_col]
    
    # Determine if Dl or Cl format
    # First check column name for explicit "Dl_" or "Cl_" prefix
    col_name_upper = columns[spectrum_col].upper()
    if col_name_upper.startswith('DL_') or col_name_upper.startswith('DL'):
        units_detected = "Dl"
    elif col_name_upper.startswith('CL_') or col_name_upper.startswith('CL'):
        units_detected = "Cl"
    else:
        # Fall back to magnitude-based detection
        header_lines_minimal = [header_line]  # Use the parsed header
        units_detected = detect_units_from_header_or_magnitude(header_lines_minimal, ell, cl_or_dl)
    
    if units_detected == "Dl":
        # Convert Dl to Cl: Cl = Dl * 2π / [l(l+1)]
        with np.errstate(divide='ignore', invalid='ignore'):
            cl = cl_or_dl * (2.0 * np.pi) / (ell * (ell + 1.0))
            cl[ell == 0] = 0.0  # Handle ell=0
            cl[ell == 1] = 0.0  # Handle ell=1
    else:
        cl = cl_or_dl
    
    # Model files typically don't include uncertainties
    # Estimate as DEFAULT_SIGMA_FRACTION of signal
    sigma = DEFAULT_SIGMA_FRACTION * np.abs(cl)
    sigma[sigma == 0] = 1e-10  # Avoid exact zeros
    
    return ell, cl, sigma, units_detected


def _load_planck_fits(filepath, spectrum_type="TT"):
    """
    Load Planck data from FITS file.
    
    Parameters
    ----------
    filepath : Path
        Path to FITS file
    spectrum_type : str
        Type of spectrum to extract: "TT", "EE", "TE", or "BB"
    
    Returns
    -------
    ell : ndarray
        Multipole moments
    cl : ndarray
        Power spectrum values (Cl units)
    sigma : ndarray
        Uncertainties
    units : str
        Units detected: "Cl" (FITS files typically use Cl)
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
            
            # Column names depend on spectrum type
            cl_names = [spectrum_type, spectrum_type.upper(), spectrum_type.lower(), 
                       f'C_{spectrum_type}', f'C_{spectrum_type.upper()}',
                       'C_ell', 'C_ELL', 'CL', 'POWER']
            sigma_names = [f'{spectrum_type}_error', f'{spectrum_type.upper()}_error',
                          'sigma', 'SIGMA', 'ERROR', 'ERR']
            
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
                raise ValueError(f"No {spectrum_type} power spectrum column found in {filepath}. "
                               f"Available columns: {list(data.names)}")
            
            sigma = None
            for name in sigma_names:
                if name in data.names:
                    sigma = data[name]
                    break
            
            if sigma is None:
                warnings.warn(f"No uncertainty column found in {filepath}. Estimating from 1% of signal.")
                sigma = 0.01 * np.abs(cl)
            
            # FITS files typically use Cl units (not Dl)
            return np.array(ell, dtype=int), np.array(cl), np.array(sigma), "Cl"
    
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
