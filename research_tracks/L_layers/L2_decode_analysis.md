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

# L2 — Decode Analysis

**Task**: `ubt_L0_L1_L2_full_audit`  
**Date**: 2026-05-05  
**Mode**: deep_repo_analysis  
**Epistemic mode**: strict

---

## Question

Does Layer 2 (System A) behave as a **decoding / projection step** in the
information-theoretic sense?

---

## Checks

### 1. Does L2 reduce dimensionality?

**L2S (Hamming)**:

```
Input:  {0,1}^8  (256 possible 8-bit blocks)
Output: {0,1}^4  (16 possible syndrome values)  → then scalar P₀ ∈ [0,1]
```

**Yes** — the Hamming parity check H: {0,1}^8 → {0,1}^4 is a surjection
(dimension 8 → 4). The further aggregation to P₀ reduces to a scalar.

**L2T (Gray transport)**:

```
Input:  {0,...,N-1}^m  (sequence of m symbols)
Output: scalar A_gray ∈ [0,1]
```

**Yes** — m symbols → 1 scalar. Massive dimensionality reduction.

**L2 winding scan**:

```
Input:  primes ∩ [101,199]  (a finite set of ~20 integers)
Output: n* ∈ ℤ  (single integer: the argmin)
```

**Yes** — set → single element (projection to minimum).

**Verdict**: L2 reduces dimensionality in all three sub-cases. [code-derived]

---

### 2. Does L2 enforce constraints?

**L2S**:

The Hamming parity check enforces the constraint:

```
H·block^T = 0   (syndrome-zero condition)
```

This partitions {0,1}^8 into:
- 16 syndrome-zero codewords (admissible)
- 240 non-codewords (non-admissible)

**Yes** — L2S enforces a linear parity constraint over GF(2). [code-derived]

**L2T**:

Gray adjacency enforces a path constraint:

```
|G^{-1}(s_i) - G^{-1}(s_{i+1})| ≡ 1  (mod N)
```

This is not an absolute constraint on individual symbols, but a statistical
preference for sequential transitions. **A_gray measures the degree of
constraint satisfaction**, not a hard gate.

**Partial yes** — L2T enforces a soft constraint (statistical preference),
not a hard filter. [code-derived]

**L2 (prime gating)**:

Restricts the domain:

```
n ∈ ℤ  →  n ∈ primes ∩ [101,199]
```

**Yes** — hard domain constraint (heuristic, not topology-derived). [doc-derived]

---

### 3. Does L2 normalize?

**L2S**: The P₀ statistic is a fraction ∈ [0,1]. This is a **normalization**
of the count of syndrome-zero blocks. [code-derived]

**L2T**: A_gray is a fraction ∈ [0,1], normalized by m-1. [code-derived]

**L2 winding scan**: V_eff values are not normalized; only the argmin is
extracted. [doc-derived]

**Verdict**: L2S and L2T produce normalized statistics (fractions).
The winding number scan produces an argmin (not normalized).

---

### 4. Is information lost?

All three L2 sub-operations are **irreversible**:

- L2S: Given P₀, cannot recover the original sequence of blocks.
- L2T: Given A_gray, cannot recover the original symbol sequence.
- L2 winding: Given n* = 137, cannot recover the full V_eff landscape.

**Yes — information is lost** at each L2 operation. [code-derived]

This is consistent with Layer-2 being an **estimation/summarization** step
over Layer-0 invariants, as described in `layer2_demote_heuristics.md`:

> Layer-2 Output = f(Layer-0 Invariants, Heuristic Choices, Numerical Errors)

---

## Comparison to Projection Operator Π

A projection operator satisfies Π² = Π.

**L2S (Π_L2S)**:

```
Π_L2S: {0,1}^8 → {0,1}^8  (if we project block to nearest codeword)
```

If Π_L2S is defined as rounding to the nearest Hamming codeword, then
Π_L2S² = Π_L2S (idempotent). This is a genuine projection.

The parity check H is **not** itself a projection (H: {0,1}^8 → {0,1}^4
is a surjection, not idempotent on the same space). But the induced selector
(retain only syndrome-zero blocks) is a projection onto the code subspace.

**Verdict**: L2S **acts as a projection** onto the Hamming code subspace,
though the repository does not use this language explicitly.

**L2T**: A_gray is not a projection in the standard sense — it is an
aggregation (mean), not idempotent. [code-derived]

---

## Comparison to Normalization

**L2S**: P₀ is a normalized probability estimate. **Yes, it normalizes.**

**L2T**: A_gray is a normalized fraction. **Yes, it normalizes.**

---

## Comparison to Error-Correcting Decode

The repository uses the language of error-correcting codes (Hamming,
Reed-Solomon) in the context of Layer-2. However:

- The documents **do not claim** that L2 implements a decode step that
  recovers a clean message from a noisy codeword.
- The Hamming code is used as a **fingerprint test** (P₀), not as a
  channel decoder.
- No "encode then decode" pipeline is defined in code.

**Verdict**: L2 uses error-correcting code structures but does NOT implement
a classical decode step (recovering a message from noisy codeword).
The P₀ statistic is a hypothesis test, not a decoder.

---

## Final Assessment: Does L2 Act as "Decode"?

| Property | L2S (Hamming) | L2T (Gray) | L2 winding |
|----------|---------------|------------|------------|
| Dimensionality reduction | ✅ Yes (8→4→1) | ✅ Yes (m→1) | ✅ Yes (set→point) |
| Constraint enforcement | ✅ Hard (parity) | ⚠️ Soft (statistical) | ✅ Hard (prime gate) |
| Normalization | ✅ Yes (P₀ ∈ [0,1]) | ✅ Yes (A_gray ∈ [0,1]) | ❌ No |
| Information loss | ✅ Yes | ✅ Yes | ✅ Yes |
| Projection (Π² = Π) | ✅ Yes (onto codewords) | ❌ No | ❌ No |
| Classical decode | ❌ Not implemented | ❌ Not implemented | ❌ Not applicable |

**Conclusion**:

Layer 2 **behaves as a projection/summarization** step, not a classical
decoder. L2S is a projection onto the Hamming code subspace (Π_L2S).
L2T is a mean aggregation. Both reduce dimension and lose information.

The term "decode" does **not appear** in the repository as an L-layer
operation. The closest match is L2S acting as a parity-based filter,
which resembles syndrome decoding in structure (checking parity) but does
not reconstruct a message from an error pattern.

---

*Generated by ubt_L0_L1_L2_full_audit, Step 5.*
