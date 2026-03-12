# extensions/

This directory holds **formal extensions** of the core UBT framework — mathematical
structures and physical sectors that are well-formalized, internally consistent, and
extend the mainline theory without contradicting it, but that are not yet (or may never
be) part of the narrowly proved canonical mainline.

## Role

`extensions/` sits between the proved canonical core (`core/`) and the
loosely speculative content (`speculative_extensions/`).  Content here should be:

- Mathematically formalized
- Not contradicting `core/` or root `DERIVATION_INDEX.md`
- Extending UBT to new sectors (e.g. dark sector, holographic duals, p-adic arithmetic)
- Clearly labeled with proof/support status per the conventions in `DERIVATION_INDEX.md`

## What belongs here (examples)

| Subdirectory | Content |
|---|---|
| `dark_sector/` | Dark matter / dark energy extensions via imaginary metric sector |
| `holographic/` | Holographic dual formulations |
| `padic/` | p-adic arithmetic extensions of UBT |
| `noncommutative/` | Non-commutative geometry sector |

## What does NOT belong here

- Content that has been proved on the canonical admissible sector → belongs in `core/`
- Content that is purely speculative ontology or lacks formalization → belongs in `speculative_extensions/`
- Numerical experiments and parameter scans → belongs in `experiments/`

---

**Last Updated**: 2026-03-12
