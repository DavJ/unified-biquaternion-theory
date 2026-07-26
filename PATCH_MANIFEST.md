# UBT no-extra-variable rank patch manifest

Baseline: `unified-biquaternion-theory-master(36).zip`
Date: 2026-07-27

The patch preserves the canonical route

`Theta -> E_mu=N0^(-1/2)D_mu Theta -> g_mu_nu`

and introduces no independent field or auxiliary variable.

## Exact results

1. For the admissible tetrad tangent space
   `A={de: F_e de in im F_Psi}` and Lorentz kernel `K=ker D_e g`,
   `rank(D_e g|A)=dim(A+K)-6`.
2. Full rank ten is equivalent to `A+K=R^16`.
3. Invertible `F_Psi` preserves pointwise first-jet rank ten using only the
   value of the original `Theta` field.
4. Nonzero scalar and scalar-pseudoscalar generalized-Dirac zero-order blocks
   are explicit sufficient realizations.
5. Eight independent real constraints acting only on the tetrad imply metric
   rank at most eight.

## Remaining boundary

Derivation of the required zero-order block/transversality from the canonical
UBT action and local existence/integrability of the implicit holomorphic PDE
remain open.
