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
        frame = None
        try:
            frame = inspect.currentframe()
            caller_frame = frame.f_back
            caller_file = caller_frame.f_globals.get('__file__')
            if caller_file:
                start_path = Path(caller_file).resolve().parent
            else:
                start_path = Path.cwd()
        finally:
            # Clean up frame references to prevent memory leaks
            del frame
    else:
        start_path = Path(start_path).resolve()
    
    current = start_path
    # Prioritize .git as the most reliable marker.
    # NOTE: This repo is frequently distributed as a ZIP without a .git directory,
    # so we include stable top-level files as additional markers.
    
    # First pass: Look for .git directory (most reliable)
    temp = current
    while temp != temp.parent:
        if (temp / '.git').exists():
            return temp
        temp = temp.parent
    # Check root directory too
    if (current.parent / '.git').exists():
        return current.parent
    
    # Second pass: If no .git found, look for combination of markers
    # that indicate the repository root (not just a subdirectory with README)
    # A true repo root should have multiple of these markers
    markers = [
        'pyproject.toml',
        'pytest.ini',
        'README.md',
        'LICENSE.md',
        'Makefile',
    ]
    
    # Walk up directory tree looking for directories with multiple markers
    temp = current
    while temp != temp.parent:
        marker_count = sum(1 for marker in markers if (temp / marker).exists())
        # Repo root should have at least 3 of these markers
        if marker_count >= 3:
            return temp
        temp = temp.parent
    
    # Check root directory too
    marker_count = sum(1 for marker in markers if (current.parent / marker).exists())
    if marker_count >= 3:
        return current.parent
    
    raise FileNotFoundError(
        f"Could not find repository root. Searched from {start_path} upward. "
        f"Looking for markers: {', '.join(markers)}"
    )
