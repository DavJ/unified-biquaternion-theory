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

Tento adresář publikuje jednu učebnici ve dvou synchronizovaných edicích.
Jedinými vstupními soubory knihy jsou `main.en.tex` a `main.cs.tex`; oba načítají
společnou jazykově neutrální sazbu z `main.tex` a odpovídající obsahové soubory
`.en.tex` nebo `.cs.tex`.

## Jazykový a obsahový kontrakt

Každý aktivní textový zdroj musí mít anglickou a českou variantu. Oba soubory
musí obsahovat identickou matematiku, rovnice, návěští, odkazy, citace, čísla,
statusy tvrzení a strukturu oddílů. Povoleny jsou pouze překladové rozdíly;
vědecké doplnění nebo vypuštění se musí ve stejné změně promítnout do obou
souborů. CI kontroluje mechanickou shodu, zatímco za významovou rovnocennost
zůstává odpovědný lidský recenzent.

## Oficiální sestavení

Z kořene repozitáře spusťte:

```bash
make -C docs/textbook verify
```

Příkaz vytvoří přesně dva oficiální soubory:

```text
build/textbook/public/UBT_Textbook_EN.pdf
build/textbook/public/UBT_Textbook_CS.pdf
```

`make -C docs/textbook publish` zkopíruje stejnou dvojici do `docs/pdfs/`.
Samostatné studentské materiály zůstávají doplňky a nejsou alternativními
edicemi učebnice.

## Vědecká a provenance pravidla

- `docs/textbook/SOURCE_MAP.md` určuje živé zdroje řídící knihu.
- `ARCHIVE/**` zůstává historické a do živé učebnice se nezapojuje.
- Klasické výsledky, kontrolované UBT mosty a nová či otevřená UBT tvrzení musí
  zůstat viditelně oddělené.
- Odvození v paperech se řídí `docs/DERIVATION_VERIFICATION_POLICY.md`.
- Obsah vytvořený s pomocí AI se řídí `ubt-ai-provenance/v1`; tento adresář
  zůstává v Tier `C_working`, dokud odpovědný lidský editor status nezmění.
