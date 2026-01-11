#!/usr/bin/env python3
"""
Shared utility functions for data provenance tools.

License: MIT
"""

from pathlib import Path


def find_repo_root(start_path=None):
    """
    Find repository root by walking upward from start_path.
    
    Looks for markers like .git or pyproject.toml.
    
    Parameters
    ----------
    start_path : Path or None
        Starting directory (default: directory containing the calling file)
    
    Returns
    -------
    Path
        Repository root directory
    
    Raises
    ------
    FileNotFoundError
        If no repository markers found
    """
    if start_path is None:
        # Use the caller's location, not this file's location
        import inspect
        frame = inspect.currentframe()
        caller_frame = frame.f_back
        caller_file = caller_frame.f_globals.get('__file__')
        if caller_file:
            start_path = Path(caller_file).resolve().parent
        else:
            start_path = Path.cwd()
    else:
        start_path = Path(start_path).resolve()
    
    current = start_path
    # Prioritize .git as the most reliable marker
    markers = ['.git', 'pyproject.toml', 'pytest.ini']
    
    # Walk up directory tree
    while current != current.parent:
        # Check if any marker exists in current directory
        for marker in markers:
            if (current / marker).exists():
                return current
        current = current.parent
    
    # Check root directory too
    for marker in markers:
        if (current / marker).exists():
            return current
    
    raise FileNotFoundError(
        f"Could not find repository root. Searched from {start_path} upward. "
        f"Looking for markers: {', '.join(markers)}"
    )
