# Dual-sector Clifford-5 / generalized-Dirac track

**Status:** research track; no canonical UBT claims are changed by this overlay.

This directory records a conservative version of the architecture discussed on
2026-07-26:

1. retain the UBT master field over complex time \(\tau=t+i\psi\);
2. use a generalized Dirac / geometric-algebra description;
3. distinguish a single biquaternionic spinor from the complete odd-Clifford
   two-branch carrier;
4. test metric rank with an explicit spinor-current tetrad rather than by
   component counting alone;
5. keep the three-qubit/SU(3) and error-detection interpretation separate from
   the gravitational proof.

The executable verifier is:

```bash
python tools/verify_dual_sector_cl5_rank.py
```

The principal result of this research note is stronger and more precise than
`16 - 6 = 10`:

- the tetrad-to-metric map has rank ten at every nondegenerate tetrad;
- an explicit **single-sector** biquaternionic/Dirac-spinor first-jet current
  already has a nonzero exact 10 x 10 Jacobian minor;
- an explicit **dual-sector cross-current** also has a nonzero exact 10 x 10
  minor.

Therefore a dual sector is not required merely to evade the value-only
8-real-component bound. Its possible motivation is instead the complete
\(\mathrm{Cl}_5(\mathbb C)\) two-branch structure, complex-time dynamics,
SU(3)/three-qubit organization, and possible physical duality.

What remains open is the rank after imposing the actual UBT equations,
complex-time holomorphy/reality conditions, gauge constraints, and the
self-consistent composite spin connection.
