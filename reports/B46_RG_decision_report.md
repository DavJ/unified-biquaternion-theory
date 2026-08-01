<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->


# B≈46 RG Decision Report

**Track**: `research_tracks/rg_B46/`  
**Author**: Ing. David Jaroš  
**Date**: May 2026  
**Task**: `derive_or_kill_B46_from_RG_and_mode_counting` — Target 4  
**Hard rules**: Do not use α, 137, B_required, or B(p)=(p+1)/3 as input.
Compare to 46 only at the end.

---

## 1. Combining All Derived Terms

### 1.1 Input from Targets 1–3

| Source | $\Delta B$ | Status | Reference |
|--------|-----------|--------|-----------|
| One-loop baseline $B_0 = 8\pi$ | 25.133 | CONDITIONAL | `one_loop_rg_derivation.tex` |
| Two-loop RG | $\lesssim 0.05$ | PLAUSIBLE | `higher_loop_thresholds.tex` §2 |
| KK threshold tower | $\approx 13.9$ | PLAUSIBLE | `higher_loop_thresholds.tex` §3 |
| Compactification threshold | 0 | DERIVED | `higher_loop_thresholds.tex` §4 |
| Winding degeneracy (T-dual) — constant | $\approx 18.5$ | **NO-GO** — see `reports/t_dual_winding_verdict.md` | `higher_loop_thresholds.tex` §5 |
| Winding increment (derived, n-dependent) | $\Delta B_\mathrm{wind}(n) = N_\mathrm{eff}n/(12\pi^2)$ | PROVED (not constant; adds $n^2\ln n$ term) | `reports/t_dual_winding_verdict.md` |
| Zero-mode subtraction | 0 | DERIVED | `higher_loop_thresholds.tex` §6 |
| Ghost determinant | 0 | DERIVED | `higher_loop_thresholds.tex` §7 |
| Curvature/torsion | 0 | DERIVED | `higher_loop_thresholds.tex` §8 |
| Torus shape ($\epsilon=0$) | 0 | CONDITIONAL | `higher_loop_thresholds.tex` §9 |

### 1.2 Non-independence warning

The winding degeneracy and KK threshold tower corrections overlap:
winding doubles the effective mode count, which is equivalent to adding one full
set of threshold corrections from the mirror (winding) sector.  They are
**not additive** — using both would double-count.  The correct strategy:

- **Path A (winding)**: $B_\mathrm{A} = B_0 + \Delta B_\mathrm{wind} \approx 25.1 + 18.5 = 43.6$ — **OBSOLETE HEURISTIC** (winding correction is NO-GO)
- **Path B (KK threshold)**: $B_\mathrm{B} = B_0 + \Delta B_\mathrm{KK} \approx 25.1 + 13.9 = 39.0$ — PLAUSIBLE ONLY
- **Path C (4D baseline + winding)**: uses the 4D formula $B_0^{4D} + \Delta B_\mathrm{wind}$ — **OBSOLETE HEURISTIC**

After the winding NO-GO, **Path A and Path C are withdrawn**.  Only Path B
(KK threshold tower, PLAUSIBLE status) survives, and it does not reach $B \approx 46$.

### 1.3 Best estimate (updated after winding NO-GO)

The former best estimate $B_\mathrm{best} \approx 43.6 = B_0 + \Delta B_\mathrm{wind}$
is **OBSOLETE HEURISTIC**.

The current strongest safe coefficient is the one-loop baseline:

$$B_0 = 8\pi \approx 25.133 \quad (\text{CONDITIONAL on KK matching}).$$

---

## 2. Uncertainty Range

After the winding NO-GO, the range based on the heuristic $B_\mathrm{max} \approx 50.6$
is **no longer valid**.  The safe range is now:

$$B_\mathrm{min} = B_0 = 8\pi \approx 25.1 \quad\text{(one-loop, CONDITIONAL)},$$
$$B_\mathrm{plausible} \approx B_0 + \Delta B_\mathrm{KK} \approx 25.1 + 13.9 = 39.0 \quad\text{(PLAUSIBLE only)}.$$

No safe upper bound beyond 39.0 is supported by the current derivation chain.

**Summary** (updated):

| Quantity | Value | Status |
|---------|-------|--------|
| $B_0$ (one-loop baseline) | $8\pi \approx 25.1$ | CONDITIONAL — strongest safe claim |
| $B_0 + \Delta B_\mathrm{KK}$ | $\approx 39.0$ | PLAUSIBLE |
| $B_\mathrm{best} \approx 43.6$ | — | **OBSOLETE HEURISTIC** (winding NO-GO) |
| $B_\mathrm{max} \approx 50.6$ | — | **OBSOLETE HEURISTIC** |

---

## 3. Comparison to Structural Values (End-of-Analysis, updated after winding NO-GO)

| Reference value | Exact | Safe derivation? | Comment |
|-----------------|-------|-----------------|---------|
| $8\pi$ | $\approx 25.133$ | ✅ CONDITIONAL | Strongest safe derived coefficient |
| $12^{3/2}$ | $\approx 41.57$ | ❌ No mechanism | Coincidence; no derivation |
| $B_\mathrm{best} \approx 43.6$ | — | ❌ OBSOLETE HEURISTIC | Based on NO-GO winding step |
| $B \approx 46$ | $46$ | ❌ NOT DERIVED | Gap fully open |

The target $B \approx 46$ was previously estimated as reachable via
$B_\mathrm{best} \approx 43.6$.  That path used a constant winding correction
which is now NO-GO.  The gap from $B_0 = 8\pi$ to $B \approx 46$ is fully open.

---

## 4. Is $B \approx 46$ Naturally Reached, Barely Reachable, or Unreachable?

| Category | Condition | Assessment |
|----------|-----------|------------|
| Naturally reached | $B_\mathrm{best}$ within 1σ of 46 | ❌ $B_\mathrm{best} \approx 43.6$ is OBSOLETE HEURISTIC (winding NO-GO) |
| Barely reachable | $B_\mathrm{plausible} \geq 46$ | ❌ $B_0 + \Delta B_\mathrm{KK} \approx 39.0 < 46$ (PLAUSIBLE only) |
| Unreachable via safe derivation | — | ✅ Correct current assessment |
| Requires fitting | $\Delta B_i$ chosen to match | Not applicable (hard rule respected) |

**Assessment**: $B \approx 46$ is **not reachable from any currently safe derivation chain**.
The gap from $B_0 = 8\pi$ to $B \approx 46$ is fully open after the winding NO-GO.

---

## 5. Verdict

$$\boxed{B_\mathrm{verdict} = \textbf{OPEN — constant winding NO-GO}}$$

**Updated justification**:

- The constant winding correction $\Delta B_\mathrm{wind} \approx 18.5$ is **NO-GO**.
  The derived expression is $\Delta B_\mathrm{wind}(n) = N_\mathrm{eff}n/(12\pi^2)$,
  which is $n$-dependent and produces an $n^2\ln n$ contribution, not a constant $B$ shift.
- $B_\mathrm{best} \approx 43.6$ is **OBSOLETE HEURISTIC**.
- The previous verdict of NUMERICALLY_PLAUSIBLE is retracted.
- The strongest safe derived coefficient is $B_0 = 8\pi \approx 25.133$ (CONDITIONAL).
- Alpha remains not derived.
- $B \approx 46$ is OPEN.

---

## 6. Failed Claims

| Claim | Why it fails |
|-------|-------------|
| $B_0 = 8\pi$ is the full answer | $8\pi \approx 25.1 \ll 46$; additional mechanism needed |
| Two-loop closes the gap | $\Delta B_\mathrm{2-loop} \lesssim 0.05 \ll 20.9$ |
| Ghost determinant shifts $B$ | Ghost contribution = 0 (U(1) abelian) |
| Adding KK + winding independently | Double-counts; cannot be done |
| **Constant winding** $\Delta B_\mathrm{wind} \approx 18.5$ | **NO-GO**: correction is $n$-dependent, produces $n^2\ln n$, not constant $B$ shift |
| $B_\mathrm{best} \approx 43.6$ | **OBSOLETE HEURISTIC**: based on NO-GO winding step |
| $B \approx 46$ is proved | Gap $\Delta B \approx 20.9$ from $B_0$ remains fully open |

---

## 7. Surviving Route

After the winding NO-GO, the surviving safe derivation is:

$$B_0 = 8\pi \approx 25.133 \quad (\text{CONDITIONAL on KK matching}).$$

This is obtained from:
1. One-loop RG in 4D with $N_\mathrm{eff} = 12$ → $b_0 = 4$
2. Factor $2\pi$ from KK compactification (conditional) → $B_0 = 8\pi$

The former "surviving route" $B_\mathrm{best} \approx 43.6 = B_0 + \Delta B_\mathrm{wind}$
is withdrawn: the constant winding correction $\Delta B_\mathrm{wind} \approx 18.5$
is NO-GO.  The actual derived winding expression is $n$-dependent,
$\Delta B_\mathrm{wind}(n) = N_\mathrm{eff}n/(12\pi^2)$, and does not provide a
constant shift of the $n\ln n$ coefficient.

For a rigorous derivation of $B \approx 46$, a non-perturbative mechanism is required
(see `B46_next_path_if_no_go.md`).  See also `reports/alpha_B_gap_after_winding_no_go.md`.
