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
- the curved Clifford relation from the canonical metric relation;
- rank 10 of `E -> g` at every nondegenerate tetrad and the six-dimensional
  Lorentz kernel;
- an exact grading/fifth matrix anticommuting with all lifted four-dimensional
  Clifford generators.

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
- preservation of the Lorentz slice and rank 10 on shell;
- Einstein and quantum low-energy limits from the same action.

## Historical branch

The former spinor-current tetrad and its exact off-shell Jacobian calculations
are retained at:

`research_tracks/history/legacy_spinor_current_tetrad_2026-07-26/`

They are useful comparative mathematics but are not the active UBT metric
mechanism.
