<!--
UBT-AI-PROVENANCE-BEGIN
schema: ubt-ai-provenance/v1
tier: C_working
ai_assistance: disclosed
human_review: risk-based
editorial_responsibility: Ing. David Jaroš
policy: AI_PROVENANCE.md
notice: Working material; exhaustive human review is not claimed.
UBT-AI-PROVENANCE-END
-->

# Patch notes: dvoustranný renormalizovaný Eulerův součin

**Datum:** 2026-08-28
**Rozsah:** aktivní výzkumná větev RH; beze změn kanonických tvrzení.

<a id="tre-patch-summary"></a>
## Shrnutí

Tento patch navazuje na audit adelických valuací dvoustranným zpracováním nekonečného součinu lokálních geometrických řad. Stanovuje standardní výsledek, že surový Eulerův součin je ve svém stopovém oboru nenulový a že konečné Maclaurinovo odečtení dává

\[
R_M(s)=\prod_p\frac{1}{1-p^{-s}}
\exp\left(-\sum_{m=1}^{M}\frac{p^{-ms}}m\right),
\qquad
\Re s>\frac1{M+1},
\]

kde je \(R_M\) holomorfní a nenulová.

<a id="tre-patch-two-charts"></a>
## Dva charty

Pro \(M=1\) je dokončená funkce na obou otevřených stranách reprezentována vztahy

\[
\xi(s)=C(s)R_1(s)e^{P(s)},
\qquad
\xi(s)=C(1-s)R_1(1-s)e^{P(1-s)}.
\]

Druhý výraz explicitně pokrývá \(\Re s<1/2\). Ke společné hranici se přistupuje pomocí \(s_\pm=1/2\pm\varepsilon+it\), pro něž

\[
\xi(s_-)=\overline{\xi(s_+)}.
\]

<a id="tre-patch-operator"></a>
## Operátorový výsledek

Všechny vrstvy prvočíselných mocnin s \(m\geq2\) dávají normově konvergentní operátor translací pro každé \(\varepsilon>0\). Necentrovaná první vrstva splňuje

\[
\left\|\sum_{p\leq X}p^{-1/2-\varepsilon}U_{\log p}\right\|
=\sum_{p\leq X}p^{-1/2-\varepsilon}
\]

a proto pro \(0<\varepsilon\leq1/2\) diverguje v operátorové normě. Další platný krok musí tuto první vrstvu kanonicky renormalizovat; pouhé zavedení nelokálního operátoru překážku konvergence nepřekonává.

<a id="tre-patch-claim-control"></a>
## Kontrola tvrzení

Centrovaná Čebyševova reprezentace ukazuje, že odmocninový odhad \(\psi(x)-x\) by dodal potřebnou kontrolu pravého polopásu, ale tento odhad má sílu RH. Patch takový odhad neodvozuje, nekonstruuje Hilbertův--Pólyův operátor a neodvozuje prvočíselné translace ani jejich centrování z UBT.

<a id="tre-patch-verification"></a>
## Ověření

- `tools/verify_two_sided_renormalized_euler.py` kontroluje konečné komplexní Maclaurinovy faktorizace, signatury konvergence na obou stranách vybraných prahů, exaktní normalizaci odrazu \(\xi(2)=\xi(-1)=\pi/6\), konečné odhady norem translací a von Mangoldtovu identitu s prvočíselnými mocninami.
- `tests/test_two_sided_renormalized_euler.py` poskytuje šest regresních testů.
- Ověřovač používá pouze prostředky standardní knihovny Pythonu 3.12.
- Lean není v běhovém prostředí dostupný; exaktní formalizace zůstává `LEAN-PENDING`.
- Zdrojem překladu byla anglická verze. Párová česká verze má shodné kotvy, rovnice, statusové značky, čísla, citace a výhrady; před sloučením je nutná lidská kontrola významové shody.
