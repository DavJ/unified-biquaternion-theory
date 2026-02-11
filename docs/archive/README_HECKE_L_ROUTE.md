# Variant C: Hecke via L-function (theta → Mellin → L(s))

Tento balíček přidává **automorfní/L-funkční** cestu zapojení Hecke do UBT:

- Postavíme half-integral theta objekt `vartheta(τ)` (z theta-konstant).
- Hecke operátor je `T(p^2)`; pro eigenformy existují eigenhodnoty `λ_p`.
- Mellinovou transformací dostaneme `L(ϑ,s)` s Eulerovým součinem `∏_p L_p(ϑ,s)`.
- Hecke sektor je lokální místo `p`. Fyzikální vazba zůstává:
  \[ \alpha_p^{-1} = p + \Delta_{\mathrm{CT}}(p). \]

## Soubory
- `tex/UBT_hecke_L_route.tex` — vložit do hlavního TeXu (sekce Variant C).
- `automorphic/hecke_l_route.py` — scaffold: θ-koeficienty, akce `T(p^2)`, Dirichletova řada.
- `automorphic/tests/test_hecke_l_route.py` — základní sanity testy.

## Integrace
1) V preambuli TeXu měj: `amsmath, amsthm, hyperref`.
2) Do hlavního TeXu vlož:
   ```tex
   \input{tex/UBT_hecke_L_route}
   ```
3) (Volit.) Pokud chceš „form-factor“ z Hecke dat, napoj ho přes `sector_form_factor(p)` (default 1.0) — jádro Δ_CT zůstává archimedeovské.

## Co má doplnit Copilot
- Nahradit `build_theta_constant_combo` za korektní kombinaci theta-konstant v Kohnen plus space.
- Ověřit eigenformové chování pro vybrané `p` a zkonstruovat rozumný `λ_p` estimator.
- (Pokročilé) Přidat lokální faktory `L_p(ϑ,s)` přímo z poznatků o Hecke-eigenformách.
