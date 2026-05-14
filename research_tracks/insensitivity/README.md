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
