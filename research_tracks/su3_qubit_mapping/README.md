<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# SU(3) Gauge Connection — Three-Qubit Encoding: Research Track Index

**Author**: Ing. David Jaroš  
**Date**: 2026-04-27  
**Status**: Research track — links canonical equivalence proof to existing qubit geometry work  
**Track type**: Bridge between canonical gauge theory and quantum-information encoding

---

## Purpose

This research track collects all material relating the UBT SU(3) gauge connection
`A_μ = A_μ^a λ_a` to the three-qubit encoded connection `A_μ^{3q} = A_μ^a G_a`
built on the one-hot (color) subspace of `ℂ²⊗ℂ²⊗ℂ²`.

The three-qubit SU(3) construction developed earlier is **not discarded**.
It is reinterpreted as a quantum-information representation of the canonical
UBT gauge connection, with a precise equivalence proved at the level of the
Lie algebra representation and the covariant derivative.

---

## Key Result

> **Theorem (SU(3) gauge–qubit equivalence, proved [L0]):**  
> Let `H_color = span{|100⟩, |010⟩, |001⟩} ⊂ ℂ²⊗ℂ²⊗ℂ²` and let
> `P: ℂ³ → ℂ⁸` be the isometric one-hot embedding.  Then the
> standard QCD covariant derivative `D_μ = ∂_μ + ig A_μ^a λ_a` and
> the encoded derivative `D_μ^{3q} = ∂_μ + ig A_μ^a G_a` satisfy
>
> ```
> P† D_μ^{3q} P = D_μ
> ```
>
> on `H_color`, where `G_a = P λ_a P†`.

For the full proof see
`canonical/interactions/su3_qubit_encoding.tex`.

---

## File Index

### Canonical Files (Proved [L0])

| File | Content | Status |
|------|---------|--------|
| `canonical/interactions/su3_qubit_encoding.tex` | Full proof: basis/generator mapping tables, commutator proof, covariant derivative equivalence, leakage sector | **Proved [L0]** |
| `canonical/bridges/su3_gauge_qubit_equivalence.tex` | Navigation bridge: status summary, cross-references, warnings | **Proved [L0]** |

### Related Canonical Files

| File | Content |
|------|---------|
| `canonical/su3_derivation/su3_from_involutions.tex` | Canonical SU(3) from involutions on ℂ⊗ℍ (Theorems G.A–G.D) |
| `canonical/su3_derivation/step1_superposition_approach.tex` | Superposition approach: SU(3) from ℂ-span{I,J,K} |
| `canonical/interactions/qcd.tex` | Canonical QCD Lagrangian in UBT notation |
| `canonical/bridges/gauge_emergence_bridge.tex` | Gauge group emergence status summary |

### Research Track Files

| File | Content | Status |
|------|---------|--------|
| `research_tracks/triqubit_su3_geometry.md` | Geometric analysis: ℂ⁸ → ℂ³ → ℂP² → SU(3); Hopf fibration; Berry phase | ✅ Geometric compatibility established |
| `research_tracks/THEORY_COMPARISONS/su3_qubit_mapping/README.md` | One-hot homomorphism construction; 9→8 constraint | ✅ Proved |
| `research_tracks/THEORY_COMPARISONS/su3_qubit_mapping/su3_qubit_core/mapping.py` | Numerical verification: isometric embedding, lifted generators, 51 algebra tests | ✅ Verified (max error < 10⁻¹²) |
| `research_tracks/THEORY_COMPARISONS/su3_qubit_mapping/triqubit_minimality_note.md` | Minimality proof: 3 qubits as minimal binary one-hot color cell | ✅ Proved |
| `research_tracks/THEORY_COMPARISONS/su3_qubit_mapping/one_hot_sector_dynamics.md` | Sector privilege: invariance, energy, stabilizer, axioms | ✅ Supported |

---

## Proof Structure Summary

The equivalence is established in four steps.

### Step 1 — Color Subspace

Define the one-hot color subspace:

```
H_color = span{|100⟩, |010⟩, |001⟩} ⊂ ℂ²⊗ℂ²⊗ℂ²
```

with basis identification:  `|100⟩ = red`, `|010⟩ = green`, `|001⟩ = blue`.

The one-hot embedding `P: ℂ³ → ℂ⁸` satisfies `P†P = I₃` (isometry).

### Step 2 — Encoded Generators

For each Gell-Mann matrix `λ_a`, define `G_a = P λ_a P†`.  Then:

- `G_a` acts as `λ_a` on `H_color`
- `G_a` vanishes on `H_color⊥`

### Step 3 — Commutation Relations

The encoded generators satisfy:

```
[G_a, G_b] = i f_{abc} G_c   on H_color
```

**Proof**: Follows from `P†P = I₃` and the standard `[λ_a, λ_b] = i f_{abc} λ_c`.  
**Numerical check**: 51 tests in `mapping.py`, max error < 10⁻¹².

### Step 4 — Covariant Derivative

For `ψ = P φ ∈ H_color`:

```
P† (∂_μ + ig A_μ^a G_a) P φ = (∂_μ + ig A_μ^a λ_a) φ
```

**Proof**: Substitute `G_a P = P λ_a` (from `P†P = I₃`) into the encoded derivative.

---

## Open Problems in this Track

| Problem | Status |
|---------|--------|
| Algebraic bridge between `ker(P₂+1) ⊂ ℂ⊗ℍ` and `range(P) ⊂ (ℂ²)³` | 🔶 Open |
| Physical interpretation of leakage sector `H_color⊥` from UBT action `S[Θ]` | 🔶 Open (speculative) |
| Extension of equivalence to full Yang-Mills dynamics (not just kinematics) | 🔶 Open |
| Confinement in the qubit encoding | 🔶 Open (Clay prize problem; separate) |

---

## Warnings

1. **Scope**: The equivalence is representation-level — it does **not** claim
   that `ℂ²⊗ℂ²⊗ℂ²` is physically identical to SU(3) or to a physical color
   Hilbert space.

2. **No QCD derivation**: The encoding does not provide a physical derivation
   of QCD dynamics, confinement, anomaly structure, or fermion representations.

3. **Leakage sector**: The five-dimensional `H_color⊥` has no canonical UBT
   interpretation; do not assert one without derivation from the UBT action.

4. **Separation of concerns**: The canonical gauge formulation lives in
   `V_c ⊂ ℂ⊗ℍ`; the qubit encoding lives in `H_color ⊂ (ℂ²)³`.
   They are compatible but not identical ambient spaces.

---

## Relation to Canonical Theory

The canonical UBT SU(3) derivation uses involutions on `ℂ⊗ℍ`:

```
V_c = ker(P₂ + 1) ≅ ℂ³ ⊂ ℂ⊗ℍ ≅ ℂ⁸
SU(3) = Aut(V_c, ⟨·,·⟩)   (Theorems G.A–G.D)
```

The qubit encoding uses the one-hot sector:

```
H_color = range(P) ≅ ℂ³ ⊂ (ℂ²)³ ≅ ℂ⁸
SU(3) = norm-preserving maps on ℂ³
```

Both extract an isometric copy of `ℂ³` from an eight-dimensional ambient space
and identify `SU(3)` as its unitary symmetry group.  The explicit algebraic
map between the two ambient `ℂ⁸` spaces is an open problem (see above).

---

*This document is a research track index.*  
*Status: Links canonical equivalence proof to supporting geometric and numerical work.*  
*License: CC BY-NC-ND 4.0 — © 2026 Ing. David Jaroš*
