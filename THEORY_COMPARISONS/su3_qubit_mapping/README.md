# SU(3) → 3-Qubit Space Mapping

## Overview

This sandbox implements the explicit **Lie algebra homomorphism**

    φ: su(3) → End(ℂ²⊗ℂ²⊗ℂ²)

that maps the 8 SU(3) generators (Gell-Mann matrices λ₁..λ₈) into the operator
algebra of three qubits.

---

## Mathematical Framework

### Construction: One-Hot Color Encoding

The 3-dimensional color space ℂ³ (with basis states |r⟩, |g⟩, |b⟩) embeds
isometrically into the 8-dimensional 3-qubit space via the **one-hot encoding**:

```
|r⟩  →  |100⟩  =  |1⟩⊗|0⟩⊗|0⟩   (index 4)
|g⟩  →  |010⟩  =  |0⟩⊗|1⟩⊗|0⟩   (index 2)
|b⟩  →  |001⟩  =  |0⟩⊗|0⟩⊗|1⟩   (index 1)
```

The embedding matrix `P` (8×3) satisfies `P† P = I₃` (isometric).

### Lifted Generators

Each Gell-Mann matrix λ_a lifts to an 8×8 operator:

    L_a = P λ_a P†

**Algebra preservation**: Because `P† P = I₃`:

    [L_a, L_b] = P [λ_a, λ_b] P† = 2i f_{abc} L_c  ✓

The map `φ(λ_a) = L_a` is a faithful Lie algebra homomorphism.

### Explicit Pauli Decompositions

Each lifted generator decomposes in the Pauli tensor-product basis
`σ_i ⊗ σ_j ⊗ σ_k` (indices: 0=I, 1=X, 2=Y, 3=Z):

| Generator | Pauli decomposition |
|-----------|---------------------|
| L₁ (λ₁) | ¼(XX⊗I + XX⊗Z + YY⊗I + YY⊗Z) |
| L₂ (λ₂) | ¼(XY⊗I + XY⊗Z − YX⊗I − YX⊗Z) |
| L₃ (λ₃) | ¼(IZ⊗I + IZ⊗Z − ZI⊗I − ZI⊗Z) |
| L₄ (λ₄) | ¼(XI⊗X + XZ⊗X + YI⊗Y + YZ⊗Y) |
| L₅ (λ₅) | ¼(XI⊗Y + XZ⊗Y − YI⊗X − YZ⊗X) |
| L₆ (λ₆) | ¼(IX⊗X + IY⊗Y + ZX⊗X + ZY⊗Y) |
| L₇ (λ₇) | ¼(IX⊗Y − IY⊗X + ZX⊗Y − ZY⊗X) |
| L₈ (λ₈) | (see numerical output; involves IIZ, ZZI, IZZ, ZII, IZI, ZIZ) |

(shorthand: `AB⊗C` = `σ_A ⊗ σ_B ⊗ σ_C`)

---

## The 9 → 8 Algebraic Constraint (Color Neutrality)

The Lie algebra **u(3)** acting on the color subspace has **9 generators**:

- **6 off-diagonal**: L₁, L₂ (rg-sector), L₄, L₅ (rb-sector), L₆, L₇ (gb-sector)
- **3 diagonal projectors**: D_r = |r⟩⟨r|,  D_g = |g⟩⟨g|,  D_b = |b⟩⟨b|

The **color neutrality constraint** (analogous to SU(3) tracelessness):

    D_r + D_g + D_b = Π_color   (identity on the color subspace)

This identifies the **u(1) direction** (overall phase generator), reducing u(3) → su(3).

**In single-qubit terms** (σ_z^(i) restricted to the color subspace):

```
σ_z^(1)|color = diag(−1, +1, +1)_{rgb}
σ_z^(2)|color = diag(+1, −1, +1)_{rgb}
σ_z^(3)|color = diag(+1, +1, −1)_{rgb}
─────────────────────────────────────────
Sum            = diag(+1, +1, +1) = I₃   ← the constraint
```

The **two traceless combinations** give the su(3) Cartan generators:
```
H₃ ∝ σ_z^(1) − σ_z^(2) = diag(−2, +2, 0)  ∝ λ₃
H₈ ∝ σ_z^(1) + σ_z^(2) − 2σ_z^(3) = diag(−2, −2, +4) ∝ λ₈
```

---

## Casimir Operators in the Qubit Representation

### Quadratic Casimir

    C₁ = (1/4) Σ_a λ_a²

- **Fundamental (3D)**:  C₁ = (4/3) I₃
- **Lifted (8D)**:       C₁^(8) = (4/3) Π_color

In the Pauli basis:

    C₁^(8) = (4/3) Π_color
    Π_color = (1/8)[3·I⊗I⊗I + I⊗I⊗Z + I⊗Z⊗I + Z⊗I⊗I
                    − I⊗Z⊗Z − Z⊗I⊗Z − Z⊗Z⊗I − 3·Z⊗Z⊗Z]

### Cubic Casimir

    C₂ = d_{abc} λ_a λ_b λ_c   (d_{abc} = symmetric structure constants)

- **Fundamental (3D)**:  C₂ = c₂ I₃  (c₂ ≈ 8.889)
- **Lifted (8D)**:       C₂^(8) = c₂ Π_color

Both Casimirs commute with all generators: **[C_i, L_a] = 0** for all a.

---

## Implementation Structure

### `su3_qubit_core/`

| File | Contents |
|------|----------|
| `gell_mann.py` | Gell-Mann matrices, structure constants f_{abc}, symmetric d-tensor |
| `qubit_ops.py` | Pauli matrices, 3-qubit tensor products, Pauli decomposition |
| `mapping.py` | One-hot embedding, lifted generators L_a, Pauli decompositions, constraint |
| `casimir.py` | C₁ and C₂ in 3D and 8D, qubit decompositions, verification |

### `tests/`

| Test file | What it checks |
|-----------|----------------|
| `test_gell_mann.py` | Normalisation, commutation, structure constants, Jacobi identity |
| `test_mapping.py` | Embedding, lifted generators, SU(3) algebra, Pauli decompositions, constraint |
| `test_casimir.py` | Casimir eigenvalues, commutativity, Pauli decompositions, analytical formulas |

### `experiments/`

| Script | Purpose |
|--------|---------|
| `e01_mapping_summary.py` | Print complete mapping table with all Pauli decompositions |

---

## Running

```bash
# From repository root:

# Run tests
pytest THEORY_COMPARISONS/su3_qubit_mapping/tests/ -v

# Run experiment (prints full mapping table)
python -m THEORY_COMPARISONS.su3_qubit_mapping.experiments.e01_mapping_summary
```

**Expected runtime**: < 1 second for tests, < 2 seconds for experiment.

---

## Key Results

1. **Homomorphism**: φ(λ_a) = P λ_a P† is a Lie algebra homomorphism su(3) → End(ℂ⁸)

2. **Constraint (9→8)**: D_r + D_g + D_b = Π_color eliminates the u(1) direction,
   reducing 3 diagonal generators → 2 Cartan generators (traceless)

3. **Pauli structure**: Each lifted generator involves exactly 4 terms of the form
   (2-qubit Pauli) ⊗ (1-qubit projector), with uniform coefficient ±1/4

4. **Casimir operators**: Both Casimirs act as c · Π_color in the qubit space;
   the Pauli decomposition of Π_color involves only Z-type operators
   (no X or Y needed to express the Casimir)

---

## Notes

- This is a **mathematical sandbox** — no physical interpretation is claimed
- The qubit space ℂ²⊗ℂ²⊗ℂ² carries an su(3) action via the lifted generators;
  this is NOT an isomorphism to su(2)³ (which has dimension 9, not 8)
- The mapping uses only the 3-dimensional color subspace of the 8-dimensional qubit space
- The full 8D space carries the **adjoint representation** of SU(3) when the
  generators act on themselves via the adjoint action (separate construction)

---

## Status: ✅ COMPLETE

- Core homomorphism implemented and verified
- All 51 tests pass
- Explicit Pauli decompositions for all 8 generators computed
- Casimir operators in qubit representation derived analytically
