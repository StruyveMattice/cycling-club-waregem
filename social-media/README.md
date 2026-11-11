# Social media: Cycling Club Waregem

Everything needed to set up the club's own **Instagram** and **Facebook** accounts.
The Lamett Classic accounts stay as they are; the club accounts sit next to them.

Handle: **@cyclingclubwaregem** (checked on 10/11/2026: free on Instagram and Facebook).

## Images in this folder

| File | Size | Use |
|---|---|---|
| `profile-picture.png` | 1080×1080 | Profile picture on Instagram, Facebook and Strava |
| `facebook-cover.png` | 1640×856 | Facebook cover. Text sits in the area that both desktop and mobile show. Replace with a group photo later. |
| `post-rij-eens-mee.png` | 1080×1350 | First recruitment post (Instagram and Facebook) |
| `post-nieuw-account.png` | 1080×1350 | Announcement for the Lamett Classic accounts |
| `highlight-*.png` | 1080×1920 | Instagram story highlight covers: Rij mee, Lamett, Reizen, Clubleven, Sponsors |

`generate.py` rebuilds all images (needs Google Chrome and ImageMagick).

## Before you start

- **Use the club's Google account as the login email.** The club already has a Google account
  for its Drive files. Sign up for Instagram (and TikTok) with its Gmail address, and use it as the
  recovery address everywhere. Nobody sees a login email, so the old Biesttrappers name doesn't matter.
  It's also safer than `info@`: if the domain is ever not renewed, `info@` stops working and no
  password can be reset any more. Show `info@cyclingclubwaregem.be` as the **public** contact email.
- **Secure that Google account first**, because whoever controls it can reset every other account.
  Turn on two-factor authentication in a way that works for at least two board members (e.g. both
  scan the same QR code in their authenticator app during setup), and keep the backup codes in the
  password manager.
- **Optional:** rename the Google account to *Cycling Club Waregem* (*Google Account → Personal info → Name*),
  so shared Drive files and emails show the new name. The Gmail address itself can't be changed, and
  a new Google account isn't worth moving all the Drive files for.
- **Store the logins in a shared password manager** (e.g. Bitwarden, free for 2 people)
  with at least one other board member.
- **Turn on two-factor authentication on Instagram too**, with an authenticator app.
- **Photo consent:** ask members at the Algemene Vergadering whether photos of them may be posted,
  and let anyone opt out. A short note in the minutes is enough.

## Instagram

1. Create the account with the club Gmail address and username **cyclingclubwaregem**.
   Instagram accounts have their own login, so this one belongs to the club, not to a person.
2. *Settings → Account type and tools → Switch to professional account → Business*,
   category **Sportclub** (or the closest match). This gives you statistics and a contact button.
3. Profile:
   - **Name** (searchable, 30 characters max): `Cycling Club Waregem | CCW`
   - **Bio** (143 of 150 characters):
     ```
     🚴 Recreatieve wielerclub uit Waregem, sinds 2000
     🔴 Elke zondag: groep A ± 28 km/u · groep B ± 24 km/u
     📍 Eetcafé De Karekiet
     👇 Rij 3× gratis mee
     ```
   - **Link**: `https://cyclingclubwaregem.be/#rij-eens-mee`
   - **Contact options → email**: `info@cyclingclubwaregem.be`
   - **Profile picture**: `profile-picture.png`
4. Post **3 to 6 posts before you announce the account**. An empty profile looks inactive.
   Start with `post-rij-eens-mee.png` plus a few ride photos.
5. Add the story highlights with the `highlight-*.png` covers.

## Facebook

1. Create a **Page** from your own personal Facebook profile: *Menu → Pages → Create new Page*.
   A Page has no login of its own: it's always run from personal profiles, but visitors don't see who runs it.
   Don't make a separate "club" profile with the club Gmail. That breaks Facebook's rules, and when
   Meta disables such a profile, the Page goes with it.
2. **Add at least one other board member as admin** with full control (*Page access* in the Page settings),
   so the Page never depends on one person.
3. Page details:
   - **Name**: `Cycling Club Waregem`
   - **Category**: `Sportclub`
   - **Bio** (95 of 101 characters):
     `Recreatieve wielerclub uit Waregem sinds 2000. Elke zondag samen op de baan. Rij 3× gratis mee!`
   - **Username**: `cyclingclubwaregem`
   - **Website**: `https://cyclingclubwaregem.be`, **email**: `info@cyclingclubwaregem.be`
   - **Address** (optional): Bessemstraat 20, 8790 Waregem, the clubhouse. Check with De Karekiet that this is fine.
   - **Action button**: *Sign up* linking to `https://cyclingclubwaregem.be/#rij-eens-mee`
   - **Profile picture** `profile-picture.png`, **cover** `facebook-cover.png`
4. **Link Instagram to the Page** in Meta Business Suite (*Settings → Linked accounts*).
   From then on you can post to both at once, and schedule posts ahead.
   If Meta suggests adding the club Instagram to your *personal* Accounts Center, skip it:
   the link with the Page is all you need.

### Do we need a Meta business account?

No. Every Page comes with **Meta Business Suite** for free, which is where you link Instagram,
schedule posts and read the statistics. A separate *business portfolio* (formerly Business Manager)
is for organisations with many people, ad accounts or an agency. Two admins on the Page already make
sure the club never loses access.

One exception: if the Lamett Classic Page already sits in a business portfolio, add the new Page and
Instagram account there too, so everything is managed in one place.

## Launch

1. **Collab post from the new account with @_lamettclassic.** Instagram's *Collab* feature
   (when posting: *Tag people → Invite collaborator*) shows the post on both profiles, so the
   Lamett followers see it straight away. This is the quickest way to get the first followers.
2. Post `post-nieuw-account.png` on the Lamett Classic Facebook and Instagram.
3. Share the Page in the club WhatsApp group and ask members to follow and share.
4. Send me the final account links, and I'll add them to the website.

## Captions

**Welcome post**
```
Hallo Instagram! 👋
Wij zijn Cycling Club Waregem (CCW): een recreatieve wielerclub met een 30-tal actieve renners. Sinds 2000 trekken we elke zondag in groep de baan op, en na de rit schuiven we aan de toog van Eetcafé De Karekiet.
Volg mee voor onze ritten, de Lamett Classic, fietsreizen en al het clubleven daarrond.

#cyclingclubwaregem #waregem #wielertoerisme #fietsclub #westvlaanderen
```

**Rij eens mee** (with `post-rij-eens-mee.png`)
```
Zin om eens mee te rijden? 🚴
Elke zondagvoormiddag vertrekken we aan Eetcafé De Karekiet (Bessemstraat 20, Waregem):
🔴 Groep A · 8u00 · ± 28 km/u
🔴 Groep B · 8u30 · ± 24 km/u
Rond 11u zijn we terug, net op tijd voor een drankje.

Je mag 3 keer gratis meerijden. Via de link in bio vraag je toegang tot onze WhatsApp-groep.

#cyclingclubwaregem #waregem #wielrennen #fietsclub #rijeensmee
```

**Announcement on the Lamett Classic accounts** (with `post-nieuw-account.png`)
```
Nieuw! 🚴 Cycling Club Waregem, de club achter de Lamett Classic, heeft nu een eigen account.
Volg @cyclingclubwaregem voor de zondagsritten, het clubleven en je kans om eens mee te rijden.
```

**Throwback** (needs a photo from 2015)
```
Throwback naar 2015 💛
Als De Biesttrappers fietsten negen leden in tien dagen 1.260 km naar Lourdes. Met de steun van zo'n 150 sponsors zamelden ze geld in voor Benito Mahieu, een Waregemse brandweerman die tijdens een interventie zwaar gewond raakte.
Samen voor elkaar rijden: dat zit vandaag nog altijd in de club.

#cyclingclubwaregem #waregem #lourdes #biesttrappers
```

## What to post

Aim for 1 to 2 posts a week, plus stories on Sunday after the ride.

| Theme | How often | Idea |
|---|---|---|
| Zondagrit | Weekly (story) | Group photo at De Karekiet after the ride |
| Rij eens mee | Monthly | The recruitment post, or a short video of the group on the road |
| Sponsor in de kijker | Monthly | One sponsor per month: 11 sponsors give almost a year of posts. Tag them, because sponsors share, which brings in new followers. |
| Lamett Classic | Spring and summer | Countdown, route previews, photos afterwards |
| Clubleven | Around each event | Nieuwjaarsreceptie, clubsouper, verrassingsreis, fietsreizen |
| Throwback | Now and then | Biesttrappers, Lourdes, old photos |

## Other platforms

- **Strava** (the club already exists): use the same profile picture, and create a recurring
  **club event** for the Sunday rides (groups A and B, time and meeting point), so members can sign up.
- **Google Business Profile**: puts the club on Google Maps when people search for "wielerclub Waregem".
  Create it with the club Google account. Use De Karekiet as the meeting point, or set Waregem as the service area.
- **Reserve @cyclingclubwaregem on TikTok** even if you won't use it. It's free and stops
  someone else taking the name.
- Skip X and LinkedIn: that's not where recreational cyclists in Waregem are.
