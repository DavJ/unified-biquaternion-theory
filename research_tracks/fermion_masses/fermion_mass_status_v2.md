<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Fermion Mass Sector: Honest Status Map — v2

**Author**: Ing. David Jaroš  
**Date**: 2026-05-10  
**Status**: RESEARCH TRACK — honest audit of fermion mass programme  
**Predecessor**: `ARCHIVE/archive_legacy/deprecated/research_tracks/fermion_mass_program.md`  
**Source files**: `ARCHIVE/archive_legacy/consolidation_project/appendix_E2_fermion_masses.tex`,
  `research_tracks/legacy_theory_variants/unified_biquaternion_theory/fermion_mass_derivation_complete.tex`

---

## 1. Purpose

This document provides a precise, honest map of the current state of the
fermion mass programme in UBT.  It supersedes `fermion_mass_program.md`
(2025) by:

1. Classifying each parameter as CLEAN [L0/L1], SEMI-EMPIRICAL [SE], or OPEN.
2. Stating the KK-mismatch theorem explicitly (see §3).
3. Listing the minimal new inputs needed to predict the full SM fermion mass spectrum.

No new physics is claimed.  No parameter is presented as derived unless a
proof exists with an explicit source citation.

---

## 2. The Mass Formula

The UBT fermion mass formula (from
`fermion_mass_derivation_complete.tex` §3):

```
m(n) = A · n^p − B_m · n · ln(n)
```

where:
- `n` = fermion mode number (winding number on S¹_ψ)
- `A` = mass scale factor (dimension: MeV)
- `p` = power exponent (dimensionless)
- `B_m` = logarithmic correction coefficient (dimension: MeV)

### Parameter classification

| Parameter | Value | Classification | Notes |
|-----------|-------|----------------|-------|
| Formula structure `n^p - B_m·n·ln n` | — | CLEAN [L1] | Follows from V_eff structure (same as α sector); see `alpha_best_route.tex` |
| `A` (mass scale) | ~0.511 MeV (from electron) | [SE] | Fitted to m_e; no derivation from S[Θ] |
| `p` (power) | ~2 (from formula) | [SE] | Plausible from kinetic term; not derived |
| `B_m` (log coefficient) | ≈ −14.099 MeV | [SE] | Fitted parameter; **not related to B_phenom ≈ 46.3 (α sector)** |
| `m_e ≈ 0.511 MeV` (0.22% accuracy) | reproduced | [SE] | Formula works; parameters are fitted |
| `m_μ/m_e ≈ 206.8` | not reproduced | OPEN | No UBT prediction exists |
| `m_τ/m_μ ≈ 16.8` | not reproduced | OPEN | No UBT prediction exists |
| Quark masses (`m_u, m_d, m_s, ...`) | not reproduced | OPEN | Partial treatment only |

**Critical note on B_m vs B_phenom**: The parameter `B_m ≈ −14.099 MeV`
(fermion mass sector, dimension MeV) is **completely distinct** from
`B_phenom ≈ 46.298` (α-sector, dimensionless).  They arise from different
sectors of the theory and should not be confused.

---

## 3. The KK-Mismatch Theorem

### Statement

> **KK-Mismatch Theorem** (from `ROADMAP.md §Phase 4`):  
> The torus approach to deriving fermion mass ratios m_μ/m_e, m_τ/m_μ from
> the Kaluza-Klein (KK) spectrum of the UBT field on a product torus
> T³ × S¹_ψ encounters a structural obstruction.  The KK mode spacing on a
> uniform torus gives mass ratios of order `n²` for integer `n`, which
> does not match the observed ratios (206.8, 16.8) for any simple integer assignment.

### Proof status

The proof of the KK-mismatch theorem is referenced in
`ARCHIVE/archive_legacy/deprecated/research_tracks/fermion_mass_program.md`
but the explicit proof text has not been located in the repository in a
self-contained form.  Possible locations:

- `ARCHIVE/archive_legacy/consolidation_project/appendix_E2_fermion_masses.tex`
- `research_tracks/legacy_theory_variants/unified_biquaternion_theory/fermion_mass_derivation_complete.tex`

**Action required**: If a self-contained proof of the KK-mismatch theorem
exists in the repository, it should be extracted and placed in
`canonical/mass_sector/kk_mismatch_theorem.tex`.  If no proof exists,
this should be opened as a canonical gap using
`.github/ISSUE_TEMPLATE/canonical_gap.yml`.

### Consequence

The KK-mismatch theorem (if proved) rules out the simplest route to mass
ratios.  Alternative approaches would need to involve:

- Non-uniform torus (shape moduli fixed by a separate mechanism)
- Yukawa couplings from the VEV structure of Θ (analogous to Standard Model Higgs)
- Running of effective mass via RG flow from the UBT beta function

None of these approaches are currently at [L0/L1] level in UBT.

---

## 4. Classification Table: All Fermion Mass Parameters

| Parameter | SM value | UBT status | Classification |
|-----------|----------|------------|----------------|
| Electron mass `m_e` | 0.511 MeV | Reproduced with 0.22% (semi-empirical) | [SE] |
| Muon mass `m_μ` | 105.66 MeV | Not reproduced | OPEN |
| Tau mass `m_τ` | 1776.86 MeV | Not reproduced | OPEN |
| Up quark `m_u` | ~2.2 MeV | Partial treatment only | OPEN |
| Down quark `m_d` | ~4.7 MeV | Partial treatment only | OPEN |
| Strange quark `m_s` | ~96 MeV | Not reproduced | OPEN |
| Charm quark `m_c` | ~1.27 GeV | Not reproduced | OPEN |
| Bottom quark `m_b` | ~4.18 GeV | Not reproduced | OPEN |
| Top quark `m_t` | ~172 GeV | Not reproduced | OPEN |
| Neutrino masses | ~eV scale | Not derived | OPEN |
| Mass scale `A` | fitted | Fitted to m_e | [SE] |
| Log coefficient `B_m` | ≈ −14.099 MeV | Fitted | [SE] |
| Power `p` | ~2 | Plausible, not derived | [SE] |
| CKM matrix angles | experimental | Not derived | OPEN |
| PMNS matrix angles | experimental | Not derived | OPEN |
| CP violation phases | experimental | Not derived | OPEN |

---

## 5. Minimal Inputs to Predict the Full SM Fermion Mass Spectrum

To predict the full SM fermion mass spectrum from UBT, the following new
inputs (currently absent from the theory) would be required:

1. **Yukawa coupling matrix derivation**: A mechanism for deriving the
   3×3 Yukawa coupling matrices `y_u, y_d, y_e` from the UBT field Θ.
   Currently these are 9+9+9 = 27 free parameters in the Standard Model.

2. **Higgs VEV from S[Θ]**: The Higgs vacuum expectation value
   `v = 246 GeV` sets the overall mass scale.  Its derivation from the
   UBT action (Gap EW-2) is open.

3. **SSB mechanism**: The mechanism by which `SU(2)_L × U(1)_Y → U(1)_EM`
   arises dynamically from the UBT potential `V(Θ)`.

4. **Resolution of KK-mismatch theorem**: If the torus approach is to be
   pursued for mass ratios, the obstruction identified by the KK-mismatch
   theorem must be resolved (either by relaxing the uniform torus assumption
   or by an alternative mass-generation mechanism).

5. **Running mass at the right scale**: Even if a mass formula is found,
   it must be matched to the renormalization-group running of the SM
   fermion masses from the GUT scale (if applicable) to the physical scale.

---

## 6. What Is Well-Founded (and Should Not Be Over-Claimed)

The following results are on solid footing:

- **Formula structure** [L1]: The `n^p - B_m·n·ln n` form follows from the
  same one-loop effective potential structure as the α sector.  This is a
  genuine UBT result (not experimental curve-fitting of the functional form).

- **Three generations** [L0]: `N_gen = 3` from `dim_ℝ(Im ℍ) = 3` is proved
  independently of mass values.  See `WHAT_IS_PROVED.md` (T2_GAUGE row).

- **Electron mass reproduction** [SE]: m_e = 0.511 MeV is reproduced to 0.22%
  with fitted parameters.  This is a consistency check, not a prediction.

---

## 7. Honest Summary for WHAT_IS_PROVED.md

The following rows should be added or updated in `WHAT_IS_PROVED.md`:

| Item | Level | Status |
|------|-------|--------|
| Formula structure `m(n) = A·n^p − B_m·n·ln n` | [L1] | Proved (given V_eff structure) |
| `N_gen = 3` | [L0] | Proved |
| `m_e` reproduced to 0.22% | [SE] | Semi-empirical (A, p, B_m fitted) |
| `m_μ/m_e`, `m_τ/m_μ` | OPEN | No UBT prediction |
| Quark masses | OPEN | Partial treatment only |
| CKM/PMNS matrices | OPEN | Not derived |
| KK-mismatch theorem proof | OPEN | Source not confirmed — see §3 |

---

## 8. Next Steps for the Fermion Mass Programme

1. **Locate or re-derive the KK-mismatch theorem proof** (§3).
   If found, extract to `canonical/mass_sector/kk_mismatch_theorem.tex`.
   If not found, file a canonical gap issue.

2. **Separate formula structure (proved) from parameter fitting (semi-empirical)**
   in all future documents.  Never present B_m as derived.

3. **Defer CKM/PMNS matrices** to a future programme that addresses the
   Yukawa coupling origin.

4. **Do not add fermion mass claims to papers/UBT_Gauge_Submission.tex**
   beyond the explicit "deferred" statement in §8 of that paper.

---

*This document is part of the research track and must not be promoted to
`canonical/` without a proof that closes Gap EW-2 and resolves the
KK-mismatch obstruction.*
