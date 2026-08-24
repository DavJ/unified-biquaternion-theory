<!-- BILINGUAL-UNIT: multisymplectic-dirac.provenance -->
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

# Eulerův--Lagrangeův systém a generalized-Diracova obstrukce pro kovariantní multisymplektickou rodinu

<!-- BILINGUAL-UNIT: multisymplectic-dirac.setup -->
## Nastavení

Nechť `V` je osmírozměrný reálný prostor pole s konstantní symplektickou
formou `omega`, `D` je symplektické spojení a položme

\[
 P:=D\Theta,\qquad Q:=\frac12\omega(P\wedge P),\qquad
 S_F^{\rm cov}=\frac12\int_{M_4}F(\Theta)Q\wedge Q.
\]

Při variaci `Theta` držíme spojení pevné. Označme
`RTheta:=D^2 Theta` a matici formy `omega` symbolem `omega_{AB}`.

<!-- BILINGUAL-UNIT: multisymplectic-dirac.el -->
## Úplný Theta Eulerův--Lagrangeův systém [L1]

Kovariantní variace dává následujících osm rovnic ve formě čtyřforem:

\[
\boxed{
 \begin{aligned}
 \mathcal E_A={}&\frac12F_{,A}Q\wedge Q
 -\omega_{AB}\,dF\wedge P^B\wedge Q\\
 &+F\omega_{AB}P^B\wedge dQ
 -F\omega_{AB}(\mathcal R\Theta)^B\wedge Q=0,
 \end{aligned}}
\]

kde

\[
 dQ=\omega(\mathcal R\Theta,P).
\]

Toto je úplná objemová rovnice pro spojení, které je při variaci
nezávislé na `Theta` a jejích jetech. Okrajová data musí na hranici
anulovat `F omega(delta Theta,P) wedge Q`.

<!-- BILINGUAL-UNIT: multisymplectic-dirac.hessian -->
## Hlavní Hessian a zrušení druhých jetů [L0/L1]

V lokálních souřadnicích je hustota

\[
 L=F\,\operatorname{Pf}(Q_{\mu\nu}),\qquad
 Q_{\mu\nu}=\omega_{AB}P_\mu^AP_\nu^B.
\]

Její Hessian podle prvního jetu přesně splňuje

\[
 W^{\mu\nu}{}_{AB}
 =-W^{\nu\mu}{}_{AB}
 =-W^{\mu\nu}{}_{BA}.
\]

Proto

\[
 W^{\mu\nu}{}_{AB}D_{(\mu}D_{\nu)}\Theta^B=0.
\]

Všechny symetrické druhé jety se zruší. Výskyty `D^2 Theta` v úplné
rovnici výše jsou pouze antisymetrický komutátor `R Theta`; pro pevné
spojení jde o nultý řád v `Theta`. Rovnice je tedy v `Theta` prvního
řádu. Tento závěr **nelze** přenést přes nedokázanou substituci
`A=A[Theta,DTheta,...]`: pak je nutné znovu spočítat řetězové pravidlo a
Leviho--Civitovo/kompozitní spojení obvykle zavádí vyšší jety.

<!-- BILINGUAL-UNIT: multisymplectic-dirac.flat-identities -->
## Přesné diferenciální identity na ploché větvi [L0]

Na plochém patchi s `A=0` je akce pullbackem čtyřformy cílového prostoru
`F omega^2/2`. Položme `P_mu=partial_mu Theta`. Cartanův vzorec dává

\[
 \mathcal E_A\,\delta\Theta^A
 =\Theta^*\!\left(\iota_{\delta\Theta}
   (dF\wedge\omega^2/2)\right).
\]

Volba tečné variace `delta Theta=P_mu xi^mu` kontrahuje pětiformu s pěti
vektory ležícími ve čtyřrozměrném obrazu `P`, a proto identicky mizí.
Tedy

\[
\boxed{P_\mu^A\mathcal E_A\equiv0\quad(\mu=0,1,2,3).}
\]

V každém jetu hodnosti čtyři jsou to čtyři nezávislé Noetherovy
identity. Osm zobrazených složk rovnice má hodnost nejvýše čtyři. Zejména
jejich Jacobiho matice podle hodnoty pole nemůže být na této větvi
invertibilní. Pro `F=H` dosahuje přesný racionální svědek použitý ve
verifikátoru hodnosti přesně čtyři, takže mez je ostrá na neprázdné
otevřené množině.

<!-- BILINGUAL-UNIT: multisymplectic-dirac.dirac -->
## Obstrukce vůči kanonické generalized-Diracově rovnici [L1]

Kanonický generalized-Diracův kandidát je osmisložkový reálný systém
prvního řádu s nenulovým lineárním hlavním symbolem. Jeho již dokázaný
postačující mechanismus hodnosti deset vyžaduje invertibilní původní blok
pole `F_Psi` velikosti `8 x 8`, například nenulový skalární nebo
skalárně--pseudoskalární hmotový blok.

Plochý multisymplektický Eulerův--Lagrangeův systém nemůže být s tímto
systémem totožný ani po invertibilní rekombinaci rovnic:

1. má čtyři identity `P_mu^A E_A=0`, a tedy v jetu hodnosti čtyři
   nejvýše čtyři nezávislé rovnice;
2. jeho závislost na prvních derivacích je homogenní stupně čtyři, zatímco
   hlavní část generalized-Diracovy rovnice je homogenní stupně jedna;
3. jeho Jacobiho matice podle hodnoty pole je singulární, a proto
   nerealizuje dosud dokázanou postačující podmínku invertibilního bloku pro
   hodnost deset.

Třetí tvrzení nedokazuje selhání obecnější podmínky `A+K=R^16`; dokazuje,
že snadná cesta přes invertibilní blok není dostupná. Ani bodová hodnost
sama o sobě nezajišťuje lokální integrabilitu jetů. Křivost nebo kompozitní
spojení mohou změnit rovnice nižšího řádu, ale pak důkaz pro pevné
spojení/pullback již nezakládá ekvivalenci a úplná kompozitní variace je
samostatný problém vyšších jetů.

Spolu s větou o kolapsu hodnosti pro pomocné spojení tak nezůstává žádné
dokázané dokončení této rodiny bez nového propagujícího pole, které by
současně bylo teorií nedegenerovaného UBT tetrádu a kanonickou
generalized-Diracovou rovnicí.

<!-- BILINGUAL-UNIT: multisymplectic-dirac.verification -->
## Verifikace

`tools/verify_multisymplectic_dirac_transversality.py` používá přesnou
aritmetiku SymPy a:

- konstruuje osm Eulerových--Lagrangeových složek jako kontrakce
  `dH wedge omega^2/2`;
- symbolicky ověřuje všechny čtyři identity `P^T E=0`;
- ověřuje hodnost čtyři (a tedy singularitu) Jacobiho matice podle hodnoty
  pole v přesném racionálním jetu hodnosti čtyři;
- derivuje pfaffovskou hustotu a v několika přesných svědcích ověřuje
  přesnou dvojitou antisymetrii úplného Hessianu podle prvního jetu a
  nulovou kontrakci s libovolnými symetrickými druhými jety.

Důkaz vnějším počtem je analytický. Stav Leanu je `LEAN-PENDING`:
repozitář nemá zkompilovanou formalizaci diferenciálních forem s potřebnými
identitami pullbacku a kontrakce pro tuto větu.

<!-- BILINGUAL-UNIT: multisymplectic-dirac.status -->
## Status

**KOVARIANTNÍ THETA ROVNICE PRO PEVNÉ SPOJENÍ A ZRUŠENÍ DRUHÝCH JETŮ:
PROVED [L1].**

**PŘÍMÁ EKVIVALENCE PLOCHÝCH MULTISYMPLEKTICKÝCH ROVNIC S KANONICKÝM
GENERALIZED-DIRACOVÝM SYSTÉMEM: CLOSED AS NO-GO [L1].**

**OBECNÁ TRANSVERZALITA HODNOSTI DESET PRO KOMPOZITNÍ/DIFERENCIÁLNĚ VYŠŠÍ
DOKONČENÍ: OPEN.**
