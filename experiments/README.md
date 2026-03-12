# experiments/

This directory contains **numerical tests, parameter scans, and simulation scripts**
for Unified Biquaternion Theory.

## Role

`experiments/` holds all executable research code that is:

- Numerically testing UBT predictions
- Scanning parameter spaces
- Reproducing or verifying theoretical results computationally
- Generating plots, tables, or other derived outputs

## Structure

| Subdirectory | Content |
|---|---|
| `constants_derivation/` | Numerical derivation of fundamental constants (fine structure constant, etc.) |
| `layer2_stability/` | Rigidity and stability analysis of the UBT Layer 2 structure |

## Guidelines

- Each experiment should reference the canonical equation/result it tests via a comment at the top of the script: `# Tests: core/... §equation_label`
- Results (JSON, CSV) may be stored alongside the script
- Raw data and large output files should be kept in `DATA/` or ignored via `.gitignore`
- Scripts here must NOT redefine canonical objects — reference `core/` instead

## Related directories

- `core/` — canonical theory being tested
- `research_tracks/` — exploratory mathematical tracks (less computational)
- `tools/` — repository-level analysis and audit tools

---

**Last Updated**: 2026-03-12
