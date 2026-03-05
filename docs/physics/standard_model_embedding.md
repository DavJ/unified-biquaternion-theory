<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# UBT Standard Model Embedding

**Status:** Partial derivation — see status table below  
**Version:** v27 (UBT Nobel Alignment)  
**Cross-references:**
- `docs/sm_embedding_roadmap.md` (open problems list)
- `docs/sm_qed_qcd_status.md` (per-sector status)
- `canonical/interactions/qed.tex`, `canonical/interactions/qcd.tex`
- `consolidation_project/appendix_E_SM_QCD_embedding.tex`
- `consolidation_project/appendix_G_internal_color_symmetry.tex` (SU(3) candidate construction)
- `reports/associative_su3_scan.md` (Aut(ℂ⊗ℍ) rank obstruction result)

---

## 1. Summary

The Standard Model gauge group `G_SM = SU(3)_c × SU(2)_L × U(1)_Y` is partially
embedded in UBT through the structure of the biquaternionic field `Θ(q,τ)` and
its automorphism algebra.

**Overall embedding status:**

| Sector | Status | Mathematical Basis |
|--------|--------|--------------------|
| U(1)_Y electromagnetic | ✅ Derived | Aut(ℂ) ≅ U(1) → minimal coupling |
| SU(2)_L weak isospin | ✅ Candidate | Left-multiplication on ℍ → sp(1) ≅ su(2) |
| SU(3)_c color | ✅ Formally derived | Internal phase fiber: Θ=Ξ·𝒰, 𝒰∈U(3); Theorems G.A–G.D in Appendix G prove su(3) algebra, fundamental/adjoint representations, and decoupling. No octonions. |
| G_SM direct product | ✅ Proved | Theorem G.D: left-right commutativity of matrix multiplication gives SU(3)_c×SU(2)_L×U(1)_Y |
| Chirality (L/R asymmetry) | ❌ Open | Key missing piece |
| Three generations | ❌ Open | Why exactly 3? |
| Yukawa couplings | ⚠️ Semi-empirical | Structure motivated; matrix elements fitted |

---

## 2. Gauge Group Structure from Biquaternionic Algebra

### 2.1 The Associative Sector: ℂ⊗ℍ

The biquaternionic algebra `ℬ = ℂ⊗ℍ` is an 8-dimensional real algebra (or
4-dimensional complex algebra). Its automorphism group is:

```
Aut(ℂ⊗ℍ) ⊇ U(1) × SU(2)
```

This follows from the factored structure:
- `Aut(ℂ) = U(1)` — complex phase rotations → U(1)_Y candidate
- `Aut(ℍ) = SO(3) ≅ SU(2)/ℤ₂` → SU(2)_L candidate (via double cover)

**Caveat (from `reports/associative_su3_scan.md`):** A complete scan of
`Aut(ℂ⊗ℍ)` confirms that SU(3) does **not** appear in the **automorphism group**
of the associative algebra alone (rank obstruction: su(3) has rank 2, gl(2,ℂ) has
rank 1; SU(3) ⊄ Aut(ℂ⊗ℍ)).

**However**, this does not rule out SU(3) from the theory. Appendix G
(`consolidation_project/appendix_G_internal_color_symmetry.tex`) presents a
**non-octonionic candidate construction** via the internal phase fiber of Θ itself
(see Section 2.4 below).

### 2.2 U(1) Electromagnetic from Complex Phase

The U(1)_Y hypercharge symmetry is the most rigorously derived gauge sector:

```
Θ(q,τ) → e^{iα Y} Θ(q,τ),    α ∈ ℝ
```

This is the global complex phase rotation of the fundamental field. Making this
local (α = α(x)) and requiring gauge invariance of the action forces the
introduction of the gauge connection `B_μ` (the hypercharge gauge boson).

The standard coupling is:

```
D_μ Θ = ∂_μ Θ + ig₁ B_μ Y Θ
```

This reproduces standard QED in the abelian sector. **Status: Proven** (see
`consolidation_project/appendix_C_electromagnetism_gauge_consolidated.tex`).

### 2.3 SU(2)_L Weak Isospin from Quaternionic Structure

The three imaginary units `{𝐢, 𝐣, 𝐤}` of `ℍ` generate `sp(1) ≅ su(2)`:

```
[L_i, L_j] = ε_{ijk} L_k     (Lie algebra of SU(2))
```

Left-multiplication by unit quaternions on `ℬ` gives an SU(2) action. The
**left**-action (as opposed to right) provides the chiral SU(2)_L:

```
Θ → e^{iθ^a T^a_L} Θ,    T^a_L = (1/2){𝐢,𝐣,𝐤} acting from left
```

Making this local gives the weak gauge bosons `W_μ^a`.

**Status: Candidate** — SU(2) structure is present; but:
- The physical identification of `T^3` with weak isospin requires choosing
  a preferred quaternionic axis
- Left-chirality (SU(2)_L vs SU(2)_R) requires an additional physical argument
- Hypercharge assignment remains open

### 2.4 SU(3)_c Color from Internal Phase Fiber (Appendix G Approach)

SU(3) color arises in UBT from the **internal phase structure** of the Θ-field itself,
without requiring an octonionic extension. The construction (from
`consolidation_project/appendix_G_internal_color_symmetry.tex`) proceeds as follows:

**Factorization of Θ:**
```
Θ(x,τ) = Ξ(x,τ) · 𝒰(x,τ),    𝒰 ∈ U(3),  𝒰†𝒰 = 1₃
```

where Ξ carries the biquaternionic kinematics (metric, GR sector) and 𝒰 is a
unitary internal phase factor acting on a rank-3 fiber. The traceless part
immediately gives SU(3):
```
Φ ∈ su(3) ⟺ tr Φ = 0     (9 − 1 = 8 generators)
```

The color connection emerges as the Maurer–Cartan form:
```
A_μ = 𝒰† ∂_μ 𝒰 − (1/3) Tr(𝒰† ∂_μ 𝒰) 1₃  ∈  su(3)
```

This is not an externally postulated gauge field — it is the intrinsic phase
connection of Θ's internal fiber. The Yang–Mills field strength
`F_μν = ∂_μA_ν − ∂_νA_μ + [A_μ,A_ν]` follows automatically.

**Status: Formally Derived (Appendix G, Theorems G.A–G.D)**

| Item | Theorem | Result |
|------|---------|--------|
| su(3) Lie algebra | Theorem G.A | Traceless Hermitian 3×3 matrices with bracket [-i·,·] ≅ su(3); proved via dimension, closure, Jacobi, explicit isomorphism |
| Quarks in fundamental **3** | Proposition G.B | Right action on ℂ³ is the unique 3D irrep by transitivity; weights (T³,T⁸) computed explicitly |
| Gluons in adjoint **8** | Theorem G.C | Gauge transformation A_μ → V⁻¹A_μV + V⁻¹∂_μV proved by direct substitution; infinitesimal form gives adjoint generators |
| SU(3)×SU(2)×U(1) direct product | Theorem G.D | Left-right commutativity (L·Θ)·R = L·(Θ·R); covariant derivative checked for independence under both factors |
| Confinement | Open | Clay Millennium problem; not derived in standard QFT either |

**Rank-3 motivation:** The fiber rank equals the number of imaginary units of ℍ (i, j, k), and the Siegel upper half-space H₃ is the unique parameter space consistent with the 3×3 period matrix Ω.

**Octonionic route (Track B — superseded):**
An independent Track B hypothesis proposed extending to `ℂ⊗𝕆`. This is no longer needed as the primary approach; Appendix G provides a complete non-octonionic derivation.

---

## 3. Fermion Sector

### 3.1 Dirac Equation from UBT Field Equation

The UBT field equation `∇†∇ Θ = κ 𝒯` contains the Dirac equation as a
first-order factor in the free, flat-space limit:

```
(∂_τ − i σ^μ ∂_μ)(∂_τ + i σ^μ ∂_μ) Θ = 0
```

The inner factor `(∂_τ + i σ^μ ∂_μ) Θ = 0` is a generalized Dirac equation
with complex-time evolution. In the ψ→0 limit, it reduces to the standard Dirac
equation `(i γ^μ ∂_μ − m) ψ = 0`. **Status: Proven** (see
`consolidation_project/appendix_D_qed_consolidated.tex`).

### 3.2 Electron Mass from Spectral Formula

The electron mass emerges from the spectral structure of the `Θ` field in the
compact ψ-dimension:

```
m_e ≈ A·n_e^p − B_m·n_e·ln(n_e)     (n_e = spectral mode number for electron)
```

Numerical result: `m_e ≈ 0.5099 MeV` (0.22% from experiment).  
**Status: Semi-empirical** (2 free parameters A, B_m).

### 3.3 Muon and Tau Masses — Open Problem

The muon and tau mass ratios `m_μ/m_e ≈ 207` and `m_τ/m_e ≈ 3477` are
**not yet derived** from the current spectral formula. The naive Kaluza-Klein
approach gives incorrect ratios (1:2 instead of 1:207). A new mechanism is
required — possibly involving ψ-instanton configurations.

See `research_tracks/three_generations/` for current approaches.

---

## 4. Gauge Coupling Constants

### 4.1 Status

| Coupling | Symbol | Derived? | Current Approach |
|----------|--------|----------|-----------------|
| Fine structure constant | α = g₁²/4π ≈ 1/137 | ✅ Baseline | Torus compactification; see `STATUS_ALPHA.md` |
| Weak coupling | g₂ | ❌ Fitted | Electroweak unification not yet derived |
| Strong coupling | g₃ = α_s | ❌ Fitted | QCD scale Λ_QCD semi-empirical |
| Weinberg angle | sin²θ_W ≈ 0.231 | ❌ Semi-empirical | 1 free parameter |

### 4.2 Fine Structure Constant (Most Advanced Result)

The inverse fine structure constant is derived from the winding number
quantization in the compact imaginary time dimension:

```
α⁻¹(bare) = 137     (from torus mode stability; 0 free parameters)
α⁻¹(corrected) = 137.036    (with two-loop QED correction; 0 additional parameters)
```

See `STATUS_ALPHA.md` and `docs/physics/action_formulation.md` for details.

---

## 5. Covariant Gauge Derivatives

### 5.1 Full Covariant Derivative

The complete SM covariant derivative acting on Θ is:

```
D_μ Θ = ∂_μ Θ + Ω_μ^grav Θ + ig₁ B_μ Y Θ + ig₂ W_μ^a T^a Θ + ig₃ G_μ^A λ^A Θ
```

where:
- `Ω_μ^grav` = gravitational connection (see `canonical/geometry/biquaternion_connection.tex`)
- `B_μ` = U(1)_Y hypercharge gauge field
- `W_μ^a` (a=1,2,3) = SU(2)_L weak gauge fields
- `G_μ^A` (A=1,...,8) = SU(3)_c gluon fields
- `Y, T^a, λ^A` = generators of respective gauge groups

### 5.2 Ward Identity

In the electromagnetic sector, the Ward identity follows from U(1) gauge invariance:

```
k_μ M^μ = 0     (for any process with external photon of momentum k)
```

This is automatically satisfied by the UBT covariant derivative structure.
**Status: Proven** (see `consolidation_project/appendix_CT_two_loop_baseline.tex`).

---

## 6. Testable Predictions from SM Embedding

| Prediction | Value | Standard Model | Significance |
|------------|-------|----------------|--------------|
| α⁻¹(bare) = 137 | 137.000 | 137.036 (running) | UBT predicts bare value geometrically |
| QED correction | +0.036 | — | Matches 2-loop QED exactly |
| Neutrino oscillations | UBT phase → lepton mixing | PDG | Geometric phase provides natural CP violation |
| g-2 anomaly | UBT predicts small correction via ψ-sector | Experiment | Testable at Fermilab |

---

## 7. What Is Needed for Complete Derivation

Priority gaps (ordered by blocking impact):

1. **Hypercharge quantization** — Derive rational hypercharge assignments geometrically
2. **Chirality mechanism** — Derive why only SU(2)_L (left) and not SU(2)_R (right)
3. **Three-generation mechanism** — Derive why exactly 3 fermion generations
4. **Weinberg angle** — Derive `sin²θ_W` without fitting
5. **Confinement** — Open problem in standard QFT (Clay Millennium Prize); color confinement not yet derived

*Note: SU(3) Lie algebra, fundamental/adjoint representations, and SU(3)_c × SU(2)_L × U(1)_Y decoupling are now formally proved (Theorems G.A–G.D in `consolidation_project/appendix_G_internal_color_symmetry.tex`).*

See `docs/sm_embedding_roadmap.md` for the full roadmap.

---

## 8. References Within Repository

| Topic | Document |
|-------|----------|
| Core SM derivation | `consolidation_project/appendix_E_SM_QCD_embedding.tex` |
| QED recovery | `consolidation_project/appendix_D_qed_consolidated.tex` |
| Electromagnetism | `consolidation_project/appendix_C_electromagnetism_gauge_consolidated.tex` |
| Fermion masses | `consolidation_project/appendix_E2_fermion_masses.tex` |
| Color (internal phase fiber) | `consolidation_project/appendix_G_internal_color_symmetry.tex` |
| Associative SU(3) scan (Aut failure) | `reports/associative_su3_scan.md` |
| SM embedding roadmap | `docs/sm_embedding_roadmap.md` |

---

*© 2025 Ing. David Jaroš — CC BY-NC-ND 4.0*
