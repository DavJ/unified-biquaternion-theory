"""
biquaternion_algebra.py — ℂ⊗ℍ ≅ Mat(2,ℂ) isomorphism and basis.

The biquaternion algebra ℂ⊗ℍ is the tensor product of the complex numbers ℂ
with the quaternions ℍ.  It is isomorphic to the 2×2 complex matrix algebra
Mat(2,ℂ) via the standard representation

    1 ↦ I₂,  i ↦ iσ₁,  j ↦ iσ₂,  k ↦ iσ₃,

where σ₁, σ₂, σ₃ are the Pauli matrices.  Over ℝ this gives an 8-dimensional
associative unital algebra — identical to Mat(2,ℂ) viewed as an ℝ-algebra.

Reference: consolidation_project/appendix_E2_SM_geometry.tex §1
           DERIVATION_INDEX.md "B = ℂ⊗ₐℍ ≅ Mat(2,ℂ) — Proven [L0]"

Author: UBT Research Team
License: See repository LICENSE.md
"""

from sympy import Matrix, I, eye, simplify, zeros, symbols, Rational

from THEORY_COMPARISONS.dimensional_economy.common.algebra import pauli_matrices


# ---------------------------------------------------------------------------
# Quaternion basis mapped to 2×2 matrices (standard representation)
# ---------------------------------------------------------------------------

def quaternion_basis():
    """
    Return the four quaternion units {1, i, j, k} as 2×2 complex matrices.

    Mapping (standard faithful 2×2 complex representation):
        1 → I₂
        i → i σ₂  = [[0,  1], [-1, 0]]
        j → i σ₁  = [[0,  I], [ I, 0]]
        k → i σ₃  = [[I,  0], [ 0,-I]]

    This satisfies all quaternion identities:
        i² = j² = k² = ijk = -1,  ij = k,  jk = i,  ki = j

    Note: the permutation i↦iσ₂, j↦iσ₁, k↦iσ₃ (rather than sequential σ₁,σ₂,σ₃)
    is required for ij = k to hold.  Concretely:
        (iσ₂)(iσ₁) = -σ₂σ₁ = iσ₃ = k  ✓
    whereas (iσ₁)(iσ₂) = -σ₁σ₂ = -iσ₃ = -k  ✗.

    Returns
    -------
    dict
        {'e': I₂, 'qi': iσ₂, 'qj': iσ₁, 'qk': iσ₃}
    """
    sigma0, sigma1, sigma2, sigma3 = pauli_matrices()
    return {
        'e':  sigma0,        # 1 ↦ I₂
        'qi': I * sigma2,    # i ↦ iσ₂
        'qj': I * sigma1,    # j ↦ iσ₁
        'qk': I * sigma3,    # k ↦ iσ₃
    }


def biquaternion_basis():
    """
    Return the 8 real-basis elements of ℂ⊗ℍ ≅ Mat(2,ℂ).

    The basis is: {I₂, iσ₁, iσ₂, iσ₃, iI₂, -σ₁, -σ₂, -σ₃}

    Equivalently, any M ∈ Mat(2,ℂ) can be written as
        M = a₀·I₂ + a₁·(iσ₁) + a₂·(iσ₂) + a₃·(iσ₃)
            + b₀·(iI₂) + b₁·(-σ₁) + b₂·(-σ₂) + b₃·(-σ₃),
    for real a_k, b_k.

    Returns
    -------
    list of sympy.Matrix
        Eight 2×2 complex matrices spanning ℂ⊗ℍ as an ℝ-vector space.
    """
    sigma0, sigma1, sigma2, sigma3 = pauli_matrices()
    return [
        sigma0,           # 1⊗1
        I * sigma1,       # 1⊗i  (= qi basis element)
        I * sigma2,       # 1⊗j
        I * sigma3,       # 1⊗k
        I * sigma0,       # i⊗1
        -sigma1,          # i⊗i  (= i·(iσ₁) = -σ₁)
        -sigma2,          # i⊗j
        -sigma3,          # i⊗k
    ]


# ---------------------------------------------------------------------------
# Isomorphism verification helpers
# ---------------------------------------------------------------------------

def verify_quaternion_relations():
    """
    Verify that the 2×2 matrix representatives satisfy quaternion identities.

    Checks:
        i² = -1,  j² = -1,  k² = -1,  ij = k,  jk = i,  ki = j,  ijk = -1

    Returns
    -------
    bool
        True if all identities hold, False otherwise.

    Raises
    ------
    AssertionError
        With a descriptive message if any identity fails.
    """
    basis = quaternion_basis()
    e  = basis['e']
    qi = basis['qi']
    qj = basis['qj']
    qk = basis['qk']

    neg_e = -e

    checks = [
        ("i² = -1",  simplify(qi * qi - neg_e)),
        ("j² = -1",  simplify(qj * qj - neg_e)),
        ("k² = -1",  simplify(qk * qk - neg_e)),
        ("ij = k",   simplify(qi * qj - qk)),
        ("jk = i",   simplify(qj * qk - qi)),
        ("ki = j",   simplify(qk * qi - qj)),
        ("ijk = -1", simplify(qi * qj * qk - neg_e)),
    ]

    for label, diff in checks:
        if diff != zeros(2, 2):
            raise AssertionError(
                f"Quaternion identity {label} FAILED: residual = {diff}"
            )

    return True


def basis_is_linearly_independent():
    """
    Check that the 8 biquaternion basis elements are ℝ-linearly independent.

    Constructs an 8×4 real coefficient matrix (real and imaginary parts of
    each basis element's upper-left entry, etc.) and checks its rank.

    Returns
    -------
    bool
        True if rank = 8 (fully independent), False otherwise.
    """
    basis = biquaternion_basis()
    # Flatten each 2×2 matrix into 8 real numbers (real+imag parts of 4 entries)
    rows = []
    for M in basis:
        row = []
        for val in M:
            row.append(sp_re(val))
            row.append(sp_im(val))
        rows.append(row)
    mat = Matrix(rows)
    return mat.rank() == 8


def sp_re(expr):
    """Symbolic real part of a number (works for I, -I, etc.)."""
    from sympy import re
    return re(expr)


def sp_im(expr):
    """Symbolic imaginary part of a number (works for I, -I, etc.)."""
    from sympy import im
    return im(expr)


def dimension_count():
    """
    Return the dimensional inventory for UBT vs competing theories.

    Returns a list of dicts describing each theory's dimensional cost,
    matching the table in the problem statement.

    Returns
    -------
    list of dict
        Each dict has keys:
        'theory', 'extra_spatial_dims', 'internal_algebra_dims',
        'total_extra', 'associative'.
    """
    return [
        {
            'theory':               'String Theory (M-theory)',
            'extra_spatial_dims':   '6–7',
            'internal_algebra_dims': '—',
            'total_extra':          '6–7',
            'associative':          True,
        },
        {
            'theory':               'Kaluza-Klein',
            'extra_spatial_dims':   1,
            'internal_algebra_dims': '—',
            'total_extra':          1,
            'associative':          True,
        },
        {
            'theory':               'Loop Quantum Gravity',
            'extra_spatial_dims':   0,
            'internal_algebra_dims': '—',
            'total_extra':          0,
            'associative':          True,
        },
        {
            'theory':               'Furey (ℂ⊗𝕆)',
            'extra_spatial_dims':   0,
            'internal_algebra_dims': 8,
            'total_extra':          8,
            'associative':          False,   # octonions are non-associative
        },
        {
            'theory':               'Connes (NCG)',
            'extra_spatial_dims':   0,
            'internal_algebra_dims': '~4',
            'total_extra':          '~4',
            'associative':          True,
        },
        {
            'theory':               'UBT (ℂ⊗ℍ + complex time)',
            'extra_spatial_dims':   0,
            'internal_algebra_dims': 8,
            'total_extra':          '8 algebraic + 1 complex time',
            'associative':          True,    # Mat(2,ℂ) is associative
        },
    ]
