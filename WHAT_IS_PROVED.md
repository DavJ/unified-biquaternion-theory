<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# WHAT_IS_PROVED.md — Definitive Map of Proved Results

**Author**: Ing. David Jaroš  
**Date**: 2026-05-13  
**Purpose**: Authoritative list of what UBT has proved, at what level,
and where the proof lives.  Every claim here is backed by a source file.
If it is not on this list, it is not claimed as proved.

---

## Proof Level Key

| Level | Meaning |
|-------|---------|
| **[L0]** | Algebraic identity — follows from the definition of ℂ⊗ℍ alone |
| **[L1]** | Formal theorem — requires axioms A1–A3 and standard mathematics |
| **[NUM]** | Numerically verified (reproducible script) |
| **[STD]** | Standard mathematics or physics result; not novel |

---

## Track T1_GR: General Relativity Recovery

All proofs in `canonical/gr_closure/` and `canonical/geometry/`.  
Comprehensive paper: `papers/UBT_GR_Submission.tex`.

### Core Chain (ψ → g → Γ → R → G = 8πGT)

| # | Claim | Level | Source |
|---|-------|-------|--------|
| G1 | The metric $g_{\mu\nu} = \mathrm{Re}[\mathrm{Tr}(\partial_\mu\Theta \cdot \partial_\nu\Theta^\dagger)]/\mathcal{N}$ is a symmetric covariant (0,2) tensor | [L1] | `step1_metric_bridge.tex` |
| G2 | $\det(g_{\mu\nu}) \neq 0$ for admissible Θ (Theorem 3.2) | [L1] | `step2_nondegeneracy.tex` |
| G3 | Lorentzian signature $(-,+,+,+)$ is a theorem from AXIOM-B alone | [L1] | `step3_signature_theorem.tex` |
| G4 | Levi-Civita connection, curvature tensors — standard GR | [STD] | Wald 1984 |
| G5 | Einstein field equations $G_{\mu\nu} = 8\pi G\,T_{\mu\nu}$ from Hilbert variation | [L1] | `step3_einstein_with_matter.tex` |
| G6 | Stress-energy tensor $T_{\mu\nu}$ is symmetric | [L1] | `canonical/geometry/stress_energy.tex` |
| G7 | Conservation $\nabla^\mu T_{\mu\nu} = 0$ | [L1] | `canonical/geometry/stress_energy.tex` |

### Schwarzschild Sector

| # | Claim | Level | Source |
|---|-------|-------|--------|
| G8 | Schwarzschild metric in isotropic coords from spherically symmetric $\Theta_0$ ansatz | [L1] | `biquaternionic_vacuum_solutions.tex §3` |
| G9 | Spatial components $g_{ij} = \Psi^4 \delta_{ij}$ verified to $< 10^{-15}$ relative error | [NUM] | `tools/verify_schwarzschild_theta.py` |
| G10 | Temporal component $g_{tt} = -\Phi^2$ from complex-time ψ-structure | [L1] | Paper §4, tcolorbox |
| G11 | ASD Weyl condition $C^+ = 0$ for $\mathrm{SU}(2)_-$ sector | [L1] | `asd_condition_ubt.tex §5` |
| G12 | Curved twistor space exists for ASD sector (Penrose nonlinear graviton) | [L1]+[STD] | Penrose 1976 |

### Linearised Gravity

| # | Claim | Level | Source |
|---|-------|-------|--------|
| G13 | Linearised UBT field equation reproduces linearised Einstein equations | [L1] | Linearisation of G5 |
| G14 | Regge-Wheeler equation (odd-parity graviton) derived without extra input | [L1] | `papers/UBT_GR_Submission.tex §5` |
| G15 | Zerilli equation (even-parity graviton) derived from linearised UBT (vacuum Schwarzschild, $\ell\ge2$) | [L1] | `canonical/gr_closure/zerilli_derivation.tex` |

### Explicitly Open (not claimed as proved)

| Gap | Description |
|-----|-------------|
| GAP-10 | Off-shell Θ-only closure (global ker J = gauge only) |
| GAP-C | FRW/de Sitter Θ ansatz |

---

## Track T2_GAUGE: Standard Model Gauge Structure

All proofs in `canonical/interactions/`, `canonical/su3_derivation/`,
`canonical/chirality/`.  Source map: `reports/gauge_truth_matrix.md`.

### Algebraic Foundation

| # | Claim | Level | Source |
|---|-------|-------|--------|
| A1 | ℂ⊗ℍ ≅ Mat(2,ℂ) | [L0] | `biquaternion_algebra.tex` |
| A2 | ℂ⊗ℍ ≅ Cl₁,₃(ℝ) | [L0] | `biquaternion_algebra.tex` |
| A3 | dim_ℝ(ℂ⊗ℍ) = 8 | [L0] | Definition |

### SU(3) Colour

| # | Claim | Level | Source |
|---|-------|-------|--------|
| S1 | 𝔰𝔲(3) realised in ℂ⊗ℍ via ℤ₂×ℤ₂×ℤ₂ involutions | [L0] | `su3_from_involutions.tex` |
| S2 | Quarks in fundamental **3** representation | [L0] | `sm_gauge.tex §G.B` |
| S3 | Gluons in adjoint **8** representation (all 28 commutator pairs) | [L0] | `sm_gauge.tex §G.C` |
| S4 | EW/strong sector algebraic decoupling | [L0] | `sm_gauge.tex §G.D` |
| S5 | Independent triqubit derivation confirms SU(3) | [L0] | `su3_qubit_encoding.tex` |
| S6 | Structural colour confinement: free quarks algebraically inadmissible | [L0] | `su3_from_involutions.tex Thm G.B` |
| S7 | Involution and triqubit routes are equivalent | [L0] | `su3_gauge_qubit_equivalence.tex` |

*Note*: Dynamical confinement (Wilson loop area law) is the Clay Millennium Problem; it is not claimed.

### Electroweak Sector

| # | Claim | Level | Source |
|---|-------|-------|--------|
| E1 | SU(2)_L from left norm-preserving action on Mat(2,ℂ) | [L0] | `sm_gauge.tex §SU2` |
| E2 | SU(2)_L acts on left-chiral doublets (chirality gap C1 closed) | [L1] | `chirality/step3_gap_C1_resolution.tex` |
| E3 | W±, W³ as gauge connections of SU(2)_L | [L1] | Gauge principle |
| E4 | U(1)_Y from right scalar phase action on Mat(2,ℂ) | [L0] | `sm_gauge.tex §U1` |
| E5 | Hypercharge quantisation from Dirac condition on ψ-circle | [L0] | `appendix_alpha_geometry.tex §1` |
| E5b | SU(3) colour-lattice Step 1 ($\mathbf{3}\to Y\in\frac{1}{3}\mathbb{Z}$) isolated as formal target theorem | OPEN / [MC] (blocker explicit) | `canonical/interactions/colour_charge_lattice.tex` |
| E6 | U(1)_EM from ψ-cycle phase after SSB | [L0] | `qed.tex` |
| E7 | Q = T₃ + Y/2 (Gell-Mann–Nishijima relation) | [L1] | Standard EW algebra |
| E8 | Photon field $A_\mu = \sin\theta_W W^3_\mu + \cos\theta_W B_\mu$ | [L1] | Standard EW |

### Three Generations

| # | Claim | Level | Source |
|---|-------|-------|--------|
| T1 | N_gen = 3 from dim_ℝ(Im ℍ) = 3 | [L0] | `DERIVATION_INDEX.md §ψ-modes` |
| T2 | Three ψ-winding modes carry identical gauge quantum numbers | [L0] | `su3_proof_status.md §Three generations` |
| T2b | Higher ψ-modes \(n\ge 4\) are currently best interpreted as heavy KK excitations above the compactification scale; a first-principles proof that only three light generations remain is still OPEN/[MC] | OPEN / [MC] | `research_tracks/EW/higher_harmonics_analysis.tex` |

### QED Sector

| # | Claim | Level | Source |
|---|-------|-------|--------|
| Q1 | Photon is massless in UBT QED sector | [L1] | `canonical/interactions/qed.tex` |
| Q2 | Electron g-factor = 2 at tree level | [L1] | `canonical/interactions/qed.tex` |
| Q3 | QED running coupling α(μ) reproduced | [L1] | `canonical/interactions/qed.tex` |

### Explicitly Open (not claimed as proved)

| Gap | Description |
|-----|-------------|
| EW-1 | Weinberg angle from pure algebra (dead end — stated explicitly) |
| EW-1b | EW1+RG conditional branch ($3/8 \to 0.231$) pending full first-principles $Y_i$ closure from Gap C2 Step 1 |
| EW-2 | Higgs doublet VEV from S[Θ] |
| C2 | Specific fermion hypercharge assignments — conditional: Step 1 (SU(3) colour lattice) OPEN; Step 2 [L1], Step 3 [L0]; uniqueness remains [MC] | `canonical/interactions/hypercharge_assignments.tex`, `canonical/interactions/colour_charge_lattice.tex` |
| Y2 | Yukawa couplings |

---

## Track T3_ALPHA: Fine Structure Constant

Source: `canonical/alpha/`, `reports/alpha_routes_ranked.md`.

| # | Claim | Level | Source |
|---|-------|-------|--------|
| α1 | N_phases = 3 from Im(ℍ) | [L0] | `canonical/n_eff/step2_AUDIT.tex` |
| α1b | N_eff = 12 = 3×2×2 | OPEN / [MC] (under critical audit) | `canonical/n_eff/step2_AUDIT.tex` |
| α1c | N_eff(loop) = 3 from S_kin[Θ] (charged complex scalars) | [L1] | `canonical/n_eff/neff_reconciliation.tex` |
| α1d | B₀(loop) = 2π from S_kin[Θ] (one-loop scalar QED, N_eff=3) | [L1] | `canonical/n_eff/neff_reconciliation.tex` |
| α1e | N_eff(R2)=12 and N_eff(loop)=3 are different quantities; identification is unproved | [MC] OPEN | `canonical/n_eff/neff_reconciliation.tex` |
| α2 | Charge quantisation from Dirac condition on ψ-circle | [L0] | `appendix_alpha_geometry.tex §1` |
| α3 | V_eff winding-mode potential: $V_\mathrm{eff}(n) = n^2 - Bn\ln n$ | [L1] | `canonical/alpha/alpha_best_route.tex` |
| α4 | $n^*(B_\mathrm{phenom}) = 137$ | [L1] (given B) | `canonical/alpha/alpha_best_route.tex` |
| α5 | 137 is prime; prime status implies V_eff stability | [L0]+[STD] | Number theory |
| α6 | One-loop QED running: α(μ₂) from α(μ₁) reproduced | [L1] | `canonical/interactions/qed.tex` |
| α7 | Hecke coincidence for 76a1: $|a_{137}|=g(X_0(137))=11$ is unique in $\{131,137,139\}$ by direct point counting; a₁₃₁=−9, a₁₃₉=−3 [L0] přímý výpočet | [MC] | `research_tracks/T3_ALPHA/hecke_alpha_connection.tex`, `reports/hecke_eigenvalue_twin_prime_test.md` |
| α8 | $\vartheta_3(0\|i)/\eta(i) = \sqrt{2}$ [Ramanujan + $\Gamma$-doplňkový vzorec] | [STD] | `research_tracks/T3_ALPHA/rogers_ramanujan_c3_connection.tex` |
| α9 | $B = 12^{3/2}\cdot 2^{1/8}\cdot\vartheta_3(0\|i)^{1/4} = 46.281$, err $0.0066\%$ | [OBS] | `research_tracks/T3_ALPHA/rogers_ramanujan_c3_connection.tex` |
| α10 | $a_2(D_{\mathrm{UBT}})$ reprodukuje Einstein-Hilbertovu akci | [Prop.] | `research_tracks/T3_ALPHA/seeley_dewitt_coefficients.tex` |
| α11 | $a_4 \propto \vartheta_3(0\|i)$ conjecture | [MC/OPEN] | `research_tracks/T3_ALPHA/seeley_dewitt_b_bridge.tex` |

### Rogers-Ramanujan Algebraic Identities (2026-05-11)

| # | Claim | Level | Source |
|---|-------|-------|--------|
| α18 | $\vartheta_3(0\|i) = \pi^{1/4}/\Gamma(3/4)$ (Ramanujan CM value at $\tau=i$) | [STD] | Berndt, *Ramanujan's Notebooks*, Part III, Ch. 17 |
| α19 | $\eta(i) = \Gamma(1/4)/(2\pi^{3/4})$ | [STD] | classical |
| α20 | $\vartheta_3(0\|i)/\eta(i) = \sqrt{2}$ — exact algebraic identity via Gamma reflection formula $\Gamma(1/4)\Gamma(3/4)=\pi\sqrt{2}$ | [L0]/[STD] | `research_tracks/T3_ALPHA/rogers_ramanujan_c3_connection.tex` |
| α21 | $Z_{c=3}(\tau=i) = [\vartheta_3(0\|i)/\eta(i)]^3 = 2\sqrt{2}$ — three free compact bosons at self-dual torus | [STD] | `research_tracks/T3_ALPHA/rogers_ramanujan_c3_connection.tex` |
| α22 | Algebraic rewriting [OBS]: $B_{\mathrm{cand}} = 12^{3/2}\cdot 2^{1/8}\cdot\vartheta_3(0\|i)^{1/4} \approx 46.281$ — numerical accuracy $0.0066\%$; **not a first-principles derivation** | [OBS] | `research_tracks/T3_ALPHA/rogers_ramanujan_c3_connection.tex` |
| α23 | $Z_{\mathrm{wind}}(\tau=i) = \vartheta_3(0\|i)$ — winding partition function at self-dual point | [STD] | `research_tracks/quantum_ubt/ncg_poisson_b0derivation.tex` |

The algebraic rewriting sharpens Gap G137-B: it makes explicit that the three
factors in the candidate $B$-formula have different physical origins (algebraic
structure, self-dual normalisation, winding partition function) and must each
be derived from $S[\Theta]$ separately.

### Explicitly Open

| Gap | Description |
|-----|-------------|
| G137-B | Derive $B = N_{\mathrm{eff}}^{3/2}\cdot 2^{1/8}\cdot Z_{\mathrm{wind}}(1)^{1/4}$ from $S[\Theta]$ without α/137/B_required input; all three factors must be derived; alpha status is STRUCTURAL / CONDITIONAL / OPEN GAP. Sharpened statement: `canonical/alpha/alpha_gap_closure_matrix.tex` |

**Single canonical reference for T3_ALPHA chain status**: `canonical/alpha/alpha_gap_closure_matrix.tex`

| # | Claim | Level | Source |
|---|-------|-------|--------|
| alpha_matrix | Gap closure matrix for T3_ALPHA | [canonical] | `canonical/alpha/alpha_gap_closure_matrix.tex` |

---

## Miscellaneous Proved Results

| # | Claim | Level | Source |
|---|-------|-------|--------|
| M1 | N_eff = 12 from ℂ⊗ℍ (full 3×2×2 factorization) | OPEN / [MC] (critical audit pending) | `canonical/n_eff/step2_AUDIT.tex` |
| M2 | B₀ = 8π from S_kin[Θ] (one-loop) | [L1] | `canonical/t_munu/` |
| M3 | FPE equivalent formulation (scalar sector) | [L1] | `research_tracks/` |
| M4 | ΔN_eff ≈ 0.046 (above CMB-S4 threshold) | [L1] | `consolidation_project/N_eff_derivation/` |
| Q1 | Kanonická kvantizace gravitonů (Zerilli+RW módy) | [STD] | `research_tracks/quantum_ubt/graviton_quantisation.tex` |

---

## What Is NOT Claimed as Proved

The following are open problems, dead ends, or out-of-scope items.
They are **not** in the above list and **not** claimed by UBT at this stage:

| Topic | Status |
|-------|--------|
| α⁻¹ = 137.036 (exact, including one-loop correction) | Open — Gap G137-B |
| Weinberg angle sin²θ_W | Conditional open — pure-algebra route is dead end; EW-1b (EW1+RG) remains conditional |
| W/Z boson masses | Open — Gap EW-2 |
| Higgs mass 125 GeV | Open |
| Fermion masses | Open-hard (KK obstruction theorem; see `research_tracks/fermion_masses/fermion_mass_status_v2.md §3`) |
| Mass formula structure `m(n) = A·nᵖ − Bₘ·n·ln n` | [SE] formula structure [L1]; parameters A, p, Bₘ are fitted, not derived |
| m_e reproduced to 0.22% | [SE] semi-empirical — parameters fitted |
| Mass ratios m_μ/m_e, m_τ/m_μ | Open — no UBT prediction |
| KK-mismatch theorem proof | Open — source not confirmed; see `fermion_mass_status_v2.md §3` |
| CKM/PMNS matrices | Open |
| Dynamical colour confinement | Clay Millennium Problem |
| Strong coupling g_s | Open |
| Quantum gravity / path integral | Long term — GAP-Q |
| Cosmological solutions (FRW/de Sitter) | Open — GAP-C |
| Off-shell Θ-only closure | Open — GAP-10 |
