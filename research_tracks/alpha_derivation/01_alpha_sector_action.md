<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Phase 1 — Alpha-sector action extraction

## Canonical action to use

From `canonical/THEORY/canonical/canonical_action.tex`, the UBT action is

\[
S[\Theta]=\int_{\mathcal M} d^4x\,\sqrt{-g}\,\mathcal L_{\mathrm{UBT}},
\qquad
\mathcal L_{\mathrm{UBT}}=\frac{1}{2\kappa}R + \mathrm{Tr}[(D_\mu\Theta)^\dagger(D^\mu\Theta)] - \frac14 F^a_{\mu\nu}F^{a\mu\nu} - V(\Theta).
\]

The fully biquaternionic form used for compact imaginary-time analysis is

\[
S[\Theta]=\int d^4x\,d\psi\,\mathrm{Re}\,\mathrm{Tr}\left[(\nabla^\dagger\Theta)^*(\nabla^\dagger\Theta)-V(\Theta)\right].
\]

## Minimal alpha-sector truncation

For winding analysis on the compact phase circle, use the sector

\[
S_\alpha[\Theta_n,A]\;=\;\int d^4x\,d\psi\;\mathrm{Sc}\Big[(D_\mu\Theta_n)^\dagger(D^\mu\Theta_n)\Big] + S_{\mathrm{1loop}}[\Theta_n,A],
\]

with \(\Theta_n\sim e^{in\psi}\), and one-loop effective action from the quadratic fluctuation operator around \(\Theta_n\):

\[
\mathcal D_n = -\nabla^\dagger\nabla + \mathcal M_n^2 + \mathcal U_{\mathrm{curv/gauge}}.
\]

## Must-answer items

### 1) What is the field variable?
- Fundamental field: \(\Theta(q,\tau)\in\mathbb C\otimes\mathbb H\), with canonical complex time \(\tau=t+i\psi\).
- Alpha sector: winding background modes \(\Theta_n\) on compact \(\psi\)-fiber.

### 2) What is the relevant operator?
- Kinetic/unified operator: \(\nabla^\dagger\nabla\) (canonical Theta equation).
- One-loop determinant operator in background \(n\): \(\mathcal D_n\) above.

### 3) What is the spectrum indexed by \(n\)?
- Winding/KK-like sector on compact \(S^1_\psi\), \(\Theta\propto e^{in\psi}\).
- Representative eigenvalue structure: \(\lambda_{k,n}\sim k^2 + n^2 + \text{curvature/gauge shifts}\) (units with \(R_\psi=1\)).

### 4) Why should the effective potential contain \(n^2\)?
- Classical winding gradient energy from \(|\partial_\psi\Theta_n|^2\) scales as \(n^2\).
- This is the canonical baseline used across alpha-route documents.

### 5) Why should it contain \(n\log n\)?
- Not from single-particle \(S^1\) determinant alone (that gives \(\log n\)-type terms).
- Canonical no-go analysis attributes \(n\log n\) to 4D one-loop/RG accumulation over \(n\)-winding quanta (or equivalent entropy/Stirling interpretation under additional dynamical assumptions).

### 6) What is currently responsible for \(B_0=8\pi\)?
- One-loop vacuum-polarization counting route in canonical alpha/n_eff chain gives
  \(B_0 = 2\pi N_{\mathrm{eff}}/3 = 8\pi\) for \(N_{\mathrm{eff}}=12\).
- This is the baseline coefficient currently used before missing correction \(\Delta B\).

## Phase-1 conclusion

The alpha-sector operator and action are identifiable from canonical UBT primitives. The unresolved part is not the existence of \(n^2\) and baseline \(B_0\), but the non-fitted derivation of a constant correction \(\Delta B\approx 21.151\).
