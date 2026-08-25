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

<a id="patch-claim-control"></a>
## Kontrola tvrzení

Konečné identity a identity v \(\Re s>1\) jsou standardní matematikou. Patch neodvozuje prvočíselné módy, energie \(\log p\) ani fermionickou paritu z kanonické UBT a netvrdí RH. Zpřesňuje již otevřenou mezeru GAP-RH-MOEBIUS-UBT.

<a id="patch-verification"></a>
## Ověření

- Exaktní kontroly podmnožin, rozvoje součinu, faktorizace a Dirichletovy konvoluce jsou v tools/verify_graded_mobius_bridge.py.
- Regresní pokrytí je v tests/test_graded_mobius_bridge.py.
- Status Lean je LEAN-PENDING; formální ověření se netvrdí.
- Dvojjazyčná struktura a zobrazené rovnice se musí před sloučením shodovat.

<a id="patch-provenance"></a>
## Údržba provenience

Inventář zdrojů a jeho deklarovaný záznam SHA-256 jsou synchronizovány tak, aby zahrnovaly dříve sloučenou dvojici rezidua–Möbius a čtyři nové spravované zdroje Markdown v tomto patchi.

