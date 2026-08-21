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

# Pravidla dvojjazyčného obsahu

## Závazné pravidlo

Veškeré aktivní vědecké, publikační, vysvětlující a studentské texty musí
existovat v úplné anglické (`en`) a české (`cs`) verzi. Obě verze jsou
normativní. Změna dokumentu není dokončena, dokud nejsou obě verze ve stejném
pull requestu a neprojdou kontrolou strukturální a významové shody.

Jde o pravidlo totožnosti obsahu, nikoli doslovného překladu. Přirozený slovosled
a idiom se mohou lišit, ale informace dostupné čtenáři se lišit nesmějí.

## Požadovaná totožnost

Každá dvojice jazykových verzí musí přesně zachovat stejné:

1. pořadí oddílů a strukturu obsahových jednotek;
2. rovnice, symboly, číselné hodnoty, jednotky, předpoklady a definiční obory;
3. definice, lemmata, věty, důkazy, příklady a protipříklady;
4. obrázky, tabulky, věcný obsah popisků a data;
5. citace, odkazy na autority, značky a křížové odkazy;
6. status tvrzení, úroveň důkazu, nejistoty, výhrady, varování a provenienci;
7. závěry a výslovně uvedené otevřené otázky.

Žádná verze nesmí přidat ani vynechat vědecké tvrzení, upřesnění, vysvětlení
nebo příklad. Redakční metadata daná jazykem se smějí lišit pouze tehdy, když
nenesou žádný vědecký význam.

## Uspořádání zdrojů

Pro dvojice samostatných zdrojů používejte jazykové přípony ISO:

```text
path/name.en.md    path/name.cs.md
path/name.en.tex   path/name.cs.tex
```

Každá překládaná obsahová jednotka musí mít v obou verzích stejný stabilní
identifikátor. V LaTeXu zachovejte shodné značky a jazykově neutrální rovnice
nebo generované tabulky ukládejte, kdykoli je to praktické, do sdílených vstupů
`*.tex`. V Markdownu používejte shodné explicitní kotvy nebo stabilní
dvojjazyčné značky jednotek. Přejmenování identifikátoru je synchronizovaná
změna.

Nevytvářejte smíšený zdroj a neoznačujte jej jako dvojjazyčný. Každá vykreslená
verze musí být jednojazyčná s výjimkou vlastních jmen, citací, citovaného
primárního materiálu, zavedených symbolů a výslovně označených překladových
poznámek.

## Postup při změně

Každý pull request měnící text v rozsahu těchto pravidel musí:

1. upravit oba párové zdroje ve stejné sérii commitů;
2. uvést, která verze byla zdrojem překladu;
3. potvrdit shodu formální struktury a označení statusu tvrzení;
4. přiložit vykreslené nebo sestavené výstupy, pokud je vytváří běžný workflow;
5. před sloučením získat výslovné lidské potvrzení významové shody.

Automatické kontroly jsou povinné tam, kde jsou dostupné, a musí selhat při
chybějící dvojici nebo neshodě identifikátorů, rovnic, citací, značek
tvrzení/statusu či struktury dokumentu. Úspěch automatických kontrol je nutný,
ale nedokazuje totožnost významu přirozeného jazyka.

## Rozsah a migrace

Pravidlo platí pro aktivní texty v repozitáři včetně učebnic, článků,
kanonických vysvětlení, vysvětlení ve výzkumných větvích, veřejné dokumentace,
zpráv a věcného obsahu README.

Mimo povinnost párování jsou:

- zdrojový kód a strojově čitelná data;
- generované soubory, jejichž dvojjazyčné vstupy pravidlům podléhají;
- neměnný historický materiál pod `ARCHIVE/`;
- doslovné citace a uložené snapshoty primárních zdrojů;
- bibliografické záznamy bez vysvětlujícího textu.

Existující nepárované nebo jazykově smíšené dokumenty jsou migrační dluh.
Dočasně mohou zůstat beze změny, ale nejsou vzorem pro novou práci. Věcná změna
musí převést celý dokument na jazykovou dvojici. Dočasná výjimka vyžaduje
záznam schválený vlastníkem repozitáře ve vyhrazeném registru výjimek; záznam
musí obsahovat přesné cesty, důvod, vlastníka a datum vypršení. Výjimky nikdy
nesmějí oslabit požadavky na status tvrzení nebo provenienci.

## Podmínka sloučení

Změna podléhající dvojjazyčným pravidlům se nesmí sloučit, dokud neplatí vše
následující:

- obě verze existují a úspěšně se sestaví nebo vykreslí;
- strukturální kontroly projdou;
- pull request obsahuje prohlášení o významové shodě;
- lidský posuzovatel významovou shodu výslovně schválí;
- nezůstává žádná nevyřešená výjimka z dvojjazyčných pravidel.

Pokud je totožnost významu nejistá, bezpečným stavem je ponechat pull request
jako draft a nevydat žádnou změněnou verzi.
