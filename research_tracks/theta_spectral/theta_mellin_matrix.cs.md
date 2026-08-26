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

# Společná Mellinova analýza Jacobiho theta sektorů

**Datum:** 2026-08-25  
**Status:** klasické Mellinovy identity, tříkanálový no-go výsledek a rozšíření hodnosti čtyři s charakteristikami modulo \(5\) jsou zavedeny; vazba odvozená z UBT zůstává otevřená.

<a id="tmm-question"></a>
## 1. Otázka

Mohou současné Mellinovy transformace všech čtyř Jacobiho theta sektorů uložit netriviálním nulám Riemannovy zeta funkce novou podmínku nad rámec funkcionální rovnice?

Pro tři nenulové theta konstanty je odpověď záporná: jejich skalární Mellinovy kanály obsahují pouze jeden stupeň volnosti zeta. Výsledek přesně ukazuje, kde musí vstoupit skutečně nová informace.

<a id="tmm-definitions"></a>
## 2. Theta jádra

Pro \(t>0\) použijme

\[
\vartheta_2(it)=\sum_{n\in\mathbb Z}e^{-\pi(n+1/2)^2t},\qquad
\vartheta_3(it)=\sum_{n\in\mathbb Z}e^{-\pi n^2t},\qquad
\vartheta_4(it)=\sum_{n\in\mathbb Z}(-1)^n e^{-\pi n^2t}.
\]

Definujme konvergentní jádra

\[
K_2(t)=\frac{\vartheta_2(it)}2,\qquad
K_3(t)=\frac{\vartheta_3(it)-1}2,\qquad
K_4(t)=\frac{1-\vartheta_4(it)}2.
\]

Čtvrtá theta konstanta splňuje

\[
\vartheta_1(0,it)=0.
\]

V bodě \(z=0\) tedy nedává skalární Mellinův kanál. Její \(z\)-derivace je nenulová a patří do rozšířeného experimentu s modulárními formami, nikoli do následující tříkanálové věty.

<a id="tmm-transforms"></a>
## 3. Mellinovy transformace

Položme

\[
A(s)=\pi^{-s/2}\Gamma\!\left(\frac s2\right).
\]

Integrace po členech ve společné polorovině

\[
\Re s>1
\]

dává

\[
\mathcal M[K_3](s)=A(s)\zeta(s),
\]

\[
\mathcal M[K_4](s)=A(s)(1-2^{1-s})\zeta(s),
\]

\[
\mathcal M[K_2](s)=A(s)(2^s-1)\zeta(s).
\]

Ekvivalentně

\[
\mathbf M(s)
=A(s)\zeta(s)
\begin{pmatrix}
2^s-1\\[2pt]
1\\[2pt]
1-2^{1-s}
\end{pmatrix}.
\]

<a id="tmm-no-go"></a>
## 4. Věta TMM-1: hodnost a množina nul

**Věta TMM-1 (standardní důsledky, dokázané zde).** Společná skalární Mellinova data \(K_2,K_3,K_4\) mají meromorfní hodnost jedna nad společným faktorem \(A(s)\zeta(s)\). V otevřeném kritickém pásu

\[
0<\Re s<1,
\]

se všechny tři analyticky pokračované kanály anulují současně právě v netriviálních nulách

\[
\zeta(s).
\]

**Důkaz.** Předchozí faktorizace dokazuje hodnost jedna. Funkce gama nemá nuly. Nuly \(2^s-1\) leží na

\[
\Re s=0,
\]

a nuly \(1-2^{1-s}\) leží na

\[
\Re s=1.
\]

Žádný násobitel se uvnitř otevřeného pásu neanuluje. Žádný ze tří kanálů proto nepřidává nezávislou vnitřní podmínku na nuly. \(\square\)

Jde o no-go výsledek pouze pro tři skalární theta konstanty. Nevylučuje novou informaci z derivací, charakteristik, součinů, vícerozměrných theta řad ani z maticového jádra odvozeného z UBT.

<a id="tmm-modular-matrix"></a>
## 5. Modulární \(S\)-matice

Při \(t\mapsto1/t\) splňují theta konstanty

\[
\begin{pmatrix}
\vartheta_2(i/t)\\
\vartheta_3(i/t)\\
\vartheta_4(i/t)
\end{pmatrix}
=\sqrt t\,
S
\begin{pmatrix}
\vartheta_2(it)\\
\vartheta_3(it)\\
\vartheta_4(it)
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
0&0&1\\
0&1&0\\
1&0&0
\end{pmatrix},
\qquad S^2=I.
\]

Vlastní kanály jsou

\[
\vartheta_3,\qquad \vartheta_2+\vartheta_4,\qquad \vartheta_2-\vartheta_4,
\]

s vlastními čísly \(+1,+1,-1\). Modulární rozklad vysvětluje reflexní symetrii, avšak hodnost jedna skalárních Mellinových dat neumožňuje umístit všechny nuly na osu symetrie.

<a id="tmm-new-information"></a>
## 6. Kde může vstoupit nová informace

| Rozšíření | Mellinův obraz | Možný nový obsah | Nutná podmínka |
|---|---|---|---|
| charakteristiky \([a,b]\) | Hurwitzova zeta a Dirichletovy \(L(s,\chi)\) | více aritmetických kanálů | dokázat vazbu vybranou UBT, nikoli vložit charaktery ručně |
| \(\partial_z\vartheta_1(0,it)\) a theta součiny | \(L\)-funkce modulárních forem | neskalární modulární sektory | zvládnout Mellinovu konvoluci a odlišit ji od přebalení zety |
| vícerozměrné theta řady | Epsteinovy/automorfní zeta funkce | geometrie mřížky | odvodit kvadratickou formu z UBT |
| maticové jádro UBT | determinant nebo operátorová transformace | podmínka pozitivity nebo samoadjungovanosti | odvodit jádro a skalární součin z kanonické akce |

Rozhodujícím cílem není další funkcionální rovnice. Je jím nezávisle odvozená pozitivita, totální pozitivita nebo samoadjungovanost dostatečně silná k vynucení reálných spektrálních parametrů.

<a id="tmm-verification"></a>
## 7. Ověření a další experiment

Artefakt `tools/verify_theta_mellin_matrix.py` kontroluje přímky nul násobitelů, přesnou involuci \(S\)-matice a její vlastní kanály a nezávislá numerická vyčíslení tří Mellinových Dirichletových řad pro reálná \(s>1\). Regresní pokrytí je v `tests/test_theta_mellin_matrix.py`.

| Tvrzení | Status |
|---|---|
| tři Mellinovy identity | **[STD/PROVED]** |
| TMM-1: hodnost jedna a žádná nová vnitřní podmínka na nuly | **[PROVED]** |
| vlastní rozklad modulární \(S\)-matice | **[STD/PROVED]** |
| výběr rozšířeného theta jádra z UBT | **[OPEN]** |
| pozitivita nebo samoadjungovanost vynucující RH | **[OPEN]** |
| formalizace v Lean | **LEAN-PENDING** |

<a id="tmm-characteristics"></a>
## 8. Rozšíření charakteristikami modulo \(5\)

Nechť \(U_5=(\mathbb Z/5\mathbb Z)^\times\). Protože \(2\) generuje \(U_5\), zapišme každou jednotku jako \(2^j\bmod5\) a definujme

\[
\chi_k(2^j)=e^{2\pi i k j/4},\qquad k=0,1,2,3.
\]

Tabulkou charakterů je čtyřbodová diskrétní Fourierova matice

\[
C_{kj}=\chi_k(2^j),
\qquad
CC^\dagger=4I,
\qquad
\operatorname{rank}C=4.
\]

Parita je

\[
\chi_k(-1)=(-1)^k.
\]

Položme \(a_k=0\) pro sudé \(k\) a \(a_k=1\) pro liché \(k\) a definujme theta jádra charakterů

\[
\Theta_k(t)=
\sum_{n\in\mathbb Z}
\chi_k(n)n^{a_k}e^{-\pi n^2t/5}.
\]

Pro \(\Re s>1\) dává integrace po členech

\[
\frac12\int_0^\infty
t^{(s+a_k)/2-1}\Theta_k(t)\,dt
=
\left(\frac5\pi\right)^{(s+a_k)/2}
\Gamma\!\left(\frac{s+a_k}{2}\right)L(s,\chi_k).
\]

Rozšíření charakteristikami má tedy čtyři nezávislé koeficientové kanály. Hlavní kanál splňuje

\[
L(s,\chi_0)=(1-5^{-s})\zeta(s),
\]

zatímco \(\chi_1,\chi_2,\chi_3\) poskytují tři nehlavní Dirichletovy \(L\)-funkce.

**Výsledek TMM-2.** Racionální charakteristiky zvyšují konečnou hodnost kanálů charakterů z jedné na čtyři. Jde o skutečně bohatší aritmetickou informaci, avšak nulám \(\zeta\) stále neukládá novou podmínku, dokud UBT neodvodí vazbu, determinant, formu pozitivity nebo společný spektrální operátor propojující čtyři dokončené \(L\)-kanály.

Následující experiment proto musí odvodit, nikoli zvolit, matici \(G_{\mathrm{UBT}}(s)\) působící na tyto kanály a otestovat, zda

\[
\mathbf\Lambda(s)^\dagger G_{\mathrm{UBT}}(s)\mathbf\Lambda(s)
\]

má kanonickou pozitivní nebo samoadjungovanou spektrální reprezentaci.

<a id="tmm-ubt-metric"></a>
## 9. Vazebné metriky přípustné symetriemi

Zapišme čtyři dokončené kanály charakterů jako

\[
\mathbf\Lambda=(\Lambda_0,\Lambda_1,\Lambda_2,\Lambda_3)^T.
\]

Násobení generátorem \(U_5\) působí v bázi charakterů prostřednictvím

\[
D=\operatorname{diag}(1,i,-1,-i).
\]

Komplexní konjugace zaměňuje \(\chi_1\leftrightarrow\chi_3\) a ponechává \(\chi_0,\chi_2\) pevné. Položme

\[
P=
\begin{pmatrix}
1&0&0&0\\
0&0&0&1\\
0&0&1&0\\
0&1&0&0
\end{pmatrix}.
\]

Pro hermitovskou vazebnou matici \(G\) požadujme invarianci vůči fázi charakterů a kompatibilitu s antiunitární konjugací,

\[
D^\dagger G D=G,
\qquad
P^\dagger G P=\overline G.
\]

**Věta TMM-3.** Tyto podmínky jsou ekvivalentní tvaru

\[
G=\operatorname{diag}(g_0,g_1,g_2,g_1),
\qquad g_0,g_1,g_2\in\mathbb R.
\]

Forma je pozitivně definitní právě tehdy, když

\[
g_0>0,\qquad g_1>0,\qquad g_2>0.
\]

Fázová a konjugační symetrie tedy ponechávají tři nezávislé reálné váhy a nevybírají kanonickou metriku.

Pokud navíc postulujeme cyklickou symetrii kanálů

\[
X(\Lambda_0,\Lambda_1,\Lambda_2,\Lambda_3)^T
=(\Lambda_3,\Lambda_0,\Lambda_1,\Lambda_2)^T,
\qquad X^\dagger G X=G,
\]

potom

\[
G=cI.
\]

Tento silnější závěr je podmíněný, protože repozitář neodvozuje působení \(X\) na Mellinovy kanály charakterů z kanonického pole UBT.

I maximálně symetrický pozitivní kandidát dává pouze

\[
Q(s)=c\sum_{k=0}^3|\Lambda_k(s)|^2.
\]

Jeho pozitivita říká, že \(Q(s)=0\) pouze při anulování všech čtyř kanálů. RH se týká nul samotného hlavního kanálu, takže pozitivita \(Q\) jejich polohu neurčuje bez další identity vynucující současné anulování nebo bez samoadjungovaného operátoru, jehož charakteristickým determinantem je hlavní dokončený kanál zeta.

Toto omezení odpovídá auditu akce v repozitáři: reálné bikvaternionové párování, znaménko a škála nejsou dokončeny; pozitivní hermitovská veličina \(\operatorname{Tr}(X^\dagger X)\) není pro obecné pole Lorentzovsky invariantní při neunitárních boostech; a kanonická seskvilineární forma potřebná pro antiunitární obrácení času zůstává otevřená. TMM-3 je proto klasifikací přípustných kandidátů, nikoli odvozením z UBT.

| Podmínka | Status |
|---|---|
| klasifikace z fáze a konjugace | **[PROVED]** |
| skalární metrika při dodatečné cyklické symetrii | **[PROVED, CONDITIONAL ON \(X\)]** |
| odvodit symetrie kanálů z kanonické UBT | **[OPEN]** |
| sladit pozitivní metriku kanálů s Lorentzovsky invariantním párováním pole | **[OPEN]** |
| získat samoadjungovaný determinant síly RH | **[OPEN]** |

Ukotvení v repozitáři: `canonical/ACTION.en.md:50-98`, `canonical/symmetry/discrete_symmetries.tex:311-317` a `canonical/symmetry/discrete_symmetries.tex:449-454`.

<a id="tmm-functional-equations"></a>
## 10. Gaussovy součty a no-go výsledek funkcionálních rovnic

Pro tři nehlavní charaktery \(\chi_k\), \(k=1,2,3\), položme \(a_k=k\bmod2\) a

\[
\tau_k=\sum_{r=1}^{4}\chi_k(r)e^{2\pi i r/5},
\qquad
\varepsilon_k=\frac{\tau_k}{i^{a_k}\sqrt5}.
\]

Všechny tři charaktery jsou primitivní. Jejich dokončené funkce

\[
\Lambda_k(s)=
\left(\frac5\pi\right)^{(s+a_k)/2}
\Gamma\!\left(\frac{s+a_k}{2}\right)L(s,\chi_k)
\]

splňují

\[
\Lambda_k(s)=\varepsilon_k\Lambda_{4-k}(1-s).
\]

Přímý výpočet Gaussových součtů dává

\[
|\tau_k|=\sqrt5,
\qquad
\varepsilon_2=1,
\qquad
\varepsilon_3=\overline{\varepsilon_1},
\qquad
\varepsilon_1\varepsilon_3=1.
\]

Na \(\mathbf\Lambda_{\mathrm{prim}}=(\Lambda_1,\Lambda_2,\Lambda_3)^T\) má tedy funkcionální rovnice tvar

\[
\mathbf\Lambda_{\mathrm{prim}}(s)
=R\mathbf\Lambda_{\mathrm{prim}}(1-s),
\qquad
R=
\begin{pmatrix}
0&0&\varepsilon_1\\
0&1&0\\
\varepsilon_3&0&0
\end{pmatrix},
\qquad
R^\dagger R=R^2=I.
\]

Omezení metriky TMM-3 na tyto kanály je

\[
G_{\mathrm{prim}}=\operatorname{diag}(g_1,g_2,g_1).
\]

Pro všechna reálná \(g_1,g_2\), nikoli pouze pro stejná, platí

\[
R^\dagger G_{\mathrm{prim}}R=G_{\mathrm{prim}}.
\]

Funkcionální rovnice proto nepřidává žádný vztah mezi vahou lichých charakterů \(g_1\) a vahou kvadratického charakteru \(g_2\).

Hlavní charakter je odlišný. Je indukován z triviálního charakteru konduktoru jedna a

\[
L(s,\chi_0)=(1-5^{-s})\zeta(s).
\]

Je-li \(\Lambda_\zeta(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)\), jeho normalizace s konduktorem pět je

\[
\Lambda_0^{(5)}(s)
=\left(5^{s/2}-5^{-s/2}\right)\Lambda_\zeta(s).
\]

Protože \(\Lambda_\zeta(s)=\Lambda_\zeta(1-s)\), dostáváme nekonstantní násobitel

\[
\Lambda_0^{(5)}(s)
=\frac{5^{s/2}-5^{-s/2}}
{5^{(1-s)/2}-5^{-(1-s)/2}}
\Lambda_0^{(5)}(1-s).
\]

Čtyři kanály tudíž netvoří konstantní unitární \(4\times4\) reprezentaci funkcionální rovnice: tři primitivní kanály tvoří uzavřený blok, zatímco hlavní kanál zeta zůstává oddělený.

**Věta TMM-4.** Přesné Gaussovy součty modulo 5 a Dirichletovy funkcionální rovnice neredukují tříparametrickou rodinu metrik z TMM-3 a nesměšují hlavní kanál zeta s primitivními kanály. Neukládají proto žádnou další podmínku netriviálním nulám \(\zeta\).

Jde o druhý no-go výsledek, nikoli o selhání výpočtu. Jakákoli silnější vazba musí pocházet z rozšířené aditivní reprezentace theta tříd, operátoru odvozeného z UBT nebo jiné identity, která není obsažena v oddělených Dirichletových funkcionálních rovnicích.

| Podmínka | Status |
|---|---|
| primitivní Gaussovy součty a kořenová čísla | **[PROVED]** |
| unitární involuce na primitivním bloku | **[PROVED]** |
| hlavní kanál má konstantní kořenové číslo při konduktoru pět | **[DISPROVED]** |
| funkcionální rovnice vynucují \(g_1=g_2\) | **[DISPROVED]** |
| vazba s hlavním kanálem odvozená z UBT | **[OPEN]** |
