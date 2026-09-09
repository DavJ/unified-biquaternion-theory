<!-- BILINGUAL-UNIT: multisymplectic-slice.provenance -->
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

# Nulovost kovariantní multisymplektické akce na Lorentzově řezu

<!-- BILINGUAL-UNIT: multisymplectic-slice.scope -->
## Rozsah a konvence

Tato poznámka zkoumá již navrženou akci

\[
S_F=\frac12\int_U F(\Theta)\,Q\wedge Q,\qquad
P=D\Theta,\qquad Q=\frac12\omega_{AB}P^A\wedge P^B
\]

na pevně stanovené kanonické Lorentzově větvi. Zde \(U\) označuje orientovanou
hladkou oblast časoprostoru, pole i koeficienty jsou hladké a variace mají
kompaktní nosič. Skalár \(F\) je hladký reálný invariant na uvažovaných
hodnotách pole; singulární koeficienty jsou vyloučeny.

Reálný prostor pole je realifikací \(M_2(\mathbb C)\), uspořádanou podle
reálných a poté imaginárních částí \(z=(a,b,c,d)^T\), s řádky matice
\((a,b)\) a \((c,d)\). Dříve klasifikované párování je

\[
h(u,v)=u^\dagger Gv,\qquad
G=\begin{pmatrix}
0&0&0&1\\0&-1&0&0\\0&0&-1&0\\1&0&0&0
\end{pmatrix},\qquad
\omega(u,v)=\operatorname{Im}h(u,v),\qquad
\Omega=\begin{pmatrix}0&G\\-G&0\end{pmatrix}.
\]

Imaginární část definuje tuto již navrženou symplektickou formu v prostoru
pole. **Nejde** o novou projekci definující fyzikální metriku. Metrika nadále
plyne z kanonické centrální antikomutátorové identity s involucí sharp.

Pro explicitní spinovou reprezentaci použitou níže platí

\[
D\Theta=d\Theta+\mathcal A\Theta+\Theta\mathcal A^\dagger
       =d\Theta+\mathcal A\Theta-\Theta\mathcal B,\qquad
\mathcal B=-\mathcal A^\dagger,\qquad
\mathcal A\in\mathfrak{sl}(2,\mathbb C).
\]

V reálných složkách jde o \(D\Theta=d\Theta+\rho_*(\mathcal A)\Theta\).
Zavedenou symplektickou konexi lze držet pevnou, variovat jako pomocnou
proměnnou nebo dosadit jako diferencovatelný složený funkcionál.
Jde o různé variační úlohy. Níže uvedená věta o nulovosti platí pro každou
z nich při splnění uvedené podmínky řezu; nevyvozuje rovnice prvního řádu
pro složenou konexi z výpočtu s pevnou konexí.

<!-- BILINGUAL-UNIT: multisymplectic-slice.lagrangian -->
## M1 — Kanonický Lorentzův řez je lagrangeovský [L0]

Použijme Pauliho reprezentaci kanonické kvaternionové báze,

\[
b_0=iI_2,\qquad b_k=-i\sigma_k,\qquad
W_L=\left\{b_a x^a:x^a\in\mathbb R\right\},\qquad
\eta=\operatorname{diag}(-1,1,1,1).
\]

Komplexní souřadnicová matice, jejímiž sloupci jsou čtyři bázové vektory, je

\[
C=\begin{pmatrix}
i&0&0&-i\\
0&-i&-1&0\\
0&-i&1&0\\
i&0&0&i
\end{pmatrix},\qquad
C^\dagger GC=-2\eta.
\]

Proto je \(h(Cx,Cy)=-2x^T\eta y\) reálné pro reálné \(x,y\), a tedy

\[
\boxed{\omega|_{W_L\times W_L}=0.}
\]

Reálné vnoření

\[
J=\begin{pmatrix}\operatorname{Re}C\\\operatorname{Im}C\end{pmatrix}
\]

má hodnost čtyři a splňuje

\[
J^T\Omega J=0,\qquad
\dim_{\mathbb R}W_L=4=\frac12\dim_{\mathbb R}V.
\]

To je přesně lagrangeovský podprostor: izotropní podprostor poloviční dimenze
vzhledem k okolnímu prostoru. Terminologie a elementární kritérium jsou
standardní; viz Ana Cannas da Silva, [Lectures on Symplectic Geometry, Homework 1](https://people.math.ethz.ch/~acannas/Papers/lsg.pdf).
Zobrazené omezení matice UBT je vypočteno zde.

Každá symplektická transformace v dané reprezentaci převádí tuto rovinu na
jinou lagrangeovskou rovinu. Zvláště společná fáze nebo lokální spinová
transformace všech čtyř jetových vektorů nemůže závěr změnit. Není třeba
volit preferovaný fázový řez.

<!-- BILINGUAL-UNIT: multisymplectic-slice.vanishing -->
## M2 — Akce i úplná první variace na řezu mizí [L1]

Předpokládejme v celé oblasti kanonickou podmínku tetrády:

\[
P_\mu=D_\mu\Theta=c_0 b_a e^a{}_\mu,\qquad
c_0=\sqrt{\mathcal N_0}>0,\qquad e^a{}_\mu\in\mathbb R.
\]

Z M1 plyne bodová identita

\[
Q_{\mu\nu}=\omega(P_\mu,P_\nu)=0.
\]

Platí pro každý reálný koreper včetně nedegenerovaných zakřivených
koreperů; nebyla použita rovnice pole ani omezení křivosti.
Omezuje pouze kovariantní jet: samotná hodnota pole nemusí ležet
v Lorentzově řezu.

Pro libovolné hladké variace všech nezávislých proměnných ve zvolené variační
úloze dává derivování před integrací per partes

\[
\delta S_F
=\frac12\int_U\delta F\,Q\wedge Q
 +\int_U F\,\delta Q\wedge Q.
\]

V každé hladké konfiguraci na řezu tedy platí

\[
\boxed{S_F=0,\qquad \delta S_F=0.}
\]

Variace nemusí zachovávat řez. Každý člen již obsahuje faktor \(Q\)
vyhodnocený na výchozí konfiguraci. To zahrnuje i indukovanou variaci složené
konexe: úplné řetězové pravidlo změní \(\delta Q\), ale nemůže odstranit
násobící faktor \(Q\). Je nutná hladká závislost a existence první variace;
singulární dosazení leží mimo rozsah věty.

Každá přípustná hladká konfigurace na řezu je tak stacionární pro tento
sektor akce. Sám nemůže rozlišit einsteinovské a neeinsteinovské korepery.
Přidání jiného sektoru akce může závěr změnit, jeho dynamiku však musí
stanovit samostatné odvození.

<!-- BILINGUAL-UNIT: multisymplectic-slice.hessian -->
## M3 — Co z toho plyne pro hessián [L1]

Ve výchozí konfiguraci s \(Q=0\) je smíšená druhá variace

\[
\boxed{\delta_1\delta_2 S_F
=\int_U F\,\delta_1Q\wedge\delta_2Q.}
\]

Členy obsahující variaci \(F\) nebo druhou variaci \(Q\) mizí, protože stále
násobí výchozí \(Q\). Je-li jedna variace tečná k hladké rodině konfigurací
na řezu, pak \(\delta_1Q=0\), takže její smíšené párování s každou jinou
variací mizí. Pokud je podmínka řezu uložena celému konfiguračnímu prostoru
před variací, omezený funkcionál je identicky nulový a všechny jeho variace mizí.

Neomezený hessián nelze prohlásit za nulový. Rozdíl ilustruje konečný jetový
příklad. Nechť

\[
H=-2\eta,\qquad
Z=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},
\qquad B=\frac12H^{-1}Z,\qquad
P_\mu(\varepsilon)=b_\mu+\varepsilon i b_aB^a{}_\mu.
\]

Přímá polarizace dává

\[
Q(\varepsilon)=\varepsilon
(dx^0\wedge dx^1+dx^2\wedge dx^3),\qquad
\frac12FQ(\varepsilon)\wedge Q(\varepsilon)
=F\varepsilon^2\,d^4x.
\]

Pro nenulový koeficient má bodová hustota v tomto směru nenulovou druhou
derivaci. To **nedokazuje** šířící se objemové módy: stále je třeba zohlednit
kompatibilní poruchy pole, integrace per partes, okrajové členy a fyzikální
kvocient módů. Například pro plochou pevnou konexi a konstantní koeficient
je původní akce daná zpětným obrazem okrajovým členem. Její objemový hessián
pak mizí, přestože bodový hessián hustoty v jetových proměnných může být nenulový.

<!-- BILINGUAL-UNIT: multisymplectic-slice.witness -->
## M4 — Explicitní stacionární koreper, který není einsteinovský [L1]

Na oblasti s \(t>0\) použijme bezrozměrné lokální souřadnice a položme

\[
e^0=dt,\qquad e^i=t^2dx^i,\qquad
\Theta=c_0t\,b_0,\qquad
g=-dt^2+t^4\sum_{i=1}^3(dx^i)^2.
\]

Nechť Lorentzova jetová konexe má jako jediné nenulové složky v reperu

\[
\widehat\omega^i{}_0=\widehat\omega^0{}_i=t\,dx^i,
\qquad
\mathcal A_{\rm jet}=-\frac t2\sum_{i=1}^3\sigma_i\,dx^i.
\]

Explicitní oboustranné působení z úvodních předpokladů pak dává

\[
D_{\rm jet}\Theta
=c_0 b_0\,dt+c_0t^2\sum_{i=1}^3 b_i\,dx^i
=c_0b_a e^a.
\]

Koreper je nedegenerovaný a reprezentant pole nemá nulovou normu:

\[
\det(e^a{}_\mu)=t^6,\qquad X^a=(c_0t,0,0,0),\qquad
\eta_{ab}X^aX^b=-c_0^2t^2.
\]

Fyzikální Lorentzova konexe bez torze je odlišná:

\[
\omega_{\rm LC}^i{}_0=\omega_{\rm LC}^0{}_i=2t\,dx^i,\qquad
K^i{}_0=K^0{}_i=-t\,dx^i,\qquad
\widehat\omega=\omega_{\rm LC}+K,\qquad w=0.
\]

Jde o explicitní složené objekty v již zavedené architektuře s oddělenou
jetovou konexí. Zobrazená jetová konexe má torzi; není ztotožněna
s fyzikální konexí bez torze. Nepostuluje se druhá šířící se konexe.
Příklad reprezentuje pole a koreper; neodvozuje samostatný zákon,
který tyto složené objekty vybírá.

Při konvenci
\(R^\rho{}_{\sigma\mu\nu}
=\partial_\mu\Gamma^\rho_{\nu\sigma}
-\partial_\nu\Gamma^\rho_{\mu\sigma}
+\Gamma^\rho_{\mu\lambda}\Gamma^\lambda_{\nu\sigma}
-\Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\mu\sigma}\)
a \(R_{\sigma\nu}=R^\rho{}_{\sigma\rho\nu}\) má fyzikální metrika křivost

\[
R_{00}=-\frac6{t^2},\qquad
R_{ii}=10t^2,\qquad R_{\mu\nu}=0\;(\mu\ne\nu),\qquad
R=\frac{36}{t^2}.
\]

Zvláště platí

\[
\frac{R_{00}}{g_{00}}=\frac6{t^2}
\ne\frac{10}{t^2}=\frac{R_{ii}}{g_{ii}}.
\]

Metrika nesplňuje \(R_{\mu\nu}=\Lambda g_{\mu\nu}\), ani kdyby byl povolen
bodově proměnný faktor úměrnosti. Přesto platí \(Q=0\) a podle M2 je
stacionární pro každého hladkého člena uvedené rodiny akcí.
Jde o konkrétní protipříklad výběru vakuové Einsteinovy geometrie samotnou
touto rodinou; netvrdí se splnění dodatečných rovnic hmoty.

<!-- BILINGUAL-UNIT: multisymplectic-slice.previous -->
## Vztah k dřívější překážce pomocné konexe

[Předchozí věta o kalibrování](theta_covariant_multisymplectic_gauging.cs.md)
předpokládala současně \(F\ne0\) a \(Q\wedge Q\ne0\), než použila symplektický
izomorfismus vnějšího součinu a generickou hodnost orbity ke snížení hodnosti
tetrády. M1 ukazuje, že její druhý předpoklad není kanonickým Lorentzovým
jetem nikdy splněn. Věta zůstává platným podmíněným tvrzením na širším
reálném prostoru pole, ale tento kanonický sektor nezkoumá.

Chybějící sektor je nyní pokryt přímo: jeho problémem je nulovost celé
akce i její první variace, a proto také mizí rovnice čistě pomocné konexe.
V tomto sektoru neposkytuje žádnou rovnici vybírající koreper.
Pro uvedenou Lorentzovu větev jde o silnější výsledek než generický argument
s hodností a nezávisí na stratu orbity ani na \(F\ne0\).

Výsledek se týká přesně rodiny uvedené v úvodních předpokladech. Nevylučuje
akce s bivektorovou či Cliffordovou křivostí, nezávisle přidané sektory
křivosti ani skutečně odvozenou kvantovou efektivní akci.

<!-- BILINGUAL-UNIT: multisymplectic-slice.verification -->
## Ověření a status

Spusťte `tools/verify_multisymplectic_lorentz_slice.py`. Doprovodný záznam je
`reports/multisymplectic_lorentz_slice_2026_09_08.json`.

Ověřovací skript obsahuje sedm skupin: přesnou Gramovu identitu na řezu;
neomezené derivování hustoty v jetových proměnných; kontroly tečných
a normálových variací; generovaný koreper a kontrolu fyzikální torze;
úplný souřadnicový výpočet Ricciho tenzoru; nezávislé kontroly komplexních
matic při spinových a fázových transformacích; a nezávislé konečné diference
hustoty. Přesné kontroly používají SymPy, nezávislé numerické kontroly NumPy
a SciPy. Verze a hashe zdrojů jsou zaznamenány v protokolu.

Funkcionální derivování a argument s hladkým řetězovým pravidlem pro složenou
konexi jsou analytické důkazy, nikoli důsledky konečného vzorkování.
Formální status je `LEAN-PENDING`: v prověřeném prostředí chybí Lean i Lake
a není dodána zkompilovaná formalizace.

**OMEZENÁ PŘEKÁŽKA VÝBĚRU AKCE: PROVED [L1].**

**NEPODMÍNĚNÁ GRAVITACE UBT, KVANTOVÝ HESSIÁN A RH: OPEN.**

Kanonický registr tvrzení se nemění. Nový výsledek uzavírá tento přesný
test existující rodiny akcí; nezavádí nový dynamický axiom.
