<!-- BILINGUAL-UNIT: microscopic-measure.provenance -->
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

# Mikroskopický konfigurační prostor a míra: kanonický GR sektor

<!-- BILINGUAL-UNIT: microscopic-measure.configuration -->
## Regulovaný konfigurační prostor

Pro výpočet GR interpretujme komplexní čas bez dvojího započítání:
$x^0=t$ patří do $M^4$ a $\psi$ je periodická vnitřní souřadnice. Tedy

\[
 \Theta:M^4\times S^1_\psi\longrightarrow
 \mathbb B\simeq\mathbb C^4\simeq\mathbb R^8,
 \qquad \Theta(x,\psi+2\pi R_\psi)=\Theta(x,\psi).
\]

Na konečném regulátoru s $N$ body je nevázaný prostor hodnot pole
$\mathcal C_N=(\mathbb R^8)^N$. Hladká nedegenerovaná pozadí s Lorentzovsky
reálnou tetrádou tvoří klasický GR sektor. Podmínka
$D_\mu\Theta\in W_L$ se bez dalšího neuvaluje na každou kvantovou fluktuaci;
takový krok by vyžadoval deklarovaný determinant vazeb.

<!-- BILINGUAL-UNIT: microscopic-measure.spin -->
## Jacobián spinové kalibrační transformace

Čistě gravitační spinový lift působí v maticové realizaci jako

\[
 \Theta\longmapsto S\Theta S^\dagger,
 \qquad S\in SL(2,\mathbb C).
\]

Po vektorizaci dostaneme komplexně lineární matici $\bar S\otimes S$. Její
komplexní determinant je
$\overline{\det S}^{,2}(\det S)^2=1$ a determinant její realifikace je
kvadrát modulu, tedy rovněž jedna. Regulovaná plochá míra

\[
 d\mu_{0,N}=\prod_{p=1}^{N}\prod_{A=1}^{8}d\theta_A(p)
\]

je proto invariantní vůči bodovému spinovému liftu. Přesný checker
`tools/verify_gr_microscopic_measure.py` nezávisle ověřuje netriviální
racionální/komplexní reprezentanty $SL(2,\mathbb C)$. Obecný Lean důkaz
determinantu realifikovaného Kroneckerova součinu je `LEAN-PENDING`; pro tento
determinant není tvrzen formální důkaz.

<!-- BILINGUAL-UNIT: microscopic-measure.nonuniqueness -->
## Proč ještě nejde o fyzickou funkcionální míru

Spinová invariance nevybírá jednoznačnou spojitou míru. Je-li $d\mu$
invariantní a $F[\Theta]$ je libovolný invariantní funkcionál, pak je
invariantní i $e^{-F[\Theta]}d\mu$. Difeomorfismová kovariance vyžaduje
hustotu nebo metriku prostoru polí. Přirozený DeWittův kandidát

\[
 \|\delta\Theta\|^2_\Theta=
 \int_{M^4\times S^1_\psi}\sqrt{|g[\Theta]|}\,
 \langle\delta\Theta,\delta\Theta\rangle_E
\]

již závisí na kompozitní metrice a vytváří netriviální determinant.
Současné axiomy tuto metriku prostoru polí nevybírají ani nevylučují jiné
lokální invariantní váhy. Samotná symetrie tedy odvozuje invariantní holou
regulovanou míru, nikoli vázanou fyzickou míru potřebnou k predikci
Einsteinova--Hilbertova koeficientu.

<!-- BILINGUAL-UNIT: microscopic-measure.quotient -->
## Hranice kalibračního kvocientu

V GR sektoru odpovídají lokální Lorentzovy transformace šesti jádrovým
směrům zobrazení tetrády na metriku, zatímco difeomorfismy odpovídají čtyřem
kalibračním směrům metriky. Faddeevův--Popovův operátor vyžaduje
kalibrační podmínky a infinitezimální působení na každou nezávislou
integrační proměnnou. Kanonická UBT určuje transformaci tetrády a
rekonstruované spinové konexe, ale dosud neurčuje, zda se v dráhovém integrálu
integruje pouze přes $\Theta$, přes algebraické split-jet proměnné jako
auxiliární pole, nebo přes vázaný prostor prvních jetů. Tyto formulace mají
různé Jacobiány, i když jejich klasické metriky na slupce souhlasí.

<!-- BILINGUAL-UNIT: microscopic-measure.verdict -->
## Verdikt kroků

- Krok 1, regulovaná konfigurace hodnot pole: **CLOSED pro deklarovaný
  regulátor GR auditu**.
- Krok 2, spinově invariantní holá míra: **CLOSED na konečném
  regulátoru**.
- Krok 2, spojitá vázaná fyzická míra: **OPEN**.
- Krok 3, úplný kalibrační/ghost kvocient: **OPEN**, zúženo na výběr a
  odvození jedné off-shell formulace integračních proměnných.

Zatím z toho neplyne žádná změna kanonického statusu GR.
