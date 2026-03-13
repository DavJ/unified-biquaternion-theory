"""
criteria.py — Scoring criteria and per-theory scores for UBT v56 comparison.

Data source: docs/czech/UBT_V56_SROVNANI_S_TEORIEMI_CZ.md (2026-03-07)

Scale: 1–10, where 10 = fully derived with zero free parameters.
Boolean criteria (no extra dimensions) are stored separately.

Theories compared:
  - string_m      : String / M-theory
  - lqg           : Loop Quantum Gravity
  - connes_ncg    : Connes Non-Commutative Geometry
  - asymptotic_safety : Asymptotic Safety
  - ubt_v56       : Unified Biquaternion Theory (version 56)

Author: UBT Research Team
License: See repository LICENSE.md
"""

from __future__ import annotations

from typing import Dict, List

# ---------------------------------------------------------------------------
# Criterion metadata
# ---------------------------------------------------------------------------

CRITERIA: List[Dict] = [
    {
        "key": "sm_gauge_group",
        "label": "SM gauge group",
        "description": "Derives SU(3)×SU(2)×U(1) from first principles?",
        "numeric": True,
    },
    {
        "key": "gravity",
        "label": "Gravity (GR)",
        "description": "Contains GR without extra postulates?",
        "numeric": True,
    },
    {
        "key": "fermion_masses",
        "label": "Fermion masses",
        "description": "Predicts or reproduces m_e, m_μ, m_τ?",
        "numeric": True,
    },
    {
        "key": "alpha_first_principles",
        "label": "α from first principles",
        "description": "Derives α⁻¹ = 137 from first principles?",
        "numeric": True,
    },
    {
        "key": "no_extra_dimensions",
        "label": "No extra dimensions",
        "description": "Works without extra spatial dimensions? (positive point)",
        "numeric": False,
    },
    {
        "key": "testable_predictions",
        "label": "Testable predictions",
        "description": "Has new, specific, falsifiable predictions?",
        "numeric": True,
    },
    {
        "key": "dynamics_qft",
        "label": "Dynamics (QFT)",
        "description": "QFT equations of motion, S-matrix, cross sections?",
        "numeric": True,
    },
    {
        "key": "mirror_dark_sector",
        "label": "Mirror/dark sector",
        "description": "Natural prediction of dark matter?",
        "numeric": True,
    },
]

NUMERIC_CRITERIA_KEYS: List[str] = [
    c["key"] for c in CRITERIA if c["numeric"]
]

# ---------------------------------------------------------------------------
# Theories
# ---------------------------------------------------------------------------

THEORIES: List[Dict] = [
    {
        "key": "string_m",
        "label": "String/M",
        "footnote": (
            "SM gauge group depends on compactification choice; not unique."
        ),
    },
    {
        "key": "lqg",
        "label": "LQG",
        "footnote": "",
    },
    {
        "key": "connes_ncg",
        "label": "Connes NCG",
        "footnote": "",
    },
    {
        "key": "asymptotic_safety",
        "label": "Asymptotic Safety",
        "footnote": "",
    },
    {
        "key": "ubt_v56",
        "label": "UBT v56",
        "footnote": "",
    },
]

# ---------------------------------------------------------------------------
# Scores
# ---------------------------------------------------------------------------
# Numeric scores: int (1–10)
# Boolean scores: True / False
#
# Source: UBT v56 comparison table, 2026-03-07
# ---------------------------------------------------------------------------

SCORES: Dict[str, Dict[str, object]] = {
    "string_m": {
        "sm_gauge_group": 6,
        "gravity": 9,
        "fermion_masses": 2,
        "alpha_first_principles": 1,
        "no_extra_dimensions": False,
        "testable_predictions": 3,
        "dynamics_qft": 9,
        "mirror_dark_sector": 2,
    },
    "lqg": {
        "sm_gauge_group": 3,
        "gravity": 9,
        "fermion_masses": 1,
        "alpha_first_principles": 1,
        "no_extra_dimensions": True,
        "testable_predictions": 4,
        "dynamics_qft": 7,
        "mirror_dark_sector": 1,
    },
    "connes_ncg": {
        "sm_gauge_group": 9,
        "gravity": 7,
        "fermion_masses": 5,
        "alpha_first_principles": 3,
        "no_extra_dimensions": True,
        "testable_predictions": 4,
        "dynamics_qft": 7,
        "mirror_dark_sector": 1,
    },
    "asymptotic_safety": {
        "sm_gauge_group": 3,
        "gravity": 9,
        "fermion_masses": 1,
        "alpha_first_principles": 1,
        "no_extra_dimensions": True,
        "testable_predictions": 5,
        "dynamics_qft": 8,
        "mirror_dark_sector": 1,
    },
    "ubt_v56": {
        "sm_gauge_group": 9,
        "gravity": 8,
        "fermion_masses": 5,
        "alpha_first_principles": 4,
        "no_extra_dimensions": True,
        "testable_predictions": 8,
        "dynamics_qft": 3,
        "mirror_dark_sector": 9,
    },
}

# ---------------------------------------------------------------------------
# Qualitative analysis
# ---------------------------------------------------------------------------

THEORY_ANALYSIS: Dict[str, Dict[str, str]] = {
    "string_m": {
        "strengths": (
            "Gravity naturally (spin-2 massless graviton), rich dynamics, "
            "dualities, holography."
        ),
        "weaknesses": (
            "10^500 vacua → no concrete prediction for SM parameters. "
            "SM gauge group not derived — chosen by compactification. "
            "α not predicted. No specific prediction for fermion masses. "
            "Testable: supersymmetry sought since 1980, not found. "
            "LHC 13 TeV — nothing."
        ),
    },
    "lqg": {
        "strengths": (
            "Gravity quantised without singularities, discrete spatial geometry."
        ),
        "weaknesses": (
            "Does not include SM at all. No predictions for particle physics. "
            "Dynamics (spin foam) technically extremely complex, few results. "
            "Low score because it is a theory of gravity, not a ToE."
        ),
    },
    "connes_ncg": {
        "strengths": (
            "SM gauge group derived elegantly from spectral triple. "
            "Higgs boson predicted before discovery "
            "(but with wrong mass ~170 GeV)."
        ),
        "weaknesses": (
            "Gravity is added, not emergent. Fermion masses semi-empirical. "
            "Spectral triple is an ad hoc construction. "
            "Weinberg angle and Yukawa couplings not derived."
        ),
    },
    "asymptotic_safety": {
        "strengths": (
            "Gravity UV-complete without extra dimensions. Consistent with SM."
        ),
        "weaknesses": (
            "SM is added, not derived. No predictions for fermion masses or α. "
            "Graviton is not spin-2 from first principles but a postulate."
        ),
    },
    "ubt_v56": {
        "strengths": (
            "SU(3)×SU(2)_L×U(1) derived from ℂ⊗ℍ without free parameters ⭐; "
            "Chirality (SU(2)_L, not SU(2)_L×SU(2)_R) — proved; "
            "GR sector: full chain Θ→g→Γ→R→Einstein proved; "
            "Born rule without postulate; "
            "QM + GR + stat.mech. as three projections of one equation; "
            "Mirror sector (α'⁻¹=139) — new prediction without ad hoc addition; "
            "Hecke signal p=137: P(chance) ≈ 0.002% — strong numerical support; "
            "Confinement algebraically — quarks are inadmissible in H_phys."
        ),
        "weaknesses": (
            "α⁻¹ = 137 still semi-empirical (B and R without derivation); "
            "Fermion masses: m_μ/m_e, m_τ/m_μ not reproduced; "
            "Dynamics: missing S-matrix, cross sections, perturbative QFT; "
            "Weinberg angle and Yukawa couplings semi-empirical."
        ),
    },
}

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Published overall scores ("Celkem /10" from the comparison table)
# ---------------------------------------------------------------------------
# These are holistic quality scores assigned by the author; they are not a
# simple arithmetic mean of the individual criteria scores.
#
# Source: UBT v56 comparison table, 2026-03-07

PUBLISHED_TOTALS: Dict[str, float] = {
    "string_m": 5.8,
    "lqg": 4.8,
    "connes_ncg": 5.8,
    "asymptotic_safety": 5.5,
    "ubt_v56": 7.1,
}

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def get_score(theory_key: str, criterion_key: str) -> object:
    """Return the score for a given theory and criterion.

    Parameters
    ----------
    theory_key:
        Key from THEORIES list (e.g. ``'ubt_v56'``).
    criterion_key:
        Key from CRITERIA list (e.g. ``'sm_gauge_group'``).

    Returns
    -------
    int or bool
    """
    return SCORES[theory_key][criterion_key]


def get_total(theory_key: str) -> float:
    """Return the published overall score for a theory.

    This is the holistic "Celkem /10" score from the comparison table,
    not a simple arithmetic average of individual criteria.

    Parameters
    ----------
    theory_key:
        Key from THEORIES list.

    Returns
    -------
    float
    """
    return PUBLISHED_TOTALS[theory_key]


def all_averages() -> Dict[str, float]:
    """Return a dict mapping each theory key to its published overall score.

    Returns
    -------
    dict[str, float]
    """
    return dict(PUBLISHED_TOTALS)
