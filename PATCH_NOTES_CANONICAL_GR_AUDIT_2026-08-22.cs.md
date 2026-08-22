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

# Audit kanonických a GR odvození

<!-- BILINGUAL-UNIT: audit.scope -->
## Rozsah

Tato změna audituje algebraické kroky důležité pro věty v kanonické vrstvě a
`papers/UBT_GR_Submission.tex`. Zdrojovým jazykem této párové poznámky a párové
opravy článku je angličtina. Automatická shoda struktury a statusů prochází;
před merge je povinná lidská kontrola sémantické ekvivalence.

<!-- BILINGUAL-UNIT: audit.result -->
## Výsledek

Kontroly centrální metriky a hodnosti, konexe a kontorze, lokální
integrability, děleného jetu, hlavního symbolu a podmíněného indukovaného
Einsteinova koeficientu procházejí v rámci zaznamenaných předpokladů. Starší
povýšení prostorové Schwarzschildovy identity na úplné kanonické řešení z
jediného Theta selhává. Autoritativní status zůstává `GAP-U2Theta: OPEN`.

Neplatné povýšení bylo odstraněno z publikované kanonické sady Pages a
nahrazeno strojově čitelným záznamem statusu a párovou opravou článku.
Historický zdroj zůstává zachován kvůli dohledatelnosti a před přepsáním nebo
odstraněním vyžaduje samostatnou dvojjazyčnou archivní migraci.

<!-- BILINGUAL-UNIT: audit.fixes -->
## Opravy

- Přidán nezávislý audit v SageMath pro přesnou hodnost metriky, přesnou
  hodnost zobrazení kontorze na torzi, přesná Schwarzschildova protipříkladová
  svědectví a koeficient tepelného jádra.
- Opraven ověřovač tepelného jádra převedením nekonečného integračního oboru
  na stabilní konečný interval.
- Rozsah staršího ověřovače NumPy byl omezen na prostorovou identitu, kterou
  skutečně kontroluje, a byla přidána ochrana kanonického Lorentzova řezu.
- Přidány regresní testy a strojově čitelný záznam ověření.
- Přidány párové anglické/české opravné dokumenty se shodnými rovnicemi,
  statusy tvrzení a omezeními.

<!-- BILINGUAL-UNIT: audit.assumptions -->
## Předpoklady a omezení

Kontroly počítačovou algebrou dokazují pouze zakódované konečně rozměrné
identity a podmíněnou kvadraturu. Nedokazují dynamický výběr, dobrou položenost
PDE, globální pokračování, preferovaný řez imaginárního času ani fyzickou
pravdivost UBT. Indukovaný Einsteinův koeficient zůstává podmíněn uvedenými
předpoklady o hessiánu Laplaceova typu, míře, cutoffu, počtu módů a
regularizátoru.

<!-- BILINGUAL-UNIT: audit.remaining -->
## Zbývající mezery

- `GAP-U2Theta: OPEN`: kanonické on-shell vytvoření úplné Schwarzschildovy
  tetrády a lapse.
- `LEAN-PENDING`: žádný současný zdroj Lean neformalizuje auditovaná GR
  tvrzení.
- Před merge je povinná lidská kontrola sémantické ekvivalence anglické/české
  dvojice.
