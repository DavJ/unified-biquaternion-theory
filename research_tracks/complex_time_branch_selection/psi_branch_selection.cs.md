<!-- © 2026 Ing. David Jaroš — CC BY-NC-ND 4.0 -->
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

# Výběr first-order dynamické větve pomocí komplexního času ψ

**Typ stopy:** RESEARCH TRACK — MATHEMATICAL SELECTION LEMMA PLUS CONJECTURAL UBT INTERPRETATION  
**Datum:** 2026-09-02  
**Status:** Matematické selekní lemma je PROPOSITION / PROOF SKETCH; UBT interpretace je CONJECTURAL; multivesmírné čtení je SPECULATIVE; RH spojitost je CONDITIONAL RESEARCH DIRECTION.

**Anglická edice:** `psi_branch_selection.en.md`  
**Bilingvní politika:** `../../BILINGUAL_CONTENT_POLICY.cs.md`  
**Verifikační skript:** `../../tools/verify_psi_branch_selection.py`

---

> **Rozsah tohoto dokumentu.** Tato výzkumná stopa zaznamenává rigorózní
> hypotézu o tom, jak by analytické pokračování do komplexní časové souřadnice
> \(\psi\) mohlo vybírat first-order dynamickou větev z kanonické second-order
> UBT rovnice. Nic v této stopě nemodifikuje kanonické axiomy, kanonickou
> master equation, `CLAIMS.yaml` ani žádný status mezery.
> Žádná mezera není povýšena na `PROVED` ani `CLOSED`.

---

<a id="psi-bs-sec1"></a>
## 1. Motivace a přesná taxonomie větví

V literatuře se vyskytují následující odlišné pojmy „větve“, které nesmí být
zaměněny.

<a id="psi-bs-taxonomy"></a>

| ID | Pojem | Doména definice |
|---|---|---|
| B1 | Frekvenční větve faktorizované second-order ODE/PDE | Funkcionální analýza; znaménko vlastní hodnoty |
| B2 | Fourierovy / winding módy na \(S^1_\psi\) | Spektrální teorie na kružnici |
| B3 | Holomorfní vs. antiholomorfní sektor | Komplexní analýza; Hardyho prostory |
| B4 | Diracovy sektory částice vs. antičástice | Teorie reprezentací; CPT |
| B5 | Dekoherované nebo Everettovy makroskopické větve | Dekoherenční teorie; interpretační |

**Těchto pět pojmů není automaticky totožných.**
Identifikace libovolných dvou z nich vyžaduje explicitní dynamický operátor a
důkaz, že daný operátor mapuje jeden pojem na druhý. Tato stopa zkoumá pouze
B1–B3 v matematicky kontrolovaném prostředí; spojitosti s B4 a B5 jsou
explicitně konjecturální nebo spekulativní (viz Sekce 5 a 7).


<a id="psi-bs-dirac5"></a>
### 5.1 Kandidátní pětidimenzionální operátor

Jako pracovní hypotézu zavádíme formální operátor

$$
\mathscr D_5 \Theta
=
\left(
i\hbar \Gamma^\mu D_\mu
+ i\hbar \Gamma_* D_\psi
- \mathcal M[\Theta]
\right)\Theta = 0,
$$

kde:

- \(\Gamma^\mu\) jsou kanonické čtyřdimenzionální UBT Cliffordovy kanály;
- \(\Gamma_*\) je Cliffordův kanál komplexního času **tehdy a jen tehdy**, pokud
  takovýto kanál vystupuje v aktuální kanonické definici (viz
  `canonical/CANONICAL_DEFINITIONS.md`); jinak jde o ansatz vyžadující definici;
- \(D_\mu = \partial_\mu + A_\mu(\cdot) - (\cdot) B_\mu\) je kanonická
  dvoustranná kovariantní derivace;
- \(\mathcal M[\Theta]\) je hmotnostní funkcionál, jehož tvar zde **není odvozen**.

<a id="psi-bs-psi-mode"></a>
### 5.2 Působení na ψ-mód

Na módech tvaru

$$
\Theta_n(q,t)\, e^{in\psi/R_\psi}
$$

derivace dává čistě algebraickou identitu

$$
-i\partial_\psi \Theta_n = \frac{n}{R_\psi}\,\Theta_n.
$$

Znaménko \(n\) rozlišuje dvě orientace \(\psi\)-windingu.
**Samo o sobě to nestanoví** žádnou z následujících věcí:

- identifikaci s fyzikální frekvenční větví;
- chiralitu nebo rukovost;
- sektor částice vs. antičástice;
- vlastní hodnotu hmotnosti;
- sektor nezávislého vesmíru.

Každá taková identifikace vyžaduje nezávislé odvození z kanonických UBT rovnic.

<a id="psi-bs-dirac5-square"></a>
### 5.3 Schematický čtverec kandidátního operátoru

Za předpokladů antikomutace
\(\{\Gamma^\mu,\Gamma^\nu\} = 2\eta^{\mu\nu}\),
\(\{\Gamma^\mu,\Gamma_*\} = 0\),
\(\Gamma_*^2 = +1\) (nebo \(-1\); znaménko musí být fixováno definicí),
a zanedbávajíce hmotnostní, kalibrační a křivostní cross-termy pro schematické
vyjádření,

$$
\mathscr D_5^2
\sim
\mathscr D_4^2 - \partial_\psi^2
+ \text{hmotnostní, kalibrační a křivostní členy}.
$$

Na módu \(e^{in\psi/R_\psi}\) přispívá \(\psi\)-Laplacián vlastní hodnotou

$$
-\partial_\psi^2 \longrightarrow \frac{n^2}{R_\psi^2},
$$

a heat trace přes \(\psi\)-módy tudíž obsahuje Jacobiho váhy

$$
e^{-s n^2/R_\psi^2}.
$$

Jde o **přesný algebraický/spektrální bridge** za uvedených antikomutačních
předpokladů. Samo o sobě to **neodvozuje** celou UBT dynamiku.

<a id="psi-bs-sec6"></a>
## 6. Diracova a Schrödingerova limita

<a id="psi-bs-hierarchy"></a>
### 6.1 Správná hierarchie

Fyzikálně správná hierarchie operátorů je:

$$
\text{first-order Dirac}
\longrightarrow
\text{nerelativistická Pauli / Schrödingerova limita}
$$

a samostatně

$$
\text{Dirac}^2
\longrightarrow
\text{Laplace / Klein–Gordon typ}
\longrightarrow
\text{heat kernel}
\longrightarrow
\text{theta funkce}.
$$

<a id="psi-bs-not-implied"></a>
### 6.2 Co analytická frekvenční selekce NEIMPLIKUJE

Analytická selekce kladně-frekvenčního sektoru second-order rovnice (Sekce 2)
**sama o sobě nevytváří** žádnou z následujících struktur:

- Lokální Cliffordův Diracův operátor.
- Spinorový podprostor nebo reprezentaci.
- Hmotnostní člen nebo hmotnostní matici.
- Grassmannovu / fermionickou statistiku.
- Interpretaci antičástice.

Každá z těchto struktur musí být **nezávisle odvozena** z kanonických UBT
rovnic a algebry.

<a id="psi-bs-sec7"></a>
## 7. Multivesmírná interpretace

> **Status: SPECULATIVE**

<a id="psi-bs-mode-decomp"></a>
### 7.1 Módový rozklad

Formálně lze zapsat

$$
\Theta(q, t, \psi)
= \sum_\alpha \Theta_\alpha(q,t)\, \chi_\alpha(\psi),
$$

kde \(\{\chi_\alpha\}\) je báze přizpůsobená \(S^1_\psi\) (např. Fourierovy
módy \(e^{in\psi/R_\psi}\)).

<a id="psi-bs-mw-caveats"></a>
### 7.2 Výhrady — proč tento ansatz neustanovuje mnoho světů

- **Bodová hodnota** \(\psi = \psi_0\) je obecně superpozicí všech Fourierových
  módů \(n\); nevybírá jediný mód.
- Fyzikální větev vyžaduje definici pomocí projektoru, superselekčního sektoru,
  prostorové lokalizace nebo dekoherenčního mechanismu.
- Bornovy váhy a kolaps vlnové funkce z tohoto ansatzu **nevyplývají**.
- Identifikace \(\psi\)-sektoru s nezávislým vesmírem vyžaduje úplné
  dekoherenční odvození, nikoliv pouhý módový rozvoj.

<a id="psi-bs-speculative-ext"></a>
### 7.3 Odkaz na spekulativní rozšíření

Čistě interpretační tvrzení týkající se kosmologických nebo many-worlds scénářů
jsou zaznamenána odděleně v podstromu `speculative_extensions/` v souladu
s politikou repozitáře.

<a id="psi-bs-sec8"></a>
## 8. Podmíněná poznámka k Riemannově hypotéze

> **Status: CONDITIONAL RESEARCH DIRECTION — NIKOLIV DŮKAZ RH ANI POKROK K RH**

<a id="psi-bs-rh-structural"></a>
### 8.1 Pouze strukturální spojitost

Při logaritmické substituci \(u = e^{2\psi}\) splňuje Jacobiho theta funkce

$$
\vartheta \xrightarrow{\mathrm{Mellin}} \xi(s),
\qquad
u \mapsto 1/u \;\leftrightarrow\; \psi \mapsto -\psi.
$$

Tento Mellinův vztah je klasický a dává **funkcionální rovnici** pro \(\xi(s)\),
nikoliv Riemannovu hypotézu.

<a id="psi-bs-rh-gaps"></a>
### 8.2 Co chybí pro jakékoli propojení s RH

1. **Operátor** \(A_\psi\), samosdružený na vhodném Hilbertově prostoru,
   se vlastností

   $$
   \det(E - A_\psi) \propto \xi(1/2 + iE),
   $$

   spolu s nezávislým důkazem tohoto ztotožnění.

2. Výskyt **prvočíselných délek** \(k \log p\) (pro prvočísla \(p\) a kladná
   celá čísla \(k\)) ve spektru, např. prostřednictvím skutečně odvozeného
   trace formula.

3. Důkaz, že operátor winding čísla \(N_\psi = -iR_\psi\partial_\psi\)
   (s **celočíselnými** vlastními hodnotami \(n\)) je spojen s operátorem
   \(A_\psi\) výše. Celočíselné spektrum \(N_\psi\) samo neodpovídá
   ordinátám nul zeta.

4. Potvrzení, že potlačení rostoucích módů nepředstavuje kruhovité přepsání
   Riemannovy hypotézy.

Žádný z těchto prvků nebyl v UBT stanoven. Strukturální pozorování je
zaznamenáno jako podmíněný směr budoucího výzkumu.

<a id="psi-bs-sec9"></a>
## 9. Audit existujících nekonzistencí tvrzení

> **Rozsah.** Tato sekce zaznamenává pozorovatelné nekonzistence v aktuálním
> repozitáři bez změny kanonických souborů. Opravný kanonický patch je
> **samostatný budoucí úkol**.

<a id="psi-bs-audit-list"></a>

1. **Second-order master equation vs. first-order kandidáti.** Kanonická master
   equation je druhého řádu: \(D^\dagger D\Theta = \kappa\mathcal T\).
   Několik dokumentů výzkumných stop zavádí first-order rovnice v \(t\) bez
   ukázky jejich odvození z kanonické formy.

2. **Dokument o emergenci Schrödingerovy rovnice.** Tento dokument používá
   \(\partial_\tau\Theta = \Box\Theta\), které se liší od kanonické master
   equation i od kandidátní first-order Diracovy formy. Status a cesta odvození
   musí být objasněny.

3. **Záměna označení: first-order vs. Klein–Gordon.** First-order rovnice v \(t\)
   nesmí být označena jako Klein–Gordonova vlnová rovnice; Klein–Gordon je
   second-order v čase z definice.

4. **Palatinská QED Diracova variace.** Variování postulovaného QED Diracova
   Lagrangiánu dává standardní Diracovu rovnici pohybu z konstrukce. To
   neodvozuje QED Lagrangián z UBT; odvození probíhá ve špatném směru.

5. **Kvadratická komutující-Θ akce.** Aktuální kandidátní kvadratická akce v
   komutujícím poli \(\Theta\) nemůže být pouhou field redefinicí převedena na
   first-order fermionickou Diracovu akci, protože first-order fermionická akce
   vyžaduje Grassmannovy (nebo Cliffordově hodnotné) kinetické členy. Jde o
   strukturální překážku, nikoliv o kalkulační mezeru.

<a id="psi-bs-sec10"></a>
## 10. Verifikace

<a id="psi-bs-verif-script"></a>
### 10.1 Verifikační skript

Skript `tools/verify_psi_branch_selection.py` provádí konečněrozměrné
algebraické a numerické kontroly. Spustit příkazem:

```bash
python tools/verify_psi_branch_selection.py
```

Kontrolované položky:

| Kontrola | Popis |
|---|---|
| V1 | Faktorizace second-order skalárního operátoru \((\partial_t^2 + A^2)\) |
| V2 | Obě časové větve \(e^{\pm itA}\) jsou řešeními |
| V3 | Analytické pokračování \(t \mapsto t - i\psi\) |
| V4 | Znaménka decay / growth obou větví pro \(\psi > 0\) |
| V5 | Konečněrozměrný diagonální příklad s kladným samosdruženým \(A\) |
| V6 | Degenerace nulového módu (sektor \(\ker A\)) |
| V7 | Fourierovy vlastní hodnoty \(n\) a \(n^2\) na \(S^1\) |
| V8 | Gaussian \(e^{-sn^2}\) nerozlišuje \(n\) a \(-n\) |

<a id="psi-bs-lean"></a>
### 10.2 Stav Lean formalizace

**LEAN-PENDING.** Lean 4 důkaz nekonečněrozměrné Hardy-\(H^2\) propozice
o výběru větve (Sekce 2.4) dosud neexistuje. Požadovaná formalizace musí
pokrývat:
- teorii domény samosdruženého operátoru v Lean/Mathlib;
- spektrální teorém pro neomezené operátory;
- Hardy-space \(H^2(\mathbb C^-)\) teorii pro operátorově hodnotené funkce.

<a id="psi-bs-sec11"></a>
## 11. Otevřené mezery

<a id="psi-bs-gap-list"></a>

| Mezera | Popis | Status |
|---|---|---|
| G1 | Hardy-\(H^2\) propozice: úplné ověření domény | PROPOSITION / PROOF SKETCH |
| G2 | Kompatibilita half-plane selekce s kompaktním \(S^1_\psi\) | OPEN |
| G3 | Odvození Cliffordova kanálu \(\Gamma_*\) z kanonické UBT | OPEN |
| G4 | Action-level odvození kandidátního Diracova operátoru \(\mathscr D_5\) | OPEN |
| G5 | Fyzikální potlačení torze a vazba na hmotnost | OPEN |
| G6 | Odvozený trace formula s prvočíselnými délkami | OPEN |
| G7 | Lean důkaz nekonečněrozměrného výběru větve | LEAN-PENDING |

<a id="psi-bs-sec12"></a>
## 12. Přehled statusů

| Sekce | Status |
|---|---|
| S2: Matematické selekční lemma | PROPOSITION / PROOF SKETCH |
| S3: Znaménková a UBT-τ algebra | ALGEBRAICKÁ IDENTITA (bez fyzikálního obsahu) |
| S4: Překážka kompaktního ψ | OPEN PROBLEM identifikován |
| S5: Kandidátní Diracova struktura | RESEARCH ANSATZ |
| S6: Hierarchie limit | STANDARDNÍ FYZIKÁLNÍ FAKT (zdokumentován) |
| S7: Multivesmírná interpretace | SPECULATIVE |
| S8: Strukturální poznámka k RH | CONDITIONAL RESEARCH DIRECTION |
| S9: Existující nekonzistence | AUDIT RECORD (žádný kanonický soubor nezměněn) |

Touto stopou nebyl změněn žádný kanonický axiom, definice, master equation
ani status mezery.
