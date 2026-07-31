# GR fiber status regression fix — 31 July 2026

Apply this overlay at the repository root.

It updates one stale regression test that required the exact historical header
`EXPLORATORY (2026-07-15)`. The test now verifies the intended invariant:

- the full profile file is explicitly a **noncanonical completion candidate**;
- the linearised profile file remains explicitly **exploratory**;
- neither file silently overrides the pointwise Axiom C metric.

No theory, derivation, paper, or generated PDF is changed.
