<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# Observable Bridge Discipline

## Scope

Module: `src/ubt/observables/physics_observable_bridge.py`

This scaffold defines interfaces from abstract UBT quantities to measurable observables without treating reference constants as UBT predictions.

## Definitions

- **Prediction**: a value computed from UBT equations without fitting to the target observable.
- **Fitted value**: a value obtained after tuning free parameters to match data; not a first-principles prediction.
- **Postdiction**: a value reproduced only after selecting assumptions informed by known data.
- **Comparison target**: externally sourced reference value (e.g., CODATA) used only for discrepancy reporting.

## Current status

- `predict_anomalous_magnetic_moment(...)` → `OPEN_GAP`
- `predict_fine_structure_constant()` → `OPEN_GAP`
- `predict_mass_ratio(...)` → `OPEN_GAP`
- `compare_to_reference_data(...)` reports reference values and does not upgrade missing predictions.

## Criteria before marking a result as prediction

A result may be promoted to **prediction** only when all are satisfied:

1. explicit derivation path from UBT action/equations,
2. no target-observable fitting in the final value,
3. uncertainty budget and sensitivity analysis,
4. reproducible implementation and tests,
5. clear separation between predicted value and comparison target data.
