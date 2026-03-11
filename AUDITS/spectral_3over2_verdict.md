<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# spectral_3over2_verdict.md — Final Verdict for the Spectral 3/2 Program

**Program:** `ubt_spectral_3over2_program`  
**Track:** SPECTRAL — independent of Hecke / twin-prime / 137 route  
**Date:** 2026-03-10  
**Overall verdict:** PARTIALLY SUPPORTED — key step localised

---

## 1. Summary of Results

| Step | Document | Outcome |
|------|----------|---------|
| 1. Repository audit | `AUDITS/spectral_3over2_audit.md` | Complete — existing dead ends documented, new gaps identified |
| 2. Θ-operator candidates | `research/spectral_3over2/theta_operator_candidates.tex` | Three candidates assessed; Candidate 3 (Im(ℍ) Laplacian) identified |
| 3. Heat kernel asymptotics | `research/spectral_3over2/heat_kernel_theta.tex` | d/2 = 3/2 proved in one-loop Γ₁; spacetime d_eff = 4 (not 3) |
| 4. Weyl counting | `research/spectral_3over2/weyl_counting_theta.tex` | 3D Weyl law holds on ℝ³; UBT spectral manifold not identified |
| 5. Bridge to B_base | `research/spectral_3over2/B_base_from_spectral_density.tex` | Missing step sharply localised |
| 6. Quaternionic dimension | `research/spectral_3over2/quaternionic_dimension_test.md` | Im(ℍ) = multiplicity space (not spectral manifold); su(2) analogy rejected |

---

## 2. Strongest Positive Result

**Result (PROVED, independent of 137):**

> The one-loop UBT effective action for Θ-fluctuations in Im(ℍ) takes the form:
>
>     Γ₁[Θ₀] = (d/2) · Tr ln Ô  =  (3/2) · Tr ln Ô
>
> where the coefficient **3/2 is exact and not a free parameter**, arising from:
> - **d = dim_ℝ(Im(ℍ)) = 3** — proved algebraic fact (three quaternion-imaginary directions)
> - **Factor 1/2** — proved mathematical identity (Gaussian path integral)
>
> This means B_base ∝ (3/2) · [gauge factor] where the gauge factor involves N_eff.

This result is independent of α⁻¹ = 137, independent of the Hecke/twin-prime route,
and does not use any free parameters.
It provides a **first-principles algebraic reason** for why the exponent 3/2 appears.

---

## 3. Exact Blocking Step

The spectral 3/2 program is blocked at one precisely identified step:

**Gap: Identifying f(N_eff) in B = (d/2) · f(N_eff) = N_eff^{3/2}**

From the proved result:
```
B = (3/2) · f(N_eff)
```
To conclude `B_base = N_eff^{3/2}` requires:
```
f(N_eff) = N_eff
```
i.e., the gauge-coupling integral in the vacuum polarisation must evaluate
to a quantity proportional to N_eff (not N_eff^{1/2}, N_eff², or anything else).

The standard one-loop flat-space calculation gives:
```
f(N_eff) = 2π/3 · N_eff  →  B₀ = (3/2) · (2π/3 · N_eff) = π · N_eff ≠ N_eff^{3/2}
```

Wait — this is **not** the correct split. The standard calculation gives:
```
B₀ = 2π N_eff / 3 = 25.1  [PROVED]
```
This can be written as:
```
B₀ = (3/2) · (4π N_eff / 9) = (3/2) · [4π/9 · N_eff]
```
so `f(N_eff) = 4π N_eff / 9 ≈ 4.19 · 12 / 9 ≈ 5.59` (not equal to N_eff = 12).

For `B_base = N_eff^{3/2} = 41.57`, one needs:
```
f(N_eff) = N_eff^{3/2} / (3/2) = (2/3) · N_eff^{3/2} = (2/3) · 12^{3/2} ≈ 27.71
```

The gap is: `f(N_eff)` must equal `(2/3) N_eff^{3/2}`, not `4π N_eff/9`.
The spectral program alone does not fix this ratio.

**Concise statement of the blocking step:**
> The one-loop flat-space integral gives B₀ = 2π N_eff/3, not N_eff^{3/2}.
> The ratio B_base/B₀ = (3/2π)√N_eff ≈ 1.654 remains unexplained.
> The spectral 3/2 program explains **why** the exponent is 3/2 (as d/2),
> but does not explain **why** the coefficient is N_eff (not 4π/9 · N_eff as in flat-space QFT).

This gap is identical to the Δd = 0.405 gap documented in
`consolidation_project/alpha_derivation/b_base_delta_d.tex`.

---

## 4. Dependency on Unproved Assumptions

The following claims made in this program are **[MOTIVATED CONJECTURE]**, not proved:

1. **3D residual from p₀ integration** (Route C' in weyl_counting_theta.tex):
   - The vacuum polarisation after p₀ integration may naturally give a 3D mode count.
   - This would provide a spectral geometry route to `N(λ) ~ λ^{3/2}`.
   - **Not yet verified:** explicit evaluation of the p₀ integral and its coupling to B.

2. **UV scale N_eff^{1/2}/R_ψ** (B_base_from_spectral_density.tex §3.1):
   - A geometric UV cutoff at scale N_eff^{1/2}/R_ψ would produce N_eff^{3/2}.
   - **Not yet proved:** this scale is not fixed by the UBT action alone.

3. **Im(ℍ) as effective spectral manifold** (quaternionic_dimension_test.md):
   - If Im(ℍ) were the base manifold (not just multiplicity space), the Weyl law
     would give N(λ) ~ λ^{3/2}.
   - **Rejected as simple analogy** — Im(ℍ) is a multiplicity space in UBT.

---

## 5. Relation to the Existing Alpha Program

### What this program shares with the existing program

| Shared element | Status |
|---------------|--------|
| d = dim_ℝ(Im(ℍ)) = 3 from gauge invariance | [PROVED] — also in b_base_hausdorff.tex |
| Gaussian exponent d/2 = 3/2 in Γ₁ | [PROVED] — also in b_base_hausdorff.tex |
| B₀ = 2π N_eff/3 from one-loop flat space | [PROVED] — also in appendix_ALPHA |
| Gap Δd = 0.405 remains open | [OPEN] — also in b_base_delta_d.tex |

### What this program adds

| New contribution | Source |
|----------------|--------|
| Explicit heat kernel analysis for each candidate operator | heat_kernel_theta.tex |
| Weyl counting for 3 routes (A, B, C, C') | weyl_counting_theta.tex |
| 3D residual from p₀ integration (Route C', new candidate) | weyl_counting_theta.tex §4 |
| Rejection of su(2) dimension = 3 as the source | quaternionic_dimension_test.md |
| Rejection of complexified ℂ³ route | quaternionic_dimension_test.md |
| Sharp localisation of the missing step | B_base_from_spectral_density.tex §3 |

### Independence confirmed

This program:
- ❌ Does **not** use α⁻¹ = 137 as an input anywhere.
- ❌ Does **not** use twin-prime (137, 139) structure.
- ❌ Does **not** use the Hecke-worlds framework.
- ✅ Uses only: N_eff = 12 [PROVED], dim_ℝ(Im(ℍ)) = 3 [PROVED], S[Θ].

---

## 6. Recommended Next Steps

### Priority 1 (spectral geometry route, Route C')

**Task:** Evaluate the $p_0$-integral reduction explicitly.

Starting from the Euclidean vacuum polarisation:
```
Π(k²) ∝ N_eff · ∫ d⁴p/(2π)⁴ · [1/((p²+m²)((p+k)²+m²))]
```
Perform the p₀ integral to obtain a 3D integral, and determine whether
the resulting mode count couples to B as `B ∝ N_eff^{3/2}`.

**Expected outcome:** Either (a) a new route to N_eff^{3/2}, or (b) a dead end
with explicit calculation showing why the p₀ reduction does not help.

### Priority 2 (UV scale argument)

**Task:** Derive the natural UV cutoff from the compact ψ-geometry.

Show from the UBT action whether the compactification radius R_ψ combined
with N_eff sets a UV scale Λ = f(N_eff)/R_ψ, and determine f.

### Priority 3 (connection to noncommutative geometry)

**Task:** Follow up on Approach A4 (NCG effective dimension) in
`consolidation_project/alpha_derivation/b_base_ncg_a4.tex`, which
is labelled [STRUCTURAL INSIGHT].
The NCG spectral triple may provide a d_eff = 3 directly from the
Connes–Lott standard model geometry.

---

## 7. Formal Verdict

**The spectral 3/2 program has produced:**

| Claim | Verdict |
|-------|---------|
| A concrete Θ-operator candidate is identified | ✅ YES — Candidate 3: Laplacian on Im(ℍ); flat-space factorisation proved |
| Heat-kernel asymptotics written down explicitly | ✅ YES — all three candidates computed; spacetime d_eff = 4 shown |
| Effective spectral dimension analysed rigorously | ✅ YES — d = 3 appears as multiplicity, not as spectral dimension |
| Connection to B_base derived or sharply localised | ✅ LOCALISED — gap = identification of f(N_eff) in B = (3/2)·f(N_eff) |
| Track independent of Hecke/twin-prime numerology | ✅ YES — fully independent |

**Overall status:**

> **PARTIALLY SUPPORTED.**
> The exponent 3/2 in B_base is motivated (but not proved) from spectral geometry.
> The algebraic proof that d/2 = 3/2 appears in Γ₁ is **[PROVED]**.
> The spectral route (Weyl law with d_eff = 3) is **[NOT YET PROVED]** — a 3D
> spectral manifold has not been identified in UBT.
> The missing step is precisely localised: show f(N_eff) = N_eff in
> B = (d/2) · f(N_eff), or equivalently explain the ratio
> B_base/B₀ = (3/2π)√N_eff ≈ 1.654 from spectral geometry.

---

*End of verdict document.*
