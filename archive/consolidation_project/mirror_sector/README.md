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
| $n^*=139$ is NOT a local min of $V_{B_{137}}$ | PROVED NUMERICALLY | `vacuum_stability.tex` |
| $n^*=139$ is global min of mirror branch $B_{139}$ | MOTIVATED CONJECTURE | `vacuum_stability.tex` |
| $\Delta B/B = 1.21\%$ between sectors | NUMERICAL OBSERVATION | `vacuum_stability.tex` |
| Mirror sector $\alpha'^{-1} = 139$ | NUMERICAL OBSERVATION | `../../reports/hecke_lepton/mirror_world_139.md` |
| Mirror sector is fully stable (not metastable) | FOLLOWS FROM CONJECTURE | `vacuum_stability.tex` |
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
3. **ΔB physical origin**: The 1.21% difference between $B_{137}$ and $B_{139}$
   needs a physical explanation within UBT. Does it arise from different
   $N_{\rm eff}$, a different $R$ correction, or a deeper algebraic mechanism?
   This is the key open question for the mirror sector.
4. **Observational signature**: Mirror matter self-interaction cross-section needs
   to be computed from UBT parameters to make quantitative predictions for
   galaxy cluster observations (Bullet Cluster constraint).

## Files in This Directory

- `vacuum_stability.tex` — Two independent vacua analysis: n*=137 and n*=139 as parallel solutions
- `README.md` — This overview file

## References

- R. Foot & R. R. Volkas, "Neutrino physics and the mirror world," Phys. Rev. D 52, 6595 (1995)
- Zhang & Frieman, "Hubble tension and mirror dark sector," (2022)

---
**Status**: [MOTIVATED CONJECTURE — two independent algebraic sectors]  
**Last Updated**: 2026-03-07  
**Author**: David Jaroš
