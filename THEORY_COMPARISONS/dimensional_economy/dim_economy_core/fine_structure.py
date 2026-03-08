"""
fine_structure.py — Fine structure constant derivation components (proved parts).

The problem statement lists several proved results regarding the fine structure
constant α in UBT.  This module implements the ones that are computationally
verifiable:

Proved [L0] — Complex time compactification:
    The imaginary time direction ψ is compactified on a circle of radius R_ψ.
    Motivation: unitarity + gauge consistency require single-valued fields.

Proved [L0] — Dirac quantisation condition:
    Single-valuedness of charged fields around the ψ-circle requires
        e · g = 2π n     (n ∈ ℤ)
    where e is the electric charge and g is the dual "magnetic" charge.
    For n=1 this fixes the minimal coupling: α = e²/(4π) in natural units.

Proved [L0] — N_eff = 12 from SM gauge group (3 × 2 × 2 counting):
    The effective number of degrees of freedom entering the one-loop
    running is N_eff = N_phases × N_helicities × N_charge = 3 × 2 × 2 = 12.

Proved [L1] — B₀ = 2π·N_eff/3 (one-loop baseline):
    The one-loop vacuum polarization coefficient is B₀ = 2π·N_eff/3.
    For N_eff = 12: B₀ = 2π·12/3 = 8π ≈ 25.13.

MOTIVATED CONJECTURE (NOT proved here):
    B_base = N_eff^{3/2} = 41.57 — Motivated Conjecture [with explicit gap] (v58)
        Exponent 3/2 = dim_R(Im H)/2: factor 3 from Im(H)=span{i,j,k}, factor 2
        from Gaussian path-integral det^{-1/2}. Gaps (a)(b) remain OPEN.
        See: consolidation_project/alpha_derivation/b_base_hausdorff.tex
    α⁻¹ = 137.036 — requires B_base derivation
    R_ψ independent fixation — Dead End

Reference: STATUS_ALPHA.md
           DERIVATION_INDEX.md "Fine Structure Constant"
           consolidation_project/appendix_ALPHA_one_loop_biquat.tex

Author: UBT Research Team
License: See repository LICENSE.md
"""

import math
import sympy as sp
from sympy import pi, Rational, simplify, symbols


# ---------------------------------------------------------------------------
# N_eff = 12 counting
# ---------------------------------------------------------------------------

def compute_neff(n_phases=3, n_helicities=2, n_charge=2):
    """
    Compute N_eff = N_phases × N_helicities × N_charge.

    In UBT the effective number of degrees of freedom entering the one-loop
    running of α is determined by the SM gauge structure:

        N_phases    = 3   (three gauge phases: SU(3), SU(2), U(1))
        N_helicities = 2  (left-handed and right-handed helicity states)
        N_charge    = 2   (particle and antiparticle charge states)

        N_eff = 3 × 2 × 2 = 12

    Parameters
    ----------
    n_phases : int
        Number of gauge-group phases (default 3).
    n_helicities : int
        Number of helicity states (default 2).
    n_charge : int
        Number of charge states (default 2).

    Returns
    -------
    int
        N_eff = n_phases × n_helicities × n_charge.
    """
    return n_phases * n_helicities * n_charge


def verify_neff_equals_twelve():
    """
    Verify that the 3 × 2 × 2 counting gives N_eff = 12.

    Returns
    -------
    bool
        True if N_eff = 12.

    Raises
    ------
    AssertionError
        If N_eff ≠ 12.
    """
    neff = compute_neff()
    if neff != 12:
        raise AssertionError(
            f"N_eff = {neff} ≠ 12: check counting factors"
        )
    return True


# ---------------------------------------------------------------------------
# B₀ = 2π·N_eff/3 one-loop formula
# ---------------------------------------------------------------------------

def compute_B0(neff=12):
    """
    Compute the one-loop vacuum polarization coefficient B₀ = 2π·N_eff/3.

    This is the standard one-loop β-function coefficient for N_eff massless
    charged Dirac fermions in QED, expressed in UBT's parameterisation.

    For N_eff = 12: B₀ = 2π·12/3 = 8π ≈ 25.133.

    Parameters
    ----------
    neff : int
        Effective degrees of freedom (default 12).

    Returns
    -------
    tuple (sympy.Expr, float)
        (exact symbolic value, numerical value)
    """
    B0_exact = 2 * pi * Rational(neff, 3)
    B0_num = float(B0_exact)
    return B0_exact, B0_num


def verify_B0_formula():
    """
    Verify that B₀ = 2π·N_eff/3 = 8π ≈ 25.13 for N_eff = 12.

    Returns
    -------
    bool
        True if B₀ equals 8π (exact) and ≈ 25.13 (numerical).

    Raises
    ------
    AssertionError
        If the formula gives a different value.
    """
    B0_exact, B0_num = compute_B0(neff=12)
    expected_exact = 8 * pi
    diff = simplify(B0_exact - expected_exact)
    if diff != 0:
        raise AssertionError(
            f"B₀ symbolic value wrong: got {B0_exact}, expected 8π, diff={diff}"
        )
    # Numerical check: 8π ≈ 25.132704...
    expected_num = 8 * math.pi
    if abs(B0_num - expected_num) > 1e-10:
        raise AssertionError(
            f"B₀ numerical value wrong: got {B0_num:.6f}, expected {expected_num:.6f}"
        )
    return True


# ---------------------------------------------------------------------------
# Dirac quantisation condition
# ---------------------------------------------------------------------------

def dirac_quantisation(n=1):
    """
    Return the Dirac quantisation condition for a charged field on the ψ-circle.

    Single-valuedness of a field with charge e under the U(1)_ψ holonomy
    requires:
        e · (flux per ψ-period) = 2π n     (n ∈ ℤ)

    For the minimal coupling n = 1, the fundamental charge is:
        e_min = 2π / (ψ-flux per period)

    In UBT parameterisation, the result is that the coupling must satisfy
        4π α = (e_min)²    (Gaussian units)
    giving the definition of the fine-structure constant in terms of the
    ψ-circle geometry.

    This function returns the symbolic quantisation condition as a string
    and the minimum charge as a symbolic expression.

    Parameters
    ----------
    n : int
        Winding number (default 1 for minimal coupling).

    Returns
    -------
    dict
        {
          'condition': 'e · g = 2π n',
          'n': n,
          'status': 'Proved [L0]'
        }
    """
    return {
        'condition': 'e · (2π R_ψ flux) = 2π n',
        'n': n,
        'status': 'Proved [L0] — single-valuedness of Θ on ψ-circle',
        'consequence': 'Fixes minimal coupling e_min; defines α = e_min²/(4π)',
    }


# ---------------------------------------------------------------------------
# ψ-compactification
# ---------------------------------------------------------------------------

def psi_compactification_motivation():
    """
    Return the physical motivation for ψ-circle compactification.

    The imaginary time coordinate ψ (imaginary part of τ = t + iψ) is
    compactified on a circle of circumference 2π R_ψ.

    Motivation (proved [L0]):
    1. Unitarity: the time-evolution operator exp(-iHτ) must be unitary;
       for complex τ = t + iψ this requires ψ to be periodic.
    2. Gauge consistency: the U(1)_Y phase exp(-iθ) must be single-valued
       on the ψ-circle; this enforces compactification.

    Returns
    -------
    dict
        {
          'mechanism': 'ψ-circle compactification',
          'circumference': '2π R_ψ',
          'motivation': ['unitarity', 'gauge consistency'],
          'status': 'Proved [L0]'
        }
    """
    return {
        'mechanism': 'ψ-circle compactification (τ = t + iψ, ψ ~ ψ + 2πR_ψ)',
        'circumference': '2π R_ψ',
        'motivation': [
            'Unitarity: exp(-iHτ) unitary requires ψ periodic',
            'Gauge consistency: exp(-iθ) single-valued on ψ-circle',
        ],
        'status': 'Proved [L0]',
        'open': 'R_ψ independent fixation: Dead End (DERIVATION_INDEX.md §Fine Structure)',
    }


# ---------------------------------------------------------------------------
# Consistency: B₀ predicts n*(B₀)
# ---------------------------------------------------------------------------

def predict_n_star(B0_val=None, alpha_obs=None):
    """
    Given B₀, predict the vacuum stabilisation quantum number n*.

    In UBT, α⁻¹ = n* · B₀ (schematic one-loop relation).  Using the
    one-loop value B₀ = 8π ≈ 25.13 and the observed α⁻¹ ≈ 137.036:

        n* = α⁻¹ / B₀ ≈ 137.036 / 25.13 ≈ 5.45  (not an integer!)

    This confirms that B₀ alone is insufficient — the B_base correction
    is needed.  This is OPEN PROBLEM A (see DERIVATION_INDEX.md).

    For the semi-empirical value B ≈ 46.3:
        n* = 137.036 / 46.3 ≈ 2.96  (≈ 3)

    Parameters
    ----------
    B0_val : float, optional
        One-loop B coefficient.  Defaults to 8π (proved value).
    alpha_obs : float, optional
        Observed α⁻¹.  Defaults to 137.036.

    Returns
    -------
    dict
        {
          'B0': float,
          'alpha_inv_obs': float,
          'n_star': float,
          'is_integer': bool,
          'status': str
        }
    """
    if B0_val is None:
        B0_val = float(compute_B0()[0])  # 8π
    if alpha_obs is None:
        alpha_obs = 137.036

    n_star = alpha_obs / B0_val
    is_integer = abs(n_star - round(n_star)) < 0.05

    return {
        'B0': B0_val,
        'alpha_inv_obs': alpha_obs,
        'n_star': n_star,
        'is_integer': is_integer,
        'status': (
            'B₀ alone insufficient — OPEN PROBLEM A'
            if not is_integer else
            'B₀ consistent with integer n*'
        ),
    }


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

def fine_structure_proved_summary():
    """
    Return a dict summarising the proved vs. open results for α in UBT.

    Returns
    -------
    dict
        Keys are result names; values are their status strings.
    """
    return {
        'Complex time compactification':    'Proved [L0]',
        'Dirac quantisation condition':     'Proved [L0]',
        'N_eff = 12 (3×2×2 counting)':      'Proved [L0]',
        'B₀ = 2π·N_eff/3 (one-loop)':       'Proved [L1]',
        'B_base = N_eff^{3/2} = 41.57':     'Motivated Conjecture [with explicit gap] — exponent 3/2 = dim_R(Im H)/2; gaps (a)(b) OPEN',
        'R_ψ independent fixation':          'Dead End [L0]',
        'α⁻¹ = 137 (bare)':                 'Semi-empirical',
        'α⁻¹ = 137.036 (full)':             'Semi-empirical',
    }
