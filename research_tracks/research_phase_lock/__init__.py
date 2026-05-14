#!/usr/bin/env python3
"""
research_phase_lock

Self-contained research harness for Phase-Lock A/B/C/D verification.

This package provides a YAML-driven grid runner for systematically testing
parameter combinations using the existing unified_phase_lock_scan.py tool.

CRITICAL: This package does NOT modify anything under forensic_fingerprint/tools/.
It only wraps and calls the existing tool with different parameter combinations.

Author: UBT Research Team
License: See repository LICENSE.md
"""

__version__ = "0.1.0"
