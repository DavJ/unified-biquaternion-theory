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

# Progressive Growth — Goals

**Project**: Progressive growth / Theta Grid architecture  
**Repository layer**: `research_tracks` (active, incomplete)  
**Author**: Ing. David Jaroš

---

## Active milestone: M2H — Exact half-grid theta-sector factorization

Decompose every original matrix operator through an intermediate half-grid
space whose frame is defined by a selected theta segment.

### What M2H establishes

- An exact algebraic factorization `V = B @ A` through a theta-sector
  frame `Phi`, using compact SVD and the pseudoinverse.
- An exact paired-ReLU insertion that preserves output for all real inputs.
- A `HalfGridSectorSchedule` for choosing different frames at successive
  half-integer positions `k + 1/2`.
- Diagnostics for canonical phi-kernel segment frames (rank, condition
  number, pseudoinverse residual, Gram eigenvalues).

### What M2H does NOT establish

- Any claim about training speed or generalization improvement.
- Action-level selection of which theta segment to use (open: GAP-10T-DYN).
- Global continuation or multi-layer composition analysis.

---

## Baseline: neuron duplication (synthetic widening)

Ordinary neuron duplication — repeating each neuron and halving its
weight — is the parameter-matched baseline.  It does **not** introduce a
theta-sector frame at position `k + 1/2`.  It is retained as a reference
for comparisons.  Do not expand this baseline into new benchmarks until
M2H is verified.

---

## Future milestones (not yet started)

- M3: Composition of half-grid factorizations across depth.
- M4: Action-level derivation of sector selection from UBT dynamics.
- M5: Training and evaluation (deferred until M2H–M4 are complete).
