# UBT-TIME-DOC-001 — Canonical cheat-sheet: when to use `T_B` vs `τ`

## Goal
Create a **single canonical** document that explains the *time regime selection rule*:
- when `T_B` (biquaternionic time) must be used,
- when `τ = t + iψ` is valid as a projection/limit,
- and what references establish those criteria.

## Instructions
1. Create a new file:
   - `DOCS/time_selection_criteria.md`
2. Keep it short (≈ 1 page).
3. It must include:
   - A clear statement: **`T_B` is primary; `τ` is a limit/projection**.
   - A bullet list of criteria, each with a pointer to the authoritative source.
   - A “Safe default” rule: if uncertain, remain in `T_B`.
   - A note that complex time usage should include `[TRANSITION_CRITERION]` or an explicit reference.

## Mandatory references to include
Link to these files (do not paraphrase them extensively; point to them):
- `consolidation_project/appendix_N2_extension_biquaternion_time.tex`
- `TRANSITION_CRITERION_COMPLEX_BIQUATERNIONIC.md`
- `REPO_GOVERNANCE.md`
- `scripts/lint_complex_time_usage.py` (as enforcement)

## Constraints
- ✅ Additive only (new file).
- ❌ No edits to existing appendices in this task.
- ❌ No new notation unless mapped to existing symbols.

## Definition of done
- `DOCS/time_selection_criteria.md` exists.
- It is short, explicit, and references the established sources.
