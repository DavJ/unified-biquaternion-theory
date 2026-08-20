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

# Canonical-relation generalized-Dirac programme

**Active research direction — updated 20 August 2026**

This track continues one geometric construction only:

\[
\Theta
\longrightarrow
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta
\longrightarrow
\begin{cases}
 g_{\mu\nu}\mathbf1
 =\tfrac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu),\\[1mm]
 \Gamma_\mu=\mathcal C(E_\mu),
 \quad\tfrac12\{\Gamma_\mu,\Gamma_\nu\}=g_{\mu\nu}I_4.
\end{cases}
\]

The curved Clifford matrices and the generalized Dirac operator are derived
from the same canonical covariant tetrad. They are not a second tetrad
construction.

## Proved now

- the central biquaternionic metric identity on the Lorentz slice;
- the exact injective block lift `E -> Gamma(E)`;
- the fixed vector-space identification `Psi=vec(Theta) in C^4`, showing that
  the lifted matrices act on the same UBT field rather than on a new field;
- the curved Clifford relation from the canonical metric relation;
- rank 10 of `E -> g` at every nondegenerate tetrad and the six-dimensional
  Lorentz kernel;
- an exact grading/fifth matrix anticommuting with all lifted four-dimensional
  Clifford generators;
- exact four- and five-channel principal-symbol factorisation, so the lifted
  Dirac characteristic cone equals the canonical UBT metric null cone;
- a conditional first-jet theorem: when the field equation is in an independent
  `psi`-normal form, the fifth channel can be solved uniquely and does not
  reduce the rank-ten spacetime tetrad data;
- the exact no-extra-field constrained-rank formula
  `rank(Dg|A)=dim(A+K)-6`, with full rank iff `A+K=R^16`;
- invertible dependence of the equation on the value `Psi=vec(Theta)` of the
  original field preserves pointwise first-jet rank ten, and nonzero scalar or
  scalar-pseudoscalar zero-order blocks realize this condition explicitly;
- eight independent real first-order constraints acting only on the tetrad
  reduce the metric rank to at most eight;
- **action-order obstruction:** the presently documented nondegenerate
  quadratic first-derivative `Theta` kinetic action has a genuinely second-order
  Euler--Lagrange principal part, so it cannot directly yield a genuinely
  first-order generalized-Dirac equation on the same field;
- exact factorisation of that second-order operator is not by itself enough to
  select one first-order Dirac factor.

The last two items are proved analytically in
`action_origin_obstruction.tex` and independently checked by an exact SymPy
script and a separate no-SymPy exact-arithmetic checker.

Run:

```bash
python tools/verify_canonical_relation_dirac_lift.py
python tools/verify_no_extra_variable_rank.py
python tools/verify_generalized_dirac_action_order.py
python tools/verify_generalized_dirac_action_order_independent.py
pytest -q \
  tests/test_canonical_relation_dirac_lift.py \
  tests/test_no_extra_variable_rank.py \
  tests/test_generalized_dirac_action_order.py
```

## Current closure target

The rank count is no longer the main blocker.  The immediate theorem-level
problem is to derive, without additional physical fields, one of the following
from canonical UBT:

1. a degenerate first-order variational structure whose chain-rule terms cancel
   the second-jet principal part even though `Gamma=Gamma(DTheta)`;
2. an exact factorisation of the second-order master operator plus an independently
   derived boundary/positivity/holomorphy/chirality principle that selects one
   generalized-Dirac factor; or
3. an equivalent `Theta`-only constrained variational principle with a proved
   one-to-one equivalence of solution sets.

Only after that step is established does the no-extra-field rank theorem decide
whether the resulting on-shell equation preserves rank ten through the exact
transversality condition `A+K=R^16`.

## Still open

- derivation of the full generalized-Dirac equation from the UBT action in one
  of the three precise senses above;
- proof that the selected equation has invertible original-field Jacobian
  `F_Psi`, or otherwise satisfies `A+K=R^16`;
- the precise physical role and signature of the complex-time `psi` channel;
- local existence/integrability of the resulting implicit holomorphic PDE and
  preservation of the Lorentz slice;
- Einstein and quantum low-energy limits from the same action.

## Verification status

`docs/DERIVATION_VERIFICATION_POLICY.md` is binding for this track.  For the
new action-order theorem, two executable exact checks are provided.  Lean is
**LEAN-PENDING** for this patch because the execution environment used by the
agent contains neither `lean` nor `lake`, and no repository Lean toolchain was
available through code search.  No uncompiled Lean-looking source is presented
as a formal proof.  The formalisation target is recorded in
`verification/generalized_dirac_action_origin.md`.

## Historical branch

The former spinor-current tetrad and its exact off-shell Jacobian calculations
are retained at:

`research_tracks/history/legacy_spinor_current_tetrad_2026-07-26/`

They are useful comparative mathematics but are not the active UBT metric
mechanism.
