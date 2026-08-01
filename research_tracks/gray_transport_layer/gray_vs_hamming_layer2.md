> © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
>
> This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
> 4.0 International License (CC BY-NC-ND 4.0).

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

# Gray vs Hamming in UBT Layer 2: State Storage vs Path Transport

**Author**: Ing. David Jaroš  
**Date**: 2026-04-27  
**Status**: Research Track

---

## 1. Introduction

UBT Layer 2 (Coding and Stability) governs the discrete selection rules that
stabilize admissible field configurations. This document distinguishes two
complementary sub-layers and their associated coding schemes:

| Sub-layer | Symbol | Code | Concern |
|-----------|--------|------|---------|
| State layer | **L2S** | Hamming (8,4,4) | *State identity* — does this configuration survive? |
| Transport layer | **L2T** | Gray adjacency | *Transition cost* — is this path consistent? |

These address orthogonal questions about physical processes. Neither replaces
the other.

---

## 2. Definitions

### 2.1 Hamming Distance

For two binary strings **u**, **v** ∈ {0,1}ⁿ, the **Hamming distance** is:

```
d_H(u, v) = |{i : u_i ≠ v_i}|
```

i.e., the number of bit positions at which **u** and **v** differ.

For the extended Hamming (8,4,4) code, the minimum distance between any two
distinct codewords is d_min = 4. Any single 1-bit error is detectable; any
single 1-bit error is correctable.

**Observable P₀**: Given a sequence of 8-symbol blocks, each block passes the
Hamming parity check if its syndrome vector is zero. P₀ is the fraction of
syndrome-zero blocks:

```
P₀ = (1/K) Σₖ δ(H sₖᵀ, 0)
```

A statistically significant excess of P₀ over a phase-randomized null is a
positive detection of L2S.

### 2.2 Gray Adjacency

A **standard binary Gray code** on N symbols is an ordering of {0,…,N−1} such
that consecutive symbols differ in exactly one bit:

```
d_H(G(n), G(n+1)) = 1   for all n
```

where G(n) is the n-th symbol in the Gray ordering.

Two symbols s, s' ∈ {0,…,N−1} are **Gray-adjacent** if they are consecutive
in the Gray ordering, i.e., |G⁻¹(s) − G⁻¹(s')| = 1 (mod N).

For 4-bit symbols (N=16) the standard Gray code is:
```
G = [0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8]
```

**Observable gray_adjacency_score**: Given a sequence of discretized phase
symbols s₁, s₂, …, sₘ, the gray_adjacency_score is:

```
A_gray = (1/(m-1)) Σᵢ 1[s_{i+1} is Gray-adjacent to sᵢ]
```

A statistically significant excess of A_gray over a null model (shuffled symbols
or phase-randomized map) is a positive detection of L2T.

---

## 3. L2S — Hamming State Layer (Canonical)

**Status**: ⭐ Canonical Layer 2 fingerprint.

The Hamming (8,4,4) code acts as a **stabilizer** for 8-symbol phase blocks.
The parity-check matrix H projects out non-codewords. Physical field
configurations that satisfy the Hamming parity constraint are "protected" in
the sense that they cannot be reached from a valid configuration by a single
1-symbol error.

### 3.1 One-Hot Triqubit Color States

The one-hot triqubit states |r⟩=|100⟩, |g⟩=|010⟩, |b⟩=|001⟩ have **Hamming
weight exactly 1**. This means:

- Any error that flips a 0→1 in a second channel creates a weight-2 state
  (outside the one-hot subspace) — detected by the parity constraint.
- Any error that flips the single 1→0 creates a weight-0 state (the vacuum) —
  also outside the one-hot subspace.

Therefore, the one-hot Hamming-weight-1 occupation constraint provides
**natural single-`X`-flip leakage detection** for color identity. It is not a
general Pauli stabilizer code and does not detect phase-only errors.

**The Hamming (8,4,4) fingerprint test (P₀) measures state survival**, not path
properties.

---

## 4. L2T — Gray Transport Layer (Research Track)

**Status**: Research Track hypothesis. Not yet validated observationally.

### 4.1 Motivation

Sequential phase-symbol transitions in the ψ-time direction cost an action
proportional to the rate of change of the field configuration. In a discrete
symbol model, the transition cost between adjacent symbols is proportional to
their Hamming distance. Gray ordering minimizes this cost by ensuring each step
changes exactly one bit.

This motivates a hypothesis: **sequences of phase symbols emerging from the UBT
ψ-cycle prefer Gray-adjacent transitions**, because these minimize the
transition action contribution in the discrete limit.

### 4.2 Generator Decomposition

SU(3) generators split naturally into two classes under the one-hot embedding:

**Off-diagonal (color-changing) generators** — λ₁, λ₂, λ₄, λ₅, λ₆, λ₇:
- Map one-hot state to a different one-hot state: |r⟩ ↔ |g⟩, |r⟩ ↔ |b⟩, |g⟩ ↔ |b⟩
- Transition Hamming distance = 2 (one 1→0, one 0→1)
- These are **state-changing** transitions; not Gray-adjacent in the phase symbol sense.
- The Hamming L2S stabilizer governs their cost.

**Diagonal (phase) generators** — λ₃, λ₈:
- Preserve the one-hot state identity
- Act as phase rotations within a color channel
- Sequential phase steps are the natural domain of Gray transport
- **Gray adjacency applies to phase transitions**, not to color transitions.

**Claim**: Gray transport (L2T) applies to sequential phase-symbol paths
along diagonal generator directions. It does not apply to color-changing
off-diagonal transitions (those are governed by Hamming L2S).

**What is not claimed**: All SU(3) generators are one SWAP. Only color
permutations (Weyl group) act as SWAP gates; diagonal generators do not.

### 4.3 Observable Distinction

| Statistic | Layer | Code | What it tests |
|-----------|-------|------|---------------|
| P₀ | L2S | Hamming (8,4,4) | Fraction of 8-symbol blocks satisfying parity — state survival |
| A_gray | L2T | Gray adjacency | Fraction of consecutive symbol pairs that are Gray-adjacent — path consistency |

These two statistics are **independent**: a sequence can have high P₀ and low
A_gray, or vice versa. They probe different aspects of the coding structure.

---

## 5. CMB Path-Fingerprint Test

The proposed test uses CMB spherical harmonic coefficients aℓm as the observable
sequence of phase symbols.

### 5.1 Input

A sequence of CMB phase symbols from discretized aℓm phases:
```
sᵢ = floor(N/(2π) * (arg(aℓm,i) + π))  ∈ {0, …, N−1}
```
with N = 16 (4-bit symbols) or N = 256 (8-bit symbols).

### 5.2 Test Procedure

1. Compute gray_adjacency_score A_gray on the observed symbol sequence.
2. Generate K=1000 null sequences by independently shuffling the symbol sequence
   (or by phase-randomizing the aℓm map).
3. Compute A_gray^null for each null sequence.
4. Report p-value: fraction of null sequences with A_gray^null ≥ A_gray^obs.

### 5.3 Metric

```
gray_adjacency_score = (fraction of consecutive pairs (sᵢ, s_{i+1}) that are Gray-adjacent)
```

Gray-adjacent means the two symbols are adjacent in the standard reflected
binary Gray code ordering.

### 5.4 Null Model

- **Shuffle null**: symbols s₁, …, sₘ randomly permuted (destroys sequential
  structure).
- **Phase-randomized null**: aℓm phases replaced by independent uniform random
  phases, then re-symbolized (destroys both spatial and spectral structure).

### 5.5 Interpretation

- p-value < 0.01: positive detection of L2T Gray transport preference.
- p-value ≥ 0.05: no evidence for L2T at this sensitivity.
- Result is independent of L2S Hamming P₀ result.
- Non-detection of L2T does not affect L2S status, and vice versa.

---

## 6. Summary Table

| Property | L2S (Hamming) | L2T (Gray) |
|----------|---------------|------------|
| Status | ⭐ Canonical | Research Track |
| Code | Extended Hamming (8,4,4) | Standard reflected binary Gray |
| Observable | P₀ (syndrome-zero fraction) | A_gray (adjacency score) |
| What it protects | State identity | Transition cost |
| Falsification | P₀ not above null → no L2S fingerprint | A_gray not above null → no L2T fingerprint |
| Does it replace the other? | No | No |
| Applies to SU(3) sector | Whole one-hot sector | Diagonal (phase) sector only |
