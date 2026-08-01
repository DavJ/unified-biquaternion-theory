<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Patch notes: final Palatini one-step cleanup

## Scope

Mechanical deletion only. No equations, claim statuses, APIs, or tests are changed.

## Verified baseline state

- Correct `gap_10t_palatini_torsion_dynamics.tex`: present.
- Correct Palatini PDF: present.
- `compute_goodness_of_fit(..., mask=None)`: present.
- Five-key Planck `get_all_predictions()` output: present; open entries remain `None`.
- History and gauge/QM honest-status patches: present.
- Kobayashi--Nomizu and Olver references: present.

## Fresh-copy validation after deletion

```text
46 passed, 1 skipped in 1.71s
```

The skip is the expected optional missing scan CSV:
`scans/tt_scan_int_100_200.csv`.
