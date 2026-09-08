<!-- BILINGUAL-UNIT: selector-completion.header -->
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


# Výběr omezené větve s úplnými doménami a zbývající most k RH

**Datum:** 2026-09-08. **Status:** ANALYTIC PROOF [L1]; LEAN-PENDING.
Tento výzkumný doplněk dokončuje analytický argument o doménách mezery G1
v `psi_branch_selection.cs.md`. Přidává také elementární důkaz domény
operátoru požadovaný jako F5 v `../prime_fock_operator/gap_inventory.md`.
Ani jeden výsledek neodvozuje kanonický generátor UBT ani nedokazuje RH.
Jde o aplikace klasické spektrální teorie bez nároku na matematické prvenství.
Jejich výslovné důkazy zachováváme pro studium a verifikaci.

<!-- BILINGUAL-UNIT: selector-completion.assumptions -->
## 1. Přesné předpoklady

Nechť \(H\) je komplexní Hilbertův prostor se skalárním součinem lineárním
v prvním argumentu a \(A\) hustě definovaný nezáporný samosdružený
operátor. Nepředpokládáme diskrétní spektrum ani kladnou spektrální mezeru.

\[
A=A^*\ge0,\qquad \mathbb C_-:=\{z\in\mathbb C:\operatorname{Im}z<0\}.
\]

Nechť \(F:\mathbb C_-\to H\) je normově holomorfní a je slabým řešením
rovnice druhého řádu v následujícím přesném smyslu:

\[
\langle F''(z),h\rangle+\langle F(z),A^2h\rangle=0
\quad(h\in D(A^2),\ z\in\mathbb C_-).
\]

Požadujeme silnou hraniční hodnotu na svislé polopřímce a omezenost na ní:

\[
u=\lim_{s\downarrow0}F(-is)\in H,\qquad
M=\sup_{s>0}\|F(-is)\|_H<\infty.
\]

Parametr \(s\) je pomocná hloubka pokračování. Neztotožňujeme jej
s kanonickou kompaktní souřadnicí \(\psi\).

<!-- BILINGUAL-UNIT: selector-completion.theorem -->
## 2. Výběr omezené větve bez spektrální mezery

**Věta S1 [L1].** Za právě uvedených předpokladů platí

\[
F(z)=e^{-izA}u\quad(z\in\mathbb C_-).
\]

Obráceně tento vzorec pro každé \(u\in H\) definuje jedinou funkci
splňující předpoklady. V otevřené polorovině patří do domény každé mocniny
a splňuje silnou rovnici prvního řádu:

\[
F(z)\in\bigcap_{k\ge1}D(A^k),\qquad
iF'(z)=AF(z),\qquad
\sup_{z\in\mathbb C_-}\|F(z)\|=\|u\|.
\]

**Důkaz.** Označme \(E_A\) spektrální míru. Pro kladná celá čísla použijme
omezená spektrální okna a projekci nulového módu

\[
P_n=E_A([1/n,n]),\quad H_n=P_nH,\quad
A_n=A|_{H_n},\quad P_0=E_A(\{0\}).
\]

Slabá rovnice testovaná proti \(H_n\subset D(A^2)\) dává obyčejnou
rovnici s omezeným operátorem pro \(w_n(s)=P_nF(-is)\):

\[
w_n''(s)=A_n^2w_n(s),\qquad
w_n(s)=e^{-sA_n}a_n+e^{sA_n}b_n.
\]

Pro úplnost: tyto konstanty existují bez derivování hraniční hodnoty.
Zvolme libovolné \(s_0>0\) a položme

\[
a_n=\tfrac12e^{s_0A_n}(w_n(s_0)-A_n^{-1}w_n'(s_0)),\qquad
b_n=\tfrac12e^{-s_0A_n}(w_n(s_0)+A_n^{-1}w_n'(s_0)).
\]

Počáteční úloha s omezeným operátorem má jediné řešení. Spektrální dolní
mez a trojúhelníková nerovnost nyní dávají

\[
e^{s/n}\|b_n\|\le\|e^{sA_n}b_n\|
 \le M+\|a_n\|\qquad(s>0).
\]

Tedy \(b_n=0\). Silná hraniční limita ukazuje \(a_n=P_nu\).
V jádře je rovnice afinní:

\[
P_0F(-is)=a_0+s b_0.
\]

Stejná svislá omezenost vynutí \(b_0=0\) a hraniční limita určí
\(a_0=P_0u\). Za zdejších předpokladů nepotřebujeme další podmínku
omezenosti v reálném čase. Protože

\[
\|(I-P_0-P_n)v\|\longrightarrow0\quad(\forall v\in H),
\]

spektrální kalkulus dává \(F(-is)=e^{-sA}u\). Tento krok zahrnuje
i spojité spektrum hromadící se u nuly.

Definujme \(G(z)=e^{-izA}u\) přímo spektrálním kalkulem. Existuje pro
každé \(u\in H\) a \(z=t-is\), protože absolutní hodnota spektrálního
multiplikátoru je \(e^{-s\lambda}\). Jeho derivace lokálně ovládá mez

\[
\sup_{\lambda\ge0}\lambda^k e^{-s\lambda}
 =\left(\frac{k}{es}\right)^k\quad(k\ge1).
\]

To dokazuje normovou holomorfii, příslušnost k doménám mocnin a silné
rovnice uvnitř poloroviny. Skalární věta o jednoznačnosti, použitá po
skalárním vynásobení libovolnými vektory, rozšíří \(F=G\) ze svislé
polopřímky na celou souvislou polorovinu. Kontraktivita a silná hraniční
limita dávají uvedenou rovnost norem a dokazují i obrácený směr.

<!-- BILINGUAL-UNIT: selector-completion.boundaries -->
## 3. Hraniční regularita a co jsme nepředpokládali

Hraniční orbita je silně spojitá unitární orbita

\[
F(t)=e^{-itA}u.
\]

Pro libovolné \(u\in H\) splňuje rovnici prvního řádu v mírném smyslu.
Silná diferencovatelnost na reálné hranici vyžaduje a je ekvivalentní
\(u\in D(A)\); silná hraniční rovnice druhého řádu
vyžaduje \(u\in D(A^2)\). Vyhlazení uvnitř poloroviny neodstraňuje
tyto hraniční požadavky na doménu.

Libovolná rostoucí větev nemusí pokračování vůbec připouštět. Její přesná
doména v hloubce \(s\) je

\[
\mu_v(B):=\|E_A(B)v\|^2,\qquad
D(e^{sA})=\left\{v\in H:
 \int_{[0,\infty)}e^{2s\lambda}\,d\mu_v(\lambda)<\infty\right\}.
\]

S1 nepředpokládá, že každé vlnové řešení v reálném čase má omezené
analytické pokračování. Klasifikuje ta, která jej mají, a konstruuje
přežívající větev. Samotná holomorfie nadále připouští obě exponenciální větve.

Jde o tvrzení o omezené analytické funkci s hodnotami v Hilbertově prostoru,
nikoli o Hardyho větu o kvadratické integrovatelnosti na reálné ose.
Pro nenulové \(u\) platí

\[
\int_{\mathbb R}\|e^{-itA}e^{-sA}u\|^2\,dt=\infty.
\]

Integrand je kladná konstanta v \(t\). Označit tuto orbitu za prvek
obvyklého vektorového \(H^2(\mathbb C_-)\) by bylo chybné.

<!-- BILINGUAL-UNIT: selector-completion.period -->
## 4. Přesné omezení periodického pokračování

**Důsledek S2 [L1].** Je-li vybrané pokračování navíc periodické
v hloubce tlumení s periodou \(L>0\), pak je neseno jádrem:

\[
e^{-(s+L)A}u=e^{-sA}u\quad(s>0)
\quad\Longrightarrow\quad u\in\ker A.
\]

**Důkaz.** Spektrální norma rozdílu je

\[
\int_{[0,\infty)}e^{-2s\lambda}(1-e^{-L\lambda})^2
 \,d\mu_u(\lambda)=0.
\]

Integrand je ryze kladný pro každou kladnou spektrální hodnotu, takže
spektrální míra je nesena nulou. Obrácený směr je okamžitý.

Přímé periodické ztotožnění této hloubky tlumení s kompaktní souřadnicí
\(S^1_\psi\) tedy nemůže zachovat vybranou orbitu s nenulovou frekvencí.
To vylučuje pouze toto přímé ztotožnění za předpokladů S1. Nevylučuje
jiné vláknové konstrukce, tepelné korelační funkce ani zkroucená data.
Odvození jakékoli alternativy z UBT zůstává otevřené; její existenci
zde netvrdíme.

<!-- BILINGUAL-UNIT: selector-completion.prime -->
## 5. Prvočíselný operátor: explicitní uzávěr a doména stopy

**Věta S3 [L1].** Na Hilbertově prostoru s ortonormální bází indexovanou
kladnými celými čísly nejprve definujme

\[
H_{\rm p}|n\rangle=(\log n)|n\rangle,\qquad
D_0=\operatorname{span}_{\rm fin}\{|n\rangle:n\ge1\}.
\]

Tento operátor je podstatně samosdružený. Jeho samosdružený uzávěr má doménu

\[
D(H_{\rm p})=\left\{a\in\ell^2(\mathbb N):
 \sum_{n\ge1}(\log n)^2|a_n|^2<\infty\right\}.
\]

**Důkaz.** Testování adjungovaného operátoru proti bázovým vektorům jej
identifikuje jako násobení výrazem \(\log n\) na právě uvedené doméně.
Obráceně tato podmínka zaručí omezenost příslušného funkcionálu, čímž
dokazuje rovnost domén. Ořezávání vektoru z této domény na konečný nosič
konverguje v grafové normě, takže \(D_0\) je jádrem operátoru ve smyslu
grafové normy. Maximální operátor násobení je samosdružený; ekvivalentně
jeho rovnice defektních podprostorů dávají

\[
(\log n\mp i)a_n=0\quad\Longrightarrow\quad a_n=0\quad(\forall n).
\]

Jednoznačný prvočíselný rozklad jej identifikuje s operátorem
\(\sum_p(\log p)N_p\) v okupační bázi; neodvozuje tento operátor z UBT.
Pro komplexní parametr \(\omega\) je tepelný operátor třídy stopy právě
při \(\operatorname{Re}\omega>1\), přičemž

\[
\operatorname{Tr}(e^{-\omega H_{\rm p}})
 =\sum_{n\ge1}n^{-\omega}=\zeta(\omega),\qquad
\|e^{-\omega H_{\rm p}}\|_1=\sum_{n\ge1}n^{-\operatorname{Re}\omega}.
\]

Tato tvrzení plynou přímo z diagonálních singulárních hodnot. Analytické
pokračování skalární zeta funkce do kritického pásu tam není tepelným
operátorem třídy stopy. Tím se dokončuje analytická část F5 ve starším
přehledu, zatímco původ operátoru z UBT a interpretace nul zeta funkce
zůstávají otevřené. Starý nepárovaný přehled tímto doplňkem tiše
nepovyšujeme ani nepřepisujeme.

<!-- BILINGUAL-UNIT: selector-completion.rh -->
## 6. Co by skutečně dokazovalo RH

Klasická vazba theta–Mellin a funkcionální rovnice jsou přesné, ale
nevynucují nuly na kritické přímce. Kladný samosdružený generátor a jeho
komplexní tepelná stopa rovněž nestačí. Například

\[
A_{\rm ex}=\operatorname{diag}(0,1,1),\qquad
Z_{\rm ex}(\omega)=1+2e^{-\omega},\qquad
Z_{\rm ex}(\log2+i\pi)=0.
\]

Tento přesný protipříklad se týká navrhované implikace, nikoli Riemannovy
zeta funkce. Ukazuje, proč nelze výběr pro libovolné kladné generátory
zaměnit za identifikaci nul zeta funkce.

Jedním postačujícím spektrálním cílem by byl nezávisle zkonstruovaný
samosdružený operátor \(T\) s nenulovými diskrétními reálnými vlastními
hodnotami \(\lambda_j\), opakovanými podle násobnosti, splňující

\[
\sum_j|\lambda_j|^{-2}<\infty,
\qquad
D_T(z)=\prod_j(1-z/\lambda_j)e^{z/\lambda_j}.
\]

Součin konverguje lokálně stejnoměrně a jeho nuly jsou přesně reálné vlastní
hodnoty. Chybí přesná identita pro všechna komplexní \(z\):

\[
\xi(1/2+iz)=\xi(1/2)e^{h(z)}D_T(z),
\qquad h\in\mathcal O(\mathbb C),
\qquad
\xi(\omega)=\tfrac12\omega(\omega-1)
 \pi^{-\omega/2}\Gamma(\omega/2)\zeta(\omega).
\]

Exponenciální faktor nikdy nemizí, takže tato identita by umístila všechny
nuly \(\xi\) na kritickou přímku. Konstrukce \(T\) ze samotných nul zeta
funkce by předpokládala chybějící odpověď. Shoda konečně mnoha nul,
shoda pouze jejich hustoty ani získání tepelné stopy nejsou touto identitou.
Jde o postačující výzkumný cíl, nikoli o hotovou konstrukci a nikoli
o jedinou možnou cestu k RH.

S1 ani S3 nekonstruují \(T\) a nedokazují tuto determinantovou identitu.
Důkazy výběru větve a domény prvočíselného operátoru uzavírají mezery
v matematickém vymezení; mezera důkazu RH zůstává otevřená.

<!-- BILINGUAL-UNIT: selector-completion.verification -->
## 7. Verifikace, zdroje a hranice statusu

Spusťte `python tools/verify_null_and_spectral_gap_steps.py`. Zpráva je
`../../reports/null_and_spectral_gap_steps_2026_09_08.json`.
Přesné kontroly v SymPy pokrývají znaménka větví, konstanty skalárních oken,
sklony v jádře, periodicitu a protipříklad tepelné stopy. Nezávislá kvadratura
v SciPy testuje spojité spektrum operátoru násobení dosahující nuly;
samostatný výpočet maticové exponenciály testuje nediagonální generátory.
Konečné výpočty nedokazují S1 ani nekonečněrozměrné tvrzení o doméně v S3.

**LEAN-PENDING:** v prověřeném prostředí není nainstalovaný Lean ani Lake.
Nepředkládáme nekontrolovaný zdroj Lean jako formální důkaz. Analytické
důkazy jsou uvedeny výše; provenience zůstává `C_working`. Před sloučením
je nadále vyžadována lidská kontrola významové shody obou jazykových verzí.

Použitý spektrální kalkulus je standardní; viz Gerald Teschl,
[Mathematical Methods in Quantum Mechanics](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/).
Konvenci doplněné zeta funkce uvádí
[DLMF, reflexní vzorce](https://dlmf.nist.gov/25.4).
Úlohu RH a spektrální motivaci popisuje
[Bombieriho oficiální vymezení problému](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf).
Tyto zdroje podpírají matematický základ, nikoli tvrzení, že UBT dodala
chybějící spektrální determinant.

Výzkumná G1 má analytickou větu s úplnými doménami; její formální
verifikace G7 zůstává nedokončená. Přímá periodická interpretace má
omezený důkaz nemožnosti S2. Doménová část prvočíselné F5 má
analytický důkaz S3. Původ akce a generátoru UBT, most ke kompaktní
souřadnici, determinantová identita, `UBT-FUND-GR-ACTION: OPEN`,
`UBT-UV-G-PREDICTION: OPEN` a `UBT-FUND-GLOBAL: OPEN` se nemění.
Nepovyšujeme žádné kanonické tvrzení ani redakční potvrzení.
