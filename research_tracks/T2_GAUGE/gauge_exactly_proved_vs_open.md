<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# T2_GAUGE — Exactly Proved vs Open: Complete Proof-Gap Map

**Track**: T2_GAUGE — Standard Model Gauge Structure  
**Purpose**: Definitive, claim-linked inventory of every gauge-sector statement,
classified strictly as PROVED, SEMI-EMPIRICAL, MOTIVATED (gap identified), or OPEN.  
**Date**: 2026-04-28  
**Sources**: `gauge_derivation_map.md`, `su3_proof_status.md`, `missing_axioms.md`,
`canonical/interactions/sm_gauge.tex`, `canonical/algebra/involutions_Z2xZ2xZ2.tex`,
`canonical/su3_derivation/`, `canonical/chirality/`, `DERIVATION_INDEX.md`

---

## Legend

| Tag | Meaning |
|-----|---------|
| **[L0]** | Algebraic identity — follows from the definition of ℂ⊗ℍ alone |
| **[L1]** | Proved theorem — requires axioms A, B, F plus standard mathematics |
| **[SE]** | Semi-empirical — value or structure fixed by experiment |
| **[MC]** | Motivated conjecture — physically/algebraically motivated, not proved |
| **[OPEN]** | Open — no proof exists; no obstruction fully characterised |
| **[OPEN-HRD]** | Open hard — resisted many approaches; requires new mathematics |

---

## 1. Algebraic Foundation

| Claim | Status | Source | Notes |
|-------|--------|--------|-------|
| ℂ⊗ℍ ≅ Mat(2,ℂ) | **[L0] PROVED** | `canonical/fields/biquaternion_algebra.tex` | Exact algebraic identity |
| ℂ⊗ℍ ≅ Cl₁,₃(ℝ) | **[L0] PROVED** | `canonical/fields/biquaternion_algebra.tex` | Clifford identification |
| dim_ℝ(ℂ⊗ℍ) = 8 | **[L0] PROVED** | Definition | |
| Frobenius inner product on Mat(2,ℂ) | **[L0] PROVED** | Standard linear algebra | |

---

## 2. SU(3)_c — Strong Gauge Sector

| Claim | Status | Source | Notes |
|-------|--------|--------|-------|
| 𝔰𝔲(3) realised in ℂ⊗ℍ (Theorem G.A) | **[L0] PROVED** | `canonical/su3_derivation/su3_from_involutions.tex` | Via ℤ₂×ℤ₂×ℤ₂ involutions |
| Quarks transform in fundamental **3** (Theorem G.B) | **[L0] PROVED** | `canonical/interactions/sm_gauge.tex §G.B` | ψ-winding modes |
| Gluons transform in adjoint **8** (Theorem G.C) | **[L0] PROVED** | `canonical/interactions/sm_gauge.tex §G.C` | Verified numerically |
| 8 Gell-Mann generators numerically verified | **[L0] PROVED** | `canonical/su3_derivation/step3_SU3_result.tex` | fᵢⱼₖ correct |
| EW/strong sector decoupling (Theorem G.D) | **[L0] PROVED** | `canonical/interactions/sm_gauge.tex §G.D` | Orthogonal subspaces |
| Independent qubit-encoding derivation of SU(3) | **[L0] PROVED** | `canonical/interactions/su3_qubit_encoding.tex` | Independent confirmation |
| Equivalence of involution and qubit routes | **[L0] PROVED** | `canonical/bridges/su3_gauge_qubit_equivalence.tex` | |
| Structural colour confinement (free quarks inadmissible) | **[L0]+exp PROVED** | `su3_proof_status.md §confinement` | Algebraic; exp. support via LHCb |
| Dynamical confinement (area law / mass gap) | **[OPEN-HRD]** | `su3_proof_status.md §OP-SU3-1` | Millennium Prize level |
| Strong coupling g_s from first principles | **[OPEN]** | `su3_proof_status.md §OP-SU3-1` | Not derived |
| CP violation / strong θ_QCD parameter | **[OPEN]** | `su3_proof_status.md §OP-SU3-3` | Complex-time sector may help |
| Quark-hadron duality / meson-baryon spectrum | **[OPEN]** | `su3_proof_status.md §OP-SU3-2` | |

---

## 3. SU(2)_L — Weak Isospin

| Claim | Status | Source | Notes |
|-------|--------|--------|-------|
| SU(2)_L from left norm-preserving action on Mat(2,ℂ) | **[L0] PROVED** | `canonical/interactions/sm_gauge.tex §SU2` | Exact algebraic fact |
| 𝔰𝔲(2)_L generators = σ^i/2 embedded in ℂ⊗ℍ | **[L0] PROVED** | Standard embedding | |
| SU(2)_L acts on left-chiral doublets | **[L0] PROVED** | `canonical/interactions/sm_gauge.tex` | From Mat(2,ℂ) left action |
| Weak bosons W±, W³ as gauge connections | **[L1] PROVED** | Gauge principle applied to SU(2)_L | |
| **Chirality: SU(2)_L not SU(2)_R** | **[MC] MOTIVATED** | `canonical/chirality/step3_gap_C1_resolution.tex` | ψ-parity argument; Gap C1 |
| W± and Z mass from SSB | **[OPEN]** | `research_tracks/research/higgs_yukawa_scan.md` | Higgs sector open |

---

## 4. U(1)_Y — Hypercharge

| Claim | Status | Source | Notes |
|-------|--------|--------|-------|
| U(1)_Y from right scalar phase action on Mat(2,ℂ) | **[L0] PROVED** | `canonical/interactions/sm_gauge.tex §U1` | Exact algebraic fact |
| U(1)_Y generator = (1/2)I in fundamental | **[L0] PROVED** | Representation theory | |
| Hypercharge quantisation from Dirac condition | **[L0] PROVED** | `canonical/appendices/appendix_alpha_geometry.tex §1` | ψ-circle winding |

---

## 5. Electroweak Mixing and Photon

| Claim | Status | Source | Notes |
|-------|--------|--------|-------|
| U(1)_EM from ψ-cycle phase after SSB | **[L0] PROVED** | `DERIVATION_INDEX.md` | Q = T₃ + Y/2 |
| Photon field A_μ = sin θ_W W³ + cos θ_W B_μ | **[L1] PROVED** | Standard electroweak algebra | Follows from unbroken generator |
| Weinberg angle θ_W — **value** sin²θ_W ≈ 0.231 | **[SE] SEMI-EMPIRICAL** | `canonical/interactions/sm_gauge.tex` | Gap EW-1; see EW derivation plan |
| tan θ_W = g'/g from UBT algebra | **[OPEN]** | `canonical/alpha/gauge_normalization_attempt.tex` | Gap EW-1 |
| sin²θ_W = 3/8 from GUT boundary (if embedded) | **[MC] MOTIVATED** | New — see `canonical/alpha/weinberg_angle_derivation.md` | EW2 workstream |

---

## 6. Three Generations

| Claim | Status | Source | Notes |
|-------|--------|--------|-------|
| N_gen = 3 from dim_ℝ(Im ℍ) = 3 | **[L0] PROVED** | `DERIVATION_INDEX.md §ψ-modes` | |
| Three ψ-winding modes carry identical gauge quantum numbers | **[L0] PROVED** | `su3_proof_status.md §Three generations` | |
| Mass hierarchy between generations | **[OPEN-HRD]** | `PRIORITIES_2026.md §Bottlenecks` | KK mismatch theorem blocks simple formula |

---

## 7. Higgs Sector and Symmetry Breaking

| Claim | Status | Source | Notes |
|-------|--------|--------|-------|
| SSB pattern SU(2)_L × U(1)_Y → U(1)_EM exists | **[MC] MOTIVATED** | `canonical/symmetry/step3_breaking_catalogue.tex` | Radiative Hosotani mechanism candidate |
| Higgs boson from UBT Θ-field VEV | **[OPEN]** | `research_tracks/research/higgs_yukawa_scan.md` | |
| Quartic Higgs coupling λ | **[OPEN]** | `DERIVATION_INDEX.md §λ-gap` | Off by ×11 vs SM |
| Higgs mass m_H ≈ 125 GeV | **[OPEN]** | — | |

---

## 8. Yukawa and Fermion Masses

| Claim | Status | Source | Notes |
|-------|--------|--------|-------|
| Yukawa coupling matrix y_ij | **[OPEN]** | `research_tracks/research/higgs_yukawa_scan.md` | |
| Fermion mass spectrum (e, μ, τ, quarks) | **[OPEN-HRD]** | `PRIORITIES_2026.md §Bottlenecks` | KK mismatch theorem |

---

## 9. Anomaly Cancellation

See `anomaly_checklist.md` for detailed per-anomaly assessment.

| Claim | Status | Notes |
|-------|--------|-------|
| U(1)_Y³ anomaly cancelled (SM result) | **[MC] MOTIVATED** | Follows from SM fermion reps if assumed |
| U(1)_Y [SU(2)_L]² anomaly cancelled (SM result) | **[MC] MOTIVATED** | Follows from SM fermion reps if assumed |
| [Gravity]² U(1)_Y anomaly cancelled (SM result) | **[MC] MOTIVATED** | |
| Anomaly cancellation from UBT first principles | **[OPEN]** | Requires deriving fermion representations from UBT |
| Green-Schwarz mechanism alternative | **[OPEN]** | Not investigated |

---

## 10. Gauge Sector Paper Readiness

### Statements that can be made in a journal paper without further work

**Zero-free-parameter results [L0]:**
1. ℂ⊗ℍ ≅ Mat(2,ℂ) — the algebraic foundation
2. 𝔰𝔲(3) realised in ℂ⊗ℍ (Theorems G.A–G.D) — four theorems
3. Quarks in **3**, gluons in **8** — confirmed numerically
4. SU(2)_L from left norm-preserving action
5. U(1)_Y from right scalar phase action
6. U(1)_EM from ψ-cycle phase
7. Three generations from dim_ℝ(Im ℍ) = 3
8. Structural colour confinement

**To be stated as open or semi-empirical:**
- Chirality (SU(2)_L not SU(2)_R): motivated, Gap C1
- Weinberg angle θ_W: semi-empirical; Gap EW-1 (new priority — see `weinberg_angle_derivation.md`)
- Higgs mechanism / gauge boson masses: open
- Fermion masses: open hard
- g_s, α_s running: open

### Impact statement

No other published framework derives all three Standard Model gauge factors from a
**single 8-dimensional real algebra** without introducing the gauge group as external
input.  The SU(3)×SU(2)×U(1) structure, three generations, structural confinement,
and charge quantisation all emerge from zero free parameters within ℂ⊗ℍ.

---

## 11. Gap Registry

| Gap | Description | Paper impact | Priority |
|-----|-------------|--------------|----------|
| C1 | Chirality (SU(2)_L not SU(2)_R) formal theorem | MEDIUM — motivated only | HIGH |
| EW-1 | tan θ_W = g'/g from UBT algebra | HIGH — core of new task | **CRITICAL** |
| EW-2 | Θ₀ VEV as SU(2)_L doublet from S[Θ] | MEDIUM | HIGH |
| GUT-UBT | ℂ⊗ℍ embedding into SU(5)/SO(10) for sin²θ_W = 3/8 | MEDIUM | HIGH |
| SU3-g_s | Strong coupling g_s from first principles | MEDIUM — standard limitation | MEDIUM |
| H-λ | Higgs quartic coupling (off by ×11) | LOW | LOW |
| Y1 | Fermion mass spectrum | LOW for gauge paper | LOW |
