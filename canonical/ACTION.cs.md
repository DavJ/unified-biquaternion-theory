<!-- BILINGUAL-UNIT: single-action.provenance -->
<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: B_machine_verified
ai_assistance: disclosed
human_review: machine-verification
editorial_responsibility: Ing. David Jaroš
policy: ../AI_PROVENANCE.md
notice: Machine-verified against named sources or verifiers; individual attestation is not claimed.
UBT-AI-PROVENANCE-END
-->

# Invariant jediné akce UBT

<!-- BILINGUAL-UNIT: single-action.rule -->
## Závazné pravidlo

UBT smí mít právě jednu fundamentální akci. Symbol `S_UBT[Theta]` je vyhrazen
výhradně této akci. Sektorový funkcionál smí být označen pouze jako redukce,
efektivní akce, pomocná akce nebo historický kandidát a musí být uvedeno jeho
odvozovací zobrazení z `S_UBT`. Dva neekvivalentní funkcionály nesmějí být oba
citovány jako „kanonická akce UBT“.

Kanonický zdroj již definuje kineticko-potenciálovou rodinu

`S_Theta = 1/2 int sqrt(-g) <D_mu Theta,D^mu Theta> - kappa V[Theta]`.

Výslovně ponechává znaménko a měřítko kinetického členu, `kappa` a tvar `V`
jako dynamické vstupy a neodvozuje úplnou gravitační akci. Aktuální hodnota
registru je proto:

```yaml
fundamental_action_family: S_Theta
source: canonical/THEORY/canonical/canonical_action.tex:46
status: DEFINED_FAMILY_NOT_FINALIZED
related_open_gap: UBT-FUND-GR-ACTION
```

Dokud nebude dokončena finalizace, není holý odkaz na „kanonickou akci“
přípustnou premisou pro uzavření dynamického gapu.

<!-- BILINGUAL-UNIT: single-action.inventory -->
## Konfliktní vzorce v současných kanonických zdrojích

| Zdroj | Míra/obor | Předpis reálného skaláru | Klasifikace |
|---|---|---|---|
| `THEORY/canonical/canonical_action.tex` | `sqrt(-g) d4x` | abstraktní párování | deklarovaná kanonická rodina; znaménko, měřítko, `kappa` a potenciál nejsou finalizovány |
| `appendices/appendix_ACTION_review.tex` | `sqrt(-g) d4x` | komplexní stopa/hermitovské členy | postulovaná efektivní akce GR + Yang–Mills + hmota, nikoli Theta-only odvození |
| `bridges/theta_quantum_structure.tex` | `sqrt(|det G|) d4x dτ` | abstraktní párování | vícerozměrný kvantový kandidát; citované odvození není současný kanonický zdroj |
| `8pi_common_origin.tex` | `d4x dψ` | `Re Tr` | kandidát/pokus indukované gravitace |
| `qm_emergence/step4_fpe_equivalence.tex` | `d4x` | varianty `Sc` i `Re(Sc)` | kandidáti uspořádání/reality pro QM redukci |
| `qm_emergence/step2_schrodinger_emergence.tex` | `sqrt(-g) d4x` a `d4x` | součin s dagger | kandidáti relativistické skalární redukce |
| `qm_emergence/step1_fpe_check.tex` | `dQ dT` | komplexní kinetická forma | nerelativistický efektivní kandidát |
| `alpha/prime_selection_principle.tex` | `d4x dτ dτbar` | neurčená kontrakce | kandidát modulárního sektoru |
| `symmetry/effective_vs_fundamental_breaking.tex` | `sqrt(-g) d4x` | zástupný symbol `L_UBT` | zástupný symbol, nikoli definice |
| `n_eff/step2_AUDIT.tex` | `d4x dψ` | `Sc` | skalární smyčková redukce použitá pro audit |

Tyto vzorce se liší integračním oborem, předpisem reality, nezávislými poli a
dynamickým obsahem. Nejde tedy o zaměnitelné zápisy jedné zavedené akce.

<!-- BILINGUAL-UNIT: single-action.requirements -->
## Požadavky na finalizaci

Finalizovaná `S_UBT[Theta]` musí bez sektorových záměn určit:

1. konfigurační prostor a zda je `psi` souřadnicí, nebo polem;
2. mikroskopickou integrační míru a kvocient/Jacobián;
3. reálné biquaternionické párování;
4. všechny nezávislé oproti kompozitním konexím a metrikám;
5. řád derivací, potenciál, hraniční členy a volné parametry;
6. úplné Eulerovy–Lagrangeovy rovnice a kalibračně fixovaný Hessián;
7. stabilitu fyzikálních a `psi` módů;
8. explicitní redukční zobrazení na efektivní akce GR, Yang–Mills, hmoty a QM.

Dimenzionální konzistence, symetrie a omezenost zdola jsou nutné testy, nikoli
důkaz výběru. Akce je vybrána teprve tehdy, když je její nevázaná variace dobře
definována a tvrzené sektorové akce z ní plynou, místo aby byly vloženy jako
další fundamentální členy.

První kritický teoretický úkol má nyní exaktní výsledek pro přesně vymezený
ansatz. Pro obecné `X=rho(Theta)` v `Mat(2,C)` při působení
`X -> exp(i alpha) S X S^dagger`, kde `S` náleží `SL(2,C)`, má každý reálný
lokální polynomiální potenciál stupně nejvýše čtyři tvar

\[
 V(X)=V_0+m^2H(X)+\lambda_1H(X)^2+\lambda_2|\det X|^2,
 \qquad H(X)=\operatorname{Tr}(X^\sharp X^\dagger).
\]

Prostor kvadratických invariantů má rozměr `1` a prostor kvartických invariantů
má rozměr `2`. Exaktní důkaz hodnosti a nezávislá racionální kontrola jsou
zaznamenány v
`research_tracks/action_selection/theta_potential_invariants.cs.md`. Kladná
hermitovská veličina `Tr(X^dagger X)` je vyloučena explicitním protipříkladem
s neunitárním boostem. Tato klasifikace určuje invariantní bázi, nikoli reálné
koeficienty. Další působení na vnitřní nosič, diskrétní involuce, omezenost zdola
a stabilita mohou rodinu dále zúžit.

<!-- BILINGUAL-UNIT: single-action.falsification -->
## Předem stanovené falzifikační kritérium

Jakmile bude explicitně deklarována konečněrozměrná rodina kandidátů, minimální
program jediné akce selhává, jestliže každý její přípustný člen selže alespoň
v jednom z těchto současně požadovaných testů:

- nenulový konečný koeficient Einsteinova–Hilbertova členu se dvěma derivacemi
  v infračerveném limitu;
- stabilní fyzikální fluktuace bez neodstraněného ghostu nebo nestabilního
  `psi` módu;
- odvozená Yangova–Millsova kinetická struktura na vybraném carrieru;
- konzistentní reálná míra a variační princip.

Selhání je výsledkem o mezích navržené dynamiky UBT. Není svolením zavést pod
stejným názvem další objekt bez zaznamenání nové volby teorie a zopakování
úplného srovnání.

<!-- BILINGUAL-UNIT: single-action.prediction -->
## Pojistka kvantitativní predikce

V tuto chvíli zde není zaregistrována žádná bezparametrická kvantitativní
predikce UBT odvozená z jediné fundamentální akce. Reprodukovaný nebo
renormalizovaný koeficient kalibrovaný z pozorování takovou predikcí není.
První přijatá predikce musí před porovnáním s daty uvést číselnou hodnotu,
nejistotu, experimentální pozorovatelnou veličinu a všechny vstupy.

<!-- BILINGUAL-UNIT: single-action.priority -->
## Priorita programu a zmrazení rozsahu

Dokud nebude fundamentální akce finalizována, nové spekulativní sektory se
nepočítají jako pokrok kanonické teorie a nesmějí zavádět další fundamentální členy.
Pořadí práce na kanonické fyzice je:

1. finalizovat již definovanou rodinu jediné akce;
2. provést její variaci bez přizpůsobování výsledku požadovanému cíli;
3. určit její Hessián, stupně volnosti a stabilitu;
4. odvodit sektorové redukce z téhož objektu;
5. teprve potom porovnat předem registrovanou kvantitativní predikci s daty.

Práce v Leanu má přednost pro konečnou kritickou algebru, která již nese
tvrzení L0: ekvivalenci biquaternionů, matic a Cliffordovy algebry, hodnost
zobrazení tetrády na metriku a jeho Lorentzovo jádro, hodnost zobrazení
kontorze na torzi a no-go pro Lorentzovsky invariantní párování. Formální
důkazy logických implikací, jejichž fyzikální premisy zůstávají předpokládány,
musí být takto označeny a neuzavírají gapy na úrovni akce.
