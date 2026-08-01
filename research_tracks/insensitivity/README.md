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

# insensitivity/ — Alpha-insensitivity sweep (core, non-speculative)

Cíl: ukázat, že klíčové kombinace pozorovatelných veličin jsou robustní (ploché) vůči drobným změnám α
při UBT škálování (tj. když se upraví související parametry společně).

## Struktura
- `insensitivity/observables.py` — definice proxy observablí (Rydberg, Thomson σ_T, Gamow proxy).
- `insensitivity/sweep.py` — sweep přes ±2 % α, případně přes různé p; ukládá CSV.
- `insensitivity/tests/test_insensitivity.py` — test plochosti (tolerance lze upravit).

## Použití
```bash
python -m insensitivity.sweep
pytest -q insensitivity/tests/test_insensitivity.py
```
