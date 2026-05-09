<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0
     Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.
     See LICENSE.md for full license text. -->

# eta_i_B_insertion_verdict.md — Does η(i) Enter the Coefficient B?

**Task**: prove_or_kill_eta_i_insertion_into_B  
**Author**: Ing. David Jaroš  
**Date**: 2026-05-09  
**Priority**: CRITICAL  
**Mode**: single_blocker_resolution  
**Gap ID**: G137-B (sub-question: η(i) in B vs. partition-function normalisation)  
**Hard rules**: No use of observed α; no use of B_required or 137 as input; no numerical agreement as proof.  
**Companion documents**:  
- `research_tracks/T3_ALPHA/cw_determinant_full_derivation.tex`  
- `research_tracks/T3_ALPHA/chowla_selberg_b_derivation.tex`  
- `research_tracks/alpha_spectral/b_coefficient_gap_resolution.tex`  
- `research_tracks/alpha_spectral/self_dual_torus_derivation.tex`  
- `research_tracks/alpha_spectral/hecke_equivariant_path_integral.tex`  
- `reports/B_gap_final_verdict.md`

---

## VERDICT: CONDITIONAL_WITH_EXACT_GAP

> **η(i) is a structurally motivated CANDIDATE for entering the coefficient B
> of V_eff(n) = n² − B n log n, but the insertion is NOT PROVED from S[Θ].**
>
> The formula B = N_eff^{3/2} · (2η(i))^{c/12} with c = 3 matches
> B_required to 0.007% — a precision that rules out pure coincidence among
> standard special values — but the derivation chain contains three
> independent open gaps, none of which has been closed.
>
> The η(i) factor currently enters only as a **partition-function
> normalisation** (n-independent); the claim that it multiplicatively
> modifies the n log n coefficient B requires a derivation that does not
> yet exist.

---

## 1. The Five Sub-Claims: Status Table

The task requires proving or rejecting the following chain:

| # | Claim | Verdict | Proof level | Notes |
|---|-------|---------|-------------|-------|
| C1 | UBT effective sector has a square torus T² with τ = i | **CONDITIONAL** | Shape stationary point proved; scale not fixed | `self_dual_torus_derivation.tex` |
| C2 | Relevant determinant is det'Δ_{T²} or UBT operator with same η(i) factor | **UNPROVED** | det'Δ_{T²} = (2π)²\|η(i)\|⁴ is proved (math); its role as *the* B-relevant operator is not proved | `chowla_selberg_b_derivation.tex` S4 |
| C3 | Physical effective central charge is c = 3 | **OPEN** | Structural counting argument exists; not derived from S[Θ] | `chowla_selberg_b_derivation.tex` S5 |
| C4 | Determinant contributes multiplicatively as (2η(i))^{c/12} | **OBSERVATION** [OBS] | 0.007% numerical match; physical mechanism plausible, not proved | `cw_determinant_full_derivation.tex` §6 |
| C5 | Multiplicative factor modifies B (n log n coefficient) not just Z | **UNPROVED** | n log n form itself not derived from UBT partition function; absorption into B not derived | `cw_determinant_full_derivation.tex` §4, §7 |

**All five claims are required to be proved for PROVED verdict.
None is fully proved. The verdict is therefore CONDITIONAL_WITH_EXACT_GAP.**

---

## 2. What Is Established (Proved)

The following results are rigorous and are not in dispute:

| Result | Status | Reference |
|--------|--------|-----------|
| Exact CW determinant on S¹_ψ: V_CW = n² − N_eff log(2 sinh(πn)) | **[L0] PROVED** | `cw_determinant_full_derivation.tex` Thm 1 |
| Integer-n CW correction is constant (translation invariance of Z) | **[L0] PROVED** | Same, §2.2 |
| Large-n limit is linear in n, not n log n | **[L1] PROVED** | Same, §3.2 |
| V_CW minimum at n* ≈ 6π ≈ 19, not 137 | **[L1] PROVED** | Same, Prop 1 |
| V_eff = n² − Bn log n is NOT the CW determinant on S¹_ψ | **[L1] PROVED** | Same, §3 |
| η(i) = Γ(1/4)/(2π^{3/4}) (Chowla–Selberg, D = −4) | **[L0] PROVED** | `chowla_selberg_b_derivation.tex` Thm 1 |
| det'(−Δ_{T²}) = (2π)² · \|η(i)\|⁴ at τ = i (spectral det.) | **[L0] PROVED** | Same, Thm 2 |
| η(i) = (det'(−Δ_{T²})/(2π)²)^{1/4} | **[L0] PROVED** | Same, Cor 1 |
| τ = i is a shape stationary point of the UBT one-loop free energy | **[L1] PROVED** (conditional) | `self_dual_torus_derivation.tex` Prop 1 |
| τ = i is locally stable in the shape mode (under spectral assumptions) | **[L1] PROVED** (conditional) | Same, Prop 2 |
| \|Γ₀(p)∖SL(2,Z)\| = p+1 for prime p | **[L0] PROVED** (arithmetic) | Diamond & Shurman Thm 3.1.1 |
| vol(X₀(p))/π = (p+1)/3 (arithmetic, hyperbolic geometry) | **[L0] PROVED** | `hecke_equivariant_path_integral.tex` Cor 2.3 |
| N_eff = 12 from dim_R(C ⊗ H) | **[L0] PROVED** | `canonical/alpha/B_base_derivation_complete.tex` |
| N_eff^{3/2} = 12^{3/2} ≈ 41.57 as base B coefficient | **[L1] PROVED** | Same |

---

## 3. The Numerical Observation

**[OBS]** The required coefficient satisfies:

```
B_required = 2 × n* / (log n* + 1)  |_{n*=137}  ≈  46.2840

B_obs = N_eff^{3/2} · (2η(i))^{c/12}  with N_eff = 12, c = 3
       = 12^{3/2} · (Γ(1/4)/π^{3/4})^{1/4}
       ≈  46.2809

Relative deviation:  |B_obs - B_required| / B_required  ≈  0.007%
```

The exponent x satisfying B_required = N_eff^{3/2} · (2η(i))^x
is x ≈ 0.25016, consistent with 1/4 to five significant figures.

A systematic scan of ~60 standard special values
(`tools/verify_b_eta_uniqueness.py`) shows no other candidate
N_eff^{3/2} · f achieves deviation below 0.8%; the next-best is
(2η(ρ))^{1/4} at 0.81%, a factor of ~115 worse.

**This precision rules out accidental coincidence at the level of 
arbitrary special values, but does not constitute a proof.**

---

## 4. The Three Open Gaps Blocking Proof

### Gap G-nlogn: Origin of the n log n Form

The exact Coleman–Weinberg effective potential on S¹_ψ is:

```
V_CW(n) = n² − N_eff log(2 sinh(πn))
```

This has minimum at n* ≈ 6π ≈ 19 and large-n behaviour
V_CW ≈ n² − π N_eff n (linear, not n log n).

The small-n limit gives V_CW ≈ n² − N_eff log n + const (form V4),
which also differs from V_eff = n² − Bn log n (form V1).

The n log n form therefore cannot come from the direct spectral
determinant of −∂²_ψ on S¹_ψ. A different physical mechanism is required.

**Candidate**: The Dirichlet divisor sum ∑_{k=1}^n τ(k) ≈ n log n
arising from the number-theoretic structure of the winding spectrum.
**Status: OPEN.** No derivation from S[Θ] exists.

**Consequence**: Even if C2–C4 were proved, the formula
B = N_eff^{3/2} · (2η(i))^{c/12} cannot be claimed to modify
the n log n coefficient without first establishing the n log n form.

### Gap G-c3: Central Charge c = 3 Not Derived

The exponent 1/4 = c/12 requires c = 3. Arguments offered:
- 3 transverse real bosonic DoF after SU(2)_L × U(1) gauge fixing in Im(H)
- Relation N_eff/4 = 12/4 = 3 (no independent derivation)

Neither argument constitutes a derivation from S[Θ].
Step S5 in `chowla_selberg_b_derivation.tex` is explicitly labelled **OPEN**.

**Consequence**: The exponent 1/4 in (2η(i))^{1/4} is inferred from
the coincidence x ≈ 0.25016 ≈ 1/4, not derived. Without a first-principles
derivation of c = 3, the exponent effectively comes from fitting,
even though the fitting target is a structurally motivated formula.

### Gap G-insertion: η(i) in B vs. Partition-Function Normalisation

This is the central question of the task.

The determinant det'(−Δ_{T²}) = (2π)²|η(i)|⁴ contributes to the
one-loop effective action as:

```
W_{1-loop} = (c/2) log det'(−Δ_{T²})
           = c log(2π) + 2c log η(i)
```

This is an **n-independent** contribution: the square torus T² at τ = i
has no winding-number dependence in its Laplacian spectrum
(the zero-mode sector only). It is therefore a **partition-function
normalisation**, not a B-coefficient modification.

For η(i) to enter B (the n log n coefficient), one of the following
must hold:

**(a)** The winding background at level n lives on a **rectangular torus**
with aspect ratio τ_n = in, so its η-function is η(in), not η(i). The
n-dependence of η(in) would then generate an n-dependent effective action.
However, log η(in) ~ −πn/12 for large n (linear in n, not n log n) and
at the self-dual point n=1 it gives η(i), contributing a **constant**
when evaluated at a fixed background n=1.

**(b)** A mechanism exists by which the **overall (n-independent)** factor
(2η(i))^c is "absorbed" into the n log n coefficient as a multiplicative
correction: B → B · (2η(i))^{c/12}. This requires:
  - A base coefficient B_base = N_eff^{3/2} from a different mechanism
  - A derivation showing that the Casimir normalisation multiplies B_base
  - The exponent c/12 arises from a conformal anomaly argument

None of these sub-steps is derived from S[Θ] in the existing documents.
The statement "the Casimir factor (2η(i))^{c/12} appears as normalisation
of V_eff" is labelled **[OPEN] (requires S5+S6)** in the derivation table.

**Status of G-insertion: OPEN — η(i) currently only justified as an
n-independent partition-function normalisation factor, not as a
modifier of the n-dependent B coefficient.**

---

## 5. Hecke-Equivariant Path-Integral Route: NO-GO

The strongest known derivation attempt
(`research_tracks/alpha_spectral/hecke_equivariant_path_integral.tex`,
2026-05-09) was completed and produced a NO-GO.

Three obstructions block the derivation:

| Label | Obstruction | Severity |
|-------|-------------|----------|
| O1 | S[Θ] not proved invariant under SL(2,Z) transformations of τ | **Critical** |
| O2 | SL(2,Z) action on winding modes Θ_n not derived from S[Θ] | **Critical** |
| O3 | Equal-action of p+1 candidate saddles cannot be established without O1 | **Blocking** |

Without O1, the p+1 coset representatives of Γ₀(p)∖SL(2,Z) cannot be
shown to be equal-action saddles of S[Θ], and the loop coefficient
cannot be identified with μ(Γ₀(p)) = p+1.

**Impact on η(i) insertion**: The Hecke route is the most promising known
mechanism for connecting the modular structure (from which η(i) arises)
to the effective action coefficient. Its failure at O1 means that the
modular origin of η(i) in B is not accessible by any currently known
derivation path.

---

## 6. Falsification Tests

The following experiments / calculations would resolve or falsify the claim:

| Test | What it would establish |
|------|------------------------|
| Two-loop calculation giving B_{2-loop} < 44 | Ruling out perturbative origin of B ≈ 46 via RG alone |
| Equal-action numerical check for p = 2,3,5 coset reps | Fast test of saddle-degeneracy mechanism (no O1 proof needed at leading order) |
| Proof that S[Θ] is NOT modular-covariant | Eliminates Hecke route entirely; forces a different mechanism |
| Derivation of c = 3 from S[Θ] via δ²S/δΘ² computation | Closes Gap G-c3; upgrades exponent 1/4 from observed to derived |
| Winding-sector partition function on T² giving n log n at leading order | Closes Gap G-nlogn; establishes the V_eff form independently |

---

## 7. Impact on the Broader G137-B Programme

The B_gap_final_verdict.md (2026-05-09) already records a CONDITIONAL verdict
on B(p) = (p+1)/3. The present analysis adds precision:

**The η(i) route does not bypass Gap G137-B — it reframes it.**
Instead of needing to derive μ(Γ₀(p))/3 from S[Θ], one needs to derive:
1. The n log n form of V_eff from the UBT partition function
2. c = 3 from S[Θ] as the effective central charge
3. The absorption of (2η(i))^{c/12} into the B coefficient (not just Z)

These three sub-gaps are **logically independent** of each other and of the
Hecke-equivariant route's obstructions O1–O3.

**Relationship to the modular index route**: The Chowla–Selberg value
B_CS = N_eff^{3/2} · (2η(i))^{1/4} ≈ 46.281 lies between the KK+winding
heuristic (43.6) and the modular index value (46.0), and is arithmetically
simpler — determined entirely by the Gaussian integer CM data at D = −4.
This suggests the η(i) formula may be the correct representation of B,
but this suggestion is not a proof.

---

## 8. Summary of Claim-by-Claim Verdicts

| Task claim | Verdict |
|-----------|---------|
| UBT effective sector has T² with τ=i | **CONDITIONAL** (shape: proved; scale: open) |
| Relevant determinant is det'Δ_{T²} with η(i) factor | **UNPROVED** (mathematical fact proved; physical relevance not) |
| Physical effective central charge c=3 | **OPEN** (counting argument only; not from S[Θ]) |
| Determinant contributes as (2η(i))^{c/12} | **OBSERVATION** (0.007% match; mechanism not derived) |
| Factor modifies B in n log n term | **UNPROVED** (n log n form itself not derived; insertion mechanism absent) |
| Exponent 1/4 from c/12, not fitting | **UNPROVED** (c=3 not derived; 1/4 effectively inferred) |

---

## 9. Final Verdict

$$\boxed{\textbf{CONDITIONAL\_WITH\_EXACT\_GAP}}$$

The η(i) Dedekind eta function at the self-dual CM point τ = i is the
**uniquely distinguished** special value (among all standard candidates)
giving a 0.007% match to B_required via the formula
B = N_eff^{3/2} · (2η(i))^{c/12} with c = 3, N_eff = 12.

The formula is:
- **Not a pure numerical coincidence** (precision 100× better than any
  competing candidate; structurally motivated by Chowla–Selberg and
  the self-dual torus geometry)
- **Not proved from S[Θ]** (three independent gaps: G-nlogn, G-c3, G-insertion)
- **Not a partition-function-only normalisation** (it is *proposed* as a
  B-modifier, but this proposal lacks a derivation)
- **Not rejected** (no falsification evidence; all numerical checks pass;
  the conditional τ=i derivation provides geometric support)

**The exact gap**: Three derivations are required before the verdict can
be upgraded to PROVED:

1. **G-nlogn**: Derive V_eff = n² − B n log n from the UBT partition
   function on T² (not from the direct CW determinant on S¹_ψ, which
   gives a hyperbolic form with minimum at n* ≈ 19, not 137).

2. **G-c3**: Prove c = 3 as the effective central charge of the UBT
   bosonic sector from the quadratic fluctuation operator δ²S[Θ]/δΘ² at
   the winding saddle, not from mode-counting heuristics.

3. **G-insertion**: Derive that (2η(i))^{c/12} multiplies the B coefficient
   (n-dependent term), not merely the n-independent partition-function
   normalisation Z₀ = (det'Δ_{T²})^{c/2}.

Until all three gaps are closed, the canonical statement is:

> B = N_eff^{3/2} · (2η(i))^{c/12} is the **best-supported candidate**
> for the missing correction factor to B, conditional on G-nlogn, G-c3,
> and G-insertion being resolved.

**No modification to canonical/ is warranted at this time.**

---

## 10. Recommended Next Action

Priority 1 (4-week time-box): Attempt to derive c = 3 from S[Θ] by
computing δ²S/δΘ² in the winding background and reading off the
coefficient of the log det'(−Δ) term. This is the narrowest of the three
gaps and success here would resolve G-c3 and upgrade the exponent 1/4
from observed to derived.

If G-c3 is closed, Priority 2: Attempt G-insertion by computing the
one-loop effective action W_eff[n] for a winding background n on T² at
τ = τ_n = in, taking the T-dual at n=1 to reach τ=i, and identifying
whether the η-function contribution enters the n-dependent or
n-independent part of W_eff.

If G-c3 fails within 4 weeks: Publish the prime-stability and integer-137
results as CONDITIONAL, citing η(i) as a strong structural candidate
for the missing correction factor with exact gap identified in this document.

---

## 11. References

| Document | Role |
|----------|------|
| `research_tracks/T3_ALPHA/cw_determinant_full_derivation.tex` | Exact CW det on S¹_ψ; min at n*≈19; n log n gap established |
| `research_tracks/T3_ALPHA/chowla_selberg_b_derivation.tex` | Chowla–Selberg formula; spectral det on T²; derivation steps S1–S8 |
| `research_tracks/alpha_spectral/b_coefficient_gap_resolution.tex` | Synthesis of all B routes; CONDITIONAL verdict on B=(p+1)/3 |
| `research_tracks/alpha_spectral/self_dual_torus_derivation.tex` | Conditional derivation of τ=i as shape stationary point |
| `research_tracks/alpha_spectral/hecke_equivariant_path_integral.tex` | Hecke NO-GO; obstructions O1–O3 |
| `reports/B_gap_final_verdict.md` | CONDITIONAL verdict on B(p)=(p+1)/3 |
| `reports/alpha_missing_lemma.md` | Formal statement of Gap G137-B |
| `reports/alpha_current_verdict.md` | Current alpha programme status |
| `tools/verify_b_eta_uniqueness.py` | Numerical scan: η(i) vs. 60 other candidates |
