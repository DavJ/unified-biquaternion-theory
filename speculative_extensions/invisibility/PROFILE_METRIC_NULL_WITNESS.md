# Profile metric-null but biquaternionically active witness

**Status:** EXACT ALGEBRAIC RESULT INSIDE A SPECULATIVE TRACK  
**Recorded:** 2026-08-01

## 1. Scope

This note distinguishes a finite-dimensional obstruction from a specifically
UBT profile-space construction.  It proves neither an on-shell solution nor
physical invisibility.

Let

\[
B(a,b)\mathbf1:=\frac12(a^\sharp b+b^\sharp a)
\]

be the central complex symmetric bilinear on
`V = C tensor H`, with `dim_C V=4`.

## 2. Pointwise rank obstruction

For any totally isotropic subspace `U`, one has `U subset U^perp`.  Since `B`
is nondegenerate,

\[
\dim U+\dim U^\perp=4.
\]

Hence

\[
2\dim U\le4,
\qquad
\boxed{\dim U\le2.}
\]

Therefore four pointwise elements satisfying

\[
B(E_\mu,E_\nu)=0
\quad\hbox{for all }\mu,\nu
\]

cannot form an invertible four-dimensional tetrad.  The pointwise
metric-null branch is necessarily degenerate.

## 3. Rank-four profile witness

Take

\[
q=\mathbf e_2+i\mathbf e_3,
\qquad
r=\mathbf1-i\mathbf e_1.
\]

They satisfy

\[
B(q,q)=B(r,r)=B(q,r)=0,
\qquad
q^\sharp r=-2\mathbf e_2-2i\mathbf e_3\ne0.
\]

On a `2 pi`-periodic profile circle define

\[
\begin{aligned}
E_0(\psi)&=e^{ i\psi}q,&
E_1(\psi)&=e^{-i\psi}r,\\
E_2(\psi)&=e^{2i\psi}q,&
E_3(\psi)&=e^{-2i\psi}r.
\end{aligned}
\]

The four functions are linearly independent because they occupy distinct
Fourier-mode/internal-direction pairs.  Define the bilinear profile average
without complex conjugation,

\[
\langle f\rangle_\psi
=\frac1{2\pi}\int_0^{2\pi}f(\psi)\,d\psi.
\]

Since `span{q,r}` is totally isotropic,

\[
\gamma^{\rm prof}_{\mu\nu}\mathbf1
:=\left\langle
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
\right\rangle_\psi
=0
\]

for all `mu,nu`.  Nevertheless Fourier pairing of opposite modes gives

\[
\Sigma^{\rm prof}_{01}=q^\sharp r\ne0,
\qquad
\Sigma^{\rm prof}_{23}=q^\sharp r\ne0,
\]

while the remaining cross-mode averages vanish.

Thus

\[
\boxed{
\operatorname{rank}_{\rm functions}\{E_0,E_1,E_2,E_3\}=4,
\quad
\gamma^{\rm prof}=0,
\quad
\Sigma^{\rm prof}\ne0.
}
\]

## 4. Interpretation barrier

The witness proves that the full UBT profile space can retain four independent
jet directions even when its averaged central metric vanishes.  It does not
produce:

- an inverse central metric or standard Levi--Civita connection;
- a nonzero ordinary four-volume;
- a regular action at degeneracy;
- an integrable `Theta(x,psi)` field solving UBT equations;
- finite energy, stability, boundary matching, or zero exterior scattering.

The next theorem sought is a covariant integrability result for profile jets,
followed by a polynomial first-order action that remains regular on this
branch.
