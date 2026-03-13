<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Fundamental Objects

The mathematical foundation of UBT is the **biquaternion algebra** ℂ⊗ℍ and its
associated structures.

**Canonical source**: [`canonical/algebra/`](https://github.com/DavJ/unified-biquaternion-theory/tree/main/canonical/algebra)  
**Definitions**: [`canonical/CANONICAL_DEFINITIONS.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/CANONICAL_DEFINITIONS.md)  
**Axioms**: [`canonical/AXIOMS.md`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/AXIOMS.md)

---

## The Biquaternion Algebra ℂ⊗ℍ

A **biquaternion** is an element of ℂ⊗ℍ — the tensor product of complex numbers with
the quaternion algebra. Concretely:

```
q = a + bi + cj + dk,   a,b,c,d ∈ ℂ
```

Key algebraic fact: **ℂ⊗ℍ ≅ Mat(2,ℂ)** — the algebra of 2×2 complex matrices.
This isomorphism is the structural bridge to the Standard Model.

**Canonical file**: [`canonical/algebra/biquaternion_algebra.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/algebra/biquaternion_algebra.tex)  
**Summary table**: [`canonical/algebra/algebra_summary_table.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/algebra/algebra_summary_table.tex)

---

## Complex Time T_B

UBT extends real time to **biquaternion time**:

```
T_B = t + iψ + jχ + kξ
```

where t is real time and ψ, χ, ξ are imaginary components. In the main physical
sector only τ = t + iψ is active (two-component complex time).

**Canonical file**: [`canonical/fields/biquaternion_time.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/fields/biquaternion_time.tex)

---

## Involutions and Z₂×Z₂×Z₂

The imaginary quaternion subspace Im(ℍ) = span{i, j, k} admits three involutions
P_I, P_J, P_K that form a Z₂×Z₂×Z₂ group. This structure forces SU(3)_c with
zero free parameters (dim Im(ℍ) = 3 is the key constraint).

**Canonical file**: [`canonical/algebra/involutions_Z2xZ2xZ2.tex`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/canonical/algebra/involutions_Z2xZ2xZ2.tex)

---

## Automorphism Group

```
Aut(ℂ⊗ℍ) ≅ [GL(2,ℂ) × GL(2,ℂ)] / ℤ₂
```

The left and right actions of this group on Θ give rise to the electroweak and
color gauge symmetries.  
Status: **Proved [L0]**

**Canonical file**: [`ARCHIVE/archive_legacy/consolidation_project/appendix_E2_SM_geometry.tex §1`](https://github.com/DavJ/unified-biquaternion-theory/blob/main/ARCHIVE/archive_legacy/consolidation_project/appendix_E2_SM_geometry.tex)

---

## See Also

- [Biquaternion Algebra](Biquaternion_Algebra) — mathematical background
- [Theta Field](Theta_Field) — the fundamental field built on this algebra
- [Gauge Structure](Gauge_Structure) — gauge symmetries from algebra automorphisms
