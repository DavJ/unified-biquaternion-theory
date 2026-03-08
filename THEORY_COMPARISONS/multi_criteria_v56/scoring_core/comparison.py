"""
comparison.py — Aggregate comparison logic and B-derivation scenario analysis.

Provides:
- best_theory_for_criterion: which theory leads on a given criterion
- b_derivation_scenarios: four scenarios for deriving the B coefficient
- summary_table: list of (theory, avg_score) sorted descending

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
