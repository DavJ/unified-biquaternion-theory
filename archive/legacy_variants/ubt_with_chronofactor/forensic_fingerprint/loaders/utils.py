#!/usr/bin/env python3
"""
Common utility functions for CMB data loaders.

License: MIT
Author: UBT Research Team
"""


def detect_html(filepath):
    """
    Check if file is an HTML error page (404/redirect).
    
    This is a critical safeguard against silent failures when downloading
    data files from remote archives. If a URL returns a 404 or redirect page,
    the download may save HTML content instead of the expected data file.
    
    Without this check, loaders would attempt to parse HTML as numeric data,
    leading to either crashes or (worse) silent garbage results.
    
    Parameters
    ----------
    filepath : str or Path
        File to check
    
    Returns
    -------
    bool
        True if file contains HTML markers, False otherwise
    
    Examples
    --------
    >>> detect_html('data.txt')  # Normal data file
    False
    >>> detect_html('error_404.html')  # HTML error page
    True
    
    Notes
    -----
    Checks first 1KB of file for common HTML markers:
    - <html (case-insensitive)
    - <!doctype (case-insensitive)
    
    This is a heuristic check and may not catch all HTML variants,
    but catches the most common error pages from data archives.
    """
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            first_kb = f.read(1024)
            lower = first_kb.lower()
            return '<html' in lower or '<!doctype' in lower
    except Exception:
        # If we can't read the file, let the loader handle it
        return False


def validate_not_html(filepath, description="file"):
    """
    Validate that a file is not an HTML error page, raising if it is.
    
    Parameters
    ----------
    filepath : str or Path
        File to validate
    description : str
        Human-readable description for error message
    
    Raises
    ------
    ValueError
        If file is detected as HTML
    
    Examples
    --------
    >>> validate_not_html('data.txt')  # OK
    >>> validate_not_html('error.html', 'model file')
    ValueError: HTML detected in model file
    """
    if detect_html(filepath):
        raise ValueError(
            f"HTML detected in {description}: {filepath}\n"
            f"This usually indicates a download error (404 or redirect page).\n"
            f"Delete the file and re-download from the correct URL."
        )
