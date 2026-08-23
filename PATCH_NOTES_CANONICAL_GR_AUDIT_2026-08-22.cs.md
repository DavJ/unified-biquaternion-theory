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
opravy článku je angličtina. Automatická shoda struktury a statusů musí projít;
před merge je povinná lidská kontrola sémantické ekvivalence.

<!-- BILINGUAL-UNIT: audit.result -->
## Výsledek

Kontroly centrální metriky a hodnosti, konexe a kontorze, lokální
integrability, děleného jetu, hlavního symbolu a podmíněného indukovaného
Einsteinova koeficientu procházejí v rámci zaznamenaných předpokladů. Starší
povýšení prostorové Schwarzschildovy identity na úplné kanonické řešení z
jediného Theta selhává a zůstává `SUPERSEDED_INVALID_DERIVATION`.

Oddělené složení již ustavené split-jet pravé inverze, nepropagující pomocné
akce a podmíněné Einsteinovy--Hilbertovy infračervené efektivní větve uzavírá
vymezenou otázku obnovy jako `GR-RECOVERY: CLOSED CONDITIONALLY`. Proto platí
`GAP-U2Theta: CLOSED CONDITIONALLY FOR GR RECOVERY` a
`GAP-B-MASTER: CLOSED CONDITIONALLY FOR EFFECTIVE GR PERTURBATIONS`, aniž by
se obnovoval neplatný historický ansatz.

Neplatné povýšení bylo odstraněno z publikované kanonické sady Pages a
nahrazeno strojově čitelným záznamem statusu a párovou opravou článku.
Historický zdroj zůstává zachován kvůli dohledatelnosti.

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
- Přidána párová věta o dokončení obnovy GR a vymezený ledger obnovy.

<!-- BILINGUAL-UNIT: audit.assumptions -->
## Předpoklady a omezení

Kontroly počítačovou algebrou dokazují pouze zakódované konečně rozměrné
identity a podmíněnou kvadraturu. Podmíněná obnova GR předpokládá konečný kladný
renormalizovaný Einsteinův--Hilbertův koeficient, dokázanou lokální split-jet
konstrukci na regulárních nenulových patchích, fyzickou Levi--Civitovu konexi a
potlačení vyšších derivací v tvrzeném infračerveném řádu. Výsledek neodvozuje
úplný mikroskopický metrický selektor pouze z Theta, omezenou kvantovou míru,
prvoprincipovou numerickou hodnotu Newtonovy konstanty, UV stabilitu psi ani
globální pokračování přes nulové patche.

<!-- BILINGUAL-UNIT: audit.remaining -->
## Zbývající fundamentální otázky

- `UBT-FUND-GR-ACTION: OPEN`: odvodit úplný efektivní selektor z finalizované
  mikroskopické akce pouze pro Theta.
- `UBT-UV-G-PREDICTION: OPEN`: odvodit kompozitní Hessián, počet módů, vazbu,
  identifikaci cutoffu a omezenou míru potřebné k predikci Newtonovy konstanty,
  nikoli pouze k obnově GR s renormalizovaným koeficientem.
- `UBT-FUND-GLOBAL: OPEN`: dokázat globální pokračování přes nulové a
  horizontové patche.
- `LEAN-PENDING`: žádný současný zdroj Lean neformalizuje auditovaná GR
  tvrzení.
- Před merge je povinná lidská kontrola sémantické ekvivalence anglické/české
  dvojice.
