<!-- BILINGUAL-UNIT: null-jet.header -->
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


# Hladké pokračování existujícího rozděleného jetu přes nulovou normu pole

**Datum:** 2026-09-08. **Status:** ANALYTIC PROOF [L1]; LEAN-PENDING.
**Rozsah:** výzkumná matematika v existující architektuře rozděleného jetu.
Jde o lokální větu o kompatibilitě předepsaných hladkých dat, nikoli o
odvození gravitační akce nebo větu o globální existenci.

<!-- BILINGUAL-UNIT: null-jet.setup -->
## 1. Data, konvence a přesná otázka

Pracujeme na hladké čtyřrozměrné oblasti s předepsanou hladkou nedegenerovanou
tetrádou, její centrální metrikou a fyzikální Levi-Civitovou konexí. Všechna
pole v této poznámce jsou hladká. Používáme existující Lorentzovsky reálný
vektorový reprezentant jediného pole; nezavádíme jiné čtení metriky:

\[
\eta=\operatorname{diag}(-1,1,1,1),\quad
X=X^a\mathbf u_a\in W_L,\quad X\ne0,\quad
c_0=\sqrt{\mathcal N_0}>0,\quad
g_{\mu\nu}=e_\mu{}^a e_\nu{}^b\eta_{ab}.
\]

Všechny kontrakce níže používají Lorentzovu formu. Korekce jetu působí ve
vektorové reprezentaci existujícího Lorentzova spinového zdvihu:

\[
\widehat D_\mu X^a=\mathring D_\mu X^a
  +K_\mu{}^a{}_bX^b+w_\mu X^a,
\qquad K_{\mu ab}=-K_{\mu ba}.
\]

V bikvaternionovém zápisu zůstávají strany násobení

\[
A^J_\mu=\mathring\Omega_\mu+\mathcal K_\mu+\tfrac12w_\mu\mathbf1,
\quad B^J_\mu=-\mathring\Omega_\mu^\ddagger-\mathcal K_\mu^\ddagger
 -\tfrac12w_\mu\mathbf1,
\quad \widehat D_\mu X=\partial_\mu X+A^J_\mu X-XB^J_\mu.
\]

Zde je \(\mathcal K\) spinový zdvih \(K\). Fyzikální křivost nadále
používá jen Levi-Civitovu konexi. Definujeme normu, nesoulad a kontrakci:

\[
\chi=X\cdot X,\qquad
Z_\mu{}^a=c_0e_\mu{}^a-\mathring D_\mu X^a,\qquad
r_\mu=X\cdot Z_\mu.
\]

Otázkou je, zda hladké konečné koeficienty jetu řeší

\[
K_\mu X+w_\mu X=Z_\mu
\]

přes \(\chi=0\). Vzorec pro nenulovou normu v souboru
`../../canonical/gr_closure/gap_10t_split_jet_right_inverse.tex`
dělí výrazem \(\chi\). Singularita tohoto konkrétního reprezentantu sama
nedokazuje singularitu všech reprezentantů.

<!-- BILINGUAL-UNIT: null-jet.divisibility -->
## 2. Přesné kritérium hladké dělitelnosti

**Věta N1 [L1].** V okolí každého bodu s \(X\ne0\) existuje hladká dvojice
\((K,w)\) právě tehdy, když je každý výraz \(r_\mu\) hladce dělitelný
výrazem \(\chi\):

\[
\exists\,w_\mu\in C^\infty:\qquad r_\mu=\chi w_\mu.
\]

**Důkaz.** Lorentzova antisymetrie dává \(X\cdot K_\mu X=0\), takže
kontrakce požadované rovnice dává nutnou podmínku dělitelnosti.
Obráceně zvolme hladký lokální vektor \(Y\) s \(X\cdot Y=1\). Taková
volba existuje u každého nenulového vektoru díky nedegenerovanosti Lorentzovy
formy; stačí jedna nenulová lokální složka. Položme

\[
U_\mu=Z_\mu-w_\mu X,\qquad
K_\mu{}^a{}_b=U_\mu{}^aY_b-Y^aU_{\mu b}.
\]

Potom

\[
X\cdot U_\mu=r_\mu-w_\mu\chi=0,\qquad
K_\mu X=U_\mu(X\cdot Y)-Y(X\cdot U_\mu)=U_\mu.
\]

Tenzor je Lorentzovsky antisymetrický a hladký a požadovaná rovnice platí.
Tím jsou dokázány oba směry. Tento reprezentant již nedělí výrazem \(\chi\),
jakmile máme hladký podíl \(w\). Různé volby \(Y\) při pevném
\(w\) se liší stabilizátorovým tenzorem, který anuluje \(X\).
Vektor \(Y\) je volba v důkazu, nikoli nové fundamentální či propagující
pole; netvrdíme, že akce určuje preferovanou volbu.

<!-- BILINGUAL-UNIT: null-jet.crossing -->
## 3. Regulární průchody nulovou normou a podmínka kompatibility tetrády

**Důsledek N2 [L1].** Předpokládejme, že \(\Sigma=\{\chi=0\}\) je
regulární nadplocha, tedy že na ní \(d\chi\ne0\). Hladké pokračování
existuje lokálně právě tehdy, když

\[
r_\mu|_\Sigma=0\quad(\forall\mu).
\]

**Důkaz.** Použijme \(\chi\) jako lokální souřadnici. Hladká funkce
mizející na její nulové nadploše má lokální rozklad

\[
r_\mu(\chi,y)=\chi\int_0^1
  (\partial_\chi r_\mu)(t\chi,y)\,dt.
\]

Ten dává hladký podíl ve větě N1. Nutnost plyne restrikcí.
Vymizení pouze v jednom bodě nestačí: podmínka platí podél lokální nadplochy.

Metrická kompatibilita dává užitečný výraz nezávislý na složkách konexe:

\[
r_\mu=c_0X_a e_\mu{}^a-\tfrac12\partial_\mu\chi.
\]

Každé hladké řešení v nenulovém vektoru pole s nulovou normou proto splňuje

\[
(\partial_\mu\chi)|_\Sigma=2c_0X_a e_\mu{}^a|_\Sigma,
\qquad
g^{\mu\nu}\partial_\mu\chi\,\partial_\nu\chi|_\Sigma=0.
\]

Tetráda je invertibilní a \(X\ne0\), takže první kovektor je nenulový.
Kompatibilní nenulový vektor s nulovou normou tedy nutně leží na regulární
nulové nadploše. Otevřená oblast s \(X\ne0\) a \(X^2\equiv0\) nemůže
splňovat úplnou jetovou relaci s nedegenerovanou tetrádou. Jde o omezení
existujícího jetu s Lorentzovým působením a dilatací, nikoli o důkaz
nemožnosti UBT jako celku. Plocha s nulovou normou pole není automaticky
horizontem černé díry.

<!-- BILINGUAL-UNIT: null-jet.rank -->
## 4. Hodnost a pomocná variace v místě průchodu

**Tvrzení N3 [L1].** Pro pevný vektor definujme

\[
L_X:\mathfrak{so}(1,3)\oplus\mathbb R\longrightarrow\mathbb R^{1,3},
\qquad L_X(K,w)=KX+wX.
\]

Jeho hodnost je

| Pole | Obraz | Hodnost |
|---|---|---|
| \(X^2\ne0\) | \(\mathbb R^{1,3}\) | 4 |
| \(X^2=0,\ X\ne0\) | \(X^\perp\) | 3 |
| \(X=0\) | \(\{0\}\) | 0 |

**Důkaz.** Výsledek pro nenulovou normu plyne z existující pravé inverze.
Pro nenulový vektor \(X\) s nulovou normou kontrakce umisťuje obraz do
\(X^\perp\). Konstrukce ve větě N1 s \(w=0\) dosahuje každého cíle
v této nadrovině. Případ nulového vektoru je okamžitý.

Algebraické rovnice multiplikátoru z existující pomocné akce jsou

\[
\lambda_a{}^\mu X^a=0,\qquad
\lambda^{\mu[a}X^{b]}=0.
\]

V samotném bodě s nenulovým vektorem nulové normy dovolují
\(\lambda_a{}^\mu=b^\mu X_a\); obvyklý bodový argument vynucující
vymizení multiplikátoru ztrácí jednu podmínku. Přesto každý spojitý
multiplikátor řešící tyto rovnice v okolí regulární nadplochy mizí i na ní:
mizí na hustém doplňku s nenulovou normou, a tedy ze spojitosti i na nadploše.
Pro hladké řešení je identicky nulový v celém okolí, takže mizí i jeho
derivace. Existující argument o odpojení pomocného sektoru se proto rozšiřuje
na tyto hladké kompatibilní průchody. Netýká se distribučních zdrojů,
singulárních polí ani kvantové míry vazeb. Následující věta se zabývá úplnou
Palatiniho variací přes hladkou nadplochu; nevychází z izolovaného bodu
s nulovou normou.

<!-- BILINGUAL-UNIT: null-jet.palatini -->
## 5. Podmíněná Palatiniho dynamika přes nulovou normu

**Věta N4 [L1].** V existujícím kandidátu s rozděleným jetem a Palatiniho akcí
nechť jsou pole hladká, kompozitní tetráda nedegenerovaná, pole nikde nemizí
a množina nulové normy je regulární nadplocha nebo prázdná. Vezměme nenulovou
Palatiniho vazebnou konstantu a pevný kosmologický koeficient. Požadujeme, aby
akce závisela na poli a jetových proměnných pouze přes kompozitní tetrádu:

\[
E^a=c_0^{-1}(dX^a+\omega^a{}_bX^b+K^a{}_bX^b+wX^a),\qquad
S_{\rm SJHP}=S_{\rm HP}[E,\omega].
\]

Fyzikální Lorentzova konexe je při variaci nezávislá. Všechny variace mají
kompaktní nosič. Stacionarita je pak ekvivalentní Palatiniho rovnicím
vyhodnoceným na kompozitní tetrádě, včetně nulové nadplochy.

**Důkaz.** Eulerovy formy tetrády a konexe zapišme jako

\[
\delta S_{\rm HP}=\int\mathcal E_a\wedge\delta E^a
 +\int\mathcal C_{ab}\wedge\delta\omega^{ab}.
\]

Mimo nulovou množinu věta N3 a libovolné jetové variace vynutí
\(\mathcal E_a=0\). Tento doplněk je hustý, takže spojitost Eulerových
forem vynutí stejnou rovnici i na nadploše. Variace fyzikální konexe je

\[
\delta_\omega S_{\rm SJHP}=\int\mathcal C_{ab}\wedge\delta\omega^{ab}
 +c_0^{-1}\int\mathcal E_a\wedge(\delta\omega^a{}_bX^b).
\]

Dává \(\mathcal C_{ab}=0\) všude. Variace pole je diferenciálním
důsledkem identicky nulové tetrádové Eulerovy formy. Obráceně, pokud obě
Palatiniho Eulerovy formy mizí, řetězové pravidlo činí každou kompozitní
variaci stacionární, aniž by používalo bodovou hodnost jetu na nulové ploše.
To dokazuje ekvivalenci rovnic pro danou hladkou konfiguraci, nikoli
existenci této konfigurace.

Pro předepsané hladké vakuové Palatiniho řešení a nikde nemizející pole
splňující N2 konstruuje věta N1 hladký zdvih přes nulovou nadplochu.
Obvyklá vakuová Cartanova rovnice bez spinu dává fyzikální Levi-Civitovu
konexi. Podmíněné lokální obnovení GR se tedy rozšiřuje přes tyto
kompatibilní hladké průchody. Palatiniho akce a její koeficienty nadále
zůstávají vstupy, nikoli odvozenou mikroskopickou dynamikou UBT.

<!-- BILINGUAL-UNIT: null-jet.fibres -->
### 5.1 Ekvivalence rovnic neztotožňuje všechny reprezentanty

Zapomenutí reprezentantu pole a jetových proměnných dává surjekci na
přípustná Palatiniho řešení. Podíl pouze podle stabilizátoru jetového tenzoru
ji neučiní injektivní, protože tento stabilizátor nemění pole.
Pro standardní plochou tetrádu, nulovou fyzikální konexi, \(c_0=1\) a nulový
kosmologický člen mají obě konstantní pole

\[
X=(1,0,0,0),\qquad \widetilde X=(2,0,0,0)
\]

pravé inverze pro nenulovou normu a dávají stejné vakuové Palatiniho řešení.
Nelze je spojit změnou pouze tenzoru anulujícího pevné pole.
Bijekce by vyžadovala podíl podle celého vlákna reprezentace; fyzikální
kalibrační interpretace celého tohoto vlákna zde není odvozena.
Dřívější diagram v `split_jet_palatii_variational_lift.cs.md` je opraven
na surjektivní zobrazení řešení.

<!-- BILINGUAL-UNIT: null-jet.examples -->
## 6. Přesné příklady a omezení

Pro standardní plochou tetrádu vezměme \(c_0=1\) a \(X^a=x^a\). Potom
\(Z=0\) a \(K=w=0\) všude. Norma pole prochází nulovým kuželem
regulárně mimo jeho vrchol; koeficienty zůstávají hladké. Ve vrcholu je
\(X=0\), takže nespadá do věty N1, ačkoli tento konkrétní afinní příklad
pokračuje i tam.

Pro standardní plochou tetrádu a konstantní vektor s nulovou normou
\(X=(1,1,0,0)\) je nesoulad \(Z_\mu=e_\mu\) a
platí \(r_0=-1\) při \(c_0=1\). Hladké koeficienty jetu nemohou řešit úplnou relaci.
Libovolné předepsané reprezentanty s nulovou normou tedy nejsou všeobecně
přípustné.

Předpoklad regularity v abstraktním důsledku o dělitelnosti je podstatný.
Hladká algebraická data

\[
X(v)=(1,1,v,0),\qquad Z(v)=(0,0,1,0),\qquad
\chi(v)=v^2,\quad r(v)=v
\]

splňují bodovou kompatibilitu při \(v=0\), ale nutný podíl je mimo nulu
\(w=1/v\). Hladké řešení přes nulu neexistuje. Jde o algebraický příklad
pro jednu složku nesouladu, nikoli o tvrzené řešení úplných rovnic pole.

<!-- BILINGUAL-UNIT: null-jet.verification -->
## 7. Verifikace a zbývající práce

Spusťte `python tools/verify_null_and_spectral_gap_steps.py`. Záznam výsledku je
`../../reports/null_and_spectral_gap_steps_2026_09_08.json`.
SymPy kontroluje přesné tenzorové identity, hodnosti a protipříklad dělitelnosti.
Nezávislá implementace v NumPy řeší úplnou lineární soustavu u nulového
kužele i na něm. Záznam uvádí verze, tolerance, rozsah a omezení.

**LEAN-PENDING:** prověřené prostředí nemá nainstalovaný Lean ani Lake;
netvrdíme existenci zkompilovaného formálního důkazu. Argumenty hladkého
rozkladu, spektra a spojitosti jsou analytické důkazy, nikoli důsledky
konečných testů. Provenience zůstává `C_working`; neměníme autorovo
potvrzení ani kanonickou úroveň.

Tím se část `UBT-FUND-GLOBAL: OPEN` týkající se pokračování přes nulovou
normu zužuje na přesné lokální kritérium. `UBT-FUND-GR-ACTION: OPEN` a
`UBT-UV-G-PREDICTION: OPEN` zůstávají. Odvození kompatibilních dat
z mikroskopické akce, pokračování v nulách pole, globální topologie,
jednoznačnost a kvantová míra jsou nadále samostatné problémy. Kanonické
přehledy statusu se nemění; tento výzkumný výsledek neuzavírá fundamentální
mezeru odvození GR.

Související práce v repozitáři:
`../../canonical/gr_closure/gap_10t_split_jet_auxiliary_completion.tex`,
`split_jet_palatii_variational_lift.cs.md` a
`../complex_time_branch_selection/bounded_selector_domain_completion.cs.md`.
