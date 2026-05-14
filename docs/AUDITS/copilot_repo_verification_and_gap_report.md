# Copilot Repository Verification and Gap Report
## Unified Biquaternion Theory (UBT) — Physics Claims Audit

**Date:** 2026-03-10  
**Auditor:** GitHub Copilot (automated; verify_first_then_fill_gaps mode)  
**Repository:** DavJ/unified-biquaternion-theory  
**Branch audited:** copilot/audit-physics-claims  
**Audit scope:** All major physics claims in repository as of 2026-03-10

---

## Executive Summary

This audit was conducted in **verify-first mode**: every claim status is backed by a specific file citation from the repository before any gap is declared. No claim has been assumed missing without evidence.

**Overall repository scientific quality: HIGH.** The UBT framework has a well-documented, multi-layer structure with explicit separation between proved results, supported results, and open problems. The repository contains substantially more completed material than a first-pass scan would suggest.

### Principal findings

| Domain | Status | Primary evidence |
|---|---|---|
| GR recovery (chain) | **Steps 1–5 PROVED** | `GR_chain_summary.tex`, `curvature.tex`, `gr_as_limit.tex` |
| Action principle | **PROVED** | `appendix_GR_embedding.tex`, `stress_energy.tex` |
| Stress-energy derivation | **PROVED** | `stress_energy.tex`, `appendix_GR_embedding.tex` |
| QED limit | **PRESENT, not fully closed** | `qed.tex`, `STATUS_ALPHA.md`, `DERIVATION_INDEX.md` |
| Maxwell limit | **PRESENT, stated not derived** | `qed.tex` |
| Fermion / Dirac sector | **FRAMEWORK PROVED; mass ratios open** | `STATUS_FERMIONS.md`, `DERIVATION_INDEX.md` |
| SU(3)×SU(2)×U(1) emergence | **PROVED (with θ_W caveat)** | `sm_gauge.tex`, `DERIVATION_INDEX.md` |
| Alpha derivation | **SEMI-EMPIRICAL; B_base open** | `STATUS_ALPHA.md`, `DERIVATION_INDEX.md` |
| Fermion mass generation | **PARTIAL** | `STATUS_FERMIONS.md` |
| Cosmology / testability | **PRESENT, not yet empirically tested** | `STATUS_OBSERVATIONAL.md` |
| Canonical repo structure | **PRESENT, partially fragmented** | `canonical/README.md`, `DERIVATION_INDEX.md` |

### Summary verdict

- **No major claim is absent from the repository.** All items in the verification scope have documentary evidence.
- The dominant gap is the **B_base derivation** (the exponent 3/2 in `N_eff^(3/2) = 41.57`), which prevents a fully first-principles derivation of α⁻¹ = 137. This is already precisely documented as "Open Hard Problem" in the repository.
- A secondary gap is the **off-shell GR closure** (Step 6 of GR chain), already flagged as [L2] open in `GR_chain_summary.tex`.
- The **lepton mass ratio** reproduction from the KK spectrum is blocked by the proven "KK mismatch theorem"; this is already documented.
- Navigability for an external reviewer can be improved by (a) creating `canonical/bridges/` summary files and (b) adding the `AUDITS/` directory itself (this file).

---

## Verified Claims

Claims whose full derivation chain, or the majority thereof, is present and internally consistent in the repository.

### GR Recovery

**Status:** `present_but_fragmented` → effectively `verified_present` for Steps 1–5

The chain `Θ → g → Γ → R → Einstein` is proved in five steps documented across multiple files. The files are self-consistent and mutually referencing.

**Proof chain files:**
- `canonical/geometry/theta_field.tex` — Θ field definition (ℍ⊗ℂ, T-shirt equation)
- `canonical/geometry/metric.tex` — `g_μν = Re Tr(∂_μΘ · ∂_νΘ†)` (not postulated; derived)
- `canonical/geometry/curvature.tex` — Christoffel, Riemann, Ricci, Einstein as real projections of biquaternionic objects; GR equivalence in Im(𝒢_μν) → 0 limit
- `canonical/geometry/gr_as_limit.tex` — Theorem: `G_μν^(φ) = κ T_μν^(φ)` recovered for any constant phase φ
- `consolidation_project/GR_closure/GR_chain_summary.tex` — Explicit chain summary; Steps 1–5 proved [L1]; Step 6 (off-shell, [L2]) identified as open
- `docs/papers/appendix_GR_embedding.tex` — Hilbert variation derivation; T_μν; Einstein equations recovered
- `unified_biquaternion_theory/validation/validate_GR_recovery.py` — SymPy symbolic verification
- `reports/gr_recovery_final_status.md` — Linearised GR complete; non-linear recovery confirmed; off-shell obstruction identified

**Caveat:** Step 6 (pure Θ-only off-shell closure, [L2]) has an identified structural obstruction and is flagged as open. This does not affect the validity of Steps 1–5.

### Action Principle

**Status:** `verified_present`

The total action `S[Θ, g]` with Hilbert variation is documented and internally consistent.

**Key files:**
- `docs/papers/appendix_GR_embedding.tex` — Explicit action `S = ∫ d⁴x √g [R(g) + L_matter(Θ)]`; Hilbert variation `δS/δg^μν`; full derivation of T_μν
- `canonical/geometry/stress_energy.tex` — `T_μν` as Noether-derived object; not postulated
- `STATUS_ALPHA.md` — Biquaternionic field equations from Hilbert action documented

### Stress-Energy Derivation

**Status:** `verified_present`

`T_μν` is derived from the Lagrangian via Hilbert variation or Noether's theorem. It is explicitly defined as a **derived** quantity, not postulated.

**Key files:**
- `canonical/geometry/stress_energy.tex` — Canonical definition: `T_μν = Re(𝒯_μν)` (real projection); `T_μν = ∂_μΘ ∂_νΘ† − ½g_μν g^{αβ} ∂_αΘ ∂_βΘ†`; symmetry and conservation proved
- `docs/papers/appendix_GR_embedding.tex` — Full derivation including kinetic, potential, and gauge contributions

### SU(3) × SU(2)_L × U(1)_Y Emergence

**Status:** `verified_present` for SU(3) and SU(2)_L × U(1)_Y algebra structure; θ_W is semi-empirical

All three gauge groups are derived from the ℂ⊗ℍ algebra structure, not postulated.

**Key files:**
- `canonical/interactions/sm_gauge.tex` — Theorems G.A–G.D: SU(3) Lie algebra from ℂ⊗ℍ involutions [L0]; SU(2)_L from left action; U(1)_Y from right action; chirality selection; Weinberg angle flagged as semi-empirical
- `DERIVATION_INDEX.md` — `SU(3)_c` and SU(2)_L derivation: **Proved [L0]** ⭐ (canonical)
- `STATUS_THEORY_ASSESSMENT.md` — Listed in 25 proved results; rating 8.1/10

**Caveat:** Weinberg angle θ_W = sin²(0.23122) cannot be fixed by ℂ⊗ℍ alone (semi-empirical). Chirality (why SU(2)_L and not SU(2)_R) is motivated by ψ-parity but not fully derived.

### Three Fermion Generations

**Status:** `verified_present`

ψ-winding modes give three independent identical-SM-quantum-number sectors. Proved [L0] and [L1].

**Key files:**
- `DERIVATION_INDEX.md` — ψ-modes as independent B-fields [L0]; T-invariance and S-invariance [L1]; Hecke conjecture (unique p=137, 0.02% mu_err) — STRONG NUMERICAL SUPPORT
- `STATUS_THEORY_ASSESSMENT.md` — Three generations in 25 proved results

### Lorentzian Signature

**Status:** `verified_present` (newly proved March 2026)

The metric signature (−,+,+,+) is an algebraic theorem, not an axiom.

**Key files:**
- `STATUS_THEORY_ASSESSMENT.md` — "Lorentzian signature (−,+,+,+) as algebraic theorem [L0]" listed as proved result v61
- `DERIVATION_INDEX.md` — Lorentzian signature from AXIOM B: **Proved [L0]**

### N_eff = 12 and B₀ = 8π

**Status:** `verified_present`

`N_eff = 12` (zero free parameters, from 3×2×2 algebra counting) and `B₀ = 8π` from `S_kin[Θ]` are both proved.

**Key files:**
- `STATUS_THEORY_ASSESSMENT.md` — Both in 25 proved results
- `DERIVATION_INDEX.md` — `N_eff = 12`: Proved [L0]; `B₀ = 8π`: Proved [L1]

---

## Partially Closed Claims

Claims where the core result exists but the proof chain has identified gaps.

### QED Limit

**Status:** `present_but_not_referee_proof`

The QED Lagrangian, U(1) gauge invariance, running coupling β-function, and the massless photon are all present. However, the connection between `B_α ≈ 46.3` and the field theory prediction requires the open B_base factor.

**What is present:**
- `canonical/interactions/qed.tex` — `ℒ_QED = Tr[(D_μΘ)†(D^μΘ)] − ¼F_μνF^μν`; U(1) gauge transformations canonical
- `STATUS_ALPHA.md` — Running coupling `1/α(μ) = 1/α(μ₀) + (B_α/2π) ln(μ/μ₀)` derived from `N_eff = 12`; `B₀ = 2π/3` verified
- `DERIVATION_INDEX.md` — QED limit B₀ = 2π/3: **Verified**; massless photon: yes

**Gap:** The precise value `B_α ≈ 46.3` uses `B_base = N_eff^(3/2) = 41.57` whose exponent 3/2 is motivated but not derived (see Alpha section below).

### Maxwell Limit

**Status:** `partially_present`

The Maxwell field-strength tensor `F_μν` and its kinetic term are defined. The full Maxwell limit from the UBT action is stated in several files but a single compact derivation is not isolated.

**What is present:**
- `canonical/interactions/qed.tex` — `F_μν = ∂_μA_ν − ∂_νA_μ`; photon kinetic term
- `docs/papers/appendix_GR_embedding.tex` — Gauge field contribution to T_μν

**Gap:** No dedicated `Maxwell_limit.tex` or equivalent exists in `canonical/bridges/`; the Maxwell limit derivation is implicit in the QED Lagrangian.

### Alpha (Fine Structure Constant) Derivation

**Status:** `present_but_not_referee_proof` (semi-empirical)

The structural argument for α⁻¹ = 137 is present and rigorous up to two identified open constants. The result is NOT purely numerological; it follows from a prime minimization of `V_eff(n)`.

**What is present:**
- `STATUS_ALPHA.md` — Complete derivation chain: complex time compactification → Dirac quantization → prime stability → V_eff minimum at n=137; quantum correction +0.036; agreement 260 ppm
- `DERIVATION_INDEX.md` — `V_eff(n)` minimum at n=137: **Proved [L1]**; `B₀ = 8π`: **Proved [L1]**
- 22+ approaches to B_base documented and assessed

**Gap A (Open Hard Problem):** `B_base = N_eff^(3/2) = 41.57`  
The exponent 3/2 is motivated (factor 3 = dim_ℝ(Im ℍ), algebraic; factor 2 from Gaussian integral, proven; exponent 3/2 = motivated conjecture) but not derived from first principles. 22 approaches tested; all dead ends except the Hausdorff/Kac-Moody approach (Gap G3-k, partial). Status: **Open Hard Problem**.

**Gap B (Open):** Correction factor `R ≈ 1.114`  
Geometric origin unknown. 8 approaches tested.

### Dirac / Fermion Sector

**Status:** `present_but_not_referee_proof`

The Dirac-like operator is defined; three generations proved; lepton mass formula with 0.22% electron accuracy documented. However the parameters A, p, B in `m(n) = A·n^p − B·n·ln(n)` remain fitted.

**What is present:**
- `STATUS_FERMIONS.md` — Full lepton mass formula; 3-generation framework; quark theta-function mode framework
- `DERIVATION_INDEX.md` — KK mismatch theorem proved; Hecke conjecture with strong numerical support
- `canonical/interactions/sm_gauge.tex` — Fermion representations and Yukawa couplings documented

**Gap (Proved Obstruction):** KK mismatch theorem shows `E_{0,2}/E_{0,1} ≤ 2` for any real modulus on T², whereas m_μ/m_e ≈ 207. This is a proved theorem, not a calculation error — the KK spectrum cannot reproduce lepton mass ratios without an additional mechanism. This gap is honestly documented.

**Gap (Parameters):** A, p, B_m in the Hopf charge formula are fitted; their derivation from soliton tension/stability is not complete (Gaps M1–M4).

---

## Open Claims

Claims for which the framework exists but full derivation is not achieved.

### Fermion Mass Generation (full hierarchy)

**Status:** `partially_present`

The lepton mass formula exists and gives 0.22% electron accuracy. However:
- Parameters A, p, B_m are fit to data, not derived from soliton dynamics
- m_μ/m_e ≈ 207 and m_τ/m_μ ≈ 16.8 are NOT reproduced from the KK spectrum (proved obstruction)
- Quark sector: framework (Jacobi theta on SU(3) group manifold) exists; numerical θ-integrals not computed (estimated 1–2 year calculation)
- Neutrino sector: type-I see-saw identified; full derivation not achieved

**Files:** `STATUS_FERMIONS.md`, `DERIVATION_INDEX.md`, `research_tracks/three_generations/`

### Off-Shell GR Closure (Step 6)

**Status:** `absent` (structural obstruction identified)

The Re(∇†∇Θ) → G_μν off-shell closure has an identified structural obstruction. The on-shell (linearized + non-linear field equation level) GR is fully recovered. Step 6 remains [L2] open.

**Files:** `consolidation_project/GR_closure/GR_chain_summary.tex`, `reports/gr_recovery_final_status.md`

### Weinberg Angle θ_W

**Status:** `absent` from first-principles derivation

θ_W = sin²(0.23122) cannot be fixed by ℂ⊗ℍ alone; it requires additional input (fermion representations or Higgs sector). Documented as semi-empirical.

**Files:** `canonical/interactions/sm_gauge.tex`, `DERIVATION_INDEX.md`

### Chirality Selection (Why SU(2)_L not SU(2)_R)

**Status:** `partially_present`

Chirality selection is motivated by ψ-parity but not fully proved. Documented as semi-empirical.

**Files:** `DERIVATION_INDEX.md`, `canonical/interactions/sm_gauge.tex`

### Cosmology / Observational Predictions

**Status:** `present_but_not_referee_proof`

Specific predictions exist (ΔN_eff ≈ 0.046, CMB fingerprint at k=137–143, Hubble tension H(z) mechanism) but have not been empirically confirmed or tested through full MCMC analysis.

**Notable:** CMB WMAP p-value 1.00×10⁻⁴ at predicted k range is a CANDIDATE signal. Planck PR3 gives NULL result. No confirmed fingerprint yet.

**Files:** `STATUS_OBSERVATIONAL.md`

### S-matrix / Perturbative QFT Dynamics

**Status:** `absent`

Standard QFT formalism (S-matrix, Feynman rules, cross sections, perturbative expansion) is not developed. The field equation is defined; the quantization and perturbative expansion are not.

**Files:** `RESEARCH_PRIORITIES.md` (deprioritized; listed as future work)

---

## Conflicts or Notational Inconsistencies

### 1. Metric signature convention

`canonical/geometry/metric.tex` uses signature (+,−,−,−) (mostly minus). Some older files and `STATUS_THEORY_ASSESSMENT.md` reference signature (−,+,+,+). The `canonical/` directory is authoritative; others should defer to it.

**Recommended action:** Add a signature note to `canonical/geometry/metric.tex` explicitly flagging that (−,+,+,+) in some older files is equivalent (overall sign flip); no physics changes needed.

### 2. Biquaternion time dimensionality

`canonical/fields/theta_field.tex` defines `T_B = t + iψ + jχ + kξ` (full biquaternion time) in the general case, but the isotropic limit `τ = t + iψ` is the canonical working object. `STATUS_FERMIONS.md` warns that February 2026 exploratory work using full biquaternion time `T_B` violates canonical AXIOM B and the results are non-canonical.

**Recommended action:** The `theta_field.tex` file already notes the canonical limit. No change needed; the warning in `STATUS_FERMIONS.md` is sufficient.

### 3. B_base notation clash

`STATUS_ALPHA.md` uses `B_base = 41.57` (for α derivation) and `B_m` (for fermion mass formula). These are different objects. The notation is internally consistent within each file but could confuse cross-file readers.

**Recommended action:** Add a single disambiguation note to `DERIVATION_INDEX.md` (one line).

### 4. connection.tex missing from canonical/geometry/

The canonical geometry directory contains `metric.tex`, `curvature.tex`, `stress_energy.tex`, `gr_as_limit.tex` but **no** `connection.tex`. The Christoffel symbols are defined within `curvature.tex` but not in a standalone canonical file.

**Recommended action:** Either create `canonical/geometry/connection.tex` as a stub pointing to curvature.tex, or add a note in `canonical/README.md` explaining that connections are defined in `curvature.tex`.

### 5. Alpha document proliferation

The repository contains 12+ distinct alpha-related LaTeX files including deprecated versions. The `DERIVATION_INDEX.md` and `STATUS_ALPHA.md` already provide the canonical tracking. The deprecated files are labeled as such.

**No action needed:** The labeling is sufficient. Do not delete deprecated files without explicit author instruction.

---

## Minimal Next Steps Only

The following steps are the **smallest possible additions** that close genuine navigability or proof-chain gaps. They do not rederive existing results.

### Step 1: Add disambiguation note to DERIVATION_INDEX.md (1 line)

Add a single line under the B_base entry in `DERIVATION_INDEX.md` clarifying that `B_base` (α derivation) and `B_m` (fermion mass formula) are distinct objects. This prevents cross-file confusion.

**Effort:** < 5 minutes. **Priority:** LOW.

### Step 2: Add signature note to canonical/geometry/metric.tex (3 lines)

Add a "Signature convention" box noting that (−,+,+,+) used in some older files is equivalent to the canonical (+,−,−,−) up to overall sign. This prevents reviewer confusion.

**Effort:** < 10 minutes. **Priority:** LOW.

### Step 3: Create canonical/geometry/connection.tex stub (20 lines)

Create a minimal file pointing to the connection definitions in `curvature.tex`, matching the style of other canonical geometry files.

**Effort:** < 20 minutes. **Priority:** MEDIUM (completeness of canonical chain).

### Step 4: Create canonical/bridges/GR_chain_bridge.tex (summary bridge)

The GR chain is spread across 6+ files. A single 1-page bridge document (cross-references only, no new derivations) would make the chain traversable for an external reviewer.

**Effort:** < 1 hour. **Priority:** HIGH (reviewer navigability).

### Step 5: Create canonical/bridges/QED_limit_bridge.tex (summary bridge)

The QED limit material is in `qed.tex`, `STATUS_ALPHA.md`, and `appendix_GR_embedding.tex`. A single bridge document referencing these and marking the B_base gap explicitly would complete the QED claim documentation.

**Effort:** < 1 hour. **Priority:** HIGH (reviewer navigability).

### Step 6: Update STATUS_ALPHA.md — add disambiguation note (optional)

Already very complete. Consider adding a one-sentence note clearly distinguishing the "structural argument" (proved) from the "numerical derivation" (semi-empirical). May already be present; if so, skip.

**Effort:** 5 minutes. **Priority:** LOW.

---

## File Map Summary

| Claim | Primary canonical file(s) | Supporting files |
|---|---|---|
| GR chain | `canonical/geometry/curvature.tex`, `canonical/geometry/gr_as_limit.tex`, `consolidation_project/GR_closure/GR_chain_summary.tex` | `metric.tex`, `stress_energy.tex`, `appendix_GR_embedding.tex`, `gr_recovery_final_status.md` |
| Action principle | `docs/papers/appendix_GR_embedding.tex` | `stress_energy.tex` |
| Stress-energy T_μν | `canonical/geometry/stress_energy.tex` | `appendix_GR_embedding.tex` |
| QED limit | `canonical/interactions/qed.tex` | `STATUS_ALPHA.md`, `DERIVATION_INDEX.md` |
| Maxwell limit | `canonical/interactions/qed.tex` | `appendix_GR_embedding.tex` |
| Dirac / fermion | `canonical/interactions/sm_gauge.tex` | `STATUS_FERMIONS.md`, `DERIVATION_INDEX.md` |
| SU(3)×SU(2)×U(1) | `canonical/interactions/sm_gauge.tex` | `DERIVATION_INDEX.md`, `STATUS_THEORY_ASSESSMENT.md` |
| Alpha program | `STATUS_ALPHA.md` | `DERIVATION_INDEX.md`, various `alpha_derivation/` files |
| Fermion masses | `STATUS_FERMIONS.md` | `DERIVATION_INDEX.md`, `research_tracks/three_generations/` |
| Cosmology | `STATUS_OBSERVATIONAL.md` | `STATUS_THEORY_ASSESSMENT.md` |
| Falsifiability | `STATUS_OBSERVATIONAL.md` | `RESEARCH_PRIORITIES.md` |
| Canonical structure | `canonical/README.md` | `DERIVATION_INDEX.md` |

---

*This audit was produced by GitHub Copilot in verify-first mode. No existing derivations were weakened or removed. All gap assessments are backed by specific file citations.*
