# Mirror Sector Physics in UBT

<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

## Overview

The **mirror sector** in UBT arises from the twin prime observation in the Hecke
analysis: the prime $p = 137$ identifies our sector (Set A Hecke forms), while
$p = 139$ identifies a structurally analogous mirror sector (Set B Hecke forms).

The two primes are **twin primes** (differ by 2), suggesting that the mirror sector
is a near-copy of our sector with $\alpha'^{-1} = 139$ instead of $\alpha^{-1} = 137$.

## Key Findings

| Result | Status | File |
|--------|--------|------|
| $V_{\rm eff}(137) < V_{\rm eff}(139)$ | NUMERICAL OBSERVATION | `vacuum_stability.tex` |
| $n^* = 139$ is metastable vacuum | MOTIVATED CONJECTURE | `vacuum_stability.tex` |
| Mirror sector $\alpha'^{-1} = 139$ | NUMERICAL OBSERVATION | `../../reports/hecke_lepton/mirror_world_139.md` |
| Mirror sector is habitable | DERIVED | See below |
| Mirror matter as dark matter candidate | CONJECTURE | This file |

## Mirror Sector Fine Structure Constant

The mirror sector has $\alpha'^{-1} = 139$.  This is within the **anthropic range**
for a habitable universe (approximately $\alpha^{-1} \in [95, 195]$):

- **Stars can burn**: Nuclear fusion works for $\alpha^{-1} \gtrsim 100$ ✓
- **Carbon chemistry works**: Organic molecules form for $\alpha^{-1} \lesssim 200$ ✓
- **Water is a solvent**: Hydrogen bonding works across a wide $\alpha$ range ✓

Therefore the mirror sector with $\alpha'^{-1} = 139$ is **anthropically habitable**.

## Mirror Matter as Dark Matter

Mirror matter (matter interacting via the mirror sector gauge group with $\alpha' = 1/139$)
is a viable dark matter candidate:

- **Gravitational interaction**: Mirror matter couples to our sector only via gravity ✓
- **Self-interaction**: Mirror matter self-interacts with cross-section
  $\sigma/m \sim (\alpha')^2/m_{\rm mirror}$, which is small for $m_{\rm mirror} \gg m_e$ ✓
- **Precedent**: Foot-Volkas mirror matter model (1995) provides a physics basis ✓
- **UBT motivation**: Twin prime algebraic structure provides additional motivation ✓

## Connection to Hecke Analysis

The Hecke forms at $p = 139$ (Set B) are:

| Form | Level $N$ | Weight $k$ | $a_{139}$ | Status |
|------|-----------|------------|-----------|--------|
| `195.2.a.c` | 195 | 2 | +15 | PROBABLE (LMFDB) |
| `50.4.a.b` | 50 | 4 | +3100 | PROBABLE (LMFDB) |
| `54.6.a.b` | 54 | 6 | +53009 | PROBABLE (LMFDB) |

See `../../reports/hecke_lepton/mirror_world_139.md` for details.

## Connection to Hubble Tension

A mirror dark sector with $\alpha' = 1/139$ predicts specific modifications to the
CMB acoustic peaks.  Zhang & Frieman (2022) showed that a similar mirror dark matter
model can resolve the Hubble tension ($H_0$ discrepancy).  This is a potential
**testable prediction** of the UBT mirror sector conjecture.

## Open Questions

1. **B coefficient derivation**: The $B$ coefficient in $V_{\rm eff}(n)$ is an open
   hard problem; its derivation is needed for quantitative vacuum stability predictions.
2. **Mirror lepton masses**: The mass ratios in the mirror sector should follow from
   Set B Hecke eigenvalues at $p = 139$; explicit computation pending.
3. **Discrete tunnelling**: The Coleman tunnelling estimate for integer-valued $n$ is
   non-trivial; a proper treatment requires discrete quantum mechanics methods.
4. **Observational signature**: Mirror matter self-interaction cross-section needs
   to be computed from UBT parameters to make quantitative predictions for
   galaxy cluster observations (Bullet Cluster constraint).

## Files in This Directory

- `vacuum_stability.tex` — Vacuum stability analysis and Coleman tunnelling estimate
- `README.md` — This overview file

## References

- S. Coleman, "Fate of the false vacuum," Phys. Rev. D 15, 2929 (1977)
- R. Foot & R. R. Volkas, "Neutrino physics and the mirror world," Phys. Rev. D 52, 6595 (1995)
- Zhang & Frieman, "Hubble tension and mirror dark sector," (2022)

---
**Status**: [NEW CONJECTURE — motivated by twin prime observation]  
**Last Updated**: 2026-03-07  
**Author**: David Jaroš
