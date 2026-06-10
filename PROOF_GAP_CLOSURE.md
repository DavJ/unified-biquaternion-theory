<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# PROOF_GAP_CLOSURE.md — T1_GR Flagship

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T1_GR — General Relativity Recovery  
**Purpose**: Complete inventory of all missing steps, exact files to patch, and
risk ranking.  Used to drive gap-closure work before arXiv submission.  
**Sources**: `research_tracks/T1_GR/proof_gap_list.md`,
`research_tracks/T1_GR/GR_PAPER_OUTLINE.md`,
`research_tracks/T1_GR/theorem_chain.tex`, `MILESTONE_REVIEW.md`

---

## Overview

The GR recovery chain has nine proved steps and zero hard blockers.  All
remaining gaps are [L2] (open problems that do not block submission) or
editorial (notation, write-up completeness).  GAP-Z is now PROVED [L1].

| Gap ID | Short name | Type | Blocks paper? | Priority |
|--------|-----------|------|--------------|----------|
| ED-1 | Notation unification | Editorial | **No** (affects readability) | Critical for draft |
| ED-2 | Regge-Wheeler source file | Write-up | **No** | High |
| ED-3 | Schwarzschild numerical table | Write-up | **No** | High |
| GAP-10 | Off-shell Θ-only closure | [L2] open problem | **No** | State as open |
| GAP-Z | Zerilli equation (even-parity) | **PROVED [L1]** — `canonical/gr_closure/zerilli_derivation.tex` | N/A — closed | — |
| GAP-M | Compact M⁴ off-shell | [L2] open problem | **No** | Mention briefly |
| GAP-Q | Quantum GR (path integral) | [L3] long-term | **No** | Mention as future work |
| GAP-C | Cosmological solutions (FRW) | [L2] lower priority | **No** | Mention as future work |

---

## ED-1: Notation Unification

**Type**: Editorial  
**Blocks paper**: No — blocks readable draft  
**Risk**: Medium — inconsistent notation across source files causes reviewer confusion

### What needs to be done

The canonical source files in `canonical/gr_closure/` use slightly different
notation conventions in different files:

| Inconsistency | Files affected | Fix |
|--------------|---------------|-----|
| $\mathcal{G}_{\mu\nu}$ vs $G_{\mu\nu}$ (biquaternionic vs Einstein tensor) | `step1_metric_bridge.tex`, `GR_chain_summary.tex` | Use $\mathcal{G}$ for biquaternionic, $G$ for Einstein throughout |
| $\hat{S}$ vs $S_\Theta$ vs $S_{\mathrm{total}}$ | `step3_einstein_with_matter.tex`, `step4_offshell_Tmunu.tex` | Standardise to $S_{\mathrm{total}}$ for full action, $S_\Theta$ for matter part |
| Normalisation $\mathcal{N}$: defined differently in steps 1 and 5 | `step1_metric_bridge.tex`, `step3_einstein_with_matter.tex` | Align with Definition~\ref{def:theta_field} in `theorem_chain.tex` |
| $\tau$ vs $\tau_\mathbb{C}$ for complex time | Various | Use $\tau \in \mathbb{C}$ throughout |

### Exact files to patch

1. `canonical/gr_closure/step1_metric_bridge.tex` — normalisation $\mathcal{N}$
2. `canonical/gr_closure/GR_chain_summary.tex` — $G$ vs $\mathcal{G}$ notation
3. `canonical/t_munu/step3_einstein_with_matter.tex` — action notation
4. `canonical/t_munu/step4_offshell_Tmunu.tex` — action notation
5. `research_tracks/T1_GR/theorem_chain.tex` — master file; adopt as notation standard

**Estimated effort**: 1 week  
**Action**: Do notation pass on all five files before drafting Sections 2–5.

---

## ED-2: Regge-Wheeler Source File

**Type**: Write-up gap  
**Blocks paper**: No  
**Risk**: Low — the result is proved; the canonical source file needs to be identified
and verified clean

### What needs to be done

Theorem 5.1 (Regge-Wheeler, `theorem_chain.tex` §6c) references the linearised
GR analysis in `canonical/gr_closure/` but the exact source file for this derivation
is not specified.  Before writing Section 5 of the paper:

1. Locate the canonical source file for the odd-parity linearised UBT analysis.
   Candidate: `canonical/gr_closure/` — scan for linearised perturbation files.
2. Verify that the Regge-Wheeler potential $V_{\mathrm{RW}}(r)$ matches the
   standard form (Regge-Wheeler 1957, eq. 9).
3. If the source file is in `research_tracks/` rather than `canonical/`, move or
   copy the clean version to `canonical/gr_closure/linearised_gravity.tex`.

### Exact files to check

- `canonical/gr_closure/` — scan for perturbation/linearised files
- `research_tracks/T1_GR/` — check for linearised GR analysis
- If absent: write `canonical/gr_closure/linearised_gravity.tex` from scratch
  (the derivation is standard; the biquaternionic specialisation is the new content)

**Estimated effort**: 3–5 days  
**Action**: Locate source during Sections 4–5 drafting phase (Week 4–6).

---

## ED-3: Schwarzschild Numerical Table

**Type**: Write-up gap  
**Blocks paper**: No  
**Risk**: Low — code exists; table formatting needed

### What needs to be done

`tools/verify_schwarzschild_theta.py` produces the Schwarzschild metric
components from the $\Theta_0$ ansatz and compares with the exact formula.
Appendix C of the paper requires:

1. Run `tools/verify_schwarzschild_theta.py` and capture the output.
2. Format as a LaTeX table: columns = $r/M$, $g_{tt}^{\mathrm{UBT}}$,
   $g_{tt}^{\mathrm{exact}}$, relative error; approximately 6–8 representative
   radii.
3. Include a brief description of the numerical method and the
   normalisation convention.

### Exact files to patch

- `tools/verify_schwarzschild_theta.py` — verify it runs and the output format
  is correct; add tabular output mode if not already present
- `research_tracks/T1_GR/GR_PAPER_OUTLINE.md` §Appendix C — cross-check output
  table format

**Estimated effort**: 1–2 days  
**Action**: Complete during Week 6.

---

## GAP-10: Off-Shell Θ-Only Closure

**Type**: [L2] open problem — does not block paper  
**Canonical source**: `research_tracks/T1_GR/proof_gap_list.md §GAP-10`,
`canonical/gr_closure/step2_theta_only_closure.tex`

### Precise statement

The on-shell result is proved: for $\Theta\in\mathcal{A}_{\mathrm{UBT}}$
satisfying its Euler-Lagrange equation, the variation map
$J = \delta g^{\mu\nu}/\delta\Theta$ is non-degenerate and the Einstein
equations follow.

What is missing: global non-degeneracy of $J$ for **all** $\Theta$ in the
full off-shell field space, not only for on-shell solutions.

### Known obstructions

1. **Rank mismatch**: $\mathrm{Re}(\nabla^\dagger\nabla\Theta)$ is rank-0;
   $G_{\mu\nu}$ is rank-2.  Direct identification fails; multi-step chain required.

2. **Topology**: Global injectivity of $\Theta\to g[\Theta]$ requires
   $H^2(M^4,\mathbb{Z})$ analysis of the $\Theta$-bundle.  Depends on topology of $M^4$.

3. **Non-perturbative existence**: A fixed-point theorem in Sobolev space is
   required for well-posedness of $\delta\hat{S}/\delta\Theta = 0$ off-shell.

### What would close this gap

- Compute the cohomology of the $\ker J$ sheaf over $M^4$.
  If $H^1(M^4, \ker J) = 0$, global non-degeneracy follows from the local result.
- Or: prove the set of degenerate $\Theta$ (where $\det J = 0$) has measure zero
  in any reasonable function space (irrelevance for path integral).

### Risk for paper

**Zero risk**.  The on-shell result is self-contained.  GAP-10 is a question
about quantum field completeness.  It will be stated as an open problem in
Section 6 with the full obstruction map above.  No reviewer can reasonably
reject the paper on this basis if it is honestly stated.

---

## GAP-Z: Zerilli Equation (Even-Parity Graviton)

**Status**: **PROVED [L1]** (closed 2026-05-13)
**Canonical proof**: `canonical/gr_closure/zerilli_derivation.tex`

Both graviton polarisation sectors are now proved at [L1]:
- Odd-parity (Regge-Wheeler): `papers/UBT_GR_Submission.tex` Theorem 5.1
- Even-parity (Zerilli): `canonical/gr_closure/zerilli_derivation.tex`

See `WHAT_IS_PROVED.md §G15` and `STATUS.md §T1_GR` for the canonical record.
This section is retained for historical reference only.

---

## GAP-M: Compact M⁴ Off-Shell Closure

**Type**: [L2] open problem — does not block paper  
**Mention**: Brief remark in Section 6 or Section 7.

For compact spacetimes (e.g., $M^4 = T^4$ or $S^4$), the off-shell closure
proof of GR recovery requires additional topological arguments (existence of
global sections of the $\Theta$-bundle).  The non-compact case (Minkowski,
Schwarzschild exterior) is the main focus and is the physically relevant case
for classical GR.

**Action for paper**: One paragraph in Section 6 noting that the compact case
is not addressed; no additional work required.

---

## GAP-Q: Quantum GR

**Type**: [L3] long-term — not relevant to this paper  
**Mention**: One sentence in Section 7 outlook.

Path-integral quantisation of UBT requires GAP-10 closure, a well-defined
measure on the $\Theta$ field space, and renormalisability/UV completion.
Out of scope for the present paper.

---

## GAP-C: Cosmological Solutions

**Type**: [L2] lower priority  
**Mention**: Outlook, Section 7.

FRW and de Sitter metrics have not been derived from an explicit $\Theta$ ansatz.
The Friedmann equations should follow from Steps 1–5 applied to an FRW metric,
but the explicit biquaternionic construction is missing.

**Action for paper**: Note in Section 7 outlook.  Priority 2 for next paper after
submission of T1_GR.

---

## Risk Ranking

| Gap | Severity if unresolved | Probability of causing rejection | Recommended action |
|-----|----------------------|--------------------------------|-------------------|
| ED-1 (notation) | Medium — readability | Low (but reviewer complaint likely) | **Do first, Week 1** |
| ED-2 (Regge-Wheeler source) | Low — completeness | Low | Weeks 4–6 |
| ED-3 (numerical table) | Low — appendix only | Very low | Week 6 |
| GAP-10 | None — on-shell proved | Very low if stated honestly | State as open; no work needed |
| GAP-Z | **PROVED [L1]** — closed | **Zero** — both graviton sectors closed | No action needed |
| GAP-M | None | Zero | Brief mention |
| GAP-Q | None | Zero | One sentence |
| GAP-C | None | Zero | Mention in outlook |

**No gap has a non-negligible probability of causing rejection if handled as described.**

---

## Work Plan for Gap Closure

| Week | Action | Files |
|------|--------|-------|
| 1 | ED-1: Complete notation unification pass | `step1_metric_bridge.tex`, `GR_chain_summary.tex`, `step3_einstein_with_matter.tex`, `step4_offshell_Tmunu.tex`, `theorem_chain.tex` |
| 4–6 | ED-2: Locate/clean Regge-Wheeler source file | `canonical/gr_closure/` scan; write `linearised_gravity.tex` if needed |
| 6 | ED-3: Run numerical script; produce LaTeX table | `tools/verify_schwarzschild_theta.py` |
| 7–9 | Draft Section 6 (open problems) with GAP-10 obstruction map | Adapted from `research_tracks/T1_GR/proof_gap_list.md`; GAP-Z is now proved — omit from open-problems section |
| 10–11 | Internal consistency check: verify all cross-references, all \ref resolve | All paper source files |

---

## What Is Not a Gap

The following are sometimes listed as concerns but are **not gaps** in the
GR recovery paper:

- **Fine structure constant α**: Unrelated to GR recovery.  Not mentioned.
- **Fermion masses**: Unrelated.  Not mentioned.
- **Gauge sector**: Separate paper (T2_GAUGE).  Not mentioned except in
  introduction as a motivation for the broader UBT program.
- **Dark matter/p-adic extensions**: Speculative; separate track.
- **Consciousness / CCT**: Entirely separate, speculative extension.
  Not mentioned.
