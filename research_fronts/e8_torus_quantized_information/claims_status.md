<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->
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


# Claims Status Registry — E8 Torus Research Front

**Author**: Ing. David Jaroš  
**Date**: 2026-04-29  
**Status**: Research front claim tracker  
**Parent document**: `e8_torus_chronofactor_paper.md`

---

## Status Labels

| Label | Meaning |
|-------|---------|
| ✅ DERIVED | Proved mathematically; no free parameters; follows from axioms or cited external theorem |
| 🔶 CONJECTURAL | Plausible and well-motivated; has a precise formulation; proof not yet given |
| ❓ OPEN | Precisely formulated question; direction unclear; requires investigation before any assessment |
| ❌ NOT CLAIMED | Explicitly excluded from the scope of this research front |

---

## Section 3: Three-Qubit Hilbert Space

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C3.1 | H₃q = (ℂ²)^⊗3 with computational basis {\|000⟩,...,\|111⟩} | ✅ DERIVED | Standard QM |
| C3.2 | dim_ℂ(H₃q) = 8 | ✅ DERIVED | 2³ = 8, algebraic |
| C3.3 | dim_ℝ(H₃q) = 16 | ✅ DERIVED | Real and imaginary parts |
| C3.4 | Projective state space is ℂP⁷ = S¹⁵/U(1) | ✅ DERIVED | Standard Hilbert-space geometry |
| C3.5 | ℝ⁸ ≅ ℂ⊗ℍ as real vector spaces | ✅ DERIVED | Dimension count only; not a canonical identification |
| C3.6 | There is a canonical identification of H₃q and ℂ⊗ℍ as structured algebras | 🔶 CONJECTURAL | Double occurrence of dim=8 is observed; identification not derived |

---

## Section 4: Torus Construction

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C4.1 | T⁸_Λ = ℝ⁸/Λ is a well-defined flat compact torus for any full-rank lattice Λ ⊂ ℝ⁸ | ✅ DERIVED | Standard differential geometry |
| C4.2 | The real 8D amplitude subspace V = span_ℝ{basis states} ≅ ℝ⁸ is well-defined | ✅ DERIVED | Trivially: real linear span of a finite orthonormal set |
| C4.3 | V is the physically relevant UBT information subspace (not the full ℂ⁸ or ℝ¹⁶) | 🔶 CONJECTURAL | Motivates E8; not derived from UBT equations |
| C4.4 | Periodic identification on V to form a torus is physically justified in UBT | 🔶 CONJECTURAL | By analogy with S¹_ψ compactification; not derived |

---

## Section 5: E8 Lattice

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C5.1 | E8 is the unique (up to scaling/rotation) even self-dual lattice in ℝ⁸ | ✅ DERIVED | Classical lattice theory result |
| C5.2 | E8 achieves the optimal sphere packing density π⁴/384 in ℝ⁸ | ✅ DERIVED | Viazovska 2016; external theorem |
| C5.3 | Kissing number of E8 is 240 | ✅ DERIVED | Combinatorial fact |
| C5.4 | T⁸_{E8} = ℝ⁸/E8 is a well-defined flat torus with unit volume | ✅ DERIVED | det(E8 Gram matrix) = 1; follows from C4.1 and self-duality |
| C5.5 | E8 is the correct UBT information lattice | 🔶 CONJECTURAL | Motivated by optimality; not derived from UBT dynamics |
| C5.6 | The 240 kissing vectors of E8 correspond to physically distinct UBT states | 🔶 CONJECTURAL | Plausible given automorphism symmetry; not derived |
| C5.7 | The 2160 deep holes of E8 correspond to syndrome or latent states | 🔶 CONJECTURAL | Error-correction interpretation; not derived |

---

## Section 6: Space Distinctions

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C6.1 | ℂP⁷ is not a flat torus and cannot be identified with T⁸_{E8} | ✅ DERIVED | ℂP⁷ has non-trivial curvature; T⁸_{E8} is flat |
| C6.2 | The E8 construction requires the real slice V ≅ ℝ⁸, not ℂ⁸ or ℝ¹⁶ | ✅ DERIVED | E8 is defined on ℝ⁸; not a complex lattice |
| C6.3 | A canonical projection from ℂ⁸ to V ≅ ℝ⁸ exists in UBT | 🔶 CONJECTURAL | The "real slice" definition depends on UBT field structure; see Q7 |

---

## Section 7: Information-Density Interpretation

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C7.1 | The packing density Δ_{E8} ≈ 0.2537 is the maximum achievable in ℝ⁸ | ✅ DERIVED | Viazovska 2016 |
| C7.2 | Maximum packing density corresponds to maximum information density | 🔶 CONJECTURAL | Requires connecting geometric density to information-theoretic capacity |
| C7.3 | Lattice points of E8 represent distinct basis states | 🔶 CONJECTURAL | Natural interpretation; not derived |
| C7.4 | Sphere interiors represent quantum fluctuation neighborhoods | 🔶 CONJECTURAL | By analogy with quantum error correction |
| C7.5 | Gap regions correspond to transitions, syndromes, latent, or hidden states | 🔶 CONJECTURAL | Speculative classification; requires derivation |

---

## Section 9: Chronofactor Projection

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C9.1 | A projection Π: T⁸_{E8} → C_chrono can be defined as a linear map on tori | ✅ DERIVED | Any linear map ℝ⁸ → ℝ^k descends to a torus map if it maps lattice to lattice |
| C9.2 | The chronofactor target space is C_chrono = S¹_t × S¹_ψ | 🔶 CONJECTURAL | Motivated by UBT complex time structure; not uniquely determined |
| C9.3 | The chronofactor target space is C_chrono = S² (Bloch sphere) | 🔶 CONJECTURAL | Competing option to C9.2; mutually exclusive |
| C9.4 | There exist lattice-compatible vectors (a, b) ∈ E8 defining Π | ❓ OPEN | Requires checking E8 primitive sublattice structure |
| C9.5 | The chronofactor projection selects observed quantum dynamics | 🔶 CONJECTURAL | Central hypothesis of the research front; not derived |
| C9.6 | Fiber directions of Π correspond to hidden/latent sectors | 🔶 CONJECTURAL | Follows from C9.5 if correct; not derived |
| C9.7 | Entanglement classes label the fibers of Π | ❓ OPEN | Natural but not investigated |

---

## Section 10: Theta Functions

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C10.1 | Θ_{E8}(τ) = E₄(τ) = 1 + 240q + ... | ✅ DERIVED | Classical modular forms result |
| C10.2 | E₄(τ) is a weight-4 modular form under SL₂(ℤ) | ✅ DERIVED | Standard |
| C10.3 | The Laplace spectrum of T⁸_{E8} is given by E8 norms {|λ|² : λ ∈ E8} | ✅ DERIVED | Standard flat torus spectral theory |
| C10.4 | Θ_{E8}(τ) serves as the UBT information-sector partition function | 🔶 CONJECTURAL | Conditional on C5.5; not derived |
| C10.5 | Θ_{E8}(τ) and ϑ₃(τ)³ are related by a modular identity | ❓ OPEN | Mathematical question Q1; not yet investigated |
| C10.6 | Viazovska's magic function conditions are satisfied by UBT's partition function | ❓ OPEN | Mathematical question Q5; not yet investigated |

---

## Section 11: N_eff and Exponent 3/2

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C11.1 | N_eff = 12 from UBT mode counting (five independent routes) | ✅ DERIVED | `ALPHA_STRUCTURAL_ORIGINS.md`; Proved [L0] |
| C11.2 | Exponent 3/2 from heat-kernel on Im ℍ ≅ ℝ³ | ✅ DERIVED | `ALPHA_STRUCTURAL_ORIGINS.md §2.1`; Proved [L0] |
| C11.3 | The factorization 12 = 8 × (3/2) is structurally meaningful | ❓ OPEN | Mathematical question Q3; may be coincidence |
| C11.4 | N_eff = 12 can be rederived from E8 rank and projection | ❓ OPEN | Candidate C4 in §11; not investigated |
| C11.5 | Exponent 3/2 arises from E8 projection geometry | ❓ OPEN | Not yet formulated as a derivation |

---

## Section 12: Quantization

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C12.1 | Three qubits have 8 basis states | ✅ DERIVED | 2³ = 8 |
| C12.2 | 3-qubit basis dimension is NOT the same as 8-bit numerical precision | ✅ DERIVED | Conceptual distinction |
| C12.3 | 8-bit precision means 256 = 2⁸ discrete levels per variable | ✅ DERIVED | Definition |
| C12.4 | E8 winding modes form the lattice ℤ-span within T⁸_{E8} | ✅ DERIVED | Standard torus winding lattice |
| C12.5 | UBT quantization is winding-mode-based on E8 | 🔶 CONJECTURAL | Extension of S¹_ψ winding; not derived for 8D |
| C12.6 | The minimum E8 root (norm √2) is the fundamental quantum of information | 🔶 CONJECTURAL | Natural interpretation; not derived |

---

## Global Overview

| Status | Count |
|--------|-------|
| ✅ DERIVED | 22 |
| 🔶 CONJECTURAL | 20 |
| ❓ OPEN | 9 |
| ❌ NOT CLAIMED | — (see below) |

### Explicitly NOT Claimed

| Non-claim | Reason |
|-----------|--------|
| Alpha is derivable from E8 geometry | E8 torus is an information-geometry structure; alpha connection would require explicit derivation via chronofactor spectrum and is not a goal of this front |
| E8 is the correct UBT information lattice (as a theorem) | Currently CONJECTURAL; would require promotion to DERIVED via Q7 + dynamics derivation |
| The chronofactor projection Π is unique | Multiple options (T², S², ...) listed; uniqueness not determined |
| E8 replaces the existing UBT partition function ϑ₃³ | Different spaces, different modular weights; coexistence is the hypothesis, not replacement |

---

## Dependency Graph

```
DERIVED (canonical inputs)
  ├─ dim_ℂ(H₃q) = 8                        [C3.2]
  ├─ T⁸_Λ torus construction                [C4.1]
  ├─ E8 optimality (Viazovska)              [C5.2]
  ├─ T⁸_{E8} well-defined                  [C5.4]
  ├─ Θ_{E8} = E₄                           [C10.1]
  └─ N_eff = 12, exponent 3/2              [C11.1, C11.2]
              ↓
CONJECTURAL (requires derivation to promote)
  ├─ V ≅ ℝ⁸ is canonical UBT slice         [C4.3, C6.3]  ←── Q7 closes this
  ├─ Λ = E8 is UBT information lattice      [C5.5]        ←── needs C4.3 + dynamics
  ├─ Chronofactor Π exists                  [C9.5]        ←── Q4 tests this
  └─ Θ_{E8} is UBT partition function       [C10.4]       ←── needs C5.5 + Q1
              ↓
OPEN (mathematical questions to resolve)
  ├─ Q1: Θ_{E8} ↔ ϑ₃³ modular relation
  ├─ Q3: 12 = 8 × 3/2 structural meaning
  ├─ Q4: Spectrum of Π: T⁸_{E8} → T²
  └─ Q7: Canonical definition of V ⊂ H₃q
```

---

*License: CC BY-NC-ND 4.0 — © 2026 Ing. David Jaroš*
