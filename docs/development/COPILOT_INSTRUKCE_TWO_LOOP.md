# COPILOT: TODO pro dokončení two-loop Δ_CT(p) napříč Hecke sektory

## Cíl
Dodat rigorózní výpočet `Δ_CT(p)` (dvousmyčka, Thomson limit) a propojit jej do TeXu i CI pro více `p` (např. 131, 137, 139).

## Co je hotovo (v tomhle balíčku)
- `alpha_core_repro/alpha_two_loop.py` — API `compute_two_loop_delta(p, cfg)` + `alpha_corrected(...)`, grid export.
- `alpha_core_repro/tests/test_alpha_two_loop.py` — sanity testy + přesná kontrola pro p=137 (mock).
- `alpha_core_repro/run_grid.py` — rychlý běh gridu a CSV.
- `p_universes/sector_ff.py` — hook na sektorový form factor (zatím 1.0).

## Úkoly
1) **Implementuj fyzikální jádro** v `_two_loop_archimedean_core(...)`:
   - Vypočti vakuovou polarizaci Π(q^2) v UBT→QED matchingu (nízké q^2), dvousmyčkově.
   - Vezmi Thomsonův limit (q^2→0), extrahuj konečnou část ⇒ `Δ_CT(p)`.
   - Dodrž schéma (MSbar nebo jiné) a `μ`. Udrž bez-fitovost vstupů.
   - Validuj pro p=137: `α^{-1} ≈ 137.035999` v toleranci `< 5e-4`.

2) **Zobecni na více p** (stejné jádro, různé sektory):
   - Použij parametr `p` a volitelný `form_factor` (zatím 1.0).
   - Vytvoř CSV přes `run_grid.py` pro p ∈ {127, 131, 137, 139, 149}.

3) **CI a testy**:
   - Dočasně může běžet mock s `UBT_ALPHA_STRICT=0`, `UBT_ALPHA_ALLOW_MOCK=1`.
   - Po doplnění fyziky přepni na `UBT_ALPHA_STRICT=1` (test bez skipu, bez mocku).

4) **TeX integrace**:
   - V hlavním TeXu referencuj per-sektor větu `α_p^{-1} = p + Δ_CT(p)`.
   - Přidej tabulku naplněnou z CSV gridu (p, Δ_CT(p), α_p^{-1}).
   - Udrž definici `Δ_CT` a vazbu na Ward/Thomson část.

## Poznámky
- `sector_form_factor(p)` nech zatím 1.0; případné Hecke/zeta korekce přidáme později.
- Nezaváděj fitované parametry. Pokud potřebuješ numerické konstanty, odvoď je z UBT/QED struktury a uveď v textu.

---

### Rychlé příkazy
```bash
export UBT_ALPHA_STRICT=0
export UBT_ALPHA_ALLOW_MOCK=1
pytest -q alpha_core_repro/tests/test_alpha_two_loop.py
python -m alpha_core_repro.run_grid
# Po implementaci fyziky:
export UBT_ALPHA_STRICT=1
unset UBT_ALPHA_ALLOW_MOCK
pytest -q
```
