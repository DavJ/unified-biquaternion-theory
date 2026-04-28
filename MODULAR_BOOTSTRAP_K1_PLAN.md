<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# MODULAR_BOOTSTRAP_K1_PLAN.md — Modular Bootstrap Attack on k=1

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T3_ALPHA — Fine Structure Constant Derivation  
**Status**: PLANNED — not yet attempted  
**Time-box**: 4 weeks (deadline: 2026-05-26)  
**Companion files**:
- `ALPHA_BEST_ROUTE.tex` — best-candidate derivation chain  
- `canonical/alpha/alpha_best_route.tex` — canonical source for derivation chain  
- `ALPHA_PROGRESS_REPORT.md` — full T3_ALPHA status and exhausted approaches  
- `research_tracks/T3_ALPHA/assumptions_audit.md` — circularity map  

---

## 1. Problem Statement

The single remaining gap in the minimum viable α derivation is:

> **Gap G3-k**: Prove that the Kac-Moody level of the current algebra of the
> biquaternion field Θ on the ψ-torus T² is **k = 1**.

If k = 1 is proved, then:

```
B_base = N_eff^{3/2} = 12^{3/2} ≈ 41.57
```

follows as a zero-parameter result, and the full chain to α⁻¹_bare = 137 closes.

If k ≠ 1 or k is not uniquely forced, then B_base is not derived, and the
minimum viable α paper cannot be written.

### Circular inputs that must NOT be used

| Input | Label | Reason |
|-------|-------|--------|
| δ = 0.036 | **[CIRC]** | Uses α and m_e as input; two-loop QED correction is external |
| R_ψ in SI units | **[SE]** | Uses electron mass m_e to fix the physical scale |
| Physical α correction | **[CIRC]** | Requires m_e-dependent UV cutoff Λ |

These three inputs are excluded from the k=1 proof.  The proof must rest solely
on the UBT algebraic structure (ℂ⊗ℍ axiom, S¹_ψ compactification, N_eff = 12).

---

## 2. What Would Constitute Proof of k = 1

A result is accepted as proof of k = 1 if and only if ALL of the following hold:

1. **No fitting**: k = 1 must be forced by crossing symmetry or an algebraic
   identity.  It must not be chosen to reproduce α or B_base.

2. **Unique value**: The argument must exclude k ≠ 1.  It is not sufficient to
   show k = 1 is *consistent* with the UBT spectrum — k = 1 must be the *unique*
   consistent value.

3. **No circular input**: The proof must not use α, m_e, or any quantity
   calibrated to α or m_e.

4. **Explicit operator content**: The proof must identify which primary operators
   of the CFT are forced by the UBT field content and show they are inconsistent
   with k ≠ 1.

5. **Reproducible**: The key crossing-symmetry computation must be either
   (a) an explicit analytic calculation, or (b) a numerical bootstrap bound
   reproducible from a script in `experiments/`.

### Partial result (not sufficient for publication)

Showing that k = 1 is *the simplest* or *most natural* value is a Motivated
Conjecture [MC], not a proof.  This has already been established in v67 via the
CS-absence / free-boson minimality argument.  A new argument must go beyond [MC].

---

## 3. Mathematical Setup

### 3.1 Partition function (already computed, Gap G8 closed)

The partition function of the UBT biquaternion field on the ψ-torus T² is:

```
Ẑ(τ) = ϑ₃(τ)³
```

where ϑ₃(τ) = Σ_{n∈ℤ} q^{n²/2}, q = e^{2πiτ}, is the Jacobi theta function.
This is the partition function of **three free compact bosons** at the
self-dual radius, or equivalently of **three independent SU(2)_1 WZW models**.

The modular weight of Ẑ(τ) = ϑ₃³(τ) is **3/2** (weight 1/2 per ϑ₃ factor),
matching the exponent in B_base = N_eff^{3/2}.  This is a structural coincidence,
not fitted.

**Key degeneracy**: Both interpretations give the same Ẑ(τ):
- Three free compact bosons at self-dual radius (c = 3, k → ∞ in SU(2) language)
- Three SU(2)_1 WZW models (c = 3, k = 1 per factor)

The modular weight alone cannot distinguish k = 1 from k = ∞.

### 3.2 Operator content (distinguishes k=1 from free boson)

| CFT interpretation | Primary dimensions h | Operator spectrum |
|--------------------|---------------------|-------------------|
| SU(2)_1 (per factor) | h = 0, 1/4 only | Two primaries: j=0 (identity) and j=1/2 (spinor) |
| Free compact boson | h = n²/(4R²), all n∈ℤ | Full tower of winding modes |
| SU(2)_k, k > 1 | h = j(j+1)/(k+2) | Extra primaries j = 1, …, k/2 present |

At the self-dual radius R = 1/√2, the free-boson and SU(2)_1 spectra coincide.
Away from the self-dual radius, they differ.  The bootstrap must check whether
the UBT spectrum is self-dual.

### 3.3 Central charge

Both interpretations give c = 3.  This is consistent with three compact bosons
from Im(ℍ) = ℝ³.  The central charge does not fix k.

---

## 4. Modular Bootstrap Steps

### Step M1: Verify conformal invariance of S[Θ] on T²

**Goal**: Show that the UBT action S[Θ] restricted to the imaginary-time torus T²
is a 2D conformal field theory (CFT) with c = 3.

**Method**: Check that the stress-energy tensor T(z) of S[Θ] satisfies the Virasoro
OPE with c = 3, using the Gaussian path integral over Θ on T².

**Expected result**: S[Θ] = three decoupled compact boson actions with c = 1 each.

**File**: `research_tracks/T3_ALPHA/bootstrap_step_m1_conformal.tex` (to be created)

**Acceptance criterion**: T(z)T(w) OPE coefficient reproduces c = 3.

---

### Step M2: Compute the 4-point function

**Goal**: Compute ⟨Θ(z₁)Θ(z₂)Θ(z₃)Θ(z₄)⟩ on T², where Θ is the lowest
charged mode of the biquaternion field.

**Method**: Use the Coulomb-gas / free-boson representation of the 4-point function.
For three free compact bosons, this is:

```
⟨∏ᵢ Vₙᵢ(zᵢ)⟩ = |∏ᵢ<ⱼ (zᵢ - zⱼ)|^{nᵢnⱼ/R²}   (charge conservation: Σnᵢ = 0)
```

where Vₙ = e^{inX/R} is the vertex operator for winding mode n.

**File**: `research_tracks/T3_ALPHA/bootstrap_step_m2_4point.tex` (to be created)

**Acceptance criterion**: Explicit expression for the 4-point function as a function
of the cross-ratio η = (z₁₂z₃₄)/(z₁₃z₂₄).

---

### Step M3: Impose crossing symmetry

**Goal**: Require that the s-channel and t-channel OPE decompositions of the
4-point function agree:

```
⟨V_{n₁}V_{n₂}V_{n₃}V_{n₄}⟩_s  =  ⟨V_{n₁}V_{n₂}V_{n₃}V_{n₄}⟩_t
```

**Method**: For the free-boson / SU(2)_1 case, crossing symmetry is automatic.
The question is whether the *restricted* UBT spectrum (only modes allowed by
gauge consistency + unitarity of Θ) satisfies crossing symmetry for a *unique* k.

Concretely, test:
1. With full winding tower (free boson, k → ∞): crossing satisfied?
2. With only j = 0, 1/2 primaries (SU(2)_1, k = 1): crossing satisfied?
3. With k = 2 (extra j = 1 primary): crossing satisfied?

**File**: `research_tracks/T3_ALPHA/bootstrap_step_m3_crossing.tex` (to be created)

**Acceptance criterion**: Crossing symmetry satisfied for one and only one value of k.

---

### Step M4: Test whether UBT field content forces SU(2)₁ / k = 1

**Goal**: Apply the UBT constraint — only the winding modes consistent with
N_eff = 12 and the Dirac quantisation condition are present — and determine
which k is forced.

**Method**:
1. List the UBT-allowed primary operators using the mode decomposition from
   `canonical/n_eff/step1_mode_decomposition.tex`.
2. Compute the OPE coefficients for each allowed operator.
3. Check whether the OPE coefficients are consistent with a WZW model at level k.
4. Determine the unique k (or show k is not unique).

**Key observable**: The OPE coefficient C₁/₂,₁/₂,₀ (spinor × spinor → identity)
is fixed to C = 1/(k+2)^{1/2} in SU(2)_k.  If UBT forces a specific C, then k
is determined.

**File**: `research_tracks/T3_ALPHA/bootstrap_step_m4_ubt_content.tex` (to be created)

**Acceptance criterion**: Unique k = 1 forced, or explicit statement that k is not
uniquely forced (route rejected).

---

### Step M5: Reject route if k remains free

**Goal**: If steps M1–M4 do not produce a unique k, declare the modular bootstrap
route exhausted and record the obstruction.

**Rejection criterion** (any one sufficient):
- k is not constrained (free parameter)
- Multiple values of k are consistent with the UBT spectrum
- The 4-point function requires a circular input (α, m_e) to close

**Action on rejection**:
- Record the obstruction in `research_tracks/T3_ALPHA/alpha_status_report.md`
- Declare T3_ALPHA time-boxed
- Redirect effort: 15% T3_ALPHA maintenance, 85% T1_GR + T2_GAUGE writing
- Activate Layer2 coding paper (see `research_tracks/T3_ALPHA/fallback_layer2_outline.md`)

---

## 5. File Checklist

Files to create during this time-box:

| File | Status | Purpose |
|------|--------|---------|
| `research_tracks/T3_ALPHA/bootstrap_step_m1_conformal.tex` | To create | Conformal invariance of S[Θ] on T² |
| `research_tracks/T3_ALPHA/bootstrap_step_m2_4point.tex` | To create | 4-point function computation |
| `research_tracks/T3_ALPHA/bootstrap_step_m3_crossing.tex` | To create | Crossing symmetry test |
| `research_tracks/T3_ALPHA/bootstrap_step_m4_ubt_content.tex` | To create | UBT field content vs. k values |
| `experiments/alpha_core_repro/bootstrap_crossing_check.py` | To create | Numerical crossing check (if needed) |

---

## 6. Decision Gate

| Date | Milestone |
|------|-----------|
| 2026-04-28 | Plan committed; Step M1 begins |
| 2026-05-05 | M1 complete (conformal invariance verified or blocked) |
| 2026-05-12 | M2 complete (4-point function explicit) |
| 2026-05-19 | M3 complete (crossing symmetry tested for k = 1, 2, ∞) |
| 2026-05-26 | M4 complete — verdict: k=1 proved / k free / route rejected |

**Gate outcome**:

| Result | Action |
|--------|--------|
| k = 1 proved (unique, no circular input) | Draft α⁻¹_bare = 137 paper; update `canonical/alpha/alpha_best_route.tex` Step 5 to PROVED |
| k free or route blocked | Declare T3_ALPHA time-boxed; activate Layer2 paper; update `ALPHA_PROGRESS_REPORT.md` |

---

## 7. Success Criteria

A successful completion of this plan satisfies ALL of the following:

- [ ] No hidden fitting: k = 1 not assumed, forced by crossing symmetry
- [ ] No missing references: all bootstrap step files created and committed
- [ ] One clean α derivation chain: `ALPHA_BEST_ROUTE.tex` updated with Step 5 proved
- [ ] Clear yes/partial/no verdict recorded in `ALPHA_PROGRESS_REPORT.md` by 2026-05-26
- [ ] Circular inputs remain marked: δ = 0.036 [CIRC], R_ψ via m_e [SE], physical α correction [CIRC]

---

## 8. References

| Document | Content |
|----------|---------|
| `ALPHA_BEST_ROUTE.tex` | Best-candidate derivation chain; status banner |
| `ALPHA_PROGRESS_REPORT.md` | Full T3_ALPHA progress; 27+ exhausted approaches |
| `canonical/alpha/alpha_best_route.tex` | Formal LaTeX derivation (canonical source) |
| `research_tracks/T3_ALPHA/assumptions_audit.md` | Circularity audit of all 12 assumptions |
| `research_tracks/T3_ALPHA/fallback_layer2_outline.md` | Layer2 paper plan (fallback) |
| `canonical/n_eff/step1_mode_decomposition.tex` | UBT mode decomposition (operator content) |
| `canonical/appendices/appendix_alpha_geometry.tex` | V_eff, n* = 137, prime stability |
| `canonical/interactions/B_base_derivation_complete.tex` | B_base partial derivation |
| `DERIVATION_INDEX.md §Fine Structure Constant` | Full approach inventory (27+ documented) |
