| GR12 | FRW N=2\dot a^2 z Cliffordovy projekce $\eta_B\to-1_2$ | [L0] | frw_from_ubt.tex §N-open |
| GR13 | FRW $g_{00}=-1$ z N derivace | [L0] | frw_from_ubt.tex |
| SM15 | $Q\in\mathbb{Z}$ z U(1)$_{\rm EM}$ holonomy na $S^1_\psi$ [L1 cond.] | [L1 cond. self-dual] | colour_charge_lattice.tex |
| \alpha33 | $Z_{\rm 1loop}(\tau=i) = \vartheta_3\vartheta_4^2/\eta^3 = 2$ z SU(2) twist sektory | [L0] | mellin_insertion_B.tex §mechanism |
| \alpha34 | $B = 12^{3/2}\cdot(2\eta)^{1/4}$ z SU(2) twist + MC heat kernel | [L0+MC] | mellin_insertion_B.tex §mechanism |
<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# WHAT_IS_PROVED.md — Definitive Map of Proved Results

**Author**: Ing. David Jaroš  
**Date**: 2026-05-18  
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
| **[MC]** | Motivated conjectural bridge; not yet derived |
| **[OBS]** | Numerical or structural observation; not a derivation |

---

## 2026-05-14 update (v28)

| # | Claim | Level | Source |
|---|-------|-------|--------|
| EW6 | Anomaly cancellation (chiral) | [L1 cond. C2] | `research_tracks/EW/anomaly_cancellation.tex` |
| EW7 | EW-1b PROVED: $\lambda=g^2/2$ from SS projection | [L1 cond.] | `research_tracks/EW/rpsi_from_action.tex` |
| Q2 | T-duality lemma target formulated | [OPEN/MC] | `canonical/THEORY/t_duality_ubt.tex` |
| GR10 | Zerilli equation | [L1] | `canonical/gr_closure/zerilli_derivation.tex` |

---

## 2026-05-19 update (v33)

| # | Claim | Level | Source |
|---|-------|-------|--------|
| SM10 | Y_Q=1/6 unique via grav. anomaly A_grav(n)=n-1=0 | [L1 family check] | `canonical/interactions/colour_charge_lattice.tex` Thm. C2-uniqueness |
| NO-GO5 | Eisenstein E_4(i) route for B: ratio 0.920 | [NO-GO] | `tools/eisenstein_B_check.py` |
| L0-B1 | Algebraic identity for B: $\sum_{n=1}^\infty \frac{q^{n^2}}{1-q^n} = \prod_{n=1}^\infty (1-q^n)^{-1}$ | [L0] | `research_tracks/T3_ALPHA/mellin_insertion_B.tex` |
| NO-GO6 | Gap G137-B: NO-GO verdict removed, narrowed to algebraic identity | [NARROWED] | `research_tracks/T3_ALPHA/mellin_insertion_B.tex` |
| EW3 | Higgs: m²_eff=-6.494 from KK scan | [MC/NUM] | `research_tracks/EW/higgs_from_theta.tex` |
| COSMO5 | de Sitter Λ=3H² from Θ=e^{Ht}Θ₀ | [Prop.] | `research_tracks/quantum_ubt/frw_from_ubt.tex` Cor. |
| COSMO6 | ΔN_eff: CONDITIONAL TENSION for g*=198 explicit UBT | [CONDITIONAL TENSION] | `research_tracks/quantum_ubt/delta_neff_prediction.tex` |
| COSMO7 | ΔN_eff: OK for g*≥389 (extended scenarios) | [CONDITIONAL OK] | `research_tracks/quantum_ubt/delta_neff_prediction.tex` |
| EW4 | Hosotani mechanism on S¹_ψ: SSB from Wilson line | [OPEN] | `research_tracks/EW/higgs_from_theta.tex` |
| SM11 | C2 from Dirac quantisation on T²: Y_min=1/6 | [MC/candidate] | `canonical/interactions/colour_charge_lattice.tex` |

---


## 2026-05-21 update (v41)

| α32 | Minimální chybějící teorém pro Gap G137-B formulován | [OPEN — formalized] | mellin_insertion_B.tex §minimal-open |
| EW8 | Weinberg 1-loop: sin²θ_W(M_Z)≈0.185 (1-loop limit) | [NUM — 1-loop only] | weinberg_angle_ew1_rg.tex §rg-numerical |
| EW9 | Weinberg 2-loop [STD]: 0.231 — konzistentní s exp. | [STD] | weinberg_angle_ew1_rg.tex §rg-numerical |
| COSMO9 | FRW N konzistence: dim. mismatch → [OPEN] | [OPEN] | frw_from_ubt.tex §N-open |
| SM14 | τ₁∘τ₂∘τ₃=id ověřeno z Pauliho matic → p=3 [L0] | [L0] | colour_charge_lattice.tex §proof |

| # | Claim | Level | Source |
|---|-------|-------|--------|
| COSMO8 | FRW explicit T_μν from UBT | [Prop. pending] | `research_tracks/quantum_ubt/frw_from_ubt.tex` |
| EW5 | Hosotani SSB: Wilson line minimum | [OPEN/NUM] | `research_tracks/EW/higgs_from_theta.tex` |
| SM12 | C2: Dirac quantisation Y_min=1/6 from T² periods | [MC/candidate] | `canonical/interactions/colour_charge_lattice.tex` |
| α28 | Mock theta route for B | [OPEN — new] | `research_tracks/T3_ALPHA/mellin_insertion_B.tex` |

---

## 2026-05-18 update

| # | Claim | Level | Source |
|---|-------|-------|--------|
| COSMO1 | ΔN_eff prediction: 0.05-0.25 (benchmark g*≥427, above CMB-S4) | [OPEN pending g* derivation] | `research_tracks/quantum_ubt/delta_neff_prediction.tex` |
| COSMO2 | FRW metric from refined Θ ansatz | [Prop.] | `research_tracks/quantum_ubt/frw_from_ubt.tex` |
| GR11 | Cl⁺₁,₃ izomorfismus (even subalgebra) | [L0] | `papers/UBT_GR_Submission.tex §2.1` |
| PY1 | Python scaffold: UBT Hilbert space [OPEN_GAP placeholder] | [scaffold] | `src/ubt/quantum/quantum_scaffold.py` |
| PY2 | Chirality algebra scaffold | [scaffold] | `src/ubt/algebra/chirality.py` |
| PY3 | Observable bridge: g-2 OPEN_GAP | [OPEN_GAP] | `src/ubt/observables/physics_observable_bridge.py` |
| COSMO3 | FRW from UBT: g_{0i}=0 globally for Θ₀=1₂ | [Prop.] | `research_tracks/quantum_ubt/frw_from_ubt.tex` |
| COSMO4 | ΔN_eff: g*(T_Pl)≥120.75 z UBT field content | [Prop.] | `research_tracks/quantum_ubt/delta_neff_prediction.tex` |
| NO-GO3 | V_eff z M⁴ ζ-regularizace: faktor 11386× | [NO-GO] | `tools/veff_functional_deriv.py` |
| NO-GO4 | V_eff z Casimir T³: faktor 9003× | [NO-GO] | `research_tracks/T3_ALPHA/mellin_insertion_B.tex §8` |
| QFT1 | Quantum scaffold: Hilbert space placeholder | [scaffold/OPEN_GAP] | `src/ubt/quantum/` |
| QFT2 | Soliton regularization: finite-energy model | [NUMERICAL_EVIDENCE] | `src/ubt/solitons/` |

---

## Track T1_GR: General Relativity Recovery

All proofs in `canonical/gr_closure/` and `canonical/geometry/`.  
Comprehensive paper: `papers/UBT_GR_Submission.tex`.

### Core Chain (ψ → g → Γ → R → G = 8πGT)

| # | Claim | Level | Source |
|---|-------|-------|--------|
| G1 | The metric $g_{\mu\nu} = \mathrm{Re}[\mathrm{Tr}(\partial_\mu\Theta \cdot \partial_\nu\Theta^\dagger)]/\mathcal{N}$ is a symmetric covariant (0,2) tensor, with $\mathcal{N}$ defined by the indefinite Clifford inner product | [L1] | `papers/UBT_GR_Submission.tex` Def. 3.1, Thm. 3.2 |
| G2 | $\det(g_{\mu\nu}) \neq 0$ for admissible Θ (Theorem 3.2) | [L1] | `step2_nondegeneracy.tex` |
| G3 | Lorentzian signature $(-,+,+,+)$ is a theorem from AXIOM-B, conditional on the indefinite Clifford inner product definition for $\mathcal{N}$ | [L1] | `papers/UBT_GR_Submission.tex` Thm. 3.4, App. A |
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
| G14 | Regge-Wheeler equation (odd-parity graviton) derived without extra input | [L1] | `canonical/gr_closure/linearised_gravity.tex` (canonical source); `papers/UBT_GR_Submission.tex §5 thm:rw` |
| G15 | Zerilli equation (even-parity graviton) derived from linearised UBT (vacuum Schwarzschild, $\ell\ge2$) | [L1] | `canonical/gr_closure/zerilli_derivation.tex` |
| G16 | FRW metric in UBT solution space | [L1] | `canonical/gr_closure/frw_cosmological_solutions.tex §2 Thm 1` |
| G17 | Friedmann equations from Steps 1–5 | [L1] | `canonical/gr_closure/frw_cosmological_solutions.tex §2 Cor 1` |
| G18 | FRW Θ-ansatz: $g_{ij}=a(t)^2\delta_{ij}$; ODE-a auto-consistent with Friedmann (Lem. ode\_a\_friedmann); ODE-f exact solutions established (v56) | [L1 cond. on Friedmann branch only] (v56: quasi-static removed) | `canonical/gr_closure/frw_cosmological_solutions.tex §3 (Theorem frw_ansatz_l1; Prop prop:ode_f_full_dynamics)` |
| G18-f | ODE-f exact solutions without quasi-static approximation: dust ($\mathrm{Si}/\mathrm{Ci}$ integrals), radiation (Bessel $J_{1/4}/Y_{1/4}$) | [L1 cond. on Friedmann branch only] | `canonical/gr_closure/frw_cosmological_solutions.tex §3 Prop prop:ode_f_full_dynamics` (v56) |
| G18-fqs | ODE-f quasi-static solutions $f_{\mathrm{qs}}\propto a^{-3(1+w)}$ for dust/radiation | [L1 cond. on Friedmann branch + quasi-static $R_\psi\ll H^{-1}$] | `canonical/gr_closure/frw_cosmological_solutions.tex §3 Prop prop:ode_f_solutions` (v56) |
| G-C-sub | $g_{0i}=0$ in comoving frame | [L1 conditional] | `canonical/gr_closure/frw_cosmological_solutions.tex §4 Lem 4.1` |

### Explicitly Open (not claimed as proved)

| Gap | Description |
|-----|-------------|
| GAP-10 | Off-shell Θ-only closure (global ker J = gauge only) |
| GAP-C | FRW Θ-ansatz: $g_{ij}=a^2\delta_{ij}$ [L1 conditional]; $g_{0i}=0$ comoving [L1 conditional — Lem.~4.1]; see `canonical/gr_closure/frw_cosmological_solutions.tex` |

---

## Track T2_GAUGE: Standard Model Gauge Structure

All proofs in `canonical/interactions/`, `canonical/su3_derivation/`,
`canonical/chirality/`.  Source map: `reports/gauge_truth_matrix.md`.

### Algebraic Foundation

| # | Claim | Level | Source |
|---|-------|-------|--------|
| A1 | ℂ⊗ℍ ≅ Mat(2,ℂ) | [L0] | `biquaternion_algebra.tex` |
| A2 | ℂ⊗ℍ ≅ Cl⁺₁,₃(ℝ) (even subalgebra) | [L0] | `papers/UBT_GR_Submission.tex §2.1` |
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
| C1-S4 | $SU(2)_R$ geometric decoupling via $\psi$-parity | [MC] | `canonical/chirality/step4_no_wr_derivation.tex §3 Thm 3.1` |
| OP-S4 | Full algebraic exclusion of $SU(2)_R$ | [L1 conditional] (Loophole~1 [L1 cond.], Loophole~2 [L1 cond.], Loophole~3 [STD]) | `canonical/chirality/step4_no_wr_derivation.tex §4` |
| OP-S4-min | Minimality anomaly-safe (cond. on C2-i); unitarity (EW-2) deferred | Remark | `canonical/chirality/step4_no_wr_derivation.tex §4 Rem rem:minimality_anomaly` |
| E3 | W±, W³ as gauge connections of SU(2)_L | [L1] | Gauge principle |
| E4 | U(1)_Y from right scalar phase action on Mat(2,ℂ) | [L0] | `sm_gauge.tex §U1` |
| E5 | Hypercharge quantisation from Dirac condition on ψ-circle | [L0] | `appendix_alpha_geometry.tex §1` |
| E5b | SU(3) colour-lattice Step 1: target theorem $Q\in\mathbb{Z}$ from $S[\Theta]$ on $S^1_\psi$ | [OPEN/MC] (blocker explicit) | `canonical/interactions/colour_charge_lattice.tex` |
| SM5 | Hypercharge assignment $Y_Q=1/6$ | [L1 conditional on C2 Step 1] (C2-i now closed v55) | `canonical/interactions/colour_charge_lattice.tex`, `papers/UBT_Gauge_Submission.tex` |
| SM10 | Y_Q=1/6 unique via grav. anomaly A_grav(n)=n-1=0 | [L1 family check] | `canonical/interactions/colour_charge_lattice.tex` Thm. C2-uniqueness |
| C2-S1 | Gap C2 Step 1: $Y=(B{-}L)/2$ from OP-S4 + SU(3) colour | [L1 cond. on OP-S4 + SU(3)] | `research_tracks/EW/hypercharge_from_ubt.tex §2 Lem lem:hypercharge_formula` (v55) |
| C2-i | $B_q=1/3$ from SU(3) colour-singlet constraint | [L1 cond. on SU(3) colour structure from UBT] | `research_tracks/EW/hypercharge_from_ubt.tex §3 Lem lem:Bq_from_su3` (CLOSED v56) |
| C2-ii | $U(1)_B$ from $\psi$-winding topology | [OPEN/MC]; Lem `lem:c2ii_candidate` [MC] v57 | `research_tracks/EW/hypercharge_from_ubt.tex §3 Rem rem:c2ii_psi_winding, Lem lem:c2ii_candidate` |
| C2-iii | Geometric coupling $S^1_\psi\leftrightarrow\mathbb{Z}_3$ colour cycle | [OPEN/MC] (blocks C2-ii) | `research_tracks/EW/hypercharge_from_ubt.tex §3 Rem rem:c2ii_psi_winding` (v57) |
| EW-1b | $\sin^2\theta_W(M_Z)\approx0.231$ (Corollary) | [L1 cond. on OP-S4 + SU(3) colour structure + scale closure] | `research_tracks/EW/weinberg_angle_ew1_rg.tex §7 Prop prop:sin2_thetaW_corollary` (v56) |
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
| EW-1b | EW1+RG conditional branch: $\sin^2\theta_W(M_Z)\approx0.231$ [L1 cond. on OP-S4 + SU(3) colour + scale closure]; C2-i conditionality removed (v55) — see `research_tracks/EW/weinberg_angle_ew1_rg.tex §7` |
| EW-2 | Higgs doublet VEV from S[Θ] |
| C2 | Gap C2 Step 1: $Y=(B{-}L)/2$ [L1 cond. on OP-S4 + SU(3) colour structure from UBT] (v55); sub-gap C2-i CLOSED [L1 cond.]; sub-gap C2-ii [OPEN/MC] — does not block | `research_tracks/EW/hypercharge_from_ubt.tex` |
| C2-ii | $U(1)_B$ from $\psi$-winding topology | does not block any paper |
| Y2 | Yukawa couplings |

---

## Track T3_ALPHA: Fine Structure Constant

Source: `canonical/alpha/`, `reports/alpha_routes_ranked.md`.

| # | Claim | Level | Source |
|---|-------|-------|--------|
| α1 | N_phases = 3 from Im(ℍ) | [L0] | `canonical/n_eff/step2_AUDIT.tex` |
| α1a | $N_{\mathrm{eff}}^{\mathrm{twist}} = 12 = 3\times2\times2$ via SU(2) twist | [L1] | `canonical/n_eff/step2_AUDIT.tex`, `research_tracks/quantum_ubt/su2_twist_neff12.tex` |
| α1b | $N_{\mathrm{eff}}^{\mathrm{loop}} = 3$ from direct $S_{\mathrm{kin}}[\Theta]$ loop counting | [L1] | `canonical/n_eff/step2_AUDIT.tex`, `canonical/n_eff/neff_reconciliation.tex` |
| α1c | Identification $N_{\mathrm{eff}}^{\mathrm{loop}} = N_{\mathrm{eff}}^{\mathrm{twist}}$ | [MC/OPEN frozen] | `canonical/n_eff/step2_AUDIT.tex` |
| α1d | $B_0^{\mathrm{loop}} = 2\pi$ from $S_{\mathrm{kin}}[\Theta]$ (one-loop scalar QED, $N_{\mathrm{eff}}^{\mathrm{loop}}=3$) | [L1] | `canonical/n_eff/neff_reconciliation.tex` |
| α1e | $B_0 = 8\pi$ from the SU(2)-twist route with $N_{\mathrm{eff}}^{\mathrm{twist}}=12$ | [L1] | `papers/ncg_poisson_B0_derivation.tex`, `research_tracks/quantum_ubt/su2_twist_neff12.tex` |
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
| α_B_obs | $B = 12^{3/2}(2\eta(i))^{1/4} \approx 46.28$ numerical match | [OBS] | `research_tracks/T3_ALPHA/mellin_insertion_B.tex §3` |
| α_B_L0 | $B = 12^{3/2}(2\eta(i))^{1/4}$ algebraic identity | [L0] | `research_tracks/T3_ALPHA/mellin_insertion_B.tex §alg-identity` |
| α_nstar | $n^*(B_{\mathrm{phenom}}) = 137$ for $B_{\mathrm{phenom}} \approx 46.298$ | [L1 cond.] | `canonical/alpha/` |
| α_Neff | $N_{\mathrm{eff}} = 12$ from SU(2)-twist | [L1] | `research_tracks/quantum_ubt/su2_twist_neff12.tex` |
| N_eff_use | Integer-137 claim uses $N_{\rm eff}^{\rm twist}=12$ [L1], not $N_{\rm eff}^{\rm loop}=3$; identification twist=loop is \textbf{[OPEN/MC frozen]} | [L1] | `canonical/n_eff/step2_AUDIT.tex §rem:neff_alpha_dependency` |
| α_Z1loop | $Z_{1\mathrm{loop}}(\tau=i) = \vartheta_3\vartheta_4^2/\eta^3 = 2$ | [L0] | `research_tracks/T3_ALPHA/mellin_insertion_B.tex §mechanism` |
| G137-B-i | Volumetric factorization $W_{\mathrm{eff}} = N_{\mathrm{eff}}^{3/2}\cdot f(Z_b)$ | [OPEN/MC] | `research_tracks/T3_ALPHA/mellin_insertion_B.tex §formal-gap` |
| G137-B-ii | $Z_{1\mathrm{real}} = 2\eta(i)$ from NS sector heat kernel | [OPEN/MC] | `research_tracks/T3_ALPHA/mellin_insertion_B.tex §formal-gap` |
| G137-B-iii | $N_{\mathrm{eff}}^{1/2}$ from $T^3$ volume element at self-dual point | [OPEN/MC] | `research_tracks/T3_ALPHA/mellin_insertion_B.tex §formal-gap` |

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
| M2 | $B_0^{\mathrm{loop}} = 2\pi$ from the direct scalar loop of $S_{\mathrm{kin}}[\Theta]$ | [L1] | `canonical/n_eff/neff_reconciliation.tex` |
| M2a | $B_0=8\pi$ from the SU(2)-twist route with $N_{\mathrm{eff}}^{\mathrm{twist}}=12$ | [L1] | `papers/ncg_poisson_B0_derivation.tex`, `research_tracks/quantum_ubt/su2_twist_neff12.tex` |
| M3 | FPE equivalent formulation (scalar sector) | [L1] | `research_tracks/` |
| M4 | ΔN_eff prediction: 0.05–0.25 for benchmark $g_*\ge 427$ | [OPEN pending g* derivation] | `research_tracks/quantum_ubt/delta_neff_prediction.tex` |
| Q1 | Kanonická kvantizace gravitonů (Zerilli+RW módy) | [STD] | `research_tracks/quantum_ubt/graviton_quantisation.tex` |
| NCG1 | B₀=8π from N_eff=12 via NCG Poisson | [L1] | `papers/ncg_poisson_B0_derivation.tex` |
| PRED1 | Proton decay τ_p~10³⁴ yr (conditional) | [CONDITIONAL] | `reports/falsifiable_prediction_sheet.md` |
| PRED2 | ΔN_eff prediction (CMB-S4): total 0.05–0.25 depending on $g_*(T_{\rm Pl})$ | [OPEN — computation done, g* derivation pending] | `research_tracks/quantum_ubt/delta_neff_prediction.tex` |

---

## What Is NOT Claimed as Proved

The following are open problems, dead ends, or out-of-scope items.
They are **not** in the above list and **not** claimed by UBT at this stage:

| Topic | Status |
|-------|--------|
| Cosmological/α — Gap G137-B | STRUCTURAL EVIDENCE — 6 routes NO-GO; 3 sub-gaps named; α NOT DERIVED; see mellin_insertion_B.tex §formal-gap |
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
| Cosmological solutions (FRW/de Sitter) | PARTIALLY CLOSED — FRW in solution space [L1]; Θ-ansatz [L1 conditional]; $g_{0i}=0$ comoving [L1 conditional] — GAP-C; see `canonical/gr_closure/frw_cosmological_solutions.tex` |
| Off-shell Θ-only closure | Open — GAP-10 |
