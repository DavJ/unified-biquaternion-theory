<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# DERIVATION_MAP.md — UBT Mathematical Derivation Map

> **Purpose**: Structured navigation map of all mathematical derivations currently
> present in the Unified Biquaternion Theory repository.  For full proof-status
> detail and gap inventory, see `DERIVATION_INDEX.md`.  For canonical definitions,
> see `canonical/README.md` and `canonical/CANONICAL_DEFINITIONS.md`.

---

## Layer Architecture

UBT derivations are organised in three layers:

| Layer | Description | Examples |
|-------|-------------|---------|
| **L0** | Pure biquaternionic geometry — no free parameters | Algebra, metric projection, SU(3) from involutions |
| **L1** | One-loop / semi-classical — at most algebraically motivated parameters | β-function, Schwinger term, N_eff=12 |
| **L2** | Higher-loop or non-perturbative — parameters from phenomenology | Mass spectrum, R-factor |

---

## 1. Algebra Foundation

**Canonical source**: `canonical/algebra/`

```
ℂ ⊗ ℍ  (biquaternion algebra)
│
├── Isomorphism:  ℂ⊗ℍ ≅ Mat(2,ℂ)                [L0 PROVED]
│   └── canonical/algebra/biquaternion_algebra.tex
│
├── Involution structure: Z₂×Z₂×Z₂                 [L0 PROVED]
│   └── canonical/su3_derivation/step1_involution_summary.tex
│
└── Biquaternion time:  T_B = t + iψ + jχ + kξ     [L0 AXIOMATIC]
    └── canonical/fields/biquaternion_time.tex
        canonical/THEORY/math/fields/biquaternion_time.tex
```

---

## 2. Fundamental Field

**Canonical source**: `canonical/fields/theta_field.tex`

```
Θ(q, τ)  (fundamental biquaternion field)
│
├── Definition and axioms                            [L0 AXIOMATIC]
│   └── canonical/fields/theta_field.tex
│
├── Master equation:  ∇†∇Θ = κT                     [L0 AXIOMATIC]
│   └── canonical/THEORY/canonical/canonical_field_equations.tex
│
└── Isotropic limit:  τ = t + iψ                    [L0]
    └── canonical/fields/theta_field.tex
```

---

## 3. Action Principle

**Canonical source**: `canonical/THEORY/canonical/canonical_action.tex`

```
S[Θ] = ∫ d⁴x √(-g) L_UBT
│
├── L_grav = R/(2κ)                                  [L0]
├── L_kin  = Tr[(D_μΘ)†(D^μΘ)]                      [L0]
├── L_gauge = -(1/4) F^a_{μν} F^{aμν}               [L0]
└── L_pot  = V(Θ)                                    [L0]
│
├── Lorentz invariance: verified by construction     [L0]
├── Euler-Lagrange → field equations                 [L1 SKETCH]
│   └── canonical/THEORY/canonical/canonical_field_equations.tex
│
└── Review appendix:
    canonical/appendices/appendix_ACTION_review.tex
```

---

## 4. Emergent Geometry

**Canonical source**: `canonical/geometry/`

```
Θ(q,τ) → geometry
│
├── Biquaternionic metric:                           [L0 PROVED]
│   G_{μν} = Tr(∂_μΘ · ∂_νΘ†) ∈ ℂ⊗ℍ
│   └── canonical/geometry/biquaternion_metric.tex
│
├── Classical metric projection:                     [L0 PROVED]
│   g_{μν} = Re(G_{μν})
│   └── canonical/geometry/metric.tex
│
├── Biquaternionic tetrad:                           [L0 PROVED]
│   └── canonical/geometry/biquaternion_tetrad.tex
│
├── Levi-Civita connection (from g_{μν}):            [L0]
│   Γ^λ_{μν} = Re(Ω^λ_{μν})
│   └── canonical/geometry/connection.tex
│       canonical/geometry/biquaternion_connection.tex
│
├── Riemann curvature tensor:                        [L0]
│   └── canonical/geometry/curvature.tex
│       canonical/geometry/biquaternion_curvature.tex
│
├── Stress-energy tensor:                            [L1]
│   T_{μν} = Re(T_{μν}[Θ])
│   └── canonical/geometry/stress_energy.tex
│       canonical/t_munu/
│
└── Review appendix:
    canonical/appendices/appendix_metric_review.tex
```

---

## 5. GR Recovery

**Canonical source**: `canonical/gr_limit/GR_limit_of_UBT.tex`

```
UBT ──→ GR (admissible sector A_UBT)
│
├── Admissibility conditions C1–C6                   [L0 PROVED]
│   └── canonical/gr_limit/GR_limit_of_UBT.tex
│
├── Hilbert variation of S[Θ]:                       [L1]
│   δS/δg^{μν} = 0 → G_{μν} = 8πG T_{μν}
│   └── canonical/gr_limit/GR_limit_of_UBT.tex §3
│
├── Einstein field equations recovered:              [L1 PROVED on A_UBT]
│   R_{μν} - ½g_{μν}R = 8πG T_{μν}
│   └── canonical/gr_limit/GR_limit_of_UBT.tex
│
├── GR closure theorems:                             [L0–L1]
│   └── canonical/gr_closure/
│       ├── step1_metric_bridge.tex
│       ├── step2_nondegeneracy.tex
│       ├── step2_theta_only_closure.tex
│       ├── step3_signature_theorem.tex
│       ├── step4_offshell_Tmunu.tex
│       └── theta_vs_metric_variation_note.tex
│
├── GR as limit:                                     [L1]
│   └── canonical/geometry/gr_as_limit.tex
│
└── Completion appendix:
    canonical/appendices/appendix_GR_completion.tex
```

---

## 6. Standard Model Gauge Structure

**Canonical source**: `canonical/interactions/`, `canonical/su3_derivation/`

```
Θ(q,τ) → SU(3) × SU(2) × U(1)
│
├── U(1)_EM — from ψ-cycle phase:                   [L0 PROVED]
│   Θ → e^{iα} Θ
│   └── canonical/interactions/qed.tex
│
├── SU(2)_L — from left action on ℂ⊗ℍ:             [L0 PROVED]
│   T^a: M ↦ (iσ^a/2) M
│   └── canonical/interactions/sm_gauge.tex
│
├── SU(3)_c — from involutions on ℂ⊗ℍ:             [L0 PROVED]
│   Theorems G.A–G.D (Lie algebra, representations, EW decoupling)
│   └── canonical/su3_derivation/su3_from_involutions.tex
│       canonical/su3_derivation/step3_SU3_result.tex
│
├── QED Lagrangian:                                  [L1 PROVED]
│   L_QED = Tr[(D_μΘ)†(D^μΘ)] - ¼F_{μν}F^{μν}
│   └── canonical/interactions/qed.tex
│
├── QCD Lagrangian:                                  [L1 PROVED]
│   L_QCD = Tr[(D_μΘ)†(D^μΘ)] - ¼G^a_{μν}G^{aμν}
│   └── canonical/interactions/qcd.tex
│
├── SU(2)_L chirality (not SU(2)_R):                [L1 PROVED]
│   └── canonical/chirality/
│       ├── step1_psi_parity.tex
│       ├── step2_chirality_result.tex
│       └── step3_gap_C1_resolution.tex
│
└── Completion appendix:
    canonical/appendices/appendix_SM_completion.tex
```

---

## 7. Fermion Sector

**Canonical source**: `canonical/qm_emergence/`

```
ℂ⊗ℍ → Dirac structure → fermions
│
├── ℂ⊗ℍ ≅ Mat(2,ℂ): Pauli matrices from quaternions  [L0 PROVED]
│   └── canonical/qm_emergence/step3_dirac_emergence.tex §2-3
│
├── Dirac γ^μ from ℂ⊗ℍ ⊗ ℂ⊗ℍ tensor product:       [L0 PROVED]
│   γ^μ in Weyl rep.; Clifford relation verified
│   └── canonical/qm_emergence/step3_dirac_emergence.tex §4
│
├── Dirac-like operator 𝒟 = iγ^μ∇_μ (unique):        [L0 PROVED]
│   └── research_tracks/legacy_theory_variants/ubt/operators/
│       dirac_like_operator.tex Thm. 2.1
│
├── Schrödinger equation emergence:                   [L0 SKETCH]
│   ∂_ψΦ = -2i∇²Φ  from  Im(∂_τΘ = □Θ)
│   └── canonical/qm_emergence/step2_schrodinger_emergence.tex
│
├── Spinorial subspace:                               [L0]
│   └── canonical/qm_emergence/step6_spinorial_subspace.tex
│
├── Born rule emergence:                              [L0]
│   └── canonical/qm_emergence/step7_born_rule.tex
│
├── Three generations from {i,j,k} quaternion units:  [L1 ALGEBRAIC]
│   └── research_tracks/research/generation_structure.tex
│
└── Fermion completion appendix:
    canonical/appendices/appendix_fermions_completion.tex
```

---

## 8. Fine Structure Constant α

**Canonical source**: `docs/STATUS_ALPHA.md`
**Topic index**: `canonical/THEORY/topic_indexes/alpha_index.md`

```
α ≈ 1/137.036  geometric derivation pipeline
│
├── Complex time compactification:                   [L0 PROVED]
│   R_ψ = ℏ/(m_e c)  (calibrated; full derivation open)
│
├── Dirac quantisation on ψ-circle:                  [L0 PROVED]
│   Single-valuedness → discrete winding modes n
│
├── N_eff = 12 from ℂ⊗ℍ algebra:                   [L0 PROVED]
│   N_phases=3 × N_helicity=2 × N_charge=2
│   └── canonical/n_eff/
│
├── B₀ = 8π (one-loop baseline):                    [L1 PROVED]
│   B₀ = 2π·N_eff/3
│   └── canonical/n_eff/step2_vacuum_polarization.tex
│
├── B_base = N_eff^{3/2} ≈ 41.57:                   [L1 PARTIAL]
│   Exponent 3/2 from T³ heat kernel [L0], N_eff=12 [L1]
│   └── canonical/interactions/B_base_derivation_complete.tex
│
├── Toroidal lattice model and discrete modes:       [L1 CONJECTURE]
│   α⁻¹ = 137 + δ  (bare + correction)
│   └── canonical/appendices/appendix_alpha_geometry.tex
│
├── V_eff(n) minimum at prime n*=137:                [L1 PROVED]
│   └── docs/STATUS_ALPHA.md §3-4
│
└── Remaining gaps:
    G3-k  (Kac-Moody level k from S[Θ])    [OPEN]
    R ≈ 1.114 correction factor             [OPEN HARD PROBLEM]
```

---

## 9. Theta Spectral Framework

**Canonical source**: `canonical/UBT_canonical_main.tex §10`

```
Θ-field spectral decomposition
│
├── Toroidal topology T³ × S¹ (ψ-circle):           [L0]
│   └── canonical/geometry/Rpsi_dynamical_fix.tex
│
├── Jacobi theta functions ϑ₃(τ):                   [L0]
│   Ẑ_T³(τ) = ϑ₃³(τ) (modular weight k=3/2)
│   └── research_tracks/research/partition_function_modular.md
│
├── Poisson summation duality:                       [L0 PROVED]
│   W(τ) = τ^{d/2} · S(τ)  (d=3)
│   └── ubt_with_chronofactor/scripts/spectral/poisson_duality_demo.py
│
└── Spectral framework appendix:
    canonical/appendices/appendix_theta_spectrum.tex
```

---

## 10. Experimental Predictions

**Canonical source**: `docs/`, `canonical/qed_phi_const/`

```
Observable predictions from UBT
│
├── Fine structure constant: α ≈ 1/137.036          [SEMI-EMPIRICAL]
├── Schwinger magnetic moment: a_e = α/(2π)          [L1 PROVED]
│   └── canonical/qed_phi_const/step4_schwinger_term.tex
├── U(1) protection → no photon mass                [L0 PROVED]
│   └── canonical/qed_phi_const/step1_u1_protection.tex
├── β-function QED (one-loop):                       [L1 PROVED]
│   └── canonical/qed_phi_const/step3_beta_function.tex
├── Lepton mass ratios (Hecke structure p=137):      [NUMERICAL SUPPORT]
│   └── docs/reports/hecke_lepton/
├── Hubble tension (metric latency mechanism):        [SPECULATIVE]
│   └── speculative_extensions/appendices/
│       appendix_HT_hubble_tension_metric_latency.tex
│
└── Predictions appendix:
    canonical/appendices/appendix_predictions.tex
```

---

## Derivation Dependency Graph

```
ℂ⊗ℍ  (algebra foundation)
    │
    ├──► Θ(q,τ) definition
    │        │
    │        ├──► Action S[Θ]  ──► field equations ∇†∇Θ = κT
    │        │
    │        ├──► G_{μν} = Tr(∂Θ ∂Θ†)  ──► g_{μν} = Re(G_{μν})
    │        │                                    │
    │        │                                    └──► Γ, R, G_{μν} → GR limit
    │        │
    │        ├──► internal phase → SU(3) × SU(2) × U(1)
    │        │
    │        ├──► ψ-winding modes → N_eff=12 → α pipeline
    │        │
    │        └──► ℂ⊗ℍ ≅ Mat(2,ℂ) → γ^μ matrices → Dirac equation
    │
    └──► T_B = t + iψ + jχ + kξ (complex time structure)
```

---

## Open Problems (Priority Order)

| # | Problem | Status | Key File |
|---|---------|--------|---------|
| 1 | Derive R_ψ in physical units from S[Θ] | Open Hard Problem | `docs/PROOFKIT_ALPHA.md` |
| 2 | Close Gap G3-k: Kac-Moody level k=1 | Open | `DERIVATION_INDEX.md §α` |
| 3 | Lepton mass ratios m_μ/m_e, m_τ/m_μ | Open Hard Problem | `DERIVATION_INDEX.md §fermions` |
| 4 | Weinberg angle sin²θ_W from ℂ⊗ℍ | Semi-empirical | `DERIVATION_INDEX.md §SM` |
| 5 | Color confinement (mass gap) | Clay Millennium | `canonical/su3_derivation/` |
| 6 | Massive Dirac equation from S[Θ] | Sketch | `canonical/qm_emergence/step3` |
| 7 | Two-loop R-factor ΔB ≈ 4.74 | Motivated Conjecture | `research_tracks/research/r_factor_two_loop.tex` |

---

## File Index by Topic

| Topic | Primary Canonical File | Review Appendix |
|-------|----------------------|-----------------|
| Action principle | `canonical/THEORY/canonical/canonical_action.tex` | `canonical/appendices/appendix_ACTION_review.tex` |
| Metric / geometry | `canonical/geometry/metric.tex` | `canonical/appendices/appendix_metric_review.tex` |
| GR recovery | `canonical/gr_limit/GR_limit_of_UBT.tex` | `canonical/appendices/appendix_GR_completion.tex` |
| SM gauge structure | `canonical/interactions/sm_gauge.tex` | `canonical/appendices/appendix_SM_completion.tex` |
| Fermion sector | `canonical/qm_emergence/step3_dirac_emergence.tex` | `canonical/appendices/appendix_fermions_completion.tex` |
| Fine structure α | `docs/STATUS_ALPHA.md` | `canonical/appendices/appendix_alpha_geometry.tex` |
| Theta spectrum | `canonical/UBT_canonical_main.tex §10` | `canonical/appendices/appendix_theta_spectrum.tex` |
| Predictions | `canonical/qed_phi_const/step6_qed_summary.tex` | `canonical/appendices/appendix_predictions.tex` |
| Symbol dictionary | `canonical/appendices/symbol_dictionary.tex` | — |
| Derivation status | `DERIVATION_INDEX.md` | — |

---

*Last updated: 2026-03-15. See `DERIVATION_INDEX.md` for full proof-status and gap inventory.*
