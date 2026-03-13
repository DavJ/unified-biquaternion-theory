#!/usr/bin/env python3
"""
UBT Planck Validation - Pre-Registered Architecture Constants

This module defines the LOCKED architecture parameters for the UBT digital-architecture
interpretation. These values are pre-registered and MUST NOT be changed based on data
analysis results.

Protocol Version: 1.0
Date: 2026-01-10
License: MIT License

CRITICAL: These are NOT tunable parameters. Any change constitutes a new protocol version.
"""

# =============================================================================
# Reed-Solomon Code Parameters (LOCKED)
# =============================================================================

RS_N = 255
"""
Reed-Solomon code length (total symbols per codeword).
LOCKED VALUE: 255 = 2^8 - 1 (maximum GF(2^8) field element)

This corresponds to the total length of a Reed-Solomon codeword over the
Galois field GF(2^8). In the digital-architecture interpretation, this
represents the fundamental discretization scale of spacetime.

DO NOT MODIFY: This value is pre-registered in Protocol v1.0
"""

RS_K = 200
"""
Reed-Solomon information symbols per codeword.
LOCKED VALUE: 200

In the RS(n,k) notation, k represents the number of information symbols.
The number of parity (check) symbols is (n-k) = 55.

Alternative hypothesis RS_K = 201 may be tested in a SEPARATE protocol file
(e.g., constants_k201.py) but this would constitute a distinct architectural
variant requiring independent pre-registration.

DO NOT MODIFY: This value is pre-registered in Protocol v1.0
"""

# Derived RS parameters (automatically calculated, not independent)
RS_PARITY = RS_N - RS_K  # 55 parity symbols
RS_CODE_RATE = RS_K / RS_N  # ~0.784 code rate

# =============================================================================
# OFDM Parameters (LOCKED)
# =============================================================================

OFDM_CHANNELS = 16
"""
Number of OFDM (Orthogonal Frequency Division Multiplexing) channels.
LOCKED VALUE: 16 = 2^4

In the digital-architecture interpretation, this represents the number of
independent frequency channels for information transmission in the
hypothetical spacetime communication system.

DO NOT MODIFY: This value is pre-registered in Protocol v1.0
"""

# =============================================================================
# Planck 2018 Observed Values (Reference, Not Parameters)
# =============================================================================
# These are the target observables from Planck 2018.
# They are NOT parameters of the theory - they are what we compare against.

PLANCK_2018_OMEGA_B_H2 = 0.02237
PLANCK_2018_OMEGA_B_H2_SIGMA = 0.00015

PLANCK_2018_OMEGA_C_H2 = 0.1200
PLANCK_2018_OMEGA_C_H2_SIGMA = 0.0012

PLANCK_2018_N_S = 0.9649
PLANCK_2018_N_S_SIGMA = 0.0042

PLANCK_2018_THETA_STAR = 1.0411
PLANCK_2018_THETA_STAR_SIGMA = 0.0003

PLANCK_2018_SIGMA_8 = 0.811
PLANCK_2018_SIGMA_8_SIGMA = 0.006

# =============================================================================
# Protocol Metadata
# =============================================================================

PROTOCOL_VERSION = "1.0"
PROTOCOL_DATE = "2026-01-10"

# =============================================================================
# Validation Functions
# =============================================================================

def validate_constants():
    """
    Validate that constants have not been accidentally modified.
    
    This function checks that all LOCKED constants match their pre-registered
    values. It should be called at the start of any analysis pipeline.
    
    Raises
    ------
    ValueError
        If any LOCKED constant has been modified from its pre-registered value.
    """
    errors = []
    
    # Check RS parameters
    if RS_N != 255:
        errors.append(f"RS_N = {RS_N}, expected 255 (LOCKED)")
    if RS_K != 200:
        errors.append(f"RS_K = {RS_K}, expected 200 (LOCKED)")
    if OFDM_CHANNELS != 16:
        errors.append(f"OFDM_CHANNELS = {OFDM_CHANNELS}, expected 16 (LOCKED)")
    
    # Check derived values
    if RS_PARITY != 55:
        errors.append(f"RS_PARITY = {RS_PARITY}, expected 55 (derived from RS_N - RS_K)")
    
    if errors:
        raise ValueError(
            "PROTOCOL VIOLATION: Pre-registered constants have been modified!\n" +
            "\n".join(errors) +
            "\n\nThese values are LOCKED in Protocol v1.0 and cannot be changed."
        )

def get_architecture_summary():
    """
    Return a summary of the pre-registered architecture parameters.
    
    Returns
    -------
    dict
        Dictionary containing all LOCKED parameters and metadata.
    """
    return {
        'protocol_version': PROTOCOL_VERSION,
        'protocol_date': PROTOCOL_DATE,
        'rs_n': RS_N,
        'rs_k': RS_K,
        'rs_parity': RS_PARITY,
        'rs_code_rate': RS_CODE_RATE,
        'ofdm_channels': OFDM_CHANNELS,
        'note': 'All values are LOCKED and pre-registered. DO NOT MODIFY.'
    }

# Auto-validate on import
validate_constants()
