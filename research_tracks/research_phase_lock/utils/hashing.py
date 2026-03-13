#!/usr/bin/env python3
"""
hashing.py

Configuration normalization and hash generation for run IDs.

This module provides utilities to:
1. Normalize configuration dictionaries to a canonical form
2. Generate deterministic run IDs based on configuration hash

Author: UBT Research Team
License: See repository LICENSE.md
"""

import hashlib
import json
from typing import Any, Dict


def normalize_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize configuration dictionary to canonical form.
    
    - Sorts keys alphabetically
    - Converts lists to tuples (for hashability)
    - Ensures consistent formatting
    
    Args:
        config: Configuration dictionary
        
    Returns:
        Normalized configuration dictionary
    """
    if isinstance(config, dict):
        return {k: normalize_config(v) for k, v in sorted(config.items())}
    elif isinstance(config, list):
        return tuple(normalize_config(item) for item in config)
    elif isinstance(config, tuple):
        return tuple(normalize_config(item) for item in config)
    else:
        return config


def config_to_hash(config: Dict[str, Any]) -> str:
    """
    Generate a deterministic hash from configuration.
    
    The hash is computed from the normalized JSON representation
    of the configuration. This ensures that identical configurations
    (regardless of key ordering) produce the same hash.
    
    Args:
        config: Configuration dictionary
        
    Returns:
        Hexadecimal hash string (first 16 characters of SHA256)
    """
    normalized = normalize_config(config)
    json_str = json.dumps(normalized, sort_keys=True, separators=(',', ':'))
    hash_obj = hashlib.sha256(json_str.encode('utf-8'))
    return hash_obj.hexdigest()[:16]


def generate_run_id(config: Dict[str, Any], prefix: str = "run") -> str:
    """
    Generate a unique run ID from configuration.
    
    Args:
        config: Configuration dictionary
        prefix: Prefix for run ID (default: "run")
        
    Returns:
        Run ID in format: {prefix}_{hash}
    """
    config_hash = config_to_hash(config)
    return f"{prefix}_{config_hash}"
