# 🧠 COPILOT_WORKFLOW_UBT_RH_LINK.md

## 🎯 Cíl
Udržet Unified Biquaternion Theory (UBT) jako **samostatný matematicko-fyzikální rámec**,  
který sjednocuje komplexní čas, kvaternionickou geometrii, spinorová pole a vědomí.  

Souvislost s Riemannovou hypotézou (RH) bude **formálně uznána jako přirozený geometricko-spektrální efekt**,  
nikoli jako přímý důkaz.

---

## 1️⃣ Oddělení cílů (cleanup)

### 1.1 UBT zůstává:
- jednotná teorie pole na prostoru \(\mathbb{C} \otimes \mathbb{H}\),
- definuje bi-kvaternionové operátory, metriky a vědomí,
- obsahuje dokumenty:
  ```
  docs/spectral_framework.tex
  consolidation_project/appendix_RH_riemann_zeta_connection.tex (upraveno)
  consolidation_project/appendix_ALPHA_*.tex
  consolidation_project/appendix_O_padic_overview.tex
  ```
- její cílem je matematická a fyzikální konzistence.

### 1.2 Vše, co explicitně tvrdí „důkaz RH":
- přesunout do samostatné složky:  
  ```
  research/rh_biquaternion_extension/
  ```
- zachovat jen **souvislosti a inspiraci**, nikoli tvrzení o důkazu.

---

## 2️⃣ Co Copilot smí a nesmí dělat

| Smí dělat | Nesmí dělat |
|------------|--------------|
| Definovat biquaternionové operátory, metriky, hermiticity a spektra. | Tvrdit, že UBT dokazuje Riemannovu hypotézu. |
| Používat \(M_{BQ}\) jako model samosprávného operátoru v 8D prostoru. | Umisťovat testy nebo důkazní věty o RH přímo do UBT repozitáře. |
| Popsat, že projekce spektra \(M_{BQ}\) do komplexní roviny připomíná zeta spektrum. | Spojovat konkrétní eigenhodnoty s nulami ζ(s). |
| Připravovat matematicky korektní spektrální rámec (LaTeX, Lean). | Nahrazovat analytickou teorii čísel bi-kvaternionovou metafyzikou. |

---

## 3️⃣ Struktura po úpravě

```
unified-biquaternion-theory/
│
├── docs/
│   └── spectral_framework.tex   ← remark o souvislosti s RH
│
├── consolidation_project/
│   ├── appendix_RH_riemann_zeta_connection.tex  ← upraveno: bez přímých tvrzení o důkazu
│   ├── appendix_ALPHA_*.tex
│   └── appendix_O_padic_overview.tex
│
├── lean/src/BiQuaternion/
│   ├── Algebra.lean
│   ├── Operators.lean
│   └── Spectrum.lean
│
├── research/
│   └── rh_biquaternion_extension/
│       ├── README.md
│       ├── RH_Spectral_Link.md  ← původní RIEMANN_HYPOTHESIS_CONNECTION.md
│       └── (případné další numerické skripty)
│
└── COPILOT_WORKFLOW_UBT_RH_LINK.md
```

---

## 4️⃣ Úkoly pro Copilota

1. **Projít všechny `.tex` soubory:**
   - odstranit nebo komentovat přímé věty o „důkazu RH",
   - ponechat nebo upravit věty ve stylu:
     > "The Riemann zeta spectrum can be viewed as a projection of the biquaternionic spectral structure."

2. **Zkontrolovat `appendix_RH_riemann_zeta_connection.tex`:**
   - odstranit fráze jako "statistical proof of the RH",
   - vložit remark:
     ```latex
     \begin{remark}[Relation to Riemann Hypothesis]
     The Riemann zeta spectrum corresponds to the complex projection of the
     real spectrum of the self-adjoint operator $M_{BQ}$ in $\mathbb{C}\otimes\mathbb{H}$.
     This connection is structural and does not constitute a proof.
     \end{remark}
     ```

3. **Upravit `docs/spectral_framework.tex`:**
   - přidat podobný remark o strukturální souvislosti

4. **Přesunout dokumentaci:**
   - `RIEMANN_HYPOTHESIS_CONNECTION.md` → `research/rh_biquaternion_extension/RH_Spectral_Link.md`

5. **Zachovat formální rámec UBT:**
   - v `lean/src/BiQuaternion/` pouze matematicky definované struktury,
   - doplnit komentáře typu:
     ```lean
     -- The following operator structure allows spectral comparison to
     -- classical zeta-related operators, but UBT itself does not assert RH.
     ```

6. **Připravit shrnutí:**
   - v `README.md` přidat sekci „Relation to Number Theory",
     kde se RH uvede jako přirozená projekce spektra.

---

## 5️⃣ Dlouhodobý plán
- V `research/rh_biquaternion_extension/` lze budovat numerické a teoretické paralely,  
  které testují propojení RH ↔ \(M_{BQ}\),  
  bez zásahu do základního teoretického jádra UBT.
- Po dokončení bude možné vydat dva články:
  - 📘 *Unified Biquaternion Theory* (hlavní fyzikálně-matematická práce),  
  - 📗 *Spectral Link between UBT and Riemann Hypothesis* (samostatná matematická studie).

---

## 6️⃣ Status implementace

✅ Dokument vytvořen  
✅ Implementace dokončena  
✅ Workflow aplikován

### Co bylo provedeno:

1. ✅ **Vytvořena nová struktura**:
   - `research/rh_biquaternion_extension/` directory
   - README.md s upozorněním na spekulativní povahu
   - RH_Spectral_Link.md (přesunutý RIEMANN_HYPOTHESIS_CONNECTION.md)

2. ✅ **Upraveny LaTeX soubory**:
   - `consolidation_project/appendix_RH_riemann_zeta_connection.tex`:
     - Přidán remark o rozsahu a omezeních
     - "statistical proof" změněno na "structural analogy"
     - "Theorem" změněno na "Conjecture" pro spekulativní tvrzení
     - "Proof Strategy" změněno na "Speculative Research Directions"
   - `docs/spectral_framework.tex`:
     - Přidán remark o strukturální souvislosti (ne důkaz)

3. ✅ **Upraveny Lean soubory**:
   - `lean/src/BiQuaternion/Spectrum.lean`
   - `lean/src/BiQuaternion/Operators.lean`
   - Přidány komentáře objasňující, že UBT netvrdí důkaz RH

4. ✅ **Aktualizován README.md**:
   - Přidána sekce "Relation to Number Theory"
   - Odděleny ověřené (zeta regularizace) od spekulativních (RH spektrum) souvislostí
   - Reference na research/ directory

### Výsledek:

- UBT zůstává samostatný matematicko-fyzikální rámec
- RH souvislost uznána jako přirozený geometricko-spektrální efekt
- Žádná přímá tvrzení o důkazu RH v hlavním repozitáři
- Spekulativní materiál oddělený v research/rh_biquaternion_extension/
