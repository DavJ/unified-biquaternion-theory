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

# UBT učebnice

Tento adresář má **jednu hlavní učebnici** a několik jasně označených doplňků.
Běžný vstupní bod pro čtení je `main.tex` → `UBT_Textbook.pdf`; ostatní kořenové
`.tex` soubory nejsou paralelní učebnice.

## Jazyk

Primární studentská edice je **česká**. Nové vysvětlující texty, názvy kapitol,
popisky a didaktické poznámky se mají psát česky. Anglickou verzi lze později
udržovat jako paralelní edici se stejnou strukturou rovnic, tvrzení a statusů;
angličtina se nemá nahodile míchat do českých kapitol. Starší anglické části,
které ještě nebyly převedeny, jsou migrační dluh, nikoli jazykový vzor pro nové
kapitoly.

## Struktura hlavní knihy

Hlavní kniha je členěna do čtyř viditelných částí:

1. **Základy a geometrie** — přehled UBT, bikvaterniony, Lorentzova geometrie,
   tetrády, konexe, torze a konstrukce metriky.
2. **Komplexní čas a spektrální struktura** — komplexní čas, theta funkce,
   Mellinova/zeta transformace, Feynmanův/path-sum most a otázka prime sektorů.
3. **Fenomenologie, verifikace a aplikace** — program konstanty jemné struktury,
   reprodukovatelnost a aplikační směry.
4. **Referenční dodatky** — důkazy, FAQ a oddělené spekulativní materiály.

Samostatné dokumenty jsou **doplňky**, nikoli konkurenční učebnice:

- `covariant_tetrad_student_paper.tex` — zaměřený geometrický výtah používající
  živý zdroj kapitoly o kovariantní tetrádě;
- `indices_torsion_anticommutator_rot_student_paper_cs.tex` — český intuitivní
  doplněk o indexech, torzi, curl/rot a UBT antikomutátoru.

## Build kontrakt

Z kořene repozitáře:

```bash
make -C docs/textbook verify
```

vzniknou stabilně pojmenované soubory:

```text
build/textbook/public/UBT_Textbook.pdf
build/textbook/public/UBT_Textbook_Supplement_Covariant_Tetrad.pdf
build/textbook/public/UBT_Textbook_Supplement_Indexy_Torze_Rot_CS.pdf
```

Pro zkopírování stejné kurátorované sady do `docs/pdfs/`:

```bash
make -C docs/textbook publish
```

GitHub Actions používá tentýž Makefile po strict kontrole `latex_audit.py` a
nahrává stabilní PDF jako artefakt `ubt-textbook-pdfs-${run_id}`.

## Vědecký a provenance režim

- `docs/textbook/SOURCE_MAP.md` určuje, které živé zdroje řídí knihu.
- `ARCHIVE/**` je historický materiál a do živé učebnice se přes `\input`
  nezapojuje.
- Klasická matematika se zachovává a odvozuje, pokud je didakticky potřebná.
- Musí zůstat viditelný rozdíl mezi klasickým výsledkem, kontrolovaným UBT
  mostem a novým/otevřeným UBT tvrzením.
- Odvození paperů se řídí `docs/DERIVATION_VERIFICATION_POLICY.md`: Lean je
  preferovaný formální kontrolor a hlavní výsledky se mají nezávisle ověřovat
  i CAS/numerickými nástroji.
- AI-assisted obsah používá existující nomenklaturu `ubt-ai-provenance/v1`;
  tento adresář je Tier `C_working`, dokud lidský autor výslovně nezmění
  autoritativní provenance mapu.
