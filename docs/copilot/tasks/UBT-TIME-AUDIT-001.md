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

# UBT-TIME-AUDIT-001 — Audit: Complex-time usage without transition criterion

## Goal
Produce a **precise audit report** listing all places where complex time (τ or “t + iψ”, or the phrase “complex time”) is used **without** referencing the established transition criterion.

This task is **report-only** (no edits).

## Why this matters
The repository standard is:
- `T_B ∈ 𝔹` is the **primary** time object.
- `τ = t + iψ` is a **projection/limit** valid only under explicit criteria.

Complex-time usage must be justified by pointing to:
- `consolidation_project/appendix_N2_extension_biquaternion_time.tex`, and/or
- `TRANSITION_CRITERION_COMPLEX_BIQUATERNIONIC.md`, and/or
- the `[TRANSITION_CRITERION]` tag.

## Instructions
1. Scan all `.md` and `.tex` files (exclude build/vendor/node_modules/__pycache__/old as the repository tools do).
2. Find occurrences of:
   - `\tau` / `τ`
   - `t + i\psi` / `t+i\psi`
   - the phrase “complex time”
3. For each file with such occurrences, check whether it contains **any** of:
   - `[TRANSITION_CRITERION]`
   - “transition criterion”
   - `TRANSITION_CRITERION_COMPLEX_BIQUATERNIONIC.md`
   - `appendix_N2_extension_biquaternion_time.tex`
4. If not, record it as a violation.

## Output
Create:

- `docs/audits/complex_time_usage_audit.md`

Format each entry as:
- **File:** `path/to/file`
- **Line(s):** if available
- **Snippet:** 1–2 lines max
- **Missing:** which reference/tag is absent
- **Suggested minimal fix:** (one sentence + a link) — do not apply the fix in this task

## Constraints
- ❌ Do not modify any existing file.
- ❌ Do not rewrite math.
- ✅ Report must be deterministic and easy to review.

## Definition of done
- The audit file exists.
- It lists every violation with actionable, minimal suggested patches.
