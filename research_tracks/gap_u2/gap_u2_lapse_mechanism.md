# GAP-U2: corrected status of the Schwarzschild lapse

Date: 2026-07-14

## What is closed

For a static vacuum metric

\[
ds^2=-N^2dt^2+h_{ij}dx^idx^j,
\]

the vacuum Einstein equations imply

\[
\Delta_hN=0,\qquad R_{ij}(h)=N^{-1}D_iD_jN.
\]

For the isotropic Schwarzschild spatial metric

\[
h_{ij}=\Psi^4\delta_{ij},\qquad \Psi=1+\frac{M}{2r},
\]

spherical symmetry gives

\[
\partial_r\left(r^2\Psi^2N'\right)=0.
\]

Therefore

\[
N=D-\frac{C}{r+M/2}.
\]

Asymptotic flatness fixes `D=1`. The horizon condition `N(M/2)=0`, or equivalently ADM matching `N=1-M/r+O(r^-2)`, fixes `C=M`. Thus

\[
N(r)=\frac{1-M/(2r)}{1+M/(2r)}.
\]

**Status:** `GAP-U2S CLOSED CONDITIONALLY` on the already established static vacuum GR branch, the spatial Schwarzschild metric, and the boundary data.

## What is not closed

It remains to derive a fiber-resolved `Theta(q,t+i psi)` configuration from the canonical UBT Euler–Lagrange equation whose induced temporal metric is `g_tt=-N^2`.

**Status:** `GAP-U2Theta OPEN`.

## Maxwell correction

The former claim that a generic source-free `U(1)_psi` Maxwell equation directly gives the Schwarzschild lapse is withdrawn.

- The corrected Abelian current is derived in `derive_connection_equation.tex`.
- A standard electrostatic Maxwell equation in the static metric contains a factor `1/N`.
- An internal component generically contains additional lapse/radion factors.
- A nonzero ordinary electromagnetic field has stress-energy and produces an Einstein–Maxwell geometry, not vacuum Schwarzschild.

The Maxwell-like harmonic equation may still be studied as a specially stated effective three-dimensional model, but it is not a first-principles closure of GAP-U2.
