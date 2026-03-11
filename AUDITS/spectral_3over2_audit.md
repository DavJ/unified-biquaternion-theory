<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# spectral_3over2_audit.md — Repository Audit for the Spectral 3/2 Program

**Program:** `ubt_spectral_3over2_program`  
**Track:** Independent — spectral geometry, heat kernel, Weyl counting  
**Date:** 2026-03-10  
**Status of audit:** COMPLETE  
**Independent of:** Hecke / twin-prime / 137/139 route

---

## 1. Purpose

Identify **all** existing repository files relevant to:

- Θ-operator dynamics and kinetic terms
- Spectral operators, Laplacians, Hamiltonians
- Heat kernel asymptotics and zeta regularisation
- Kaluza–Klein towers and mode counting
- Spectral determinants and functional determinants
- Density of states / Weyl counting
- B_base and the 3/2 exponent
- Three-dimensional internal structure in Im(ℍ) or SU(3)

---

## 2. Θ-Operator Candidates

### 2.1 Primary Θ-field definition

| File | Relevant content | Status |
|------|-----------------|--------|
| `THETA_FIELD_DEFINITION.md` | Full formal definition of Θ(q,τ): domain B⁴×C, action S[Θ], covariant derivative ∇, kinetic term ½⟨∇Θ,∇Θ⟩ | DEFINITIVE |
| `consolidation_project/appendix_A_theta_action.tex` | Rigorous action functional with measure, Hermitian structure, boundary terms, Euler–Lagrange derivation | AUTHORITATIVE |
| `canonical/bridges/theta_quantum_structure.tex` | Quantum structure of Θ: canonical quantisation, propagator, mode expansion | RELEVANT |
| `research/theta_quantum_field.tex` | QFT treatment of Θ: vacuum polarisation, KK sum, B_base remark | RELEVANT |

### 2.2 Kinetic operator identification

The UBT kinetic term is:
```
S_kin[Θ] = ½ ∫ d⁴q d²τ √|G| ⟨∇_μ Θ, ∇^μ Θ⟩
```

This implies the Θ-Laplacian (Lichnerowicz-type):
```
Δ_Θ := −∇†∇ = −G^μν ∇_μ ∇_ν
```

Files defining or using this operator:

| File | Content | Relevance |
|------|---------|-----------|
| `THETA_FIELD_DEFINITION.md §5` | Euler–Lagrange equation ∇†∇Θ + ∂V/∂Θ† = 0 | defines Δ_Θ |
| `consolidation_project/appendix_ALPHA_one_loop_biquat.tex §B.3` | KK mode expansion of Δ_Θ; vacuum polarisation integral | quantitative |
| `emergent_alpha_calculations.tex` | Full α derivation chain including Δ_Θ eigenvalues | quantitative |
| `ubt/operators/` | (directory exists, further files may be present) | check |
| `ubt/spectral/laplacian_torus.py` | Numerical Laplacian on d-torus; eigenvalue computation | numerical tool |

---

## 3. Existing Heat Kernel Mentions

| File | Content | Status |
|------|---------|--------|
| `consolidation_project/alpha_derivation/b_base_delta_d.tex §C1` | Seeley–DeWitt curvature correction to heat kernel; concluded DEAD END (correction → 0 as Λ⁻²) | [DEAD END] |
| `consolidation_project/alpha_derivation/b_base_hausdorff.tex` | Gaussian path integral = heat kernel at t=½; identifies d=3 from Im(ℍ); explicit gap stated | [MOTIVATED CONJECTURE] |
| `consolidation_project/alpha_derivation/b_base_nonpert.tex` | Background for non-perturbative approaches; re-states heat kernel basis | [CONTEXT] |
| `research/B_base_spectral_determinant.tex` | Torus Laplacian, spectral zeta, N^{3/2} test (Attempt E-2) | [MOTIVATED CONJECTURE] |
| `ubt_with_chronofactor/scripts/spectral/poisson_duality_demo.py` | Poisson summation duality W(τ) = τ^{d/2} S(τ); spectral/winding duality on T^d | [TOOL] |

**Key gap identified in existing material:**  
The heat kernel for Δ_Θ on the **full** domain (ℝ⁴ × S¹ or ℝ⁴ × Im(ℍ)) has not been
computed explicitly. Existing work refers to the Gaussian identity but does not write
down K(t) = Tr(exp(−t Δ_Θ)) with explicit asymptotics.

---

## 4. Existing Spectral Determinant Mentions

| File | Content | Status |
|------|---------|--------|
| `research/B_base_spectral_determinant.tex` | det(−Δ_{T^d}) via spectral zeta ζ_Δ(s); N^{3/2} scaling test; attempt E-2 | [MOTIVATED CONJECTURE] |
| `consolidation_project/alpha_derivation/b_base_hausdorff.tex §gap` | Gap: explicit computation of det(S''[Θ₀]) on Im(ℍ) not done | [OPEN GAP] |
| `consolidation_project/alpha_derivation/b_base_delta_d.tex` | Seeley–DeWitt expansion of log det(Δ); result: curvature correction → 0 | [DEAD END] |
| `report/alpha_spectral_relation_candidates.md` | Dedekind η, torus eigenvalue spacing, spectral determinant candidates | [CANDIDATES] |

---

## 5. Kaluza–Klein Mode Documents

| File | Content | Status |
|------|---------|--------|
| `consolidation_project/appendix_ALPHA_one_loop_biquat.tex §B.3` | KK tower sum Σ_n Π^(n); mass spectrum m_n² = n²/R²_ψ + m²_0 | [PROVED framework] |
| `research/theta_quantum_field.tex §KK` | KK remark: B_base relates to Σ_n Π^(n); see B_base_spectral_determinant.tex | [REFERENCE] |
| `tools/compute_B_KK_sum.py` | Numerical KK sum; approach A1; concluded: sum diverges, no natural cutoff | [DEAD END] |
| `consolidation_project/alpha_derivation/b_base_spinor_approach.tex` | Approach A1: spinor KK modes; dead end documented | [DEAD END] |

---

## 6. B_base Related Files (complete list)

| File | Approach label | Status |
|------|---------------|--------|
| `STATUS_ALPHA.md §9` | Overview of all B_base approaches | [REFERENCE] |
| `DERIVATION_INDEX.md` | Derivation status table | [INDEX] |
| `consolidation_project/alpha_derivation/b_base_spinor_approach.tex` | A1: KK spinor | [DEAD END] |
| `consolidation_project/alpha_derivation/b_base_hausdorff.tex` | A2: spectral zeta/Hausdorff | [MOTIVATED CONJECTURE] |
| `consolidation_project/alpha_derivation/b_base_delta_d.tex` | C1,C2: Seeley–DeWitt; mode interference | [DEAD END] |
| `consolidation_project/alpha_derivation/b_base_nonpert.tex` | D1,D2,D3: unitarity, dim. transmutation, Cartan–Killing | [DEAD END] |
| `consolidation_project/alpha_derivation/b_base_ncg_a4.tex` | NCG/A4: noncommutative geometry, effective dimension | [STRUCTURAL INSIGHT] |
| `consolidation_project/alpha_derivation/b_base_g_approaches.tex` | G-approaches | [CANDIDATES] |
| `consolidation_project/alpha_derivation/b_base_kac_moody_level.tex` | Kac–Moody level | [CANDIDATES] |
| `consolidation_project/alpha_derivation/b_base_km_level_ii.tex` | Kac–Moody level II | [CANDIDATES] |
| `consolidation_project/alpha_derivation/b_base_new_directions.tex` | New directions (general) | [CANDIDATES] |
| `research/B_base_spectral_determinant.tex` | E-2: torus spectral determinant | [MOTIVATED CONJECTURE] |
| `tools/explore_b_exponent.py` | Numerical: d_eff(B) analysis | [TOOL] |
| `tools/compute_B_KK_sum.py` | Numerical: KK sum | [TOOL] |
| `emergent_alpha_calculations.tex` | Full α chain; B used but not derived | [REFERENCE] |

---

## 7. Possible 3D Internal Structure Sources

| Source | Content | Connection to d=3 |
|--------|---------|-------------------|
| `consolidation_project/alpha_derivation/b_base_hausdorff.tex §three` | PROVED: dim_ℝ(Im ℍ) = 3 | algebraic |
| `Appendix_G_Emergent_SU3.tex` | SU(3) emergence from biquaternion structure | Lie algebra dim = 8, not 3 |
| `consolidation_project/alpha_derivation/b_base_ncg_a4.tex §A4` | Effective dimension d_eff analysis | structural insight |
| `THETA_FIELD_DEFINITION.md §1` | Field decomposition Θ = Θ_S + Θ_V; V lives in Im(ℍ) | algebraic |
| `ubt/spectral/laplacian_torus.py` | Torus Laplacian in d=1,2,3 dimensions | numerical |
| `research_tracks/associative_su3/` | Associative SU(3) structure | tangential |

**Key distinction not yet made explicit in existing files:**  
The three imaginary quaternion directions {I,J,K} give a 3-dimensional *linear space*.
Whether this translates to a 3-dimensional *spectral manifold* (i.e., whether the
Laplacian governing Θ fluctuations has d_eff = 3) is the central open question of
the spectral 3/2 program.

---

## 8. Summary of What Is and Is Not Established

### Established (PROVED)

| Fact | Source |
|------|--------|
| dim_ℝ(Im ℍ) = 3 | b_base_hausdorff.tex Lemma 1 |
| Gaussian path integral gives (det A)^{-1/2} | b_base_hausdorff.tex Prop. 1 |
| One-loop flat-space result B₀ = 2π N_eff/3 = 25.133 | appendix_ALPHA_one_loop_biquat.tex |
| d_eff(B₀) = 2.595 ≠ 3 | b_base_delta_d.tex |
| Δd = d_eff(B_base) − d_eff(B₀) = 0.405 is the gap | b_base_delta_d.tex |
| Torus Laplacian eigenvalues λ_k = (2π/L)² |k|² | ubt/spectral/laplacian_torus.py |

### Conjectured / Motivated

| Fact | Source |
|------|--------|
| B_base = N_eff^{3/2} | b_base_hausdorff.tex Conjecture 1 |
| Effective spectral dimension = 3 | b_base_hausdorff.tex (algebraic motivation) |
| Heat kernel K(t) ~ (4πt)^{-3/2} for Θ-sector | b_base_delta_d.tex C1 (not derived, only referenced) |

### Not Yet Attempted in Repository

| Missing item | Where to address |
|-------------|-----------------|
| Explicit derivation of K(t) = Tr(exp(−t Δ_Θ)) with d_eff = 3 | `heat_kernel_theta.tex` (this program) |
| Weyl counting N(λ) ~ C λ^{d_eff/2} for Θ-spectrum | `weyl_counting_theta.tex` (this program) |
| Bridge from spectral counting to B_base formula | `B_base_from_spectral_density.tex` (this program) |
| Explicit identification of the Θ-Laplacian | `theta_operator_candidates.tex` (this program) |
| Test: is Im(ℍ) a spectral manifold or only an algebraic space? | `quaternionic_dimension_test.md` (this program) |

---

## 9. Independence from Hecke / Twin-Prime Program

The spectral 3/2 program is strictly independent from:

- The Hecke-worlds framework (`UBT_HeckeWorlds_theta_zeta_primes_appendix.tex`)
- The twin-prime / (137, 139) pairing route
- Any use of α⁻¹ = 137 as an input

The only shared inputs are:
- N_eff = 12 [PROVED, independent of α]
- dim_ℝ(Im ℍ) = 3 [PROVED, algebraic]
- UBT action S[Θ] [foundational]

These are available to both programs without circularity.

---

*End of audit.*
