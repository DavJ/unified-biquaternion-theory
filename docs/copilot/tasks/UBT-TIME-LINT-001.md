# UBT-TIME-LINT-001 — Guardrail: strengthen complex-time linting (no mass edits)

## Goal
Strengthen the repository’s enforcement so that new work does not silently drift toward treating complex time as fundamental.

## Current state
The repo already has a linter:
- `scripts/lint_complex_time_usage.py`

And CI calls it via:
- `.github/workflows/latex_build.yml`

## Instructions
1. Review the current detection patterns and allowed-list behavior in `scripts/lint_complex_time_usage.py`.
2. Improve it **without** mass-editing documents.
3. Desired improvements (pick what is clearly correct and minimal):
   - Expand patterns to catch additional common forms of `τ = t + iψ` usage.
   - Ensure that the presence of *either* `[TRANSITION_CRITERION]` *or* a link to `TRANSITION_CRITERION_COMPLEX_BIQUATERNIONIC.md` *or* Appendix N2 is accepted.
   - Tighten the allowed-list to only truly legacy/intro files.
   - Improve error messages: show file, line number, and a short fix suggestion.
4. Add/update a short doc describing the rule:
   - `docs/linting_rules_complex_time.md`

## Constraints
- ✅ Changes limited to tooling + a short rule doc.
- ❌ Do not touch dozens of `.tex`/`.md` files.
- ❌ Do not change canonical math.

## Definition of done
- Linter still runs in CI.
- Violations produce clear actionable errors.
- The lint rule is documented.
