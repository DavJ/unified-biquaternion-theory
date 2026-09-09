<!-- BILINGUAL-UNIT: action-decision.provenance -->
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

# Rozhodovací hranice pro bezpodmínečné uzavření GR

<!-- BILINGUAL-UNIT: action-decision.result -->
## Přesný současný výsledek

Existující zamčené kinematické axiomy **neurčují** jedinou mikroskopickou akci
dostatečně silně k povýšení obnovy GR z `CLOSED_CONDITIONALLY` na
bezpodmínečné `CLOSED`.

Nejde pouze o nedokončený výpočet. Repozitář nyní obsahuje několik exaktních
obstrukcí:

- kinematické axiomy připouštějí spojitou rodinu vzniklou přidáním libovolného
  Einsteinova–Hilbertova koeficientu včetně nuly, takže tento koeficient není
  důsledkem kinematiky;
- úplný kvartický potenciál invariantní vůči spojené symetrii má na
  koeficientech nezávislý nekompaktní plochý směr `H=D=0` a sám nemůže vybrat
  izolované vakuum;
- každý čistě gravitační skalár nezávislý na hodnotě pole a algebraicky
  závislý pouze na témže prvním jetu se redukuje na kosmologickou objemovou
  hustotu;
- na čistě gradientové větvi metric-locku je zobrazený kvadratický kinetický
  člen Jacobiánovým null Lagrangianem a nedává objemový propagující Hessián;
- kompozice `S_EH` s metrickým zobrazením `g(Theta)` dává
  `delta S/delta Theta = L_Theta^* E`; Einsteinova dynamika plyne opačným
  směrem až po důkazu diferenciální injektivity adjungovaného operátoru nebo
  ekvivalence, kterou bodová hodnost metriky neposkytuje;
- split-jet omezení je surjektivní pro každou tetrádu, takže konfigurace GR
  reprezentuje, ale nemůže z `Theta` jednu vybrat;
- pro existující skalární multisymplektickou rodinu platí
  \(Q=0\), \(S_F=0\) a \(\delta S_F=0\) na kanonickém Lorentzově jetu,
  a to i po diferencovatelném dosazení složené konexe; explicitní stacionární
  neeinsteinovskou metriku poskytuje
  [audit Lorentzova řezu](multisymplectic_lorentz_slice_audit.cs.md).

Žádná poctivá změna statusu proto nemůže zbývající gap na úrovni akce
odstranit. Je nutná nová **odvozená dynamická věta** nebo explicitně schválený
**nový dynamický princip**.

<!-- BILINGUAL-UNIT: action-decision.routes -->
## Zbývající cesty výběru akce

### Cesta A — přímá kompozitní akce křivosti

Použít funkcionál vyššího jetu, jehož geometrická redukce obsahuje
`sqrt(-g(Theta)) R[g(Theta)]`.

Než se tato cesta započítá jako mikroskopické odvození, je nutné:

- sestrojit skutečně lokální zakřivené zobrazení `Theta -> g[Theta]` bez
  nezávisle propagující tetrády/konexe;
- dokázat podmínku injektivity adjungovaného operátoru nebo ekvivalence pro
  linearizaci metriky;
- určit, proč je vybrán právě tento invariant křivosti, a nikoli spojitá
  rodina s libovolným koeficientem a přídavnými členy vyšší křivosti.

Pokud se Einsteinův–Hilbertův člen prostě postuluje, GR je zakódována v nové
akci, nikoli odvozena z předchozích axiomů UBT.

### Cesta B — spektrální/generalizovaná Diracova akce

Povýšit úplně definovaný generalizovaný Diracův operátor UBT na spektrální
akci a odvodit nízkoenergetické koeficienty z jeho tepelného jádra. Tato cesta
je strukturálně atraktivní, protože stejná spektrální expanze může v principu
vytvořit gravitační i gauge kinetické členy.

V současnosti není uzavřena. Vyžaduje finalizovaný operátor a jeho obor,
podmínky reality/samosdruženosti nebo kontrolované eukleidovské pokračování,
fyzikální Hilbertův prostor a kvocient módů, princip cutoffu/profilu a důkaz,
že všechny tyto objekty jsou funkcemi jediných dat UBT a nejsou importovanými
strukturami Standardního modelu/GR. Současná spektrální trojice v repozitáři je
explicitně pracovní/spekulativní konstrukce.

### Cesta C — UBT-native degenerovaná/vyšší-jetová akce Theta

Odvodit novou lokální akci přímo z bikvaternionové/theta struktury, případně s
antisymetrickými členy vyššího jetu, komutátory křivosti nebo degenerovanými
členy prvního řádu, a dokázat, že její nevázané Eulerovy–Lagrangeovy rovnice
vybírají požadovanou zakřivenou metrickou větev.

To by byl nejsilnější význam emergence, ale žádná současně dokázaná modulární
nebo Jacobiho tepelná identita zatím není ustanovena jako fyzikální dynamický
selektor. Povýšení theta heat equation na dynamiku by bylo novou volbou teorie,
pokud nebude samostatně odvozeno.

### Cesta D — přímá biquaternionová indukovaná gravitace

Odvodit skutečný gauge-fixovaný nedegenerovaný fluktuační operátor z finální
jediné akce `Theta` a spočítat jeho koeficient tepelného jádra při zachování
kanonické kovariantní tetrády. Jde o cestu nazvanou „B“ v současné výzkumné
diskusi. Zůstává výzkumnou možností. V Lorentzově reálné omezené objemové
akci má úplný Hessián nulový symbol druhého řádu jak pro pevnou zakřivenou
Lorentzovu konexi, tak pro konexi závislou pouze na hodnotách pole, včetně
zahrnutí celé této závislosti do variace. Výsledek nepokrývá konexi závislou
na derivacích ani všech osm reálných biquaternionových fluktuačních směrů.
Úplné Eulerovy a Jacobiho vzorce pro pevnou konexi, důkaz pro závislost na
hodnotách pole a zbývající kompozitní řetězové pravidlo uvádí
[audit biquaternionové indukované gravitace](biquaternionic_induced_gravity_boundary.cs.md).

<!-- BILINGUAL-UNIT: action-decision.recommendation -->
## Výzkumné doporučení

Upřednostněnou cestou je nyní cesta D, formulovaná přímo s původním
biquaternionovým polem a kovariantní tetrádou
\(E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\). Cliffordův nebo generalizovaný
Diracův lift může zůstat algebraickou diagnostikou, ale nesmí nahradit
`Theta`, tetrádu ani fyzický fluktuační Hessián.

Dalším vysoce hodnotným výpočtem je proto úplný kompozitní biquaternionový
Hessián včetně indukovaných variací `E`, `g` a fyzikální konexe. Jeho
kalibrační/omezující podíl, eukleidovská kontura, vazba na křivost a princip UV
škály musí být poté odvozeny, než lze koeficient tepelného jádra označit za
predikci `G`. Cesta A zůstává konzistentním efektivním doplněním s jedním
koeficientem, pokud se ji autor rozhodne přijmout, ale není preferovaným
výsledkem z prvních principů.

<!-- BILINGUAL-UNIT: action-decision.status -->
## Status

**UNCONDITIONAL GR ACTION SELECTION FROM CURRENT LOCKED AXIOMS: NOT DERIVED.**

**SEARCH SPACE: NARROWED TO EXPLICIT HIGHER-JET / SPECTRAL / INDUCED DYNAMICAL
PRINCIPLES.**

Tento dokument nemění zamčené axiomy a neopravňuje novou fundamentální akci.
Zaznamenává přesný bod, v němž by se stala nutnou autorská volba teorie, pokud
se nenajde další odvození.
