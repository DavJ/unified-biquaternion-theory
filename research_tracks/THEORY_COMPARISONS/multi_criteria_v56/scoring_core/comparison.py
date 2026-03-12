"""
comparison.py — Aggregate comparison logic and B-derivation scenario analysis.

Provides:
- best_theory_for_criterion: which theory leads on a given criterion
- b_derivation_scenarios: four scenarios for deriving the B coefficient
- summary_table: list of (theory, avg_score) sorted descending
- recommend_for_goal: goal-based theory recommendation ("Která teorie je nejlepší?")
- ubt_unique_advantages: UBT's 5 unique simultaneous achievements (objektivní závěr)

Source document: docs/czech/UBT_V56_SROVNANI_S_TEORIEMI_CZ.md (2026-03-07)

Author: UBT Research Team
License: See repository LICENSE.md
"""

from __future__ import annotations

from typing import Dict, List, Tuple

from .criteria import (
    CRITERIA,
    THEORIES,
    SCORES,
    NUMERIC_CRITERIA_KEYS,
    THEORY_ANALYSIS,
    get_total,
    all_averages,
)

# ---------------------------------------------------------------------------
# Best-theory queries
# ---------------------------------------------------------------------------

def best_theory_for_criterion(criterion_key: str) -> List[str]:
    """Return the theory key(s) with the highest score on a numeric criterion.

    For boolean criteria, returns theories where the value is True.

    Parameters
    ----------
    criterion_key:
        Key from CRITERIA list.

    Returns
    -------
    list[str]
        Theory keys with the best (maximum) score.
    """
    criterion = next(c for c in CRITERIA if c["key"] == criterion_key)
    if criterion["numeric"]:
        scores = {t["key"]: SCORES[t["key"]][criterion_key] for t in THEORIES}
        max_score = max(scores.values())
        return [k for k, v in scores.items() if v == max_score]
    else:
        return [t["key"] for t in THEORIES if SCORES[t["key"]][criterion_key]]


def summary_table() -> List[Tuple[str, float]]:
    """Return theories sorted by average score (descending).

    Returns
    -------
    list of (theory_key, average_score)
    """
    avgs = all_averages()
    return sorted(avgs.items(), key=lambda x: x[1], reverse=True)


def ubt_is_top_candidate() -> bool:
    """Return True if UBT v56 has the highest average score.

    Returns
    -------
    bool
    """
    table = summary_table()
    return table[0][0] == "ubt_v56"


# ---------------------------------------------------------------------------
# B-derivation scenarios
# ---------------------------------------------------------------------------

# Each scenario is a dict with:
#   label    : short name
#   score    : float
#   status   : human-readable description
#   achieved : bool (True = already done)

B_DERIVATION_SCENARIOS: List[Dict] = [
    {
        "label": "B still semi-empirical (today)",
        "score": 7.1,
        "status": "Strong candidate, not yet a breakthrough",
        "achieved": True,
    },
    {
        "label": "B derived from N_eff^{3/2} algebraically",
        "score": 8.5,
        "status": "Publishable in PRL",
        "achieved": False,
    },
    {
        "label": "B + R both derived",
        "score": 9.2,
        "status": "Nature Physics level",
        "achieved": False,
    },
    {
        "label": "B + R + fermion masses",
        "score": 9.8,
        "status": "Nobel territory",
        "achieved": False,
    },
]


def get_current_scenario() -> Dict:
    """Return the currently achieved B-derivation scenario.

    Returns
    -------
    dict
    """
    achieved = [s for s in B_DERIVATION_SCENARIOS if s["achieved"]]
    return achieved[-1]


def get_breakthrough_scenario() -> Dict:
    """Return the next immediate breakthrough scenario (first not yet achieved).

    Returns
    -------
    dict
    """
    not_achieved = [s for s in B_DERIVATION_SCENARIOS if not s["achieved"]]
    return not_achieved[0]


# ---------------------------------------------------------------------------
# Goal-based theory recommendations
# ---------------------------------------------------------------------------
# Source: "Která teorie je nejlepší?" section,
#         docs/czech/UBT_V56_SROVNANI_S_TEORIEMI_CZ.md

# Each entry maps a research goal to the recommended theory key(s) and a note.
GOAL_RECOMMENDATIONS: List[Dict] = [
    {
        "goal": "gravity_plus_sm_no_extra_dims",
        "description": (
            "Gravity + SM from one principle, without extra dimensions"
        ),
        "recommended": ["ubt_v56"],
        "note": (
            "Only theory that does this with proved results"
        ),
    },
    {
        "goal": "most_developed_math",
        "description": (
            "Most developed mathematics and largest community"
        ),
        "recommended": ["string_m"],
        "note": "But without SM prediction",
    },
    {
        "goal": "quantum_gravity_only",
        "description": "Quantum gravity only (not full ToE)",
        "recommended": ["lqg", "asymptotic_safety"],
        "note": "",
    },
    {
        "goal": "sm_most_elegant",
        "description": "Standard Model most elegantly",
        "recommended": ["connes_ncg"],
        "note": "But gravity is not emergent",
    },
]


def recommend_for_goal(goal_key: str) -> Dict:
    """Return the recommendation dict for a given research goal.

    Parameters
    ----------
    goal_key:
        One of: ``'gravity_plus_sm_no_extra_dims'``,
        ``'most_developed_math'``, ``'quantum_gravity_only'``,
        ``'sm_most_elegant'``.

    Returns
    -------
    dict
        With keys: ``goal``, ``description``, ``recommended``, ``note``.

    Raises
    ------
    KeyError
        If goal_key is not recognised.
    """
    matches = [r for r in GOAL_RECOMMENDATIONS if r["goal"] == goal_key]
    if not matches:
        raise KeyError(f"Unknown goal key: {goal_key!r}")
    return matches[0]


def all_goals() -> List[str]:
    """Return all defined goal keys.

    Returns
    -------
    list[str]
    """
    return [r["goal"] for r in GOAL_RECOMMENDATIONS]


# ---------------------------------------------------------------------------
# UBT unique simultaneous advantages
# ---------------------------------------------------------------------------
# Source: "Objektivní závěr" section,
#         docs/czech/UBT_V56_SROVNANI_S_TEORIEMI_CZ.md

UBT_UNIQUE_ADVANTAGES: List[str] = [
    "Derives the exact SM gauge group SU(3)×SU(2)_L×U(1) — not variants",
    "Contains GR as an emergent sector",
    "Has a numerical signal for α⁻¹ = 137 with P(chance) < 0.003%",
    "Naturally predicts a mirror sector without ad hoc additions",
    "Achieves all of the above from a single object: field Θ ∈ ℂ⊗ℍ",
]


def ubt_unique_advantages() -> List[str]:
    """Return the list of UBT's unique simultaneous achievements.

    These are the five properties that UBT satisfies simultaneously
    and that no single competing theory also satisfies simultaneously.

    A new list is returned on each call so callers cannot inadvertently
    mutate the module-level ``UBT_UNIQUE_ADVANTAGES`` list.

    Returns
    -------
    list[str]
        The five advantage statements.
    """
    return list(UBT_UNIQUE_ADVANTAGES)


def theory_analysis(theory_key: str) -> Dict[str, str]:
    """Return the qualitative strengths/weaknesses dict for a theory.

    Parameters
    ----------
    theory_key:
        Key from THEORIES list.

    Returns
    -------
    dict
        With keys ``'strengths'`` and ``'weaknesses'``.

    Raises
    ------
    KeyError
        If theory_key is not recognised.
    """
    valid_keys = {t["key"] for t in THEORIES}
    if theory_key not in valid_keys:
        raise KeyError(f"Unknown theory key: {theory_key!r}")
    return dict(THEORY_ANALYSIS[theory_key])
