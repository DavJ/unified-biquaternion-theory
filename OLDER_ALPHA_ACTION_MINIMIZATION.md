# Starší hodnota α z predikce minimalizací akce

## Přehled

Tento dokument shrnuje **starší přístup** k odvození jemné strukturní konstanty α z UBT pomocí **minimalizace akce** s efektivním potenciálem.

---

## Hlavní vzorec

Efektivní akce (potenciál) pro konfiguraci s topologickým číslem vinutí `n`:

```
V_eff(n) = A·n² - B·n·ln(n)
```

kde:
- **A·n²** = kinetická energie z gradientů pole
- **-B·n·ln(n)** = kvantové korekce (vakuová polarizace, energie nulového bodu)

---

## Parametry

Z UBT výpočtů:
- **A = 1** (normalizace)
- **B = 46.3** (odvozeno z počítání módů)

Tento parametr B byl později upřesněn v různých verzích:
- B ≈ 20.3 (starší verze, `emergent_alpha_calculations.tex`)
- **B = 46.3** (aktuální hodnota, `alpha_padic_executive_summary.tex`)
- B = 46.27 (velmi přesná hodnota, `scripts/verify_B_integral.py`)

---

## Minimalizace

Minimalizace V_eff(n) přes prvočísla dává:

```
n_opt = 137
```

Toto je **první fáze** dvoustupňového mechanismu:

1. **Entropický filtr**: Pouze prvočísla jsou topologicky stabilní
2. **Energetická selekce**: n = 137 je lokální minimum akce

---

## Výsledek

```
α₀ = 1/137
```

**Teoretická hodnota**: α⁻¹ = 137.000 (přesně)  
**Experimentální hodnota**: α⁻¹ ≈ 137.036  
**Rozdíl**: ~0.026% (vysvětlen QFT korekcemi - běh vazební konstanty)

---

## Vztah k novým přístupům

Tento **starší přístup** (akce minimalizace) je **komplementární** k novým přístupům v tomto PR:

| Přístup | Metoda | Výsledek α⁻¹ | Chyba |
|---------|--------|--------------|-------|
| **Akce minimalizace** | V_eff(n) = An² - Bn·ln(n) | 137.000 | 0.026% |
| M⁴×T² torus/theta | Dedekind η(i) determinant | 137.032 | 0.003% |
| CxH plný biquaternion | Strukturální N_eff=32 | 136.973 | 0.046% |

---

## Klíčové rozdíly

### Starší přístup (akce minimalizace):
- **Diskrétní topologické číslo**: n ∈ ℤ (prvočísla)
- **Parametr B**: Odvozeno z počítání módů (B = 46.3)
- **Výsledek**: α⁻¹ = 137 (přesně)
- **Vysvětlení odchylky**: QFT běh konstanty

### Nové přístupy (torus/CxH):
- **Kontinuální parametry**: A₀, N_eff (strukturální)
- **Dedekind η-funkce**: B₁ = -1.0547 z η(i)
- **Výsledek**: α⁻¹ ≈ 137.0 (s variací 136.97-137.03)
- **Vysvětlení**: Geometrická determinanta

---

## Dokumenty

Starší přístup je dokumentován v:

1. **`unified_biquaternion_theory/solution_P4_fine_structure_constant/alpha_constant_derivation.tex`**
   - Rigorózní odvození
   - Dvoustupňový mechanismus
   - V_eff(n) = A·n² - B·n·ln(n)

2. **`alpha_padic_executive_summary.tex`**
   - Exekutivní souhrn
   - P-adická rozšíření
   - B = 46.3 z počítání módů

3. **`emergent_alpha_executive_summary.tex`** (DEPRECATED)
   - Původní explorativní práce
   - B/A ≈ 20.3 (starší hodnota)
   - Označeno jako zastaralé (listopad 2025)

4. **`emergent_alpha_calculations.tex`**
   - Numerické výpočty
   - Explicitní minimalizace
   - Python skripty

5. **`scripts/emergent_alpha_calculator.py`**
   - Numerická implementace
   - V_eff(n, A=1.0, B=46.3)
   - Citlivostní analýza B/A

---

## Přesné hodnoty z dokumentů

### Z `alpha_padic_executive_summary.tex`:

```latex
V_eff(n) = A n^2 - B n \ln(n)

From UBT calculations: A = 1, B = 46.3
```

Minimalizace:
```latex
\boxed{n_{\text{opt}} = 137}
```

Výsledek:
```latex
\alpha^{-1} = 137
```

### Z `alpha_constant_derivation.tex`:

```latex
S(n) \approx A \cdot n^2 - B \cdot n \ln(n)
```

Selekce:
1. **Entropický filtr** → prvočísla
2. **Princip nejmenší akce** → n = 137

```latex
\alpha_0 = \frac{1}{137}
```

---

## Status

**Současný status** těchto starších prací:

- ✓ Platné jako **komplementární přístup**
- ✓ Použitelné pro **p-adická rozšíření**
- ⚠ Některé dokumenty označeny jako **DEPRECATED**
- ⚠ Parametr B vyžaduje **odvození z prvních principů**

**Doporučení**: Použít **nové přístupy** (M⁴×T², CxH) pro přesnější predikce, ale **zachovat starší přístup** pro p-adickou teorii a multiverse strukturu.

---

## Reference

**Hlavní dokumenty**:
- `solution_P4_fine_structure_constant/alpha_constant_derivation.tex` - rigorózní odvození
- `alpha_padic_executive_summary.tex` - aktuální exekutivní souhrn
- `consolidation_project/appendix_ALPHA_one_loop_biquat.tex` - moderní odvození B

**Numerické skripty**:
- `scripts/emergent_alpha_calculator.py`
- `scripts/verify_B_integral.py`
- `scripts/test_symbolic_alpha.py`

---

## Datum

Dokumentováno: 2025-11-13  
Starší práce: 2024-2025  
Status: **Archivováno s referencí na nové přístupy**
