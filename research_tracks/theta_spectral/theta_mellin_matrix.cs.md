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
**Status:** klasické Mellinovy identity a tříkanálový no-go výsledek jsou zavedeny; rozšířené jádro odvozené z UBT zůstává otevřené.

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
\vartheta_3,qquad \vartheta_2+\vartheta_4,qquad \vartheta_2-\vartheta_4,
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

Následující experiment má přidat theta charakteristiky a spočítat hodnost výsledné rodiny po vytknutí známých dokončených \(L\)-funkcí. Zvýšení hodnosti se matematicky očekává; otázkou UBT je, zda kanonická dynamika vybere netriviální kombinaci s vlastností pozitivity.
