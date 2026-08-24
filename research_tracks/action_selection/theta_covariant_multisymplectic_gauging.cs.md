<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.provenance -->
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

# Lokální gauge kovariantizace multisymplektické rodiny Theta

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.scope -->
## Rozsah

Předchozí poznámka konstruuje nedegenerovanou reálnou symplektickou formu na
prostoru polí

\[
\omega(u,v)=\operatorname{Im}(u^\dagger Gv)
\]

z jediného kvadratického invariantu spojeného spinového a fázového působení.
Tato poznámka klade dvě ostřejší otázky:

1. lze obyčejnou derivaci v first-order pullback rodině nahradit lokální
   kovariantní derivací, aniž by se vrátily rovnice druhého jetu?;
2. lze potřebnou konexi učinit čistě pomocnou proměnnou a přitom zachovat
   nedegenerovanou čtyřrozměrnou tetrádu UBT?

Odpovědi jsou po řadě **ano** a na obecné nedegenerované větvi **ne**.

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.symplectic-connection -->
## Spojené generátory UBT jsou symplektické [L0]

Nechť `V` je podkladový osmidimenzionální reálný prostor polí a `rho_*`
realifikovaná infinitezimální reprezentace šesti spinových generátorů
`SL(2,C)` spolu s centrálním fázovým generátorem. Pro každý generátor `T`
dává exaktní maticová algebra

\[
\boxed{T^T\Omega+\Omega T=0.}
\]

Spojená reprezentace tedy leží v `Sp(V,omega)`. Ekvivalentně je lokální konexe
`A` s hodnotami v této reprezentované Lieově algebře symplektickou konexí:

\[
D\omega=0.
\]

Exaktní matice generátorů a tato podmínka jsou kontrolovány v
`tools/verify_theta_covariant_multisymplectic_gauging.py`.

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.action -->
## Gauge-kovariantní first-order rodina s pevnou konexí [L1]

Nechť

\[
D\Theta=d\Theta+\mathcal A\Theta
\]

v reprezentovaném reálném prostoru polí; stejné tvrzení platí po zabalení
dvoustranné biquaternionické konexe do její reálné lineární reprezentace.
Definujme gauge-invariantní prostorovou dvouformu

\[
Q:=\frac12\,\omega(D\Theta\wedge D\Theta)
\]

a pro libovolný invariantní reálný skalár `F(Theta)` definujme

\[
\boxed{S_F^{\rm cov}[\Theta;\mathcal A]
=\frac12\int_{M_4}F(\Theta)\,Q\wedge Q.}
\]

Při lokální reprezentované transformaci `R(x)`,

\[
\Theta\mapsto R\Theta,
\qquad
\mathcal A\mapsto R\mathcal A R^{-1}-dR\,R^{-1},
\qquad
D\Theta\mapsto R D\Theta.
\]

Protože `R` zachovává `omega` a `F` je invariantní, jsou `Q` i celá akce
lokálně gauge invariantní. Akce je také difeomorfně invariantní, protože
integruje čtyřformu a nepotřebuje žádnou pozadovou metriku časoprostoru.

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.first-order -->
## Kovariantní zrušení druhého jetu [L1]

Během variace podle `Theta` držme konexi pevnou a položme

\[
\alpha:=\omega(\delta\Theta,D\Theta),
\qquad
\mathcal R\Theta:=D^2\Theta.
\]

Symplektická kompatibilita dává exaktní identity

\[
\delta Q=d\alpha-\omega(\delta\Theta,\mathcal R\Theta),
\qquad
 dQ=\omega(\mathcal R\Theta,D\Theta).
\]

Proto modulo hraniční člen `d(F alpha wedge Q)` platí

\[
\begin{aligned}
\delta S_F^{\rm cov}
={}&\frac12\int \delta F\,Q\wedge Q
-\int dF\wedge\alpha\wedge Q\\
&+\int F\,\alpha\wedge dQ
-\int F\,\omega(\delta\Theta,\mathcal R\Theta)\wedge Q.
\end{aligned}
\]

Nezůstává žádný symetrický hlavní člen `D_mu D_nu Theta`. Jediná druhá
kovariantní derivace se objevuje přes komutátor křivosti
`D^2 Theta = mathcal R Theta`. Pro konexi, která je během této variace
nezávislá na `Theta` a jeho derivacích, je tedy Eulerova–Lagrangeova rovnice pro
`Theta` skutečně first-order v `Theta`.

Jde o lokálně gauge-kovariantní analogii double-antisymmetric kritéria Hessianu
prvního jetu. Dokazuje, že samotná lokální gauge kovariantizace first-order
zrušení **nezničí**.

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.auxiliary -->
## Rovnice čistě pomocné konexe

Tatáž akce neobsahuje derivaci `mathcal A`. Pokud se konexe v tomto sektoru
variuje nezávisle, pak

\[
\delta_{\mathcal A}D\Theta=(\delta\mathcal A)\Theta
\]

a Eulerova–Lagrangeova rovnice konexe je algebraická. Pro každý reprezentovaný
Lieův generátor `T_r` má tvar

\[
\boxed{
F\,\omega(T_r\Theta,D\Theta)\wedge Q=0.
}
\]

Konexe zavedená pouze touto akcí je tedy nepropagující, ale její algebraická
rovnice je moment-map omezení, nikoli požadovaná věta o rekonstrukci konexe
UBT.

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.no-go -->
## Obecný no-go pomocné gauge konexe pro nedegenerovanou tetrádu [L1]

Předpokládejme v bodě

\[
F(\Theta)\ne0,
\qquad
Q\wedge Q\ne0.
\]

Ve čtyřech rozměrech je dvouforma s `Q wedge Q != 0` symplektická a zobrazení

\[
\Lambda^1T^*M\longrightarrow\Lambda^3T^*M,
\qquad
\beta\longmapsto\beta\wedge Q
\]

je izomorfismus. Rovnice pomocné konexe proto implikuje

\[
\omega(T_r\Theta,D_\mu\Theta)=0
\quad\text{for every }r,\mu.
\]

Ekvivalentně

\[
\boxed{D_\mu\Theta\in(\mathfrak g\cdot\Theta)^\omega.}
\]

Exaktní klasifikace invariantů poskytuje na obecném stratu dva funkčně
nezávislé invarianty `H` a `D=|det X|^2`, takže reálný rozměr grupové orbity je
tam nejvýše šest. Exaktní racionální svědek

\[
z=(1+i,\;2+3i,\;4+5i,\;6+7i)
\]

má hodnost orbity přesně šest. Nenulový `6 x 6` minor a nezávislost `dH` a `dD`
tedy certifikují neprázdný otevřený stratum s

\[
\dim(\mathfrak g\cdot\Theta)=6.
\]

Protože `omega` je na osmidimenzionálním prostoru polí nedegenerovaná,

\[
\boxed{\dim(\mathfrak g\cdot\Theta)^\omega=8-6=2.}
\]

Všechny čtyři kovariantní derivace `D_mu Theta` tedy leží ve stejném nejvýše
dvourozměrném podprostoru pole. Na klasickém Lorentzově řezu

\[
E_\mu=\mathcal N_0^{-1/2}D_\mu\Theta\in W_L,
\]

takže čtyři tetrádové vektory rozpínají nejvýše dvě dimenze. Proto

\[
\boxed{\operatorname{rank}e\le2,\qquad\det e=0.}
\]

Nedegenerovaná Lorentzova metrika je na této obecné větvi
`F != 0`, `Q wedge Q != 0` nemožná.

Proto:

**KOVARIANTNÍ MULTISYMPLEKTICKÁ AKCE S ÚPLNOU SPIN+PHASE KONEXÍ
VARIOVANOU JAKO ČISTĚ POMOCNOU PROMĚNNOU NEMŮŽE PODPOROVAT OBECNOU
NEDEGENEROVANOU TETRÁDU UBT.**

Jde o no-go pro čistě pomocnou implementaci tohoto konkrétního sektoru konexe,
nikoli pro každé možné doplnění konexe v UBT.

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.fork -->
## Důsledek: větev konexe je nyní přesně rozdělená

Výsledky ponechávají tři logicky odlišné cesty:

1. **Pevná/externí symplektická konexe:** lokální gauge invariance a first-order
   rovnice `Theta` jsou exaktní, ale to není přijatelné jako finální dynamika
   UBT jediného pole, protože geometrie by byla dodána zvenčí.
2. **Čistě pomocná úplná spin+phase konexe:** konexe nepropaguje, ale její
   moment-map rovnice zkolabuje obecnou hodnost tetrády a je vyloučena výše
   uvedenou větou.
3. **Kompozitní nebo rozšířená dynamika konexe:** fyzická konexe UBT musí být
   místo toho rekonstruována z `Theta`/tetrády/torze nebo musí mít další
   akční strukturu, jejíž rovnice konexe není čistým moment-map omezením.
   Eliminace kompozitní konexe Levi–Civitova typu obecně zavádí derivace
   tetrády, a tedy vyšší jety `Theta`; výše uvedenou first-order větu po této
   substituci nelze prostě znovu použít.

Tím se problém výběru akce výrazně posouvá. Dalším životaschopným cílem je
**Theta-only vyšší-jet/kompozitní dokončení, nebo akce konexe, jejíž dodatečná
struktura je sama odvozena z UBT a jejíž eliminace reprodukuje kanonickou konexi
bez kolapsu hodnosti**.

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.verification -->
## Ověření

`tools/verify_theta_covariant_multisymplectic_gauging.py` exaktně kontroluje:

- pseudo-unitární zachování hermitovské formy všemi sedmi spojenými spin+phase
  generátory;
- symplektické zachování `T^T Omega + Omega T = 0`;
- funkční nezávislost `H` a `|det X|^2` v exaktním svědkovi;
- exaktní hodnost šest obecného strata orbity;
- exaktní hodnost šest matice moment-map omezení a její dvourozměrné jádro.

Tvrzení z exterior kalkulu, čtyřrozměrný wedge izomorfismus a kovariantní
variace jsou analytické. Formalizace v Leanu je `LEAN-PENDING`.

<!-- BILINGUAL-UNIT: theta-covariant-multisymplectic.status -->
## Stav

**LOKÁLNÍ GAUGE KOVARIANTIZACE S PEVNOU SYMPLEKTICKOU KONEXÍ:
PROVED [L1].**

**ČISTĚ POMOCNÉ ÚPLNÉ SPIN+PHASE GAUGING NA OBECNÉ NEDEGENEROVANÉ VĚTVI:
CLOSED AS NO-GO [L1].**

**KOMPOZITNÍ/VYŠŠÍ-JET DOKONČENÍ KONEXE A NEPODMÍNĚNÉ GR:
OPEN.**
