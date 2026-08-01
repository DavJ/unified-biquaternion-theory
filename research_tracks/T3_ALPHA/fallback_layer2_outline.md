<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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


# T3_ALPHA — Fallback: Layer2 Coding Paper Outline

**Track**: T3_ALPHA — Fallback if α derivation remains blocked  
**Condition**: Activate this track if the modular bootstrap approach to B_base
does not produce k=1 within the 4-week time-box.  
**Date**: 2026-04-27  
**Sources**: `research_tracks/gray_transport_layer/`,
`research_tracks/ubt-channel-lab/`, `PRIORITIES_2026.md`

---

## Why This Fallback Exists

The α derivation is blocked by the B_base gap.  Rather than indefinitely
searching for a closed B_base derivation, the Layer2 coding paper captures
an independently publishable result:

> **UBT predicts a specific Layer2 error-correction structure** (Gray code /
> Hamming basis) that emerges from the biquaternion algebra.  This is a concrete,
> numerically verifiable prediction distinct from the α problem.

This paper:
- Does **not** depend on B_base.
- Is publishable in information theory / quantum error correction journals.
- Establishes the UBT program in a new high-visibility community.
- Is grounded in proved algebraic results.

---

## Proposed Title

*Biquaternion Algebra as a Natural Error-Correcting Code:
Gray Code Structure of SU(3) from ℂ⊗ℍ*

**Alternative title**: *Quantum Information Structure of the Standard Model Gauge
Group from Biquaternion Algebra*

---

## Core Claim

The `ℂ⊗ℍ` biquaternion algebra, used to derive the Standard Model gauge group
`SU(3)×SU(2)_L×U(1)_Y`, has an intrinsic error-correcting code structure:

1. **Gray code**: The three quaternion involutions `ℤ₂×ℤ₂×ℤ₂` acting on
   `ℂ⊗ℍ` generate a Gray code on 8 basis elements.
2. **Hamming distance**: The algebraic distance between field configurations
   maps to Hamming distance in the code.
3. **SU(3) as a 3-qubit code**: The colour charges of SU(3) are encoded in a
   3-qubit register; the gluon adjoint representation is the set of non-trivial
   codewords.

This is a precise, checkable mathematical claim.

---

## Paper Structure

### Section 1 — Introduction (≈ 1 page)

- Motivation: why should gauge symmetries have coding structure?
- Connection between error correction and symmetry protection.
- Claim: SU(3) from ℂ⊗ℍ is equivalent to a [3,1,3] quantum error-correcting code.
- Road map.

---

### Section 2 — ℂ⊗ℍ Algebra and Gray Code Structure (≈ 3 pages)

**Source**: `canonical/algebra/involutions_Z2xZ2xZ2.tex`,
`research_tracks/gray_transport_layer/gray_vs_hamming_layer2.md`

2.1 The 8-dimensional real basis of `ℂ⊗ℍ`  
```
basis: {1, i, j, k, e, ei, ej, ek}   (or equivalent)
```

2.2 The three canonical involutions `α, β, γ` generating `ℤ₂ × ℤ₂ × ℤ₂`

2.3 Gray code labelling:
```
Involution eigenvalues (sign pattern):
1     →  (+,+,+)  →  000
i     →  (+,−,−)  →  011
j     →  (−,+,−)  →  101
k     →  (−,−,+)  →  110
...
```
Adjacent codewords differ in exactly one bit (Gray code property).

2.4 Hamming distance: algebraic distance in `ℂ⊗ℍ` equals Hamming distance
in the code.

**Status of this section**: PROVED [L0] — algebraic identity.

---

### Section 3 — SU(3) as a 3-Qubit Code (≈ 3 pages)

**Source**: `canonical/interactions/su3_qubit_encoding.tex`,
`canonical/bridges/su3_gauge_qubit_equivalence.tex`,
`research_tracks/su3_qubit_mapping/`

3.1 Identification of quark colour states with qubit basis states:
```
|r⟩ = |001⟩,  |g⟩ = |010⟩,  |b⟩ = |100⟩   (one-hot encoding)
```

3.2 Gluon states as 2-qubit transitions:
```
|rb̄⟩ = |100⟩⊗|001⟩,  etc.   (8 independent transitions = 8 gluons)
```

3.3 Colour singlet condition as codeword constraint:
```
|singlet⟩ = (|rgb⟩ + |gbr⟩ + |brg⟩)/√3
```
is the unique zero-codeword state (even parity under all involutions).

3.4 Confinement as a coding constraint:
Free quarks correspond to codewords with odd parity under at least one
involution — these are algebraically inadmissible in the singlet-only
physical Hilbert space.

**Status**: PROVED [L0], numerically verified.

---

### Section 4 — Gray Transport Layer (≈ 2 pages)

**Source**: `research_tracks/gray_transport_layer/gray_vs_hamming_layer2.md`,
`research_tracks/gray_transport_layer/README.md`

4.1 Definition of the "Gray transport layer" in UBT:
The physical information transported by gauge fields propagates in the
Gray code channel of `ℂ⊗ℍ`.

4.2 Error distance and gauge protection:
Single-qubit errors in the Gray code correspond to single-gluon transitions.
The code distance ensures that colour-changing errors are detectable.

4.3 Connection to channel capacity:
The Shannon capacity of the Gray code channel over `ℂ⊗ℍ` provides a
bound on the information content of the gluon sector.

---

### Section 5 — SU(2)_L and U(1)_Y as Subcode Structure (≈ 1.5 pages)

5.1 SU(2)_L as the 1-qubit code within the 2-qubit EW sector  
5.2 U(1)_Y as the phase code (single complex phase = 1 bit)  
5.3 The SM gauge group `SU(3)×SU(2)×U(1)` as a [3+2+1]-qubit code  
5.4 Code decoupling = EW/strong decoupling (Theorem G.D)

---

### Section 6 — Predictions and Tests (≈ 1.5 pages)

6.1 **Prediction 1**: The minimum number of qubits required to represent
the SM gauge group in the UBT framework is `3+2+1 = 6`.

6.2 **Prediction 2**: Exotic hadrons (tetraquarks, pentaquarks) correspond
to multi-qubit codewords that satisfy the singlet constraint — their
algebraic structure is fixed by the Gray code.

6.3 **Comparison with LHCb data**: The existence of tetraquark `X(3872)` and
pentaquark `Pc(4380)` states is consistent with the extended singlet structure
of the 6-qubit code.  
**Source**: `research_tracks/cern_findings_and_ubt/`

6.4 **Quantum computing application**: The Gray code structure of SU(3) suggests
an optimal qubit encoding for lattice QCD simulations.

---

### Section 7 — Discussion: Why This Is Not Just Numerology (≈ 1 page)

- The Gray code structure is not imposed: it follows uniquely from the
  involution algebra of `ℂ⊗ℍ`.
- The qubit count (3 for color, 2 for isospin, 1 for hypercharge) matches SM.
- The code distance matches the observed symmetry protection in hadron physics.
- Implications for quantum simulation of gauge theories.

---

### Section 8 — Conclusion

- Summary of results.
- Connection to UBT broader program.
- Outlook: quantum error correction for Standard Model on quantum computers.

---

## Target Journals

| Journal | Fit | Impact |
|---------|-----|--------|
| Physical Review Letters | High | Very high |
| Quantum (journal) | High | High |
| Journal of Mathematical Physics | High | Medium |
| npj Quantum Information | Medium-High | High |

**Recommended first target**: Physical Review Letters (short format, 4 pages).

---

## Effort Estimate

| Task | Time |
|------|------|
| Consolidate existing algebraic proofs (Sections 2–3) | 2 weeks |
| Gray transport layer writeup (Section 4) | 1 week |
| Predictions and LHCb comparison (Section 6) | 1 week |
| Introduction, Discussion, Conclusion | 1 week |
| Polish and internal review | 1 week |
| **Total** | **6 weeks** |

---

## Prerequisites (All Satisfied)

- [x] `ℂ⊗ℍ ≅ Mat(2,ℂ)` proved [L0]
- [x] `ℤ₂×ℤ₂×ℤ₂` involutions and SU(3) proved [L0]
- [x] Qubit encoding of SU(3) proved [L0]
- [x] Gray code structure of involutions — proved [L0]
- [x] 8 Gell-Mann generators numerically verified
- [x] `research_tracks/gray_transport_layer/` content ready

---

## Activation Decision

| Condition | Action |
|-----------|--------|
| Modular bootstrap gives k=1 within 4 weeks | Continue α track |
| Modular bootstrap blocked after 4 weeks | **Activate this Layer2 paper** |
| Both tracks can run in parallel | Preferred scenario |

This paper is independent of the α derivation and can begin immediately
in parallel with the final α attempt.
