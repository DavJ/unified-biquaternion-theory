<!-- BILINGUAL-UNIT: holomorphy-factor.provenance -->
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

# Samotná holomorfie nevybírá jeden Diracův faktor

<!-- BILINGUAL-UNIT: holomorphy-factor.scope -->
## Rozsah

Kanonický program generalizovaného Diracova operátoru ponechává otevřenou cestu,
v níž se operátor druhého řádu faktorizuje a komplexně-časová analyticity vybere
jeden faktor prvního řádu. Tato poznámka testuje selekční sílu samotné
holomorfie, nezávisle na dodatečné podmínce pozitivity, chirality, okrajové nebo
spektrální podmínce.

Nechť

\[
\tau=t+i\psi
\]

je kanonická komplexní časová proměnná.

<!-- BILINGUAL-UNIT: holomorphy-factor.counterexample -->
## Přesný protipříklad [L0]

Uvažujme faktorizovaný skalární model

\[
(\partial_\tau-m)(\partial_\tau+m)f=0,
\qquad m\ne0.
\]

Obě funkce

\[
\boxed{f_+(\tau)=e^{m\tau},\qquad f_-(\tau)=e^{-m\tau}}
\]

jsou celé holomorfní funkce `tau`. Splňují

\[
(\partial_\tau-m)f_+=0,
\qquad
(\partial_\tau+m)f_-=0,
\]

a tedy obě řeší stejnou rovnici druhého řádu. Proto

\[
\boxed{\text{holomorphy alone does not distinguish the two factors}.}
\]

Tvrzení nezávisí na konvenci znaménka použité k pojmenování obou faktorů
prvního řádu.

<!-- BILINGUAL-UNIT: holomorphy-factor.periodic -->
## Kompaktní `psi` samo neodstraní degeneraci znaménka

Předpokládejme, že imaginární časový směr je kompaktní s periodou
`2 pi R_psi`. Při pevném reálném `t`,

\[
f_\pm(t+i(\psi+2\pi R_\psi))
=f_\pm(t+i\psi)e^{\pm i2\pi mR_\psi}.
\]

Kdykoli je periodicita splněna obvyklou celočíselnou podmínkou

\[
mR_\psi\in\mathbb Z,
\]

splňují ji **obě znaménka současně**, protože
`exp(+i 2 pi n)=exp(-i 2 pi n)=1`. Holomorfie spolu s běžnou periodicitou
kompaktního `psi` tedy stále nevybírá jednoznačný faktor prvního řádu.

Obecnější twistované okrajové podmínky mohou rozlišit sektory až poté, co je
sám twist nezávisle vybrán. Takový twist je dodatečné fyzikální datum, nikoli
důsledek samotné holomorfie.

<!-- BILINGUAL-UNIT: holomorphy-factor.consequence -->
## Důsledek pro program původu akce UBT

Ani exaktní faktorizace rovnice druhého řádu UBT by stále potřebovala další
větu, která vybere jednu generalizovanou Diracovu větev. Kanonická podmínka
holomorfie sama tuto roli nemůže plnit.

Životaschopný selektor musí obsahovat informaci nad rámec analyticity,
například odvozenou podmínku pozitivity/energie, projekci chirality, orientovanou
spektrální podmínku, netriviální okrajové/twistové datum nebo skutečně
degenerovaný variační princip prvního řádu. Každý takový návrh musí být odvozen
z téže struktury UBT, nikoli zvolen až po znalosti požadovaného faktoru.

<!-- BILINGUAL-UNIT: holomorphy-factor.verification -->
## Ověření

`tools/verify_holomorphy_factor_no_go.py` kontroluje obě faktorové rovnice a
identitu periodicity kompaktního `psi` symbolicky pomocí SymPy.
`tests/test_holomorphy_factor_no_go.py` udržuje protipříklad v CI.

Protipříklad je elementární a exaktní. Formalizace v Leanu je `LEAN-PENDING`.

<!-- BILINGUAL-UNIT: holomorphy-factor.status -->
## Dopad na status

**HOLOMORPHY-ONLY DIRAC FACTOR SELECTION: CLOSED AS NO-GO [L0].**

Tím se uzavírá jedna navrhovaná podcesta gapu původu generalizovaného Diracova
operátoru z akce. Holomorfie tím není vyloučena jako jedna složka silnějšího
selektoru; je vyloučeno pouze použití samotné analyticity jako chybějící věty
o výběru větve.
