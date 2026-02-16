"""
ubt_bridge.py - Bridge layer between twistor 2×2 matrices and UBT 4×4 framework

Provides minimal embedding of 2×2 Hermitian matrices into UBT's 4×4 
complex matrix representation.

IMPORTANT: This is NOT a claim of equivalence between twistor theory and UBT.
It is merely a structural mapping to explore potential connections.

Author: UBT Research Team
License: See repository LICENSE.md
"""

import sympy as sp
from sympy import Matrix, zeros, simplify, eye, I
import sys
from pathlib import Path

# Add parent directories to path
repo_root = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(repo_root))

from THEORY_COMPARISONS.penrose_twistor.common.linalg import (
    is_hermitian, hermitian_conjugate, trace, determinant
)


def X2_to_ubt_matrix(X2, mode='block_diagonal'):
    """
    Embed 2×2 Hermitian matrix X into a 4×4 complex matrix.
    
    Several embedding conventions are possible. This function supports:
    
    1. 'block_diagonal': [[X,  0],
                          [0,  X†]]
    
    2. 'block_antidiagonal': [[0,   X],
                              [X†,  0]]
    
    3. 'direct_sum': [[X,  0],
                      [0,  X]]
    
    Parameters
    ----------
    X2 : sympy.Matrix (2×2)
        Hermitian matrix from twistor formalism
    mode : str, optional
        Embedding mode. Options: 'block_diagonal', 'block_antidiagonal', 'direct_sum'
        Default: 'block_diagonal'
    
    Returns
    -------
    sympy.Matrix (4×4)
        Embedded matrix in UBT-like 4×4 format
    
    Notes
    -----
    - UBT uses 4×4 complex matrices for biquaternions
    - This embedding is EXPERIMENTAL and does not imply theoretical equivalence
    - The choice of embedding affects how spacetime structure maps to UBT
    - X† denotes Hermitian conjugate (for Hermitian X, X† = X)
    
    Examples
    --------
    >>> from sympy import symbols, Matrix
    >>> from THEORY_COMPARISONS.penrose_twistor.twistor_core.minkowski_spinor import x_to_X
    >>> t, x, y, z = symbols('t x y z', real=True)
    >>> X2 = x_to_X(t, x, y, z)
    >>> X4 = X2_to_ubt_matrix(X2)
    >>> X4.shape
    (4, 4)
    """
    if X2.shape != (2, 2):
        raise ValueError(f"X2 must be 2×2, got {X2.shape}")
    
    # Compute Hermitian conjugate (for Hermitian X2, this equals X2)
    X2_dag = hermitian_conjugate(X2)
    
    # Zero blocks
    Z2 = zeros(2, 2)
    
    if mode == 'block_diagonal':
        # [[X,  0],
        #  [0,  X†]]
        X4 = Matrix.vstack(
            Matrix.hstack(X2, Z2),
            Matrix.hstack(Z2, X2_dag)
        )
    
    elif mode == 'block_antidiagonal':
        # [[0,   X],
        #  [X†,  0]]
        X4 = Matrix.vstack(
            Matrix.hstack(Z2, X2),
            Matrix.hstack(X2_dag, Z2)
        )
    
    elif mode == 'direct_sum':
        # [[X,  0],
        #  [0,  X]]
        X4 = Matrix.vstack(
            Matrix.hstack(X2, Z2),
            Matrix.hstack(Z2, X2)
        )
    
    else:
        raise ValueError(f"Unknown embedding mode: {mode}")
    
    return simplify(X4)


def ubt_matrix_to_X2(X4, mode='block_diagonal'):
    """
    Extract 2×2 Hermitian matrix from 4×4 UBT-like matrix.
    
    Inverse of X2_to_ubt_matrix. Extracts the embedded 2×2 block.
    
    Parameters
    ----------
    X4 : sympy.Matrix (4×4)
        UBT-like 4×4 matrix
    mode : str, optional
        Extraction mode (must match embedding mode)
    
    Returns
    -------
    sympy.Matrix (2×2)
        Extracted Hermitian matrix
    """
    if X4.shape != (4, 4):
        raise ValueError(f"X4 must be 4×4, got {X4.shape}")
    
    if mode == 'block_diagonal':
        # Extract top-left 2×2 block
        X2 = X4[:2, :2]
    
    elif mode == 'block_antidiagonal':
        # Extract top-right 2×2 block
        X2 = X4[:2, 2:]
    
    elif mode == 'direct_sum':
        # Extract top-left 2×2 block
        X2 = X4[:2, :2]
    
    else:
        raise ValueError(f"Unknown extraction mode: {mode}")
    
    return simplify(X2)


def verify_embedding_roundtrip(X2, mode='block_diagonal'):
    """
    Verify that X2 → X4 → X2 recovers the original matrix.
    
    Parameters
    ----------
    X2 : sympy.Matrix (2×2)
        Original Hermitian matrix
    mode : str, optional
        Embedding mode
    
    Returns
    -------
    bool
        True if roundtrip is exact
    """
    X4 = X2_to_ubt_matrix(X2, mode=mode)
    X2_recovered = ubt_matrix_to_X2(X4, mode=mode)
    
    diff = simplify(X2 - X2_recovered)
    
    return diff == zeros(2, 2)


def embedding_properties(X2, mode='block_diagonal'):
    """
    Analyze properties of the embedded 4×4 matrix.
    
    Parameters
    ----------
    X2 : sympy.Matrix (2×2)
        Hermitian matrix to embed
    mode : str, optional
        Embedding mode
    
    Returns
    -------
    dict
        Dictionary with properties:
        - 'is_hermitian': bool
        - 'trace': sympy expression
        - 'determinant': sympy expression
        - 'rank': int
    """
    X4 = X2_to_ubt_matrix(X2, mode=mode)
    
    properties = {
        'is_hermitian': is_hermitian(X4),
        'trace': trace(X4),
        'determinant': determinant(X4),
        'rank': X4.rank(),
    }
    
    return properties


def compare_traces(X2, mode='block_diagonal'):
    """
    Compare trace of X2 with trace of embedded X4.
    
    Parameters
    ----------
    X2 : sympy.Matrix (2×2)
        Original matrix
    mode : str, optional
        Embedding mode
    
    Returns
    -------
    dict
        {'trace_2x2': expr, 'trace_4x4': expr, 'ratio': expr}
    """
    X4 = X2_to_ubt_matrix(X2, mode=mode)
    
    tr2 = trace(X2)
    tr4 = trace(X4)
    
    # Ratio (if tr2 ≠ 0)
    ratio = simplify(tr4 / tr2) if tr2 != 0 else None
    
    return {
        'trace_2x2': tr2,
        'trace_4x4': tr4,
        'ratio': ratio
    }


def compare_determinants(X2, mode='block_diagonal'):
    """
    Compare determinant of X2 with determinant of embedded X4.
    
    Parameters
    ----------
    X2 : sympy.Matrix (2×2)
        Original matrix
    mode : str, optional
        Embedding mode
    
    Returns
    -------
    dict
        {'det_2x2': expr, 'det_4x4': expr, 'relation': str}
    """
    X4 = X2_to_ubt_matrix(X2, mode=mode)
    
    det2 = determinant(X2)
    det4 = determinant(X4)
    
    # Simplify ratio
    if det2 != 0:
        ratio = simplify(det4 / det2)
        relation = f"det(X4) / det(X2) = {ratio}"
    else:
        relation = "det(X2) = 0"
    
    return {
        'det_2x2': det2,
        'det_4x4': det4,
        'relation': relation
    }


def embedding_notes():
    """
    Return documentation about embedding conventions.
    
    Returns
    -------
    str
        Multi-line string explaining embedding choices
    """
    notes = """
UBT BRIDGE EMBEDDING NOTES
===========================

This module provides EXPERIMENTAL embeddings of 2×2 Hermitian matrices
(from twistor theory) into 4×4 complex matrices (UBT framework).

EMBEDDING MODES:

1. block_diagonal (DEFAULT):
   X4 = [[X,  0],
         [0,  X†]]
   
   Properties:
   - Preserves Hermiticity if X is Hermitian
   - Trace(X4) = 2·Trace(X)
   - Det(X4) = Det(X)²
   - Rank(X4) = 2·Rank(X) if X non-zero

2. block_antidiagonal:
   X4 = [[0,   X],
         [X†,  0]]
   
   Properties:
   - Hermitian if X is Hermitian
   - Trace(X4) = 0 (always!)
   - Different spectral structure
   - Off-diagonal form

3. direct_sum:
   X4 = [[X,  0],
         [0,  X]]
   
   Properties:
   - Simple direct sum
   - Hermitian if X is Hermitian
   - Trace(X4) = 2·Trace(X)
   - Det(X4) = Det(X)²

IMPORTANT DISCLAIMERS:

- These are MATHEMATICAL MAPPINGS, not physical equivalences
- UBT uses biquaternions; twistor theory uses spinors - different foundations
- No claim that one theory derives from or reduces to the other
- This is for EXPLORATORY RESEARCH to identify structural parallels

FUTURE DIRECTIONS:

- Investigate how complex time τ = t + iψ relates to twistor geometry
- Explore whether UBT's phase space has twistor-like structure
- Study conformal invariance in both frameworks

For UBT documentation, see repository root.
For twistor theory references, see ../references.md
"""
    return notes


# Export embedding documentation when module is imported
__doc__ += "\n\n" + embedding_notes()
