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

# Progressive Growth — Theta Grid Architecture

**Author**: Ing. David Jaroš  
**Repository layer**: `research_tracks` (active, incomplete)

---

## Overview

This project explores the UBT progressive-growth architecture, which
decomposes weight matrices through intermediate half-grid spaces whose
frames are defined by selected theta segments from the canonical UBT
phi kernel.

This is **not** ordinary neuron duplication (synthetic widening).
Neuron duplication is retained only as a baseline.

---

## Architecture

```
[original layer k] ---(theta segment at k + 1/2)--- [original layer k+1]
```

The half-grid frame `Phi` at position `k + 1/2` determines the
intermediate representation.  Different positions carry different frames;
this is half-grid theta-sector interleaving.

## Current milestone

**M2H — Exact half-grid theta-sector factorization** (implemented)

See `STATUS.md` for results, `GOALS.md` for scope,
`reports/HALF_GRID_FACTORIZATION.md` for mathematics.

## Module structure

```
src/ubt_theta_lab/progressive_growth/
    __init__.py
    half_grid.py            -- core factorization and ReLU insertion
    theta_sector_frame.py   -- frame analysis and diagnostics
    phi_segment_adapter.py  -- canonical phi-kernel segment builder

tests/progressive_growth/
    test_half_grid_factorization.py

projects/progressive_growth/
    GOALS.md
    STATUS.md
    README.md (this file)
    reports/HALF_GRID_FACTORIZATION.md
    scripts/check_half_grid_factorization.py
```

## Running the diagnostic

```bash
python projects/progressive_growth/scripts/check_half_grid_factorization.py
```

## Running the tests

```bash
pytest tests/progressive_growth -q
```

## What is not claimed

- No training-performance improvement is claimed.
- No proven Theta Grid speedup.
- No action-level derivation of sector selection.
