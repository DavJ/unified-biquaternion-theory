<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
<!-- Licensed under CC BY-NC-ND 4.0. See LICENSE.md. -->

# External Audit: T1_GR Paper — July 2026

**Date:** July 2026  
**Reviewer:** External (GPT-assisted audit)  
**File reviewed:** `papers/UBT_GR_Submission.tex`  
**Verification tool output:** `tools/verify_schwarzschild_theta.py` reports `g_tt: OPEN`

---

## Summary

The July 2026 external audit identified several claim-level mismatches between
the paper's stated status and what is actually proved in the repository. The
findings motivated the honest-status reframe implemented in v10.1.4.

---

## Findings

### F1 — GAP-10 mis-characterised as non-blocking

**Finding:** The paper stated "None of [the open problems] affect the validity
of the Main Theorem or Theorems 1–4." However, GAP-10 (off-shell Θ-only
closure) is a *classical variational-equivalence question*: without control of
the image of the variational map δΘ → δg_μν[δΘ], stationarity of the total
action under available variations has not been shown to imply the full Einstein
equations from Θ alone. The earlier characterisation ("off-shell path-integral
sector") understated the classical nature of the obstruction.

**Resolution:** GAP-10 box text updated; Open Problems preamble rewritten.

---

### F2 — GAP-U2: Temporal Schwarzschild component unverified

**Finding:** `tools/verify_schwarzschild_theta.py` reports `g_tt: OPEN`.
The relation ∂_ψΘ₀ = iΦΘ₀ is used to obtain g_tt = −Φ² but has not been
derived from the field equation ∇†∇Θ = 0 and boundary conditions.

**Resolution:** GAP-U2 named and boxed in §6 (Open Problems). Abstract and
Key Claims item 5 updated to "spatial Schwarzschild reconstruction" only.

---

### F3 — GAP-B: Perturbation bridge is an assumption

**Finding:** The reduction of linearised UBT to Regge–Wheeler and Zerilli
equations uses the identification δ(∇†∇Θ) → δG_μν. This is not derived from
linearised UBT dynamics; it is an assumption. The paper presented the reduction
as "[L1] Proved" without flagging this bridge.

**Resolution:** GAP-B named and boxed in §6. RW and Zerilli labels updated
to "[L1 cond. given GAP-B]". Key Claims item 6 rewritten.

---

### F4 — GAP-U1: Uniqueness of metric bilinear (lower priority)

**Finding:** The metric bilinear ⟨∂_μΘ, ∂_νΘ⟩_η involves a choice of
bilinear form on the four-dimensional real projection. Alternative admissible
forms are not ruled out in the paper, yet no uniqueness argument is provided.

**Resolution:** GAP-U1 added to the lower-priority gaps table in §6.

---

### F5 — Title and abstract overclaim

**Finding:** The original title "General Relativity as a Real-Projected Limit
of Unified Biquaternion Theory" and abstract opening "We prove that Einstein's
field equations … emerge" overstate the result given F1–F3.

**Resolution:** Title and abstract replaced with honest formulations.

---

## Conclusion

After implementing the honest-status reframe (v10.1.4), the paper accurately
represents the state of the derivation: steps 1–4 proved, step 5 conditional on
GAP-10, spatial Schwarzschild proved, temporal and perturbation sectors open.
No scientific content (equations, proofs, theorem statements) was changed.


## Implemented resolutions — pure-Theta closure revision (2026-07-14)

- Replaced the local metric denominator, which forced `g_00=-1`, by a constant asymptotic normalization.
- Distinguished the raw biquaternionic quadratic tensor from its scalar/real metric projection.
- Derived the exact total pure-Theta Euler-Lagrange equation.
- Proved a fixed-psi rank no-go and a local compact-psi fiber-free closure theorem.
- Split GAP-10 into the closed local kinematic result and open single-action, selected-Jacobi, and global sub-gaps.
- Corrected the Abelian current and withdrew the claim that an ordinary Maxwell equation generates vacuum Schwarzschild.
- Replaced GAP-U2 language by the static-vacuum lapse theorem plus the open canonical-Theta dynamical bridge.
