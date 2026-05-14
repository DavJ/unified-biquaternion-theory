#!/usr/bin/env python3
"""
io.py

File I/O utilities for the research harness.

Provides helpers for:
- Reading/writing YAML configs
- Reading/writing CSV results
- Creating output directories
- File path manipulation

Author: UBT Research Team
License: See repository LICENSE.md
"""

import csv
import os
import yaml
from pathlib import Path
from typing import Any, Dict, List, Optional


def load_yaml(path: str) -> Dict[str, Any]:
    """
    Load YAML configuration file.
    
    Args:
        path: Path to YAML file
        
    Returns:
        Configuration dictionary
        
    Raises:
        FileNotFoundError: If file doesn't exist
        yaml.YAMLError: If YAML is invalid
    """
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def save_yaml(data: Dict[str, Any], path: str) -> None:
    """
    Save dictionary to YAML file.
    
    Args:
        data: Data to save
        path: Output path
    """
    ensure_dir(path)
    with open(path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)


def ensure_dir(path: str) -> None:
    """
    Create directory for file path if needed.
    
    Args:
        path: File path (creates parent directory)
    """
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)


def read_csv_dict(path: str) -> List[Dict[str, str]]:
    """
    Read CSV file as list of dictionaries.
    
    Args:
        path: Path to CSV file
        
    Returns:
        List of row dictionaries (keys from header)
    """
    rows = []
    with open(path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(dict(row))
    return rows


def write_csv_dict(rows: List[Dict[str, Any]], path: str, fieldnames: Optional[List[str]] = None) -> None:
    """
    Write list of dictionaries to CSV file.
    
    Args:
        rows: List of row dictionaries
        path: Output path
        fieldnames: Column names (if None, use keys from first row)
    """
    if not rows:
        return
    
    ensure_dir(path)
    
    if fieldnames is None:
        fieldnames = list(rows[0].keys())
    
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def make_output_dir(base: str, run_id: str) -> str:
    """
    Create output directory for a run.
    
    Args:
        base: Base output directory
        run_id: Run identifier
        
    Returns:
        Full path to run directory
    """
    run_dir = os.path.join(base, run_id)
    os.makedirs(run_dir, exist_ok=True)
    return run_dir
