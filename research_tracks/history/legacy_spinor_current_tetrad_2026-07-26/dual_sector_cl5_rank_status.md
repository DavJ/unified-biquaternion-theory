# Dual-sector Clifford-5 generalized-Dirac architecture

## 1. Proof-status summary

### Proved as standard algebra

Let \(\mathbb B=\mathbb C\otimes\mathbb H\cong\operatorname{Mat}(2,\mathbb C)\).
Then

\[
\operatorname{End}_{\mathbb C}(\mathbb B)
\cong \mathbb B\otimes\mathbb B^{\mathrm{op}}
\cong \operatorname{Mat}(4,\mathbb C)
\cong \mathrm{Cl}_4(\mathbb C).
\]

For odd complex Clifford dimension five,

\[
\mathrm{Cl}_5(\mathbb C)
\cong \operatorname{Mat}(4,\mathbb C)\oplus
       \operatorname{Mat}(4,\mathbb C).
\]

The two simple ideals are selected by the central volume-element projectors

\[
P_\pm=\frac12(1\pm\Omega_5).
\]

A faithful two-branch spinor carrier has complex dimension eight and is
therefore vector-space isomorphic to

\[
\mathbb B_+\oplus\mathbb B_-
\cong\mathbb C^8
\cong(\mathbb C^2)^{\otimes3}.
\]

The fermionic/exterior grading of three modes gives

\[
\Lambda^\bullet\mathbb C^3
=\Lambda^0\oplus\Lambda^1\oplus\Lambda^2\oplus\Lambda^3,
\qquad
1+3+3+1,
\]

and under the standard \(SU(3)\) action this is

\[
\mathbf 1\oplus\mathbf 3\oplus\bar{\mathbf 3}\oplus\mathbf 1.
\]

These facts do not by themselves identify the two ideals with two physical
universes or prove QCD dynamics.

## 2. Correction to the naive rank argument

For a value-only map

\[
\Theta(x)\in\mathbb B\longmapsto g_{\mu\nu}(x),
\]

one has the elementary bound

\[
\operatorname{rank}D_\Theta g\le 8.
\]

This bound does **not** apply to a first-jet map depending on
\((\Theta,D_\mu\Theta)\). A spacetime one-form index can arise from the
covariant derivative, while the Lorentz index arises from the Clifford
matrices.

The mnemonic

\[
16-6=10
\]

is compatible with a 16-real-component dual carrier modulo a six-parameter
Lorentz orbit, but it is not a proof that the quotient is the space of metrics.
The correct proof test is the Jacobian rank of an explicit composite map.

## 3. Single-sector composite tetrad

For a Dirac/biquaternionic spinor \(\theta\), define the real current tetrad

\[
E_\mu{}^a[\theta]
=
\operatorname{Re}\!\left[
\frac{i}{2}\left(
\bar\theta\gamma^a D_\mu\theta
-
\overline{D_\mu\theta}\,\gamma^a\theta
\right)
\right].
\]

Then

\[
g_{\mu\nu}[\theta]
=E_\mu{}^a\eta_{ab}E_\nu{}^b.
\]

At the explicit integer first-jet witness stored in the verifier,

\[
\det E=4452\ne0,
\]

and a specified exact \(10\times10\) minor of

\[
D_{J^1\theta}(g_{00},g_{01},\ldots,g_{33})
\]

has determinant

\[
9016261632000\ne0.
\]

Therefore this particular polynomial first-jet map has generic off-shell rank
10 on a nonempty open set.

### What this theorem does not prove

It does not yet prove rank ten after imposing:

- the generalized UBT Dirac equation;
- holomorphy or other constraints in \(\tau=t+i\psi\);
- normalization, reality, gauge, or sector-selection constraints;
- a self-consistent spin connection reconstructed from the same composite
  tetrad;
- the Einstein equations from the canonical UBT action.

## 4. Dual-sector cross-current

For two sectors \(\theta_+\) and \(\theta_-\), define

\[
\begin{aligned}
E_\mu{}^a[\theta_+,\theta_-]
=\operatorname{Re}\!\left[\frac{i}{2}\big(&
\bar\theta_-\gamma^aD_\mu\theta_+
-
\overline{D_\mu\theta_-}\gamma^a\theta_+
\\
&+\bar\theta_+\gamma^aD_\mu\theta_-
-
\overline{D_\mu\theta_+}\gamma^a\theta_-
\big)\right].
\end{aligned}
\]

At the exact witness in the verifier,

\[
\det E=327\ne0,
\]

and the selected metric-Jacobian minor is

\[
68394848345664\ne0.
\]

Hence the dual cross-current also has generic off-shell metric rank ten.

## 5. Consequences

1. **Rank:** dual-sector independence is not required solely for rank ten;
   one spinor first jet already supplies a rank-ten witness.
2. **Clifford-5:** the dual sector remains natural if the complete
   \(\mathrm{Cl}_5(\mathbb C)\) algebra, rather than one irreducible branch, is
   physically required.
3. **Complex time:** a fifth generalized-Dirac channel may be associated with
   \(D_\psi\), but this is a physical postulate until its role is derived.
4. **Three qubits/SU(3):** \(\mathbb C^8\) naturally carries the
   \(1\oplus3\oplus\bar3\oplus1\) grading. This is a representation theorem,
   not yet a derivation of confinement, QCD dynamics, or an error-correcting
   code.
5. **QEC:** the existing one-hot color sector detects individual \(X_i,Y_i\)
   leakage but fails the Knill-Laflamme conditions for correcting an unknown
   single bit flip. A second/outside coding layer is still needed for genuine
   correction.

## 6. Canonical decision gate

Do not merge this track into canonical UBT until all of the following are
proved:

- a covariant generalized-Dirac action over \(\tau=t+i\psi\);
- preservation of rank ten on the physical on-shell constraint surface;
- closure of the implicit \(\theta\to E\to\omega(E)\to D\theta\) system;
- Lorentzian signature and nondegeneracy on the admitted branch;
- the GR/Einstein low-energy equations;
- compatibility with the existing SU(3), quantum, and Layer-2 coding tracks.
