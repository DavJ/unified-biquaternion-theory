<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# PRIMARY_ROUTE.md — Single Strongest Alpha Derivation Route

**Author**: Ing. David Jaroš  
**Date**: 2026-04-28  
**Track**: T3_ALPHA — Fine Structure Constant  
**Purpose**: Commit to one primary route.  All weaker routes are explicitly killed.
**Source analysis**: `canonical/alpha/alpha_derivation_routes.md`,
`canonical/alpha/prime_137_status.md`, `reports/alpha_routes_ranked.md`

---

## Decision

**Primary route**: **V_eff Prime Attractor (Route A_PRIME)**

**Single publishable claim**: α⁻¹_bare = 137 (integer) from UBT without fitting,
conditional on one missing lemma (Gap G137-B: derivation of the effective
coupling parameter B).

**No other route is being pursued as primary.**

---

## What the Primary Route Claims

The effective potential for winding modes on the imaginary-time circle S¹_ψ is:

```
V_eff(n) = n² − B · n · ln n
```

The minimum of V_eff selects a preferred winding number n* satisfying:

```
2n* = B(ln n* + 1)
```

**Proved facts in this route** (no fitting, zero free parameters):

| Claim | Status | Source |
|-------|--------|--------|
| Three winding modes (N_eff = 12 candidate) | **OPEN/[MC] under critical audit** | `canonical/n_eff/step2_AUDIT.tex` |
| The prime status of n* is a stability condition for V_eff | **[L1] Proved** | `canonical/alpha/alpha_best_route.tex` |
| n*(B_phenom) = 137 for B_phenom ≈ 46.298 | **[L1] Conditional** (given B) | `canonical/alpha/alpha_best_route.tex` |
| 137 is prime — consistent with stability | **[L0]** (number theory) | Standard |
| B₀ = 8π (one-loop UBT effective coupling) | **[L1] Proved** | `canonical/t_munu/` |
| **B_phenom ≈ 46.298 from UBT axioms** | **[L2] OPEN (Gap G137-B)** | `canonical/alpha/prime_137_status.md` |

**Bottom line**: The route is internally consistent and produces n* = 137 when
B = B_phenom.  The gap is deriving B_phenom from UBT first principles.
B₀ = 8π gives n* ≈ 65, not 137; the gap is the factor ≈ 1.84 between them.
`B_Ram` is **OBS only, not derived from S[Theta]**. `lambda_exact` and
`lambda_frac` are **OBS only, no derivation currently known**.

---

## Why This Route Is Primary

1. **Deepest foundation**: N_eff = 12 is a motivated mode-counting candidate, currently OPEN/[MC] under critical audit; see canonical/n_eff/step2_AUDIT.tex.
   V_eff structure has a motivated winding / prime-entropy route, but the full derivation from S[Theta] remains conditional.
   The prime-attractor argument is structural, not ad hoc.

2. **Integer result is already publishable**: The claim "α⁻¹_bare = 137 (integer)
   from UBT structural argument" is a conditional but precise result.
   A short paper making this claim — with the B gap explicitly stated — is
   more credible than claiming 137.036 without a proof.

3. **Two independent corroborations exist**: The prime 137 also appears in
   (a) the modular curve μ(Γ₀(137))/3 ≈ B_phenom (error 0.64%), and
   (b) Hecke eigenvalues reproducing lepton mass ratios to 0.02–0.1%.
   These are independent of V_eff and non-trivially reinforce the selection.

4. **Clear, testable missing lemma**: Gap G137-B is precisely stated (see
   `reports/alpha_missing_lemma.md`).  If solved, the route becomes [L1].
   If failed, the route is explicitly downgraded.

5. **All competing routes are either conditional on the same gap (A1, A2)
   or definitively failed (A3, A4)**: See `reports/alpha_routes_ranked.md`.

---

## Killed Routes

### Route A1 (Gauge Normalization) — KILLED AS INDEPENDENT ROUTE

Status: Conditional on Gap EW-1 (tan θ_W from algebra).
Gap EW-1 depends on fixing g'/g ratio, which has resisted all algebraic
approaches.  This route does NOT independently determine α.
It is subsumed in the T2_GAUGE track (chirality/EW mixing paper).

### Route A2 (Symmetry-Breaking Projection) — KILLED AS INDEPENDENT ROUTE

Status: Conditional on the same Gap EW-1.
Identical blocking mechanism as A1.  Killed for the same reason.

### Route A3 (Theta/Modular Route) — **DEFINITIVELY FAILED**

Status: Failed.  
Exhaustive search: no modular invariant or Hecke eigenvalue produces
α⁻¹ = 137.036 from complex-time structure alone.
The integer 137 as a modular feature (via V_eff / P¹(𝔽₁₃₇)) is already
captured by Route A_PRIME.  No independent content remains.
**This route is closed.**

### Route A4 (Layer 2 Coding Constraint) — **DEFINITIVELY FAILED**

Status: Failed.  
Coding constraints fix charge quantization (integer multiples of a unit
charge) but cannot fix the magnitude of the unit charge.
α = e²/(4π) requires coupling magnitude, not just charge spectrum.
**This route is closed.**

---

## Honest Probability Assessment

| Scenario | P(success) | Outcome |
|----------|-----------|---------|
| Gap G137-B solved in 4-week modular bootstrap | 20–30% | Route becomes [L1]; paper claims α⁻¹_bare = 137 proved |
| Gap G137-B not solved | 70–80% | Route publishes as conditional: "integer 137 from structural argument, B gap explicit" |
| Route A_PRIME independently falsified | < 5% | N_eff = 12 candidate would need to fail critical audit (currently OPEN/[MC]) |

**Expected state in 4 weeks**: conditional claim at ~85% probability.
Definitive proof at ~25% probability.

---

## Recommended Publication Strategy

**Option 1 (preferred)**: Time-box 4 weeks for Gap G137-B (modular bootstrap
approach: derive B = μ(Γ₀(n*))/3 from S[Θ] evaluated at n*).  If closed,
publish as clean integer α result.  If not, publish as:

> *"UBT predicts α⁻¹_bare = 137 from the prime-attractor structure of the
> winding-mode spectrum, given the effective coupling B = B_phenom.  The
> derivation of B from the UBT action is an open problem (Gap G137-B)."*

**Option 2 (fallback)**: Publish the integer-137 structural result as a
companion note to T1_GR, not as a standalone paper.  This avoids the
impression that the α claim is in the same completion state as the GR result.

---

## References

- `canonical/alpha/alpha_derivation_routes.md` — full route survey
- `canonical/alpha/prime_137_status.md` — prime 137 structural roles
- `canonical/alpha/alpha_best_route.tex` — V_eff derivation chain
- `reports/alpha_routes_ranked.md` — ranked comparison of all routes
- `reports/alpha_missing_lemma.md` — exact statement of Gap G137-B
- `FLAGSHIP_SELECTION.md` — context for why T3_ALPHA is not primary flagship


Cross-references: `canonical/alpha/gamma_entropy_alpha_refinement_status.tex`, `reports/gamma_entropy_alpha_interpolation_audit.md`.
