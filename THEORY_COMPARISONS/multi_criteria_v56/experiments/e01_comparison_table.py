#!/usr/bin/env python3
"""
e01_comparison_table.py — Render the UBT v56 multi-criteria comparison table.

Prints a human-readable table of theory scores across all criteria,
followed by the average scores (numeric criteria only) and a brief
qualitative summary for each theory.

Run with:
    python -m THEORY_COMPARISONS.multi_criteria_v56.experiments.e01_comparison_table

Author: UBT Research Team
License: See repository LICENSE.md
"""

from THEORY_COMPARISONS.multi_criteria_v56.scoring_core.criteria import (
    CRITERIA,
    THEORIES,
    SCORES,
    get_total,
)
from THEORY_COMPARISONS.multi_criteria_v56.scoring_core.comparison import (
    summary_table,
)

# Width helpers
_COL = 18
_CRIT_COL = 28


def _bool_symbol(val: bool) -> str:
    return "✅" if val else "❌"


def run() -> None:
    """Print the multi-criteria comparison table and analysis."""
    print("=" * 90)
    print("UBT v56 — MULTI-CRITERIA COMPARISON (2026-03-07)")
    print("Scale: 1–10  (10 = fully derived with zero free parameters)")
    print("=" * 90)
    print()

    # Header row
    theory_labels = [t["label"] for t in THEORIES]
    header = f"{'Criterion':<{_CRIT_COL}}" + "".join(
        f"{lbl:>{_COL}}" for lbl in theory_labels
    )
    print(header)
    print("-" * len(header))

    # Score rows
    for crit in CRITERIA:
        row = f"{crit['label']:<{_CRIT_COL}}"
        for theory in THEORIES:
            val = SCORES[theory["key"]][crit["key"]]
            if isinstance(val, bool):
                cell = _bool_symbol(val)
            else:
                cell = str(val)
            row += f"{cell:>{_COL}}"
        print(row)

    print("-" * len(header))

    # Average row
    avg_row = f"{'Total /10':<{_CRIT_COL}}"
    for theory in THEORIES:
        total = get_total(theory["key"])
        avg_row += f"{total:>{_COL}}"
    print(avg_row)
    print()

    # Footnotes
    for theory in THEORIES:
        if theory["footnote"]:
            print(f"* {theory['label']}: {theory['footnote']}")
    print()

    # Ranking
    print("RANKING (by numeric average):")
    for rank, (key, score) in enumerate(summary_table(), 1):
        label = next(t["label"] for t in THEORIES if t["key"] == key)
        print(f"  {rank}. {label:<22} {score:.1f}/10")
    print()


if __name__ == "__main__":
    run()
