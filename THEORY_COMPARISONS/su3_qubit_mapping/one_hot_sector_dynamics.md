# One-Hot Sector Dynamics: Physical Privilege of the One-Hot 3-State Sector

**Author**: Ing. David Jaroš  
**Date**: 2026-03-12  
**Status**: Analysis — Mixed (partially supported, partially conjectural)

> © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0

---

## Purpose and Scope

This document addresses the question: **Is the one-hot 3-state sector of the
3-qubit color space physically privileged, or is it merely a mathematical
construction that was chosen for convenience?**

A sector is *physically privileged* if one of the following holds:
1. It is preserved by the relevant effective Hamiltonian (dynamical conservation).
2. It corresponds to the lowest-energy excitation (energetic selection).
3. It is protected by a code constraint / stabilizer (topological / gauge protection).
4. It is selected by the axioms of the UBT simulation cell (foundational selection).

We analyze each route and state clearly whether the claimed privilege is:
- **Proved**: A rigorous mathematical argument within an established formalism.
- **Supported**: Physically plausible with partial evidence but not fully proved.
- **Conjectural**: Motivated but lacking formal justification.

---

## 1. The One-Hot Sector and Its Complement

### 1.1 Definitions

The 3-qubit Hilbert space H₃ = ℂ²⊗ℂ²⊗ℂ² has dimension 8. We partition it into:

**One-hot sector** (color subspace):
```
C = span{|100⟩, |010⟩, |001⟩}   (Hamming weight = 1)
```
Projector: Π_C = |100⟩⟨100| + |010⟩⟨010| + |001⟩⟨001|

**Complementary sector** (non-color subspace):
```
C⊥ = span{|000⟩, |011⟩, |101⟩, |110⟩, |111⟩}   (Hamming weight ≠ 1)
```
Projector: Π_⊥ = I₈ - Π_C

### 1.2 The Question

Why should the physical color state of a quark occupy C rather than an arbitrary
linear combination in H₃? If we construct a 3-qubit simulation of color physics,
why is the one-hot sector the *correct* one rather than, say, any other 3-dimensional
subspace?

---

## 2. Route 1: Sector Preserved by Effective Hamiltonian

### 2.1 The Color Hamiltonian and SU(3) Generators

The SU(3) color generators, lifted to the 3-qubit space via the one-hot embedding,
take the form:
```
L_a = P λ_a P†   (8×8 matrices, a = 1, …, 8)
```
where P is the 8×3 embedding matrix.

By construction: **L_a Π_C = Π_C L_a**

Proof: For any |ψ⟩ = P|c⟩ ∈ C (with |c⟩ ∈ ℂ³):
```
L_a |ψ⟩ = P λ_a P† P |c⟩ = P λ_a |c⟩ ∈ C
```
since λ_a maps ℂ³ to ℂ³, hence P λ_a |c⟩ ∈ range(P) = C.

Similarly, L_a |ψ⊥⟩ ∈ C⊥ for all |ψ⊥⟩ ∈ C⊥ (the generators do not mix C and C⊥).

**Result**: The one-hot sector C is an *invariant subspace* of all SU(3) color
generators L_a.

**Status: ✅ PROVED** (within the one-hot embedding framework).

Any Hamiltonian built purely from the color generators L_a will preserve C:
```
H = Σ_a c_a L_a + Σ_{a,b} c_{ab} L_a L_b + …
⟹  [H, Π_C] = 0   ⟹   e^{-iHt} C ⊆ C
```

**Caveat**: This proves preservation only for Hamiltonians that are *polynomials
in the L_a generators*. A Hamiltonian involving qubit operators outside this set
(e.g., pure qubit interactions between qubits 1 and 2 not respecting color
structure) would not necessarily preserve C.

---

## 3. Route 2: Sector Selected by Lowest-Energy Excitation

### 3.1 Hamming-Weight Penalty (Explicit Construction)

Define the **color constraint Hamiltonian**:
```
H_c = λ_c (n̂₁ + n̂₂ + n̂₃ - 1)²   (λ_c > 0)
```
where n̂_i = (I - Z_i)/2 is the number operator for qubit i.

Eigenvalues:
- Hamming weight 0 (|000⟩): eigenvalue = λ_c (1)² = λ_c
- Hamming weight 1 (C): eigenvalue = 0 ← **ground sector**
- Hamming weight 2 (|011⟩, |101⟩, |110⟩): eigenvalue = λ_c (1)² = λ_c
- Hamming weight 3 (|111⟩): eigenvalue = λ_c (2)² = 4λ_c

The one-hot sector C has the **uniquely lowest energy** (E = 0) under H_c.

**Status: ✅ PROVED** — under the Hamming-weight penalty Hamiltonian H_c, the
one-hot sector is the ground sector. The energy gap is Δ = λ_c.

### 3.2 UBT Effective Hamiltonian

The question of whether the UBT biquaternionic effective Hamiltonian naturally
produces a Hamming-weight-like penalty (without explicit external imposition) is
more subtle.

The UBT effective Hamiltonian for a single color degree of freedom at a spacetime
point would arise from the normal-ordering and mode expansion of the biquaternionic
field equation:
```
∇†∇Θ(q, τ) = κ 𝒯(q, τ)
```

In the internal color fiber, the relevant part of the dynamics involves the
SU(3) covariant kinetic term. After projection to the color sector:

1. **Color singlet states** (weight-0 sector |000⟩ in qubit language): These
   correspond to color-neutral configurations. In QCD, isolated color singlets
   are possible (mesons, baryons), but an isolated quark (a single color charge)
   cannot be color-neutral — **the |000⟩ state is not physical for a single quark**.

2. **One-hot states** (color triplet): These correspond to a single color charge —
   the physical states of a single quark.

3. **Higher-weight states**: In the one-hot encoding, weight-2 states (e.g., |110⟩)
   would represent "two simultaneous color excitations" on a single color degree of
   freedom, which has no direct physical counterpart within the one-quark sector.

**Physical argument**: The one-hot constraint is the qubit incarnation of the
statement "a quark carries exactly one color charge." This is not a dynamical
statement but a *definition* of what we mean by a quark color state.

**Status: 🔶 SUPPORTED but not proved from first UBT principles.** The one-hot
sector is selected by the physical definition of a quark's color charge, but a
derivation that a specific UBT Hamiltonian dynamically confines to weight-1 states
without an explicit penalty term has not been completed.

---

## 4. Route 3: Sector Protected by Code Constraint / Stabilizer

### 4.1 Stabilizer Structure of the One-Hot Code

The one-hot sector C = span{|100⟩, |010⟩, |001⟩} can be described as the
code space of a **stabilizer code**. Define the projector:

```
Π_C = (I + Z₁Z₂)(I + Z₁Z₃)(I - Z₁)(I - Z₂)(I - Z₃) / (normalization)
```

More directly, the one-hot sector is the simultaneous +1 eigenspace of the
**parity checks**:

- **Total parity**: n̂₁ + n̂₂ + n̂₃ = 1 (Hamming weight exactly 1)
- This is equivalent to the syndrome conditions:
  - n̂₁ + n̂₂ ≠ 0 (at most one of q₁, q₂ is 1) — ensured by Z₁Z₂ anticommutation
  - n̂₁ + n̂₃ ≠ 0
  - n̂₂ + n̂₃ ≠ 0

### 4.2 Color Neutrality Constraint as Stabilizer

The UBT color neutrality constraint (see `su3_qubit_core/mapping.py`):
```
D_r + D_g + D_b = Π_C
```
is precisely the **stabilizer condition** that defines the one-hot sector:
a state is in the one-hot sector if and only if it is in the range of Π_C.

This constraint arises from the identification of the u(1) direction in u(3) and
its identification with the projector onto the full color subspace (§ "9→8
Algebraic Constraint" in README.md).

**Status: ✅ PROVED** — The one-hot sector is the unique sector satisfying the
color neutrality constraint D_r + D_g + D_b = Π_C. This is a gauge constraint
(analogous to a stabilizer condition in quantum error correction), and the one-hot
sector is its code space.

**Physical interpretation**: The color neutrality constraint is the qubit-level
analog of the SU(3) Gauss law: physical quark states must transform in the
fundamental representation, and the projector Π_C identifies exactly those states.
This is a *gauge protection* argument — the one-hot sector is protected by the
gauge constraint.

---

## 5. Route 4: Selected by UBT Simulation-Cell Axioms

### 5.1 The UBT Simulation Cell

UBT models the quark color degree of freedom via a minimal simulation cell — the
smallest quantum system that can faithfully represent the SU(3) color algebra.
The simulation cell axioms (in the binary/qubit substrate) are:

**Axiom S1 (Binary substrate)**: The simulation cell consists of n binary channels
(qubits) — ℍ_cell = (ℂ²)^⊗n.

**Axiom S2 (Color algebra)**: The cell admits a faithful representation of the
su(3) Lie algebra via traceless Hermitian operators L_a satisfying
[L_a, L_b] = 2i f_{abc} L_c.

**Axiom S3 (Isometric embedding)**: The color states {|r⟩, |g⟩, |b⟩} embed
isometrically: ∃ P with P†P = I₃ such that |color⟩ = P|c⟩ for |c⟩ ∈ ℂ³.

**Axiom S4 (Minimality)**: n is the smallest integer satisfying S1–S3.

Under these axioms:
- S4 + S3 + S1 directly force the one-hot sector: by `triqubit_minimality_note.md`
  §3.2, the minimal isometric embedding of ℂ³ into (ℂ²)^⊗n requires n = 3, and
  the unique (up to qubit permutation) isometric embedding at n = 3 is the one-hot
  embedding.

**Status: ✅ PROVED** — Given axioms S1–S4, the one-hot sector is the unique
minimal choice (up to qubit permutation).

**Caveat**: Axioms S1–S4 are a choice of framework. If axiom S3 (isometric
embedding) is relaxed or replaced by a different structural requirement, other
sectors may be preferred. The privilege of the one-hot sector is conditional on
these axioms.

---

## 6. Summary: Is the One-Hot Sector Physically Privileged?

### 6.1 Results Table

| Route | Claim | Status | Conditions |
|-------|-------|--------|------------|
| Route 1: Hamiltonian invariance | C preserved by all SU(3) generators L_a | ✅ Proved | One-hot embedding assumed |
| Route 2a: Energy (H_penalty) | C is ground sector of H_c = λ(n̂_total - 1)² | ✅ Proved | H_c must be externally imposed |
| Route 2b: Energy (UBT H_eff) | C is ground sector of UBT effective Hamiltonian | 🔶 Supported | Full derivation open |
| Route 3: Stabilizer / gauge | C is code space of color neutrality Π_C constraint | ✅ Proved | Constraint physically motivated |
| Route 4: Simulation cell axioms | One-hot is unique minimal isometric binary embedding | ✅ Proved | Axioms S1–S4 assumed |

### 6.2 Overall Assessment

The one-hot sector is **physically privileged** in the following senses, each
with the stated status:

1. **Proved**: The one-hot sector is an invariant subspace of all SU(3) generators
   (no mixing with the complementary sector under color dynamics).

2. **Proved**: The one-hot sector is the ground sector of the Hamming-weight
   penalty Hamiltonian, which is the natural enforcement of the "exactly one color
   charge" constraint.

3. **Proved**: The one-hot sector is the code space of the color neutrality
   constraint D_r + D_g + D_b = Π_C — a gauge constraint that can be regarded as
   a physical axiom of the quark color sector.

4. **Proved (conditional)**: Under the UBT simulation cell axioms (binary substrate,
   isometric embedding, minimality), the one-hot sector is the unique minimal
   choice.

5. **Supported but not yet proved from first UBT principles**: A derivation that
   the UBT biquaternionic effective Hamiltonian itself dynamically confines to the
   one-hot sector (without externally imposed penalty) is an open research
   direction.

### 6.3 Honest Statement

The current situation is this: **the one-hot sector is not merely chosen — it is
the unique sector satisfying all reasonable structural requirements for a binary
color simulation cell**. The privilege is established at the level of algebraic
and axiomatic argument.

What remains open is whether the UBT dynamics *directly* generates a Hamiltonian
confining to the one-hot sector without an external imposition — this would
constitute the strongest possible physical privilege claim and is a target for
future work.

---

## 7. Open Questions and Future Directions

1. **UBT effective Hamiltonian**: Derive the explicit qubit-basis effective
   Hamiltonian from the UBT field equation ∇†∇Θ = κ𝒯, and verify whether the
   resulting H_eff naturally has the one-hot sector as its ground sector.

2. **Confinement analogy**: In QCD, color confinement means isolated color charges
   cannot exist asymptotically. In the qubit model, does the UBT dynamics produce
   an effective "confinement" of the simulation cell to C (analogous to QCD
   confinement preventing free quarks)?

3. **Sector transitions**: Are there physical processes in UBT that can cause a
   state to transition from C to C⊥, and if so, what is their physical
   interpretation?

4. **General binary embeddings**: Are there other 3-dimensional subspaces of H₃
   that satisfy equivalent physical requirements while having different structure?
   (Exploring this would strengthen or challenge the uniqueness of the one-hot
   construction.)

---

## 8. References

- Jaroš, D. — `THEORY_COMPARISONS/su3_qubit_mapping/su3_qubit_core/mapping.py`
  (color neutrality constraint implementation)
- Jaroš, D. — `THEORY_COMPARISONS/su3_qubit_mapping/README.md`
  (§ "9→8 Algebraic Constraint")
- Jaroš, D. — `THEORY_COMPARISONS/su3_qubit_mapping/triqubit_minimality_note.md`
  (minimality proof)
- Jaroš, D. — `THEORY_COMPARISONS/su3_qubit_mapping/triqubit_optimality_criteria.md`
  (optimality metrics)
- Jaroš, D. — `consolidation_project/appendix_G_internal_color_symmetry.tex`
  (UBT SU(3) derivation)
- Nielsen, M.A. & Chuang, I.L. (2000). *Quantum Computation and Quantum
  Information.* Cambridge University Press. (stabilizer codes)
- Gottesman, D. (1997). "Stabilizer Codes and Quantum Error Correction."
  arXiv:quant-ph/9705052.
