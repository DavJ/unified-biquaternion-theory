# GitHub Copilot Instructions for Unified Biquaternion Theory
<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- Last updated: 2026-06-10 (v51) -->

## 1. Repository Overview

This repository contains the **Unified Biquaternion Theory (UBT)**, a theoretical
physics framework that derives General Relativity, Standard Model gauge structure,
and quantum mechanics from a single biquaternionic field Θ defined over complex
time τ = t + iψ.

**Author**: Ing. David Jaroš  
**License**: CC BY-NC-ND 4.0 (theory files) · MIT (code/scripts) — see §2  
**Primary language**: LaTeX, with supporting Python scripts  
**Single source of truth for theory status**: `STATUS_OF_UBT.md`

The core field equation is:

```
∇†∇Θ(q,τ) = κ𝒯(q,τ)
```

which reduces to Einstein's field equations R_μν − ½g_μν R = 8πG T_μν in the
real limit. UBT **generalizes and embeds** GR; it does not replace or contradict it.

Language rules:
- ✅ "UBT generalizes GR", "UBT embeds GR", "recovers Einstein's equations"
- ❌ "alternative to GR", "replacement for GR", "contradicts GR"

---

## 2. License and Copyright — CRITICAL

**These rules are non-negotiable. Never weaken, relax, or silently change them.**

### 2.1 General rules

- **NEVER** remove, relax, or downgrade any license statement.
- **NEVER** change the author name "Ing. David Jaroš" or copyright year.
- **NEVER** suggest a more permissive license than what is already present.
- When in doubt about any licensing or copyright change: **STOP** and wait for
  explicit user instruction.

### 2.2 Current licensing state

| Content type | License |
|---|---|
| Theory files (`.tex`, `.md` documents) | **CC BY-NC-ND 4.0** |
| Code and scripts (`.py`, `.sh`, etc.) | **MIT** |
| Files in `ARCHIVE/` or `original_release_of_ubt/` | Treat as read-only archival; do not modify |

Earlier commits may carry CC BY 4.0. Do not propagate that to new files.

### 2.3 Header templates

**Theory files (LaTeX, Markdown):**
```latex
% © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
%
% This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives
% 4.0 International License (CC BY-NC-ND 4.0).
%
% License History: Earlier drafts (up to v0.3) were released under CC BY 4.0.
% From v0.4 onward, all material is released under CC BY-NC-ND 4.0 to protect
% the integrity of the theoretical work during ongoing academic development.
%
% See LICENSE.md for full license text.
```

**Code files (Python, shell):**
```python
# Copyright (c) 2026 Ing. David Jaroš
# Licensed under the MIT License
# See LICENSE file in the repository root for full license text
```

### 2.4 Prohibited actions

- Do NOT insert CC BY 4.0 headers into new files.
- Do NOT change "NC" (NonCommercial) or "ND" (NoDerivatives) to more permissive variants.
- Do NOT propose GPL/BSD/Apache license changes.
- Do NOT remove copyright notices.
- Do NOT change author attribution to any name other than "Ing. David Jaroš".

---

## 3. Proof-Level Label System

Every claim in the repository carries a label. **Never upgrade a label without
explicit instruction from the user.** In particular, never change `[MC]` to `[L1]`
on your own initiative.

| Label | Meaning |
|---|---|
| `[L0]` | Algebraic identity or tautology; follows by direct computation, no proof needed |
| `[L1]` | Formal theorem with a complete proof in a canonical source file |
| `[L2]` | Open problem; identified and stated, does not block current papers |
| `[MC]` | Motivated Candidate — argument is given and structurally sound, but not a complete formal proof |
| `[STD]` | Follows from standard mathematics or physics (cited reference) |
| `[OBS]` | Observed or numerically confirmed; not yet derived from S[Θ] |
| `[NUM]` | Numerical result only; no analytical proof |
| `OPEN` | Gap with no current candidate solution |
| `CONDITIONAL` | Result holds given an unresolved assumption; assumption must be stated |

Source of truth for label definitions: `DERIVATION_STATUS_STANDARD.md`.

---

## 4. Active Repository Structure

The live working tree. Legacy directories (`consolidation_project/`,
`unified_biquaternion_theory/`) are preserved for archival provenance but are
**not** the active working location for new derivations.

```
.
├── .github/
│   ├── copilot-instructions.md     ← this file
│   ├── latex_roots.txt             ← list of standalone .tex files for CI
│   └── workflows/                  ← GitHub Actions (LaTeX build, CI, etc.)
├── canonical/                      ← ALL active proof source files
│   ├── algebra/                    ← biquaternion algebra foundations
│   ├── alpha/                      ← T3_ALPHA: fine structure constant
│   ├── chirality/                  ← chirality / no-W_R derivation chain
│   │   ├── step3_gap_C1_resolution.tex   ← Gap C1 Step 3 [L1]
│   │   └── step4_no_wr_derivation.tex    ← Gap C1 Step 4 [MC] — NEW v49
│   ├── geometry/                   ← geometry, connections, ASD Weyl
│   ├── gr_closure/                 ← T1_GR proof chain
│   │   ├── step1_metric_bridge.tex
│   │   ├── step2_nondegeneracy.tex
│   │   ├── step3_signature_theorem.tex
│   │   ├── step3_einstein_with_matter.tex
│   │   ├── GR_chain_summary.tex
│   │   ├── zerilli_derivation.tex        ← Zerilli [L1]
│   │   └── frw_cosmological_solutions.tex ← GAP-C [L1]+[MC] — NEW v49
│   ├── interactions/               ← SM gauge structure
│   ├── n_eff/                      ← N_eff derivations
│   └── su3_derivation/             ← SU(3) from involutions
├── papers/                         ← submission-ready manuscripts
│   ├── UBT_GR_Submission.tex       ← T1_GR canonical manuscript (submit-ready)
│   └── UBT_Gauge_Submission.tex    ← T2_GAUGE draft paper
├── research_tracks/                ← exploratory and in-progress tracks
│   ├── T1_GR/
│   ├── T3_ALPHA/
│   ├── EW/
│   └── quantum_ubt/
├── tools/                          ← Python validation scripts
│   └── verify_schwarzschild_theta.py
├── tests/                          ← automated tests (pytest)
├── DATA/                           ← Planck, WMAP data manifests
├── reports/                        ← review documents, audit reports
├── docs/                           ← generated PDFs, comparison tables
├── speculative_extensions/         ← FROZEN speculative content (see §9)
├── ARCHIVE/                        ← read-only historical record
├── STATUS_OF_UBT.md                ← SINGLE SOURCE OF TRUTH for track statuses
├── WHAT_IS_PROVED.md               ← complete proved-results inventory
├── DERIVATION_INDEX.md             ← index of all derivation files + levels
├── ROADMAP.md                      ← execution-control layer, locked sequencing
├── DERIVATION_STATUS_STANDARD.md  ← label definitions
├── CLAIMS_MATRIX.md                ← cross-track claims
└── CHANGELOG.md
```

---

## 5. Theory Track Status (as of v51, 2026-06-10)

This is a summary for Copilot orientation. The authoritative record is
`STATUS_OF_UBT.md`. When in conflict, `STATUS_OF_UBT.md` governs.

### T1_GR — General Relativity Recovery

**Status: SUBMIT READY**

The five-step chain Θ → g → Γ → R → G_μν = 8πGT_μν is complete at [L1].

| Claim | Level | Source |
|---|---|---|
| Metric g_μν from Θ | [L1] | `canonical/gr_closure/step1_metric_bridge.tex` |
| Non-degeneracy det(g) ≠ 0 | [L1] | `canonical/gr_closure/step2_nondegeneracy.tex` |
| Lorentzian signature from AXIOM-B | [L1] | `canonical/gr_closure/step3_signature_theorem.tex` |
| Einstein equations from Hilbert variation | [L1] | `papers/UBT_GR_Submission.tex §3` |
| T_μν symmetric, ∇^μT_μν = 0 | [L1] | `canonical/geometry/stress_energy.tex` |
| Schwarzschild metric (< 10⁻¹⁵ error) | [L1]+[NUM] | `tools/verify_schwarzschild_theta.py` |
| Regge-Wheeler equation (odd-parity graviton) | [L1] | `papers/UBT_GR_Submission.tex §5` |
| Zerilli equation (even-parity graviton) | [L1] | `canonical/gr_closure/zerilli_derivation.tex` |
| Flat FRW metric in UBT solution space | [L1] | `canonical/gr_closure/frw_cosmological_solutions.tex §2` |
| Friedmann equations from Steps 1–5 | [L1] | `canonical/gr_closure/frw_cosmological_solutions.tex §2` |
| Explicit FRW Θ-ansatz: g_ij = a(t)²δ_ij, solves ∇†∇Θ = κ𝒯_FRW on reduced ODE branch | [L1 conditional] — Thm frw_ansatz_l1; conditional on Friedmann branch + ODE system | `canonical/gr_closure/frw_cosmological_solutions.tex §3` |
| g_0i = 0 in comoving frame (GAP-C sub-gap) | **[L1 conditional]** — Lem 4.1; conditional on standard comoving-frame averaging | `canonical/gr_closure/frw_cosmological_solutions.tex §4` |
| GAP-10: off-shell Θ-only closure | [L2] open | Does not block submission; state in paper |

**Next action**: Submit `papers/UBT_GR_Submission.tex` to arXiv (gr-qc or math-ph).

### T2_GAUGE — Standard Model Gauge Structure

**Status: NEAR READY (85%)**

SU(3)×SU(2)_L×U(1)_Y derived from ℂ⊗ℍ with zero free parameters.

| Claim | Level | Source |
|---|---|---|
| ℂ⊗ℍ ≅ Mat(2,ℂ) ≅ Cl₁,₃(ℝ) | [L0] | `canonical/algebra/biquaternion_algebra.tex` |
| SU(3) from ℤ₂×ℤ₂×ℤ₂ involutions | [L0] | `canonical/su3_derivation/su3_from_involutions.tex` |
| Quarks in **3**, gluons in **8** | [L0] | `canonical/interactions/sm_gauge.tex` |
| SU(2)_L from left norm-preserving action | [L0] | `canonical/interactions/sm_gauge.tex` |
| SU(2)_L acts on left-chiral doublets (Gap C1 Step 3) | [L1] | `canonical/chirality/step3_gap_C1_resolution.tex` |
| SU(2)_R geometric decoupling via ψ-parity (Gap C1 Step 4) | [MC] | `canonical/chirality/step4_no_wr_derivation.tex §3 Thm 3.1` |
| Loophole 1: P_ψ-even SU(2)_R coupling to n<0 sector observationally decoupled | [L1 conditional on Step 1 Lem 4] | `canonical/chirality/step4_no_wr_derivation.tex Cor 3.2` |
| Loophole 2: no light SU(2)_R-doublet scalar in minimal S[Θ] | [L1 conditional on minimality of S[Θ]] | `canonical/chirality/step4_no_wr_derivation.tex §4 Lem no_doublet` |
| Loophole 3: SU(2)_R in n≠0 KK tower acquires mass ≥ M_KK → decouples | [STD] | `canonical/chirality/step4_no_wr_derivation.tex §4 Prop 4.3` |
| Full algebraic exclusion of SU(2)_R (OP-S4) | **[L1 conditional]** — all three loopholes closed; conditional on Step 1 Lem 4 + minimality of S[Θ] | `canonical/chirality/step4_no_wr_derivation.tex §4` |
| U(1)_Y from right scalar phase | [L0] | `canonical/interactions/sm_gauge.tex` |
| U(1)_EM from ψ-cycle phase | [L0] | `canonical/interactions/qed.tex` |
| Three generations from ψ-winding | [L0] | `canonical/n_eff/` |
| Hypercharge quantisation from Dirac condition | [L0] | `canonical/qed_phi_const/appendix_alpha_geometry.tex §1` |
| Weinberg angle — pure algebra route | **DEAD END** (no-go proved) | Keep dead-end statement in T2 paper §6 |
| Weinberg angle — EW-1b (EW1+RG) route | CONDITIONAL | Blocked on Gap C2 Step 1 |
| W/Z masses, Higgs VEV (EW-2) | DEFERRED | Separate Higgs paper |
| Fermion masses, Yukawa (Y2) | OPEN | — |
| Dynamical confinement | OPEN | Clay Millennium Problem |

**Next action**: Submit T2_GAUGE paper after T1_GR submission. Target arXiv week 8–10.

### T3_ALPHA — Fine Structure Constant

**Status: CONDITIONAL — blocked on Gap G137-B**

Integer α⁻¹_bare = 137 is proved conditional on B = B_phenom. Full derivation
(137.036) requires Gap G137-B.

| Claim | Level | Source |
|---|---|---|
| n*(B_phenom) = 137 for B_phenom ≈ 46.298 | [L1] conditional | `canonical/alpha/` |
| Prime stability of n* | [L0] | — |
| N_eff^twist = 12 (SU(2)-twist route) | [L1] | `canonical/n_eff/step2_AUDIT.tex` |
| N_eff^loop = 3 (scalar loop) | [L1] | `canonical/n_eff/step2_AUDIT.tex` |
| twist = loop identification | **OPEN/[MC]** | `canonical/n_eff/step2_AUDIT.tex` |
| B_Ram = 12^(3/2)·(2η)^(1/4) from SU(2) twist | [L0]+[MC] | v42 result |
| η⁻²·θ₃·θ₄² = 2η(i) algebraic identity | [L0] | v42 result |
| B_phenom ≈ 46.298 derived from S[Θ] | **OPEN — Gap G137-B** | — |
| Routes A3, A4 | **KILLED** (exhaustive proof) | `reports/failed_routes_graveyard.md` |
| Weinberg pure-algebra route (EW-1) | **DEAD END** | — |

**Decision gate**: 4-week modular bootstrap on Gap G137-B (A_PRIME route only).
If G137-B not solved (~70–80% probability): publish conditional integer-137 note,
downgrade T3_ALPHA to "structural evidence", redirect effort to T2_GAUGE.

---

## 6. Active Open Gaps — Priority Order

These are the gaps to work on. Do not open new derivation tracks while
gaps 1–4 are unresolved (ROADMAP governance rule).

| Priority | Gap ID | Description | Blocker for | File |
|---|---|---|---|---|
| 1 | **G137-B** | Derive B_phenom ≈ 46.298 from S[Θ] without α input | T3_ALPHA paper | `canonical/alpha/ALPHA_MASTER_STATUS.md` |
| 2 | **N_eff loop-counting** | Close multiplicity-factor audit in loop branch; identify twist = loop | T3_ALPHA | `canonical/n_eff/step2_AUDIT.tex` |
| 3 | **Gap C2 Step 1** | Fermion hypercharge assignments from UBT structure | EW-1b, anomaly cancellation | `research_tracks/EW/` |
| 4 | **EW-1b** | First-principles EW+RG closure for sin²θ_W ≈ 0.231 | T2_GAUGE completeness | `research_tracks/EW/weinberg_angle_ew1_rg.tex` |
| 5 | **FRW ODE system** | Solve ẍ+3Hẋ+(1/R_ψ²)x = κ𝒯 for f(t) from first principles; verify consistency with Friedmann equations | FRW ansatz full [L1] (remove conditionality) | `canonical/gr_closure/frw_cosmological_solutions.tex §3` |
| 6 | **OP-S4 minimality** | Prove minimality assumption of S[Θ] is self-consistent (no extension forced by anomaly cancellation or unitarity) | OP-S4 unconditional | `canonical/chirality/step4_no_wr_derivation.tex §4` |
| 7 | **GAP-10** | Off-shell Θ-only closure (global non-degeneracy of J) | Long-term [L2] | `canonical/gr_closure/step2_theta_only_closure.tex` |

---

## 7. Derivation Work Instructions

Both D1 (OP-S4 Loophole 2 — Lemma no_doublet) and D2 (FRW ansatz field-equation
matching — Theorem frw_ansatz_l1) from the v50 task list were completed in v51.
The two highest-priority remaining targets are now G137-B and the N_eff
loop-counting audit. Below are precise instructions.

### 7.1 Task D1 — Gap G137-B: derive B_phenom from S[Θ] without α input

**Target files**: `canonical/alpha/ALPHA_MASTER_STATUS.md` and
`research_tracks/T3_ALPHA/mellin_insertion_B.tex`

**The problem**: The integer-137 result is proved conditional on B = B_phenom ≈ 46.298.
The Ramanujan form B_Ram = 12^(3/2)·(2η)^(1/4) ≈ 46.2809 is an [OBS] observation.
The algebraic identity η⁻²·θ₃·θ₄² = 2η(i) is established [L0]. The missing step:
derive B_phenom from S[Θ] evaluated at n* = 137 without using α as an input.

**Active route (A_PRIME — modular bootstrap)**:
Evidence: μ(Γ₀(137))/3 ≈ 46.00 (0.64% from B_phenom). Target: derive
B = μ(Γ₀(n*))/3 from S[Θ] evaluated at winding number n* = 137.

Step 1: Write out the modular-bootstrap argument in `mellin_insertion_B.tex`.
The claim to prove: the S[Θ] partition function on T³ at τ = i, evaluated at
winding number n*, produces a Mellin coefficient equal to μ(Γ₀(n*))/3 at the
prime attractor n* = 137.

Step 2: The η⁻²·θ₃·θ₄² = 2η(i) identity [L0] gives the zero-mode normalization.
The remaining factor from B₀ = 8π to B_phenom is ≈ 1.84. Compute the one-loop
and two-loop corrections to the Mellin normalization in the SU(2)-twist sector
(reference: v41 results — 1-loop = 0.185, 2-loop [STD] = 0.231).

Step 3: If μ(Γ₀(137))/3 = B₀ · (loop correction factor) derivable from S[Θ],
state as a Theorem [L1]. The gate: does the loop-corrected B equal B_phenom to
algebraic precision [L0/L1], or only numerically [NUM]?

**If bootstrap fails (4-week time-box exhausted)**:
Write a formal no-go memo in `ALPHA_MASTER_STATUS.md`: state precisely which
step cannot be completed and what additional input would be required. Downgrade
T3_ALPHA from CONDITIONAL to STRUCTURAL EVIDENCE. Do not leave the route in a
partially-attempted state.

**Success criterion**: Either a Theorem [L1] deriving B = B_phenom from S[Θ],
or a formal no-go with precise obstruction. Update STATUS_OF_UBT.md T3_ALPHA
section same-day.

### 7.2 Task D2 — N_eff loop-counting: close twist = loop identification

**Target file**: `canonical/n_eff/step2_AUDIT.tex`

**The problem**: Two routes give N_eff = 12:
- SU(2)-twist route: N_eff^twist = 12 [L1]
- Scalar loop counting: N_eff^loop = 3 [L1]

The identification twist = loop is [OPEN/MC]. Without it, B₀ = 8π has two
separate justifications that may not be compatible, and Task D1 is ambiguous
about which N_eff to use.

Step 1: Read `step2_AUDIT.tex`. Identify the precise statement of the N_charge
double-counting issue.

Step 2: Determine whether N_eff^twist and N_eff^loop count the same physical
degrees of freedom. Write a Proposition: either
(a) "N_eff^twist = N_eff^loop because [explicit isomorphism]" — level [L1], or
(b) "They count different objects; their numerical equality is explained by
[symmetry argument]" — with justification at [L1].

Step 3: If (b), state explicitly which N_eff enters B₀ in the A_PRIME route
and justify from S[Θ].

**Success criterion**: N_eff audit status upgraded from OPEN/[MC] to [L1] or
[L1 conditional] in `step2_AUDIT.tex`. Entry in `WHAT_IS_PROVED.md` updated.
STATUS_OF_UBT.md T3_ALPHA section updated same-day.

### 7.3 Task D3 — Reduce conditionality in GAP-C and OP-S4

Both GAP-C (FRW ansatz) and OP-S4 (no-W_R) are now [L1 conditional]. This
task tracks work to remove or justify their explicit conditions.

**GAP-C FRW ODE consistency** (`canonical/gr_closure/frw_cosmological_solutions.tex §3`):
The two ODEs from Theorem frw_ansatz_l1:
```
f̈ + 3Hf̊ + (1/R_ψ²)f = κ𝒯₀(t)
ä + 3Hȧ + (1/R_ψ²)a = κ𝒯₁(t)
```
Write a Lemma: "The ODE for a(t) is consistent with the Friedmann equation
ȧ² = (8πG/3)ρa² if and only if 𝒯₁(t) = [explicit expression in ρ, p, R_ψ]."
If this holds identically for any perfect fluid, the conditionality on the
a(t)-sector becomes automatic. The f(t) ODE remains a condition on the
scalar envelope; state the residual conditionality precisely.

**OP-S4 minimality** (`canonical/chirality/step4_no_wr_derivation.tex §4`):
Write a Remark: "The minimality assumption (no scalar beyond Θ in S[Θ]) is
consistent with anomaly cancellation (T2_GAUGE paper §anomaly) and with unitarity
of the ψ-winding spectrum (Step 1). It is not forced by an external consistency
requirement but is the Occam choice for the minimal theory." This documents the
conditionality honestly for T2_GAUGE paper reviewers without asserting new claims.

### 7.4 Task D4 — Update status tracking files for v51 results

Apply the following updates if not already present (v51 should have done all of
these; verify and correct if any are missing):

**`WHAT_IS_PROVED.md`**:
```
G18   | FRW Θ-ansatz: g_ij=a²δ_ij and ∇†∇Θ=κ𝒯 on reduced ODE branch | [L1 conditional] | frw_cosmological_solutions.tex §3 Thm frw_ansatz_l1
OP-S4 | Full SU(2)_R exclusion (all 3 loopholes closed)                | [L1 conditional] | step4_no_wr_derivation.tex §4
```

**`STATUS_OF_UBT.md`** T2_GAUGE table — OP-S4 row:
```
| Full algebraic exclusion of SU(2)_R (OP-S4) | [L1 conditional] | step4_no_wr_derivation.tex §4 |
```

**`STATUS_OF_UBT.md`** T1_GR table — G18 row:
```
| FRW Θ-ansatz: g_ij=a²δ_ij and ∇†∇Θ=κ𝒯 on ODE branch | [L1 conditional] | frw_cosmological_solutions.tex §3 |
```

### 7.5 Task D5 — CI workflow: new latex_build.yml structure (v51)

The CI workflow was substantially rewritten in v51 (`latex_build.yml`). It now
has three jobs: `lint` → `compile` and `compile_standalone_roots` (parallel,
both need lint) → `publish_pdfs` (needs both, master-branch push only).

**lint job**: runs `scripts/lint_complex_time_usage.py` (continue-on-error —
warns only) and `scripts/test_symbolic_alpha.py` (must pass — blocks compile).
Any new Python scripts in `scripts/` must not break `test_symbolic_alpha.py`.

**compile job**: builds only `canonical/UBT_canonical_main.tex`. Fails if
`Undefined control sequence` found in logs. Extra packages: `physics`, `braket`.

**compile_standalone_roots job**: matrix build over exactly:
```
canonical/chirality/step4_no_wr_derivation.tex
canonical/gr_closure/frw_cosmological_solutions.tex
```
Extra packages installed: `mdframed booktabs mathtools hyperref xcolor physics braket`.

**publish_pdfs job**: commits `docs/pdfs/UBT_canonical_main.pdf` back to master.
Only runs when both compile jobs succeed on a master push.

**When adding a new standalone canonical `.tex` file**, add it to **both**:
1. `.github/latex_roots.txt`
2. The `matrix.root` list in the `compile_standalone_roots` job of `latex_build.yml`

---

## 8. Status Governance Rules

These rules apply to all edits to status-tracking files.

1. `STATUS_OF_UBT.md` is the **single source of truth**. Every track status change
   must be mirrored there on the same day as the change.

2. Never upgrade a proof level (`[MC]`→`[L1]`, `OPEN`→`[MC]`, etc.) without
   explicit instruction from the user.

3. No new derivation tracks or alpha routes may be opened while the ROADMAP
   Top-10 items 1–4 are unresolved.

4. Dead-end routes stay dead. Routes A3, A4 (alpha) and the pure-algebra Weinberg
   route (EW-1) are **killed** — do not reopen them.

5. Speculative content (consciousness/psychons, CTCs, Theta Resonator, p-adic
   dark sector) remains **frozen** in `speculative_extensions/`. Do not expand,
   reference as active research, or move to core directories.

6. The `ARCHIVE/` directory is **read-only**. Do not modify, move, or delete
   its contents.

---

## 9. Speculative Extensions — Frozen

The following tracks are frozen indefinitely and must not be expanded, referenced
as active research, or moved to core directories:

| Topic | Location | Status |
|---|---|---|
| Complex Consciousness Theory / Psychons | `speculative_extensions/complex_consciousness/` | FROZEN — no mathematical closure |
| Closed Timelike Curves (CTCs) | `speculative_extensions/appendices/` | FROZEN — speculative, no experimental anchor |
| Theta Resonator | `speculative_extensions/` | FROZEN |
| p-adic dark sector | `research_tracks/p_universes/` | DEFERRED — beyond 21-day window |

When editing any file, do not add references to these topics in core theory
sections. They belong only in their designated directories.

---

## 10. LaTeX Conventions

### 10.1 Standalone / included files

All canonical derivation files use the `\ifdefined\INCLUDEMODE` guard pattern
so they compile both standalone and via `\input{}` inclusion:

```latex
\ifdefined\INCLUDEMODE
\else
  \documentclass[12pt,a4paper]{article}
  % ... preamble ...
  \begin{document}
  \maketitle
\fi

% ... content ...

\ifdefined\INCLUDEMODE
\else
  \end{document}
\fi
```

New canonical theory files must follow this pattern.

### 10.2 Notation standards

| Symbol | Meaning | LaTeX |
|---|---|---|
| Θ | UBT fundamental field | `\Theta` |
| τ | Complex time τ = t + iψ | `\tau` |
| ψ | Imaginary time component | `\psi` |
| R_ψ | ψ-circle radius | `R_\psi` |
| P_ψ | ψ-parity operator ψ → −ψ | `P_\psi` |
| 𝒢_μν | Biquaternionic Einstein tensor | `\mathcal{G}_{\mu\nu}` |
| G_μν | Standard Einstein tensor | `G_{\mu\nu}` |
| S_total | Full UBT action | `S_{\mathrm{total}}` |
| S_Θ | Matter part of action | `S_\Theta` |
| 𝒩 | Normalisation factor in metric formula | `\mathcal{N}` |
| ℂ⊗ℍ | Biquaternion algebra | `\mathbb{C}\otimes\mathbb{H}` |
| ℬ | Biquaternion algebra (shorthand) | `\mathcal{B}` |

Inconsistencies to avoid across the GR chain files:
- Use `\mathcal{G}` for biquaternionic and `G` for Einstein tensor (not mixed)
- Use `S_{\mathrm{total}}` for full action, `S_\Theta` for matter part (not `\hat{S}`)
- Use `\tau \in \mathbb{C}` for complex time (not `\tau_\mathbb{C}`)
- Align `\mathcal{N}` definition with `theorem_chain.tex` Definition 1

### 10.3 Theorem environments

All canonical files use the standard set:

```latex
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
```

And four `mdframed` status boxes:

```latex
\newmdenv[backgroundcolor=yellow!20, linecolor=orange, linewidth=1.5pt]{gapbox}
\newmdenv[backgroundcolor=green!15, linecolor=green!60!black, linewidth=1.5pt]{resultbox}
\newmdenv[backgroundcolor=red!10, linecolor=red!60, linewidth=1.5pt]{deadendbox}
\newmdenv[backgroundcolor=blue!8, linecolor=blue!50, linewidth=1.5pt]{insightbox}
```

Use `gapbox` for open gaps, `resultbox` for closed results, `deadendbox` for
killed routes, `insightbox` for physical interpretation remarks.

### 10.4 Compilation

```bash
# Single file:
pdflatex -interaction=nonstopmode file.tex
pdflatex -interaction=nonstopmode file.tex   # second pass for references

# With bibliography:
pdflatex file.tex && bibtex file && pdflatex file.tex && pdflatex file.tex
```

CI compiles every file listed in `.github/latex_roots.txt` on every push/PR.
Always verify CI passes after adding or editing a `.tex` file.

---

## 11. Python Scripts

Scripts live in `tools/` (validation) and `tests/` (automated). They are
auxiliary to the LaTeX theory.

- Use numpy/scipy for numerics; no exotic dependencies without listing them in
  a comment header.
- Include a docstring explaining the theoretical basis of each function.
- Validate results against known limits (e.g., `verify_schwarzschild_theta.py`
  checks < 10⁻¹⁵ relative error against exact Schwarzschild).
- MIT license header on all code files.

---

## 12. Key Reference Files

| Question | File |
|---|---|
| What is the current status of every track? | `STATUS_OF_UBT.md` |
| What is proved at what level? | `WHAT_IS_PROVED.md` |
| What is the execution order and sequencing? | `ROADMAP.md` |
| Where is each derivation? | `DERIVATION_INDEX.md` |
| What does each proof level mean? | `DERIVATION_STATUS_STANDARD.md` |
| What claims span multiple tracks? | `CLAIMS_MATRIX.md` |
| What routes have been killed and why? | `reports/failed_routes_graveyard.md` |
| What notational inconsistencies need fixing? | `PROOF_GAP_CLOSURE.md §ED-1` |
| What are the open editorial gaps for T1_GR? | `PROOF_GAP_CLOSURE.md` |
| What are the current research priorities? | `docs/RESEARCH_PRIORITIES.md` (updated 2026-06-10) |

---

## 13. What Copilot Must Never Do

- Change any license, copyright line, or author attribution without explicit instruction.
- Upgrade a proof level label (`[MC]`→`[L1]`, etc.) without explicit instruction.
- Add content to `speculative_extensions/` or reference frozen speculative tracks
  in core theory files.
- Modify any file in `ARCHIVE/` or `original_release_of_ubt/`.
- Reopen killed routes (A3, A4, EW-1 pure-algebra Weinberg).
- Open new derivation tracks while ROADMAP items 1–4 are unresolved.
- Edit `STATUS_OF_UBT.md` without mirroring all status changes it introduces
  back into the same file in the same session.
- Commit generated PDFs — CI handles PDF generation.
- Use the author name "UBT Team" or any name other than "Ing. David Jaroš" in
  new files (some legacy consolidated documents use "UBT Team" — do not propagate this).
