# Priority archive integration and GR architecture audit — 2026-07-26

## Scope

This patch integrates selected historical evidence from `research-master`
without importing the entire archive or mixing historical concepts with current
proof status. It also combines the torsion-free concurrent-vector obstruction
and the torsionful arbitrary-tetrad representer into an architecture-level GR
no-go.

## Priority integration

- Replaced the blanket priority statement with mechanism-specific claims.
- Recorded SHA-256 hashes for both Google Takeout archives, five relevant pages,
  and selected original equation assets.
- Added the evidence-backed public date 18 March 2016 for the biquaternion
  electroscalar formulation.
- Recorded the 8 November 2020 backup as evidence for the historical heuristic
  linkage of scalar `G` to gravity.
- Explicitly prohibited backdating the 2026 projection-free tetrad and GR
  theorems.
- Kept the complete historical archive external; only selected small assets and
  a manifest are included.

## GR result

`GAP-10T-MINIMAL-ONE-CONNECTION-GR` is closed as a no-go [L1]. If the same
metric-compatible connection inside `DTheta` is the physical connection:

- the torsion-free branch obeys the concurrent-vector restriction and excludes
  generic GR;
- the arbitrary-tetrad right inverse requires nonzero contortion and therefore
  makes that same physical connection torsionful.

The preferred exact-GR continuation is now sharply defined: derive a composite
or algebraically auxiliary nonpropagating jet connection distinct from the
physical Levi-Civita connection. The alternative is an explicitly torsionful
modified-gravity branch.

## Constructive split-jet completion

A second exact note closes `GAP-10T-JET-KIN` locally. For non-null
Lorentz-real `X`, decompose `Z=sE-D_LC X` into parallel and orthogonal parts.
The parallel part gives a fixed relative central jet one-form; the orthogonal
part gives a fixed Lorentz jet tensor. Their sum satisfies `Dhat X=sE` exactly
while the physical connection remains Levi-Civita.

This is a kinematic right inverse, not a dynamical `E[Theta]` map.
`GAP-10T-JET-DYN` remains open.

## Remaining GR lemmas

1. action-level selection of the explicit split-jet right inverse and of
   `E[Theta]`, including proof of nonpropagation;
2. canonical Hilbert-Palatini curvature term with sign and Newton coefficient;
3. no-ghost/nonpropagation audit;
4. on-shell Schwarzschild/Kerr/FRW and two-polarization perturbation theorem.

The patch does not claim unconditional GR derivation.

## Publication hygiene

- `papers/UBT_GR_Submission.tex` remains the only GR canonical manuscript.
- `papers/UBT_GR_Flagship.tex` and `papers/UBT_GR_RC2_final.tex` are explicitly
  labelled superseded in the publication registry; their historical complete-GR
  language is not current status.
- The May 2026 arXiv checklist and prepared ZIP references are marked
  superseded. The GR track is not submission-ready for an unconditional
  derivation claim while `GAP-10T-JET-DYN` and `GAP-10D` remain open.
