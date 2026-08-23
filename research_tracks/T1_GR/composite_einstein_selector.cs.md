<!-- BILINGUAL-UNIT: composite-selector.provenance -->
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

# Kompozitní Einsteinův selector: rozhodovací kandidát kanonického jádra

<!-- BILINGUAL-UNIT: composite-selector.definition -->
## Kandidát

Zachovejme uzamčenou kovariantní tetrádu a na každém regulárním patchi
s hodností deset definujme

\[
S_{\rm comp}[\Theta]
=c\int d^4x\,\sqrt{-g[\Theta]}\,(R[g[\Theta]]-2\Lambda),
\qquad c\ne0.
\]

Po provedení kompozice neobsahuje žádné nezávislé metrické pole:
$g[\Theta]$ je centrální Gramova metrika kovariantní tetrády. Jako
dynamický selector je nesurjektivní, protože jeho stacionární konfigurace
musí splňovat metrické Eulerovy--Lagrangeovy rovnice; nejde o již odmítnutou
surjektivní split-jet vazbu.

<!-- BILINGUAL-UNIT: composite-selector.variation -->
## Přesný variační most

Nechť $J=d g_\Theta$ je diferenciál z přípustných variací $\Theta$ do
symetrických variací metriky a $\mathcal E_g$ je metrický
Eulerův--Lagrangeův kovektor Einsteinova--Hilbertova funkcionálu. První
variace kompozitní akce je

\[
\delta S_{\rm comp}[\Theta]=c\,\mathcal E_g(J\,\delta\Theta).
\]

Kanonická věta o hodnosti zobrazení tetrády na metriku zajišťuje na každé
nedegenerované tetrádě surjektivitu do deseti metrických směrů. Stacionarita
pro každou přípustnou $\delta\Theta$ proto implikuje $\mathcal E_g=0$. Pro
$c\ne0$ jde o Einsteinovu--$\Lambda$ rovnici. Lean věta
`metricEquationOfCompositeStationarity` kernelově kontroluje přesnou implikaci
ze surjektivního pullbacku a `nonzeroCoefficientPreservesEquation` kontroluje
odstranění nenulového celkového koeficientu.

Tento argument je lokální a předpokládá, že již dokázané algebraické
zobrazení hodnosti deset se rozšíří na deklarovaný prostor přípustných
variací s požadovanými okrajovými podmínkami. Neprovádí výpočet nelineárního
kompozitního Hessianu.

<!-- BILINGUAL-UNIT: composite-selector.decision -->
## Rozhodovací hranice

Po přijetí kandidát uzavírá **klasický kompozitní variační most**;
neodvozuje vlastní přijetí. Difeomorfismová kovariance, lokální Lorentzova
symetrie, lokalita se dvěma derivacemi a absence dalších lehkých geometrických
polí omezují infračervený metrický funkcionál na Einsteinův--$\Lambda$ tvar
až na koeficienty, ale současné kinematické axiomy připouštějí $c=0$ i
$c\ne0$.

Nepodmíněný status `CLOSED` proto vyžaduje jeden ze dvou poctivých vstupů:

1. povýšit nenulový kompozitní Einsteinův funkcionál na kanonický dynamický
   axiom; nebo
2. odvodit jej ze samostatně dokončené mikroskopické míry/Hessianu.

Bez jednoho z nich by změna statusu byla kruhová. I po volbě 1 zůstávají
kvantová predikce $G$, vázaný Hessian/míra a fyzická stabilita $\psi$-sektoru
samostatnými otázkami UV dokončení, pokud rozsah `CLOSED` není výslovně
omezen na klasickou lokální obnovu GR.
