

# Onderzoek raketreis
**Door: Maurits en Twan**

## **Inleiding (Twan)**
Het ruimtevaartbedrijf *SpaceX* is van plan om in de toekomst grote wereldreizen een stuk sneller te maken. Elon Musk is er namelijk van overtuigd dat reizen door de ruimte met behulp van een raket veel sneller is dan een normale vliegreis. Dat zetten ons aan het denken. Hoeveel verschil zal een reis door de ruimte eigenlijk maken? Daarom hebben wij gekozen voor de onderzoeksvraag: **Hoe snel kun je met een raket aan de andere kant van de wereld komen?**
## **Belangrijke krachten (Maurits)**
### **Gravitatiekracht** 
Gebruikte formule

𝐹𝑔=𝐺⋅𝑀𝑟𝑎𝑘𝑒𝑡⋅𝑀𝑎𝑎𝑟𝑑𝑒𝑟2

|Grootheid|Start waarde|Eenheid|Toelichting|
| :- | :- | :- | :- |
|Fg|0|Newton (N)|De gravitatiekracht in newton|
|G|6.67384 \* 10-11|Nm2/kg2|De gravitatie constante binas tabel 31A|
|Mraket|520.870|<p>Kilogram (kg)</p><p></p>|De massa van alle onderdelen van de raket samen|
|Maarde|5.972\*1024 |Kilogram (kg)|De massa van de aarde  binas tabel 31A|
|r|6,371 \* 106|Meter (m)|De afstand tussen de raket en het massamiddelpunt van de aarde|
### **Luchtweerstand**
Gebruikte formules

𝑔=𝐺⋅𝑀𝑎𝑎𝑟𝑑𝑒𝑟2

- g is de gravitatie versnelling in m/s2
- G is de gravitatie constante in Nm2/kg2
- Maarde is de massa van de aarde in kg
- r is de straal van de aarde + de hoogte ten opzichte van het aardoppervlak in m

𝑝=100⋅𝑝0⋅𝑒−𝑀⋅𝑔⋅h𝑅⋅𝑇

p0 wordt vermenigvuldigd met 100, omdat de eenheid hPa is en we Pa nodig hebben.

- p is de luchtdruk in Pa
- p0 is een constante 1013 hPa de druk op zeeniveau
- e is Eulers nummer (ongeveer 2,71)
- M = de molaire massa van lucht (0,02897 kg/mol)
- g = gravitatie versnelling in m/s2
- R = de gasconstante (8,314472)
- h is de hoogte in m
- T = de temperatuur in K

𝜌=𝑝⋅𝑀𝑅⋅𝑇

- p is de luchtdruk in Pa
- M = de molaire massa van lucht (0,02897 kg/mol)
- R = de gasconstante (8,314472)
- T = de temperatuur in K
## **Opstijgen (Maurits)**
### **Formules**
(Zie formules voor gravitatiekracht en luchtweerstand onder [‘Belangrijke krachten’](#_Belangrijke_krachten_\(Maurits\)))

### **Startwaardes**

|**Grootheid**|**Start waarde**|**Toelichting**|
| :- | :- | :- |
|Massa first stage brandstof (Mfirststage\_brandstof)|395.700 kg|Massa van de brandstof in de eerste stage van de raket (gevonden op: <https://www.spaceflightinsider.com/hangar/falcon-9/>)|
|Massa first stage (Mfirststage)|25.600 kg|Massa van het raket onderdeel zonder de brandstof van de eerste stage (gevonden op: <https://www.spaceflightinsider.com/hangar/falcon-9/>)|
|Massa second stage brandstof (Msecondstage\_brandstof)|92.670 kg|De massa van de brandstof van de tweede stage van de raket (gevonden op: <https://www.spaceflightinsider.com/hangar/falcon-9/>)|
|Massa second stage (Msecondstage)|3.900 kg|Massa van het raket onderdeel zonder de brandstof van de tweede stage. (gevonden op: <https://www.spaceflightinsider.com/hangar/falcon-9/>)|
|<p>Massa capsule</p><p>Mcapsule</p>|3.000 kg|Massa van de capsule van de raket (gevonden op: <https://www.spaceflightinsider.com/hangar/falcon-9/>)|
|Stuwkracht first stage (Fstuw\_firststage)|<p>7.607.000 N</p><p></p>|De stuwkracht van de eerste stage van de raket (gevonden op <https://www.spacex.com/>)|
|<p>Stuwkracht second stage (Fstuw\_secondstage)</p><p></p>|<p>981.000 N</p><p></p>|<p>De stuwkracht van de tweede stage van de raket (gevonden op <https://www.spacex.com/>)</p><p></p>|
|Burn rate first stage (burn\_rate\_first)|<p>1529.63 kg/s</p><p></p>|Het aantal brandstof dat de raket per seconde gebruikt als de eerste stage is geactiveerd. Berekend met de brandstof massa en de burn time.|
|Burn rate second stage (burn\_rate\_second)|233.425 kg/s|Het aantal brandstof dat de raket per seconde gebruikt als de tweede stage is geactiveerd. Berekend met de brandstof massa en de burn time|
|Hoogte (h)|0 m|De hoogte aan het begin|
|Snelheid (v)|0 m/s|De snelheid aan het begin|
|Temperatuur (T)|298 K|De temperatuur in kelvin|
|Oppervlak (area)|Pi \* 3.72  m2|Het frontaal oppervlak van de raket|
|Cw |0.82 |Luchtweerstandscoeficient van een cilinder lang volgens binas tabel 28A|
|Fnetto|0 N|` `De netto kracht aan het begin|
|Fstuw |Fstuw\_firststage  N|De stuwkracht is de stuwkracht van de eerste stage aan het begin|
|Burn\_rate|Burn\_rate\_first kg/s|Het aantal brandstof dat er per seconde wordt verbruikt|
|<h3>Mhuidige\_brandstof\_tank</h3>|Mfirststage\_brandstof kg|De brandstof tank die wordt gebruikt voor het produceren van de stuwkracht van de raket|
|Mraket|Mfirststage\_brandstof + Mfirststage + Msecondstage\_brandstof + Msecondstage + Mcapsule kg|De massa van de raket aan het begin is gelijk aan de massa van allen raket onderdelen|
|<h3>**Als dan**</h3>|<h3>**Action**</h3>|<h3>**Eenheid**</h3>|<h3>**omschrijving**</h3>|
|<h3>h >= 100.000 m</h3>|Mraket = Msecondstage + Msecondstage\_drandstof + Mcapsule|<h3>kg</h3>|<h3>Bij 100 km hoogte wordt de first stage weggedaan waardoor de massa van de raket die onderdelen niet meer meeneemt</h3>|
|h >= 100.000 m |<h3>Fstuw  = Fstuw\_secondstage</h3>|<h3>N</h3>|<h3>Bij 100 km wordt de first stage weggedaan en wordt de second stage motor aan gedaan en die heeft een andere stuwkracht</h3>|
|h >= 100.000m|Mhuidige\_brandstof\_tank = Msecondstage\_brandstof|<h3>kg</h3>|<h3>Het wisselen van de brandstof tank die wordt gebruikt van first stage naar second stage</h3>|
|<h3>h >= 100.000 m</h3>|Burn\_rate = burn\_rate\_second|<h3>kg/s</h3>|<h3>Bij 100 km hoogte wordt de motor van de second stage aangedaan en die heeft een andere burn rate dan de first stage raket motor</h3>|
### **Uitkomst**
We zijn bij het opstijgen van de raket ervanuit gegaan dat de raket een constante stuwkracht heeft en een constante massa afname. En dat de stuwkracht en massa afname veranderen als de raket 100 km heeft aflegt. We zijn er ook vanuit gegaan dat de raket recht omhoog opstijgt en dat de temperatuur constant is met een waarde van 298 Kelvin (25°C).

Op de grafiek hieronder kan je zien dat de massa van de raket heel erg afneemt op een hoogte van 100.000 meter dat komt doordat hij hier de first stage weg doet, maar op dit moment is de first stage ook nog niet leeg dus verliest de raket erg veel massa wat je weer terugziet in de grafiek. Bij de tweede grafiek hieronder kan je zien dat de massa eerst lineair afneemt over de tijd dit komt door de verbranding van de brandstof en op ongeveer 160 seconden neemt het erg af door dat de first stage wordt losgelaten op dat moment

In de grafiek hieronder zie je de netto kracht over de tijd. In deze grafiek zijn een paar aparte gebeurtenissen namelijk op ongeveer t = 50 hier is de luchtweerstand op zijn hoogste punt terwijl de snelheid wel nog blijft toenemen. In de grafiek (Fw over tijd) kan je zien dat de luchtweerstand het hoogst is op ongeveer t=50 en daarna afneemt dit komt doordat de hoogte zo hoog wordt dat de luchtdichtheid heel erg begint af te nemen en dat gaat veel sneller dan dat de luchtweerstand groter wordt door middel van de snelheid.

In de grafiek is ook te zien dat op ongeveer t=160 de grafiek erg daalt in netto kracht. Dat komt doordat de second stage hier activeert en die heeft minder stuwkracht dan de first stage. Door het loslaten van de second stage met nog veel brandstof neemt de gravitatiekracht ook erg af (wat je kan zien in de grafiek Fg over tijd), waardoor de verminderede stuwkracht wel nog genoeg kracht levert om te versnellen. En de luchtweerstand is verwaarloosbaar op dit moment, omdat de luchtdichtheid heel erg laag is.


Hierboven kan je in de grafiek (fg over tijd zien) dat de massa lineair afneemt dan opeens heel veel afneemt en dan weer lineair afneemt. Dit komt doordat de massa afname constant is tot op het punt van de grootte afname hier wordt de first stage weg gedaan waardoor er veel massa weggaat en daarna is het weer lineair, maar minder snel dalend, omdat de massa afname per seconden kleiner is dan daarvoor.

In de grafiek hieronder (snelheid over tijd) kan je zien dat de snelheid steeds sneller toeneemt tot op een bepaald punt waar de snelheid nog maar een klein beetje omhooggaat. Dit komt door het wegdoen van de eerste stage want de tweede stage heeft minder stuwkracht. 

### **Conclusie**
Aan het einde van het opstijgen van de raket is de snelheid ongeveer 1700 m/s. En het opstijgen duurde 228 seconden dat is 3 minuten en 48 seconden de uiteindelijke afstand die is afgelegd is 200 km. De massa van de raket is op het einde 82.342 kg dit is vooral de brandstof van de second stage die nog niet is gebruikt. 
## **Halve baan (Twan)**
### **Formules**
∆𝑥 = 𝜋⋅𝑟 (Niet 2π, omdat we uitgaan van een halve baan)

- Δx = verschil in afstand in m
- r = afstand van raket tot het massamiddelpunt van de aarde

Δ𝑡 =Δ𝑥𝑣

- Δt = verschil in tijd in s
- Δx = verschil in afstand in m
- v = snelheid in m/s

We zijn uitgegaan van een constante snelheid zodat we minder complexe simulaties hoefde te maken. Er is op 200km boven het aardoppervlak welleswaar nog een heel klein beetje luchtweerstand, maar dat is zo klein dat we dat hier voor het gemak hebben verwaarloosd. Deze snelheid hebben we gebaseerd om de eindsnelheid (op 200km hoogte) van onze simulatie bij het opstijgen van de raket. We hebben hierbij geen rekening gehouden met de hoek die de raket moet maken om in de baan te komen.
### **Startwaardes**

|**Grootheid**|**Waarde**|**Toelichting**|
| :- | :- | :- |
|Radius (r)|6,871⋅106 m|Radius aarde = 6,371⋅106 m (BiNaS 31) hoogte = 2⋅106 m (low earth orbit)|
|Snelheid (v)|1700 m/s|Eindsnelheid simulatie opstijgen|
### **Uitkomst**
∆𝑡=6,871⋅106 𝑚1700 𝑚𝑠−1=4042 𝑠
### **Conclusie**
Een halve baan om de aarde met een constante snelheid van 1700m/s duurt 4042 seconden ofwel 1 uur en 7 minuten.


## **Landing (Twan)**
### **Formules**
(Zie formules voor gravitatiekracht en luchtweerstand onder [‘Belangrijke krachten’](#_Belangrijke_krachten_\(Maurits\)))

𝑎 = 𝜋⋅𝑟2

- a = oppervlakte in m2 (nodig voor het berekenen van de luchtweerstand)
- r = radius raket (of parachute) in m
### **Startwaardes** 
We zijn uitgegaan bij de landing met een raket die vanuit stilstand recht naar beneden valt en op 5km hoogte een parachute uitklapt. In werkelijkheid gebruiken raketten vaak meerdere parachutes, maar wij hebben voor het gemak 1 grote parachute gekozen. 

*SpaceX* raketten staan er om bekent om op motorkracht helemaal tot stilstand te komen. We konden hier helaas niet genoeg data over vinden, dus we zijn uitgegaan van een parachute landing van de capsule.

|**Grootheid**|**Startwaarde**|**Toelichting**|
| :- | :- | :- |
|Hoogte (h)|200.000m|De raket valt van deze hoogte naar beneden|
|Snelheid (v)|0 m/s|Door de raket recht naar beneden te laten landen, moet de raket volledig uit de baan ontsnappen door af te remmen tot 0 m/s|
|Massa raket (Mraket)|3000kg|Alleen de capsule blijft over. We zijn uitgegaan van de massa van de *Falcon 9* capsule.|
|Radius raket (Rraket)|3,7 m|Van *Falcon 9* raket (gevonden op <https://www.spacex.com/>)|
|Radius Parachute (Rparachute)|25 m|<p>We konden hier niet veel over vinden, dus we hebben deze waarde geschat. (Normaal worden er meerder parachutes gebruikt)</p><p></p>|
|Cw Raket|0,82|“Cilinder lang” (BiNaS 28A)|
|Cw Parachute|1,5|“Uit panelen opgebouwde bolvormige parachute” (<https://drra.eu/daalsnelheid-parachute/>) |
|Uitklaphoogte parachute|5000m|Geschatte waarde.|
### **Uitkomst**

Je ziet dat zonder parachute door de luchtweerstand de snelheid afneemt rond de 25km hoogte. Dit komt omdat de luchtdichtheid steeds groter wordt naarmate de raket dichter bij de grond komt. Hierdoor neemt de weerstand toe (te zien in de afbeelding hieronder). De remmende werking van de luchtweerstand is natuurlijk nog niet genoeg om de raket te landen. Zonder parachute is de eindsnelheid 38 m/s (137 km/h). Een landing op deze snelheid zullen de inzittende waarschijnlijk niet overleven. Met het uitklappen van een parachute op 5km hoogte kan de eindsnelheid afnemen tot 4,1 m/s (15 km/h). Dit is een vergelijkbare snelheid met landingen die ik op internet kon vinden. De eindtijd van de landing met parachute is 1518 seconden, ofwel 25 minuten.

Hier onder staat de luchtweestand en gravitatiekracht bij een landing met parachute afgebeeld. In de weerstandsgrafiek van het landen met parachute is bijna niet meer de remkracht door luchtweerstand te zien, zoals op de grafiek hierboven, maar alleen nog een klein bobbeltje op t=200.  Dit komt door de enorme toename van de weerstand bij het uitklappen van de parachute op t=460. Deze kracht is overdreven groot, omdat de gigantische parachute in 1 keer wordt uitgeklapt. In het echt duurt het even voordat de hele parachute is uitgeklapt en zal deze kracht zich dus verspreiden over een langere periode. 

De gravitatiekracht (rechts) is te verklaren door de hoogte-tijd grafiek nog eens te bekijken. Hoe dichter de raket bij de grond komt, hoe hoger de gravitatiekracht.

Tot slot de snelheids-tijd grafiek (hieronder), waarbij je goed kunt zien dat de snelheid afneemt door luchtweerstand rond t=200 en op t=460 een sprongetje maakt naar een lagere snelheid door het uitklappen van de parachute.
### **Conclusie**
Het kost 1518 seconden (25 minuten) om een capsule van 3.000kg te laten landen door middel van een parachute met een eindsnelheid van 4,1 m/s.


## **Conclusie (Twan)**
Wij hebben met onze simulatie een idee gekregen van hoeveel tijd het zou kosten om met een raket aan de andere kant van de wereld te komen. Over land is deze afstand 20.015 km, de raket vliegt 200km boven het aardoppervlak en reist daardoor 21.043 km. De raket doet er 228 seconden over om op 200km hoogte te komen. Het kost 4042 seconden (1 uur en 7 minuten) voor de raket om een halve baan om de aarde te maken. En de raket heeft 1518 seconden (25 minuten) nodig om weer op aarde te landen.

|**Fase**|**Tijd**|
| :- | :- |
|Opstijgen|228 seconden (3 minuten en 48 seconden)|
|Halve baan|4042 seconden (1 uur en 7 minuten)|
|Landen|1518 seconden (25 minuten)|
|Totaal|5788 seconden (1 uur, 36 minuten en 28 seconden)|

Het is dus mogelijk om met een raket aan de andere kant van de wereld te komen in iets meer dan anderhalf uur. Volgens <https://www.distance.to/> duurt een vergelijkbare vliegreis van Amsterdam naar Wellington (Nieuw-Zeeland) van rond de 19.000km over land en zee ongeveer 22 uur en 20 minuten. Je bent dus met een raket 14 keer sneller op je eindbestemming dan met het vliegtuig. Dus als geld en klimaatopwarming geen rol speelt, maakt een raketreis een enorm verschil in reistijd voor een reis naar de andere kant van de wereld.

We hebben onze simulaties gemaakt in de programmeertaal *Python.* Je kunt onze code die we hebben gemaakt voor deze al onze simulaties bekijken op: <https://github.com/Mauritshidde/raket-landing-simulatie> 
