"""
UBT Planck Validation Package

Pre-registered, court-grade validation of UBT digital-architecture predictions
against Planck 2018 cosmological observations.

Protocol Version: 1.0
Date: 2026-01-10
License: MIT License

Modules
-------
constants : Pre-registered architecture parameters (LOCKED)
mapping : UBT parameter mappings (NO tunable parameters)
metrics : Statistical evaluation metrics
report : Report generation (markdown, CSV, JSON)

Example
-------
>>> from tools.planck_validation import mapping, metrics, report
>>> 
>>> # Get predictions
>>> predictions = mapping.get_all_predictions()
>>> 
>>> # Generate full report
>>> summary = report.generate_report()
>>> 
>>> # Check success criterion
>>> print(summary['success'])
True
"""

__version__ = "1.0"
__protocol_version__ = "1.0"
__protocol_date__ = "2026-01-10"

from . import constants
from . import mapping
from . import metrics
from . import report

__all__ = ['constants', 'mapping', 'metrics', 'report']
