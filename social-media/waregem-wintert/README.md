# CCW-chalet op Waregem Wintert: zaterdag 5 december 2026

**Doel:** zoveel mogelijk volk naar onze chalet aan de ijspiste op de Markt, en van die bezoekers
zoveel mogelijk volgers en nieuwe renners maken.

**Voorstel van mikpunten:** 150 mensen persoonlijk uitgenodigd, 100 nieuwe volgers op Instagram,
10 mensen die willen meerijden.

## Wat het meeste volk oplevert

1. **Leden nodigen persoonlijk uit.** 30 renners die elk 5 mensen een berichtje sturen, dat is 150
   persoonlijke uitnodigingen. Niets werkt beter dan "kom je ook, ik sta er?".
2. **Een Facebook-evenement** met de Lamett Classic-pagina als medeorganisator, zodat de bestaande
   volgers het meteen zien. Facebook herinnert iedereen die op "Geïnteresseerd" klikt.
3. **Affiches bij de sponsors, in De Karekiet en bij Velo Fane** (daar komen de fietsers).
4. **Sponsors en bevriende wielerclubs uitnodigen.** Een ploeg die na de zaterdagrit langskomt, vult meteen de toog.
5. **Zichtbaar zijn op de dag zelf**: in clubkledij, met stories doorheen de dag en de toogkaart met QR-code.

## Materiaal

De gekozen ontwerpen staan in `v2/`: het gezellige kerstontwerp met een koersfiets vol kerstlichtjes, een
kersttrui-boord met fietsjes, een gouden "Elk uur happy hour!"-sticker naast de fiets en een gouden regel over de
wedstrijd. De sticker en de wedstrijdregel haal je weg met `HAPPY = None` en `CONTEST = None` bovenaan `generate.py`. Het eerste, strakkere ontwerp staat nog in `v1/`.

| Bestand in `v2/` | Gebruik |
|---|---|
| `affiche-a3.pdf` | Om af te drukken. A3 voor uitstalramen; A4 kan ook (zelfde verhouding). Een gewone printer laat een witte rand; een drukkerij drukt tot aan de rand. |
| `affiche.png` | Om door te sturen via WhatsApp en mail |
| `post-instagram.png` | Post voor Instagram en Facebook (1080×1350) |
| `story-instagram.png` | Story voor Instagram en Facebook (1080×1920) |
| `facebook-evenement.png` | Omslagfoto van het Facebook-evenement (1920×1005) |
| `video-story.mp4` | Geanimeerde versie voor stories en reels (1080×1920, 8 seconden, loopt naadloos): voor de advertenties |
| `video-post.mp4` | Geanimeerde versie voor de feed (1080×1350, 8 seconden) |
| `drankkaart-instagram.png` | "Wat schenken we?": de drankkaart als post voor Instagram en Facebook (1080×1350). Nog voorlopig: wordt bijgewerkt zodra de kaart en de prijzen vastliggen. |
| `toogkaart-a4.pdf`, `toogkaart.png` | Op de toog van de chalet: "Zin om mee te fietsen?" met een QR-code naar "Rij eens mee" |
| `generate.py` | Maakt alles opnieuw na een wijziging (uren, aanbod…). Bovenaan staan de gegevens. De video's maak je met het extra argument `video` (een paar minuten); daarvoor gebruikt het `capture.mjs` en `encode.swift`. |

De website kondigt de chalet ook aan, bovenaan cyclingclubwaregem.be. Die aankondiging verdwijnt vanzelf na 5 december.

## Eerst te bevestigen

- [x] **Openingsuren:** van 9.30 tot 22 uur. Let op: volgens de stad gaan de chalets open om 10 uur en krijg je de
      sleutel pas vanaf 9.30 uur. Zorg dus dat alles klaarstaat om meteen te schenken (de soep al warm in een
      thermoskan), of vraag de stad of je de sleutel wat vroeger kunt krijgen.
- [ ] **Definitieve drankkaart** (volgt nog, samen met de prijzen). Voorlopig gaan we uit van de lijst van vorig jaar:
      - Jenever: dreupel of fles, en de smaken appel, vanille, choco en chocoretto
      - Warm: verse soep en warme choco
      - Cava, rosé, pils, cola (zero), spuitwater en plat water
      - Om te knabbelen: een partymix van frituurhapjes
- [ ] **Prijzen.** De stad legt minimumprijzen op: pils € 1,50, frisdrank € 1,25, cava € 2, warme dranken € 1,50.
- [ ] **Betalen:** cash en Payconiq? Zet de QR-code van Payconiq goed zichtbaar op de toog.
- [ ] **Happy hours:** welke actie in welk uur? Zie het voorstel onder "Happy hours".

## Regels van de stad

Uit [de chaletpagina van Waregem Wintert](https://www.waregem.be/waregemwintert/winterchalets):

- **Uren:** de chalets zijn open van 10 tot 22 uur. De sleutel haal je vanaf 9.30 uur bij de schaatsverhuur.
  Om 22 uur is het echt gedaan; de sleutel gaat dan naar de security.
- **Leeftijd:** bier en wijn vanaf 16 jaar, **sterke drank (dus jenever) pas vanaf 18 jaar.** Vraag bij twijfel een identiteitskaart.
- **Geen glas en geen wegwerp.** Herbruikbare bekers zijn verplicht voor alle dranken, **ook voor de jenever**:
  dus herbruikbare shotbekertjes, geen glaasjes. Te huren bij WerkPlus of IMOG. Warme dranken en borden
  (de soep en het hapje) mogen in biologisch afbreekbaar materiaal.
- **Elektriciteit:** maximaal 3000 watt; geen gas, open vuur of verwarming. Een airfryer (1500 à 2000 W), een
  soepketel en iets om de choco warm te maken gaan samen zeker over die grens. Maak de soep en de warme choco
  thuis en houd ze warm in pompthermossen; dan heeft de airfryer het stopcontact voor zich alleen.
- **Fles jenever:** een glazen fles mag niet naar de tafels onder de tent. Vraag de stad hoe dat kan
  (de fles in de chalet houden en uitschenken in herbruikbare shotbekertjes), of verkoop "een fles" als een plateau dreupels.
- **Geen reclame voor handelszaken aan de chalet.** Laat het sponsordoek dus thuis. De sponsors bedanken kan wel op sociale media.
- **Muziek** regelt de stad: onder de hele tent speelt dezelfde muziek.
- **Zelf meebrengen:** afwasgerief (bassin, product, sponzen, handdoeken) en vuilzakken. Al het afval neem je zelf mee.
- **Roken** is verboden aan de chalets.

**De andere chalets:** die dag baten drie andere verenigingen ook een chalet uit. Via ijspiste@waregem.be
of 056 62 13 92 krijg je hun contactgegevens. Spreek af wie wat schenkt: als iedereen jenever heeft, valt ons aanbod minder op.

## Waarom 5 december een goeie dag is

- **Het is de eerste zaterdag van Waregem Wintert.** De ijspiste opent op vrijdag 4 december, dus alles is nieuw en het centrum loopt vol.
- **Kinderen op het ijs, ouders aan de kant.** Op zaterdag is er van 10 tot 12 uur schaatsgewenning voor kinderen
  en vanaf 12 uur discoschaatsen. Ons haakje voor de ouders: *een soepje of een druppel terwijl de kinderen schaatsen.*
- **De zaterdagmarkt staat vlakbij, op de Zuiderpromenade.** De stad trakteert er die dag zelf op gratis soep.
  's Ochtends zetten we dus beter de jenever in de verf dan de soep.
- **Het is Sinterklaasavond.** De chocojenever en de warme choco passen daar perfect bij: zet ze die dag in de kijker.

## Boodschap

**Kern:** *Tijd voor de bevoorrading! Jenever, verse soep, warme choco en hapjes aan de chalet van de wielerclub.
Elk uur een andere happy hour, en het laatste uur wordt het helemaal zot. Zaterdag 5 december, aan de ijspiste op de Markt.*

Elke fietser kent de bevoorrading van een toertocht: de stop waar soep en een drankje klaarstaan. Zo zie je meteen
dat er een wielerclub achter de chalet zit, en wie niet fietst, snapt toch dat er iets te eten en te drinken is.

| Wie | Haakje | Kanaal |
|---|---|---|
| Familie, vrienden en collega's van leden | "Kom de club eens zien, ik sta er ook" | WhatsApp, persoonlijk |
| Ouders van schaatsende kinderen | "Een soepje of een druppel terwijl de kinderen schaatsen" | Affiches in het centrum, Facebook |
| Fietsers uit de streek | "Leer de club kennen, rij 3× gratis mee" | Instagram, Velo Fane, bevriende clubs |
| Volgers van de Lamett Classic | "De club achter de Lamett Classic" | Facebook en Instagram van de Lamett Classic |
| Sponsors | "Kom een glas drinken, wij trakteren" | Persoonlijke uitnodiging |

## Happy hours (voorstel)

Elk uur een andere actie, telkens ingeluid met een **fietsbel**. Een krijtbordje aan de chalet toont de actie van het
moment, en elk uur komt er een story op Instagram: zo hebben de volgers een reden om (nog eens) langs te komen.
Vooraf verklappen we alleen het idee en het laatste uur; de rest is elk uur een verrassing.

| Uur | Naam | Actie |
|---|---|---|
| 9.30–11 | De vroege vlucht | Bij elke soep of warme choco een gratis hapje: voor de marktgangers en de ouders van de schaatsertjes |
| 11–12 | De bevoorrading | Soep met een portie hapjes samen aan een voordeelprijs |
| 12–13 | De tussensprint | Na het belsignaal krijgen de eerste 10 bestellingen een gratis hapje |
| 13–14 | Sinterklaasuur | Bij elke choco, warm of als jenever, een chocolademuntje of een speculaasje: het is Sinterklaasavond |
| 14–15 | Volg de kopman | Toon dat je @cyclingclubwaregem volgt op Instagram en krijg een gratis hapje |
| 15–16 | De waaier | Groepsdeal vanaf 4 personen: een plateau dreupels met een portie hapjes aan een groepsprijs |
| 16–17 | De bergprijs | De smaakjes (appel, vanille, choco, chocoretto) aan de prijs van een gewone dreupel |
| 17–18 | De gele trui | In fietskledij, met een fluohesje of in de clubjas? Een gratis hapje bij je bestelling |
| 18–19 | De ploegentijdrit | Drie smaakjes naast elkaar op een plankje, aan een vaste prijs |
| 19–20 | Het kersttruiklassement | In een kersttrui of met een kerstmuts? Een chocolademuntje bij elke bestelling, en een foto voor onze story |
| 20–21 | De rode vod | De laatste kilometer: wie een fles jenever neemt voor de groep, krijgt er een portie hapjes bij |
| 21–22 | **De massasprint** | Het zotste uur van de dag (zie hieronder) |

**De massasprint (21–22 uur): het zotste uur**
- **Elke 10 minuten de fietsbel**, met telkens een flitsactie die pas dan bekend wordt
- **Het rad van fortuin**: bij elke bestelling één keer draaien. Prijzen: een gratis hapje, een chocolademuntje,
  een CCW-sticker, en als hoofdprijs een fles jenever
- **Om 21.15 uur de winnaar van de wedstrijd**: wie wint de 2 inschrijvingen voor de Lamett Classic 2027? (zie "Wedstrijd")
- **Iedereen achter de toog in kerstpak** of met een kerstmuts
- **Om 21.30 uur de verkiezing** van de zotste kerstmuts of de foutste kersttrui: de winnaar krijgt een plateau dreupels voor de hele groep
- **Om 21.55 uur de finishfoto**: iedereen aan de chalet klinkt samen op de club, en wij filmen het voor Instagram

**Spelregels**
- De minimumprijzen van de stad gelden ook tijdens de happy hours (pils € 1,50, frisdrank € 1,25, cava € 2,
  warme dranken € 1,50). Geef daarom liever iets extra, zoals een hapje of een chocolaatje, dan dat je de prijs verlaagt.
- Bier en wijn pas vanaf 16 jaar, sterke drank pas vanaf 18: ook bij de acties, het rad van fortuin en de verkiezing.
- Eén actie per uur, duidelijk op het krijtbordje, zodat de shift niet moet nadenken.
- Vraag de stad of happy hours mogen (de vraag staat in de mail hieronder).

## Wedstrijd: win 2 inschrijvingen voor de Lamett Classic 2027 (voorstel)

Staat ook op de affiche. Zo zien we het verlopen:

- **Meedoen kan enkel online, via de QR-code aan de chalet**, zodat het een reden is om langs te komen. Het kaartje op de
  toog heeft een QR-code naar een kort Google Formulier (in het Google-account van de club): naam, e-mailadres en de
  schiftingsvraag. Gratis, zonder aankoop, één keer per persoon.
- **De schiftingsvraag:** "Hoeveel fietsers reden de laatste Lamett Classic?" Wie het dichtst bij het juiste aantal zit,
  wint. Bij gelijke stand wint wie het eerst meedeed.
- **Meedoen kan tot 21 uur. Om 21.15 uur, midden in de massasprint, maken we de winnaar bekend** aan de chalet.
  Is de winnaar er niet, dan krijgt die een mail. Op Instagram en Facebook noemen we enkel de voornaam, en alleen als
  de winnaar dat goedvindt.
- **Privacy:** op het formulier staat waarvoor we de gegevens gebruiken. Wie nieuws over de Lamett Classic en de club
  wil, vinkt dat zelf aan in een apart vakje dat standaard leeg staat. De gegevens van de anderen wissen we na de wedstrijd.
- **Wat het oplevert:** een lijst mensen uit de buurt die interesse hebben in de Lamett Classic. Zodra de inschrijvingen
  openen, krijgen zij een mail: een stap richting 1000 deelnemers.

Nog te regelen:
- [ ] Bevestigen dat we 2 gratis inschrijvingen kunnen geven, en hoe: een kortingscode, of zelf inschrijven via het inschrijvingsplatform
- [ ] Het Google Formulier maken (tekst hieronder) en de link doorgeven, zodat het kaartje met de QR-code gemaakt kan worden
- [ ] Het juiste antwoord op de schiftingsvraag opzoeken

### Het formulier

Maak het aan in het Google-account van de club, met deze instellingen:
- *E-mailadressen verzamelen: ingevoerd door respondent*. Dan vraagt Google zelf het e-mailadres en controleert het of het
  een geldig adres is.
- Inloggen met Google laat je uit, zodat iedereen snel kan meedoen.

**Titel:** Win 2 inschrijvingen voor de Lamett Classic 2027

**Beschrijving**
```
Doe mee aan de wedstrijd van Cycling Club Waregem op Waregem Wintert, zaterdag 5 december 2026.
Wie het dichtst bij het juiste antwoord op de schiftingsvraag zit, wint 2 inschrijvingen voor de Lamett Classic 2027.
Meedoen kan tot 21 uur. Om 21.15 uur maken we de winnaar bekend aan onze chalet aan de ijspiste.
```

**Vragen**
1. *Voornaam*: kort antwoord, verplicht
2. *Achternaam*: kort antwoord, verplicht
3. *Hoeveel fietsers reden de laatste Lamett Classic?*: kort antwoord, verplicht, met de validatie *Getal → Geheel getal*
4. *Nieuws ontvangen?*: selectievakje, niet verplicht:
   "Ja, stuur me nieuws over de Lamett Classic en Cycling Club Waregem, bijvoorbeeld wanneer de inschrijvingen openen."
5. *Akkoord*: selectievakje, verplicht:
   "Ik ben minstens 18 jaar en ga akkoord met het wedstrijdreglement en de privacyverklaring hieronder."

**Wedstrijdreglement en privacy** (als tekstblok onderaan het formulier)
```
Wedstrijdreglement
- Organisator: Cycling Club Waregem. Meedoen is gratis en zonder aankoopverplichting, één keer per persoon, vanaf 18 jaar.
  Bestuursleden van de club doen niet mee.
- Meedoen kan tot zaterdag 5 december 2026 om 21 uur.
- Wie het dichtst bij het juiste antwoord zit, wint. Bij gelijke stand wint wie het eerst meedeed.
- De prijs: 2 inschrijvingen voor de Lamett Classic 2027. De prijs is niet inwisselbaar voor geld.
- We maken de winnaar op 5 december om 21.15 uur bekend aan onze chalet en sturen de winnaar een mail.
  Op sociale media noemen we enkel de voornaam, en alleen als de winnaar dat goedvindt.

Privacy
Cycling Club Waregem gebruikt je naam en e-mailadres alleen voor deze wedstrijd: om de winnaar te bepalen en te
contacteren. Vink je aan dat je nieuws wilt, dan mailen we je ook over de Lamett Classic en de club; uitschrijven kan
altijd. De gegevens van wie geen nieuws wil, wissen we uiterlijk op 31 december 2026.
Je gegevens inkijken, verbeteren of laten wissen? Mail naar info@cyclingclubwaregem.be.
```

**Bevestiging na het verzenden**
```
Bedankt, je doet mee! Om 21.15 uur maken we de winnaar bekend aan onze chalet.
Ondertussen: tijd voor de bevoorrading! 🥃
```

**De winnaar vinden**
- Om 21 uur zet iemand het formulier op *Reacties niet meer accepteren*.
- Open de reacties in een Google Sheet. De kolommen zijn dan: tijdstip, e-mailadres, voornaam, achternaam, schiftingsvraag.
  Zet in een lege kolom `=ABS(E2-600)`, met het juiste aantal in plaats van 600, en trek de formule door.
- Sorteer op die kolom en daarna op tijdstip: bovenaan staat de winnaar.
- Deed iemand twee keer mee (zelfde e-mailadres), dan telt enkel de eerste deelname.

## Advertenties (Facebook en Instagram)

- **Nu:** het advertentieaccount instellen in Meta Business Suite. Heeft de club geen btw-nummer, dan rekent Meta 21 % btw
  bovenop het budget. Besteed alvast een klein deel (± 20 %) aan het promoten van het Facebook-evenement, gericht op
  "Geïnteresseerd": wie dat aanklikt, krijgt vanzelf herinneringen van Facebook.
- **De laatste week (28/11 tot 5/12):** de rest, met het meeste van donderdag 3 tot zaterdag 5 december, en op de dag zelf
  tot in de vooravond. Gebruik `video-story.mp4` voor stories en reels, en `video-post.mp4` voor de feed.
- **Instellingen:** minimumleeftijd 18 jaar (de advertentie noemt jenever), een straal van ± 15 km rond de Markt, en verder
  een breed publiek.
- **De boodschap:** de chalet, de datum, soep en warme choco, en de Lamett-wedstrijd. Maak happy hours of jenever niet de
  haak van de advertentie.
- **Meten:** bereik en "Geïnteresseerd" op Facebook, en op de dag zelf vragen hoe mensen van de chalet hoorden
  (turven op het krijtbordje).

## Planning

### Deze week (tot 15/11): voorbereiden

- [ ] De punten onder "Eerst te bevestigen" afvinken
- [ ] De stad mailen (tekst hieronder): de andere chalets, en de vraag om CCW te vermelden in hun communicatie
- [ ] Herbruikbare bekers en shotbekertjes reserveren
- [ ] Shiftenlijst opmaken, bijvoorbeeld 5 shiften van 2,5 uur (vanaf 9.30, 12, 14.30, 17 en 19.30 uur) met telkens
      3 mensen, plus iemand die om 9.30 uur de sleutel haalt
- [ ] Affiches laten drukken (A3 voor uitstalramen, A4 voor prikborden)
- [ ] De happy hours kiezen (voorstel hierboven), en in de mail aan de stad vragen of dat mag
- [ ] Het advertentieaccount instellen en het Facebook-evenement promoten (zie "Advertenties")

### 16/11 tot 22/11: aankondigen

- [ ] **Facebook-evenement** op de CCW-pagina, met `facebook-evenement.png` als omslagfoto en de Lamett Classic-pagina
      als medeorganisator. Leden klikken op "Gaat" en nodigen hun vrienden uit.
- [ ] **Instagram:** `post-instagram.png` als Collab-post met @_lamettclassic
- [ ] **WhatsApp:** affiche in de clubgroep, met de vraag om ze naar 5 mensen door te sturen (tekst hieronder)
- [ ] **Affiches ophangen:** De Karekiet, alle sponsors, Velo Fane, bakker, frituur, sporthal, bib, en op het werk van leden
- [ ] **Sponsors** persoonlijk uitnodigen (tekst hieronder)
- [ ] De activiteit gratis invoeren op [uitdatabank.be](https://www.uitdatabank.be): ze verschijnt dan op uitinvlaanderen.be
      en vaak ook in de agenda's van stad en regio

### 23/11 tot 29/11: warm maken

- [ ] Post **"Wat schenken we?"** zodra de kaart vastligt: `drankkaart-instagram.png` (bijgewerkt), eventueel samen met
      een foto van de jeneverflessen op een rij
- [ ] Story of reel van de soep in de maak. Wie is onze soepchef?
- [ ] **Bevriende wielerclubs** uitnodigen om na hun zaterdagrit langs te komen
- [ ] **Lokale pers:** het korte bericht hieronder, met de affiche, naar Krant van West-Vlaanderen, Het Nieuwsblad en HLN (regio Waregem)

### 30/11 tot 4/12: laatste week

- [ ] Instagram-story met een **aftelsticker**: volgers kunnen daarmee een herinnering instellen
- [ ] Herinnering in de WhatsApp-groep en in het Facebook-evenement ("nog 3 dagen!")
- [ ] **Teaser** van het laatste uur, de massasprint (tekst hieronder)
- [ ] **Advertenties** met de video's, vooral van donderdag 3 tot zaterdag 5 december (zie "Advertenties")
- [ ] **Vrijdag 4/12, opening van de ijspiste** (16 uur dj, 19 uur kunstschaatsshow): ga met een paar leden kijken
      en deel kaartjes uit met "Morgen staan wij hier!". Vraag de stad even of dat mag.
- [ ] Alles klaarzetten: wisselgeld, Payconiq-QR, prijsbord, toogkaart, bekers, afwasgerief, verlengkabel,
      en voor de happy hours een fietsbel, een krijtbordje, chocolademuntjes en het rad van fortuin

### Zaterdag 5/12: de dag zelf

- [ ] Iedereen achter de toog in **clubkledij**, zodat de mensen zien wie we zijn
- [ ] Clublogo of clubvlag aan de chalet (geen sponsorlogo's)
- [ ] **Toogkaart** goed zichtbaar. Vertel actief over de club, zeker aan wie zelf fietst.
- [ ] **Stories** doorheen de dag: opbouw, eerste soep, sfeer op het ijs, groepsfoto 's avonds, en elk uur de happy hour
      van dat moment ("Nu aan de chalet: de waaier!")
- [ ] De **wedstrijd** voor de Lamett Classic 2027 (zie "Wedstrijd"): het kaartje met de QR-code op de toog, om 21 uur
      het formulier sluiten en om 21.15 uur de winnaar bekendmaken
- [ ] Hou bij wat er verkocht wordt (soep, jenevers, hapjes, pintjes): handig voor volgend jaar

### Na afloop (6/12 tot 12/12)

- [ ] **Bedankpost** met de beste foto's
- [ ] Wie wil meerijden, krijgt binnen de week een berichtje met de eerstvolgende rit
- [ ] Zodra de inschrijvingen voor de Lamett Classic 2027 openen: een mail aan de deelnemers van de wedstrijd die nieuws wilden
- [ ] Korte evaluatie met het bestuur: wat werkte, wat doen we anders volgend jaar?

## Teksten

**WhatsApp-bericht dat leden kunnen doorsturen**
```
Zaterdag 5 december staat onze wielerclub met een chalet aan de ijspiste op de Markt (Waregem Wintert) 🎄⛸️
Tijd voor de bevoorrading: jenever, verse soep, warme choco en hapjes. Van 9.30 tot 22 uur, iedereen welkom!
Elk uur een andere happy hour, en het laatste uur wordt het helemaal zot 🔔
Kom zeker eens langs, ik sta er ook 🍻
```

**Facebook-evenement**
- Naam: `Tijd voor de bevoorrading! CCW-chalet op Waregem Wintert`
- Datum: zaterdag 5 december 2026, 9.30 tot 22.00 uur. Locatie: Markt, 8790 Waregem
```
Op zaterdag 5 december baat Cycling Club Waregem een van de winterchalets aan de ijspiste op de Markt uit.

🥃 Verschillende jenevers
🍲 Verse soep
☕ Warme choco
🍟 Warme hapjes
🔔 Elk uur een andere happy hour, en het laatste uur wordt het helemaal zot!
🎁 Win 2 inschrijvingen voor de Lamett Classic 2027: meedoen kan aan de chalet

Tijd voor de bevoorrading! Kom langs na het schaatsen, terwijl de kinderen hun toeren draaien, of gewoon voor de ambiance.
Goesting om volgend seizoen mee te fietsen? Kom gerust een babbeltje doen: je mag 3 keer gratis meerijden.

Iedereen welkom!
```

**Instagram: aankondiging** (Collab met @_lamettclassic, bij `post-instagram.png`)
```
Save the date! 🎄
Op zaterdag 5 december staan we met de club in een chalet aan de ijspiste op de Markt, tijdens Waregem Wintert.
Tijd voor de bevoorrading: een jenever, verse soep, warme choco of een hapje. Van 9.30 tot 22 uur, iedereen welkom!
Elk uur een andere happy hour 🔔 en het laatste uur wordt het helemaal zot.
Bovendien kun je aan de chalet 2 inschrijvingen winnen voor de Lamett Classic 2027 🎁

#cyclingclubwaregem #waregemwintert #waregem #ijspiste
```

**Delen met je persoonlijke account** (voor alle leden: bij het delen van het Facebook-evenement of de post)
```
Zaterdag 5 december staat onze wielerclub, Cycling Club Waregem, met een chalet aan de ijspiste op de Markt, en ik sta er ook 🎄🚴
Kom gerust langs voor een jenever, verse soep of een warme choco. Elk uur is er een andere happy hour, en het laatste uur wordt het helemaal zot!
Je kan er bovendien 2 inschrijvingen voor de Lamett Classic 2027 winnen 🎁
Van 9.30 tot 22 uur. Hopelijk tot dan! 🍻
```
Voor een Instagram-story, met een linksticker naar het evenement:
```
5/12 sta ik aan onze chalet op Waregem Wintert 🎄
Kom je een dreupel drinken? 🥃 @cyclingclubwaregem
```

**Delen met het account van de Lamett Classic**

Facebook (het evenement delen, of de affiche posten):
```
Wie de Lamett Classic reed, kent de bevoorrading 😉
Op zaterdag 5 december staat Cycling Club Waregem, de club achter de Lamett Classic, met een chalet aan de ijspiste
op de Markt in Waregem.
🥃 Jenever, verse soep, warme choco en hapjes
🔔 Elk uur een andere happy hour
🎁 Win er 2 inschrijvingen voor de Lamett Classic 2027!
Van 9.30 tot 22 uur, iedereen welkom.
Volg ook de club zelf: Cycling Club Waregem op Facebook en @cyclingclubwaregem op Instagram.
```
Instagram: de Collab-post verschijnt al vanzelf op het profiel van de Lamett Classic. Deel hem daarnaast in de story:
```
Win 2 inschrijvingen voor de Lamett Classic 2027 🎁
Enkel aan de chalet van @cyclingclubwaregem, zaterdag 5/12 op Waregem Wintert 🎄
```

**Teaser voor het laatste uur** (story of post in de laatste week)
```
Elk uur een andere happy hour aan onze chalet 🔔
Maar om 21 uur start de massasprint: het zotste uur van de dag. Meer verklappen we niet 🏁
Zaterdag 5 december, aan de ijspiste op de Markt.
```

**Instagram: "Wat schenken we?"** (bij `drankkaart-instagram.png`; pas aan zodra de definitieve kaart er is)
```
Goesting in een dreupel? 🥃
Op 5 december schenken we jenever per dreupel of per fles, en in de smaken appel, vanille, choco en chocoretto.
En omdat het Sinterklaasavond is, mag de choco zeker niet ontbreken 🎁
Liever iets anders? Verse soep, warme choco, cava, rosé, pils en frisdrank staan ook klaar,
en voor de kleine honger is er een partymix van frituurhapjes 🍟
Zaterdag 5 december, 9.30 tot 22 uur, aan de ijspiste op de Markt.
```

**Uitnodiging voor de sponsors**
```
Dag [naam],

Op zaterdag 5 december baat Cycling Club Waregem een chalet uit aan de ijspiste op de Markt (Waregem Wintert).
Als dank voor je steun trakteren we je graag op een drankje: kom gerust langs tussen 9.30 en 22 uur, met collega's of familie.

Mogen we je ook vragen om onze affiche (in bijlage) op te hangen in je zaak, of te delen op jullie sociale media?
Daar zou je de club enorm mee helpen.

Sportieve groeten,
[naam], Cycling Club Waregem
```

**Mail aan de stad** (naar ijspiste@waregem.be)
```
Onderwerp: Chalet Waregem Wintert 5 december - Cycling Club Waregem

Beste,

Cycling Club Waregem baat op zaterdag 5 december een chalet uit tijdens Waregem Wintert.
Mogen we de contactgegevens van de andere verenigingen die die dag een chalet uitbaten? Dan stemmen we ons aanbod op elkaar af.

Nog enkele vraagjes:
- We willen om 9.30 uur openen. Kunnen we de sleutel iets vroeger ophalen om alles klaar te zetten?
- Mogen we in de chalet uitschenken uit glazen flessen (jenever, cava, rosé), als er enkel herbruikbare bekers naar
  buiten gaan? En hoe pakken we het aan als een groep een fles jenever wil?
- We willen elk uur een andere happy hour doen, zonder onder de minimumprijzen te gaan. Is dat in orde?
- Kan Cycling Club Waregem vermeld worden in jullie communicatie over de chalets? Onze affiche zit in bijlage.

Alvast bedankt!
[naam], Cycling Club Waregem
```

**Kort bericht voor de lokale pers**
```
Bevoorrading bij de wielerclub op Waregem Wintert

Op zaterdag 5 december baat Cycling Club Waregem (CCW), de recreatieve wielerclub achter de Lamett Classic,
een winterchalet uit aan de ijspiste op de Markt. Van 9.30 tot 22 uur schenkt de club verschillende jenevers,
verse soep en warme choco, met warme hapjes erbij. Elk uur is er een andere happy hour, met om 21 uur
als afsluiter "de massasprint".
CCW telt een 30-tal actieve renners en rijdt elke zondag in twee groepen vanuit Eetcafé De Karekiet.
Wie de club wil leren kennen, is welkom aan de chalet: nieuwe renners mogen drie keer gratis meerijden.
Meer info: cyclingclubwaregem.be
```

**Bedankpost**
```
Merci Waregem! 🙏
Wat een ambiance aan onze chalet. Bedankt aan iedereen die langskwam, aan onze vrijwilligers achter de toog
en aan de stad voor Waregem Wintert.
Goesting gekregen om mee te fietsen? Je mag 3× gratis meerijden: link in bio.
```
