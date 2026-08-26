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

<a id="tmm-additive-residues"></a>
## 11. Aditivní reziduální kanály a konečná Weilova reprezentace

Pro \(r\in\mathbb Z/5\mathbb Z\) definujme

\[
\Theta_r(t)=
\sum_{n\equiv r\ (\mathrm{mod}\ 5)}
e^{-\pi n^2t/5},
\qquad t>0.
\]

Poissonova sumace dává vektorovou transformaci

\[
\mathbf\Theta(t)=t^{-1/2}\mathcal S\mathbf\Theta(1/t),
\qquad
\mathcal S_{rs}=\frac1{\sqrt5}e^{2\pi i rs/5}.
\]

Pro holomorfní verzi působí posun o dvě modulární jednotky vztahem

\[
\Theta_r(\tau+2)=e^{2\pi i r^2/5}\Theta_r(\tau),
\qquad
\mathcal T=\operatorname{diag}
\left(e^{2\pi i r^2/5}\right)_{r=0}^{4}.
\]

Nechť \(\mathcal P\) obrací rezidua, \((\mathcal Pv)_r=v_{-r}\). Přímý výpočet dává

\[
\mathcal S^\dagger\mathcal S=I,
\qquad
\mathcal S^2=\mathcal P,
\qquad
\mathcal S^4=I,
\qquad
[\mathcal T,\mathcal P]=0.
\]

Úplný prostor koeficientů se rozkládá na sektory parity reziduí

\[
\mathbb C^5=V_+\oplus V_-,
\qquad
\dim V_+=3,
\qquad
\dim V_-=2,
\qquad
\Pi_\pm=\frac12(I\pm\mathcal P).
\]

Vyřešení úplných rovnic komutantu

\[
[G,\mathcal S]=[G,\mathcal T]=0
\]

dává

\[
G=a\Pi_+ + b\Pi_-.
\]

Pro hermitovské \(G\) jsou koeficienty \(a,b\) reálné a pozitivita vyžaduje \(a,b>0\). Úplná pětirozměrná reprezentace má tedy dvě nezávislé invariantní váhy.

Skalární theta konstanty však splňují

\[
\Theta_r(t)=\Theta_{-r}(t).
\]

Obsazují proto pouze

\[
V_+=\operatorname{span}
\left\{e_0,\frac{e_1+e_4}{\sqrt2},
\frac{e_2+e_3}{\sqrt2}\right\}.
\]

Omezený komutant \(\mathcal S\) a \(\mathcal T\) na tomto třírozměrném sektoru má dimenzi jedna. Jeho invariantní hermitovská metrika je tudíž

\[
G_+=aI_3.
\]

Dva liché kanály při \(z=0\) chybějí; lze je dodat derivacemi podle eliptické proměnné, analogicky k chybějícímu skalárnímu kanálu \(\vartheta_1\).

Hlavní funkce zeta je nyní skutečně obsažena v aditivním systému, protože

\[
\frac12\sum_{r=0}^{4}
\left(\Theta_r(t)-\delta_{r0}\right)
=\sum_{n=1}^{\infty}e^{-\pi n^2t/5},
\]

a tedy pro \(\Re s>1\)

\[
\frac12\int_0^\infty t^{s/2-1}
\sum_{r=0}^{4}\left(\Theta_r(t)-\delta_{r0}\right)dt
=\left(\frac5\pi\right)^{s/2}
\Gamma\!\left(\frac s2\right)\zeta(s).
\]

**Věta TMM-5.** Aditivní reziduální reprezentace skutečně směšuje nulovou reziduální třídu se čtyřmi nenulovými třídami. Modulární invariance určuje metriku skalárního sudého sektoru jednoznačně až na celkovou škálu. Kanál zeta je však lineárním funkcionálem tří theta složek, zatímco pozitivita \(aI_3\) kontroluje jejich současné anulování. Nevyplývá z ní proto, že nuly tohoto lineárního funkcionálu leží na \(\Re s=1/2\).

Tento experiment poskytuje kanonické modulární směšování a skalární metriku na realizovaném sektoru, nikoli však spektrální operátor síly RH. Zbývající chybějící složkou je samoadjungovaný operátor odvozený z UBT, jehož determinant nebo význačný vlastní kanál se rovná dokončené funkci zeta.

| Podmínka | Status |
|---|---|
| Fourierova transformace pěti reziduí | **[PROVED]** |
| úplný komutant \(a\Pi_++b\Pi_-\) | **[PROVED]** |
| skalární metrika na realizovaném sudém sektoru | **[PROVED]** |
| aditivní systém obsahuje Mellinův kanál zeta | **[PROVED]** |
| pozitivita určuje polohu nul tohoto lineárního kanálu | **[DISPROVED]** |
| samoadjungovaný operátor zeta odvozený z UBT | **[OPEN]** |

<a id="tmm-elliptic-derivatives"></a>
## 12. Eliptické derivace a lichý sektor

Zaveďme eliptická reziduální jádra

\[
\Theta_r(z,\tau)=
\sum_{n\equiv r\ (\mathrm{mod}\ 5)}
\exp\!\left(\frac{\pi i\tau n^2}{5}
+\frac{2\pi i n z}{5}\right)
\]

a jejich první derivace v \(z=0\), normalizované jako

\[
\Phi_r(t)=
\frac5{2\pi i}
\left.\frac{\partial}{\partial z}\Theta_r(z,it)\right|_{z=0}
=\sum_{n\equiv r\ (\mathrm{mod}\ 5)}
n e^{-\pi n^2t/5}.
\]

Mají lichou paritu reziduí,

\[
\Phi_0(t)=0,
\qquad
\Phi_{-r}(t)=-\Phi_r(t),
\qquad
\sum_{r=0}^{4}\Phi_r(t)=0.
\]

Vektor derivací tedy leží v

\[
V_-=\operatorname{span}
\left\{\frac{e_1-e_4}{\sqrt2},
\frac{e_2-e_3}{\sqrt2}\right\}.
\]

Derivování Poissonovy transformace nebo přímá transformace váženého Gaussova jádra dává

\[
\mathbf\Phi(t)
=-i\,t^{-3/2}\mathcal S\mathbf\Phi(1/t).
\]

Mocnina se mění z \(t^{-1/2}\) na \(t^{-3/2}\): sektor derivací má modulární váhu vyšší o jedna. Posun o dvě stále působí prostřednictvím \(\mathcal T\).

Omezený komutant na \(V_-\) má dimenzi jedna, takže jeho invariantní hermitovská metrika je

\[
G_-=bI_2.
\]

Úplná metrika skalárních a derivovaných kanálů je proto

\[
G=aI_3\oplus bI_2
=a\Pi_+ + b\Pi_-.
\]

Mohlo by se zdát, že derivace vynutí \(a=b\). Nevynutí. Vyřešení všech rovnic pro konstantní intertwiner

\[
Q\mathcal S_+=(-i\mathcal S_-)Q,
\qquad
Q\mathcal T_+=\mathcal T_-Q,
\qquad
Q:V_+\longrightarrow V_-
\]

dává pouze

\[
Q=0.
\]

To odpovídá rozdílným dimenzím a modulárním vahám obou ireducibilních sektorů. Derivace propojuje podkladové funkce, není však konstantním endomorfismem konečné reprezentace koeficientů.

**Věta TMM-6.** První eliptické derivace realizují dva chybějící liché reziduální kanály a dávají jim skalární invariantní metriku. Sdružená Jacobiho data zachovávají dvě nezávislé pozitivní škály \(a,b\); modulární kovariance neposkytuje nenulový konstantní intertwiner ze sudého do lichého sektoru, a proto nevynucuje \(a=b\).

Sudé/liché rozdělení lze použít jako pečlivě omezenou bosonickou/fermionickou analogii: skalární theta hodnoty jsou sudé a derivované kanály liché, přičemž v druhých nastává párové rušení. Nejde o odvození fyzikálních částic, spinové statistiky ani stavů částice-antičástice. Taková interpretace by vyžadovala gradovaný Hilbertův prostor odvozený z UBT a operátor Diracova typu nebo supernáboj měnící váhu.

| Podmínka | Status |
|---|---|
| lichá derivovaná jádra a jejich Poissonův zákon | **[PROVED]** |
| skalární invariantní metrika \(bI_2\) | **[PROVED]** |
| nenulový konstantní modulární intertwiner \(V_+\to V_-\) | **[DISPROVED]** |
| modulární kovariance vynucuje \(a=b\) | **[DISPROVED]** |
| Diracova nebo supernábojová vazba odvozená z UBT | **[OPEN]** |
| interpretace fyzikálních fermionů | **[OPEN]** |
