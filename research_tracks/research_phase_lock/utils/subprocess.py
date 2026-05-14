#!/usr/bin/env python3
"""
subprocess.py

Subprocess utilities for calling external tools.

Provides safe wrappers for:
- Running subprocess commands
- Capturing stdout/stderr
- Error handling and logging

Author: UBT Research Team
License: See repository LICENSE.md
"""

import subprocess
import sys
from typing import List, Optional, Tuple


def run_command(
    cmd: List[str],
    cwd: Optional[str] = None,
    capture_output: bool = True,
    check: bool = True,
    verbose: bool = False
) -> Tuple[int, str, str]:
    """
    Run a command via subprocess.
    
    Args:
        cmd: Command and arguments as list
        cwd: Working directory (None = current)
        capture_output: Whether to capture stdout/stderr
        check: Whether to raise exception on non-zero exit
        verbose: Whether to print command before running
        
    Returns:
        Tuple of (returncode, stdout, stderr)
        
    Raises:
        subprocess.CalledProcessError: If check=True and command fails
    """
    if verbose:
        print(f"[subprocess] Running: {' '.join(cmd)}", file=sys.stderr)
    
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=capture_output,
            text=True,
            check=check
        )
        
        stdout = result.stdout if capture_output else ""
        stderr = result.stderr if capture_output else ""
        
        return result.returncode, stdout, stderr
        
    except subprocess.CalledProcessError as e:
        # Re-raise with more context
        # When capture_output=True, stdout and stderr are always available
        stdout = e.stdout or ""
        stderr = e.stderr or ""
        
        if verbose:
            print(f"[subprocess] Command failed with exit code {e.returncode}", file=sys.stderr)
            if stderr:
                print(f"[subprocess] stderr: {stderr}", file=sys.stderr)
        
        raise


def run_python_module(
    module: str,
    args: List[str],
    cwd: Optional[str] = None,
    verbose: bool = False
) -> Tuple[int, str, str]:
    """
    Run a Python module using the current Python interpreter.
    
    Args:
        module: Module name (e.g., 'forensic_fingerprint.tools.unified_phase_lock_scan')
        args: Command-line arguments
        cwd: Working directory
        verbose: Whether to print command
        
    Returns:
        Tuple of (returncode, stdout, stderr)
    """
    cmd = [sys.executable, '-m', module] + args
    return run_command(cmd, cwd=cwd, verbose=verbose)
