#!/usr/bin/env python3
"""
e03_qualitative_analysis.py — Per-theory strengths/weaknesses, goal-based
recommendations, and UBT's five unique simultaneous advantages.

Reproduces the following sections from
docs/czech/UBT_V56_SROVNANI_S_TEORIEMI_CZ.md (2026-03-07):

  - "Detail: Proč tato skóre"
  - "Která teorie je nejlepší?"
  - "Objektivní závěr"

Run with:
    python -m THEORY_COMPARISONS.multi_criteria_v56.experiments.e03_qualitative_analysis

Author: UBT Research Team
License: See repository LICENSE.md
"""

from THEORY_COMPARISONS.multi_criteria_v56.scoring_core.criteria import (
    THEORIES,
    get_total,
)
from THEORY_COMPARISONS.multi_criteria_v56.scoring_core.comparison import (
    GOAL_RECOMMENDATIONS,
    ubt_unique_advantages,
    theory_analysis,
)

_SEP = "=" * 72


def _print_qualitative_analysis() -> None:
    print(_SEP)
    print("QUALITATIVE ANALYSIS — WHY THESE SCORES")
    print(_SEP)
    for theory in THEORIES:
        key = theory["key"]
        label = theory["label"]
        total = get_total(key)
        analysis = theory_analysis(key)
        print()
        print(f"  {label}  ({total:.1f}/10)")
        print(f"  {'─' * 40}")
        print(f"  STRENGTHS:\n    {analysis['strengths']}")
        print(f"  WEAKNESSES:\n    {analysis['weaknesses']}")
    print()


def _print_goal_recommendations() -> None:
    print(_SEP)
    print("WHICH THEORY IS BEST? — DEPENDS ON YOUR GOAL")
    print(_SEP)
    print()
    for rec in GOAL_RECOMMENDATIONS:
        theory_labels = ", ".join(
            next(
                (t["label"] for t in THEORIES if t["key"] == k),
                k,  # fall back to key if label not found
            )
            for k in rec["recommended"]
        )
        note = f"  ({rec['note']})" if rec["note"] else ""
        print(f"  If you want: {rec['description']}")
        print(f"  → {theory_labels}{note}")
        print()


def _print_ubt_advantages() -> None:
    print(_SEP)
    print("OBJECTIVE CONCLUSION — UBT'S UNIQUE SIMULTANEOUS ACHIEVEMENTS")
    print(_SEP)
    print()
    print(
        "UBT is the only theory that simultaneously satisfies all five:"
    )
    print()
    for i, advantage in enumerate(ubt_unique_advantages(), 1):
        print(f"  {i}. {advantage}")
    print()
    print(
        "Main condition for breakthrough: Derive B from first principles.\n"
        "Once α⁻¹ = 137 becomes a zero-parameter prediction, UBT jumps\n"
        "to 9+/10 and becomes publishable in a top journal (PRL, Nature Physics)."
    )
    print()


def run() -> None:
    """Run all three qualitative analysis sections."""
    _print_qualitative_analysis()
    _print_goal_recommendations()
    _print_ubt_advantages()


if __name__ == "__main__":
    run()
