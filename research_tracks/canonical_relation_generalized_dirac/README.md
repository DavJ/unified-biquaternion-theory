# Canonical-relation generalized-Dirac programme

**Active research direction — 2026-07-27**

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
- an exact constrained-rank projection theorem: the on-shell rank is the rank
  of `D_e g` on tetrad variations whose equation residual can be absorbed by
  nonmetric variables; a surjective nonmetric block preserves rank 10;
- a rank-budget no-go: eight independent real constraints acting only on the
  16 tetrad coefficients leave metric rank at most eight.

Run:

```bash
python tools/verify_canonical_relation_dirac_lift.py
pytest -q tests/test_canonical_relation_dirac_lift.py
```

## Still open

- derivation of the full generalized-Dirac operator from the UBT action;
- the precise physical role and signature of the complex-time `psi` channel;
- local existence of the self-consistent implicit system
  `Theta -> E -> Gamma -> omega(E) -> D Theta`;
- derivation of the real holomorphic constraint Jacobian `(F_e, F_z)` from
  the action and verification of the exact projection criterion;
- preservation of the Lorentz slice and rank 10 for the fully constrained
  holomorphic on-shell system;
- Einstein and quantum low-energy limits from the same action.

## Historical branch

The former spinor-current tetrad and its exact off-shell Jacobian calculations
are retained at:

`research_tracks/history/legacy_spinor_current_tetrad_2026-07-26/`

They are useful comparative mathematics but are not the active UBT metric
mechanism.
