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
plochostní no-go, ale ještě sama nedokazuje existenci řešení pro každou
zakřivenou metriku.

## 10. Implicitní versus transcendentní rovnice

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

## 11. Derivace versus variace

Derivace \(D_\mu\Theta\) popisuje změnu jedné konfigurace v časoprostoru.
Variace porovnává sousední možné konfigurace:

\[
\Theta_\varepsilon=\Theta+\varepsilon\delta\Theta.
\]

Variace je nutná k odvození Eulerových–Lagrangeových rovnic z akce. Není to
náhrada za prostorovou nebo časovou derivaci.

## 12. Co je nyní dokázané a co zůstává otevřené

### Uzavřené

1. Centrální antikomutátor dává Lorentzovu metriku bez projekce.
2. Lokální tetrádová mapa má rank deset a šest Lorentzových gauge směrů.
3. `GAP-10Ω-KIN`: po zadání tetrády a torze je metrická konexe jednoznačná.
4. `GAP-10Ω-GR`: pro nulovou torzi je \(\Omega\) Levi-Civitova spinová konexe.
5. `GAP-10L-CONN`: metrická Lorentzova konexe zachovává Lorentzův řez.
6. `GAP-10I-SR`: Minkowského tetráda má explicitní reprezentující
   \(\Theta_{\mathrm{SR}}\).
7. `GAP-10I-1S`: jednoduchá jednostranná invertibilní větev je pro obecnou
   křivost uzavřena jako no-go.

### Zúžené, ale ne úplně uzavřené

1. `GAP-10I-2S`: oboustranná derivace odstraňuje plochostní no-go a převádí
   integrabilitu na vztah mezi levou a pravou křivostí.

### Otevřené

1. `GAP-10T-DYN`: odvodit torzi nebo její nulovost z UBT akce.
2. `GAP-10I-CURVED`: dokázat existenci a jednoznačnost implicitního systému pro
   obecné zakřivené tetrády.
3. `GAP-10L-DYN`: dokázat zachování Lorentzova řezu úplnou dynamikou \(\Theta\).
4. `GAP-10D`: odvodit Einsteinovu dynamiku ze stejné UBT akce.
5. `GAP-10ψ`: odvodit klasickou stabilitu podél imaginárního času.
6. Dynamicky vybrat Schwarzschildovu, Kerrovu, FRW a vlnovou větev.

Dřívější fiberová konstrukce zůstává matematickou alternativou, ale není
součástí minimální kanonické struktury UBT.
