#!/usr/bin/env python3
"""Regenerate the social media graphics. Needs Google Chrome and ImageMagick.

Usage (from the project root):  python3 social-media/generate.py "$PWD" "$(mktemp -d)"
"""
import base64, pathlib, subprocess, sys

PROJECT = pathlib.Path(sys.argv[1])
OUT = PROJECT / "social-media"
WORK = pathlib.Path(sys.argv[2])
OUT.mkdir(exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def b64(p): return base64.b64encode((PROJECT / p).read_bytes()).decode()
BEBAS = b64("assets/fonts/bebas-neue-latin.woff2")
ROBOTO = b64("assets/fonts/roboto-latin-variable.woff2")
LOGO = b64("assets/img/logo-cycling-club-waregem.png")

BASE_CSS = f"""
@font-face {{ font-family: Bebas; src: url(data:font/woff2;base64,{BEBAS}) format('woff2'); }}
@font-face {{ font-family: Roboto; font-weight: 100 900; src: url(data:font/woff2;base64,{ROBOTO}) format('woff2'); }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: 100%; height: 100%; overflow: hidden; }}
body {{ font-family: Roboto, sans-serif; color: #1a1a1a; -webkit-font-smoothing: antialiased; }}
.t {{ font-family: Bebas, sans-serif; text-transform: uppercase; letter-spacing: .02em; line-height: .95; }}
.red {{ background: #cc2625; color: #fff; }}
"""

# Faint dashed "route" line used as decoration on red backgrounds
ROUTE = """<svg style="position:absolute;inset:0;width:100%;height:100%" viewBox="0 0 100 100" preserveAspectRatio="none">
<path d="M-5 80 C 15 60, 30 95, 50 70 S 80 40, 105 55" fill="none" stroke="rgba(255,255,255,.14)" stroke-width=".6" stroke-dasharray="1.6 1.6" vector-effect="non-scaling-stroke" style="stroke-width:6px"/>
</svg>"""

def page(w, h, body, css=""):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{BASE_CSS}{css}</style></head><body style='width:{w}px;height:{h}px'>{body}</body></html>"

graphics = {}

# Facebook cover 1640x856: desktop shows the middle ~1640x624, mobile crops the sides.
graphics["facebook-cover"] = (1640, 856, page(1640, 856, f"""
<div class="red" style="position:relative;width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
  {ROUTE}
  <div class="t" style="font-size:190px;position:relative">Cycling Club Waregem</div>
  <div style="font-size:44px;margin-top:22px;opacity:.95;position:relative">Recreatieve wielerclub sinds 2000 &middot; Elke zondag samen op de baan</div>
  <div style="margin-top:44px;position:relative;background:#fff;color:#cb2925;font-size:38px;font-weight:700;padding:14px 38px;border-radius:999px">Rij 3&times; gratis mee &rarr; cyclingclubwaregem.be</div>
</div>"""))

# Instagram / Facebook post 1080x1350: recruitment
card = lambda g, t, s: f"""
<div style="flex:1;background:#fff;border-radius:28px;overflow:hidden;box-shadow:0 8px 24px rgba(0,0,0,.08);text-align:center">
  <div class="red t" style="font-size:64px;padding:18px 0 12px">Groep {g}</div>
  <div style="padding:28px 10px 34px">
    <div style="font-size:26px;letter-spacing:.08em;color:#4b5563;text-transform:uppercase">Vertrek</div>
    <div class="t" style="font-size:120px">{t}</div>
    <div style="font-size:26px;letter-spacing:.08em;color:#4b5563;text-transform:uppercase;margin-top:18px">Gemiddeld</div>
    <div class="t" style="font-size:88px">&plusmn; {s} km/u</div>
  </div>
</div>"""
graphics["post-rij-eens-mee"] = (1080, 1350, page(1080, 1350, f"""
<div style="width:100%;height:100%;background:#f1f2f3;display:flex;flex-direction:column">
  <div class="red" style="position:relative;padding:70px 60px 60px;text-align:center">
    {ROUTE}
    <div class="t" style="font-size:170px;position:relative">Rij eens mee</div>
    <div style="font-size:34px;margin-top:16px;position:relative;white-space:nowrap">Elke zondagvoormiddag &middot; vertrek aan Eetcaf&eacute; De Karekiet</div>
  </div>
  <div style="display:flex;gap:40px;padding:56px 60px 0">{card("A", "8u00", "28")}{card("B", "8u30", "24")}</div>
  <div style="display:flex;align-items:center;justify-content:center;gap:18px;margin:48px 60px 0;font-size:36px">
    <svg width="44" height="44" viewBox="0 0 24 24" fill="#cc2625"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5Z"/></svg>
    <span><b>Eetcaf&eacute; De Karekiet</b> &middot; Bessemstraat 20, Waregem</span>
  </div>
  <div style="text-align:center;margin-top:auto;padding:0 60px 64px">
    <div class="t" style="font-size:96px;color:#cb2925">3&times; gratis meerijden</div>
    <div style="font-size:36px;margin-top:14px">Rond 11u terug &middot; <b>link in bio</b></div>
  </div>
</div>"""))

# Announcement for the Lamett Classic accounts 1080x1350
graphics["post-nieuw-account"] = (1080, 1350, page(1080, 1350, f"""
<div class="red" style="position:relative;width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:80px">
  {ROUTE}
  <img src="data:image/png;base64,{LOGO}" style="width:360px;height:360px;position:relative">
  <div class="t" style="font-size:150px;margin-top:50px;position:relative">Volg nu ook<br>de club</div>
  <div style="font-size:42px;margin-top:22px;line-height:1.35;position:relative">Cycling Club Waregem, de club achter de Lamett Classic, heeft een eigen account</div>
  <div style="margin-top:56px;position:relative;background:#fff;color:#cb2925;font-size:52px;font-weight:700;padding:18px 48px;border-radius:999px">@cyclingclubwaregem</div>
</div>"""))

# Instagram story highlight covers 1080x1920 (only the centre circle shows)
for name, label in [("rij-mee", "Rij mee"), ("lamett", "Lamett"), ("reizen", "Reizen"), ("clubleven", "Club&shy;leven"), ("sponsors", "Sponsors")]:
    graphics[f"highlight-{name}"] = (1080, 1920, page(1080, 1920, f"""
<div class="red" style="width:100%;height:100%;display:flex;align-items:center;justify-content:center">
  <div style="width:640px;height:640px;border:10px solid #fff;border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center">
    <div class="t" style="font-size:150px;max-width:520px">{label}</div>
  </div>
</div>"""))

for name, (w, h, html) in graphics.items():
    src = WORK / f"{name}.html"
    src.write_text(html)
    png = WORK / f"{name}.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={w},{h + 200}", "--virtual-time-budget=4000", f"--screenshot={png}", src.as_uri()],
                   check=True, capture_output=True)
    # PNG for covers/highlights (sharp text), high-quality JPG is fine too but PNG avoids artefacts
    subprocess.run(["magick", str(png), "-crop", f"{w}x{h}+0+0", "+repage", "-strip", str(OUT / f"{name}.png")], check=True)
    print(name, w, h)
