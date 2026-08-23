<!-- BILINGUAL-UNIT: legacy-action.provenance -->
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

# Starší akce z Appendix AA jako GR selector: rozhodovací audit

<!-- BILINGUAL-UNIT: legacy-action.question -->
## Otázka a rozsah

Tato poznámka testuje, zda archivní `appendix_AA_theta_action.tex` může dodat
chybějící mikroskopickou jedno-$\Theta$ akci, míru funkcionálního integrálu
a Hessian potřebné pro nepodmíněnou obnovu GR. Zdroj je historický; je
testován, nikoli znovu aktivován. Tento audit neklasifikuje všechny možné
jedno-$\Theta$ akce.

<!-- BILINGUAL-UNIT: legacy-action.dependencies -->
## Test závislostí

Archivní funkcionál explicitně závisí na metrice $G_{\mu\nu}$, spinové
konexi $\Omega_\mu$, kalibrační konexi $A_\mu$, kalibrační křivosti
$F_{\mu\nu}$, neurčeném interakčním potenciálu a hraničním členu
s křivostí. Nedefinuje všechny tyto objekty jako funkcionály $\Theta$ ani
neprovádí variaci s řetězovým pravidlem vyžadovanou uzamčenou kompozitní
tetrádovou architekturou. Jde tedy o akci
$S[\Theta,G,\Omega,A,\ldots]$, nikoli o požadovanou dokončenou akci
$S[\Theta]$.

Pokud se její kinetická metrika místo toho sváže podmínkou
$g_{\mu\nu}[\Theta]=\mathcal N_0^{-1}\langle D_\mu\Theta,D_\nu\Theta\rangle_\sharp$,
přesná kontrakce již dokázaná v kanonickém auditu převede kinetický skalár
na $4\mathcal N_0$ (nebo $2\mathcal N_0$ se zobrazeným faktorem jedna polovina).
Stane se z něj objemový člen a neposkytne Einsteinův--Hilbertův selector.

<!-- BILINGUAL-UNIT: legacy-action.measure -->
## Test míry a párování

Zdroj deklaruje čtyři souřadnice $q^\mu\in\mathbb B$, každou s osmi reálnými
složkami, a navíc $(t,\psi)\in\mathbb R^2$, ale integruje pouze
$d^4q\,dt\,d\psi$. Deklarovaný reálný počet souřadnic je tedy
$4\cdot8+2=34$, zatímco zobrazený diferenciál má šest faktorů. Není zadána
žádná mapa, vazba, Jacobián ani indukovaná míra podvariety, které by
redukovaly 34 rozměrů na 6.

Funkcionální míra $\mathcal D\Theta$ je pouze pojmenována. Není zkonstruován
její kalibrační kvocient, Jacobián přechodu od $\Theta$ ke kompozitním
proměnným, vazby, ghosty, regularizace ani normalizace. Nemůže proto určit
počet fyzických módů ani konečný koeficient Einsteinova--Hilbertova členu.

Uvedené párování je navíc ve zapsané podobě vnitřně neslučitelné: pomocí
`Re` je deklarováno jako reálné, současně se o něm ale tvrdí, že je komplexně
seskvilineární. Pro nenulovou reálnou hodnotu $z$ vyžaduje komplexní
antilinearita při $\lambda=i$ hodnotu $-iz$, která není reálná. Jediná
hodnota splňující oba požadavky pro všechny argumenty je nula, což odporuje
pozitivní definitnosti.

<!-- BILINGUAL-UNIT: legacy-action.verification -->
## Ověření

Lean soubor `formal/lean/UBT/GR/LegacyActionObstructions.lean` kernelově
kontroluje neshodu počtu souřadnic a přesné lemma o komplexních číslech, které
je jádrem rozporu v párování. Dřívější Lean věta
`CompositeKinetic.compositeKineticCollapse` pokrývá kolaps po svázání metriky.
Tyto formální výsledky ověřují pouze zakódované překážky; nedokazují, že
nemůže fungovat jiná mikroskopická akce.

<!-- BILINGUAL-UNIT: legacy-action.verdict -->
## Verdikt a další kandidát

**ODMÍTNUTO JAKO VSTUP PRO UZAVŘENÍ.** Archivní funkcionál z Appendix AA
neuzavírá `UBT-FUND-GR-ACTION`, `UBT-UV-G-PREDICTION` ani
`UBT-UV-PSI-STABILITY` a nesmí být citován jako chybějící mikroskopická
míra. Obnova GR zůstává `CLOSED_CONDITIONALLY`.

Další přípustný kandidát musí vycházet přímo z uzamčené architektury
kovariantní tetrády, deklarovat nesurjektivní jedno-$\Theta$ invariant nad
rámec zkolabovaného kvadratického skaláru prvního jetu a určit svůj
konfigurační prostor i kalibrační kvocient dříve, než bude použit jeho Hessian
nebo indukovaný Newtonův koeficient.
