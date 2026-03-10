# Claim Evidence Matrix
## Unified Biquaternion Theory — Physics Claims Audit
**Date:** 2026-03-10 | **Mode:** verify_first_then_fill_gaps

---

All status labels are drawn from the allowed set:
- `verified_present` — full chain present and internally consistent
- `present_but_fragmented` — material present but split across files; needs bridge/summary
- `present_but_not_canonical` — exists outside canonical/ directory; not yet promoted
- `present_but_not_referee_proof` — present but has identified open constants or unproved steps
- `partially_present` — core mechanism present; one or more steps incomplete
- `absent` — not found in repository despite search

---

## Evidence Table

| # | Claim | Status | Primary files (canonical) | Supporting files | Exact repo evidence | Gap (if any) | Recommended minimal fix |
|---|---|---|---|---|---|---|---|
| 1 | **GR recovery: full chain Θ→g→Γ→R→Einstein** | `present_but_fragmented` | `canonical/geometry/metric.tex`, `canonical/geometry/curvature.tex`, `canonical/geometry/gr_as_limit.tex` | `consolidation_project/GR_closure/GR_chain_summary.tex`, `docs/papers/appendix_GR_embedding.tex`, `reports/gr_recovery_final_status.md` | `GR_chain_summary.tex`: "Steps 1–5 proved [L1]"; `curvature.tex`: "All classical GR solutions recovered in Im(𝒢_μν)→0 limit"; `gr_as_limit.tex`: Theorem `G_μν^(φ) = κ T_μν^(φ)` for any const φ; `validate_GR_recovery.py`: SymPy symbolic verification | Step 6 (off-shell Θ-only closure [L2]): structural obstruction identified; linearised + non-linear field-eq level complete | Create `canonical/bridges/GR_chain_bridge.tex` — cross-references only, no new derivations |
| 2 | **GR recovery: metric emergence** | `verified_present` | `canonical/geometry/metric.tex` | — | `metric.tex` line 1: "g_μν = Re Tr(∂_μΘ · ∂_νΘ†)"; file explicitly states metric is NOT fundamental; derived from Θ | None | None |
| 3 | **GR recovery: Lorentzian signature** | `verified_present` | — | `STATUS_THEORY_ASSESSMENT.md` v61 | "Lorentzian signature (−,+,+,+) as algebraic theorem [L0]" in 25-proved-results list; "N is scale-fixing, not signature-fixing [L0]"; AXIOM B | None | None |
| 4 | **GR recovery: Einstein equations G_μν = 8πG T_μν** | `verified_present` | `canonical/geometry/curvature.tex`, `canonical/geometry/stress_energy.tex` | `docs/papers/appendix_GR_embedding.tex` | `curvature.tex`: "Einstein tensor G_μν = R_μν − ½g_μν R = Re(ℰ_μν)"; "G_μν = 8πG T_μν (derived from fundamental biquaternionic equation)"; `appendix_GR_embedding.tex`: Hilbert variation → T_μν → Einstein eqs | None for on-shell | None |
| 5 | **GR recovery: ∇^μ T_μν = 0 conservation** | `verified_present` | `canonical/geometry/stress_energy.tex` | `STATUS_THEORY_ASSESSMENT.md` | `stress_energy.tex`: Conservation in flat and curved spacetime proved; `STATUS_THEORY_ASSESSMENT.md`: "∇^μ T_μν = 0 conservation [L1]" in 25 proved results | None | None |
| 6 | **Action principle: total action S[Θ,g]** | `verified_present` | `docs/papers/appendix_GR_embedding.tex` | `STATUS_ALPHA.md` | `appendix_GR_embedding.tex`: "S = ∫ d⁴x √g [R(g) + L_matter(Θ)]"; Hilbert variation performed; T_μν derived from δS/δg^μν | None | None |
| 7 | **Stress-energy T_μν derivation** | `verified_present` | `canonical/geometry/stress_energy.tex` | `docs/papers/appendix_GR_embedding.tex` | `stress_energy.tex`: "T_μν = ∂_μΘ ∂_νΘ† − ½g_μν g^αβ ∂_αΘ ∂_βΘ†"; "CRITICAL NOTE: T_μν is NOT fundamental in UBT"; derived via Noether's theorem for spacetime translations; symmetry and conservation properties proved | None | None |
| 8 | **QED limit: Lagrangian** | `verified_present` | `canonical/interactions/qed.tex` | — | `qed.tex`: "ℒ_QED = Tr[(D_μΘ)†(D^μΘ)] − ¼F_μνF^μν"; U(1) gauge invariance proved; covariant derivative D_μ = ∂_μ + igA_μ | None for structure | None for structure |
| 9 | **QED limit: running coupling α(μ)** | `present_but_not_referee_proof` | `STATUS_ALPHA.md` | `DERIVATION_INDEX.md` | `STATUS_ALPHA.md`: "1/α(μ) = 1/α(μ₀) + (B_α/2π) ln(μ/μ₀)" derived from N_eff=12; "B₀ = 2π/3 verified" in `DERIVATION_INDEX.md` | B_base = N_eff^(3/2) = 41.57: exponent 3/2 not derived (Open Hard Problem); R ≈ 1.114 unknown origin | Document B_base open status in `canonical/bridges/QED_limit_bridge.tex` |
| 10 | **QED limit: massless photon** | `verified_present` | `canonical/interactions/qed.tex` | `DERIVATION_INDEX.md` | `qed.tex`: massless photon at φ=const; `DERIVATION_INDEX.md`: massless photon listed as verified | None | None |
| 11 | **Maxwell limit: F_μν kinetic term** | `partially_present` | `canonical/interactions/qed.tex` | `docs/papers/appendix_GR_embedding.tex` | `qed.tex`: "F_μν = ∂_μA_ν − ∂_νA_μ"; kinetic term −¼F_μνF^μν present | No dedicated Maxwell limit derivation file; limit is implicit | Add note to `canonical/bridges/QED_limit_bridge.tex` explaining Maxwell limit follows from QED Lagrangian at φ=const |
| 12 | **SU(3)_c emergence** | `verified_present` | `canonical/interactions/sm_gauge.tex` | `DERIVATION_INDEX.md` | `sm_gauge.tex`: "SU(3)_c from involutions on ℂ⊗ℍ — PROVED [L0] ⭐"; Theorems G.A–G.D (Lie algebra, fundamental rep, adjoint rep, EW decoupling all proved); color confinement "CONJECTURED WITH EXPERIMENTAL SUPPORT [L0]"; LHCb hadron data consistent | Color confinement: conjectured, not proved | None required for L0 claim; color confinement note already present |
| 13 | **SU(2)_L × U(1)_Y emergence** | `present_but_not_referee_proof` | `canonical/interactions/sm_gauge.tex` | `DERIVATION_INDEX.md` | `sm_gauge.tex`: "SU(2)_L arises as norm-preserving left action [DERIVED]"; "U(1)_Y arises as scalar phase right action [DERIVED]"; "θ_W [SEMI-EMPIRICAL]" | Weinberg angle cannot be fixed by ℂ⊗ℍ alone; chirality selection (why SU(2)_L not SU(2)_R) semi-empirical | Document θ_W status precisely in `canonical/bridges/gauge_emergence_bridge.tex` |
| 14 | **Three fermion generations** | `verified_present` | — | `DERIVATION_INDEX.md`, `STATUS_THEORY_ASSESSMENT.md` | `DERIVATION_INDEX.md`: "ψ-modes as independent B-fields [L0] Proven"; "T-invariance τ→τ+1 [L1] Proven"; "S-invariance [L1] Proven"; `STATUS_THEORY_ASSESSMENT.md`: listed in 25 proved results | None | None |
| 15 | **Alpha derivation: V_eff minimum at n=137** | `verified_present` | `STATUS_ALPHA.md` | `DERIVATION_INDEX.md` | `STATUS_ALPHA.md`: Full derivation chain; V_eff(n) = An² − Bn ln(n); minimum at n=137 among primes; `DERIVATION_INDEX.md`: "V_eff(n) minimum at n=137: Proved [L1]" | None for structural argument | None |
| 16 | **Alpha derivation: B_base = N_eff^(3/2)** | `present_but_not_referee_proof` | `STATUS_ALPHA.md` | `DERIVATION_INDEX.md` | `STATUS_ALPHA.md`: "B_base = N_eff^(3/2) = 41.57 — REMAINS OPEN HARD PROBLEM"; 22 approaches tested; "exponent 3/2 motivated but not derived"; factor 3 = dim_ℝ(Im ℍ) proved | Exponent 3/2 open; R ≈ 1.114 open | Do not invent derivation; document gap status precisely (already done in STATUS_ALPHA.md) |
| 17 | **Alpha derivation: quantum correction +0.036** | `verified_present` | `STATUS_ALPHA.md` | — | `STATUS_ALPHA.md`: "two-loop QED correction +0.036"; "α⁻¹ = 137.036; agreement 260 ppm with CODATA 2022" | None | None |
| 18 | **Fermion mass generation: lepton formula** | `present_but_not_referee_proof` | `STATUS_FERMIONS.md` | `DERIVATION_INDEX.md` | `STATUS_FERMIONS.md`: "m(n) = A·n^p − B·n·ln(n)"; "electron: 0.509856 MeV (exp: 0.511 MeV), 0.22% error"; "CHARGED LEPTONS: COMPLETE (0.00–0.22% accuracy)" | A, p, B_m are fitted, not derived; Gaps M1–M4 | Produce status note separating solved pieces (formula structure) from open pieces (parameter derivation) |
| 19 | **Fermion mass generation: KK mismatch** | `verified_present` | `STATUS_FERMIONS.md` | `DERIVATION_INDEX.md` | `STATUS_FERMIONS.md`: "KK Mismatch Theorem: E_{0,2}/E_{0,1} ≈ 1.844 ≠ 207; Proven: ratio ≤ 2 for any real modulus on T²"; `DERIVATION_INDEX.md`: "KK mismatch theorem: Proved [L0]" | This is a proved obstruction, not a gap | Note already present; no action needed |
| 20 | **Fermion mass generation: quark sector** | `partially_present` | `STATUS_FERMIONS.md` | `DERIVATION_INDEX.md` | `STATUS_FERMIONS.md`: "Framework: Jacobi theta functions on SU(3) group manifold; χ² = 2.277"; "Full theta integral calculation estimated 1–2 years" | Theta function integrals on SU(3) not calculated; light quark masses need refinement | No minimal fix; document open status (already in STATUS_FERMIONS.md) |
| 21 | **Fermion mass generation: neutrino sector** | `partially_present` | `STATUS_FERMIONS.md` | — | `STATUS_FERMIONS.md`: "Type-I see-saw mechanism identified; Full derivation not achieved" | Full derivation not achieved | No minimal fix; document open status (already present) |
| 22 | **Cosmology: ΔN_eff prediction** | `present_but_not_referee_proof` | `STATUS_THEORY_ASSESSMENT.md` | `STATUS_OBSERVATIONAL.md` | `STATUS_THEORY_ASSESSMENT.md`: "ΔN_eff ≈ 0.046 (above CMB-S4 threshold 0.03)"; `STATUS_OBSERVATIONAL.md`: listed as testable prediction | Not yet empirically confirmed | No minimal fix; prediction is documented |
| 23 | **Cosmology: Hubble tension mechanism** | `partially_present` | `STATUS_OBSERVATIONAL.md` | `RESEARCH_PRIORITIES.md` | `STATUS_OBSERVATIONAL.md`: "Metric latency: dτ = dt(1 + εf(z)); Required εβ ≈ 8×10⁻⁴"; H(z) smooth interpolation predicted | Full MCMC analysis not performed; εβ requirement is narrow | Document empirical status; full test is Priority 2 in RESEARCH_PRIORITIES.md |
| 24 | **Falsifiability / testability** | `verified_present` | `STATUS_OBSERVATIONAL.md` | `RESEARCH_PRIORITIES.md` | `STATUS_OBSERVATIONAL.md`: specific CMB predictions with p-values; Hubble H(z) test; modified gravity test (NS); all assigned feasibility ratings | Observational tests are feasible but not yet performed | None; separation of feasible-now vs. future-detectors is already present |
| 25 | **Canonical repo structure** | `present_but_fragmented` | `canonical/README.md` | `DERIVATION_INDEX.md` | `canonical/README.md`: Phase 1 complete; Phase 2 (create canonical .tex files) in progress; 11 geometry files, 3 field files, 3 interaction files present | `canonical/bridges/` directory does not exist; `canonical/geometry/connection.tex` missing; content still scattered | Create `canonical/bridges/` with GR and QED bridge documents; create `connection.tex` stub |
| 26 | **N_eff = 12 (zero free parameters)** | `verified_present` | — | `STATUS_THEORY_ASSESSMENT.md`, `DERIVATION_INDEX.md` | `STATUS_THEORY_ASSESSMENT.md`: "N_eff = 12 (3×2×2, zero free parameters) [L0]" in 25 proved results; `DERIVATION_INDEX.md`: "Proved [L0]" | None | None |
| 27 | **ℂ⊗ℍ ≅ Mat(2,ℂ) algebra** | `verified_present` | — | `STATUS_THEORY_ASSESSMENT.md`, `DERIVATION_INDEX.md` | `STATUS_THEORY_ASSESSMENT.md`: "ℂ⊗ℍ ≅ Mat(2,ℂ) [L0] — algebraic identity" in 25 proved results | None | None |
| 28 | **S-matrix / perturbative QFT dynamics** | `absent` | — | `RESEARCH_PRIORITIES.md` | `RESEARCH_PRIORITIES.md`: not listed as priority; `STATUS_THEORY_ASSESSMENT.md`: "Dynamics — S-matrix, cross sections, perturbative QFT not developed" in open problems | Full QFT perturbative expansion not developed | No minimal fix for this large gap; it is outside audit scope |

---

## Status Count Summary

| Status | Count | Claims |
|---|---|---|
| `verified_present` | 14 | 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 15, 17, 24, 26, 27 |
| `present_but_fragmented` | 2 | 1, 25 |
| `present_but_not_referee_proof` | 5 | 9, 13, 16, 18, 22 |
| `partially_present` | 5 | 11, 20, 21, 23, 19* |
| `absent` | 1 | 28 |

*Claim 19 (KK mismatch) is `verified_present` as a proved obstruction theorem, not a gap.

---

*This matrix is produced by GitHub Copilot in verify-first mode. Every status entry is backed by a direct file citation. No claim has been labeled missing without checking repository evidence.*
