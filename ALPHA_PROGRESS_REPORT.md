<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# ALPHA_PROGRESS_REPORT.md — P4: Fine Structure Constant Closure Program

> **DEPRECATED / SUPERSEDED STATUS: This document contains pre-audit alpha claims. Current alpha status is given by STATUS_OF_UBT.md and canonical/alpha/ALPHA_MASTER_STATUS.md.**
> Audit references: `canonical/alpha/gamma_entropy_alpha_refinement_status.tex`, `reports/gamma_entropy_alpha_interpolation_audit.md`.


> **LEGACY / SUPERSEDED BANNER (2026-05-10)**  
> This root-level progress snapshot is historical and superseded.  
> Canonical alpha truth is only `canonical/alpha/ALPHA_MASTER_STATUS.md`.  
> Current verdict: alpha is **NOT derived**; `alpha_bare^{-1}=137` is **CONDITIONAL ONLY**;  
> physical `alpha^{-1}=137.036` is **NOT derived**; **Gap G137-B remains open**.

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T3_ALPHA — Fine Structure Constant Derivation  
**Purpose**: Consolidated progress report on the α derivation program — what is
proved, what has been tried and failed, what remains to attempt, and what the
strategic decision gate is.  
**Sources**: `research_tracks/T3_ALPHA/alpha_status_report.md`,
`research_tracks/T3_ALPHA/assumptions_audit.md`,
`research_tracks/T3_ALPHA/fallback_layer2_outline.md`,
`reports/alpha_no_fit_audit.md`,
`DERIVATION_INDEX.md §Fine Structure Constant (α)`,
`MILESTONE_REVIEW.md §4`, `PRIORITIES_2026.md §4`

> **Historical status (2026-05-10)**: This progress snapshot is retained for
> provenance and is superseded for active alpha claims by
> `canonical/alpha/ALPHA_MASTER_STATUS.md`.

---

## 1. Executive Summary

| Item | Verdict |
|------|---------|
| α derivation: overall status | **INCOMPLETE** — first-principles claim not yet achieved |
| Minimum viable claim (α⁻¹_bare = 137) | **ACHIEVABLE** — if and only if k=1 is proved |
| Full first-principles claim (α⁻¹ = 137.036) | **NOT ACHIEVED** — three blocking gaps remain |
| Exhausted approaches | 27+ documented approaches; no new directions in this space |
| One untested route | Modular bootstrap (Ẑ(τ) = ϑ₃³(τ) + crossing symmetry) |
| Strategic recommendation | Time-box modular bootstrap to 4 weeks; activate Layer2 fallback in parallel |
| Layer2 coding paper | **Publishable now** — independent of B_base; high-impact target |

---

## 2. What Is Proved (Zero-Parameter Results)

### 2.1 N_eff = 12 — [L0] PROVED

```
N_eff = N_phases × N_helicity × N_charge
      = dim_ℝ(Im ℍ) × 2 × 2
      = 3 × 2 × 2 = 12
```

**Source**: `canonical/n_eff/step1_mode_decomposition.tex` (Theorem 1.4),
`canonical/n_eff/step3_N_eff_result.tex`  
**Verification**: `ARCHIVE/archive_legacy/consolidation_project/N_eff_derivation/verify_N_eff.py`  
**Circularity check**: Clean — no reference to α or m_e  
**Status**: Zero-free-parameter algebraic theorem

---

### 2.2 B₀ = 8π (one-loop baseline) — [L1] PROVED

```
B₀ = 2π N_eff / 3 = 2π × 12 / 3 = 8π ≈ 25.133
```

Derived from the one-loop vacuum polarisation of N_eff = 12 charged modes on
the ψ-circle.  The QED limit (N_eff = 1) gives B₀ = 2π/3, verified.

**Source**: `canonical/n_eff/step2_vacuum_polarization.tex` (Theorem 3.1)  
**Circularity check**: Clean  
**Status**: Proved; no free parameters in the functional form

---

### 2.3 V_eff(n) = n² − B·n·ln n — [L1] PROVED (given B)

The one-loop effective potential for winding mode n on S¹_ψ follows from the
standard one-loop field theory calculation.  The functional form is clean; the
only input is the coefficient B.

**Source**: `canonical/appendices/appendix_alpha_geometry.tex §3`  
**Circularity check**: Clean given B

---

### 2.4 Stationarity condition for V_eff — [L1] PROVED (given B)

The one-loop effective potential $V_{\mathrm{eff}}(n) = n^2 - B \cdot n \cdot \ln n$
has its continuous minimum at $n^*$ satisfying the **transcendental equation**:

```
∂V_eff/∂n|_{n*} = 0  ⟹  2n* = B·(ln n* + 1)
```

This equation has **no elementary closed form**; it is solved numerically.
Selected values:

| B | n\*_continuous |
|---|--------------|
| 8π ≈ 25.13 | 65.0 |
| N_eff^{3/2} ≈ 41.57 | 120.4 |
| 46.284 | 137.000 |
| 46.298 (B_phenom) | 137.05 |

**Correction of earlier error**: This section previously stated `n* = √(B/2)`,
which is the stationarity condition of a *different* potential `V = n² − B·ln n`
(missing the `n` factor).  For `B = 46.3`, `√(B/2) ≈ 4.8`, which is clearly
not 137.  The `√(B/2)` formula was a transcription error and is now removed.

```
n* = 137  is a prime-stable attractor of V_eff  
given B ≈ 46.284–46.298 (the phenomenological value)
```

**Source**: `canonical/appendices/appendix_alpha_geometry.tex §4`,
`canonical/alpha/veff_corrected_statement.tex`  
**Status**: Proved given B_phenom (phenomenological; conditional on Gap G137-B)

---

### 2.5 Prime stability of n* = 137 — [L1] PROVED

The winding number n must be stable under π₁(S¹_ψ) deformations, which requires
n* to be prime (no sub-harmonic modes exist to break the mode).  137 is prime.
The argument is a homotopy stability theorem.

**Source**: `canonical/appendices/appendix_alpha_geometry.tex §4`  
**Status**: Proved as a mathematical theorem; primality of 137 is a consequence

---

### 2.6 Two-loop QED correction structure — [L1] PROVED

```
α⁻¹(m_e) = α⁻¹_bare + (1/3π) ln(Λ/m_e) + O(α)
```

The structure of the two-loop QED correction is standard QED; the coefficient
1/(3π) is derived.  The issue is that Λ requires m_e as input (circular).

**Source**: `experiments/alpha_core_repro/alpha_two_loop.py`,
`experiments/alpha_core_repro/two_loop_core.py`

---

### 2.7 Toroidal compactification and Dirac quantisation — [L0] PROVED

The ψ-circle compactification and the Dirac quantisation condition:
```
e^{iq ∮_ψ A_ψ dψ} = 1
```
are derived from unitarity and gauge consistency of the charged Θ field.

**Source**: `canonical/appendices/appendix_alpha_geometry.tex §1`  
**Circularity check**: Clean

---

## 3. The Central Blocking Gap: B_base (Gap G3-k)

### 3.1 What Is Needed

Derive B_base = N_eff^{3/2} = 12^{3/2} ≈ 41.57 from UBT field theory.
Specifically: prove that the Kac-Moody level k = 1 in the WZW-type description
of the biquaternion field on the ψ-torus.

### 3.2 Why It Matters

```
If k = 1 is proved:
   B_base is clean → n* = 137 is derived → minimum viable α paper possible

If k = 1 remains conjecture:
   B_base is conditional → α derivation is incomplete → no publication claim
```

### 3.3 Inventory of Tested Approaches (27+ exhausted)

| Approach group | Method | Result | Status |
|----------------|--------|--------|--------|
| H1 | Direct N_eff counting with one-loop anomaly | B₀ = 8π | Proved [L1]; does not give B_base |
| H2 | CS-term absence → k=1 | k=1 motivated by free-boson/WZW fixed point minimality | [MC] — conjecture, not proof |
| H3 | Dynkin index (adjoint, fundamental reps) | adjoint → k=6; fundamental → k=3/2; neither = 1 | [DEAD END] |
| A2/Hausdorff | Gaussian measure on Im(ℍ); exponent d/2 = 3/2 from d=3 | Exponent 3/2 structural; det(S'') not computed | [PARTIAL/MC] |
| A3 | Modular: Ẑ(τ) = ϑ₃³(τ), weight k=3/2 under S-duality | Confirms exponent 3/2 algebraic origin; does not fix k_KM=1 | [L0 COMPUTED]; Gap G8 clarified |
| B1 | Volume ratios | No natural combination produces B_base | [DEAD END] |
| B2 | Algebraic search: best candidate 1+α(N_eff+π+1/4) ≈ 1.1123 | 0.15% error; no algebraic derivation | [NUMERICAL OBSERVATION] |
| B3 | Two-loop β-function on T³×S¹ | Scalar c≈1.91; SU(2) c≈7.33; all-mode c=44; no natural content reproduces target | [DEAD END — confirmed] |
| C1 | Seeley-DeWitt curvature on Im(ℍ) | Correction ∝ Λ⁻² → 0 in UV | [DEAD END] |
| C2 | Mode pair interference | Algebraic identity restatement | [DEAD END] |
| D1 | Unitarity constraint on Im(ℍ) | Reduces N_eff 12→8 (wrong direction) | [DEAD END] |
| D2 | Dimensional transmutation on Im(ℍ) | Requires R_ψ as free parameter | [DEAD END] |
| D3 | Cartan-Killing metric on su(2) | Normalised form = Euclidean; no correction | [DEAD END] |
| E1 | Instantons on SU(2) | B_base/B₀ > 1 requires negative instanton action — impossible | [DEAD END] |
| E2 | Index theorem / anomaly on Im(ℍ) | ind(D_{S³}) = 0 (odd-dimensional manifold) | [DEAD END] |
| E3 | Holomorphic factorisation | Im(ℍ) has no complex structure; real Gaussian forced | [STRUCTURAL CONFIRMATION of 3/2 exponent; not new path] |
| E4 | NCG spectral triple (UBT version) | B_base/N_gen² ≈ 4.619 ≈ 3π/2; gap (a) [det(S'')] open | [PARTIAL — numerical observation] |
| F1–F4 | NCG a₄ coefficient variants | F4: [dim_ℝ(ℍ)×dim_ℝ(Im ℍ)]^{3/2} = 41.57 — algebraic identity but restatement of Hausdorff; no independent 3/2 derivation | [PARTIAL — no new closure] |
| G2 | Weyl anomaly coefficient | c̃ = 1/15 rational; required exponent ≈ 2.65 unnatural | [DEAD END] |
| G4 | Fueter mode count | Cumulative 650 or degree 36/49; neither = 41.57 | [DEAD END] |
| G7 | QK index, ℂ⊗ℍ over ℍ | ind=4 (flat); N_eff-independent | [DEAD END] |
| R-factor v70–v73 | Two-scale ratio, modular near τ=i, heat kernel on flat T³ | All dead ends; best candidate ΔB = 3π/2 ≈ 4.712 (Motivated Conjecture only) | [DEAD END — confirmed; MC status for ΔB=3π/2] |
| Canonical norm r²_vac | r²=1 from ‖Θ‖²=1; k=2π∉ℤ — non-integer KM level | [CONFIRMED DEAD END] | |

**Total exhausted**: 27+ approaches across 73+ tracked versions in `DERIVATION_INDEX.md`.

---

### 3.4 The One New Route: Modular Bootstrap

**Not yet attempted** (as of 2026-04-27).

**Method**:
1. Compute the partition function Ẑ(τ) = ϑ₃³(τ) on the UBT torus (already
   established: ϑ₃³(τ) transforms as modular weight 3/2 — Gap G8 computed).
2. Apply modular bootstrap: impose crossing symmetry constraints on the
   4-point function of the biquaternion field theory on T².
3. Check whether crossing symmetry forces k_KM = 1 as a consistency condition.

**Known obstacle**: ϑ₃³(τ) has modular weight 3/2 — this is the *partition
function* modular weight, not the Kac-Moody level k.  These are different
quantities.  Whether crossing symmetry forces k=1 is not obvious.

**Estimated difficulty**: Hard.  Requires a full CFT treatment of the biquaternion
field theory on T².  May involve Virasoro characters and modular bootstrap
technology from 2D CFT.

**Time-box**: 4 weeks.  If k=1 does not emerge from this approach, redirect
effort to T1_GR + T2_GAUGE writing (higher-value work).

---

## 4. The Correction Gap: δ = 0.036

| Item | Status | Circularity |
|------|--------|-------------|
| δ = α⁻¹ − 137 ≈ 0.036 | SEMI-EMPIRICAL | **CIRCULAR** — uses α and m_e as inputs |
| ΔB = 3π/2 ≈ 4.712 additive conjecture | [MC] — motivated by k_mod = 3/2 and θ_W^min = π | Clean (no α, m_e) but three unclosed sub-gaps |
| Best algebraic candidate for R | 1+α(N_eff+π+1/4) ≈ 1.1123 (0.15% error) | Circular — uses α |

**Bottom line**: The correction term cannot be derived without circular reference
to α or m_e.  The minimum viable paper claim is α⁻¹_bare = 137, which does
**not** require the correction term.

---

## 5. R_ψ: Physical Calibration

| Item | Status |
|------|--------|
| T-duality self-dual point R_ψ = R_t (algebraic) | [L1] — clean |
| Physical value R_ψ = ℏ/(m_e c) | [SE] SEMI-EMPIRICAL — uses m_e |

Deriving R_ψ in physical units without m_e input is an open hard problem.
It requires either a non-circular derivation of the electron mass or an
independent algebraic fixation of the energy scale.

**Source**: `canonical/geometry/Rpsi_dynamical_fix.tex`

---

## 6. No-Fit Audit Summary

The `reports/alpha_no_fit_audit.md` audits all active derivation routes against
the strict criterion: **no parameter may be chosen to match α**.

| Route | Classification | Blocking gap |
|-------|---------------|--------------|
| A1 — Gauge normalization | CONDITIONAL | EW-1: g'/g from Aut(ℂ⊗ℍ) not fixed |
| A2 — Symmetry breaking | CONDITIONAL | EW-1 + EW-2: VEV structure |
| A3 — Modular | FAILED (integer 137 already from L1 result) | — |
| A4 — Coding (Layer2 scan) | FAILED | Coding = charge spectrum structure, not coupling magnitude |

**Primary bottleneck** (from audit): All viable routes converge on Gap EW-1 —
the ratio g'/g must be derived from the UBT algebra to fix θ_W and hence α.

---

## 7. Strategic Decision Gate

### Gate: +4 weeks from 2026-04-28 → 2026-05-26

**Evaluate**: Has the modular bootstrap approach produced k=1 from crossing
symmetry constraints?

| Outcome | Action |
|---------|--------|
| k=1 proved from bootstrap | Draft minimal "α⁻¹_bare = 137" paper |
| Bootstrap blocked or ambiguous | **Declare T3_ALPHA time-boxed; redirect 15% effort to T1+T2 writing** |

**Regardless of gate outcome**: Activate Layer2 coding paper in parallel
immediately (does not compete with α attempt).

---

## 8. Layer2 Fallback: Current Status

The Layer2 coding paper (Gray code structure of SU(3) from ℂ⊗ℍ) is
**publication-ready in 6 weeks** and does **not** depend on B_base.

| Prerequisite | Status |
|-------------|--------|
| ℂ⊗ℍ ≅ Mat(2,ℂ) | [L0] PROVED |
| ℤ₂×ℤ₂×ℤ₂ involutions and SU(3) | [L0] PROVED |
| Qubit encoding of SU(3) | [L0] PROVED |
| Gray code structure of involutions | [L0] PROVED |
| 8 Gell-Mann generators numerically verified | Done |
| gray_transport_layer/ content | Ready |

**All prerequisites satisfied.**  Paper can be begun immediately.

**Proposed title**: *Biquaternion Algebra as a Natural Error-Correcting Code:
Gray Code Structure of SU(3) from ℂ⊗ℍ*

**Target**: Physical Review Letters (4 pages), or npj Quantum Information

**Outline**: `research_tracks/T3_ALPHA/fallback_layer2_outline.md`

---

## 9. Clean Chain Summary

```
CLEAN (proved, zero free parameters, no α or m_e as input):
   A1 (ℂ⊗ℍ axiom)  ────────────────────────────────────────────────────►  [L0]
   A2 (τ = t+iψ, S¹_ψ)  ──────────────────────────────────────────────►  [L0]
   A3 (N_eff = 12)  ───────────────────────────────────────────────────►  [L0]
   A4 (B₀ = 8π)  ─────────────────────────────────────────────────────►  [L1]
   A6 (V_eff form)  ───────────────────────────────────────────────────►  [L1] given B
   A7 (stationarity: 2n* = B·(ln n* + 1))  ──────────────────────────────►  [L1] given B
   A8 (prime stability of 137)  ───────────────────────────────────────►  [L1]

BLOCKED (A5 requires k=1 proof):
   A5 (B_base = N_eff^{3/2})  ─────────── k=1 OPEN  ──────────────────►  [MC]
                                                │
                               Modular bootstrap attempt (4-week time-box)

NOT CLEAN (circular or semi-empirical — must not appear in first-principles claim):
   A9 (δ = 0.036)  ────── uses α, m_e ──────────────────────────────►  [CIRC]
   A10 (R_ψ physical)  ── uses m_e ───────────────────────────────────►  [SE]
   A12 (ΔB = 3π/2)  ────── uses θ_W (indirect) ──────────────────────►  [MC]
```

---

## 10. What Would Constitute a Publishable α Paper

### Minimum viable claim (α⁻¹_bare = 137)

Required:
- Prove k=1 via modular bootstrap or any other clean route
- Accept α⁻¹_bare = 137 (integer, bare value)
- State δ = 0.036 as the known two-loop QED correction (external fact, not UBT prediction)

This would be a significant result: the bare electromagnetic coupling constant
predicted from biquaternion algebra alone, no free parameters.

### Full first-principles claim (α⁻¹ = 137.036)

Additionally required:
- Derive δ = 0.036 without using α or m_e as input (Gap A9)
- Derive R_ψ in physical units without m_e as input (Gap A10)
- Derive ΔB = 3π/2 from S[Θ] without θ_W as input (Gap A12)

This is the "strong claim" that would be the most significant result.
Current probability: ~8% (MILESTONE_REVIEW.md §4.3).

---

## 11. References

| File | Content |
|------|---------|
| `research_tracks/T3_ALPHA/alpha_status_report.md` | Full status by component |
| `research_tracks/T3_ALPHA/assumptions_audit.md` | Circularity map of all 12 assumptions |
| `research_tracks/T3_ALPHA/fallback_layer2_outline.md` | Layer2 paper full outline |
| `reports/alpha_no_fit_audit.md` | No-fit audit of four active routes |
| `DERIVATION_INDEX.md §Fine Structure Constant` | Full approach inventory (27+ documented) |
| `canonical/appendices/appendix_alpha_geometry.tex` | Prime-attractor L1 proof |
| `canonical/n_eff/` | N_eff = 12 and B₀ = 8π proofs |
| `canonical/interactions/B_base_derivation_complete.tex` | B_base partial derivation |
| `canonical/geometry/Rpsi_dynamical_fix.tex` | R_ψ hard-problem documentation |
| `experiments/alpha_core_repro/alpha_two_loop.py` | Two-loop QED correction code |
| `experiments/validation/validate_B_coefficient.py` | Non-circularity verification |
| `MILESTONE_REVIEW.md §4` | Strategic assessment of T3_ALPHA |
| `PRIORITIES_2026.md §4` | Current priority framing |
