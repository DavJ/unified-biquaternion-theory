# GitHub Copilot Instructions for Unified Biquaternion Theory
<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- Last updated: 2026-06-11 (v54) -->

## 1. Repository Overview

**Author**: Ing. David Jaroš | **License**: CC BY-NC-ND 4.0 (theory) · MIT (code)
**Status source of truth**: `STATUS_OF_UBT.md`

Core field equation: `∇†∇Θ(q,τ) = κ𝒯(q,τ)` reduces to Einstein's equations in the real limit. UBT **generalizes and embeds** GR — never say "alternative to" or "replacement for" GR.

---

## 2. License and Copyright — CRITICAL

**Never weaken, relax, or silently change these rules.**

- NEVER remove or downgrade license statements, author name "Ing. David Jaroš", or copyright year.
- Theory files (`.tex`, `.md`): **CC BY-NC-ND 4.0**. Code (`.py`, `.sh`): **MIT**.
- Do NOT insert CC BY 4.0 headers. Do NOT change NC/ND to more permissive variants.
- `ARCHIVE/` is read-only. When in doubt: **STOP** and wait for explicit instruction.

**Theory file header:**
```latex
% © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
% Licensed under CC BY-NC-ND 4.0. See LICENSE.md.
```

---

## 3. Proof-Level Label System

**Never upgrade a label without explicit user instruction.**

| Label | Meaning |
|---|---|
| `[L0]` | Algebraic identity; follows by direct computation |
| `[L1]` | Formal theorem with complete proof |
| `[L2]` | Open problem; does not block current papers |
| `[MC]` | Motivated Candidate — argument given, not a complete proof |
| `[STD]` | Follows from standard math/physics (cited) |
| `[OBS]` | Numerically confirmed; not derived from S[Θ] |
| `OPEN` | No current candidate solution |
| `CONDITIONAL` | Holds given an unresolved assumption (must be stated) |

Source: `DERIVATION_STATUS_STANDARD.md`

---

## 4. Active Repository Structure

```
canonical/
  gr_closure/
    step1_metric_bridge.tex         ← metric derivation [L1]
    step2_nondegeneracy.tex         ← non-degeneracy [L1]
    step3_signature_theorem.tex     ← Lorentzian signature [L1]
    step3_einstein_with_matter.tex  ← Einstein eqs [L1]
    GR_chain_summary.tex            ← chain overview
    zerilli_derivation.tex          ← Zerilli [L1]
    linearised_gravity.tex          ← Regge-Wheeler [L1] (ED-2 closed)
    frw_cosmological_solutions.tex  ← FRW [L1]+[L1 cond.]
    schwarzschild_table.tex         ← numerical table (ED-3 closed)
  chirality/
    step3_gap_C1_resolution.tex     ← SU(2)_L [L1]
    step4_no_wr_derivation.tex      ← OP-S4 [L1 conditional]
  alpha/                            ← T3_ALPHA (STRUCTURAL EVIDENCE)
  n_eff/step2_AUDIT.tex             ← N_eff audit; twist=12 clarification
  interactions/                     ← SM gauge structure
papers/
  UBT_GR_Submission.tex    ← T1_GR SUBMIT READY — all editorial items closed
  UBT_Gauge_Submission.tex ← T2_GAUGE paper COMPLETE
  UBT_Gauge_Draft_v1.bib   ← bibliography
research_tracks/T3_ALPHA/
  mellin_insertion_B.tex   ← formal no-go record (6 routes, 3 sub-gaps)
  integer_137_note.tex     ← companion note
research_tracks/EW/
  hypercharge_from_ubt.tex ← Gap C2 Step 1 — Y=(B-L)/2 [L1 cond. on OP-S4 + C2-i]; sub-gap C2-i [OPEN/MC]
STATUS_OF_UBT.md           ← SINGLE SOURCE OF TRUTH
WHAT_IS_PROVED.md          ← Complete proved-results inventory
DERIVATION_INDEX.md        ← Index of derivation files + levels
ROADMAP.md                 ← Execution-control, locked sequencing
PROOF_GAP_CLOSURE.md       ← ED-1, ED-2, ED-3 ALL DONE
```

---

## 5. Theory Track Status (as of v54, 2026-06-11)

### T1_GR — GR Recovery: SUBMIT READY — NO BLOCKERS

All five theorem-chain steps proved [L1]. Both graviton polarisations [L1]. FRW cosmology [L1]+[L1 cond.]. All three editorial items closed. **The paper is ready to submit today.**

| Claim | Level | Source |
|---|---|---|
| Metric g_μν from Θ | [L1] | `step1_metric_bridge.tex` |
| Non-degeneracy det(g)≠0 | [L1] | `step2_nondegeneracy.tex` |
| Lorentzian signature from AXIOM-B | [L1] | `step3_signature_theorem.tex` |
| Einstein equations | [L1] | `UBT_GR_Submission.tex §3` |
| T_μν conservation | [L1] | `stress_energy.tex` |
| Schwarzschild (<10⁻¹⁵) | [L1]+[NUM] | `schwarzschild_table.tex` |
| Regge-Wheeler (odd-parity) | [L1] | `linearised_gravity.tex` + paper §5 |
| Zerilli (even-parity) | [L1] | `zerilli_derivation.tex` |
| Flat FRW in solution space | [L1] | `frw_cosmological_solutions.tex §2` |
| Friedmann equations from Steps 1–5 | [L1] | `frw_cosmological_solutions.tex §2` |
| ODE-a consistency with Friedmann | [L1] | `frw_cosmological_solutions.tex §4 Lem ode_a_friedmann` |
| FRW Θ-ansatz solves ∇†∇Θ=κ𝒯 | [L1 cond. on Friedmann + ODE-f] | `frw_cosmological_solutions.tex §3` |
| g_0i=0 in comoving frame | [L1 cond. on comoving averaging] | `frw_cosmological_solutions.tex §4` |
| ODE-f: κ𝒯₀=κρ; explicit solutions f∝a^{-3(1+w)} | [L1 cond. on quasi-static approx.] | `frw_cosmological_solutions.tex §3 Prop ode_f_solutions` |
| GAP-10: off-shell Θ-only closure | [L2] open | State in paper; does not block |
| ED-1 notation unification | ✅ DONE | `GR_chain_summary.tex`, `step1_metric_bridge.tex` |
| ED-2 Regge-Wheeler source | ✅ DONE | `linearised_gravity.tex` |
| ED-3 Schwarzschild table | ✅ DONE | `schwarzschild_table.tex` |

### T2_GAUGE — Gauge Sector: PAPER COMPLETE

All sections §1–§9 complete. Chirality at OP-S4 [L1 conditional]. α at STRUCTURAL EVIDENCE. NCG/Furey comparison table in Discussion.

| Claim | Level |
|---|---|
| Full SM gauge group SU(3)×SU(2)_L×U(1)_Y | [L0] — 0 free params |
| OP-S4: full SU(2)_R exclusion | [L1 conditional] |
| Minimality: anomaly-safe + unitarity deferred | Remark in step4_no_wr_derivation.tex §4 |
| Gap C2 Step 1: hypercharge from ψ-winding + OP-S4 | [L1 cond. on OP-S4 + C2-i] — hypercharge_from_ubt.tex Lem lem:hypercharge_formula; sub-gap C2-i [OPEN/MC] |
| Three generations from ψ-winding | [L0] |
| sin²θ_W (EW-1b via RG) | [L1 cond. on Gap C2] |
| Weinberg angle pure algebra | **DEAD END** — stated in paper |
| W/Z masses, Higgs, Yukawa | DEFERRED |

### T3_ALPHA — Fine Structure Constant: STRUCTURAL EVIDENCE

**Downgraded 2026-06-11. 6 routes NO-GO. α NOT DERIVED.**
Companion note `integer_137_note.tex` written.

| Claim | Level |
|---|---|
| n*(B_phenom)=137 | [L1 conditional on B] |
| N_eff^twist=12 (integer-137 uses this route) | [L1] |
| N_eff^loop=3 (independent; gives n*≈10.5) | [L1] |
| twist=loop identification | **[OPEN/MC frozen]** |
| G137-B-i/ii/iii (three named sub-gaps) | **[OPEN/MC]** |
| B_phenom from S[Θ] | **NOT DERIVED** |
| α | **NOT DERIVED** |

---

## 6. Active Open Gaps — Priority Order

**T1_GR has no remaining blockers. The only action is submission.**

| # | Task | Description | File |
|---|---|---|---|
| 1 | **Submit T1_GR** | arXiv + journal — no scientific or editorial blockers | `papers/UBT_GR_Submission.tex` |
| 2 | **Submit T2_GAUGE** | Paper complete; submit after T1_GR clears initial review | `papers/UBT_Gauge_Submission.tex` |
| 3 | **Gap C2 Step 1** | Fermion hypercharge assignments from UBT — see `hypercharge_from_ubt.tex` | `research_tracks/EW/` |
| 4 | **EW-1b** | First-principles EW+RG closure for sin²θ_W≈0.231 | `research_tracks/EW/weinberg_angle_ew1_rg.tex` |
| 5 | **OP-S4 minimality** | Prove minimality assumption consistent with anomaly cancellation — see Remark in step4 §4 | `step4_no_wr_derivation.tex §4` |
| 6 | **FRW ODE-f** | Derive f(t) beyond quasi-static approx.; see Prop. ode_f_solutions | `frw_cosmological_solutions.tex §3` |
| 7 | **GAP-10** | Off-shell Θ-only closure [L2] — does not block any paper | `step2_theta_only_closure.tex` |

---

## 7. Work Instructions for Next Iteration

**Priority context**: T1_GR submission is purely a publication action — no Copilot work needed.
The next substantive technical tasks are further work on Gap C2, OP-S4 minimality, and FRW ODE-f.

### D1 — Gap C2 Step 1: fermion hypercharge assignments (DONE — outcome documented)

**File**: `research_tracks/EW/hypercharge_from_ubt.tex`

The derivation attempt documents:
- Hypercharge via Y = (B-L)/2 (ψ-winding topology + OP-S4) gives correct SM values [L1 cond. on OP-S4] **for the six standard fermion representations**
- The ψ-winding fractions (quark B=1/3 from n=1/3) are derived from the colour-charge quantisation in the SU(3) sector but the fractional winding numbers introduce a **sub-gap C2-i**: the precise mechanism assigning n=1/3 to quarks (rather than n=1 leptons) requires a full derivation from the SU(3)×SU(2)_L action on ψ-winding states
- **Status**: Hypercharge formula Y=(B-L)/2 is [L1 conditional on OP-S4 + C2-i]; sub-gap C2-i is [OPEN/MC]

### D2 — OP-S4 minimality: Remark on anomaly cancellation (DONE)

**File**: `canonical/chirality/step4_no_wr_derivation.tex §4` (Remark `rem:minimality_anomaly`)

Added after Corollary `cor:loophole2_closed`: checks (a) gauge anomaly safety with minimal content (anomaly-safe conditional on Gap C2 — T2_GAUGE paper §anomaly) and (b) unitarity of W/Z scattering (EW-2 deferred; noted as open item, not inconsistency).

### D3 — FRW ODE-f: quasi-static solutions (DONE)

**File**: `canonical/gr_closure/frw_cosmological_solutions.tex §3` (Proposition `prop:ode_f_solutions`)

Added after Remark `rem:ode_f_residual`: κ𝒯₀(t) = κρ(t) from T_μν scalar-sector projection; quasi-static particular solutions f ∝ a^{-3(1+w)} for dust (w=0) and radiation (w=1/3). Conditionality on ODE-f remains (quasi-static approximation required); label [L1 cond. on Friedmann + quasi-static].

### D4 — Status sync

`STATUS_OF_UBT.md`, `WHAT_IS_PROVED.md`, `DERIVATION_INDEX.md` updated to reflect D1–D3 results (same session as D1–D3 completion).

---

## 8. Status Governance Rules

1. `STATUS_OF_UBT.md` is the single source of truth. Mirror every status change there same-day.
2. Never upgrade a proof level without explicit user instruction.
3. No new alpha routes without explicit instruction. α is NOT DERIVED.
4. Dead routes stay dead: A3, A4, EW-1 pure-algebra Weinberg.
5. `ARCHIVE/` is read-only. Speculative extensions frozen (no expansion).

---

## 9. Speculative Extensions — Frozen

Do not expand or reference in core files:
- Complex Consciousness / Psychons → `speculative_extensions/complex_consciousness/`
- Closed Timelike Curves → `speculative_extensions/appendices/`
- p-adic dark sector → `research_tracks/p_universes/` (deferred)

---

## 10. LaTeX Conventions

### 10.1 Standalone file pattern
```latex
\ifdefined\INCLUDEMODE\else
  \documentclass[12pt,a4paper]{article}  % preamble
  \begin{document}\maketitle
\fi
% content
\ifdefined\INCLUDEMODE\else\end{document}\fi
```

### 10.2 Notation standards (ED-1 complete)

| Symbol | Meaning | LaTeX |
|---|---|---|
| Θ | UBT fundamental field | `\Theta` |
| τ∈ℂ | Complex time t+iψ | `\tau \in \mathbb{C}` |
| 𝒢_μν | Biquaternionic Einstein tensor | `\mathcal{G}_{\mu\nu}` |
| G_μν | Standard Einstein tensor (real limit only) | `G_{\mu\nu}` |
| S_total | Full UBT action | `S_{\mathrm{total}}` |
| S_Θ | Matter part of action | `S_\Theta` |
| 𝒩 | Normalisation — align with `theorem_chain.tex` | `\mathcal{N}` |

### 10.3 Status box environments
```latex
\newmdenv[backgroundcolor=yellow!20,linecolor=orange,linewidth=1.5pt]{gapbox}
\newmdenv[backgroundcolor=green!15,linecolor=green!60!black,linewidth=1.5pt]{resultbox}
\newmdenv[backgroundcolor=red!10,linecolor=red!60,linewidth=1.5pt]{deadendbox}
\newmdenv[backgroundcolor=blue!8,linecolor=blue!50,linewidth=1.5pt]{insightbox}
```

### 10.4 CI workflow (v51 structure)

Three jobs: `lint` → `compile` + `compile_standalone_roots` (parallel) → `publish_pdfs` (master only).
- `lint`: `test_symbolic_alpha.py` must pass; `lint_complex_time_usage.py` warns only.
- `compile_standalone_roots` matrix currently covers:
  `step4_no_wr_derivation.tex`, `frw_cosmological_solutions.tex`, `linearised_gravity.tex`, `integer_137_note.tex`
- Extra packages: `mdframed booktabs mathtools hyperref xcolor physics braket`

When adding a new standalone `.tex` file: add to both `.github/latex_roots.txt` AND `matrix.root` in `latex_build.yml`.

---

## 11. Key Reference Files

| Question | File |
|---|---|
| Current track status | `STATUS_OF_UBT.md` |
| What is proved at what level | `WHAT_IS_PROVED.md` |
| T1_GR editorial gaps (all closed) | `PROOF_GAP_CLOSURE.md` |
| Alpha no-go record | `research_tracks/T3_ALPHA/mellin_insertion_B.tex §formal-gap` |
| Alpha companion note | `research_tracks/T3_ALPHA/integer_137_note.tex` |
| N_eff which route enters α | `canonical/n_eff/step2_AUDIT.tex §rem:neff_alpha_dependency` |
| Gap C2 Step 1 derivation | `research_tracks/EW/hypercharge_from_ubt.tex` |
| Execution order | `ROADMAP.md` |
| All derivation file locations | `DERIVATION_INDEX.md` |

---

## 12. What Copilot Must Never Do

- Change license, copyright, or author attribution without explicit instruction.
- Upgrade a proof level label without explicit instruction.
- Open new alpha routes or derivation tracks without explicit instruction.
- Add content to `speculative_extensions/` or reference frozen tracks in core files.
- Modify `ARCHIVE/` or `original_release_of_ubt/`.
- Reopen killed routes (A3, A4, EW-1 pure-algebra Weinberg).
- Edit `STATUS_OF_UBT.md` without mirroring all changes in the same session.
- Commit generated PDFs — CI handles PDF generation.
- Use "UBT Team" or any name other than "Ing. David Jaroš" in new files.
- Claim α is derived, B_phenom is derived, or Gap G137-B is closed.
