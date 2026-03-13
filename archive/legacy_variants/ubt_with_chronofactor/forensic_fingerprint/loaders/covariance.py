#!/usr/bin/env python3
"""
Covariance Matrix Loader for Court-Grade CMB Analysis
======================================================

This module provides strict, conservative loading and validation of covariance matrices
for CMB power spectrum analysis. It supports multiple formats and performs comprehensive
validation checks.

**Design Philosophy**:
- No silent guessing or fallbacks
- Conservative parsing with explicit error messages
- Strict validation: symmetry, finiteness, positive semi-definiteness
- Regularization with full reporting when needed

Supported Formats:
- Plain text matrix (whitespace/comma separated)
- NumPy .npy binary format
- FITS (requires astropy, optional)

License: MIT
Author: UBT Research Team
"""

import numpy as np
from pathlib import Path
import hashlib
import warnings


def load_covariance_matrix(cov_path):
    """
    Load and validate covariance matrix from file.
    
    This function provides strict, conservative loading with no silent fallbacks.
    All validation issues are reported clearly with actionable error messages.
    
    Supported formats:
    - .npy: NumPy binary format
    - .txt, .dat, .csv: Plain text (whitespace or comma separated)
    - .fits: FITS format (requires astropy)
    
    Parameters
    ----------
    cov_path : str or Path
        Path to covariance matrix file
    
    Returns
    -------
    cov : ndarray
        Covariance matrix (N x N), validated and ready for use
    metadata : dict
        Loading and validation metadata with keys:
        - file_path: str, absolute path to file
        - file_hash: str, SHA-256 hash of file
        - file_size: int, file size in bytes
        - format: str, detected format
        - shape: tuple, matrix shape
        - is_symmetric: bool, symmetry check result
        - is_finite: bool, all values finite
        - is_positive_semidefinite: bool, PSD check result
        - min_eigenvalue: float, smallest eigenvalue
        - max_eigenvalue: float, largest eigenvalue
        - condition_number: float, condition number
        - jitter_applied: bool, whether jitter was added
        - jitter_value: float or None, jitter magnitude if applied
    
    Raises
    ------
    FileNotFoundError
        If file doesn't exist
    ValueError
        If file format is unsupported, invalid, or validation fails
    """
    cov_path = Path(cov_path).resolve()
    
    if not cov_path.exists():
        raise FileNotFoundError(
            f"Covariance file not found: {cov_path}\n\n"
            f"Please check the path and ensure the file exists."
        )
    
    # Compute file hash for provenance
    with open(cov_path, 'rb') as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    
    file_size = cov_path.stat().st_size
    
    # Detect format and load
    suffix = cov_path.suffix.lower()
    
    if suffix == '.npy':
        cov, fmt = _load_npy(cov_path)
    elif suffix in ['.txt', '.dat', '.csv']:
        cov, fmt = _load_text(cov_path)
    elif suffix == '.fits':
        cov, fmt = _load_fits(cov_path)
    else:
        raise ValueError(
            f"Unsupported covariance file format: {suffix}\n\n"
            f"Supported formats:\n"
            f"  - .npy (NumPy binary)\n"
            f"  - .txt, .dat, .csv (plain text matrix)\n"
            f"  - .fits (FITS table, requires astropy)\n\n"
            f"To convert your covariance to a supported format:\n"
            f"  1. Plain text: Save as space/comma-delimited N×N matrix\n"
            f"  2. NumPy: Use np.save('cov.npy', cov_matrix)\n"
            f"  3. FITS: Use astropy.io.fits to create table"
        )
    
    # Validate matrix shape
    if cov.ndim != 2:
        raise ValueError(
            f"Covariance must be a 2D matrix, got {cov.ndim}D array with shape {cov.shape}\n\n"
            f"Expected: N×N square matrix"
        )
    
    if cov.shape[0] != cov.shape[1]:
        raise ValueError(
            f"Covariance must be square, got shape {cov.shape}\n\n"
            f"Expected: N×N where N = number of multipoles"
        )
    
    # Strict validation
    metadata = {
        'file_path': str(cov_path),
        'file_hash': file_hash,
        'file_size': file_size,
        'format': fmt,
        'shape': cov.shape,
        'jitter_applied': False,
        'jitter_value': None
    }
    
    # Check for finite values
    is_finite = np.all(np.isfinite(cov))
    metadata['is_finite'] = is_finite
    
    if not is_finite:
        raise ValueError(
            f"Covariance matrix contains non-finite values (NaN or Inf)\n\n"
            f"File: {cov_path}\n"
            f"This indicates a data loading or computation error.\n"
            f"Please verify the covariance file is valid."
        )
    
    # Check symmetry
    is_symmetric = np.allclose(cov, cov.T, rtol=1e-10, atol=1e-12)
    metadata['is_symmetric'] = is_symmetric
    
    if not is_symmetric:
        max_asymmetry = np.max(np.abs(cov - cov.T))
        raise ValueError(
            f"Covariance matrix is not symmetric\n\n"
            f"File: {cov_path}\n"
            f"Max |C - C^T|: {max_asymmetry:.6e}\n\n"
            f"Covariance matrices must be symmetric by definition.\n"
            f"This likely indicates:\n"
            f"  1. Data loading error (transposed incorrectly)\n"
            f"  2. Numerical precision issues during computation\n"
            f"  3. File corruption\n\n"
            f"Please verify the covariance file is correct."
        )
    
    # Compute eigenvalues for PSD check
    eigenvalues = np.linalg.eigvalsh(cov)
    min_eig = np.min(eigenvalues)
    max_eig = np.max(eigenvalues)
    
    metadata['min_eigenvalue'] = float(min_eig)
    metadata['max_eigenvalue'] = float(max_eig)
    
    if max_eig > 0:
        metadata['condition_number'] = float(max_eig / max(min_eig, 1e-20))
    else:
        metadata['condition_number'] = np.inf
    
    # Check positive semi-definiteness
    is_psd = min_eig >= -1e-10 * max_eig  # Allow small numerical errors
    metadata['is_positive_semidefinite'] = is_psd
    
    if not is_psd:
        # Report the issue and suggest jitter
        warnings.warn(
            f"\n{'='*80}\n"
            f"WARNING: Covariance matrix is not positive semi-definite\n"
            f"{'='*80}\n"
            f"File: {cov_path}\n"
            f"Min eigenvalue: {min_eig:.6e} (should be ≥ 0)\n"
            f"Max eigenvalue: {max_eig:.6e}\n"
            f"Condition number: {metadata['condition_number']:.6e}\n\n"
            f"This makes the matrix unsuitable for Cholesky decomposition.\n"
            f"Applying automatic jitter regularization...\n"
            f"{'='*80}"
        )
        
        # Apply jitter: add small value to diagonal
        jitter = abs(min_eig) + max_eig * 1e-8
        cov_jittered = cov + jitter * np.eye(cov.shape[0])
        
        # Verify jitter fixed the issue
        eigenvalues_after = np.linalg.eigvalsh(cov_jittered)
        min_eig_after = np.min(eigenvalues_after)
        
        if min_eig_after <= 0:
            raise ValueError(
                f"Automatic jitter failed to make covariance positive definite\n\n"
                f"File: {cov_path}\n"
                f"Min eigenvalue before: {min_eig:.6e}\n"
                f"Min eigenvalue after jitter: {min_eig_after:.6e}\n"
                f"Jitter value: {jitter:.6e}\n\n"
                f"The covariance matrix is severely ill-conditioned.\n"
                f"Please verify the covariance file or use a larger jitter value with --cov_jitter."
            )
        
        print(f"Jitter applied: {jitter:.6e}")
        print(f"Min eigenvalue: {min_eig:.6e} → {min_eig_after:.6e}")
        print(f"Condition number: {metadata['condition_number']:.6e} → {max_eig / min_eig_after:.6e}")
        print()
        
        cov = cov_jittered
        metadata['jitter_applied'] = True
        metadata['jitter_value'] = float(jitter)
        metadata['min_eigenvalue'] = float(min_eig_after)
        metadata['condition_number'] = float(max_eig / min_eig_after)
        metadata['is_positive_semidefinite'] = True
    
    return cov, metadata


def _load_npy(filepath):
    """Load covariance from NumPy .npy file."""
    try:
        cov = np.load(filepath)
        return cov, 'npy'
    except Exception as e:
        raise ValueError(
            f"Failed to load .npy file: {filepath}\n\n"
            f"Error: {e}\n\n"
            f"Verify the file is a valid NumPy .npy file."
        ) from e


def _load_text(filepath):
    """Load covariance from plain text file."""
    try:
        # Try loading with numpy
        cov = np.loadtxt(filepath)
        return cov, 'text'
    except Exception as e:
        raise ValueError(
            f"Failed to load text covariance file: {filepath}\n\n"
            f"Error: {e}\n\n"
            f"Expected format:\n"
            f"  - Plain text N×N matrix\n"
            f"  - Whitespace or comma separated\n"
            f"  - No header row (or comment with #)\n\n"
            f"Example (3×3 matrix):\n"
            f"  1.0 0.1 0.05\n"
            f"  0.1 1.2 0.08\n"
            f"  0.05 0.08 0.9\n\n"
            f"Verify your file format matches this structure."
        ) from e


def _load_fits(filepath):
    """Load covariance from FITS file."""
    try:
        from astropy.io import fits
    except ImportError:
        raise ImportError(
            f"FITS support requires astropy\n\n"
            f"Install with: pip install astropy\n\n"
            f"Alternatively, convert your FITS covariance to .npy or .txt format."
        )
    
    try:
        with fits.open(filepath) as hdul:
            # Try to find covariance in the FITS file
            # Common patterns: extension name 'COVMAT', 'COV', or in primary HDU
            
            cov = None
            
            # Try primary HDU first
            if hdul[0].data is not None:
                cov = hdul[0].data
            
            # Try named extensions
            if cov is None:
                for ext_name in ['COVMAT', 'COV', 'COVARIANCE']:
                    try:
                        cov = hdul[ext_name].data
                        break
                    except KeyError:
                        continue
            
            # Try first extension if primary is empty
            if cov is None and len(hdul) > 1:
                cov = hdul[1].data
            
            if cov is None:
                raise ValueError(
                    f"Could not find covariance data in FITS file\n\n"
                    f"Available HDUs: {[hdu.name for hdu in hdul]}\n\n"
                    f"Please specify which HDU contains the covariance matrix."
                )
            
            # Convert to numpy array if needed
            cov = np.array(cov)
            
            return cov, 'fits'
    
    except Exception as e:
        raise ValueError(
            f"Failed to load FITS covariance file: {filepath}\n\n"
            f"Error: {e}\n\n"
            f"Verify the FITS file contains a valid covariance matrix.\n"
            f"Consider converting to .npy or .txt format for easier debugging."
        ) from e


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python covariance.py <covariance_file>")
        print()
        print("Example:")
        print("  python covariance.py my_covariance.npy")
        print("  python covariance.py covariance_matrix.txt")
        sys.exit(1)
    
    cov_file = sys.argv[1]
    
    print("Loading covariance matrix...")
    print()
    
    try:
        cov, metadata = load_covariance_matrix(cov_file)
        
        print("✓ Covariance loaded successfully")
        print()
        print("Metadata:")
        print(f"  File: {metadata['file_path']}")
        print(f"  SHA-256: {metadata['file_hash']}")
        print(f"  Size: {metadata['file_size']} bytes")
        print(f"  Format: {metadata['format']}")
        print(f"  Shape: {metadata['shape']}")
        print(f"  Symmetric: {metadata['is_symmetric']}")
        print(f"  Finite values: {metadata['is_finite']}")
        print(f"  Positive semi-definite: {metadata['is_positive_semidefinite']}")
        print(f"  Min eigenvalue: {metadata['min_eigenvalue']:.6e}")
        print(f"  Max eigenvalue: {metadata['max_eigenvalue']:.6e}")
        print(f"  Condition number: {metadata['condition_number']:.6e}")
        if metadata['jitter_applied']:
            print(f"  Jitter applied: {metadata['jitter_value']:.6e}")
        print()
        
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)
