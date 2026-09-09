<!-- BILINGUAL-UNIT: biquat-induced.provenance -->
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

# Biquaternionová tetrádová cesta k indukované gravitaci

<!-- BILINGUAL-UNIT: biquat-induced.scope -->
## Oprava rozsahu

Tento audit zachovává zmrazenou architekturu UBT:

\[
\Theta\in\mathbb C\otimes\mathbb H,\qquad
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta,\qquad
\frac12(E_\mu^\sharp E_\nu+E_\nu^\sharp E_\mu)
=g_{\mu\nu}\mathbf1.
\]

Geometrickým mostem je kovariantní tetráda. Nezavádíme nezávislou tetrádu,
spinorovou náhradu za `Theta` ani dodatečný fyzický geometrický sektor. Periodický směr `psi` se níže používá pouze za výslovného předpokladu o
spektrálním oboru, který již uvádí výpočet indukované gravitace; nedefinuje ani
neprůměruje kanonickou metriku.

Otázkou je, zda kvantové fluktuace téhož biquaternionového pole mohou indukovat
Einsteinův člen a jeho koeficient.

<!-- BILINGUAL-UNIT: biquat-induced.questions -->
## Dva logicky odlišné gravitační vstupy

V eukleidovské efektivní metrické teorii uvažujme
\[
S_{\rm EH}[g]=-\frac1{16\pi G}\int d^4x\sqrt g\,R.
\]
Jsou zde dvě samostatné otázky: proč je tento člen přítomen a jaký má
renormalizovaný koeficient. Při neomezených variacích metriky s kompaktním
nosičem přijetí této akce s libovolným nenulovým konstantním koeficientem dává
vakuovou Einsteinovu rovnici; velikost koeficientu se vykrátí. S hmotou se
stává pozorovatelnou jako `G`. Toto tvrzení předpokládá efektivní metrický
variační princip. Nedokazuje, že variace kompozitní metriky prostřednictvím
`Theta` realizují všechny tyto variace. Kosmologický člen také potřebuje
vlastní odvození nebo vstup.

Dosazení změřeného `G` tedy doplňuje konkrétní efektivní gravitační akci.
Nedodává chybějící mikroskopickou akci ani nedokazuje její variační redukci
z biquaternionových axiomů.

<!-- BILINGUAL-UNIT: biquat-induced.formula -->
## Podmíněný Sacharovův koeficient

Předpokládejme hladké čtyřrozměrné eukleidovské pozadí bez hranice,
dobře definovanou bosonickou Gaussovu míru a skalární Laplaceovy operátory
\[
P_{j,n}=-\nabla^2+m_j^2+\frac{n^2}{R_\psi^2}+\xi_jR,
\qquad n\in\mathbb Z,\qquad m_j^2\geq0.
\]
Periodické módy, jejich násobnosti, konstantní hmotnosti a vazby na křivost
jsou zde předpoklady. Jakýkoli další endomorfismus, kalibrační nebo ghostový
operátor je nutné odvodit a zahrnout před použitím tohoto skalárního vzorce.
Má-li úplný determinant nulové módy, použijme vhodný infračervený předpis.

Lokální rozvoj tepelného jádra a předpis vlastního času dávají
\[
\operatorname{Tr}e^{-sP_j}\sim
\frac{e^{-m_j^2s}\vartheta_3(0,e^{-s/R_\psi^2})}{(4\pi s)^2}
\int\sqrt g\,\bigl[1+s(1/6-\xi_j)R+\cdots\bigr],
\qquad
\Gamma_1=-\frac12\sum_j\int_{M_{\rm UV}^{-2}}^\infty
\frac{ds}{s}\operatorname{Tr}e^{-sP_j}.
\]
Vynechané členy zahrnují vyšší mocniny křivosti a derivace.
Definujme
\[
\mathcal I_1(M_{\rm UV},R_\psi,m)
:=\int_{M_{\rm UV}^{-2}}^\infty ds\,s^{-2}e^{-m^2s}
\vartheta_3(0,e^{-s/R_\psi^2}).
\]
Porovnání lokálního členu lineárního v křivosti se zobrazenou Einsteinovou
akcí dává
\[
\Gamma_{1,R}=-\frac1{192\pi^2}
\sum_j(1-6\xi_j)\mathcal I_1\int\sqrt g\,R,
\qquad
\boxed{\frac1{G_{\rm ind}}=
\frac1{12\pi}\sum_j(1-6\xi_j)\mathcal I_1(M_{\rm UV},R_\psi,m_j).}
\]
Tím je určen koeficient v uvedeném lokálním rozvoji a regulačním předpisu.
Nejde o exaktní úplný determinant při libovolné křivosti, kontrolu jeho
infračervené části ani odvození fluktuačního operátoru UBT.

Pro \(M_{\rm UV}R_\psi=1\) a \(m_j=0\) platí
\[
C_\psi:=\int_1^\infty\frac{du}{u^2}\vartheta_3(0,e^{-u})
=1.303410251859279308\ldots,
\]
\[
\boxed{\frac1{G_{\rm ind}}=
\frac{C_\psi M_{\rm UV}^2}{12\pi}N_{\rm ind},
\qquad N_{\rm ind}:=\sum_j(1-6\xi_j).}
\]
Pro nezávislé vyhodnocení dovoluje pozitivita integraci po členech
(Tonelliho věta); jedna integrace per partes dává
\[
C_\psi=1+2\sum_{n=1}^\infty
\bigl[e^{-n^2}-n^2 E_1(n^2)\bigr],
\qquad E_1(z)=\int_z^\infty\frac{e^{-t}}t\,dt.
\]
Zbytek po \(N\) členech splňuje
\[
0<r_N\leq
\frac{2e^{-(N+1)^2}}{(N+1)^2[1-e^{-(2N+3)}]}.
\]
Každý vynechaný integrál je totiž omezen výrazem \(e^{-n^2}/n^2\) a sousední
čtverce se liší alespoň o \(2N+3\). To kontroluje useknutí řady;
numerická integrace v pohyblivé řádové čárce má ještě vlastní chybu.

Totožné konformně vázané skalární módy, \(\xi_j=1/6\), přispívají k tomuto
Einsteinovu koeficientu nulou. V nehmotném případě se společným poloměrem
vyžaduje kladný indukovaný Newtonův koeficient \(N_{\rm ind}>0\).
Ostatní sektory vyžadují vlastní koeficienty tepelného jádra.

<!-- BILINGUAL-UNIT: biquat-induced.count -->
## Rozměr biquaternionu ještě není počtem fyzických módů

Pišme

\[
X=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad
H(X)=2\operatorname{Re}(a\bar d)-|b|^2-|c|^2.
\]

V reálných souřadnicích má kvadratický tvar invariantní vůči souvislé symetrii
signaturu

\[
\boxed{\operatorname{sig}_{\mathbb R}H=(2,6).}
\]

Na kanonickém Lorentzově reálném podprostoru

\[
X=i x^0I-i x^k\sigma_k,\qquad x^a\in\mathbb R,
\]

se omezuje na

\[
\boxed{H(X)=2\left[(x^0)^2-(x^1)^2-(x^2)^2-(x^3)^2\right],}
\]

se signaturou \((1,3)\). Ani „osm reálných souřadnic jednoho
biquaternionu“, ani „čtyři Lorentzovy reálné souřadnice“ proto samy o sobě
nejsou počtem zdravých eukleidovských bosonických módů. Fyzický počet vyžaduje
určit vazby, kalibrační směry, statistiku a přípustnou eukleidovskou konturu.

Definujme \(\bar M_{\rm Pl}^2=(8\pi G_{\rm ind})^{-1}\) v jednotkách
\(\hbar=c=1\). Pouze pro orientaci dávají dvě naivní dosazení s minimální
vazbou v předchozím nehmotném bodě se shodnými škálami

\[
\left.\frac{\bar M_{\rm Pl}}{M_{\rm UV}}\right|_{N_{\rm ind}=8}
=0.1049059378244545\ldots,
\qquad
\left.\frac{\bar M_{\rm Pl}}{M_{\rm UV}}\right|_{N_{\rm ind}=4}
=0.0741797000224061\ldots.
\]

Faktor \(\sqrt2\) mezi nimi již stačí k důkazu, že prosté počítání komponent
nelze mlčky použít jako predikci `G`.

<!-- BILINGUAL-UNIT: biquat-induced.locked -->
## Úplná variace objemu pro pevnou konexi

Uzamčení metriky dává exaktní čtyřrozměrnou identitu
\[
\frac12\sqrt{|g|}\,g^{\mu\nu}
\langle D_\mu\Theta,D_\nu\Theta\rangle_\sharp
=2\mathcal N_0\sqrt{|g|}.
\]
Párování zde označuje centrální koeficient antikomutátoru s involucí sharp.
Involuce \(\sharp\) je kvaternionové sdružení (maticová adjugovaná matice),
nikoli komplexní sdružení. Položme \(c_0=\sqrt{\mathcal N_0}>0\).

**Lemma B-VAR [L1].** Pracujme na orientovaném souřadnicovém plátu s hladkým
Lorentzovým reálným polem a pevnou hladkou Lorentzovou konexí \(C\):
\[
\Theta=b_aX^a,\quad X^a\in\mathbb R,\quad
b_0=iI,\quad b_k=-i\sigma_k,\quad
\eta=\operatorname{diag}(-1,1,1,1),\quad
C^T\eta+\eta C=0.
\]
Oboustranné působení je
\[
D_\mu\Theta=\partial_\mu\Theta+A_\mu\Theta-\Theta B_\mu,
\qquad A_\mu=\Omega_\mu,\quad B_\mu=-\Omega_\mu^\dagger,
\]
kde \(\Omega\) reprezentuje \(C\) na těchto biquaternionech. Proto
\[
E^a=c_0^{-1}(dX^a+C^a{}_bX^b),\quad
F=dC+C\wedge C,\quad DE^a=c_0^{-1}F^a{}_bX^b.
\]
Pro variaci zafixujme lokální rámec; \(C\) je předepsaná konexe, nikoli další
variované pole. Předpokládejme hladké \(X,C\), \(\det E>0\) a hladké variace
\(u,v\) s kompaktním nosičem, dostatečně malé pro zachování nedegenerovanosti.
Čtyři reálné komponenty jsou omezením téhož `Theta`, nikoli náhradním polem.
Definujme
\[
J[X]=\int\operatorname{vol}_E,\qquad
\operatorname{vol}_E=\frac1{4!}\epsilon_{abcd}
E^a\wedge E^b\wedge E^c\wedge E^d,\qquad \epsilon_{0123}=1.
\]
Potom Eulerova čtyřforma a její úplná linearizace jsou
\[
\boxed{\delta J[v]=\int v^a\mathcal A_a,\qquad
\mathcal A_a=-\frac1{2c_0^2}\epsilon_{abcd}
(F^b{}_eX^e)\wedge E^c\wedge E^d,}
\]
\[
\boxed{(\mathcal L v)_a=
-\frac1{2c_0^2}\epsilon_{abcd}(F^b{}_ev^e)\wedge E^c\wedge E^d
-\frac1{c_0^3}\epsilon_{abcd}(F^b{}_eX^e)\wedge Dv^c\wedge E^d.}
\]
Zejména
\[
\delta^2J[u,v]=\int u^a(\mathcal L v)_a
=\delta^2J[v,u].
\]

**Důkaz.** Variace determinantu dává
\[
\delta J[v]=\frac1{6c_0}\int\epsilon_{abcd}
Dv^a\wedge E^b\wedge E^c\wedge E^d.
\]
Protože \(D\epsilon=0\), vnější derivace výrazu
\(\epsilon_{abcd}v^a E^b\wedge E^c\wedge E^d\) je zobrazený integrand bez
prefaktoru plus
\(3\epsilon_{abcd}v^a DE^b\wedge E^c\wedge E^d\).
Její integrál díky kompaktnímu nosiči mizí. Dosazení
\(DE=c_0^{-1}FX\) dokazuje první vzorec. Derivujme jej při pevných
\(C,F\) s použitím \(\delta E=c_0^{-1}Dv\). Obě variace tetrády jsou po
přejmenování antisymetrických indexů stejné, což dává zobrazené
\(\mathcal L\). Rovnost smíšených variací hladkého determinantového
funkcionálu dokazuje formální symetrii; nebyla předpokládána žádná polní rovnice.

Pro \(F=0\) mizí Eulerova forma i linearizace: lokální Piolův výsledek
o nulovém Lagrangiánu. Pro zakřivenou pevnou \(C\) může být Eulerova forma
nenulová, ale její linearizace má řád nejvýše jedna. Není tedy skalárním
Laplaceovým operátorem druhého řádu předpokládaným v předchozím výpočtu
koeficientu. Jde o výsledek pro tuto Lorentzovu reálnou omezenou akci,
nikoli o klasifikaci všech osmi reálných biquaternionových fluktuačních směrů.

<!-- BILINGUAL-UNIT: biquat-induced.value-connection -->
## Zahrnutí všech variací konexe závislé na hodnotách pole

**Lemma B-VAL [L1].** Nechť \(C_\mu=C_\mu(x,X)\) je libovolný předepsaný
hladký funkcionál Lorentzovy konexe závislý na hodnotách pole, bez derivací
\(X\). Zahrňme jeho indukovanou variaci. Pro libovolný hladký skalár
\(f(x,X)\) uvažujme
\[
S_f[X]=\int d^4x\,f(x,X)\det E,\qquad
p_\mu^a:=\partial_\mu X^a,\qquad
E_\mu^a=c_0^{-1}[p_\mu^a+C_\mu{}^a{}_b(x,X)X^b].
\]
Použijme stejné předpoklady o plátu a kompaktním nosiči jako v B-VAR. Potom
úplná Eulerova rovnice a její linearizace mají řád nejvýše jedna.

**Důkaz.** Při derivování hustoty podle prvních derivací držíme \(x,X\) pevné:
\[
\frac{\partial E_\rho^c}{\partial p_\mu^a}
=c_0^{-1}\delta_\rho^\mu\delta_a^c,\qquad
W_{ab}^{\mu\nu}:=
\frac{\partial^2(f\det E)}{\partial p_\mu^a\partial p_\nu^b}
=\frac{f}{2c_0^2}\epsilon^{\mu\nu\rho\sigma}
\epsilon_{abcd}E_\rho^cE_\sigma^d.
\]
Horní epsilon je souřadnicový permutační symbol, nikoli Lorentzův tenzor
s indexy zvednutými metrikou. Proto
\[
W_{ab}^{\mu\nu}=-W_{ab}^{\nu\mu},\qquad
W_{ab}^{\mu\nu}k_\mu k_\nu=0.
\]
Jediné druhé derivace ve výrazu
\(\partial L/\partial X^a-\partial_\mu(\partial L/\partial p_\mu^a)\)
mají koeficient \(-W_{ab}^{\mu\nu}\); komutující souřadnicové derivace je
vyruší. Všechny derivace \(C(x,X)\) a \(f(x,X)\) jsou zahrnuty ve zbývajících
členech nultého a prvního řádu. Linearizace tohoto výrazu nemůže znovu zavést
druhé derivace.

To zahrnuje algebraický potenciál násobený stejnou objemovou hustotou.
Uzavírá to možnost nápravy pouhou závislostí konexe na hodnotách pole v této
rodině. Neopravňuje to používat Eulerův vzorec pro pevnou \(C\), když se \(C\)
mění.

<!-- BILINGUAL-UNIT: biquat-induced.jet-connection -->
## Přesné zbývající řetězové pravidlo pro závislost na derivacích

Pro konkrétní hladký lokální funkcionál tetrády závislý na prvních derivacích
\(E_\alpha=E_\alpha(x,X,p)\) nechť \(\alpha\) označuje komponentu tetrády
a \(I,J\) komponenty prvních derivací. Definujme
\[
Q_\alpha=\frac{\partial\det E}{\partial E_\alpha},\quad
H_{\alpha\beta}=\frac{\partial^2\det E}
{\partial E_\alpha\partial E_\beta},\quad
J_{\alpha I}=\frac{\partial E_\alpha}{\partial p_I}.
\]
Úplný Hessián podle prvních derivací je přesně
\[
\boxed{W_{IJ}=f\left(
J_{\alpha I}H_{\alpha\beta}J_{\beta J}
+Q_\alpha\frac{\partial^2E_\alpha}{\partial p_I\partial p_J}
\right).}
\]
Jde o dvojí použití řetězového pravidla včetně druhé derivace kompozitní
tetrády. Může změnit výše uvedené zrušení; nezaručuje nenulový ani eliptický
hlavní symbol. Závisí-li konexe implicitně na \(E,\partial E\), je nejprve
nutné prokázat diferencovatelné zobrazení řešení; samotný vzorec pro první
derivace tento diferenciální problém nepokrývá. Výpočet operátoru pro
skutečně vybranou akci a konexi zůstává `GAP-10D-HESS-COMP`.

<!-- BILINGUAL-UNIT: biquat-induced.renormalization -->
## Holý člen, regulátor a současně vznikající vakuový člen

Připuštění holého Einsteinova členu dává v témže lokálním předpisu
\[
\boxed{\frac1{G_{\rm ren}}=\frac1{G_{\rm bare}}
+\frac1{12\pi}\sum_j(1-6\xi_j)\mathcal I_1(M_{\rm UV},R_\psi,m_j)
+\kappa_{\rm other,ct}.}
\]
Zde \(\kappa_{\rm other,ct}\) zahrnuje ostatní sektory a protičleny.
Čistá Sacharovova indukce proto vyžaduje důvod pro
\(G_{\rm bare}^{-1}=0\) spolu s renormalizační podmínkou.
Predikce také potřebuje odvozenou UV škálu nebo UV doplnění kontrolující
závislost na regulátoru. Položení cutoffu rovného změřené Planckově škále
by udělalo z údajné predikce `G` kruhový argument.

Tentýž rozvoj tepelného jádra vytváří objemový člen a členy vyšších mocnin
křivosti. Při pevném \(M_{\rm UV}R_\psi\) a pevných poměrech hmotností
ke cutoffu se vedoucí objemový koeficient škáluje jako \(M_{\rm UV}^4\).
Je-li naopak pevné \(R_\psi\) a \(M_{\rm UV}R_\psi\gg1\), věž módů změní
vedoucí škálování na \(R_\psi M_{\rm UV}^5\). Jeho renormalizace nebo zrušení
je součástí téhož výpočtu.

Návrh indukované gravitace viz
[Sacharov](https://www.mathnet.ru/eng/dan33444). Předpis vlastního času
a zde použité lokální koeficienty tepelného jádra jsou uvedeny v rovnicích
(1.20) a (4.26)–(4.27) práce
[Vassilevich](https://arxiv.org/abs/hep-th/0306138).

<!-- BILINGUAL-UNIT: biquat-induced.program -->
## Správný biquaternionový program pro cestu B

Nejkratší přímá cesta nyní je:

1. finalizovat jednu mikroskopickou akci původního `Theta`, jejíž tetráda je
   \(E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\);
2. spočítat její úplnou druhou variaci včetně
   \(\delta E,\delta g,\delta\Omega\) a všech vazeb;
3. určit kalibračně fixovaný fyzický/ghostový operátor a platnou eukleidovskou
   konturu, nikoli položit počet módů roven 8 pouhým pohledem;
4. vyhodnotit úplnou tepelnou superstopu a dokázat, že její Einsteinův
   koeficient je nenulový a má fyzické znaménko;
5. odvodit \(M_{\rm UV}\) ze škálových dat UBT, uvést renormalizační podmínku a
   současně řešit objemový člen;
6. teprve potom porovnat výsledný bezrozměrný poměr
   \(G\sqrt{\mathcal N_0}\) s experimentem.

Pro tyto kroky není potřeba Cliffordův spinorový nosič ani pomocný geometrický
sektor. Současná překážka předchází dlouhému numerickému součtu: úplný
biquaternionový kompozitní Hessián ještě není určen.

<!-- BILINGUAL-UNIT: biquat-induced.verification -->
## Ověření

`tools/verify_biquaternionic_induced_gravity_boundary.py` kontroluje:

- exaktní signatury \((2,6)\) a \((1,3)\);
- všech \(4^4\) komponent Hessiánu determinantu a zanikající hlavní symbol
  druhého řádu;
- kovariantní Eulerův a Jacobiho vzorec proti samostatně derivovanému
  souřadnicovému determinantu na příkladu neploché Lorentzovy konexe;
- zrušení pro konexi závislou na hodnotách pole s algebraickým prefaktorem;
- oba členy kompozitního řetězového pravidla pro první derivace na nelineárním
  příkladu;
- \(C_\psi\) numerickou integrací a nezávisle useknutou kladnou řadou,
  mez zbytku, oba podmíněné Planckovy poměry a \(\xi=1/6\).

Analytické důkazy stanovují obecná tvrzení z uvedených předpokladů.
Příklady a numerické výpočty kontrolují konvence a implementaci; tyto důkazy
nenahrazují. Doprovodný záznam je
`reports/biquaternionic_induced_gravity_boundary_2026_09_08.json` a uvádí
skutečné datum ověření, verze, hashe a omezení. Regresní kontrola prověřuje
tyto vědecké identity.

Formalizace zůstává `LEAN-PENDING`: v kontrolovaném prostředí nejsou Lean ani
Lake a není dodán žádný zkompilovaný důkaz v Leanu. Úplný kvantový Hessián,
fyzická míra a sémantická ekvivalence překladu stále vyžadují příslušná ověření.

<!-- BILINGUAL-UNIT: biquat-induced.status -->
## Stav

- B-VAR, B-VAL: `CLOSED [L1]` pro zobrazené omezené rodiny akcí.
- Řetězové pravidlo pro závislost na derivacích: `CLOSED [L1]` jako identita
  pro konkrétní lokální zobrazení prvních derivací; neplyne z něj elipticita.
- Program biquaternionové indukované gravitace: `OPEN`.
- `GAP-10D-HESS-COMP`, fyzické módy/kontura, nenulový Einsteinův koeficient,
  UV škála a renormalizace: `OPEN`.
- Úplné odvození UBT a RH: `OPEN`. Žádný kanonický status tvrzení se nepovyšuje.
