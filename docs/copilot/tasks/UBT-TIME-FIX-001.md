<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# UBT-TIME-FIX-001 — Minimal compliance fixes for top offenders (max 5 files)

## Goal
After the audit exists, apply **minimal textual patches** to the highest-visibility files that use complex time without justification.

## Depends on
- `copilot/tasks/UBT-TIME-AUDIT-001.md`

## Instructions
1. From `docs/audits/complex_time_usage_audit.md`, choose up to **five** highest-impact files (e.g., `README.md`, top-level overviews, key derivation guides).
2. For each chosen file, apply the smallest possible fix:
   - Add one sentence clarifying:
     - `T_B` is primary; `τ` is a limit/projection.
   - Add a link to:
     - `ARCHIVE/duplicate_or_snapshot_roots/DOCS/time_selection_criteria.md`
   - Add `[TRANSITION_CRITERION]` tag or explicit reference to:
     - `TRANSITION_CRITERION_COMPLEX_BIQUATERNIONIC.md` / Appendix N2
3. Keep edits localized and reviewable.
4. Prefer one small commit per file.

## Constraints
- ❌ Do not change equations.
- ❌ Do not rename symbols.
- ✅ Do not exceed 5 files.

## Definition of done
- The selected files are compliant with the linter expectations.
- Edits are minimal and do not affect core derivations.
