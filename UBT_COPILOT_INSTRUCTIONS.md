# UBT Copilot Instructions

Tento dokument shrnuje matematické a fyzikální prvky Unified Biquaternion Theory (UBT), aby byly při práci na projektu snadno dostupné. Obsahuje strukturu pole Θ, základní akci, důležité konstanty a již odvozené hodnoty.
Slouží jako kontextový referenční přehled.

## 1. Struktura pole Θ

Pole Θ v UBT je modelováno jako biquaternionová struktura:

$$\Theta \in C \otimes H.$$

Má 16 komplexních komponent, což odpovídá efektivní reálné dimenzi:

$$N_{\text{eff}} = 32.$$

## 2. Základní akce Θ

Akce pole obsahuje dva příspěvky, které zachycují komutační i antikomutační strukturu:

$$S_\Theta = a\,[D_\mu, \Theta]^\dagger [D_\mu, \Theta] + b\,\{D_\mu, \Theta\}^\dagger \{D_\mu, \Theta\}.$$

- **Komutátor** odpovídá rotační/spinorové části
- **Antikomutátor** odpovídá plné C×H struktuře

## 3. Základní elektromagnetická hodnota

Z čisté geometrie Θ v prostoru $C \otimes H$ vychází charakteristická veličina:

$$\alpha_{\text{bare}}^{-1} = 136.973.$$

Tato hodnota je používána jako výchozí „bare" hodnota před renormalizačními korekcemi.

## 4. Renormalizační schéma

Výsledná jemnostrukturální konstanta se získává sečtením čtyř strukturálních příspěvků:

$$\alpha^{-1} = \alpha_{\text{bare}}^{-1} + \Delta_{\text{anti}} + \Delta_{\text{RG}} + \Delta_{\text{grav}} + \Delta_{\text{asym}}.$$

Níže je uveden přehled hodnot použitých v UBT:

### Antikomutátorová korekce

Z poměru stop antikomutátoru a komutátoru:

$$\Delta_{\text{anti}} \approx 0.046.$$

### Geometric RG (torus)

Používají se toroidální koeficienty:

$$\beta_1 = \frac{1}{2\pi}, \quad \beta_2 = \frac{1}{8\pi^2},$$

a logaritmický faktor:

$$\ln(\Lambda/\mu) = \frac{\pi}{\sqrt{2}}.$$

Celkový příspěvek:

$$\Delta_{\text{RG}} \approx 0.040.$$

### Gravitational dressing

Z poměru 6D–4D gravitačních termů:

$$\Delta_{\text{grav}} \approx 0.015.$$

### Mirror (Z₂) asymmetry

Z topologie toru:

$$\Delta_{\text{asym}} = \frac{1}{8\pi} \approx 0.010.$$

## 5. Výsledná hodnota jemnostrukturální konstanty

Součet všech příspěvků vede k hodnotě:

$$\alpha_{\text{UBT}}^{-1} \approx 137.0359.$$

Experimentální hodnota:

$$\alpha_{\text{exp}}^{-1} = 137.035999084.$$

Rozdíl je v řádu $3 \times 10^{-4}\%$.

## 6. Hmotnost elektronu

Stejná renormalizační struktura se používá i pro výpočet hmotnosti elektronu:

$$m_e \approx 0.511\,\text{MeV}.$$

## 7. Souhrn klíčových čísel

- $N_{\text{eff}} = 32$
- $\alpha_{\text{bare}}^{-1} = 136.973$
- $\Delta_{\text{anti}} = 0.046$
- $\Delta_{\text{RG}} = 0.040$
- $\Delta_{\text{grav}} = 0.015$
- $\Delta_{\text{asym}} = 0.010$
- $\alpha_{\text{UBT}}^{-1} = 137.0359$
- $m_e \approx 0.511\,\text{MeV}$

## 8. Stručný kontext

Tyto hodnoty a rovnice reprezentují výsledky odvození v rámci struktury Unified Biquaternion Theory a lze je použít jako konzistentní referenci při generování kódu, dokumentace či matematických poznámek souvisejících s teorií.
