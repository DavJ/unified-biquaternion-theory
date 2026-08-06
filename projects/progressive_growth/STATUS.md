<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Progressive Growth — Status

**Last updated**: 2026-08-05  
**Author**: Ing. David Jaroš

---

## M2H — Exact half-grid theta-sector factorization: IMPLEMENTED

### Completed

- `src/ubt_theta_lab/progressive_growth/half_grid.py`
  — `HalfGridFactorizationMetadata`, `factor_matrix_through_frame`,
    `factor_relu_layer_through_frame`, `HalfGridSectorSchedule`
- `src/ubt_theta_lab/progressive_growth/theta_sector_frame.py`
  — `ThetaSectorFrame`, `analyze_sector_frame`
- `src/ubt_theta_lab/progressive_growth/phi_segment_adapter.py`
  — `build_phi_segment_frame` (canonical phi-kernel segments)
- `tests/progressive_growth/test_half_grid_factorization.py`
  — Full test suite: linear/ReLU/failure/interleaving/phi-segment cases
- `projects/progressive_growth/reports/HALF_GRID_FACTORIZATION.md`
  — Mathematical documentation
- `projects/progressive_growth/scripts/check_half_grid_factorization.py`
  — Diagnostic script

### Key numerical results (from diagnostic script)

| Frame | Rank | Cond | Pinv residual | Lin err | ReLU err | Verdict |
|-------|------|------|---------------|---------|----------|---------|
| Orthogonal baseline | 6 | 1.0 | 8.9e-16 | 1.8e-15 | 1.1e-14 | EXACT_TRANSFER |
| Non-orthogonal synthetic | 4 | 1.64 | 1.1e-15 | 3.1e-15 | 1.1e-14 | EXACT_TRANSFER |
| phi segment: 0.1, 0.2, 0.3 | 3 | 193 | 1.2e-14 | 3.8e-14 | 1.5e-13 | EXACT_TRANSFER |
| phi segment: 0.5, 1.0, 1.5 | 3 | 3.8e8 | 9.4e-9 | 1.6e-8 | 4.4e-8 | EXACT_TRANSFER |
| phi segment: 100, 200, 300 | 1 | — | — | — | — | SECTOR_INSUFFICIENT |

### Open gaps

- `GAP-10T-DYN`: action-level sector selection remains open.
- Multi-layer composition: error accumulation not analyzed.
- Training dynamics: out of scope for M2H.

---

## Baseline: neuron duplication

Status: retained, not expanded.  Serves as parameter-matched reference.

---

## M1 (prior): synthetic widening benchmark

Status: baseline only.  Do not continue expanding.
