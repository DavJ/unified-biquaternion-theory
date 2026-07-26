# Kovariantní geometrie UBT pro studenty

## 1. Čistá struktura

Základním objektem zůstává jediné biquaternionické pole

\[
\Theta(q,\tau),\qquad \tau=t+i\psi.
\]

Lokální geometrie se nevytváří mapou do pomocného prostoru, projekcí ani
průměrem přes „fiber“. V klasickém sektoru se vezmou čtyři kovariantní derivace

\[
E_\mu:=\frac{1}{\sqrt{\mathcal N_0}}D_\mu\Theta,
\qquad \mu=0,1,2,3.
\]

Tyto čtyři biquaterniony fungují jako tetráda: jeden lokální časový směr a tři
prostorová pravítka.

Čistá lokální struktura UBT je

\[
\boxed{
\Theta
\longrightarrow
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta
\longrightarrow
\begin{cases}
\tfrac12\{E_\mu,E_\nu\}_\sharp=g_{\mu\nu}\mathbf1,\\[2mm]
\tfrac12[E_\mu,E_\nu]_\sharp=\Sigma_{\mu\nu},\\[2mm]
[D_\mu,D_\nu]=\mathcal R_{\mu\nu}.
\end{cases}}
\]

Antikomutátor dává metriku, algebraický komutátor dává bivektorovou/spinovou
část a komutátor kovariantních derivací dává křivost konexe.

## 2. Od obyčejné derivace ke kovariantní derivaci

Obyčejná parciální derivace

\[
\partial_\mu\Theta=\frac{\partial\Theta}{\partial x^\mu}
\]

měří změnu složek pole v pevně zvolené bázi. Lokální biquaternionická nebo
Lorentzova báze se ale může při pohybu prostorem otáčet či boostovat. Změna
složek pak obsahuje dva efekty:

1. skutečnou změnu pole;
2. změnu báze, ve které pole zapisujeme.

Kovariantní derivace opravuje druhý efekt. Schematicky

\[
D_\mu\Theta=\partial_\mu\Theta+\rho_*(\Omega_\mu)\Theta.
\]

\(\Omega_\mu\) je **konexe**: pravidlo, jak porovnávat lokální báze v sousedních
bodech. Symbol \(\rho_*\) říká, v jaké reprezentaci a z které strany konexe
působí. U biquaternionů nejsou levé, pravé a oboustranné násobení totéž.

## 3. Souvislost s Christoffelovými symboly

Christoffelovy symboly

\[
\Gamma^\rho{}_{\mu\nu}
\]

transportují souřadnicové indexy časoprostoru. Lorentzova konexe
\(\omega_\mu{}^a{}_b\) transportuje lokální tetrádovou bázi a
\(\Omega_\mu\) je její spinová nebo biquaternionická reprezentace.

Spojuje je tetrádová kompatibilita

\[
\partial_\mu e_\nu{}^a
-\Gamma^\rho{}_{\mu\nu}e_\rho{}^a
+\omega_\mu{}^a{}_b e_\nu{}^b=0.
\]

Takže \(\Gamma\) a \(\Omega\) nejsou stejné objekty ani neplatí
\(\Gamma=\operatorname{Re}\Omega\). Jsou to dva zápisy stejného geometrického
transportu:

- \(\Gamma\) v souřadnicové bázi;
- \(\omega\), resp. \(\Omega\), v lokální Lorentzově/biquaternionické bázi.

## 4. Je \(\Omega_\mu\) další volné pole?

### 4.1 Torsion-free klasická GR větev

V běžné klasické GR požadujeme:

1. metrickou kompatibilitu;
2. nulovou torzi.

Pak je Lorentzova konexe určena tetrádou jednoznačně:

\[
\boxed{
\mathring\omega_\mu{}^a{}_b
=e_b{}^\nu
\left(
\mathring\Gamma^\rho{}_{\mu\nu}(g)e_\rho{}^a
-\partial_\mu e_\nu{}^a
\right).}
\]

Kroužek připomíná, že jde o Levi-Civitovu, tedy torsion-free konexi.
V této větvi \(\Omega_\mu\) není nové nezávislé fyzikální pole. Je vypočtena z
tetrády podobně, jako se Christoffelovy symboly vypočítají z metriky.

### 4.2 Torze a kontorze

Torze je dvouforma

\[
T^a=de^a+\omega^a{}_b\wedge e^b.
\]

Obecná metrická konexe se rozloží na

\[
\boxed{\omega=\mathring\omega(e)+K(T),}
\]

kde \(K\) je kontorze. Při konvenci výše platí ve frame indexech

\[
\boxed{
K_{abc}=\frac12\left(T_{cab}-T_{abc}-T_{bca}\right).}
\]

To je důležitý posun: **po zadání tetrády a torze je i obecná metrická konexe
jednoznačná**. Nezůstává žádná libovolná „omega navíc“.

Otevřená otázka plné UBT tedy zní jinak:

> Vynutí UBT akce ve vakuu \(T=0\), nebo určí nenulovou torzi ze spinu či jiné
> biquaternionické struktury?

Jinými slovy, otevřená je dynamika torze, nikoli kinematická rekonstrukce
konexe.

## 5. Plochý vesmír a explicitní speciálně-relativistické řešení

V plochém Minkowského prostoru lze v inerciálních kartézských souřadnicích
zvolit

\[
\Gamma^\rho{}_{\mu\nu}=0,\qquad
\Omega_\mu=0,\qquad
D_\mu=\partial_\mu.
\]

Nyní lze napsat přímo jedno pole, které generuje Minkowského tetrádu:

\[
\boxed{
\Theta_{\mathrm{SR}}(x)
=\Theta_0+\sqrt{\mathcal N_0}
\left(i x^0\mathbf1+x^k\mathbf e_k\right).}
\]

Potom

\[
\frac1{\sqrt{\mathcal N_0}}\partial_0\Theta_{\mathrm{SR}}
=i\mathbf1,
\qquad
\frac1{\sqrt{\mathcal N_0}}\partial_k\Theta_{\mathrm{SR}}
=\mathbf e_k.
\]

Antikomutátor těchto čtyř směrů dává

\[
g_{\mu\nu}=\operatorname{diag}(-1,1,1,1).
\]

Navíc jsou všechny druhé derivace nulové. V běžné ploché vakuové větvi proto
\(\Theta_{\mathrm{SR}}\) řeší i homogenní druhý řád master rovnice. Tím je
speciální relativita v UBT nejen předpokládaná, ale má explicitní jedno-polové
reprezentující řešení.

V polárních nebo zrychlených souřadnicích mohou být \(\Gamma\) a \(\Omega\)
nenulové, i když je prostor stále plochý. Fyzikálně rozhoduje křivost, ne
samotná hodnota koeficientů konexe.

## 6. Metrika z antikomutátoru bez projekce

Označme quaternionovou konjugaci symbolem \(\sharp\). V klasickém Lorentzově
řezu má tetráda tvar

\[
E_\mu=i e_\mu{}^0\mathbf1+e_\mu{}^k\mathbf e_k,
\qquad e_\mu{}^a\in\mathbb R.
\]

Pak platí čistá algebraická identita

\[
\boxed{
\frac12\left(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu\right)
=g_{\mu\nu}\mathbf1.}
\]

\(\mathbf1\) je jednotkový biquaternion. Celý antikomutátor už je reálný skalár
násobený jednotkou, takže se nic netrasuje, neprůměruje ani neprojektuje.

Po rozvinutí

\[
g_{\mu\nu}=e_\mu{}^a e_\nu{}^b\eta_{ab},
\qquad \eta_{ab}=\operatorname{diag}(-1,1,1,1).
\]

Časové minus vznikne z \(i^2=-1\).

## 7. Co dělají komutátory

Je nutné rozlišit tři objekty:

\[
\{E_\mu,E_\nu\}_\sharp
\longrightarrow \text{metrika},
\]

\[
[E_\mu,E_\nu]_\sharp
\longrightarrow \text{lokální bivektor, orientace a spin},
\]

\[
[D_\mu,D_\nu]
\longrightarrow \text{křivost konexe nebo gauge field strength}.
\]

Pro jednu konexi působící zleva je

\[
\mathcal R_{\mu\nu}
=\partial_\mu\Omega_\nu-\partial_\nu\Omega_\mu
+[\Omega_\mu,\Omega_\nu].
\]

V plochém sektoru je \(\mathcal R_{\mu\nu}=0\).

## 8. Rankový problém

Metrika má deset nezávislých komponent. Samotná hodnota \(\Theta\) má osm
reálných komponent, ale to je chybný objekt pro počítání ranku. Metriku určují
čtyři biquaternionické tetrády \(E_\mu\), tedy reálná matice \(e_\mu{}^a\) se
šestnácti komponentami.

Šest změn tetrády jsou lokální rotace a boosty, které metriku nemění:

\[
16-6=10.
\]

Pro libovolnou malou symetrickou změnu metriky \(h_{\mu\nu}\) lze zvolit

\[
\delta e_\mu{}^a=\frac12h_{\mu\rho}e^{\rho a},
\]

což dává \(\delta g_{\mu\nu}=h_{\mu\nu}\). Lokální tetrádová mapa má tedy plný
rank deset.

### 8.1 Metodologické poučení z rankové odbočky

Dřívější rankový no-go nebyl početně chybný. Platí pro jinou formulaci, v níž
se metrika chápe jako indukovaná embeddingová bilineární forma a Einsteinovy
rovnice se mají získat pouze z normálových variací jedné sekce. V takovém rámci
je normálový prostor příliš malý.

Chyba vznikla až při přenosu tohoto výsledku na tetrádovou architekturu. Z
pravdivé věty

> jednosekční embeddingová variace nemá dost normálových směrů

neplyne

> čtyři kovariantní derivace \(D_\mu\Theta\) nemohou tvořit tetrádu.

Fiberové módy tedy opravovaly překážku vytvořenou zvolenou formulací, nikoli
vlastnost původní UBT intuice. Fiberová cesta zůstává matematicky konzistentní,
ale má slabou selektivitu: velký prostor reprezentantů umí zapsat mnoho metrik,
aniž vysvětlí, proč dynamika vybere právě jednu.

Obecné pravidlo pro další práci proto zní:

> Než překážku opravíme přidáním polí, módů, projekcí nebo rozměrů, musíme
> nejprve ověřit, zda překážka není artefaktem formulace.

## 9. Integrabilita: proč nestačí libovolně přidat konexi

Tetráda není v UBT nezávislá:

\[
E_\mu=\frac1{\sqrt{\mathcal N_0}}D_\mu\Theta.
\]

Pokud se \(\Omega[E]\) vypočítá z tetrády, dostáváme samokonzistentní rovnici

\[
E_\mu=\frac1{\sqrt{\mathcal N_0}}
\left(\partial_\mu\Theta+\rho_*(\Omega_\mu[E])\Theta\right).
\]

Neznámé \(E\) je na obou stranách. To je implicitní nelineární diferenciální
rovnice nebo fixed-point problém. Jednoznačné určení \(\Omega\) ještě samo
nezaručuje, že řešení \(E,\Theta\) existuje.

### 9.1 Proč jednoduché působení pouze zleva selhává

Uvažujme

\[
D_\mu^L\Theta=\partial_\mu\Theta+A_\mu\Theta.
\]

Pak

\[
[D_\mu^L,D_\nu^L]\Theta=F^L_{\mu\nu}\Theta.
\]

V torsion-free kompatibilní tetrádové větvi musí antisymetrická kovariantní
derivace tetrády zmizet. Dostaneme proto

\[
F^L_{\mu\nu}\Theta=0.
\]

Je-li \(\Theta\) invertibilní, násobení \(\Theta^{-1}\) dává

\[
F^L_{\mu\nu}=0.
\]

Taková jednoduchá jednostranná reprezentace by tedy genericky dovolila jen
plochou konexi. Je to formální no-go pro obecnou zakřivenou GR větev.

### 9.2 Přirozená oboustranná biquaternionická derivace

Biquaterniony mohou přirozeně působit zleva i zprava. Minimální obecný tvar je

\[
\boxed{
D_\mu\Theta
=\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu.}
\]

Komutátor dává přesnou identitu

\[
\boxed{
[D_\mu,D_\nu]\Theta
=F^A_{\mu\nu}\Theta-\Theta F^B_{\mu\nu}.}
\]

Integrabilita pak nevyžaduje nulovou křivost, ale

\[
F^A_{\mu\nu}\Theta=\Theta F^B_{\mu\nu}.
\]

Pro invertibilní \(\Theta\)

\[
\boxed{
F^A_{\mu\nu}
=\Theta F^B_{\mu\nu}\Theta^{-1}.}
\]

Levá a pravá křivost mohou být nenulové; \(\Theta\) mezi nimi funguje jako
propojovací neboli intertwining objekt. Oboustranná derivace tedy odstraňuje
jednostranné plochostní no-go, ale ještě sama nedokazuje existenci řešení pro
každou zakřivenou metriku.

### 9.3 Jsou \(A_\mu\) a \(B_\mu\) nová pole?

Nemusejí být. Požadavek, aby derivace zachovávala Lorentzův řez a jeho metriku,
vynutí v nejúspornější větvi

\[
\boxed{A_\mu=\Omega_\mu,\qquad B_\mu=-\Omega_\mu^\ddagger,}
\]

až na společný centrální člen, který se mezi levým a pravým násobením přesně
zruší. V této větvi tedy \(A\) a \(B\) nejsou dva nové fyzikální objekty, ale
dvě reprezentace jediné spinové konexe.

Tato úsporná volba má však v **beztorzní** větvi překvapivě silný
důsledek. Jestliže je \(K=0\) a jedno pole \(\Theta\) generuje
nedegenerovanou tetrádu, existuje vektor \(V\) takový, že

\[
\boxed{\mathring\nabla_\mu V^\nu=\delta_\mu{}^\nu.}
\]

Metrika by tedy musela připouštět vlastní homotetrii
\(\mathcal L_Vg=2g\). Nenulový Schwarzschildův vakuový exteriér tuto
podmínku nesplňuje. To je přesné no-go pro beztorzní větev; nezávisí na tom,
zda v přírodě existuje ideálně nerotující černá díra, protože stejná metrika
popisuje i vakuový exteriér sférického tělesa.

Tím však není vyloučena stejná jediná spinová konexe s pomocnou kontorzí.
Na malém okolí lze zvolit nenulovou Gaussovu souřadnici \(\rho\), pro niž
\(g^{-1}(d\rho,d\rho)=\varepsilon=\pm1\), a položit

\[
V^\mu=\varepsilon\rho\nabla^\mu\rho,
\qquad
W_{\mu\nu}=g_{\mu\nu}-\mathring\nabla_\mu V_\nu,
\]

\[
\boxed{
K_{\nu\mu\rho}
=\frac{W_{\mu\nu}V_\rho-V_\nu W_{\mu\rho}}{V^2}.}
\]

Tato kontorze je metrická a splňuje
\(\nabla^{(\mathring\Gamma+K)}_\mu V^\nu=\delta_\mu{}^\nu\). Pro

\[
\Theta=\sqrt{\mathcal N_0}\,V^a\mathbf u_a
\]

pak přesně vyjde \(D_\mu\Theta=\sqrt{\mathcal N_0}E_\mu\). Každá hladká
Lorentzova tetráda tedy má lokální jedno-\(\Theta\) representer se složenou
kontorzí a bez dvou nezávislých polí \(A,B\).

Relativní větev

\[
A_\mu=\Omega_\mu+P_\mu,\qquad
B_\mu=-\Omega_\mu^\ddagger+Q_\mu
\]

proto není nutná pro lokální kinematickou existenci. Zůstává možnou cestou,
pokud chceme zachovat beztorzní fyzikální konexi. Pak ale člen
\(P_\mu X-XQ_\mu\) musí být odvozen z kanonické akce jako složená nebo pomocná
veličina a nesmí přidávat propagující stupně volnosti. Společná centrální
konstanta ani konstantní člen potenciálu beztorzní překážku neodstraní, protože
v derivaci zaniká.

## 10. Co se podařilo uzavřít na dynamické úrovni

### 10.1 Minimální Palatiniho větev a torze

Jestliže v nízkoenergetické klasické větvi vezmeme tetrádu a Lorentzovu
konexi jako nezávislé proměnné, minimální první řád obsahuje Hilbertův--
Palatiniho člen. Variace podle konexe dává Cartanovu rovnici

\[
\epsilon_{abcd}\,T^a\wedge e^b=\kappa\tau_{cd}.
\]

Má 24 rovnic pro 24 komponent torze. Pro nedegenerovanou tetrádu má tato
lineární mapa přesně rank 24. Proto:

- nulový spinový proud \(\tau_{cd}=0\) jednoznačně dává \(T=0\);
- zadaný spinový proud jednoznačně určí torzi a kontorzi;
- torze v této minimální větvi není propagující pole, ale pomocná algebraická
  veličina.

To neznamená, že už jsme z fundamentální UBT odvodili právě tuto akci. Uzavřeli
jsme však otázku, co se s torzí stane, **pokud** UBT v klasickém limitu vybere
minimální Palatiniho větev.

### 10.2 Zachování Lorentzova řezu

Lorentzův reálný řez lze popsat bez ruční projekce jako množinu pevných bodů
antilineární involuce

\[
\mathcal JX=-\overline{X^\sharp}.
\]

Pokud jsou rovnice, zdroje a počáteční data invariantní vůči \(\mathcal J\) a
Cauchyho úloha má jediné řešení, pak se řešení z Lorentzova řezu nemůže dostat:
\(\mathcal J U\) by totiž bylo druhé řešení se stejnými daty. Jednoznačnost je
proto vynutí ztotožnit.

Toto je přesný podmíněný teorém. Zbývá ověřit, že finální kanonická UBT rovnice
má požadovanou ekvivarianci a dobře položenou evoluci.

### 10.3 Stabilita metriky podél imaginárního času

Jestliže změna tetrády podél \(\psi\) je pouze lokální Lorentzova rotace nebo
boost,

\[
\partial_\psi e_\mu{}^a=\Lambda_\psi{}^a{}_b e_\mu{}^b,
\qquad \Lambda_{\psi ab}=-\Lambda_{\psi ba},
\]

pak

\[
\partial_\psi g_{\mu\nu}=0.
\]

Metrika se tedy může jevit jako nezávislá na \(\psi\), i když samotná tetráda
po \(\psi\) běží po Lorentzově gauge orbitě. Druhá dostatečná možnost je
\(\psi\)-translačně invariantní jednoznačná dynamika s počátečními daty
nezávislými na \(\psi\). Otevřené zůstává, který mechanismus skutečně vybere
kanonická UBT a zda existují fyzikální nestabilní negaugeové módy.

### 10.4 Zakřivená integrabilita jako holonomie

Pro **zadané** \(E_\mu,A_\mu,B_\mu\) je rovnice

\[
\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu
=\sqrt{\mathcal N_0}\,E_\mu
\]

lineární nehomogenní systém pro \(\Theta\). Přidáním konstantní komponenty lze
zapsat \(Y=(\Theta,1)^T\) a celou rovnici chápat jako paralelní transport v
rozšířeném prostoru. Jednohodnotné řešení se zadanou počáteční hodnotou existuje
právě tehdy, když rozšířená holonomie tuto počáteční hodnotu zachovává.

To uzavírá lokální/globální kriterium pro předepsané koeficienty. Neuzavírá to
samokonzistentní UBT problém, protože v něm \(E,A,B\) samy závisejí na
\(\Theta\), torzi a akci.

### 10.5 Proč je Einsteinova dynamika nyní zúžená

Minimální Palatiniho akce s nulovým spinovým proudem dává Einsteinovy rovnice s
kosmologickou konstantou. Navíc Lovelockova věta říká, že ve čtyřech rozměrech
je za standardních podmínek -- lokálnost, obecná kovariance, identická
bezdivergentnost, nejvýše druhé derivace metriky a žádná další lehká geometrická
pole -- jediným možným metrickým tenzorem

\[
aG_{\mu\nu}+b g_{\mu\nu}.
\]

Einstein--\(\Lambda\) je tedy jednoznačný **podmíněný nízkoenergetický cíl**.
Hlavní otevřený krok už není „která rovnice by mohla vyjít“, ale proč
fundamentální UBT splňuje právě tyto nízkoenergetické předpoklady a jak určí
\(\kappa\), \(\Lambda\) a hmotový sektor.

## 11. Implicitní versus transcendentní rovnice

Tyto dva pojmy nejsou úplně stejné, i když z praktického pohledu oba znamenají,
že se neznámá nedá snadno izolovat.

**Implicitní** říká, že neznámá je schovaná na obou stranách:

\[
E=\mathcal F(E,\Theta).
\]

**Transcendentní** říká, že rovnice obsahuje nealgebraické funkce, například
exponenciálu, logaritmus nebo Jacobiho theta funkci:

\[
E=e^{-E}.
\]

UBT rovnice pro tetrádu je už sama o sobě implicitní a diferenciální. Pokud je
\(\Theta(q,\tau)\) současně Jacobiho theta funkcí nebo jinou transcendentní
strukturou, může být celý konkrétní systém zároveň implicitní **i**
transcendentní.

Nejpřesnější popis je tedy:

> UBT tetráda, pole a konexe tvoří implicitní nelineární PDE/fixed-point systém;
> při Jacobi-theta realizaci může být tento systém navíc transcendentní.

## 12. Derivace versus variace

Derivace \(D_\mu\Theta\) popisuje změnu jedné konfigurace v časoprostoru.
Variace porovnává sousední možné konfigurace:

\[
\Theta_\varepsilon=\Theta+\varepsilon\delta\Theta.
\]

Variace je nutná k odvození Eulerových–Lagrangeových rovnic z akce. Není to
náhrada za prostorovou nebo časovou derivaci.

## 13. Co je nyní dokázané a co zůstává otevřené

### Uzavřené nebo podmíněně uzavřené

1. Centrální antikomutátor dává Lorentzovu metriku bez projekce.
2. Lokální tetrádová mapa má rank deset a šest Lorentzových gauge směrů.
3. `GAP-10Omega-KIN/GR`: zadaná tetráda a torze určují konexi; bez torze jde o
   Levi-Civitovu spinovou konexi.
4. `GAP-10T-PALATINI` **podmíněně**: minimální Cartanova rovnice má rank 24/24;
   nulový nebo zadaný spinový proud jednoznačně určí torzi.
5. `GAP-10L-CONN` a `GAP-10L-SYM` **podmíněně**: kompatibilní transport a
   jedinečná ekvivariantní evoluce zachovávají Lorentzův řez.
6. `GAP-10I-SR`: Minkowského/konstantní tetráda má explicitní afinní
   \(\Theta\)-representer.
7. `GAP-10I-1S`: jednoduchá jednostranná invertibilní větev je pro obecnou
   torsion-free křivost uzavřena jako no-go.
8. `GAP-10I-PAIR-KIN`: čistá Lorentzova dvojice se redukuje na jedinou
   spinovou konexi, takže \(A,B\) nejsou dvě nová gravitační pole.
9. `GAP-10I-PAIR-GR`: beztorzní větev je uzavřena jako no-go, protože
   vynucuje konkurenční vektor a vylučuje nenulový Schwarzschildův vakuový
   exteriér.
10. `GAP-10I-TORSION-LOCAL`: každá hladká Lorentzova tetráda má lokální
    jedno-\(\Theta\) representer s explicitní složenou metrickou kontorzí.
11. `GAP-10I-PRESCRIBED`: pro zadané \((E,A,B)\) platí přesné holonomické
    kritérium existence a jednohodnotnosti.
12. `GAP-10D-PALATINI/UNIQUENESS` **podmíněně**: minimální první řád a
    Lovelockovy předpoklady vedou jednoznačně k Einstein--\(Lambda\).
13. `GAP-10psi-KIN/SYM`: Lorentzova gauge evoluce nebo translační symetrie
    chrání klasickou metriku za přesně uvedených podmínek.

### Zúžené, ale ne úplně uzavřené

1. `GAP-10T-SPIN` je podmíněně uzavřen pro přímou variaci efektivní
   Palatiniho větve při pevném tetrádu, metrice, míře a poli $\Theta$.
   `GAP-10T-FLAT-NOGO` a `GAP-10T-PAIRING-NOGO` jsou uzavřené jako no-go:
   minimální afinní beztorzní větev nefunguje a žádná nenulová nedegenerovaná
   symetrická Lorentzovsky invariantní bilineární forma tento problém
   neodstraní. `GAP-10T-DYN` zůstává zúžen na úplnou kompozitní variaci
   $\Theta$ a odvození ne-minimálního torzního rušení nebo translační/relativní
   bimodulové kompletace bez nových propagujících polí.
2. `GAP-10I-CURVED`: lokální kinematika je uzavřena. Zbývá z kanonické
   akce vybrat a fyzikálně omezit složenou torzní větev, případně odvodit
   pomocnou beztorzní relativní větev, a dokázat regularitu a globální
   pokračování. `GAP-10I-2S` už není nutný pro lokální existenci, ale zůstává
   volitelnou beztorzní cestou.
3. `GAP-10L-DYN`: ověřit ekvivarianci a dobře položenou jednoznačnost finálních
   UBT rovnic.
4. `GAP-10D`: odvodit nízkoenergetické Palatiniho/Lovelockovy předpoklady,
   \(\kappa\), \(\Lambda\) a hmotový sektor z kanonické akce.
5. `GAP-10psi`: určit, který stabilizační mechanismus vybere UBT, a vyloučit
   fyzikální nestabilní negaugeové módy.

### Stále otevřené mosty

1. `GAP-B-MASTER`: perturbativní most z původní UBT master rovnice.
2. `GAP-U2Theta`: dynamický výběr plné Schwarzschildovy tetrády a lapse.
3. Následné on-shell větve Kerr, FRW a gravitační vlny v téže kanonické
   dynamice.

Dřívější fiberová konstrukce zůstává matematicky konzistentní historickou
alternativou, ale není součástí minimální kanonické struktury UBT kvůli slabé
selektivitě a velké redundanci representerů.
