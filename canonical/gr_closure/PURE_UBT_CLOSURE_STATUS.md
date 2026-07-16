# UBT GR Closure Status — Covariant-Tetrad Route

**Date:** 2026-07-16  
**Canonical route:** local covariant tetrad, unique connection reconstruction,
and two-sided integrability; not compact-fiber averaging.

## Canonical chain

\[
\Theta(q,\tau)
\to E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta
\to \tfrac12\{E_\mu,E_\nu\}_\sharp=g_{\mu\nu}\mathbf1
\to \omega(e,T)
\to [D_\mu,D_\nu].
\]

## Closed results

- **GAP-10K — CLOSED locally.** The nondegenerate tetrad-to-metric map has
  rank ten and a six-dimensional local-Lorentz kernel.
- **GAP-10Ω-KIN — CLOSED [L1].** For specified tetrad and torsion,
  \(\omega=\mathring\omega(e)+K(T)\) is the unique metric-compatible frame
  connection, up to local Lorentz gauge.
- **GAP-10Ω-GR — CLOSED [L1].** The torsion-free classical branch has
  \(K=0\) and the unique Levi-Civita spin connection.
- **GAP-10L-CONN — CLOSED [L1].** Metric-compatible Lorentz transport
  preserves \(\eta\) and the real Lorentz slice.
- **GAP-10I-SR — CLOSED [L1].** Every constant Lorentz tetrad has the affine
  representer
  \(\Theta=\Theta_0+\sqrt{\mathcal N_0}E_\mu x^\mu\).
- **GAP-10I-1S — CLOSED AS NO-GO [L1].** A naive one-sided regular connection
  with invertible \(\Theta\) forces zero curvature under torsion-free
  compatibility.
- **Two-sided curvature identity — PROVED [L1].** For
  \(D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu\),
  \[
  [D_\mu,D_\nu]\Theta=F^A_{\mu\nu}\Theta-\Theta F^B_{\mu\nu}.
  \]

## Newly closed conditional subgaps

- **GAP-10T-PALATINI — CLOSED CONDITIONALLY [L1]:** the minimal first-order
  Cartan equation has an invertible 24-component torsion map; zero spin current
  gives zero torsion and a specified spin current gives unique contorsion.
- **GAP-10L-SYM — CLOSED CONDITIONALLY [L1]:** the Lorentz slice is the fixed
  set of \(\mathcal JX=-\overline{X^\sharp}\) and is propagated by every
  unique equivariant evolution with fixed data.
- **GAP-10I-PRESCRIBED — CLOSED [L1]:** for specified \((E,A,B)\), existence
  and path independence are exactly controlled by augmented holonomy.
- **GAP-10D-PALATINI / GAP-10D-UNIQUENESS — CLOSED CONDITIONALLY [L1]:** the
  minimal first-order action yields Einstein--\(\Lambda\), and Lovelock
  assumptions make that infrared metric equation unique.
- **GAP-10ψ-KIN — CLOSED [L1]:** a psi-flow tangent to a local Lorentz orbit
  leaves the metric invariant.
- **GAP-10ψ-SYM — CLOSED CONDITIONALLY [L1]:** unique psi-translation-invariant
  dynamics preserves psi-independent data.

## Narrowed or open results

- **GAP-10I-2S — NARROWED:** two-sided action avoids the flatness obstruction,
  but the canonical action must fix the paired left/right connections and
  involution.
- **GAP-10T-DYN — NARROWED:** derive the minimal first-order branch, exact spin
  current, normalization, and possible torsion dynamics from canonical UBT.
- **GAP-10L-DYN — NARROWED:** verify equivariance and well-posed uniqueness for
  the complete UBT equations and sources.
- **GAP-10I-CURVED — NARROWED:** self-consistent on-shell generation,
  regularity, and global continuation remain open.
- **GAP-10D — NARROWED:** derive the Palatini/Lovelock infrared assumptions,
  coefficients, and matter coupling from the canonical action.
- **GAP-10ψ — NARROWED:** show that canonical dynamics realizes a sufficient
  stability mechanism and excludes unstable physical psi modes.
- **GAP-U2Θ and GAP-B-MASTER — OPEN.**

## Fiber branch

`pure_ubt_fiber_closure.tex`, `linearised_fiber_closure.tex`, and the associated
rank checker are retained for historical and comparative research. Their
mathematics is not deleted, but compact-fiber averaging is not the canonical
metric or the primary GR-closure mechanism.
