<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: ../../AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Verification record — canonical generalized-Dirac action-origin step

This record follows `docs/DERIVATION_VERIFICATION_POLICY.md`.

| Claim / equation | Analytic status | Tool | Artifact | Version | Result | Scope | Limitation | Lean status |
|---|---|---|---|---|---|---|---|---|
| Nondegenerate quadratic first-jet kinetic term gives a genuinely second-order Euler–Lagrange principal part | theorem in `action_origin_obstruction.tex` | SymPy | `tools/verify_generalized_dirac_action_order.py` | SymPy 1.14.0 in agent runtime | PASS | Exact velocity-Hessian and finite-dimensional principal-Hessian identities | Does not derive the physical UBT coefficients or global PDE theory | LEAN-PENDING |
| Same order obstruction, independent formulation | analytic theorem | Python standard library exact arithmetic | `tools/verify_generalized_dirac_action_order_independent.py` | Python runtime; `fractions.Fraction` | PASS | Independent exact discrete Hessian and nonzero Kronecker determinant instance | Finite-dimensional cross-check, not a general formal proof | LEAN-PENDING |
| Exact second-order factorisation does not imply either first-order factor | theorem/counterexample in `action_origin_obstruction.tex` | SymPy | `tools/verify_generalized_dirac_action_order.py` | SymPy 1.14.0 | PASS | Substitutes both exact exponential solutions into the factorised operator and one first-order factor | Toy model establishes the logical non-implication, not a UBT-specific spectrum theorem | LEAN-PENDING |
| Same factorisation non-implication, independent formulation | analytic theorem | Python standard library integer arithmetic | `tools/verify_generalized_dirac_action_order_independent.py` | Python runtime | PASS | Checks characteristic polynomial roots ±m and the single root of one factor exactly | Characteristic-polynomial formulation only | LEAN-PENDING |

## Lean status

**LEAN-PENDING.** The execution environment used for this patch was checked on
20 August 2026 and contained neither a `lean` nor a `lake` executable.  GitHub
code search also exposed no repository `lean-toolchain` or `lakefile` at the
start of this patch.  Therefore no statement in this branch is labelled
"Lean verified" or "formally proved".

Formalisation targets, in order:

1. the finite-dimensional linear-algebra lemma that a nonzero/nondegenerate
   velocity Hessian supplies a nonzero second-jet Euler–Lagrange principal
   coefficient;
2. the algebraic implication failure
   `(D-m)(D+m)f=0 ↛ (D+m)f=0`, represented by the two characteristic roots;
3. after a repository Lean toolchain is established, the already existing
   constrained-rank theorem `rank(Dg|A)=dim(A+K)-6`.

A generated but uncompiled `.lean` file is intentionally not committed merely
to satisfy the policy cosmetically.  The policy requires an actually checked
Lean proof before claiming formal verification.

## Reproduction

```bash
python tools/verify_generalized_dirac_action_order.py
python tools/verify_generalized_dirac_action_order_independent.py
pytest -q tests/test_generalized_dirac_action_order.py
```

## Scientific interpretation

The checks verify an **order-of-variation obstruction** for the currently
documented nondegenerate quadratic kinetic action and a logical limitation of
operator factorisation.  They do not prove that every possible `Theta`-only UBT
action is second order.  A specially derived degenerate first-order action,
chain-rule cancellation, or a derived branch-selection theorem remains a valid
route and is the next research target.
