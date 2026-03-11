# Explicit Gap Backlog — Audit Follow-Up (2026-03)

**Path**: `AUDITS/followup_gap_backlog_2026_03.md`  
**Date**: 2026-03-11  
**Authority**: Derived from audit report and repository review  
**Hard rules**: Keep negative and null results visible. Every gap must reference the
exact file(s) where it appears or where the fix should be applied.

---

## Overview

This document lists all substantive gaps identified by the 2026 repository audit that
have not yet been fully resolved.  Each gap has:
- A clear problem statement
- File references (exact paths)
- Current status
- Required action for closure

This backlog is **not** a list of problems to suppress — gaps that cannot be fixed
should be documented as open problems, not removed from sight.

---

## GAP-01: GR full Θ-only closure not proved

**Category**: Mathematical / derivation  
**Severity**: High — affects central claim of UBT

**Problem**: The claim that varying the action S[g[Θ], Θ] with respect to Θ *alone*
(without independently varying g) rigorously recovers Einstein's equations is not
fully proved.  The current argument (step2_theta_only_closure.tex, Theorem 1) holds
only on-shell and requires an injectivity assumption (the map Θ → g[Θ] must have no
kernel direction at the solution).  Off-shell injectivity is an open problem.

**What IS proved**: On-shell equivalence when the injectivity assumption holds.  
**What is NOT proved**: Off-shell or global injectivity; full non-perturbative
equivalence without the injectivity assumption.

**Files**:
- `consolidation_project/GR_closure/step2_theta_only_closure.tex` — theorem statement
- `reports/gr_recovery_final_status.md` — summary table

**Required action**:
- Ensure the theorem statement in step2 makes the injectivity assumption prominent
  in the main theorem box, not only in the caveat subsection.
- The status in summary files must be labelled `indicated` or `open (L2)`, not `proved`.
- A future task could attempt to bound the kernel of δg/δΘ globally.

**Current resolution**: Partial — injectivity gap is documented in `step2_theta_only_closure.tex`
Section 4 (On-Shell Injectivity), but prominence of this caveat could be increased.

**Status**: 🔶 partially addressed; full proof remains open.

---

## GAP-02: Signature theorem — failed Euclidean intermediate block

**Category**: Mathematical / proof structure  
**Severity**: Medium — internal proof has a failed sub-derivation that should be
clearly marked

**Problem**: In `step3_signature_theorem.tex`, the proof of Lemma (Signature of Q)
contains an intermediate block (lines 156–179 approx) where the naive scalar-part
computation yields a Euclidean form Q(v) = t² + x² + y² + z² (positive definite).
The text then says "the sign flip arises from the metric formula" and implies the
normalization 𝒩 carries the signature information.

This claim is **incorrect as stated**: rescaling by a positive scalar 𝒩 > 0 cannot
change the signature of a bilinear form.  The correct resolution is the Clifford
algebra argument in the following subsection (Theorem: Lorentzian signature from
Clifford embedding), which is valid.

**Risk**: A reader may take the intermediate (Euclidean) result at face value or be
confused about the role of 𝒩.

**Files**:
- `consolidation_project/GR_closure/step3_signature_theorem.tex` — Lemma proof block

**Required action**:
- Add a visible warning to the failed Euclidean derivation block labelling it as a
  "failed approach" that is kept for transparency, with a clear pointer to the
  correct Clifford proof.
- Ensure no prose implies that normalization alone fixes signature.
- The Clifford proof (Theorem: Lorentzian signature from Clifford embedding) is correct
  and should be presented as the authoritative result.

**Current resolution**: Not yet resolved — the failed block is present without
a clear "FAILED APPROACH" label.

**Status**: ❓ open — editorial fix needed.

---

## GAP-03: `canonical/geometry/curvature.tex` — projection commutes with products

**Category**: Mathematical correctness  
**Severity**: Medium

**Problem**: Line 85 of `canonical/geometry/curvature.tex` states:
> "This classical formula is valid because the real projection commutes with
> derivatives and products."

The claim that Re(·) commutes with **products** is **false in general** for
biquaternion-valued functions: Re(AB) ≠ Re(A) Re(B) in general.  The claim is
valid for:
- Linear operations: Re(A + B) = Re(A) + Re(B) ✓
- Scalar multiplication: Re(λA) = λ Re(A) for real λ ✓
- Derivatives of real-valued functions: Re(∂_μ f) = ∂_μ Re(f) ✓ (if ∂_μ is real)
- The specific case of real Christoffel symbols (derived from real metric): ✓

**Required action**:
- Replace the overly broad claim with an accurate statement covering only the valid
  cases (linearity and real derivatives).
- See: GR recovery and canonical geometry documents.

**Current resolution**: Not yet resolved.

**Status**: ❓ open — one-line fix needed.

---

## GAP-04: `T_munu_derivation/step3_einstein_with_matter.tex` — not labelled as
Hilbert variation

**Category**: Documentation / clarity  
**Severity**: Low-Medium

**Problem**: `step3_einstein_with_matter.tex` derives G_μν = 8πG T_μν by varying
S_total[g, Θ] with **g^μν** as an independent variable (Hilbert variation).  The
abstract says "Einstein equations derived, not asserted" but does not make explicit
that this is the **two-field** (g, Θ independently varied) approach, not the Θ-only
approach.

A reader could conflate this with the Θ-only closure result of step2, which is a
different and stronger (unproved) claim.

**Required action**:
- Add a note in the abstract or introduction that this is the Hilbert (metric
  variation) derivation with g treated as an independent field.
- Explicitly state that this is **not** the full Θ-only closure (which requires
  additional injectivity assumptions; see `step2_theta_only_closure.tex`).

**Current resolution**: Not yet resolved.

**Status**: ❓ open — clarification note needed.

---

## GAP-05: SU(2,2) candidate not fully classified

**Category**: Algebraic / classification  
**Severity**: Medium

**Problem**: Experiment e08 (`experiments/e08_lie_algebra_audit.py`) finds a
15-dimensional semisimple Lie algebra with Killing signature (8, 7, 0) from UBT
generators.  The report (`reports/e08_summary.md`) labels this a "STRONG INDICATION"
of su(2,2) but does not provide:
- A Cartan classification checking the root system against A₃ non-compact real forms
- An explicit generator-by-generator isomorphism to a standard su(2,2) basis
- A check that the particular 4×4 matrix embedding used is canonical

Without these, the identification remains indicated, not proved.

**Files**:
- `experiments/e08_lie_algebra_audit.py`
- `reports/e08_summary.md`
- `THEORY_COMPARISONS/penrose_twistor/su22_notes.md`
- `THEORY_COMPARISONS/penrose_twistor/STATUS.md` (new — documents status correctly)

**Required action**:
- In `e08_summary.md`: clearly separate exact results from conjectural identification.
- Add Cartan-style classification attempt (at minimum: compute rank, Cartan subalgebra
  dimension, check against A₃ Satake diagrams).
- Never write "proved isomorphism" until an explicit isomorphism is exhibited.

**Current resolution**: Partially addressed by `STATUS.md §3.1`.  e08_summary.md
still needs explicit separation of exact vs conjectural sections.

**Status**: 🔶 partially addressed — STATUS.md correct; e08_summary.md needs update.

---

## GAP-06: τ = t + iψ mapping to twistor geometry — open

**Category**: Conceptual / research  
**Severity**: Research gap (not an error)

**Problem**: The role of the imaginary time coordinate ψ in twistor or spinor-conformal
geometry is not understood.  Multiple candidates have been investigated; two are ruled
out; the others remain open.

**Files**:
- `THEORY_COMPARISONS/penrose_twistor/tau_phase_mapping.md` (new — documents candidates)

**Required action**: Ongoing research.  The gap is documented; no claim of resolution
should be made until a candidate is confirmed.

**Status**: ❓ open — documented in `tau_phase_mapping.md`.

---

## GAP-07: Fine-structure constant α — chain still semi-empirical

**Category**: Physical derivation  
**Severity**: Medium

**Problem**: The fine-structure constant baseline α⁻¹ = 137.000 (from Hopfion topology,
zero fitted parameters) is a genuine first-principles result.  However, the corrections
that bring α⁻¹ closer to the measured 137.036 involve structural corrections with
parameters that are motivated but not fully derived from first principles.

**Status in `CURRENT_STATUS.md`**: "~90% DERIVED" — this phrasing is appropriate but
must not be upgraded to "fully derived" without eliminating all fitted parameters.

**Files**:
- `CURRENT_STATUS.md` — status section
- `STATUS_ALPHA.md` (if present)
- `docs/status_legend.md` (new — defines semi_empirical status)

**Required action**:
- Use status label `semi_empirical` for the corrected α result.
- Reserve `proved` for the zero-parameter baseline only.
- Maintain this distinction in all status summaries.

**Status**: 🔶 partially addressed — `CURRENT_STATUS.md` wording is cautious but
could be made more precise using the canonical status labels.

---

## GAP-08: Fermion mass coefficients not first-principles

**Category**: Physical derivation  
**Severity**: Medium

**Problem**: Fermion mass ratios (lepton and quark masses) in UBT involve coefficients
that are fitted or motivated by pattern-matching, not derived from a first-principles
calculation.

**Status**: Honestly described in `FITTED_PARAMETERS.md` and `CURRENT_STATUS.md`.

**Required action**:
- Ensure no file calls the fermion mass derivation "proved" or "fully derived".
- Use `semi_empirical` label consistently.

**Status**: 🔶 partially addressed — check for any overclaims in summary files.

---

## GAP-09: Status claims inconsistent across files

**Category**: Documentation / consistency  
**Severity**: Low-Medium

**Problem**: Different files use different vocabularies for the same status level:
- "fully derived", "derived", "DERIVED", "proved", "obtained" — used inconsistently
- No canonical legend was defined until `docs/status_legend.md` (2026-03-11)

**Files to scan**:
- `README.md`
- `CURRENT_STATUS.md`
- `FITTED_PARAMETERS.md`
- `DERIVATION_INDEX.md`
- `THEORY_COMPARISONS/penrose_twistor/README.md`
- `THEORY_COMPARISONS/penrose_twistor/reports/e08_summary.md`

**Required action**:
- Use `docs/status_legend.md` as the reference for all future status labelling.
- In a future cleanup pass, align existing documents with the canonical labels.

**Status**: ❓ open — legend created; document alignment is future work.

---

## Resolution Tracking

| Gap | Description | Status | Last updated |
|-----|-------------|--------|--------------|
| GAP-01 | GR Θ-only closure not proved | 🔶 partial | 2026-03-11 |
| GAP-02 | Euclidean block in signature proof | ❓ open | 2026-03-11 |
| GAP-03 | Real projection over products claim | ❓ open | 2026-03-11 |
| GAP-04 | T_munu step3 not labelled Hilbert | ❓ open | 2026-03-11 |
| GAP-05 | su(2,2) candidate not classified | 🔶 partial | 2026-03-11 |
| GAP-06 | τ=t+iψ mapping to twistor open | ❓ open | 2026-03-11 |
| GAP-07 | α chain semi-empirical | 🔶 partial | 2026-03-11 |
| GAP-08 | Fermion mass coefficients fitted | 🔶 partial | 2026-03-11 |
| GAP-09 | Status labels inconsistent | ❓ open | 2026-03-11 |
