<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# STEERING_MEMO_AFTER_PRIORITIES_PR.md

**Role**: Strict scientific steering committee  
**Date**: 2026-04-27  
**Branch context**: `copilot/sanity-patch-after-priorities-2026-update`  
**Verification basis**: Direct file inspection + `git show --stat HEAD`

---

## Section 1 — Truth Check: What the Last PR Actually Did

### Verified commit

```
35db20c — docs: add PRIORITIES_2026.md — strategic research priorities for UBT next phase
1 file changed, 644 insertions(+), 0 deletions(-)
```

**The last PR touched exactly one file: `PRIORITIES_2026.md` (root level).**  
Nothing else was modified, renamed, or deleted.

### What it improved

| Improvement | Evidence |
|---|---|
| Single authoritative, dated priority ranking (10 priorities, April 2026) | `PRIORITIES_2026.md §2` |
| Honest maturity table per sector (algebra, GR, SM, QM, α, lepton, Higgs, CMB) | `PRIORITIES_2026.md §1.1` |
| Near-breakthrough identification: SM gauge paper publishable now | `PRIORITIES_2026.md §Near-Breakthrough Alert` |
| Concrete 90-day roadmap (May–July 2026, three papers) | `PRIORITIES_2026.md §5` |
| Explicit "Stop-Doing" list (8 items) with actionable directives | `PRIORITIES_2026.md §6` |
| Directive to freeze CMB coding fingerprint track (STOP-2, Priority 10) | `PRIORITIES_2026.md §6, §2 P10` |
| Honest documentation of 27+ exhausted B_base routes | `PRIORITIES_2026.md §4 OHP-1` |
| Clear Dead-End declaration for Weinberg angle from ℂ⊗ℍ alone | `PRIORITIES_2026.md §4 OHP-3` |

### What it did NOT touch

The following pre-existing issues were **not addressed** by this PR:

| Untouched item | Location | Consequence |
|---|---|---|
| Competing priorities doc (Jan 2026) | `docs/RESEARCH_PRIORITIES.md` | Now has two authority sources |
| Competing priorities YAML | `docs/research_priorities.yaml` | Machine-readable priorities out of sync |
| `biquaternion_time.tex` header contradiction | `canonical/fields/biquaternion_time.tex` lines 1–4 | Header says "Status: Canonical" but body says "deprecated" |
| CMB coding section label in DERIVATION_INDEX | `DERIVATION_INDEX.md` line 489 | Still reads "Experimental (Strong)" and "Canonical fingerprint" |
| Acceptance percentage estimates in Section 3 | `PRIORITIES_2026.md §3` | Predicting journal acceptance rates (e.g., "70–80%") is not evidence-based |
| Missing explicit proof-file references in flagships | `PRIORITIES_2026.md §3` | Flagship claims lack canonical citation paths |

---

## Section 2 — Previous Review Corrections

The problem statement that triggered this branch listed several claimed issues.
Below is an accurate audit of each claim against repository reality.

### Claim: file to modify is `canonical/THEORY/math/fields/biquaternion_time.tex`

**INCORRECT.** That path does not exist.  
**Correct path**: `canonical/fields/biquaternion_time.tex`  
*(verified: `ls canonical/fields/` → `biquaternion_algebra.tex  biquaternion_time.tex  theta_field.tex`)*

### Claim: biquaternion_time.tex declares T_B as canonical

**PARTIALLY CORRECT — but the issue is older than this PR.**  
The file header (lines 1–4) still reads `% Status: Canonical - DO NOT DUPLICATE`.  
However, the body of the same file (Historical Note section, Symbol Standardization table,
Simplification section) already correctly states that T_B is "deprecated/historical" and that
τ = t+iψ is canonical.  
This internal self-contradiction is a **pre-existing issue that predates the PRIORITIES_2026 PR**.  
`canonical/CANONICAL_DEFINITIONS.md §1` and `canonical/AXIOMS.md §AXIOM B` already correctly
define τ = t+iψ as canonical and explicitly declare T_B deprecated. The contradiction is
isolated to the header of one file.

### Claim: docs/RESEARCH_PRIORITIES.md and docs/research_priorities.yaml are competing authority docs

**CORRECT — and this is a pre-existing issue that the PR worsened.**  
`docs/RESEARCH_PRIORITIES.md` is dated "Last Updated: February 9, 2026" and contains
a different 5-priority structure.  `docs/research_priorities.yaml` mirrors the same structure.  
These predate PRIORITIES_2026.md and were not authored by this PR.  The PR added a third
authority level without deprecating the existing two.

### Claim: acceptance probability estimates (e.g., "70–80%") need to be removed

**CORRECT — and these were introduced by this PR.**  
`PRIORITIES_2026.md §3` Flagship tables contain rows such as:

```
| Chance of success (paper accepted) | **High** (70–80%) |
| Chance of success | **Low** (15–25%) |
```

Predicting journal acceptance rates is not evidence-based and invites criticism.
These should be replaced with reviewer-risk categories (low/medium/high).
This is a **new issue introduced by this PR**, not pre-existing.

### Claim: CMB coding track needs to be marked as "frozen research track"

**CORRECT — partially done in PRIORITIES_2026.md but NOT in DERIVATION_INDEX.md.**  
PRIORITIES_2026.md correctly states STOP-2 and Priority 10 (freeze/archive the track).  
However, `DERIVATION_INDEX.md` line 489 still reads:

```
## Layer 2 Coding Fingerprints (L2S and L2T) — L2S confidence: Experimental (Strong)
```

And line 499:

```
| L2S: Hamming (8,4,4) state fingerprint | ⭐ Canonical fingerprint |
```

The label "Canonical fingerprint" and "Experimental (Strong)" directly contradict the
freeze directive in PRIORITIES_2026.md. This mismatch is a **pre-existing issue** that
the PR's STOP-2 directive now highlights without resolving.

### Claim: flagship proof-file references are missing

**CORRECT — introduced by this PR.**  
Section 3 of PRIORITIES_2026.md makes flagship claims (e.g., "proofs exist") without
citing the canonical source files. DERIVATION_INDEX.md does contain these paths; the
flagship tables do not. This is a gap introduced by the PR.

---

## Section 3 — Priority Alignment with Repository Reality

For each top priority in PRIORITIES_2026.md:

| Priority | Aligned with repo | Evidence files | Realism (1–10) | Remain top priority? |
|---|---|---|---|---|
| **P1** — Write SM Gauge Paper | ✅ Yes | `canonical/su3_derivation/su3_from_involutions.tex` (Theorems G.A–G.D); `canonical/su3_derivation/step1_superposition_approach.tex`; `tools/verify_su3_superposition.py`; DERIVATION_INDEX §SM: "Proved [L0] ⭐ CANONICAL" | **9** | ✅ Yes |
| **P2** — Write GR Recovery Paper | ✅ Yes | `canonical/gr_closure/GR_chain_summary.tex` (Steps 1–5); `research_tracks/research/graviton_schwarzschild.tex` (Regge-Wheeler); `research_tracks/research/schwarzschild_from_theta.tex`; DERIVATION_INDEX §GR: "Proved [L1]" | **8** | ✅ Yes |
| **P3** — Write QM Emergence Paper | ✅ Yes | DERIVATION_INDEX §QM: Born rule proved, Dirac (massless) proved, FPE↔EL proved all sectors; gap S1 (diffusion coefficient) partially closed | **7** | ✅ Yes |
| **P4** — Close B_base Gap (new route) | ✅ Yes (problem real) | `canonical/interactions/B_base_derivation_complete.tex`; `docs/PROOFKIT_ALPHA.md §5`; DERIVATION_INDEX: 27+ dead ends documented | **4** — correctly placed after papers | ✅ Yes, at P4 |
| **P5** — Zerilli Even-Parity Graviton | ✅ Yes | `research_tracks/research/graviton_schwarzschild.tex §8.2`; off-diagonal V₀₁ gap identified | **7** | ✅ Yes |
| **P6** — Hecke/Lepton Non-CM Search | ✅ Partial | `experiments/research_tracks/three_generations/step6_nonCM_search.tex`; `nonCM_search_results.json`; LMFDB/SageMath access pending | **6** — requires external tool access | ✅ Yes |
| **P7** — Resolve R_ψ Two-Scale | ✅ Yes | `research_tracks/research/r_factor_two_loop.tex §9`; `docs/STATUS_ALPHA.md §8.4` | **5** | ✅ Yes |
| **P8** — Fermionic Statistics / Spin | ✅ Yes | DERIVATION_INDEX §QM: Grassmannian measure proved [L1]; Noether charge on soliton: next step | **7** | ✅ Yes |
| **P9** — Mirror Sector Falsifiability | ✅ Partial | DERIVATION_INDEX §Hecke: p=139 mirror vacuum documented; mass spectrum not computed | **5** | ✅ Yes, at P9 |
| **P10** — Freeze CMB Coding Track | ✅ Yes (directive correct) | DERIVATION_INDEX §L2: no first-principles derivation; algebraic connection not established | **9** — freeze is the right call | ✅ Yes |

**Overall assessment of PRIORITIES_2026.md**: The priority document is **genuinely well-calibrated**.
The ranking accurately reflects the theoretical maturity demonstrated in DERIVATION_INDEX.md
and the canonical/ source files. The near-breakthrough identification (SM gauge paper) is
supported directly by DERIVATION_INDEX.md. The stop-doing list is conservative and evidence-backed.

---

## Section 4 — Pre-Existing Repository Issues

These issues exist in the current snapshot, **regardless of the PRIORITIES PR**:

### Issue 1 — `canonical/fields/biquaternion_time.tex` header contradiction (pre-existing)

**Location**: `canonical/fields/biquaternion_time.tex` lines 1–4  
**Problem**: Header says `% Status: Canonical - DO NOT DUPLICATE` but body (Historical Note,
Symbol Standardization, Simplification sections) says T_B is "deprecated/historical extension"  
**Impact**: Low (AXIOMS.md and CANONICAL_DEFINITIONS.md are correct; this file is a secondary reference)  
**Fix**: One-line change — update header status to `% Status: Historical/Deprecated`  

### Issue 2 — Dual competing priority systems (pre-existing, worsened by PR)

**Locations**: `docs/RESEARCH_PRIORITIES.md` (Feb 2026, 5-priority structure) and
`docs/research_priorities.yaml` (Mar 2026, machine-readable) vs. `PRIORITIES_2026.md` (Apr 2026, 10-priority)  
**Problem**: Three authority documents with different structures and no deprecation notices  
**Impact**: Medium — automated tooling or new contributors will receive inconsistent guidance  
**Fix**: Add a dated deprecation header to `docs/RESEARCH_PRIORITIES.md` and `docs/research_priorities.yaml`
pointing to PRIORITIES_2026.md as the canonical source  

### Issue 3 — DERIVATION_INDEX CMB section label conflicts with STOP-2 (pre-existing)

**Location**: `DERIVATION_INDEX.md` line 489  
**Problem**: Section header says `L2S confidence: Experimental (Strong)` and line 499 labels
L2S Hamming (8,4,4) as `⭐ Canonical fingerprint`  
This directly contradicts PRIORITIES_2026.md STOP-2 ("No new CMB fingerprint experiments")
and Priority 10 ("Archive and Freeze")  
**Impact**: Medium — DERIVATION_INDEX is a reference document; the mismatch signals the
fingerprint track is still live when PRIORITIES says it is frozen  
**Fix**: Update section header to `Frozen Research Track — see PRIORITIES_2026.md §STOP-2`;
relabel L2S fingerprint from "Canonical fingerprint" to "Frozen Research Track fingerprint"  

### Issue 4 — Acceptance percentage estimates in PRIORITIES_2026.md Section 3 (introduced by PR)

**Location**: `PRIORITIES_2026.md §3` — all flagship assessment tables  
**Problem**: Rows like `| Chance of success (paper accepted) | **High** (70–80%) |`
predict journal acceptance rates as numeric percentages; this is not evidence-based and
invites methodological criticism  
**Impact**: Low-Medium — document is internal; if shared externally the percentages look speculative  
**Fix**: Replace `(70–80%)`, `(65–75%)`, `(30–40%)`, etc. with reviewer-risk categories:
`reviewer-risk: low`, `reviewer-risk: medium`, `reviewer-risk: high`  

### Issue 5 — Flagship claims in PRIORITIES_2026.md lack proof-file citations (introduced by PR)

**Location**: `PRIORITIES_2026.md §3` Flagship #1 and #2 assessment tables  
**Problem**: Tables say "proofs exist" and "results are technically solid" without citing
the canonical source files. A reviewer cannot independently verify the claim.  
**Impact**: Low-Medium — easy to fix; the paths exist in DERIVATION_INDEX.md  
**Fix for Flagship #1**: Add under the table:  
  > **Proof files**: `canonical/su3_derivation/su3_from_involutions.tex` (Theorems G.A–G.D),
  > `canonical/su3_derivation/step1_superposition_approach.tex`,
  > `tools/verify_su3_superposition.py`  
  > **Assumptions**: (1) Confinement remains a Clay Millennium Problem — UBT claims structural
  > argument only, not full proof. (2) Weinberg angle sin²θ_W is a declared Dead End (OHP-3).
  > (3) Chirality (Gap C1) is conditional on minimal coupling.

**Fix for Flagship #2**: Add under the table:  
  > **Proof files**: `canonical/gr_closure/GR_chain_summary.tex` (Steps 1–5),
  > `research_tracks/research/schwarzschild_from_theta.tex` (Schwarzschild),
  > `research_tracks/research/graviton_schwarzschild.tex` (Regge-Wheeler)  
  > **Assumptions**: (1) Zerilli even-parity graviton open (§8.2 off-diagonal V₀₁ gap).
  > (2) Off-shell compact M⁴ open. (3) Metric uniqueness outside A_UBT admissible class unproved.

### Issue 6 — Some AXIOMS.md cross-references point to moved paths (pre-existing)

**Location**: `canonical/AXIOMS.md §Cross-References`  
**Problem**: References include `consolidation_project/appendix_FORMAL_emergent_metric.tex`
and `consolidation_project/appendix_R_GR_equivalence.tex` — these paths may reside under
`ARCHIVE/archive_legacy/` after the truth-refresh commit (#455)  
**Impact**: Low (axioms themselves are correct; only cross-reference paths may be stale)  
**Fix**: Verify paths exist; update references if moved  

---

## Section 5 — Top 5 Next Actions for the Next 30 Days

Ranked by scientific leverage, not governance overhead.

### Action 1 — Write and submit the SM Gauge Structure paper *(highest leverage)*

**Why**: This is a zero-parameter mathematical theorem that is already proved and unpublished.
DERIVATION_INDEX confirms `Proved [L0] ⭐ CANONICAL` at both SU(3) routes.
No new derivation is needed — only writing.  
**How**: Draft from `canonical/su3_derivation/` + `canonical/interactions/`;
target *Journal of Mathematical Physics* or *Letters in Mathematical Physics*  
**Time**: 6–8 weeks to submittable draft  
**Governance cost**: Zero  

### Action 2 — Deprecate the old priority documents

**Why**: `docs/RESEARCH_PRIORITIES.md` and `docs/research_priorities.yaml` now compete
with PRIORITIES_2026.md. New contributors or automated tools will receive conflicting signals.  
**How**: Add a two-line deprecation header to each:
```
> **SUPERSEDED**: This document is superseded by PRIORITIES_2026.md (2026-04-27).
> Retained for historical reference only.
```  
**Time**: 15 minutes  
**Governance cost**: Zero  

### Action 3 — Fix biquaternion_time.tex header (one line)

**Why**: `canonical/fields/biquaternion_time.tex` header says "Status: Canonical — DO NOT DUPLICATE"
while its own body and AXIOMS.md say T_B is deprecated. This is a factual error in one comment line.  
**How**: Change line 4 from `% Status: Canonical - DO NOT DUPLICATE` to
`% Status: Historical/Deprecated — canonical time is τ = t+iψ (see AXIOMS.md §AXIOM B)`  
**Time**: 2 minutes  
**Governance cost**: Zero  

### Action 4 — Update DERIVATION_INDEX CMB section to "Frozen Research Track"

**Why**: Line 489 of DERIVATION_INDEX.md says "Experimental (Strong)" and labels the
L2S Hamming fingerprint as "Canonical fingerprint". This directly contradicts PRIORITIES_2026.md
STOP-2 and Priority 10. The index is consulted by any contributor evaluating what to work on.  
**How**: Change section header at line 489 to:
```
## Layer 2 Coding Fingerprints (L2S and L2T) — ⚠️ FROZEN RESEARCH TRACK (see PRIORITIES_2026.md §STOP-2)
```
Change line 499 label from `⭐ Canonical fingerprint` to `[Frozen Research Track]`  
**Time**: 5 minutes  
**Governance cost**: Zero  

### Action 5 — Replace acceptance percentages with reviewer-risk categories in PRIORITIES_2026.md

**Why**: Quantitative acceptance estimates ("70–80%") are not evidence-based and are the
most likely target of criticism if the document is shared externally.  
**How**: Replace each `(70–80%)`, `(65–75%)`, etc. with `(reviewer-risk: low)`,
`(reviewer-risk: medium)`, or `(reviewer-risk: high)` respectively; add proof-file citations
to Flagship #1 and #2 assessment tables (see Issue 5 above).  
**Time**: 20 minutes  
**Governance cost**: Zero  

---

## Section 6 — Do Not Waste Time On

### 6.1 — Maintaining competing governance documents

`docs/RESEARCH_PRIORITIES.md`, `docs/research_priorities.yaml`, and `PRIORITIES_2026.md`
should not be kept in sync as parallel systems. Deprecate the older two (Action 2 above),
then let PRIORITIES_2026.md be the single source of truth. Do not create a fourth.

### 6.2 — New CMB / Hamming / Gray fingerprint experiments

PRIORITIES_2026.md STOP-2 is correct and evidence-backed. The L2S/L2T track lacks an
algebraic first-principles derivation from UBT axioms. The statistical signal does not
constitute a UBT prediction. No new experiments, no new Reed-Solomon branches.

### 6.3 — B_base via any of the 27 documented dead-end routes

DERIVATION_INDEX documents 27+ approaches explicitly. Re-attempting variants of
KK sum, zeta function, Hausdorff, NCG spectral triple, instanton action, two-loop
β-function, Weyl anomaly, Dynkin index, Cartan-Killing, canonical norm, two-scale R_ψ,
or flat-T³ heat kernel will not close Gap G3-k. Only a genuinely new route qualifies.

### 6.4 — Weinberg angle sin²θ_W from ℂ⊗ℍ algebra alone

OHP-3 is a declared Dead End. The mixing ratio g/g' is not fixed by the biquaternion
algebra. This limitation must be stated in every publication; it should not be an
active research item.

### 6.5 — Consciousness / psychon / Reed-Solomon cosmology in physics outputs

These are correctly isolated in `speculative_extensions/`. They should not appear in
arXiv submissions, internal physics papers, or future PRIORITIES documents. Any agent
or contributor who injects these into core documents should be flagged immediately.

### 6.6 — Creating additional governance files to resolve governance problems

The correct fix for the duplicate priority docs is a two-line deprecation header (Action 2),
not a fourth priorities document, a synthesis YAML, or a meta-governance framework.
Adding governance overhead to manage governance overhead is a known failure mode.

---

## Overall Assessment

**PRIORITIES_2026.md is a net positive contribution.** The ranking is well-calibrated
against DERIVATION_INDEX.md reality. The near-breakthrough identification is correct
and actionable. The stop-doing list is conservative and warranted.

**The three issues it did not fix** (competing priority docs, biquaternion_time.tex header,
DERIVATION_INDEX CMB label) are pre-existing and require minor targeted edits — not
a new document.

**The two issues it introduced** (acceptance percentages, missing proof-file citations) are
low-severity and easily corrected in a follow-up patch.

**No imaginary regressions detected.** The SM gauge structure result was provably ready
before this PR; the PR correctly identified it as the highest-value action. The GR and QM
paper recommendations are consistent with DERIVATION_INDEX evidence. All 10 priorities
are defensible.

---

*Compiled from direct file inspection: `git show --stat HEAD`, `PRIORITIES_2026.md`,
`DERIVATION_INDEX.md` (lines 489, 499), `canonical/AXIOMS.md §AXIOM B`,
`canonical/CANONICAL_DEFINITIONS.md §1`, `canonical/fields/biquaternion_time.tex` (lines 1–4),
`docs/RESEARCH_PRIORITIES.md`, `docs/research_priorities.yaml`, `canonical/README.md`*

---

**Author**: Copilot steering agent  
**On behalf of**: Ing. David Jaroš  
**License**: CC BY-NC-ND 4.0
