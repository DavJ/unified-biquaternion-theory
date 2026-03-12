# Triqubit Minimality Note: 3 Qubits as Minimal Binary One-Hot Triplet Cell

**Author**: Ing. David Jaroš  
**Date**: 2026-03-12  
**Status**: Mathematical Note — Minimality Argument

> © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0

---

## Executive Summary

This note formalizes the claim that **three binary channels (qubits) are the
minimal binary substrate** for realizing the three *distinguished*, mutually
exclusive one-hot states required to represent an SU(3) color triplet sector via
a one-hot encoding.

**What is proved**: Three qubits are minimal for one-hot binary triplet encoding.

**What is not proved**: This does not prove uniqueness among all possible SU(3)
realizations, nor does it establish that the triqubit cell is the globally optimal
quantum simulation substrate for SU(3).

---

## 1. Binary Encoding Problem Statement

### 1.1 The Task

We seek to represent a **color triplet state** — one of three mutually exclusive,
distinguishable values {r, g, b} (red, green, blue) — using the smallest possible
collection of binary channels (classical bits or qubits).

The **one-hot constraint** requires:

```
Exactly one channel is in state |1⟩; all others are in state |0⟩.
```

This encodes:
```
|r⟩  ↦  (1, 0, 0, …)
|g⟩  ↦  (0, 1, 0, …)
|b⟩  ↦  (0, 0, 1, …)
```

### 1.2 Why One-Hot Encoding?

One-hot encoding is physically motivated because:

1. **Color charge exclusivity**: A single quark carries exactly one color, not a
   superposition (in the color basis); the one-hot pattern directly represents this
   exclusivity.
2. **Symmetry transparency**: The SU(3) Weyl group permutations (r↔g, g↔b, r↔b)
   act as elementary swap gates on one-hot states — a maximal structural simplicity.
3. **Isometric embedding**: The embedding P: ℂ³ → ℂ²⊗ℂ²⊗ℂ² satisfying P†P = I₃
   (see `su3_qubit_core/mapping.py`) preserves all inner products exactly, making
   it a faithful isometric representation.
4. **Algebra faithfulness**: Because P†P = I₃, the Lie algebra homomorphism
   φ(λ_a) = P λ_a P† exactly preserves the commutation relations
   [L_a, L_b] = 2i f_{abc} L_c (verified in `tests/test_mapping.py`).

### 1.3 Formal Problem Statement

**Problem**: Find the minimum integer n such that there exist n binary channels
(qubits) and an injective map φ: {r, g, b} → {0,1}^n that is:
- **Faithful**: φ(r), φ(g), φ(b) are distinct bit-strings.
- **One-hot**: Each image has exactly one 1-bit.
- **Symmetric**: The SU(3) Weyl group {r↔g, g↔b, r↔b} acts as bit permutations.

---

## 2. Why One and Two Qubits Are Insufficient for Three Distinguished One-Hot Channels

### 2.1 One Qubit: n = 1

A single qubit has the computational basis {|0⟩, |1⟩} — only **two** orthogonal
states. One-hot encoding on 1 qubit yields only:
```
|0⟩ → (channel 0 is "hot")
|1⟩ → (channel 1 is "hot")
```
This can encode at most **2** distinguishable one-hot states.

Since we need **3** distinguishable states (r, g, b), one qubit is **insufficient**.

**Impossibility**: |{0,1}^1| = 2 < 3. ∎

### 2.2 Two Qubits: n = 2

A two-qubit system has computational basis {|00⟩, |01⟩, |10⟩, |11⟩} — four
states. One-hot states in 2 bits are those with exactly one 1-bit:
```
|01⟩  (weight 1, channel 0 hot)
|10⟩  (weight 1, channel 1 hot)
```
The state |11⟩ has weight 2 (not one-hot). The state |00⟩ has weight 0
(not one-hot). Therefore, the one-hot subspace of 2-bit strings contains
exactly **2** states.

Since we need **3** one-hot states for the triplet, two qubits are **insufficient**.

**Counting argument**: For n bits, the number of one-hot strings is exactly n
(one for each bit position). To accommodate 3 one-hot states:
```
n ≥ 3
```

**Impossibility for n = 2**: Exactly 2 one-hot strings exist in 2-bit space,
which is fewer than 3. ∎

### 2.3 Alternative 2-Bit Encodings?

One might try to use non-one-hot binary encodings for 2 bits (e.g., Gray code):
```
r ↦ 00,  g ↦ 01,  b ↦ 10   (standard binary)
r ↦ 00,  g ↦ 01,  b ↦ 11   (Gray code variant)
```
These encode 3 states in 2 bits, but they violate the **one-hot requirement**:
- The state 00 has zero 1-bits (not one-hot).
- The state 11 has two 1-bits (not one-hot).

If the one-hot constraint is not mandatory, 2 bits suffice for 3 states (using
⌈log₂ 3⌉ = 2 bits). However:

1. Non-one-hot encodings **lose the isometric embedding property** (P†P ≠ I₃).
2. They **break the permutation-symmetry** of the Weyl group (r↔g is no longer
   a simple qubit swap).
3. They produce **non-uniform Hamming weights**, making the SU(3) generators less
   natural in the Pauli basis.

Under the one-hot constraint, 2 bits are definitively insufficient.

---

## 3. Three Qubits as Minimal Binary One-Hot Triplet Cell

### 3.1 Constructive Proof (Existence)

For n = 3, the one-hot subspace of {0,1}³ contains exactly **3** states:
```
|100⟩,  |010⟩,  |001⟩
```
We define the color identification:
```
|r⟩  →  |100⟩
|g⟩  →  |010⟩
|b⟩  →  |001⟩
```
This assignment:
- Is **injective** (three distinct bit-strings).
- Satisfies **one-hot** (each has exactly one 1-bit).
- Is **Weyl-symmetric**: each color permutation r↔g, g↔b, r↔b acts as the
  corresponding SWAP gate on qubits.

The embedding matrix P (8×3) is explicitly:
```
P[:, 0] = e₄  (|r⟩ → |100⟩, 3-qubit index 4)
P[:, 1] = e₂  (|g⟩ → |010⟩, 3-qubit index 2)
P[:, 2] = e₁  (|b⟩ → |001⟩, 3-qubit index 1)
```
Satisfying P†P = I₃ (isometric). See `su3_qubit_core/mapping.py:embedding_matrix()`.

### 3.2 Minimality Proof

**Theorem**: 3 qubits are the minimum number of qubits for a one-hot encoding of
a 3-element set.

**Proof**:
- For n qubits, the number of one-hot states (Hamming weight = 1 states) is
  exactly n.
- To encode a 3-element set injectively via one-hot, we need at least 3 one-hot
  states, hence n ≥ 3.
- n = 3 achieves exactly 3 one-hot states (|100⟩, |010⟩, |001⟩).
- Therefore, n = 3 is the minimum. ∎

**Corollary**: The 3-qubit (triqubit) cell is the **minimal binary one-hot triplet
cell** for encoding the SU(3) color triplet {r, g, b}.

### 3.3 Quantum Lifting

The one-hot encoding extends naturally to quantum superpositions:
```
α|r⟩ + β|g⟩ + γ|b⟩  →  α|100⟩ + β|010⟩ + γ|001⟩
```
This is an isometric embedding of ℂ³ into ℂ²⊗ℂ²⊗ℂ² (the 3-qubit Hilbert
space). The isometry is essential for:
- Preserving inner products (no information loss).
- Faithfully lifting the SU(3) action: φ(U)|ψ_color⟩ = P U P†|ψ_qubit⟩.
- Maintaining Lie algebra relations: [L_a, L_b] = 2i f_{abc} L_c.

---

## 4. Qutrit vs Triqubit Comparison

### 4.1 Qutrit Approach

A **qutrit** is a single 3-level quantum system with Hilbert space ℂ³. It
directly represents the color triplet without any encoding overhead:
```
|r⟩,  |g⟩,  |b⟩  (basis of ℂ³)
```
SU(3) acts naturally on ℂ³ as the defining/fundamental representation.

**Advantages of qutrit**:
- Zero encoding overhead (no extra dimensions).
- Exact fit: dim(ℂ³) = 3, matching the color triplet.
- Compact: fewer physical degrees of freedom.

**Disadvantages of qutrit**:
- Not a binary (qubit) substrate; requires ternary hardware.
- Harder to implement in binary-native architectures (superconducting qubits,
  trapped ions in qubit mode, etc.).
- Quantum error correcting codes (surface codes, stabilizer codes) are natively
  designed for qubits; qutrit error correction is more complex.

### 4.2 Triqubit Approach (One-Hot)

The triqubit uses 3 binary channels to represent the same 3 states.

**Advantages of triqubit**:
- Native binary substrate; compatible with qubit-based quantum hardware.
- Weyl symmetry (r↔g, g↔b, r↔b) expressed as SWAP gates (standard 2-qubit gates).
- Stabilizer structure: The one-hot constraint (Hamming weight = 1) is a natural
  stabilizer code — the code subspace is protected against weight-0 and weight-≥2
  errors.
- Pauli decomposition of SU(3) generators is explicit and sparse (4 terms each).

**Disadvantages of triqubit**:
- Overhead: 3 qubits for 3 states (vs 1 qutrit). The 8-dimensional Hilbert space
  is used, but only a 3-dimensional subspace is physical.
- Five of the eight basis states (|000⟩, |011⟩, |101⟩, |110⟩, |111⟩) are outside
  the code subspace and must be suppressed or identified as errors.

### 4.3 Dimension Comparison

| Encoding | Physical Hilbert space | Used subspace | Overhead factor |
|----------|----------------------|---------------|----------------|
| Qutrit | ℂ³ | ℂ³ (full) | 1× |
| Triqubit (one-hot) | ℂ⁸ (= ℂ²⊗ℂ²⊗ℂ²) | ℂ³ (one-hot sector) | 8/3 ≈ 2.67× |
| 2-bit binary | ℂ⁴ | ℂ³ (non-one-hot) | 4/3 ≈ 1.33× |

The triqubit uses 8/3 times more Hilbert space than the qutrit, but this overhead
provides the stabilizer structure and binary compatibility.

### 4.4 SU(3) Generator Complexity

| Encoding | Generator representation | Pauli terms per generator |
|----------|--------------------------|--------------------------|
| Qutrit (fundamental rep) | 3×3 Gell-Mann matrices | N/A (not Pauli) |
| Triqubit (one-hot) | 8×8 lifted matrices L_a = P λ_a P† | 4 (uniform) |
| Triqubit (general 8D) | Full 8×8 adjoint representation | Up to 64 |

The one-hot lifting achieves a **sparse Pauli decomposition** (4 terms per
generator, all with uniform coefficient ±1/4), which is structurally optimal for
qubit-based quantum simulation.

---

## 5. Minimality vs Uniqueness vs Optimality

### 5.1 Minimality (What Is Proved)

**Proved**: Three qubits are the *minimum* number of qubits for one-hot binary
triplet encoding.

This is a simple counting argument: the number of Hamming-weight-1 strings in
{0,1}^n equals n; to have ≥ 3 such strings requires n ≥ 3.

### 5.2 Uniqueness (What Is Not Claimed)

**Not proved**: The triqubit one-hot encoding is the *unique* way to realize SU(3)
on a qubit system.

Alternative realizations exist:
- **Adjoint representation on 8 qubits**: SU(3) acts on the 8-dimensional adjoint
  space directly; requires 3 qubits for the 8-dimensional space but represents a
  different sector.
- **Qubit encodings of qutrits**: Techniques exist to encode one qutrit into 2 or
  3 qubits using non-one-hot mappings (e.g., Ding et al. 2023 for qudit simulation).
- **Gauge group encodings for lattice QCD**: Various qubit register choices for
  SU(3) link variables exist (Byrnes-Yamamoto, Ciavarella-Klco-Savage, etc.) using
  different binary embeddings.
- **Minimal qubit encoding of SU(3) generators**: Requires ⌈log₂ 9⌉ = 4 qubits
  to store all 9 generators of u(3) in binary; different from the one-hot approach.

Uniqueness is not established because there exist multiple valid qubit embeddings
of SU(3), each with different properties.

### 5.3 Optimality (Context-Dependent)

**Not universally proved, but supported under specific assumptions**:
The triqubit may be *optimal* under binary-substrate-plus-QEC assumptions.

See `triqubit_optimality_criteria.md` for a detailed analysis of optimality metrics.
Briefly:
- Under the constraint that the encoding must be one-hot (binary, weight-1), the
  triqubit achieves the minimum n = 3.
- Under the constraint that color permutation symmetry (Weyl group S₃) be realizable
  as single-layer SWAP circuits, the triqubit is natural and efficient.
- Under quantum error correction considerations, the Hamming-weight-1 stabilizer
  structure provides natural single-error detection.

### 5.4 Summary Table

| Property | Status | Justification |
|----------|--------|---------------|
| 3 qubits minimal for one-hot binary triplet | ✅ Proved | Counting argument (§3.2) |
| Triqubit unique among all SU(3) qubit realizations | ❌ Not proved | Multiple alternatives exist (§5.2) |
| Triqubit optimal under binary + QEC assumptions | 🔶 Supported | See triqubit_optimality_criteria.md |
| Triqubit equivalent to qutrit in all respects | ❌ Not claimed | Different substrates; triqubit has overhead |
| One-hot sector physically privileged | 🔶 Conjectural | See one_hot_sector_dynamics.md |

---

## 6. References

- Nielsen, M.A. & Chuang, I.L. (2000). *Quantum Computation and Quantum
  Information.* Cambridge University Press.
- Ciavarella, A., Klco, N., Savage, M.J. (2021). "Trailhead for quantum simulation
  of SU(3)." *Phys. Rev. D* 103, 094501.
- Georgi, H. (1982). *Lie Algebras in Particle Physics.* Benjamin/Cummings.
- Jaroš, D. — `THEORY_COMPARISONS/su3_qubit_mapping/su3_qubit_core/mapping.py`
- Jaroš, D. — `THEORY_COMPARISONS/su3_qubit_mapping/README.md`
- Jaroš, D. — `consolidation_project/appendix_G_internal_color_symmetry.tex`
