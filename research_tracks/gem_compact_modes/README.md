<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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


# GEM compact-mode track

**Status:** active non-canonical research track  
**Confidence:** Candidate for kinematics; Open for dynamics  
**Canonical impact:** none

This track studies whether counter-propagating compact-`psi` modes of the UBT
master field can provide a physically admissible source for a metric response,
including a possible rotating or Gödel-type branch.

The track deliberately separates four questions:

1. **Compact-mode kinematics:** what energy, compact momentum, and gradient
   pressure are carried by a `(+n,-n)` pair?
2. **Biquaternionic orientation:** can a momentum-balanced pair retain a
   non-zero averaged bivector/spin observable?
3. **Metric response:** does a candidate interaction produce symmetric tetrad
   strain, rather than only a local Lorentz-frame rotation?
4. **Gödel-type dynamics:** can the canonical UBT action select a rotating
   homogeneous tetrad and its required source?

The exact compact-mode identities and the pure-Lorentz no-go are closed in this
track.  The action-level source, non-zero balanced spin channel, and Gödel-type
solution are open.

## Files

- `gem_compact_modes.tex` — self-contained research note.
- `STATUS.md` — claim ledger and precise closure boundary.
- `FALSIFICATION.md` — failure conditions and decision tree.
- `LEGACY_MAP.md` — relation to preserved historical CTC/imaginary-metric work.
- `../../tools/verify_gem_compact_modes.py` — exact/numerical verifier.
- `../../tests/test_gem_compact_modes.py` — regression tests.

## Central result

For

```tex
Theta = A_+ Q_+ exp(-i omega t + i n psi/R_psi)
      + A_- Q_- exp(-i omega t - i n psi/R_psi),
```

with normalized internal amplitudes and `k=n/R_psi`, circle averaging gives

```tex
j_psi = k (|A_+|^2-|A_-|^2),
P_psi = k^2 (|A_+|^2+|A_-|^2).
```

Thus a balanced pair has zero net compact current but non-zero compact-gradient
energy/pressure.  This can source a scalar/radion-like response, but does not by
itself select a rotation direction.  Rotation requires a surviving covariant
orientation observable, such as an averaged UBT bivector or spin current, and a
canonical action term that couples it to the connection/tetrad.

## Non-claims

This track does **not** claim:

- that information has an intrinsic mass independent of its physical carrier;
- that a standing wave automatically rotates spacetime;
- that odd Clifford grades are fundamental UBT fields;
- that a Gödel universe or closed timelike curves have been derived;
- that an enhanced gravitoelectric coupling beyond standard stress-energy has
  been established.
