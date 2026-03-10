<!-- © 2025 Ing. David Jaroš — CC BY-NC-ND 4.0 -->

# Mirror Sector Physics — Topic Index

**Status**: **NUMERICAL OBSERVATION** (twin prime structure); **MOTIVATED CONJECTURE** (vacuum stability)  
**Last updated**: 2026-03-10  
**Canonical source**: `consolidation_project/mirror_sector/README.md`

---

## Quick Answer

The mirror sector arises from the twin prime observation in the Hecke analysis:
- Our sector: prime **p = 137**, Set A Hecke forms, α⁻¹ = 137
- Mirror sector: prime **p = 139**, Set B Hecke forms, α'⁻¹ = 139

The two primes are twin primes (differ by 2). The mirror sector is predicted to be
a habitable parallel sector with a fine structure constant α' = 1/139 ≈ 0.0072.
Mirror matter is a viable dark matter candidate that couples to our sector only
via gravity.

| Claim | Status |
|-------|--------|
| n* = 137, n** = 139 twin prime structure | **NUMERICAL OBSERVATION** |
| V_eff(137) < V_eff(139) for same B | **NUMERICAL OBSERVATION** |
| n* = 139 is not a local minimum of V_{B_137} | **PROVED NUMERICALLY** |
| n** = 139 is global minimum of mirror branch B₁₃₉ | **MOTIVATED CONJECTURE** |
| Mirror sector is fully stable (no false vacuum) | **FOLLOWS FROM CONJECTURE** |
| Mirror sector α'⁻¹ = 139 in anthropic habitable range | **DERIVED** (given the conjecture) |
| Mirror matter as dark matter candidate | **CONJECTURE** |

---

## Canonical Sources (Start Here)

| Document | Role | Status |
|----------|------|--------|
| `consolidation_project/mirror_sector/README.md` | **CANONICAL** — overview, key findings, dark matter connection | Navigation |
| `consolidation_project/mirror_sector/vacuum_stability.tex` | **CANONICAL** — vacuum stability analysis, V_eff comparison | NUMERICAL/CONJECTURE |
| `reports/hecke_lepton/mirror_world_139.md` | **CANONICAL** — Set B Hecke forms, global scan at p=139 | NUMERICAL OBSERVATION |

---

## Supporting Files

| Document | Label | Content |
|----------|-------|---------|
| `DERIVATION_INDEX.md` (Mirror Sector section) | **supporting** | Status table for all mirror sector claims |
| `DERIVATION_INDEX.md` (Hecke Bridge section) | **supporting** | Hecke bridge: weights, levels, characters for both sectors |
| `reports/hecke_lepton/sage_results_2026_03_07.md` | **supporting** | SageMath results confirming Set B |
| `reports/hecke_lepton/prime_specificity_results.txt` | **supporting** | Global prime scan confirming exclusivity of 137/139 |

---

## Connection to Alpha and Hecke

The mirror sector is intimately linked to both:
- **Alpha derivation**: The absence of a Chern-Simons term in S[Θ] is proved using
  the parity symmetry between n* = 137 and n** = 139 — see `b_base_kac_moody_level.tex §H2`
- **Hecke topic**: Sets A and B are the two canonical inputs — see `THEORY/topic_indexes/hecke_index.md`

---

## Sandbox / Speculative Files

| Document | Label | Why Not Canonical |
|----------|-------|-------------------|
| `speculative_extensions/UBT_HeckeWorlds_theta_zeta_primes_appendix.tex` | **speculative** | Extends mirror sector to multiverse / Hecke worlds; highly speculative |
| `UBT_HeckeWorlds_theta_zeta_primes_appendix.tex` | **speculative** | Same content at root level; should be consulted with caution |
| `consolidation_project/gap_A_resolution/A4_hecke_connection.tex` | **sandbox** | Speculative connection to gap A in alpha derivation |

---

## Open Problems

| Problem | Description | Files |
|---------|-------------|-------|
| Derive B_{139} from ℂ⊗ℍ first principles | Currently motivated by analogy with B_{137} | `vacuum_stability.tex` |
| Quantitative dark matter prediction | Mirror matter abundance, self-interaction cross-section | `mirror_sector/README.md §4` |
| Connection to Hubble tension | Mirror sector photons could affect CMB N_eff | `mirror_sector/README.md §5` |
| Why twin primes? | No algebraic explanation for why 137 and 139 specifically | Open |

---

## DERIVATION_INDEX Cross-Reference

Main entries in `DERIVATION_INDEX.md`, Mirror Sector section:
- V_eff(137) < V_eff(139) — NUMERICAL OBSERVATION
- n*=139 not local min of V_{B_137} — PROVED NUMERICALLY
- n**=139 global min of B₁₃₉ — MOTIVATED CONJECTURE
- Sets A and B algebraically independent — NUMERICAL OBSERVATION
- Mirror sector α'⁻¹ = 139 — NUMERICAL OBSERVATION
- Mirror matter as dark matter — CONJECTURE

---

## What a New Reader Should Do

1. Read `consolidation_project/mirror_sector/README.md` (canonical overview, ~3 pages)
2. Read `reports/hecke_lepton/mirror_world_139.md` for the Hecke numerical evidence
3. For vacuum stability analysis, read `consolidation_project/mirror_sector/vacuum_stability.tex`
4. For the connection to α derivation, see `b_base_kac_moody_level.tex §H2` (CS-term absence proof)
5. Treat `UBT_HeckeWorlds_theta_zeta_primes_appendix.tex` as speculative background reading only
