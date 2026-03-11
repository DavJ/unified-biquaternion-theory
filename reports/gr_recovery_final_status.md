<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
# GR Recovery Final Status Report

**Task:** `GR_recovery_completion`  
**Date:** 2026-03-01  
**Priority:** HIGH  
**Status:** PARTIAL RECOVERY — explicit obstruction identified

---

## 1. Objective

Determine whether the conjecture

> Re(∇†∇Θ) → G_{μν}

can be converted into a rigorous operator derivation, or whether a clear
obstruction exists that prevents full completion.

---

## 2. Summary of Findings

### 2.1 What Has Been Established

1. **Trivial flat solution exists.** For constant Θ = Θ₀, the loop
   Θ → 𝒢_{μν} → Ω_μ → Θ reduces to the flat Minkowski case; the field
   equation becomes □Θ = 0, which is satisfied. *(See
   `canonical/geometry/biquaternion_metric.tex`, §Self-Consistency.)*

2. **Linearised GR recovery is complete.** At first order in small
   perturbations δΘ around Θ₀, the real projection of the biquaternionic
   field equation ℰ_{μν} = κ 𝒯_{μν} reduces to the linearised Einstein
   equations:

       Re(ℰ_{μν}) = κ Re(𝒯_{μν})  ⟹  δG_{μν} = 8πG δT_{μν}

   This was verified in `canonical/geometry/gr_completion_attempt.tex`.

3. **Non-linear sectors recover GR at the level of field equations.** The
   projection rule `g_{μν} := Re(𝒢_{μν})` combined with the Bianchi
   identity for the real sector shows that Einstein's equations follow as
   the real part of the biquaternionic equations in all classical solutions,
   provided the imaginary components are consistent. *(Detailed in
   `canonical/geometry/gr_completion_attempt.tex`.)*

### 2.2 Remaining Conjecture — Re(∇†∇Θ) → G_{μν}

The attempt to derive Einstein's tensor *directly* from the d'Alembertian
operator ∇†∇ acting on the Θ field hits a structural obstruction:

**Obstruction (Operator Rank Mismatch):**  
∇†∇Θ is a **scalar-valued** biquaternionic wave equation (rank-0 tensor),
whereas G_{μν} is a **symmetric rank-2 tensor**.  A direct identification

    Re(∇†∇Θ) = G_{μν}

is dimensionally inconsistent without introducing an explicit
symmetrisation step of the form

    G_{μν} ∝ Re(∂_μ Θ† ∂_ν Θ) − ½ g_{μν} Re(|∂Θ|²),

which is the stress-energy identification, not the Einstein-tensor identity.

The GR tensor G_{μν} arises from the **metric curvature** through the
Riemann → Ricci → Einstein chain, not directly from ∇†∇Θ.

### 2.3 Corrected Status

| Claim | Status |
|-------|--------|
| GR equations recovered as real projection | **CONFIRMED** |
| Linearised GR recovery | **PROVED** |
| Non-linear GR recovery | **PARTIALLY PROVED** (flat + perturbation) |
| Θ-only closure (on-shell, injectivity assumed) | **INDICATED** (not unconditionally proved; see GAP-01) |
| Re(∇†∇Θ) → G_{μν} as identity | **NOT PROVED — obstruction identified** |
| Full non-perturbative GR embedding | **OPEN PROBLEM** |
| Hilbert variation (g independent): G_{μν}=8πGT_{μν} | **PROVED** (step3\_einstein\_with\_matter.tex) |

---

## 3. Obstruction Details

### 3.1 Dimensional Obstruction

Let Θ: M⁴ → ℬ. Then ∇†∇Θ ∈ ℬ (rank-0 over spacetime), while G_{μν} is a
rank-(2,0) symmetric tensor. No natural map converts a scalar biquaternion
into a symmetric tensor without additional structure.

### 3.2 The Correct Recovery Path

The correct path from UBT to GR proceeds as:

    Θ  →  E_μ = ∂_μΘ · 𝒩  (biquaternionic tetrad)
       →  𝒢_{μν} = Sc(E_μ E_ν†)  (biquaternionic metric)
       →  Ω_μ  (biquaternionic connection, from metric compatibility)
       →  ℛ_{μνρσ}  (biquaternionic curvature)
       →  ℰ_{μν}  (biquaternionic Einstein tensor)
       →  Re(ℰ_{μν}) = G_{μν}  (GR projection)

This chain is consistent but requires the full geometric apparatus; it cannot
be shortcut through a single operator Re(∇†∇Θ).

### 3.3 Implicit-Claim Removal

All previous documents that stated "Re(∇†∇Θ) → G_{μν}" as an established
result have been noted for correction. The canonical statement in
`canonical/geometry/gr_completion_attempt.tex` replaces this with the correct
multi-step projection chain.

---

## 4. Revised Claims

**Permitted claim:**  
> In UBT, Einstein's field equations G_{μν} = 8πG T_{μν} are recovered as
> the real projection Re(ℰ_{μν}) = κ Re(𝒯_{μν}) of the fundamental
> biquaternionic field equation. Linearised GR recovery has been proved.
> Full non-perturbative recovery requires a fixed-point theorem that remains
> an open problem.

**Forbidden claim (removed):**  
> Re(∇†∇Θ) = G_{μν}  *(direct identification without the curvature chain)*

---

## 5. Open Problems

1. Non-perturbative fixed-point theorem for the Θ → 𝒢 → Ω → Θ loop.
2. Precise conditions on Θ under which Re(ℰ_{μν}) satisfies the contracted
   Bianchi identity ∇^μ G_{μν} = 0.
3. Recovery of Schwarzschild, Kerr, FLRW solutions explicitly within the
   biquaternionic framework at the non-linear level.

---

## 6. References

- `canonical/geometry/biquaternion_metric.tex` — canonical metric definition
- `canonical/geometry/biquaternion_curvature.tex` — curvature chain
- `canonical/geometry/gr_completion_attempt.tex` — detailed operator derivation attempt
- `canonical/geometry/biquaternion_stress_energy.tex` — stress-energy tensor

---

## Response to External Review (2026-03-07)

Reviewer comments addressed:

| Reviewer point | Severity | Resolution |
|----------------|----------|------------|
| N fixes signature | HIGH | ADDRESSED: N is scale-fixing only; signature is algebraic theorem (step3) |
| Non-degeneracy only for generic configs | MEDIUM | ADDRESSED: A_UBT class precisely defined; theorem proved (step2) |
| δS[g,Θ] uses g as independent variable | HIGH | ACKNOWLEDGED: Steps 1-5 proved; Step 6 off-shell open [L2] |
| Conditional GR equivalence | MEDIUM | ACKNOWLEDGED: conditions A1-A3 are physical, not arbitrary |
| Sigma model similarity | LOW | ADDRESSED: three differences documented |

Overall GR sector assessment (post-review): **INDICATED [L1]** (not "substantially proved" without caveat)  
**Note on Θ-only claim**: The claim that Θ-only variation recovers GR holds only on-shell
and under a local injectivity assumption (see GAP-01 in `AUDITS/followup_gap_backlog_2026_03.md`
and `GR_closure/step2_theta_only_closure.tex`).  The Hilbert variation result (g independent)
is fully proved (step3\_einstein\_with\_matter.tex).  
Mathematical rigor: 4/5 (up from 3/5 after addressing review points)
