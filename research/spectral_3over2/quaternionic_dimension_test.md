<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# quaternionic_dimension_test.md — Testing Im(ℍ) as a Spectral Manifold

**Program:** `ubt_spectral_3over2_program` — Step 6  
**Track:** SPECTRAL — independent of Hecke / twin-prime  
**Date:** 2026-03-10

---

## 1. Question Being Tested

Can the three imaginary quaternion directions **I, J, K** — which form
`Im(ℍ) = span{I, J, K}` — provide a **spectral dimension** of 3 for the
Θ-field operator, in a way that rigorously produces the Weyl law
`N(λ) ~ C · λ^(3/2)`?

This is distinct from the purely algebraic fact that `dim_ℝ(Im(ℍ)) = 3`.

---

## 2. What Is Already Established (No New Assumptions)

| Fact | Source | Status |
|------|--------|--------|
| `dim_ℝ(Im(ℍ)) = 3` | `b_base_hausdorff.tex` Lemma 1 | **[PROVED]** |
| Im(ℍ) = span{I, J, K} is the gauge mode space | `b_base_hausdorff.tex` | **[PROVED]** |
| Gaussian integral gives (det A)^{-1/2} in d variables | standard mathematics | **[PROVED]** |
| One-loop Γ₁ ∝ (d/2) · Tr ln Ô with d = 3 | `heat_kernel_theta.tex` Prop. 1 | **[PROVED]** |

---

## 3. Lie Algebra Dimension vs. Spectral Dimension

### 3.1 Lie algebra dimensions in UBT

The gauge group SU(3) × SU(2) × U(1) has:
- `dim(su(3)) = 8`
- `dim(su(2)) = 3`
- `dim(u(1)) = 1`
- Total: 12 = N_eff (proved)

**None of these is 3 in the sense relevant for the spectral exponent.**  
The Lie algebra dimension of SU(2) is 3, but:
- This counts the generators of the weak sector only (not all N_eff = 12).
- The relevant d = 3 in the B_base formula comes from Im(ℍ) ⊂ ℍ, not from su(2).

**Verdict:** The coincidence `dim(su(2)) = dim_ℝ(Im(ℍ)) = 3` is a coincidence
of the number 3; they describe different structures.
The spectral 3/2 mechanism uses `dim_ℝ(Im(ℍ)) = 3`, not `dim(su(2)) = 3`.

### 3.2 SU(3)-related internal sector

SU(3) has dimension 8. The number 8 does not produce 3/2 as d/2 = 4, not 3/2.
The SU(3) sector is **not** the source of the spectral dimension 3.

**Verdict:** The SU(3) sector is irrelevant for the spectral 3/2 mechanism.

---

## 4. Is Im(ℍ) a Spectral Manifold?

A *spectral manifold* (in the sense relevant for the Weyl law) is a
Riemannian manifold M of dimension d such that:
1. A Laplace-Beltrami operator `Δ_M` is well-defined on M.
2. The eigenvalue counting function satisfies `N(λ) ~ C · vol(M) · λ^(d/2)`.

### 4.1 Im(ℍ) as a linear space

`Im(ℍ) ≅ ℝ³` as a **linear space** (vector space over ℝ).
As such, it carries the standard Euclidean Laplacian:
```
Δ_{Im(ℍ)} = ∂²/∂I² + ∂²/∂J² + ∂²/∂K²
```
and the Weyl law on ℝ³ gives `N(λ) ~ C₃ · λ^(3/2)`.

**Conclusion:** Im(ℍ) **does** support a 3D Laplacian with the correct
Weyl exponent 3/2 — **as a 3-dimensional Euclidean space**.

### 4.2 The role of Im(ℍ) in UBT mode counting

In UBT, the vacuum polarisation integral runs over **spacetime momenta**
`k ∈ ℝ⁴`, not over `Im(ℍ)` directly.
The three components of `δΘ_V ∈ Im(ℍ)` enter as:
- **Three independent copies** of a scalar field in spacetime (multiplicity factor).
- Not as three spatial directions.

Therefore Im(ℍ) is a **multiplicity space** for UBT mode counting,
not a spectral manifold over which the Θ-Laplacian acts.

**Critical distinction:**

| Role | Im(ℍ) enters as | d_eff contribution |
|------|----------------|-------------------|
| Linear space (algebraic) | multiplicity d = 3 in Tr ln Ô | factor d in coefficient, not in exponent of λ |
| Spectral manifold (geometric) | base of a Laplacian Δ_{Im(ℍ)} | exponent d/2 = 3/2 in N(λ) |

The current evidence supports the **first role** (multiplicity), not the second.

---

## 5. Can Im(ℍ) Act as Both?

The question is whether the multiplicity factor d = 3 and the spectral
dimension d = 3 can be identified, giving a self-consistent picture.

### 5.1 Analogy with the standard model fermion count

In d-dimensional QFT, the one-loop effective action for N real scalar fields is:
```
Γ₁ = N/2 · Tr ln Ô = (d/2) · Tr ln Ô  (identifying N = d)
```
If the N fields live in a d-dimensional internal space, the system is
equivalent to a single field on a d-dimensional **product space**:
```
(spacetime ℝ⁴) × (internal ℝ^N)
```
The Weyl law on this product space gives `N(λ) ~ λ^{(4+N)/2}`,
which is **not** the same as `λ^{N/2}`.

**Verdict:** Simply identifying d = N (multiplicity) does not give
a d-dimensional Weyl law. The product space gives `(4+d)/2`, not `d/2`.

### 5.2 When multiplicity gives the d/2 exponent

The d/2 exponent appears in **one specific way**:
as the coefficient of `Tr ln Ô` in the one-loop effective action.
This exponent governs the **amplitude** of B_base, not the spectral power.

Specifically (Proposition 1 in `heat_kernel_theta.tex`):
```
Γ₁ = (d/2) · Tr ln Ô  →  B ∝ (d/2) · [gauge-coupling integral]
```
If the gauge-coupling integral evaluates to `N_eff^{1/2} · (constant)`,
then `B = (d/2) · N_eff^{1/2} · C = (3/2) · N_eff^{1/2} · C`.

For `B = N_eff^{3/2}` one needs `C = N_eff`, which remains unproved.

---

## 6. Test: Span_ℂ{I, J, K} as a 3D Complex Mode Space

The complexification of Im(ℍ) is `Im(ℍ) ⊗ ℂ ≅ ℂ³`.
Under SU(3) (which acts on ℂ³ in the fundamental representation),
this space carries a natural Hermitian metric and a Laplacian.

**Question:** Is the vacuum polarisation tensor for the strong sector
equivalent to a Laplacian on ℂ³ ≅ Im(ℍ) ⊗ ℂ?

**Answer (current evidence):**
- The strong sector gauge group is SU(3), acting on colour triplets in ℂ³.
- The dimension of ℂ³ as a real manifold is 6, not 3.
- `N_eff^{6/2} = N_eff³ ≠ N_eff^{3/2}`.

**Verdict:** The complexified Im(ℍ) gives d = 6, not d = 3.
This path is a **[DEAD END]** for the spectral 3/2 mechanism.

---

## 7. Summary: Quaternionic Dimension Test Results

| Hypothesis | Test result | Status |
|-----------|------------|--------|
| Im(ℍ) is a 3D linear space | `dim_ℝ(Im(ℍ)) = 3` | **[PROVED]** |
| Im(ℍ) contributes d = 3 multiplicity to Γ₁ | $(d/2)$ in one-loop coefficient | **[PROVED]** |
| Im(ℍ) is a spectral manifold giving `N(λ) ~ λ^{3/2}` | Weyl law on ℝ³ holds | [MATHEMATICAL FACT but not UBT mechanism] |
| Im(ℍ) = spectral base for Θ-Laplacian in UBT | Θ-Laplacian acts on spacetime ℝ⁴, not Im(ℍ) | **[NOT SUPPORTED]** |
| `dim(su(2)) = 3` is the same 3 | Coincidence of number 3; different structures | **[REJECTED — only analogy]** |
| Complexified Im(ℍ) ⊗ ℂ ≅ ℂ³ gives d = 3 | d_real = 6, not 3 | **[DEAD END]** |
| 3D residual from p₀ integration | p₀-integral reduces to 3D (unverified) | [NEW CANDIDATE — see weyl_counting_theta.tex] |

---

## 8. Conclusion

The three imaginary quaternion directions I, J, K provide:

1. **A proved algebraic dimension:** `dim_ℝ(Im(ℍ)) = 3` — this gives the
   multiplicity factor d = 3 in the Gaussian path integral.

2. **A proved Gaussian exponent:** d/2 = 3/2 in the one-loop effective action.

3. **A supported but unproved spectral interpretation:** If the vacuum
   polarisation integral is effectively 3-dimensional (from p₀ reduction
   or another mechanism), then `N(λ) ~ λ^{3/2}` and the Weyl law
   directly connects to B_base.

**What is rejected as analogy only:**
- Identifying `dim(su(2)) = 3` with the spectral dimension.
- Using the complexified ℂ³ (6 real dimensions).
- Assuming Im(ℍ) is the base manifold of the Θ-Laplacian without further argument.

**The honest conclusion:**
Im(ℍ) plays the role of a **multiplicity space** (giving d/2 = 3/2 in Γ₁),
not a spectral manifold.
The exponent 3/2 in B_base is algebraically motivated from this multiplicity,
but the spectral geometry interpretation (Weyl law with d = 3) requires
identifying a genuinely 3-dimensional mode space in UBT.
This remains an open problem.

---

*End of quaternionic dimension test.*
