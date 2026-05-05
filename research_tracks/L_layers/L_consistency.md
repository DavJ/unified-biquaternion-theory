> © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
>
> This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
> 4.0 International License (CC BY-NC-ND 4.0).

# L0 / L1 / L2 — UBT Interpretation Consistency Check

**Task**: `ubt_L0_L1_L2_full_audit`  
**Date**: 2026-05-05  
**Mode**: deep_repo_analysis  
**Epistemic mode**: strict

---

## Scope

This document compares the actual repository content (code + documents)
with three candidate UBT interpretations of L0, L1, L2. Each claim is
classified as:

- `[supported]` — directly evidenced by code or documents in the repo
- `[contradicted]` — repo content explicitly contradicts the claim
- `[not present in code]` — claim is a conceptual interpretation with no
  code-level implementation

---

## Candidate Interpretation A: "L0 = raw field"

**Claim**: L0 is the "raw field" — the unprocessed biquaternionic field
Θ(q,τ) before any transformation or symmetry analysis.

| Evidence | Classification |
|----------|----------------|
| `FORMAL_INVARIANT_EXTRACTION_LAYER0.tex` §1.1: "Layer 0: Fundamental algebraic field Θ(q,τ) on complex manifold, minimal action S[Θ], continuous symmetries" | `[supported]` |
| `docs/LAYER0_INVARIANT_EXTRACTION_README.md`: Layer-0 invariants are defined purely from Θ and its derivatives, "no discretization, numerical procedures, or free parameters required" | `[supported]` |
| `docs/architecture/LAYERS.md`: The closest match is "Layer 1" which includes "Biquaternionic field structure ℂ⊗ℍ" — note the layer numbering differs between files | `[supported]` (with numbering caveat) |
| No Python function `L0()` exists that takes a field and returns raw invariants | `[not present in code]` |

**Verdict**: `[supported]` as a documentation concept. The repository
consistently defines L0 as the layer of the fundamental field and its
purely algebraic/topological invariants. Not implemented as a Python
callable.

---

## Candidate Interpretation B: "L1 = evolution / theta / transform"

**Claim**: L1 is the "evolution or transformation layer" — where the
Θ field is evolved, or where UBT transformations are applied to produce
observable physics.

| Evidence | Classification |
|----------|----------------|
| `ALPHA_PROGRESS_REPORT.md` §2.2–2.4: [L1] labels mark one-loop results — V_eff(n), B₀ = 8π — these are perturbative (loop) computations derived from the field dynamics | `[supported]` (System B, loop order) |
| `FORMAL_INVARIANT_EXTRACTION_LAYER0.tex` §1.1: "Layer 1: Emergent metric structure, classical GR/QFT limits" | `[supported]` (System A) |
| `docs/architecture/LAYERS.md` §Layer 1: "continuous symmetries, structural invariants, and dynamical laws" — does not mention "evolution" or "transform" explicitly | `[partially supported]` |
| "Theta transform" is not a defined operation at Layer 1. The name "Theta" refers to the field Θ itself, not a transform | `[contradicted]` — the phrase "theta transform" is not present in repo as an L1 concept |
| No Python function implements an "L1 evolution" step | `[not present in code]` |

**Verdict**: `[partially supported]`. L1 is the one-loop physics layer and
the emergent-structure layer. The characterization as "evolution" is not
standard in the repository. "Theta" in L1 refers to the field, not a
transform. The claim is partly supported but imprecise.

---

## Candidate Interpretation C: "L2 = projection to physical state"

**Claim**: L2 acts as a projection that maps a continuous field configuration
onto the physical (observable) state.

| Evidence | Classification |
|----------|----------------|
| `docs/architecture/LAYERS.md` §Layer 2: defines L2 as "coding/modulation/protocol" — discrete choices and engineering selections | `[supported]` (L2 involves discretization) |
| `docs/INVARIANT_EXTRACTION_SUMMARY.md`: "Layer-2 introduces additional structure beyond Layer-0" — not merely a projection | `[contradicted]` — L2 is NOT described as a projection to physical state; it adds postulates |
| `layer2_demote_heuristics.md`: "Layer-2 is an Estimator, Not a Physics Source" | `[contradicted]` — L2 is explicitly described as an estimator, not a projector |
| `L2_decode_analysis.md` (this audit): L2S acts as a Hamming parity projection onto codewords (Π² = Π) | `[supported]` (in the restricted sense of L2S parity check) |
| `research_tracks/alpha/layer2_coding_alpha_scan.py`: tests_combined_coding_constraint() returns "failed" — coding does not fix physical coupling | `[contradicted]` for the interpretation that L2 produces the physical state |
| `gray_vs_hamming_layer2.md`: "L2S protects state identity" — Hamming code does select admissible states | `[supported]` (weakly: L2S selects, but does not "project from continuous to physical") |

**Verdict**: `[contradicted]` for the strong claim that L2 projects a
continuous field onto the full physical state. **Qualified support**: L2S
enforces a discrete stabilizer (parity-based projection onto codewords).
But the repository explicitly states L2 is an estimator with heuristic
choices, not a fundamental projector that derives the physical state.

---

## Additional Consistency Checks

### Check 1: Are L0/L1/L2 labels consistently used?

**Finding**: The labels are used in two incompatible systems (see
`L_definitions_raw.md`):
- **System A** (architecture): Layer 0/1/2 as abstraction tiers
- **System B** (perturbative loop order): [L0] = tree, [L1] = one-loop, [L2] = higher-loop

These systems coexist in the repository without explicit disambiguation
at the point of use. A reader must infer the meaning from context.

**Classification**: `[not present in code]` as a unified system — the
disambiguation is implicit and requires cross-referencing multiple files.

### Check 2: Does the numeric test confirm dimensional reduction?

**Finding** (from `experiments/L_layer_flow_test.py` output):

```
Field input (proxy): 64-dimensional complex array
L0 invariants: 3 scalars (I_spec_proxy, I_wind_proxy, I_phase_proxy)
L1 output: 2 scalars (n*, V_eff(n*))
L2S output: 1 scalar (P₀)
L2T output: 1 scalar (A_gray)
```

Dimensionality decreases strictly at each stage. `[supported]`

### Check 3: Is Layer-2 a physics source?

**Finding**: `layer2_demote_heuristics.md` explicitly states:

```
Layer-2 does NOT produce I_spec.
Layer-2 ESTIMATES I_spec with controlled + heuristic errors.
```

**Classification**: `[supported]` — Layer-2 is consistently characterized
as an estimator/approximation, not a source of fundamental physics.

### Check 4: Is n=137 derived at any layer?

**Finding**: Multiple documents (`docs/architecture/LAYERS.md`,
`docs/INVARIANT_EXTRACTION_SUMMARY.md`, `layer2_demote_heuristics.md`)
all confirm:

- n=137 is classified as **Layer 2 (empirical calibration)** in System A
- The stability scan shows n=137 is NOT the unique maximum/minimum

**Classification**: n=137 is `[not present in code]` as a derived result.
It is `[supported]` as a calibration parameter (empirical, Layer 2).

---

## Summary Classification Table

| Claim | Classification |
|-------|----------------|
| L0 = fundamental algebraic field Θ(q,τ) and its invariants | `[supported]` |
| L0 = "raw field" (conceptual shorthand) | `[supported]` (with caveat: L0 already includes invariant extraction) |
| L1 = emergent metric, GR/QFT limits | `[supported]` (System A) |
| L1 = one-loop results | `[supported]` (System B) |
| L1 = "evolution layer" (conceptual) | `[partially supported]` (imprecise) |
| L1 = "theta transform" | `[contradicted]` (not defined in repo) |
| L2 = discretization/coding layer (System A) | `[supported]` |
| L2 = higher-loop (System B) | `[supported]` |
| L2 = projection to physical state | `[contradicted]` (L2 = estimator, not fundamental projector) |
| L2 = decode step | `[not present in code]` (P₀ is a test, not a decoder) |
| L2S acts as parity projection onto codewords | `[supported]` (limited scope) |
| n=137 derived at any layer | `[not present in code]` (it is a calibration parameter) |
| Dimensional flow L0→L1→L2 is strictly decreasing | `[supported]` (numerically confirmed) |
| All L-layer transformations are information-preserving | `[contradicted]` (all are lossy) |
| Gray code G(n) is reversible | `[supported]` (bijection on {0,...,N-1}, numerically verified) |

---

*Generated by ubt_L0_L1_L2_full_audit, Step 7.*
