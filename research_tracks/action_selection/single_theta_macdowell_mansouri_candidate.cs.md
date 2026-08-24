<!-- BILINGUAL-UNIT: single-theta-mm.provenance -->
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

# Single-Theta split-jet kandidát MacDowellovy--Mansouriho uzávěry

<!-- BILINGUAL-UNIT: single-theta-mm.goal -->
## Cíl

Nyní lze spojit dva nezávislé výsledky výzkumné linie výběru akce:

- pomocná split-jet mapa umí reprezentovat a variovat všechny čtyři směry
  tetrády bez zavedení nezávislé fundamentální tetrády;
- kanonický pátý Cliffordův kanál převádí jediný kvadrát rozšířené
  křivosti s graduací na Eulerovu topologii, Hilbertovu--Palatiniho gravitaci
  a kosmologický člen s pevnými relativními koeficienty.

Tato poznámka zaznamenává spojeného kandidáta a jeho přesný lokální
klasický důsledek. Nepovyšuje kandidáta na zamčenou akci UBT.

<!-- BILINGUAL-UNIT: single-theta-mm.fields -->
## Architektura polí

Nechť `X` je Lorentzovsky reálná projekce jediného fundamentálního pole
`Theta` a pracujme na patchi s

\[
X^2\ne0.
\]

Použijme fyzické Lorentzovo spojení `omega` a algebraické split-jet proměnné
`K_J,w`. Definujme

\[
\boxed{
E^a=\frac1{\sqrt{N_0}}
\left(dX^a+\omega^a{}_bX^b+K_J{}^a{}_bX^b+wX^a\right).}
\]

Pomocné proměnné neobsahují derivace. Nejsou nezávislými fyzickými stupni
volnosti tetrády; parametrizují lokálně surjektivní single-Theta jetovou
reprezentaci. Fyzická křivost používá `omega`, nikoli `K_J`.

Nechť pátá kanonická Cliffordova matice splňuje

\[
\Gamma_\psi^2=\varepsilon_\psi I_4,
\qquad
\varepsilon_\psi=\pm1.
\]

Definujme rozšířené Cliffordovo spojení

\[
\boxed{
\mathcal A
=\frac14\omega^{ab}\Gamma_a\Gamma_b
+\frac1{2\ell}E^a\Gamma_a\Gamma_\psi.}
\]

<!-- BILINGUAL-UNIT: single-theta-mm.action -->
## Jeden kandidát kvadrátu křivosti

S bezrozměrnou gravitační křivostní vazbou `g_G` uvažujme

\[
\boxed{
S_{\rm cand}[\Theta,\omega,K_J,w]
=-\frac{i\varepsilon_\psi}{g_G^2}
\int\operatorname{Tr}
\left(\Gamma_*\mathcal F\wedge\mathcal F\right),
\qquad
\mathcal F=d\mathcal A+\mathcal A\wedge\mathcal A.}
\]

V tomto výrazu není nezávisle variovaná tetráda. Tetráda je výše uvedeným
kompozitním split-jet objektem. `omega`, `K_J` a `w` jsou geometrické nebo
pomocné variační proměnné; tato poznámka netvrdí, že jde o nová fundamentální
propagující pole.

Přesný Cliffordův výpočet dává

\[
\boxed{
\kappa=\frac{g_G^2\ell^2}{2},
\qquad
\Lambda=\frac{3\varepsilon_\psi}{\ell^2},
\qquad
\kappa\Lambda=\frac32\varepsilon_\psi g_G^2.}
\]

S těmito identifikacemi je akce

\[
\boxed{
S_{\rm cand}
=S_{\rm HP}[E,\omega;\kappa,\Lambda]
-\frac{\varepsilon_\psi\ell^2}{8\kappa}
\int\epsilon_{abcd}R^{ab}\wedge R^{cd}.}
\]

Druhý člen je Eulerova topologie a při pevné topologii nemění lokální
objemové rovnice.

<!-- BILINGUAL-UNIT: single-theta-mm.variation -->
## Lokální věta o množině řešení [L1]

Na každém patchi s `X^2 != 0` je split-jet variační mapa

\[
(\delta K_J,\delta w)\longmapsto\delta E
\]

bodově surjektivní na všechny směry tetrády. Její transpozice je tedy
injektivní na Palatiniho tetrádové Eulerově formě. Stacionarita `S_cand`
vzhledem ke split-jet pomocným proměnným dává úplnou tetrádovou rovnici

\[
\boxed{\mathcal E_a^{\rm HP}=0.}
\]

Fyzické spojení se objevuje jak v křivosti, tak v kompozitní tetrádě.
Příspěvek druhého typu z řetězového pravidla je úměrný
`mathcal E_a^{HP}` a po dosazení split-jet rovnice mizí. Zbývající variace
`omega` je standardní Palatiniho variací spojení. Ve vakuu bez spinu

\[
\boxed{T^a=0,
\qquad
\omega=\mathring\omega(E).}
\]

Variace `Theta`/`X` je diferenciálním důsledkem úplné tetrádové rovnice,
protože `X` vstupuje do objemové gravitační akce přes kompozitní `E`. Obráceně
lze každé lokální Palatiniho řešení liftovat do split-jet proměnných pomocí
explicitní nenulové pravé inverze.

Proto až na algebraický jetový stabilizátor a okrajová/topologická data platí

\[
\boxed{
\{\text{local stationary points of }S_{\rm cand}\}
\longleftrightarrow
\{\text{local Einstein--Lambda Palatini solutions}\}}
\]

na nenulovém split-jet patchi.

Jde o lokální podmíněnou větu o ekvivalenci pro **zvoleného kandidáta**.
Nejde o odvození tohoto kandidáta ze starší zamčené kinetické akce.

<!-- BILINGUAL-UNIT: single-theta-mm.advance -->
## Skutečný posun

Zbývající GR gap už není spojením několika nesouvisejících problémů. V
rámci jednoho přesně specifikovaného kandidáta nyní máme:

- žádné nezávislé tetrádové pole;
- lokálně hodnostně surjektivní single-Theta reprezentaci tetrády;
- úplnou tetrádovou Einsteinovu rovnici, nikoli projektovanou rovnici;
- pomocné fyzické spojení redukující se ve vakuu na Leviho--Civitovo;
- Palatiniho tenzorovou kontrakci generovanou kanonickou Cliffordovou graduací;
- kosmologický člen generovaný toutéž rozšířenou křivostí;
- pouze dva spojité parametry kandidáta, `g_G` a `ell`, které nahrazují
  nezávislé `kappa` a `Lambda`.

Tvar klasického GR sektoru je tedy podstatně méně libovolný než v dřívější
vložené Hilbertově--Palatiniho větvi.

<!-- BILINGUAL-UNIT: single-theta-mm.remaining -->
## Přesné zbývající fundamentální otázky

Nepodmíněná rekonstrukce GR z UBT stále vyžaduje mikroskopické odpovědi na
následující body:

1. **princip rozšířené kalibrační symetrie:** odvodit, proč kanonický pátý
   Cliffordův kanál patří do fyzického rozšířeného spojení s koeficientem
   `1/(2 ell)`;
2. **graduace/redukce symetrie:** odvodit vložení `Gamma_*` nebo ekvivalentní
   Lorentzovu projekci z dynamiky komplexního času/pátého kanálu, nikoli je
   zvolit pro reprodukci orientovaného Palatiniho kanálu;
3. **výběr škály:** odvodit `ell`; jeho ztotožnění s poloměrem `psi` je pouze
   kandidátem, dokud není určen fyzický význam kanálu `psi`;
4. **celková vazba:** odvodit `g_G` nebo jeho vztah k jiné nezávisle odvozené
   vazbě UBT; existující poznámky o `8 pi` jej neurčují;
5. **globální dokončení:** ošetřit patche `X^2=0`, topologii/hranice a
   globální pokračování;
6. **úplné sektory:** ukázat, že tatáž fundamentální akce dává také
   požadovanou kalibrační, hmotovou, kvantovou a fyzickou `psi` dynamiku bez
   přidání samostatných fundamentálních akcí.

Nyní jde o otázky výběru/původu. Samotná lokální klasická variační
architektura již není hlavní obstrukcí tohoto kandidáta.

<!-- BILINGUAL-UNIT: single-theta-mm.falsification -->
## Ostré podmínky falzifikace

Tento kandidát má být odmítnut jako fundamentální dokončení UBT, pokud
nastane cokoli z následujícího:

- neexistuje UBT-nativní odvození rozšířeného spojení pátého kanálu;
- požadované vložení graduace je neslučitelné se zamčenými symetriemi
  komplexního času;
- větev `X^2=0` nelze pokrýt regulární ekvivalentní formulací;
- odvozené `g_G,ell` predikují Newtonův/kosmologický sektor neslučitelný s
  pozorováním;
- tatáž akce nedokáže pojmout negravitační sektory bez přidání nezávislých
  fundamentálních členů.

Selhání kandidáta by nevyvrátilo dřívější kinematické výsledky UBT;
vyloučilo by toto konkrétní dokončení akce.

<!-- BILINGUAL-UNIT: single-theta-mm.verification -->
## Verifikace

Konečná kritická algebra věty je nezávisle kontrolována pomocí:

- `tools/verify_split_jet_palatii_variational_lift.py` — split-jet variace
  hodnosti čtyři a explicitní pravá inverze;
- `tools/verify_clifford_palatini_trace_selector.py` — kanonická gradovaná stopa
  a klasifikace bivectorových invariantů;
- `tools/verify_fifth_channel_macdowell_mansouri.py` — komutátory pátého
  kanálu, gradovaná projekce a přesné sesouhlasení koeficientů.

Variační složení používá již zavedené Palatiniho/Cartanovy identity a
identitu Eulerovy topologie. Formalizace úplné věty o diferenciálních formách
v Leanu zůstává `LEAN-PENDING`.

<!-- BILINGUAL-UNIT: single-theta-mm.status -->
## Status

**LOKÁLNÍ SINGLE-THETA SPLIT-JET KANDIDÁT KVADRÁTU KŘIVOSTI S EKVIVALENCÍ
MNOŽINY EINSTEINOVÝCH--LAMBDA ŘEŠENÍ: CLOSED CONDITIONALLY [L1].**

**VZTAHY PARAMETRŮ UVNITŘ KANDIDÁTA:
`kappa=g_G^2 ell^2/2`, `Lambda=3 epsilon_psi/ell^2`: PROVED [L1].**

**MIKROSKOPICKÝ VÝBĚR ROZŠÍŘENÉHO SPOJENÍ, GRADUACE, `g_G` A `ell`:
OPEN.**

**NEPODMÍNĚNÁ REKONSTRUKCE GR Z DŘÍVE ZAMČENÉ DYNAMIKY UBT:
NOT YET CLOSED.**
