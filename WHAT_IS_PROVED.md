<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# WHAT_IS_PROVED.md — Definitive Map of Proved Results

## 2026-07-19 update — torsion-free no-go and torsionful local representer

| # | Claim | Level | Source |
|---|---|---|---|
| GR-T1 | Central identity $\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)=g_{\mu\nu}\mathbf1$ on the Lorentz slice | [L0] | `canonical/gr_closure/covariant_tetrad_rank_theorem.tex` |
| GR-T2 | Every local Lorentz metric has a nondegenerate tetrad representation of the central identity | [STD]+[L1] | same |
| GR-T3 | Tetrad-to-metric differential has rank 10; kernel dimension 6 equals local Lorentz freedom | [L1] | same; `tools/verify_covariant_tetrad_rank.py` |
| GR-T4 | For specified tetrad and torsion, the metric-compatible frame connection is uniquely $\omega=\mathring\omega(e)+K(T)$ | [L1] | `canonical/gr_closure/gap_10omega_connection_elimination.tex`; `tools/verify_gap_10omega_connection.py` |
| GR-T5 | The torsion-free GR branch has the unique Levi--Civita spin connection | [L1] | same |
| GR-T6 | Metric-compatible Lorentz transport preserves $\eta_{ab}$ and the Lorentz slice | [L1] | same |
| GR-T7 | Every constant Lorentz tetrad has an explicit affine single-$\Theta$ representer | [L1] | `canonical/gr_closure/gap_10i_integrability_selection.tex` |
| GR-T8 | $\Theta_{\rm SR}=\Theta_0+\sqrt{\mathcal N_0}(ix^0\mathbf1+x^k\mathbf e_k)$ generates Minkowski spacetime and has zero second derivatives | [L1] | same; `tools/verify_gap_10i_integrability.py` |
| GR-T9 | Naive one-sided regular connection + invertible $\Theta$ + torsion-free compatibility forces zero curvature | [L1 NO-GO] | same |
| GR-T10 | Two-sided derivative obeys $[D_\mu,D_\nu]\Theta=F^A_{\mu\nu}\Theta-\Theta F^B_{\mu\nu}$ and permits nonzero intertwined curvatures | [L1] | same |
| GR-T11 | Lorentz-slice and metric compatibility reduce the pure pair to $A_\mu=\Omega_\mu$, $B_\mu=-\Omega_\mu^\ddagger$ modulo a cancelling central term | [L1] | `canonical/gr_closure/gap_10i_paired_connection_audit.tex`; `tools/verify_gap_10i_paired_connection.py` |
| GR-T12 | With $K=0$, the pure Lorentz pair implies $\mathring\nabla_\mu V^\nu=\delta_\mu{}^\nu$ and excludes the non-flat Schwarzschild vacuum exterior with $M\ne0$ | [L1 NO-GO] | same |
| GR-T13 | Every smooth Lorentzian tetrad has a local single-$\Theta$ representer with explicit composite metric-compatible contortion | [L1, local] | `canonical/gr_closure/gap_10i_torsionful_local_representer.tex`; `tools/verify_gap_10i_torsionful_local_representer.py` |
| GR-T14 | Direct fixed-background pure-pair matter spin current is derived; the minimal affine torsion-free branch and Lorentz-invariant pairing escape route are no-go results | [L1 conditional / L1 no-go] | `canonical/gr_closure/gap_10tdyn_10d_canonical_action_audit.tex`; `tools/verify_canonical_spin_current.py` |
| GR-T15 | Canonical UBT action selects a composite/non-minimal or translational-relative torsion completion, with physical torsion control and global continuation | [OPEN/NARROWED] | GAP-10I-CURVED, GAP-10T-DYN |
| GR-T16 | Einstein dynamics from the original UBT master equation | [OPEN] | GAP-10D |

The former compact-$\psi$ fiber-average rank closure is noncanonical and must
not be listed as the proved UBT metric mechanism.

---


**Author**: Ing. David Jaroš  
**Date**: 2026-07-19  
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


## 2026-06-11 update (v59)

| # | Claim | Level | Source |
|---|-------|-------|--------|
| C2-iv-NO-GO | C2-iv formal NO-GO: all 3 routes (p=3, homeomorphism, approach-b) fail; fiber decoupling is algebraic root cause | [FORMAL NO-GO within current $S[\Theta]$] | `research_tracks/EW/hypercharge_from_ubt.tex §3 Rem rem:c2iii_attempts` (v59) |
| λ-consistency | $\lambda=g^2/2$ from SS projection matches $\lambda_{\mathrm{target}}\approx0.119$ to within $2.7\%$; no other UBT combination within $20\%$ | [MC/L1 conditional on SS] | `research_tracks/EW/rpsi_from_action.tex §7 Rem rem:lambda_ubt_comparison` (v59) |

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

The authoritative local route is the projection-free covariant tetrad
\(E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\).  Historical metric, fiber, FRW,
and Schwarzschild ansätze are not promoted to current canonical proofs until
they are rederived in this route.

### Current proved/narrowed chain

| # | Claim | Level | Source |
|---|---|---|---|
| G1 | Central anticommutator metric on the Lorentz slice | [L0] | `canonical/gr_closure/covariant_tetrad_rank_theorem.tex` |
| G2 | Nondegenerate tetrad-to-metric differential has rank 10 and Lorentz kernel 6 | [L1] | same; `tools/verify_covariant_tetrad_rank.py` |
| G3 | For specified tetrad and torsion, \(\omega=\mathring\omega(e)+K(T)\) is the unique metric-compatible frame connection | [L1] | `canonical/gr_closure/gap_10omega_connection_elimination.tex` |
| G4 | Torsion-free branch is the Levi--Civita spin connection | [L1] | same |
| G5 | Metric-compatible Lorentz transport preserves \(\eta_{ab}\) and the Lorentz slice | [L1] | same |
| G6 | Every constant Lorentz tetrad has an affine single-\(\Theta\) representer; Minkowski is explicit | [L1] | `canonical/gr_closure/gap_10i_integrability_selection.tex` |
| G7 | Naive one-sided, invertible, torsion-free curved representation forces zero curvature | [L1 NO-GO, under stated assumptions] | same |
| G8 | Two-sided derivative gives exact left/right curvature identity and allows nonzero intertwined curvatures | [L1 identity; route narrowed] | same |
| G9 | Minimal Palatini action yields Einstein--Λ and Lovelock assumptions make the four-dimensional infrared endpoint unique | [L1 conditional] | `gap_10d_low_energy_uniqueness.tex` |
| G10 | Prescribed paired-connection system has an exact augmented-holonomy existence criterion | [L1] | `gap_10i_augmented_holonomy.tex` |
| G11 | Minimal Palatini branch has an invertible algebraic torsion equation | [L1 conditional] | `gap_10t_palatini_torsion_dynamics.tex` |
| G11b | Direct fixed-background pure-pair matter current derived; affine torsion-free and Lorentz-invariant pairing escape routes excluded | [L1 conditional / L1 no-go] | `gap_10tdyn_10d_canonical_action_audit.tex` |
| G11c | Full composite UBT selects its torsion completion and self-consistent curved tetrad | [NARROWED/OPEN] | `GAP-10T-DYN`, `GAP-10I-CURVED` |
| G12 | Schwarzschild full tetrad/lapse selected by canonical \(\Theta\) dynamics | [OPEN] | `GAP-U2Theta` |

### Perturbations and named metrics

| Claim | Current status |
|---|---|
| Regge--Wheeler and Zerilli reductions | Standard GR reductions, conditional on `GAP-B-MASTER` and an on-shell covariant-tetrad Schwarzschild background |
| Schwarzschild spatial numerical ansatz | Historical/numerical evidence only until rederived with the central anticommutator tetrad |
| Temporal Schwarzschild lapse | `GAP-U2Theta` OPEN; the former phase/Maxwell wording is withdrawn |
| FRW, Kerr, and wave branches | Candidate/historical branches requiring covariant-tetrad on-shell rederivation |
| Fiber-closure perturbation theorem | Exploratory result inside the noncanonical fiber branch; not closure of `GAP-B-MASTER` |

### Covariant-tetrad closure ledger

| Gap | Description |
|---|---|
| GAP-10K | **CLOSED locally:** tetrad-to-metric rank 10; Lorentz kernel 6 |
| GAP-10Ω-KIN | **CLOSED [L1]:** specified tetrad and torsion reconstruct the metric-compatible connection |
| GAP-10Ω-GR | **CLOSED [L1]:** torsion-free branch is Levi--Civita |
| GAP-10T-PALATINI | **CLOSED CONDITIONALLY [L1]:** minimal Cartan torsion map is algebraic and invertible |
| GAP-10T-SPIN | **CLOSED CONDITIONALLY [L1]:** direct fixed-background pure-pair matter current derived |
| GAP-10T-FLAT-NOGO | **CLOSED AS NO-GO [L1]:** minimal affine torsion-free branch excluded |
| GAP-10T-PAIRING-NOGO | **CLOSED AS NO-GO [L1]:** no nonzero nondegenerate symmetric Lorentz-invariant pairing cure |
| GAP-10T-DCOMP-SECTOR | **CLOSED [L0]:** Lorentz-real D-composite sector forces Theta into W_L |
| GAP-10T-DCOMP-LIN-OFFRES | **CLOSED CONDITIONALLY [L1]:** frozen-coefficient symbol identity A³=qA²; off q=1 driven solutions exactly holonomic (pullback-flat) |
| GAP-10T-DCOMP-RES | **OPEN:** all linearized anholonomy confined to the 6-dim resonant sector at q=1 |
| GAP-10T-GRADIENT-FLATNESS | **CLOSED AS NO-GO [L1]:** every nondegenerate exact-gradient tetrad `e^a=N₀^{-1/2}dY^a` is locally a pullback of Minkowski space; curvature and the Hilbert-Palatini term vanish identically, while affine stationarity is only a Jacobian/null-Lagrangian corollary |
| GAP-10T-DYN | **NARROWED:** the canonical self-consistent `D`-composite variation and any non-minimal or translational/relative torsion completion remain |
| GAP-10L-CONN | **CLOSED [L1]:** compatible Lorentz transport preserves the Lorentz slice |
| GAP-10L-SYM | **CLOSED CONDITIONALLY [L1]:** unique equivariant dynamics preserves the fixed set |
| GAP-10L-DYN | **NARROWED:** verify canonical equivariance and well-posed uniqueness |
| GAP-10I-SR | **CLOSED [L1]:** affine representer for constant Lorentz tetrads |
| GAP-10I-1S | **CLOSED AS NO-GO [L1]:** stated one-sided invertible curved route forces flatness |
| GAP-10I-PAIR-KIN | **CLOSED [L1]:** the Lorentz-compatible pair reduces to one spin connection; no independent A,B fields |
| GAP-10I-PAIR-GR | **CLOSED AS A TORSION-FREE NO-GO [L1]:** with $K=0$ the pure Lorentz pair implies a concurrent vector and excludes the non-flat Schwarzschild vacuum exterior |
| GAP-10I-TORSION-LOCAL | **CLOSED LOCALLY [L1]:** every smooth Lorentzian tetrad has a local single-$\Theta$ representer with composite metric-compatible contortion |
| GAP-10I-2S | **NOT REQUIRED FOR LOCAL KINEMATICS:** remains an optional torsion-free composite/auxiliary route |
| GAP-10I-PRESCRIBED | **CLOSED [L1]:** exact augmented-holonomy criterion for specified coefficients |
| GAP-10I-CURVED | **LOCAL KINEMATICS CLOSED; DYNAMICS/GLOBAL PART NARROWED:** action selection, physical torsion constraints, and global continuation remain |
| GAP-10D-PALATINI / UNIQUENESS | **CLOSED CONDITIONALLY [L1]:** conditional Einstein--Λ infrared endpoint |
| GAP-10D | **NARROWED:** derive the low-energy assumptions, coefficients, and matter action from UBT |
| GAP-10ψ-KIN / SYM | **CLOSED / CLOSED CONDITIONALLY [L1]:** gauge or translation symmetry protects the metric |
| GAP-10ψ | **NARROWED:** prove canonical selection and exclude unstable physical modes |
| GAP-B-MASTER | **OPEN:** perturbation bridge from original canonical dynamics |
| GAP-U2Theta | **OPEN:** on-shell full Schwarzschild tetrad/lapse |

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
| S8 | One-hot color detects every single `X_i`/`Y_i` error as leakage | [L1] | `gap_su3_triqubit_qec.tex`, `verify_triqubit_qec_status.py` |
| S9 | One-hot color cannot correct an unknown single `X_i` and does not detect general `Z_i` | [L1 no-go] | Knill--Laflamme witness in `gap_su3_triqubit_qec.tex` |

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
| C2-ii | $U(1)_B$ from $\psi$-winding topology | [OPEN/MC]; Lem `lem:c2ii_candidate` [MC] added v57 | `research_tracks/EW/hypercharge_from_ubt.tex §3 Rem rem:c2ii_psi_winding, Lem lem:c2ii_candidate` |
| C2-iii | Geometric coupling $S^1_\psi\leftrightarrow\mathbb{Z}_3$ colour cycle | [OPEN/MC] (blocks C2-ii); Steps 1+2 attempted v58 | `research_tracks/EW/hypercharge_from_ubt.tex §3 Rem rem:c2iii_attempts` (v58) |
| C2-iv | Fiber Decoupling in $S[\Theta]$: $S^1_\psi$ and colour fiber $\mathbb{C}^3$ algebraically decoupled | [FORMAL NO-GO within current $S[\Theta]$] (v59, deadendbox) — root cause of C2-iii; does not block papers | `research_tracks/EW/hypercharge_from_ubt.tex §3 Rem rem:c2iii_attempts` (v59) |
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

### Covariant-tetrad closure ledger

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

### Modular Symmetry and R_ψ Fixation (v62, 2026-06-11)

| ID | Claim | Level | Source |
|----|-------|-------|--------|
| psi-compact-SS | ψ compact from SS BC: Θ(ψ+2πR_ψ)=σ₃Θσ₃ | [L1] | `su2_twist_neff12.tex` |
| psi-compact-Z | ψ compact from periodicity \|Z[τ+1]\|²=\|Z[τ]\|² | [L0] | `modular_symmetry_rpsi.tex Prop prop:compact` |
| Z-total | Z[τ_E]=η(τ_E)^{-12} from det P=η² [STD] + N_eff=12 [L1] | [L1 conditional] | `modular_symmetry_rpsi.tex Prop prop:Z` |
| Rpsi-sdp | τ_E=i unique S-fixed point on {iR_ψ : R_ψ>0} | [L0] | `modular_symmetry_rpsi.tex Def def:sdp` |
| Rpsi-stat | Re S[Θ] stationary under modular flow at τ_E=i | [L0] | `modular_symmetry_rpsi.tex Prop prop:Smod` |
| Rpsi-Z | R_ψ=1 fixed point of Z[τ] symmetry | [L1 conditional] | `modular_symmetry_rpsi.tex Thm thm:fixed` |
| Rpsi-poly | Polynomial R⁶+R⁴+R²=3 unique solution R_ψ=1; N_eff cancels | [L0] | `modular_symmetry_rpsi.tex Thm thm:poly` |
| Rpsi-min | R_ψ=1 is minimum of S_eff, d²S/dR²=20C>0 | [L0]+[NUM] | `modular_symmetry_rpsi.tex Cor cor:min` |

### Information-Loss Alpha Derivation Chain (v70–v72, 2026-06-13)

| ID | Claim | Level | Source |
|----|-------|-------|--------|
| il-Omega | Ω_η(1) = 1/24 − 1/(8π) from Eisenstein G₂(i) | [L0] | `layer2_kernel_derivation.tex Lem lem:omega_eta` |
| il-12pi | 12π·Ω_η(1) = (π−3)/2 | [L0] | `layer2_kernel_derivation.tex Cor cor:12pi_omega` |
| il-CQ | C_Q = 4 from Dirac spinor dimension in UBT | [L1 cond.] | `layer2_kernel_derivation.tex Prop prop:CQ4` |
| il-Hcolour | H_colour = Ω_η·Π_colour (one-loop colour Hamiltonian) | [L1 cond.] | `layer2_kernel_derivation.tex Def def:H_colour` |
| il-Zcolour | Z_colour = Tr_{ℂ³}[I+H_colour] = 3(1+Ω_η) | [L0] | `layer2_kernel_derivation.tex Lem lem:Z_colour` |
| il-KL2 | K_L2 = √(1+Ω_η)·Π_colour (Layer2 Kraus operator) | [L1 cond.] | `layer2_kernel_derivation.tex Prop prop:kraus` |
| il-rL2 | r_L2 = Tr(Π_colour K†K) = 3(1+Ω_η) | [L1 cond.] | `layer2_kernel_derivation.tex Thm thm:rL2` |
| il-mwind | m²_wind = n²π (winding zero-mode mass) | [L1 cond.] | `gap_A_proof.tex Lem lem:wind_action` |
| il-meff | m²_eff = n²π/C_Q (equipartition across C_Q channels) | [L1 cond.] | `gap_A_proof.tex Lem lem:c0var` |
| il-rho | ρ = exp(−C_Q/(2πn)) from Gaussian zero-mode fidelity | [L1 cond.] | `gap_A_proof.tex Thm thm:gapA` |
| il-alpha | α⁻¹_UBT = 137.035999177549 (+0.026σ CODATA 2022) | [L1 cond.] | `information_loss_alpha_self_consistency.tex` |

**All steps are [L1 conditional]. Conditions**: det P=η² [STD]; N_eff=12 [L1]; one-loop approximation; Dirac eq. [L1]; SS BC [L1].
**Alpha: NOT DERIVED unconditionally.**

**Conditions for [L1 conditional]**: (i) det P_eff=η² [STD, Polchinski §7.2]; (ii) N_eff=12 [L1]; (iii) one-loop approximation (higher loops do not shift the fixed point). All conditions are explicit.

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
| Covariant-tetrad local closure | GAP-10K, GAP-10Ω-KIN/GR, GAP-10L-CONN, and GAP-10I-SR closed; one-sided curved route closed as no-go; torsion dynamics, curved integrability, Einstein dynamics, and ψ-stability remain open |
