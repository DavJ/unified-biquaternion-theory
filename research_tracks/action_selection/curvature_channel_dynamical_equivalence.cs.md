<!-- BILINGUAL-UNIT: curvature-equivalence.provenance -->
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

# Nejednoznačnost kanálů křivosti a přesný cíl klasické GR

<!-- BILINGUAL-UNIT: curvature-equivalence.scope -->
## Rozsah

Existující Cliffordův audit klasifikuje dva Lorentzovsky invariantní kanály
křivosti. Je třeba rozlišovat jednoznačnost akce a ekvivalenci jejích
lokálních klasických rovnic. Tato poznámka dokazuje příslušnou ekvivalenci
ve dvou určených rodinách včetně případů selhání.
Žádnou z rodin nevybírá jako fundamentální akci UBT.

Klasický Palatiniho--Holstův mechanismus je standardní; viz
[zobecněná Hilbertova--Palatiniho akce Sörena Holsta](https://arxiv.org/abs/gr-qc/9511026).
Kontext rozšířené konexe poskytuje standardní MacDowellova--Mansouriho
konstrukce; viz [Cartanovský výklad Dereka Wise](https://arxiv.org/abs/gr-qc/0611154).
U těchto gravitačních konstrukcí se netvrdí novost. Zde jsou použity
k upřesnění zbývajících požadavků na výběr kanonických Cliffordových
kandidátů UBT a kandidátů s oddělenou jetovou konexí.

Pracujeme lokálně na orientované hladké čtyřrozměrné oblasti
s nedegenerovaným reálným koreperem \(E^a\), Lorentzovou metrikou
\(\eta=\operatorname{diag}(-1,1,1,1)\) a fyzikální Lorentzovou konexí
\(\omega^{ab}=-\omega^{ba}\). Všechna pole jsou hladká a variace mají
kompaktní nosič. Koreper a konexe jsou zprvu nezávislé.

\[
R^{ab}=d\omega^{ab}+\omega^a{}_c\wedge\omega^{cb},\qquad
T^a=dE^a+\omega^a{}_b\wedge E^b,\qquad
\Sigma_{ab}=E_a\wedge E_b.
\]

Vnitřní dualita působí na Lorentzovy indexy, nikoli na stupeň časoprostorové
diferenciální formy:

\[
(\star Y)_{ab}=\frac12\epsilon_{ab}{}^{cd}Y_{cd},\qquad
\epsilon_{0123}=1,\qquad \star^2=-I.
\]

<!-- BILINGUAL-UNIT: curvature-equivalence.holst -->
## H1 — Celá reálná Palatiniho--Holstova rodina dává vakuovou GR [L1]

Pro konstantní reálné koeficienty uvažujme

\[
S_{u,v,\lambda}
=\frac u4\int\epsilon_{abcd}E^a\wedge E^b\wedge R^{cd}
 +\frac v2\int E^a\wedge E^b\wedge R_{ab}
 -\frac{\lambda}{24}\int\epsilon_{abcd}
 E^a\wedge E^b\wedge E^c\wedge E^d.
\]

**Věta.** Pro tuto samotnou akci ve vakuu s \(u\ne0\) jsou rovnice
přesně

\[
\boxed{T^a=0,\qquad
G_{\mu\nu}+\frac{\lambda}{u}g_{\mu\nu}=0.}
\]

Každé konstantní reálné \(v\) dává při pevných \(u,\lambda\) stejné
lokální vakuové rovnice. Není zahrnut zdroj hmoty ani další sektor akce.

**Důkaz: rovnice konexe.** Variujme křivost před eliminací konexe,
použijme \(\delta R=D_\omega\delta\omega\) a integrujme per partes.
Rovnice má tvar

\[
\mathcal P_{u,v}D_\omega\Sigma=0,\qquad
\mathcal P_{u,v}=u\star+vI.
\]

Identita pro Lorentzovu signaturu dává

\[
\det\mathcal P_{u,v}=(u^2+v^2)^3,\qquad
\mathcal P_{u,v}^{-1}
=\frac{vI-u\star}{u^2+v^2}.
\]

Proto \(D_\omega\Sigma=0\). Zobrazení
\(T^a\mapsto T^a\wedge E^b-E^a\wedge T^b\) je pro nedegenerovaný
koreper injektivní. Přímý důkaz používá jeho duální reper \(\iota_a\).
Položme \(\zeta=\sum_a\iota_aT^a\). Kontrakce
\(E^a\wedge T^b-E^b\wedge T^a=0\) se součtem přes druhý index dává
\(T^a=-E^a\wedge\zeta\). Další kontrakce vede k
\(\zeta=-3\zeta\), tedy \(\zeta=0\) a \(T^a=0\).
Fyzikální konexe je proto Leviho--Civitova.

**Důkaz: rovnice koreperu.** Nezávislá variace koreperu dává

\[
\frac u2\epsilon_{abcd}E^b\wedge R^{cd}
 +vE^b\wedge R_{ab}
 -\frac{\lambda}{6}\epsilon_{abcd}E^b\wedge E^c\wedge E^d=0.
\]

Po uložení rovnice konexe první Bianchiho identita
\(D_\omega T^a=R^a{}_b\wedge E^b\) vynuluje Holstův člen.
Zbývá uvedená Einsteinova rovnice. Obráceně každé Einsteinovo řešení
bez torze splňuje obě původní variační rovnice.
Tento argument nejprve provádí variaci; nemaže Holstův člen předběžným
dosazením konexe bez torze do akce.

V této určené rodině platí identifikace

\[
\kappa=\frac1u,\qquad \Lambda=\frac{\lambda}{u}.
\]

Věta neurčuje tyto konstanty ani fyzikální znaménko \(u\).

<!-- BILINGUAL-UNIT: curvature-equivalence.limits -->
## H2 — Přesné meze ekvivalence

**Čistý Holstův člen.** Jestliže \(u=0\), \(v\ne0\) a \(\lambda=0\),
rovnice konexe stále vynucuje nulovou torzi, ale rovnice koreperu je pak
pouze Bianchiho identitou. Splňuje ji každý koreper bez torze včetně
neeinsteinovských metrik. Pokud naopak \(\lambda\ne0\), objemová rovnice
nemá řešení s nedegenerovaným koreperem. Nenulová Palatiniho složka je nezbytná.

**Komplexní koeficienty.** Pro \(v=\pm iu\ne0\) má komplexní bivektorové
zobrazení hodnost tři a zobrazená inverze neexistuje. Chirální formulace
vyžadují vlastní proměnné a podmínky reality; tato věta je nevylučuje.

**Spinový proud.** Zadaný proud definujme konvencí

\[
\delta_\omega S_{\rm m}=\frac12\int\tau_{ab}\wedge\delta\omega^{ab}.
\]

Rovnice konexe pak zní

\[
\mathcal P_{u,v}D_\omega\Sigma=\tau,\qquad
D_\omega\Sigma=\frac{vI-u\star}{u^2+v^2}\tau.
\]

Pro nenulový proud torzní odezva obecně závisí na \(v\).
Vakuová věta nemůže určit vazbu na hmotu ani fyzikální kvocient módů.

**Proměnný koeficient.** Je-li \(u\ne0\) konstantní, ale \(v=v(x)\), platí

\[
(u\star+vI)D_\omega\Sigma+dv\wedge\Sigma=0.
\]

Na nedegenerované větvi bez torze to vyžaduje \(dv=0\): jednoforma,
jejíž vnější součin s každou dvouformou koreperu mizí, musí sama být nulová.
Libovolný Holstův koeficient závislý na poli tedy věta H1 nepokrývá.

<!-- BILINGUAL-UNIT: curvature-equivalence.commutant -->
## C1 — Konstantní Lorentzovsky skalární Cliffordovy vložky [L0]

Použijme kanonické matice \(\Gamma_a,\Gamma_*\) a
\(\mathcal J_{ab}=\Gamma_a\Gamma_b/2\) pro různé indexy.
Cliffordovy, gradační a stopové konvence jsou

\[
\{\Gamma_a,\Gamma_b\}=2\eta_{ab}I_4,\qquad
\Gamma_*^2=I_4,\qquad \{\Gamma_*,\Gamma_a\}=0,\qquad
\operatorname{Tr}(\Gamma_*\Gamma_a\Gamma_b\Gamma_c\Gamma_d)
=-4i\epsilon_{abcd}.
\]

Pátá matice je pevně určena jako

\[
\Gamma_\psi=
\begin{cases}
\Gamma_* & \varepsilon_\psi=+1,\\
i\Gamma_* & \varepsilon_\psi=-1.
\end{cases}
\]

Pro konstantní komplexní matici \(Z\) je přesný komutant

\[
[Z,\mathcal J_{ab}]=0\quad(\forall a<b)
\quad\Longleftrightarrow\quad
Z=z_0I_4+z_*\Gamma_*.
\]

V kanonické blokové bázi komutování se třemi rotacemi vynutí, aby každý
ze čtyř maticových bloků byl skalárním násobkem jednotkové matice.
Komutování se třemi boosty vynutí nulovost mimodiagonálních bloků.
Zbývající dva skalární diagonální bloky tvoří přesně uvedený lineární obal.
Ověřovací skript navíc řeší úplný maticový systém bez předpokladu blokového tvaru.

Pro obě znaménka pátého kanálu přidání všech translačních generátorů
\(P_a=\Gamma_a\Gamma_\psi/2\) ke komutačním podmínkám vynutí
\(z_*=0\). Komutant úplné rozšířené reprezentace tedy obsahuje
jen skalární matice.

To klasifikuje konstantní vložky, které jsou samy skaláry dané symetrie.
Nejde o klasifikaci všech možných akcí závislých na poli.

<!-- BILINGUAL-UNIT: curvature-equivalence.topology -->
## C2 — Negradovaný čtverec rozšířené křivosti je lokálně neúčinný [L1]

Zachovejme již navrženou rozšířenou konexi s konstantami
\(\ell>0\) a \(\varepsilon_\psi=\pm1\):

\[
\mathcal A=\frac14\omega^{ab}\Gamma_a\Gamma_b
 +\frac1{2\ell}E^a\Gamma_a\Gamma_\psi,\qquad
\mathcal F=d\mathcal A+\mathcal A\wedge\mathcal A.
\]

Existující rozklad křivosti a negradované Cliffordovy stopy dávají

\[
\boxed{
\operatorname{Tr}(\mathcal F\wedge\mathcal F)
=-\frac12R^{ab}\wedge R_{ab}
 +\frac{\varepsilon_\psi}{\ell^2}
 \left(E^a\wedge E^b\wedge R_{ab}-T^a\wedge T_a\right).}
\]

Smíšená stopa Lorentzovy a translační části mizí.
Kontrahovaný člen se čtyřmi formami koreperu mizí kvůli opakování jednoforem.
Stopa čtverce translační části dává uvedený koeficient čtverce torze.
Tato tvrzení platí před uložením nulové torze.

Identita

\[
d(E^a\wedge T_a)
=T^a\wedge T_a-E^a\wedge E^b\wedge R_{ab}
\]

plyne z první Bianchiho identity. Negradovaná hustota je tedy
Lorentzovou Pontryaginovou hustotou plus Niehovým--Yanovým okrajovým členem.
Ekvivalentně úplná rozšířená Bianchiho identita dává

\[
\boxed{
\delta\operatorname{Tr}(\mathcal F\wedge\mathcal F)
=2\,d\operatorname{Tr}(\delta\mathcal A\wedge\mathcal F).}
\]

Její integrál s konstantním koeficientem má nulovou lokální objemovou
variaci i tehdy, když je rozšířená konexe hladkým složeným funkcionálem
variovaných polí. To zahrnuje úplnou indukovanou variaci koreperu i konexe.
Globální topologie, okrajové pozorovatelné veličiny a kvantové fáze mohou
na tomto koeficientu nadále záviset.

Pro zadaný nekonstantní koeficient \(c(x)\) variace konexe s kompaktním
nosičem místo toho dává

\[
\delta\int c\,\operatorname{Tr}(\mathcal F\wedge\mathcal F)
=-2\int dc\wedge
\operatorname{Tr}(\delta\mathcal A\wedge\mathcal F).
\]

Dynamický koeficient přispívá i svou vlastní variací. Předpoklad
konstantního koeficientu nelze mlčky vypustit.

<!-- BILINGUAL-UNIT: curvature-equivalence.extended -->
## C3 — Co musí gradovaný kanál skutečně dodat [L1]

Pro konstantní reálné koeficienty uvažujme úplnou rodinu se dvěma vložkami

\[
S_{c_g,c_t}=\int
\left[
c_g\,i\operatorname{Tr}(\Gamma_*\mathcal F\wedge\mathcal F)
+c_t\,\operatorname{Tr}(\mathcal F\wedge\mathcal F)
\right].
\]

Podle C2 druhý člen nepřispívá k lokálním objemovým rovnicím.
Rozvinutí prvního členu včetně jeho Eulerovy hustoty určuje

\[
u=-\frac{2\varepsilon_\psi c_g}{\ell^2},\qquad
\lambda=-\frac{6c_g}{\ell^4},\qquad
\kappa=-\frac{\ell^2}{2\varepsilon_\psi c_g},\qquad
\Lambda=\frac{3\varepsilon_\psi}{\ell^2}
\quad(c_g\ne0).
\]

Každé konstantní \(c_t\) dává při pevných \(c_g,\ell,\varepsilon_\psi\)
přesně stejné objemové Eulerovy formy, a to i mimo větev s nulovou torzí.
Pokud \(c_g=0\), celá akce je lokálně topologická a neposkytuje rovnici
vybírající Einsteinovu geometrii.

Lokální klasická GR tedy nevyžaduje důkaz nepřítomnosti negradovaného
koeficientu. Vyžaduje nenulový gradovaný koeficient a již uvedené
variační předpoklady. Úplná rozšířená symetrie působící na konstantní
skalární vložky podle C1 připouští pouze lokálně topologický směr.
Odvození potřebné redukce symetrie z UBT zůstává nezbytné.
Samotná existence \(\Gamma_*\) nevynucuje nenulovost jeho koeficientu.

Tento závěr zužuje cíl výběru. Neurčuje délkovou škálu ani Newtonovu
vazbu a neopravňuje k zavedení nové fundamentální akce.

<!-- BILINGUAL-UNIT: curvature-equivalence.splitjet -->
## Použití na existující jetovou konstrukci jediného pole

Použijme existující Lorentzovsky reálný reprezentant \(X\) a existující
oboustrannou spinovou reprezentaci s Lorentzovou jetovou korekcí \(K\)
a centrální relativní korekcí \(w\):

\[
E^a=c_0^{-1}
\left(dX^a+\omega^a{}_bX^b+K^a{}_bX^b+wX^a\right),\qquad
c_0=\sqrt{\mathcal N_0},\qquad K_{ab}=-K_{ba}.
\]

V maticovém zápisu jsou strany násobení explicitně

\[
\widehat D X=dX+A^JX-XB^J,\qquad
A^J=\Omega+\mathcal K+\tfrac12wI_2,\qquad
B^J=-\Omega^\dagger-\mathcal K^\dagger-\tfrac12wI_2.
\]

Zde \(\Omega\) a \(\mathcal K\) jsou zavedená spinová zvednutí
\(\omega\) a \(K\).

Nezávislými variačními proměnnými jsou \(X,\omega,K,w\); fyzikální křivost
používá \(\omega\). Předpokládejme \(X\ne0\), nedegenerovaný koreper a množinu
nulové normy tvořenou regulární nadplochou nebo prázdnou množinou.
Vyžadujme, aby tyto sektory akce neměly další explicitní závislost na
reprezentantu ani jetových proměnných mimo zobrazený koreper.

Na doplňku nulové normy variace jetových proměnných dosáhne každého směru
koreperu. Jejich rovnice proto vynutí úplnou Eulerovu formu koreperu.
Hladkost rozšíří její nulovost přes kompatibilní nulovou nadplochu.
Indukovaná část variace fyzikální konexe přes koreper pak zmizí
a zbude úplná nezávislá rovnice konexe. Plyne i rovnice reprezentantu.
Opačný směr vyplývá z řetězového pravidla.
Jde o stejný přesný argument jako ve
[větě o hladkém Palatiniho pokračování](split_jet_null_continuation.cs.md).

H1 a C3 se tedy přenášejí na tuto zvolenou jetovou akci na uvedených
oblastech. Konstantní topologické členy u C3 argument nemění.
Lokální zvednutí Einsteinových konfigurací existují na dostatečně malých
oblastech s nenulovou normou díky zavedené pravé inverzi.
Zvednutí přes zadaný nulový přechod nadále vyžadují jeho hladkou
podmínku kompatibility.

Zobrazení zapomínající jetové reprezentanty je lokálně surjektivní,
ale není bijekcí pouze po kvocientu stabilizátorem při pevném \(X\).
Stále mohou existovat různí reprezentanti téhož koreperu.
Netvrdí se globální zvednutí ani úplná kvantová ekvivalence.

<!-- BILINGUAL-UNIT: curvature-equivalence.verification -->
## Ověření a zbývající mezera

Spusťte `tools/verify_curvature_channel_equivalence.py`; záznam je v
`reports/curvature_channel_equivalence_2026_09_08.json`.
Jeho devět skupin pokrývá přesnou bivektorovou inverzi; determinant
úplného torzního zobrazení; překážku proměnného koeficientu; Bianchiho
zrušení; Lorentzův a rozšířený komutant; všechny gradované a negradované
bloky stop; porovnání koeficientů; nezávislé souřadnicové výpočty křivosti
v jiné Diracově reprezentaci; a nezávislá řešení torze se zdrojem.
Verze SymPy a NumPy, hashe zdrojů i rozsah kontrol jsou zaznamenány.

Hladké variační argumenty, transgrese a pokračování jsou analytické.
Konečné vzorkování je nedokazuje. Formální status je `LEAN-PENDING`:
v prověřeném prostředí chybí Lean i Lake a není dodána zkompilovaná formalizace.

**VAKUOVÁ EKVIVALENCE KONSTANTNÍ REÁLNÉ PALATINIHO--HOLSTOVY RODINY: PROVED [L1].**

**KONSTANTNÍ NEGRADOVANÁ ROZŠÍŘENÁ STOPA: NULOVÁ LOKÁLNÍ OBJEMOVÁ VARIACE [L1].**

**PŮVOD NENULOVÉHO GRAVITAČNÍHO KANÁLU V UBT, NORMALIZACE,
ÚPLNÉ SEKTORY A RH: OPEN.**

Kanonický registr tvrzení se nemění. Jednoznačná fundamentální akce může
stále vyžadovat výběr koeficientů, i když je klasické objemové rovnice
nedokážou rozlišit.
