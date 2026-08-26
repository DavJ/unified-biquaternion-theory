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

# Poznámky k patchi: gradovaný Möbiův most

**Datum:** 2026-08-25  
**Rozsah:** aktivní výzkumná větev RH; beze změn kanonických tvrzení.

<a id="patch-summary"></a>
## Shrnutí

Tento patch přidává spárované anglické/české výzkumné poznámky odvozující klasickou gradovanou prvočíselnou Fockovu identitu

\[
\operatorname{Str}(e^{-sH_P^-})=\prod_{p\in P}(1-p^{-s})
=\sum_n\mu_P(n)n^{-s}.
\]

Propojuje tuto identitu s existující bosonickou prvočíselnou Fockovou větví a s programem racionálních theta revivalů.

Patch také přidává první společný rozhodovací experiment theta–Mellin. Přesná faktorizace ukazuje, že skalární Mellinovy kanály \(\vartheta_2,\vartheta_3,\vartheta_4\) mají pouze jeden stupeň volnosti zeta, a proto uvnitř otevřeného kritického pásu neukládají nulám nezávislou podmínku.

Rozšíření charakteristikami modulo \(5\) poté zvyšuje hodnost koeficientových kanálů na čtyři Dirichletovy \(L\)-kanály. Jejich vazba odvozená z UBT zůstává otevřená.

Fázová a konjugační symetrie klasifikují přípustné hermitovské metriky kanálů jako \(\operatorname{diag}(g_0,g_1,g_2,g_1)\). Dodatečná, dosud neodvozená cyklická symetrie kanálů redukuje tuto rodinu na \(cI\), jehož samotná pozitivita stále neomezuje nuly hlavního kanálu zeta.

Funkcionální rovnice primitivních charakterů modulo \(5\) zaměňují sdružené liché charaktery a ponechávají kvadratický charakter pevný, ale zachovávají stejné nestejné váhy kanálů. Hlavní charakter je imprimitivní a při konduktoru \(5\) nemá konstantní kořenové číslo, takže tyto funkcionální rovnice neposkytují směšování s kanálem zeta.

Pět aditivních reziduálních kanálů poskytuje kanonické Fourierovo směšování. Jejich úplná invariantní metrika má oddělené sudé a liché váhy, zatímco skalární theta konstanty obsazují pouze třírozměrný sudý sektor, kde je metrika určena až na škálu. Mellinova transformace zeta je lineární kombinací tohoto sektoru, ale pozitivita sektorové normy stále neurčuje polohu jejích nul.

První eliptické derivace realizují dva liché reziduální kanály s modulární vahou vyšší o jedna. Jejich invariantní metrika je skalární, avšak prostor konstantních modulárních intertwinerů mezi třemi sudými a dvěma lichými kanály má nulovou dimenzi. Jacobiho kovariance proto sama neztotožňuje obě škály metriky; nadále je nutný operátor měnící váhu a odvozený z UBT.

<a id="patch-claim-control"></a>
## Kontrola tvrzení

Konečné identity a identity v \(\Re s>1\) jsou standardní matematikou. Patch neodvozuje prvočíselné módy, energie \(\log p\) ani fermionickou paritu z kanonické UBT a netvrdí RH. Zpřesňuje již otevřenou mezeru GAP-RH-MOEBIUS-UBT.

<a id="patch-verification"></a>
## Ověření

- Exaktní kontroly podmnožin, rozvoje součinu, faktorizace a Dirichletovy konvoluce jsou v tools/verify_graded_mobius_bridge.py.
- Regresní pokrytí je v tests/test_graded_mobius_bridge.py.
- Theta–Mellinův no-go výsledek nezávisle kontrolují tools/verify_theta_mellin_matrix.py a tests/test_theta_mellin_matrix.py.
- Status Lean je LEAN-PENDING; formální ověření se netvrdí.
- Dvojjazyčná struktura a zobrazené rovnice se musí před sloučením shodovat.

<a id="patch-provenance"></a>
## Údržba provenience

Inventář zdrojů a jeho deklarovaný záznam SHA-256 jsou synchronizovány tak, aby zahrnovaly dříve sloučenou dvojici rezidua–Möbius a čtyři nové spravované zdroje Markdown v tomto patchi.
