<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

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
| Winding degeneracy (T-dual) | $\approx 18.5$ | HEURISTIC | `higher_loop_thresholds.tex` §5 |
| Zero-mode subtraction | 0 | DERIVED | `higher_loop_thresholds.tex` §6 |
| Ghost determinant | 0 | DERIVED | `higher_loop_thresholds.tex` §7 |
| Curvature/torsion | 0 | DERIVED | `higher_loop_thresholds.tex` §8 |
| Torus shape ($\epsilon=0$) | 0 | CONDITIONAL | `higher_loop_thresholds.tex` §9 |

### 1.2 Non-independence warning

The winding degeneracy and KK threshold tower corrections overlap:
winding doubles the effective mode count, which is equivalent to adding one full
set of threshold corrections from the mirror (winding) sector.  They are
**not additive** — using both would double-count.  The correct strategy:

- **Path A (winding)**: $B_\mathrm{A} = B_0 + \Delta B_\mathrm{wind} \approx 25.1 + 18.5 = 43.6$
- **Path B (KK threshold)**: $B_\mathrm{B} = B_0 + \Delta B_\mathrm{KK} \approx 25.1 + 13.9 = 39.0$
- **Path C (4D baseline + winding)**: uses the 4D formula $B_0^{4D} + \Delta B_\mathrm{wind}$

Path A reproduces the known KK+winding estimate and is the most internally consistent
heuristic available.

### 1.3 Best estimate

$$B_\mathrm{best} = B_0 + \Delta B_\mathrm{wind} + \Delta B_\mathrm{2-loop}
\approx 25.133 + 18.5 + 0.05 = 43.68.$$

---

## 2. Uncertainty Range

The principal sources of uncertainty are:

| Uncertainty | Origin | Range |
|-------------|--------|-------|
| $B_0$ exact value | $2\pi$ factor in compactification matching | $\pm 3$ |
| Winding correction | T-duality at $R_\psi = 1$ (not derived) | $\pm 5$ |
| Two-loop | Coupling strength $g_\psi$ unknown | $[0, 0.05]$ |
| Torus shape | Modular parameter $\epsilon$ not derived | $[0, \mathcal{O}(1)]$ |
| Non-independence of corrections | Overlap between winding and KK | $\pm 2$ |

**Conservative range** (using all plausible corrections, avoiding double-counting):

$$B_\mathrm{min} = B_0 = 8\pi \approx 25.1 \quad\text{(no winding, no KK threshold)},$$
$$B_\mathrm{max} \approx B_0 + \Delta B_\mathrm{wind} + \Delta B_\mathrm{KK}/2
\approx 25.1 + 18.5 + 7.0 = 50.6.$$

**Summary**:

| Quantity | Value |
|---------|-------|
| $B_\mathrm{min}$ | $8\pi \approx 25.1$ |
| $B_\mathrm{best}$ | $\approx 43.6$ |
| $B_\mathrm{max}$ | $\approx 50.6$ |

---

## 3. Comparison to Structural Values (End-of-Analysis)

| Reference value | Exact | In range $[B_\mathrm{min}, B_\mathrm{max}]$? | Comment |
|-----------------|-------|----------------------------------------------|---------|
| $8\pi$ | $\approx 25.133$ | At $B_\mathrm{min}$ | This *is* $B_\mathrm{min}$ (one-loop only) |
| $12^{3/2}$ | $\approx 41.57$ | Yes, in $[25.1, 50.6]$ | Coincidence? No mechanism identified |
| $B \approx 46$ | $46$ | Yes, in $[25.1, 50.6]$ | In range but not at $B_\mathrm{best}$ |

The phenomenological target $B \approx 46$ lies within $[B_\mathrm{min}, B_\mathrm{max}]$,
but $\Delta B = 46 - B_\mathrm{best} \approx 2.4$ is unaccounted.

---

## 4. Is $B \approx 46$ Naturally Reached, Barely Reachable, or Unreachable?

| Category | Condition | Assessment |
|----------|-----------|------------|
| Naturally reached | $B_\mathrm{best}$ within 1σ of 46 | ❌ $B_\mathrm{best} \approx 43.6$, gap $\approx 2.4$ |
| Barely reachable | $B_\mathrm{max} \geq 46$ | ✅ $B_\mathrm{max} \approx 50.6 > 46$ |
| Unreachable | $B_\mathrm{max} < 46$ | ❌ Not the case |
| Requires fitting | $\Delta B_i$ chosen to match | Not applicable (hard rule respected) |

**Assessment**: $B \approx 46$ is **within the uncertainty range** but is not the best
estimate from the current perturbative calculation.  The gap $\Delta B \approx 2.4$
(5.2% of the target) is physical and unaccounted.

---

## 5. Verdict

$$\boxed{B_\mathrm{verdict} = \textbf{NUMERICALLY\_PLAUSIBLE}}$$

**Justification**:

- $B \approx 46$ is within $[B_\mathrm{min}, B_\mathrm{max}] = [25.1, 50.6]$.
- The best perturbative estimate is $B_\mathrm{best} \approx 43.6$, falling short by $\approx 2.4$.
- The gap 2.4 (5.2%) has no identified perturbative source (two-loop $\lesssim 0.05$,
  curvature and ghost are zero, torus shape speculative).
- The result is numerically plausible but not proved.

---

## 6. Failed Claims

| Claim | Why it fails |
|-------|-------------|
| $B_0 = 8\pi$ is the full answer | $8\pi < 43.6$; winding modes needed |
| Two-loop closes the gap | $\Delta B_\mathrm{2-loop} \lesssim 0.05 \ll 2.4$ |
| Ghost determinant shifts $B$ | Ghost contribution = 0 (U(1) abelian) |
| Adding KK + winding independently | Double-counts; cannot be done |
| $B \approx 46$ is proved | Gap $\Delta B \approx 2.4$ remains open |

---

## 7. Surviving Route

The surviving computational chain is:

$$B_\mathrm{best} \approx 43.6 = B_0 + \Delta B_\mathrm{wind},$$

obtained from:
1. One-loop RG in 4D with $N_\mathrm{eff} = 12$ → $b_0 = 4$
2. Factor $2\pi$ from KK compactification (conditional) → $B_0 = 8\pi$
3. T-duality at $R_\psi = 1$ doubles the contribution (heuristic) → $+\Delta B_\mathrm{wind}$

The residual $\Delta B \approx 2.4$ to reach $B \approx 46$ is not identified in
the perturbative/semiclassical framework.  For a rigorous derivation, a
non-perturbative mechanism is required (see `B46_next_path_if_no_go.md`).
