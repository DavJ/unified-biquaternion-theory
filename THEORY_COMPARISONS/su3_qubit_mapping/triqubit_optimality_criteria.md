# Triqubit Optimality Criteria

**Author**: Ing. David Jaroš  
**Date**: 2026-03-12  
**Status**: Analysis — Optimality Criteria Definition

> © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0

---

## Purpose

This document defines the criteria under which the 3-qubit (triqubit) one-hot
cell can be called *optimal* for realizing the SU(3) color triplet sector in a
binary quantum simulation substrate.

Optimality is **context-dependent**: the triqubit may be optimal under some
criteria and suboptimal under others. This document makes each criterion precise
and states the triqubit's performance explicitly.

---

## Criterion 1: Binary Channel Count

**Definition**: Minimum number of binary channels (qubits) required to represent
the required set of states with the desired structural properties.

**Metric**: n_qubits (lower is better).

| Encoding | n_qubits | One-hot? | Isometric? |
|----------|----------|----------|------------|
| Qutrit (not qubit) | — | N/A | Yes |
| 2-bit binary (non-one-hot) | 2 | No | No |
| Triqubit (one-hot) | **3** | Yes | Yes |
| 4-qubit register (arbitrary) | 4 | Possible | Possible |

**Assessment**: Under the **one-hot + isometric embedding** constraint, n = 3 is
minimal (proved in `triqubit_minimality_note.md`). The triqubit is **optimal** by
binary channel count within the one-hot constraint.

If the one-hot constraint is relaxed, a non-one-hot 2-qubit encoding suffices for
storing 3 classical states, but at the cost of structural properties listed below.

---

## Criterion 2: Code Distance

**Definition**: The minimum Hamming distance d between any two codewords in the
encoding. Higher d provides better error detection and correction.

**Metric**: d (higher is better for noise resilience).

The one-hot triqubit codewords are:
```
|100⟩,  |010⟩,  |001⟩
```

Pairwise Hamming distances:
```
d(|100⟩, |010⟩) = 2   (differ in positions 1 and 2)
d(|010⟩, |001⟩) = 2   (differ in positions 2 and 3)
d(|100⟩, |001⟩) = 2   (differ in positions 1 and 3)
```

The code has **uniform distance d = 2**: any single-bit-flip error moves a
codeword to a non-codeword (error detection), but not to another codeword
(no uncorrectable single-bit-flip error within the code).

**Comparison**:
| Encoding | Code distance d | Single-bit flip detected? |
|----------|-----------------|--------------------------|
| 2-bit binary {00,01,10} | 1 (00↔01) | No |
| Triqubit one-hot | **2** (uniform) | Yes |
| 3-bit parity check code | 2 | Yes |
| Full quantum error correcting code (5-qubit) | 3 | Yes (corrects) |

**Assessment**: The triqubit achieves the **maximum possible code distance d = 2**
for a one-hot code with 3 codewords in 3 bits. This is optimal within the
one-hot constraint. It provides single-error *detection* but not correction.

For single-error *correction*, d ≥ 3 is required, which would need a larger code
(e.g., 5+ qubits for the standard quantum error-correcting code).

---

## Criterion 3: Noise Tolerance

**Definition**: The ability of the encoding to maintain fidelity of the SU(3)
algebra under local noise processes (bit-flip, phase-flip, depolarizing).

**Metric**: Noise threshold ε such that for single-qubit error rate p < ε, the
encoded SU(3) generators remain faithful to within a given tolerance.

### 3.1 Bit-Flip Noise (X errors)

A single bit-flip X_i on the one-hot subspace:
- Flips |100⟩ → |000⟩ or |110⟩ (depending on which bit is flipped)
- All results are outside the one-hot subspace (weight 0 or 2)
- **Error is detectable**: any bit-flip exits the code subspace

The projection Π_color (color neutrality projector) can detect this: a state
outside the one-hot sector has D_r + D_g + D_b ≠ Π_color.

**Tolerance**: All single-qubit X errors are *detectable* (though not correctable
without additional ancilla).

### 3.2 Phase-Flip Noise (Z errors)

Phase-flip Z_i on the one-hot states:
```
Z_1 |100⟩ = -|100⟩   (sign flip, still a codeword up to phase)
Z_1 |010⟩ = +|010⟩
Z_1 |001⟩ = +|001⟩
```
Phase flips on different qubits produce different relative phases between codewords:
- Z_1 acts as diag(-1, +1, +1) on {|r⟩, |g⟩, |b⟩} — equivalent to applying
  a diagonal SU(3) matrix (Cartan element).
- Z errors are not detectable by Hamming-weight checks alone; they remain in the
  code subspace but rotate the state.

**Implication**: Phase noise is the dominant vulnerability of the triqubit encoding,
as it maps code states to code states (logical errors). Additional ancilla or
syndrome measurements are needed to detect phase errors.

### 3.3 Overall Noise Assessment

| Error type | Detectable? | Correctable (single error)? |
|-----------|-------------|----------------------------|
| Bit-flip (X) | ✅ Yes (exits one-hot sector) | ❌ No (ancilla needed) |
| Phase-flip (Z) | ❌ No (stays in one-hot sector) | ❌ No |
| Combined (Y = iXZ) | ✅ Partially (X component exits) | ❌ No |

**Assessment**: The triqubit is **optimally noise-tolerant for bit-flip errors**
within the one-hot constraint (all X-errors are detected). Phase-flip errors
require additional QEC structure. The triqubit is not optimal under general
depolarizing noise without augmentation.

---

## Criterion 4: Symmetry Naturalness

**Definition**: How naturally the discrete symmetries of SU(3) (Weyl group,
outer automorphisms) are represented as simple quantum gates.

**Metric**: Gate depth and type required to implement SU(3) Weyl group elements.

The Weyl group of SU(3) ≅ S₃ (symmetric group on 3 elements) acts on the color
triplet by permuting {r, g, b}. In the triqubit one-hot encoding:

| Weyl element | Color permutation | Qubit implementation |
|-------------|------------------|---------------------|
| e (identity) | r→r, g→g, b→b | Identity |
| (r g) | r↔g | SWAP(q₁, q₂) |
| (g b) | g↔b | SWAP(q₂, q₃) |
| (r b) | r↔b | SWAP(q₁, q₃) |
| (r g b) | r→g→b→r | 2×SWAP (or CSWAP) |
| (r b g) | r→b→g→r | 2×SWAP |

Each Weyl group element is a **SWAP or SWAP-composition gate** — the simplest
2-qubit entangling gates available on quantum hardware.

**Comparison**:
| Encoding | Weyl group implementation |
|----------|--------------------------|
| Qutrit | SU(3) × U(1) rotations on ℂ³ (no simple binary gate) |
| 2-bit binary (Gray code) | Non-uniform, asymmetric gate sequences |
| Triqubit (one-hot) | **SWAP gates** (maximal simplicity) |

**Assessment**: The triqubit one-hot encoding achieves **maximal symmetry
naturalness** — the full SU(3) Weyl group is realized by the simplest possible
2-qubit gates. This is a strong structural optimality argument.

---

## Criterion 5: Energetic or Dynamical Selectivity

**Definition**: Under a physically motivated Hamiltonian (UBT effective Hamiltonian
or a natural qubit Hamiltonian), whether the one-hot subspace corresponds to the
lowest-energy sector or is otherwise dynamically distinguished.

**Metric**: Energy gap Δ between the one-hot sector and the rest of the 3-qubit
Hilbert space (larger Δ → stronger dynamical selection).

### 5.1 Hamming-Weight Penalty Hamiltonian

A natural qubit Hamiltonian that dynamically selects the one-hot sector is the
**Hamming-weight penalty**:

```
H_penalty = λ (n̂_total - 1)²
```

where n̂_total = n̂₁ + n̂₂ + n̂₃ is the total number operator and λ > 0 is a
coupling constant. This Hamiltonian:
- Has eigenvalue 0 on all one-hot states |100⟩, |010⟩, |001⟩ (Hamming weight 1)
- Has eigenvalue λ on |000⟩ (weight 0) and on the three weight-2 states
- Has eigenvalue 4λ on |111⟩ (weight 3)

The one-hot sector is thus the **ground sector** of H_penalty, with an energy gap
Δ = λ separating it from all other states.

### 5.2 Stabilizer / Syndrome Interpretation

Equivalently, the Hamming-weight-1 condition defines a **stabilizer code**: the
code space is the +1 eigenspace of the projector Π_color = |100⟩⟨100| + |010⟩⟨010|
+ |001⟩⟨001|. This can be implemented as a syndrome measurement on an ancilla.

### 5.3 Status

- **Within an explicitly constructed H_penalty**: The one-hot sector is proved to
  be the ground sector with energy gap Δ = λ. This is a **constructive proof of
  energetic selectivity** under a specific (artificial) Hamiltonian.
- **Within the UBT effective Hamiltonian**: Whether the UBT biquaternionic dynamics
  naturally prefer the one-hot sector without external penalty is **conjectural
  and open**. See `one_hot_sector_dynamics.md` for a detailed analysis.

**Assessment**: Dynamical selectivity is **proved under a specific penalty
Hamiltonian** and is **supported but not proved from first UBT principles**.

---

## Overall Optimality Summary

| Criterion | Triqubit Performance | Optimal? |
|-----------|---------------------|---------|
| Binary channel count | n = 3 (minimal under one-hot) | ✅ Yes (conditional) |
| Code distance | d = 2 (uniform, maximal for one-hot 3-codeword code) | ✅ Yes |
| Noise tolerance (X errors) | All single-qubit X errors detected | ✅ Yes |
| Noise tolerance (Z errors) | Z errors undetected without ancilla | 🔶 Partial |
| Symmetry naturalness | Weyl group = SWAP gates | ✅ Yes |
| Energetic selectivity (H_penalty) | Ground sector of Hamming-weight penalty | ✅ Yes (conditional) |
| Energetic selectivity (UBT H) | Open question | 🔶 Conjectural |

**Conclusion**: The triqubit one-hot cell is **optimal under the conjunction of**:
1. Binary substrate (no qutrits),
2. One-hot encoding constraint,
3. Isometric embedding requirement,
4. Weyl symmetry implemented as SWAP gates,
5. Hamming-weight-penalty stabilizer structure.

It is **not claimed to be universally optimal** among all possible SU(3) qubit
realizations. The qutrit outperforms it on raw channel count, and more general qubit
encodings may outperform it on full-depolarizing noise tolerance.

---

## References

- Nielsen, M.A. & Chuang, I.L. (2000). *Quantum Computation and Quantum
  Information.* Cambridge University Press. (Chapters 10–11 for QEC)
- Ciavarella, A., Klco, N., Savage, M.J. (2021). "Trailhead for quantum simulation
  of SU(3)." *Phys. Rev. D* 103, 094501.
- Gottesman, D. (1997). "Stabilizer Codes and Quantum Error Correction."
  PhD thesis, Caltech. arXiv:quant-ph/9705052.
- Jaroš, D. — `THEORY_COMPARISONS/su3_qubit_mapping/triqubit_minimality_note.md`
- Jaroš, D. — `THEORY_COMPARISONS/su3_qubit_mapping/one_hot_sector_dynamics.md`
