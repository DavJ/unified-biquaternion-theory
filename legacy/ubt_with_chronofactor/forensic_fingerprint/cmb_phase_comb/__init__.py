#!/usr/bin/env python3
"""
UBT Forensic Fingerprint - CMB Phase-Comb Test Module
======================================================

Court-grade test for phase coherence / relational structure in CMB spherical harmonics.

This module tests for periodic phase-locking in a_lm coefficients, complementing
the existing TT power spectrum comb test which only examines |a_lm|^2 averaged over m.

Key Difference from TT Spectrum Test:
- TT spectrum test: Analyzes C_ℓ = ⟨|a_ℓm|²⟩_m (power, phases discarded)
- Phase-comb test: Analyzes φ_ℓm = arg(a_ℓm) (phase coherence)

Pre-registered Periods:
- Primary: 255, 256 (Reed-Solomon related)
- Secondary: 137, 139 (fine structure constant vicinity, optional)

License: MIT
Author: UBT Research Team
"""

from .phase_comb import (
    compute_phase_coherence,
    run_phase_comb_test,
    generate_phase_surrogates,
    compute_p_values,
)

from .report import (
    save_results_json,
    generate_verdict_markdown,
)

try:
    from .io_healpix import (
        load_healpix_map,
        compute_alm,
    )
    HEALPY_AVAILABLE = True
except ImportError:
    HEALPY_AVAILABLE = False
    import warnings
    warnings.warn(
        "healpy not available. HEALPix I/O disabled. "
        "Install with: pip install healpy",
        ImportWarning
    )

from .nulls import (
    randomize_phases_preserve_cl,
    validate_cl_preservation,
)

__version__ = "1.0.0"
__all__ = [
    'compute_phase_coherence',
    'run_phase_comb_test',
    'generate_phase_surrogates',
    'compute_p_values',
    'save_results_json',
    'generate_verdict_markdown',
    'randomize_phases_preserve_cl',
    'validate_cl_preservation',
    'HEALPY_AVAILABLE',
]

if HEALPY_AVAILABLE:
    __all__.extend(['load_healpix_map', 'compute_alm'])
