# UBT Theory Status Overview

**Purpose**: Clear separation of solved results, partially solved claims,
and open research problems.  
**Date**: 2026-03-10  
**Based on**: `AUDITS/copilot_repo_verification_and_gap_report.md` and
`AUDITS/claim_evidence_matrix.md`

Proof-level labels:
- **[L0]** — exact algebraic/geometric identity, no free parameters
- **[L1]** — proved given verified assumptions
- **[L2]** — requires additional lemmas not yet proved
- **[SE]** — semi-empirical: formula correct but one parameter not fully derived
- **[P]** — partially present: framework exists, derivation incomplete
- **[O]** — open problem: no complete derivation in repository

---

## 1. Solved Results

These claims have complete, referee-readable derivations in the repository.

### 1.1 Algebra and Structure

| Result | Proof Level | Primary Source |
|--------|------------|----------------|
| ℂ⊗ℍ ≅ Mat(2,ℂ) algebraic identity | **[L0]** | `canonical/algebra/involutions_Z2xZ2xZ2.tex` |
| Z₂³ grading of biquaternion algebra | **[L0]** | `canonical/algebra/involutions_Z2xZ2xZ2.tex` |
| SU(3)_c from ℂ⊗ℍ involutions | **[L0]** | `canonical/interactions/sm_gauge.tex` Th.G.A–G.D |
| SU(2)_L from norm-preserving left action | **[L0]** | `canonical/interactions/sm_gauge.tex` §2 |
| U(1)_Y from scalar phase right action | **[L0]** | `canonical/interactions/sm_gauge.tex` §3 |
| Three generations from ψ-winding modes | **[L0]** | `canonical/interactions/sm_gauge.tex` §4 |

### 1.2 Geometry and GR Recovery

| Result | Proof Level | Primary Source |
|--------|------------|----------------|
| Metric emergence: Θ → g_μν (Step 1) | **[L1]** | `canonical/geometry/metric.tex`; `step1_metric_bridge.tex` |
| Equivalence of derivative and tetrad definitions | **[L0]** | `consolidation_project/GR_closure/step1_metric_bridge.tex` |
| Non-degeneracy of g_μν (Step 2) | **[L0]** | `consolidation_project/GR_closure/step2_nondegeneracy.tex` |
| Lorentzian signature (Step 3) | **[L0]** | `consolidation_project/GR_closure/step3_signature_theorem.tex` |
| Riemann curvature from metric (Step 4) | Standard | `canonical/geometry/curvature.tex` |
| Einstein field equations (Step 5) | **[L1]** | `canonical/geometry/gr_as_limit.tex`; `GR_chain_summary.tex` |
| T_μν derived (not postulated) | **[L1]** | `canonical/geometry/stress_energy.tex`; `step4_offshell_Tmunu.tex` |
| GR at any constant phase φ | **[L1]** | `canonical/geometry/gr_as_limit.tex` |
| Phase frame bundle, U(1) symmetry | **[L0]** | `canonical/geometry/phase_projection.tex` |

### 1.3 Electromagnetism and Maxwell Equations

| Result | Proof Level | Primary Source |
|--------|------------|----------------|
| U(1) gauge invariance from UBT | **[L1]** | `canonical/interactions/qed.tex` §2 |
| QED Lagrangian | **[L1]** | `canonical/interactions/qed.tex` §1 |
| Massless photon | **[L1]** | `canonical/interactions/qed.tex` §3 |
| Field tensor F_μν | **[L1]** | `canonical/interactions/qed.tex` §2 |
| Homogeneous Maxwell equations (Bianchi) | **[L1]** | `canonical/bridges/Maxwell_limit_bridge.tex` §3 |
| Inhomogeneous Maxwell equations | **[L1]** | `canonical/bridges/Maxwell_limit_bridge.tex` §4 |
| Covariant Maxwell in curved spacetime | **[L1]** | `canonical/interactions/qed.tex` §6 |
| Charge conservation ∂_μj^μ = 0 | **[L1]** | `canonical/interactions/qed.tex` §4 |
| Biquaternionic form F = (E+iB)·σ | **[L1]** | `appendix_C_electromagnetism_gauge_consolidated.tex` |
| B₀ = 8π (bare coupling) | **[L1]** | `canonical/interactions/qed.tex` §4 |

### 1.4 Fine Structure Constant (Structural Part)

| Result | Proof Level | Primary Source |
|--------|------------|----------------|
| α formula structure: α = B₀/(B_base + B_α) | **[L1]** | `canonical/interactions/qed.tex` §5 |
| B₀ = 8π derivation | **[L1]** | `canonical/interactions/qed.tex` §4 |

---

## 2. Partially Solved Results

These have a complete framework but at least one open parameter or step.

### 2.1 Fine Structure Constant (Numerical)

| Claim | Status | Gap | Source |
|-------|--------|-----|--------|
| B_α ≈ 46.3 (running correction) | **[SE]** | Depends on open B_base | `appendix_ALPHA_one_loop_biquat.tex` |
| B_base ≈ 41.57 numerical value | **[P]** | Exponent 3/2 not derived | `appendix_ALPHA_padic_derivation.tex` |
| N_eff = 11.53 from BRST | **[L2]** | Spectral uniqueness not proved | `THEORY/axioms/core_assumptions.tex` A1–A3 |
| R ≈ 1.114 geometric factor | **[P]** | Geometric origin unknown | *(8 approaches tested)* |

**Summary**: The formula α ≈ 1/137.036 is reproduced numerically but one
parameter (B_base exponent = 3/2) is not derived from first principles.
22 approaches have been tested without complete success.

### 2.2 Fermion Masses

| Claim | Status | Gap | Source |
|-------|--------|-----|--------|
| Electron mass m_e ≈ 0.511 MeV (0.22% accuracy) | **[SE]** | Parameters fitted, not derived | `consolidation_project/electron_mass/` |
| Fermion mass formula | **[SE]** | Fitted to data | `unified_biquaternion_theory/fermion_mass_derivation_complete.tex` |
| Quark masses | **[P]** | Partial only | `consolidation_project/appendix_QA2_quarks_CKM.tex` |

**Summary**: The mass formula reproduces known values with good accuracy
but the parameters are fitted to data rather than derived from first principles.

### 2.3 Gauge Sector

| Claim | Status | Gap | Source |
|-------|--------|-----|--------|
| Weinberg angle θ_W ≈ 0.23122 | **[SE]** | Cannot be fixed by ℂ⊗ℍ alone | `canonical/interactions/sm_gauge.tex` §5 |
| Chirality (why SU(2)_L not SU(2)_R) | **[L2]** | Motivated by ψ-parity, not proved | `consolidation_project/chirality_derivation/` |
| Color confinement | **[L2]** | Conjectured, no proof | `consolidation_project/confinement/` |

### 2.4 Fermion Sector (Dirac)

| Claim | Status | Gap | Source |
|-------|--------|-----|--------|
| Dirac equation from UBT | **[P]** | Follows standard QFT; biquaternionic derivation partial | `canonical/interactions/qed.tex` §4 |

### 2.5 Cosmology

| Claim | Status | Gap | Source |
|-------|--------|-----|--------|
| Dark matter Hopfion model | **[L2]** | Conjectured, not proved | `solution_P5_dark_matter/` |
| Dark energy from imaginary curvature | **[P]** | Framework present | `solution_P6_dark_energy/` |
| CMB TT-spectrum prediction | **[P]** | NULL result vs Planck data (noted) | `appendix_W_testable_predictions.tex` |
| N_eff cosmological prediction | **[P]** | Partial only | `consolidation_project/N_eff_derivation/` |

---

## 3. Open Research Problems

These require new theoretical work. They are clearly labelled as open
throughout the repository and are not claimed as solved.

### 3.1 Critical Open Problems

| Problem | Description | Approaches Tried | Source |
|---------|-------------|-----------------|--------|
| **B_base exponent** | Derive why N_eff^(3/2) with exponent 3/2 | 22 approaches, none complete | `canonical/bridges/QED_limit_bridge.tex` §3 |
| **R ≈ 1.114 factor** | Derive geometric origin of radiative correction R | 8 approaches, none complete | `canonical/bridges/QED_limit_bridge.tex` §3 |
| **Off-shell Θ-only GR closure** (Step 6) | Derive Einstein eq. purely from Θ with no matter source | Structural obstruction found | `canonical/geometry/gr_completion_attempt.tex` |
| **Fermion mass ratios** | Derive m_μ/m_e and m_τ/m_μ from first principles | Fitted parameters | `consolidation_project/masses/` |
| **CKM matrix elements** | Derive mixing angles from biquaternion algebra | Partial only | `consolidation_project/appendix_QA2_quarks_CKM.tex` |

### 3.2 Missing Physics

| Missing Element | Description | Status |
|----------------|-------------|--------|
| S-matrix / perturbative QFT dynamics | Scattering amplitudes, Feynman rules | ABSENT — no file found |
| Renormalization group in UBT framework | RGE equations from UBT first principles | PARTIAL |
| Neutrino masses and mixing | PMNS matrix from UBT | PARTIAL |
| Baryon asymmetry | CP violation from ψ-sector | SPECULATIVE |

### 3.3 Speculative Extensions (Not Part of Core Theory)

These are maintained in `speculative_extensions/` and are explicitly labelled
as speculative — not part of the verified UBT framework:

- **Consciousness (psychons)**: `speculative_extensions/complex_consciousness/`
- **Closed Timelike Curves**: `speculative_extensions/appendices/`
- **Multiverse structure**: `speculative_extensions/appendices/`
- **Riemann Hypothesis connection**: `research/rh_biquaternion_extension/`

---

## 4. Overall Assessment

| Category | Count | Notes |
|----------|-------|-------|
| Fully proved [L0/L1] results | ~20 | Algebra, GR chain, Maxwell, U(1) |
| Semi-empirical [SE] results | ~5 | α, m_e, θ_W — formula correct, one parameter open |
| Partially present [P] results | ~8 | Framework exists, derivation incomplete |
| Open problems [O] | ~5 | Critical gaps: B_base, R, off-shell closure |
| Absent | 1 | S-matrix/perturbative QFT |
| Speculative | ~5 | Maintained separately |

**Overall quality**: The core theory (GR recovery, Maxwell limit, gauge groups)
is at publication quality. The fine structure constant and fermion mass programs
are scientifically valuable despite open parameters. Open problems are clearly
labelled and not claimed as solved.

---

## 5. Reading Path for External Referee

1. Start: `THEORY/README.md` — overview and disclaimers
2. Core: `THEORY/canonical/canonical_axioms.tex` — foundations
3. GR: `canonical/bridges/GR_chain_bridge.tex` — GR recovery
4. EM: `canonical/bridges/Maxwell_limit_bridge.tex` + `QED_limit_bridge.tex`
5. Gauge: `canonical/bridges/gauge_emergence_bridge.tex`
6. Status: `AUDITS/claim_evidence_matrix.md` — full evidence matrix
7. Full audit: `AUDITS/copilot_repo_verification_and_gap_report.md`

---

*See `THEORY/theory_navigation_map.md` for file locations of all derivations.*
