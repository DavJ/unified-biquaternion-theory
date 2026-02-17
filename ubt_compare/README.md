# UBT Comparison Harness

## Purpose

This directory provides an A/B comparison harness for two first-class formulations of Unified Biquaternion Theory:

| Formulation | Directory | Key Assumption |
|---|---|---|
| **With Chronofactor** | `../ubt_with_chronofactor/` | Chronofactor τ/χ drives external time evolution |
| **Without Chronofactor** | `../ubt_no_chronofactor/` | Phase-only 8D Θ field; no external chronofactor |

> **Status note**: The meaning of the chronofactor is an open research question and an active
> axis of investigation. Neither formulation is deprecated; both are maintained as equals.

## What question do they differ on?

- **ubt_with_chronofactor**: Evolution is governed by an explicit chronofactor that couples
  phase and time. The biquaternionic field Θ(q, τ) has τ = t + iψ as an external complex-time
  coordinate carrying physical meaning.
- **ubt_no_chronofactor**: The 8D Θ field encodes all dynamical content via phase channels
  Σ_Θ alone; the chronofactor does not appear as a separate entity.

## Comparison Protocol

1. Pick a shared observable (e.g. CMB power-spectrum fingerprint, fine-structure constant α).
2. Run the same extraction pipeline on each formulation.
3. Compare predicted invariants listed in `invariants.md`.
4. Record which invariants agree across formulations and which diverge.
5. Document results in `ubt_compare/scripts/` or a dedicated report.

See `mapping_table.md` for the object-level correspondence between the two formulations.

## Files

| File | Description |
|---|---|
| `invariants.md` | Invariants that must/may differ across formulations |
| `mapping_table.md` | Object-level mapping between the two formulations |
| `scripts/` | Comparison scripts scaffold (empty; to be populated) |
