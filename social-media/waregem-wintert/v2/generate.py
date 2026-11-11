#!/usr/bin/env python3
"""Version 2 (cozy Christmas) of the poster and social graphics for the CCW chalet at Waregem Wintert.

Needs Google Chrome, ImageMagick and macOS: the QR code comes from CoreImage and the handwriting from
the SignPainter font that ships with macOS. Nothing to install.
Usage (from the project root):  python3 social-media/waregem-wintert/v2/generate.py "$PWD" "$(mktemp -d)"
"""
import base64, math, pathlib, random, subprocess, sys

PROJECT = pathlib.Path(sys.argv[1])
OUT = PROJECT / "social-media" / "waregem-wintert" / "v2"
WORK = pathlib.Path(sys.argv[2])
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# ---- Event details: change these and rerun -------------------------------------------------
KICKER = "Waregem Wintert"
LEAD, HEADLINE = "Tijd voor de", "Bevoorrading"
DAY, DATE, MONTH, HOURS = "Zaterdag", "5", "december", "9.30 &ndash; 22 uur"
HERO = "Jenevers &amp; verse soep"
EXTRA = "+ warme choco en hapjes"
PLACE = "Chalet aan de ijspiste &middot; Markt, Waregem"
RIDE_URL = "https://cyclingclubwaregem.be/#rij-eens-mee"
MENU_LEFT = [("Jenever", ["Dreupel of fles", "Appel", "Vanille", "Choco", "Chocoretto"]),
             ("Warm", ["Verse soep", "Warme choco"])]
MENU_RIGHT = [("Bubbels &amp; wijn", ["Cava", "Ros&eacute;"]),
              ("Bier &amp; fris", ["Pils", "Cola / Cola Zero", "Spuitwater", "Plat water"])]
MENU_BOTTOM = ("Om te knabbelen", ["Partymix van frituurhapjes"])
HAPPY = ("Elk uur", "Happy", "hour!")  # gold sticker next to the bike; set to None to leave it out
CONTEST = "Win 2 inschrijvingen voor de Lamett Classic 2027"  # gold line under the offer; None to leave it out
# ---------------------------------------------------------------------------------------------

RED, RED_DARK, CREAM, GOLD, INK, KRAFT = "#cc2625", "#8f1915", "#fbf1df", "#f4c35a", "#2b211c", "#ecd3a3"
FRAME = "#e23a2f"
BG = "radial-gradient(ellipse 80% 62% at 50% 40%, #265d44 0%, #1b4935 55%, #10301f 100%)"
BULBS = {"gold": "#ffd15c", "red": "#ff5d4f", "white": "#fff3cf", "green": "#a3eab2"}
YARN = {  # base, light, dark, shade between the stitches
    "R": ("#cc2625", "#e5483e", "#a01c18", "#5f110e"),
    "C": ("#f6e8cf", "#fffaf0", "#dcc8a6", "#a8916c"),
    "G": ("#2e7a54", "#3f9567", "#215c3f", "#163e2b"),
    "Y": ("#f4c35a", "#ffdc8c", "#d6a03a", "#8d6a22"),
}

def b64(p): return base64.b64encode((PROJECT / p).read_bytes()).decode()
BEBAS = b64("assets/fonts/bebas-neue-latin.woff2")
ROBOTO = b64("assets/fonts/roboto-latin-variable.woff2")
LOGO = f"data:image/png;base64,{b64('assets/img/logo-cycling-club-waregem.png')}"

CSS = f"""
@font-face {{ font-family: Bebas; src: url(data:font/woff2;base64,{BEBAS}) format('woff2'); }}
@font-face {{ font-family: Roboto; font-weight: 100 900; src: url(data:font/woff2;base64,{ROBOTO}) format('woff2'); }}
@font-face {{ font-family: Script; src: local('SignPainter-HouseScriptSemibold'), local('SignPainter-HouseScript'); }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ overflow: hidden; }}
body {{ font-family: Roboto, sans-serif; color: {CREAM}; -webkit-font-smoothing: antialiased;
        -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.t {{ font-family: Bebas, sans-serif; font-weight: 400; text-transform: uppercase; letter-spacing: .02em; line-height: .9; }}
.s {{ font-family: Script, 'Snell Roundhand', cursive; line-height: 1; }}
.canvas {{ position: relative; overflow: hidden; background: {BG}; width: 100%; height: 100%; }}
.layer {{ position: absolute; inset: 0; }}
.flow {{ position: absolute; left: 0; right: 0; display: flex; flex-direction: column; align-items: center; text-align: center; }}
/* Ribbon banner: the band in front, two notched tails behind it */
.rb {{ position: relative; display: inline-block; isolation: isolate; color: {CREAM}; }}
.rb::before, .rb::after {{ content: ""; position: absolute; top: .26em; height: 100%; width: 1.05em; background: {RED_DARK}; z-index: -1; }}
.rb::before {{ left: -.8em; clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%, .32em 50%); }}
.rb::after {{ right: -.8em; clip-path: polygon(0 0, 100% 0, calc(100% - .32em) 50%, 100% 100%, 0 100%); }}
.rb > span {{ position: relative; display: block; background: {RED}; padding: .17em .5em .06em; }}
.rb > span::before, .rb > span::after {{ content: ""; position: absolute; top: 100%; width: .26em; height: .26em; background: #4f0d0b; }}
.rb > span::before {{ left: 0; clip-path: polygon(0 0, 100% 0, 100% 100%); }}
.rb > span::after {{ right: 0; clip-path: polygon(0 0, 100% 0, 0 100%); }}
"""


# ---- Little drawings ------------------------------------------------------------------------
def defs():
    """Gradients shared by every SVG on the page: the glow of the lights and the shading of the yarn."""
    glow = "".join(f'<radialGradient id="glow-{k}"><stop offset="0" stop-color="{c}" stop-opacity=".75"/>'
                   f'<stop offset=".3" stop-color="{c}" stop-opacity=".3"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>'
                   for k, c in BULBS.items())
    yarn = "".join(f'<linearGradient id="yarn-{k}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{light}"/>'
                   f'<stop offset=".55" stop-color="{base}"/><stop offset="1" stop-color="{dark}"/></linearGradient>'
                   for k, (base, light, dark, _) in YARN.items())
    return f'<svg width="0" height="0" style="position:absolute"><defs>{glow}{yarn}</defs></svg>'

def bulb(x, y, angle, r, key):
    """A Christmas light hanging from (x, y), with its glow."""
    return (f'<g class="bulb" transform="translate({x:.1f} {y:.1f}) rotate({angle:.1f})">'
            f'<circle class="glow" cx="0" cy="{18 * r:.1f}" r="{42 * r:.1f}" fill="url(#glow-{key})"/>'
            f'<rect x="{-4.5 * r:.1f}" y="{-r:.1f}" width="{9 * r:.1f}" height="{9 * r:.1f}" rx="{2 * r:.1f}" fill="#0b2219"/>'
            f'<ellipse class="lamp" cx="0" cy="{19 * r:.1f}" rx="{8 * r:.1f}" ry="{12 * r:.1f}" fill="{BULBS[key]}"/>'
            f'<ellipse cx="{-2.6 * r:.1f}" cy="{15 * r:.1f}" rx="{2.3 * r:.1f}" ry="{4 * r:.1f}" fill="#fff" fill-opacity=".6"/></g>')

def garland(w, h, y, sag, spans, per_span, r, seed, opacity=1.0):
    """A string of lights drooping across the top."""
    rnd, keys, wire, bulbs = random.Random(seed), list(BULBS), [], []
    xs = [-w * .03 + i * w * 1.06 / spans for i in range(spans + 1)]
    for i in range(spans):
        x0, x1 = xs[i], xs[i + 1]
        cx, cy = (x0 + x1) / 2, y + 2 * sag
        wire.append(f"M{x0:.1f} {y:.1f} Q{cx:.1f} {cy:.1f} {x1:.1f} {y:.1f}")
        for k in range(per_span):
            t = (k + .5) / per_span
            px = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t * t * x1
            py = (1 - t) ** 2 * y + 2 * (1 - t) * t * cy + t * t * y
            bulbs.append(bulb(px, py, rnd.uniform(-14, 14), r, keys[(i * per_span + k) % len(keys)]))
    return (f'<svg class="layer" style="bottom:auto;height:{h}px;opacity:{opacity}" viewBox="0 0 {w:.1f} {h}">'
            f'<path d="{" ".join(wire)}" fill="none" stroke="#0b2219" stroke-width="{2.6 * r:.1f}"/>{"".join(bulbs)}</svg>')

def flake(cx, cy, r, opacity, rot):
    sw = max(2.0, r * .09)
    arms = "".join(
        f'<g transform="rotate({rot + k * 60:.1f} {cx:.1f} {cy:.1f})">'
        f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{cx:.1f}" y2="{cy - r:.1f}"/>'
        f'<polyline points="{cx - r * .3:.1f},{cy - r * .75:.1f} {cx:.1f},{cy - r * .5:.1f} {cx + r * .3:.1f},{cy - r * .75:.1f}"/></g>'
        for k in range(6))
    return f'<g fill="none" stroke="{CREAM}" stroke-opacity="{opacity:.2f}" stroke-width="{sw:.1f}" stroke-linecap="round">{arms}</g>'

def snowfall(w, h, dots, flakes, seed, s=1.0):
    rnd = random.Random(seed)
    d = "".join(f'<circle cx="{rnd.uniform(0, w):.1f}" cy="{rnd.uniform(0, h):.1f}" r="{rnd.uniform(1.6, 4.6) * s:.1f}" '
                f'fill="{CREAM}" fill-opacity="{rnd.uniform(.12, .5):.2f}"/>' for _ in range(dots))
    f = "".join(flake(rnd.uniform(0, w), rnd.uniform(h * .15, h), rnd.uniform(16, 40) * s, rnd.uniform(.07, .15), rnd.uniform(0, 60))
                for _ in range(flakes))
    return f'<svg class="layer" style="bottom:auto;height:{h:.0f}px" viewBox="0 0 {w:.1f} {h:.1f}">{d}{f}</svg>'

def snow_layers(w, h, seed, s=1.0):
    """Falling snow for the videos: two tiled layers that each fall exactly one tile per loop, so the video loops seamlessly."""
    rnd, layers = random.Random(seed), []
    for tile, count, rmin, rmax, omin, omax, sway in [(480, 26, 1.4, 3.2, .15, .4, 8), (900, 18, 2.6, 5.2, .3, .6, 14)]:
        dots = "".join(f'<circle cx="{rnd.uniform(0, w):.1f}" cy="{rnd.uniform(0, tile):.1f}" r="{rnd.uniform(rmin, rmax) * s:.1f}" '
                       f'fill="{CREAM}" fill-opacity="{rnd.uniform(omin, omax):.2f}"/>' for _ in range(count))
        tiles = "".join(f'<g transform="translate(0 {k * tile})">{dots}</g>' for k in range(-1, int(h // tile) + 2))
        layers.append(f'<g class="snowlayer" data-ht="{tile}" data-sway="{sway}">{tiles}</g>')
    return f'<svg class="layer" style="bottom:auto;height:{h:.0f}px" viewBox="0 0 {w:.1f} {h:.1f}">{"".join(layers)}</svg>'

# Moves the lights, snow, date tag and sticker to time t (seconds); the capture script calls renderAt() for every frame.
ANIM_JS = """(() => {
  const T = SECONDS;
  let seed = 7;
  const rand = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const bulbs = [...document.querySelectorAll('.bulb')].map(g => ({
    glow: g.querySelector('.glow'), lamp: g.querySelector('.lamp'), k: 1 + Math.floor(rand() * 3), p: rand() * 2 * Math.PI }));
  const layers = [...document.querySelectorAll('.snowlayer')].map(el => ({ el, ht: +el.dataset.ht, sway: +el.dataset.sway, p: rand() * 2 * Math.PI }));
  const tag = document.getElementById('tag'), tagBase = tag.getAttribute('transform');
  const badge = document.getElementById('badge');
  window.renderAt = t => {
    const w = 2 * Math.PI * t / T;
    for (const b of bulbs) {  // whole cycles per loop, so the twinkle loops seamlessly
      const v = 0.5 + 0.5 * Math.sin(w * b.k + b.p);
      b.glow.setAttribute('opacity', (0.3 + 0.7 * v).toFixed(3));
      b.lamp.setAttribute('opacity', (0.72 + 0.28 * v).toFixed(3));
    }
    for (const l of layers) {
      l.el.setAttribute('transform', `translate(${(l.sway * Math.sin(w + l.p)).toFixed(2)} ${((t / T) * l.ht).toFixed(2)})`);
    }
    tag.setAttribute('transform', tagBase.replace(/rotate\\(([-\\d.]+)/, () => `rotate(${(9 + 2 * Math.sin(w)).toFixed(3)}`));
    if (badge) {
      const { cx, cy, rot } = badge.dataset;
      const s = 1 + 0.07 * Math.pow(Math.max(0, Math.sin(2 * w)), 6);
      badge.setAttribute('transform', `rotate(${rot} ${cx} ${cy}) translate(${cx} ${cy}) scale(${s.toFixed(4)}) translate(${-cx} ${-cy})`);
    }
  };
  renderAt(0);
})();"""


# ---- Knitted Christmas-sweater band with bikes and trees ------------------------------------
BIKE = [
    ".......XXX.......XXX......",
    "........XXXXXXXXXX..X.....",
    ".......X.X.......X........",
    "...XXX.X.X......X.X.XXX...",
    ".XX...XX..X....X..XX...XX.",
    ".X...X.X..X..XX...XX....X.",
    "X....X..X..XX....X..X....X",
    "X...XXXXXXXX.....X...X...X",
    "X.......X........X.......X",
    ".X.....X..........X.....X.",
    ".XX...XX..........XX...XX.",
    "...XXX..............XXX...",
]
TREE = [
    "....Y....",
    "....G....",
    "...GGG...",
    "..GGGGG..",
    "...GGG...",
    "..GGGGG..",
    ".GGGGGGG.",
    "..GGGGG..",
    ".GGGGGGG.",
    "GGGGGGGGG",
    "....R....",
    "....R....",
]

def sweater_grid(cols, zig_at_top=True):
    """Rows of yarn colours: a red band with a zigzag edge and a cream row of bikes and Christmas trees."""
    unit = [("tree", 9), ("gap", 4), ("bike", 26), ("gap", 4)]
    span = sum(width for _, width in unit)
    reps = cols // span + 4
    strip = [["C"] * (reps * span) for _ in range(len(BIKE))]
    x, bikes = 0, []
    for _ in range(reps):
        for kind, width in unit:
            if kind != "gap":
                for r, line in enumerate(TREE if kind == "tree" else BIKE):
                    for c, ch in enumerate(line):
                        if ch != ".":
                            strip[r][x + c] = "R" if ch == "X" else ch
                if kind == "bike":
                    bikes.append(x + 13)
            x += width
    start = bikes[len(bikes) // 2] - cols // 2  # a bike in the middle
    motif = [["C"] * cols] + [row[start:start + cols] for row in strip] + [["C"] * cols]
    teeth = ["XXXXX.", ".XXX..", "..X..."]
    phase = (cols // 2 - 2) % 6
    zig = [["C" if t[(c - phase) % 6] == "X" else "R" for c in range(cols)] for t in teeth]
    red = lambda: ["R"] * cols
    if zig_at_top:   # band along the bottom edge
        return [red()] + zig + [red()] + motif + [red(), red()]
    return [red(), red()] + motif + [red()] + zig + [red()]  # band along the top edge

def knit(cols, sw, zig_at_top=True, prefix="k"):
    """Render the grid as knitted V-stitches. Returns (svg, height)."""
    sh = sw * .8
    grid = sweater_grid(cols, zig_at_top)
    w, h = cols * sw, len(grid) * sh
    shade = []
    for r, row in enumerate(grid):  # dark yarn between the stitches, one rectangle per run of colour
        c0 = 0
        while c0 < cols:
            c1 = c0
            while c1 < cols and row[c1] == row[c0]:
                c1 += 1
            shade.append(f'<rect x="{c0 * sw:.2f}" y="{r * sh:.2f}" width="{(c1 - c0) * sw + .5:.2f}" height="{sh + .5:.2f}" fill="{YARN[row[c0]][3]}"/>')
            c0 = c1
    leg = lambda cx, rot, k: (f'<ellipse cx="{cx:.2f}" cy="{sh * .5:.2f}" rx="{sw * .25:.2f}" ry="{sh * .62:.2f}" '
                              f'transform="rotate({rot} {cx:.2f} {sh * .5:.2f})" fill="url(#yarn-{k})"/>')
    stitches = "".join(f'<g id="{prefix}{k}">{leg(sw * .29, -32, k)}{leg(sw * .71, 32, k)}</g>' for k in YARN)
    uses = "".join(f'<use href="#{prefix}{k}" x="{c * sw:.2f}" y="{r * sh:.2f}"/>' for r, row in enumerate(grid) for c, k in enumerate(row))
    return (f'<svg width="{w:.1f}" height="{h:.1f}" viewBox="0 0 {w:.2f} {h:.2f}" style="display:block">'
            f'<defs>{stitches}</defs>{"".join(shade)}{uses}</svg>'), h


# ---- The racing bike in Christmas lights, with a Santa hat and the date on a gift tag --------
def wrap_lights(a, b, turns, amp, seed, t0=.12, t1=.88):
    (ax, ay), (bx, by) = a, b
    dx, dy = bx - ax, by - ay
    ln = math.hypot(dx, dy)
    nx, ny = -dy / ln, dx / ln
    pts = []
    for i in range(81):
        u = i / 80
        t, s = t0 + (t1 - t0) * u, math.sin(u * turns * 2 * math.pi)
        pts.append(f"{ax + dx * t + nx * amp * s:.1f} {ay + dy * t + ny * amp * s:.1f}")
    out = [f'<path d="M{" L".join(pts)}" fill="none" stroke="#0b2219" stroke-width="2.4"/>']
    keys = list(BULBS)
    for k in range(int(turns * 2)):
        u = (2 * k + 1) / (4 * turns)
        t, s = t0 + (t1 - t0) * u, math.sin(u * turns * 2 * math.pi)
        x, y = ax + dx * t + nx * amp * s, ay + dy * t + ny * amp * s
        angle = math.degrees(math.atan2(ny * s, nx * s)) - 90
        out.append(bulb(x, y, angle, .6, keys[(k + seed) % len(keys)]))
    return "".join(out)

def badge(cx, cy, r, rot):
    """Gold starburst sticker announcing the happy hours."""
    pts = " ".join(f"{cx + (r if i % 2 == 0 else r * .9) * math.cos(i * math.pi / 18):.1f},"
                   f"{cy + (r if i % 2 == 0 else r * .9) * math.sin(i * math.pi / 18):.1f}" for i in range(36))
    top, line1, line2 = HAPPY
    text = lambda y, size, fill, s, extra="": (f'<text x="{cx}" y="{cy + y * r:.1f}" text-anchor="middle" font-family="Bebas" '
                                               f'font-size="{size * r:.1f}" fill="{fill}" {extra}>{s}</text>')
    return (f'<g id="badge" data-cx="{cx}" data-cy="{cy}" data-rot="{rot}" transform="rotate({rot} {cx} {cy})">'
            f'<polygon points="{pts}" transform="translate(4 6)" fill="#000" fill-opacity=".25"/>'
            f'<polygon points="{pts}" fill="{GOLD}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r * .86:.1f}" fill="none" stroke="{RED_DARK}" stroke-width="2.5" stroke-dasharray="6 5"/>'
            f'{text(-.32, .28, INK, top, "letter-spacing=\"2\"")}{text(.12, .5, RED, line1)}{text(.55, .5, RED, line2)}</g>')

def bike_scene():
    c = CREAM
    RH, FH, BB, ST, HTT, HTB, SP = (0, 0), (330, 0), (138, 24), (88, -148), (282, -164), (295, -118), (70, -206)
    line = lambda a, b, col, w, extra="": (f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{col}" '
                                           f'stroke-width="{w}" stroke-linecap="round" {extra}/>')
    p = []
    for hx, hy in (RH, FH):  # wheels
        spokes = "".join(line((hx + 9 * math.cos(a), hy + 9 * math.sin(a)), (hx + 92 * math.cos(a + .16), hy + 92 * math.sin(a + .16)), c, 1.6)
                         for a in (i * math.pi / 10 for i in range(20)))
        p.append(f'<g opacity=".4">{spokes}</g>')
        p.append(f'<circle cx="{hx}" cy="{hy}" r="94" fill="none" stroke="{c}" stroke-width="3.5" opacity=".85"/>')
        p.append(f'<circle cx="{hx}" cy="{hy}" r="106" fill="none" stroke="{c}" stroke-width="13"/>')
        p.append(f'<circle cx="{hx}" cy="{hy}" r="9" fill="{c}"/>')
    p.append(f'<circle cx="0" cy="0" r="13" fill="none" stroke="{c}" stroke-width="3"/>')
    p.append(line((BB[0], BB[1] - 27), (0, -13), c, 3, 'stroke-dasharray="4 3" opacity=".6"'))
    p.append(line((BB[0], BB[1] + 27), (0, 13), c, 3, 'stroke-dasharray="4 3" opacity=".6"'))
    p += [line(BB, RH, FRAME, 9), line(ST, RH, FRAME, 9), line(BB, ST, FRAME, 12), line(ST, HTT, FRAME, 12),
          line(BB, HTB, FRAME, 14), line(HTB, HTT, FRAME, 16)]
    p.append(f'<path d="M295 -118 C301 -76 309 -36 330 0" fill="none" stroke="{FRAME}" stroke-width="10" stroke-linecap="round"/>')
    p.append(line(ST, SP, "#e9dcc2", 8))
    p.append(f'<path d="M26 -214 C50 -224 92 -222 116 -214 C120 -210 114 -205 104 -205 L44 -205 C30 -205 22 -209 26 -214Z" fill="{c}"/>')
    p.append(f'<polyline points="282,-164 279,-180 322,-186" fill="none" stroke="{c}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>')
    p.append(f'<path d="M322 -186 C356 -188 368 -162 360 -140 C354 -124 336 -122 326 -130" fill="none" stroke="{c}" stroke-width="8" stroke-linecap="round"/>')
    p.append(f'<path d="M332 -188 C344 -197 356 -192 356 -178" fill="none" stroke="{c}" stroke-width="9" stroke-linecap="round"/>')
    p.append(f'<circle cx="{BB[0]}" cy="{BB[1]}" r="27" fill="none" stroke="{c}" stroke-width="4.5"/>')
    p.append(line(BB, (BB[0] + 22, BB[1] + 46), c, 8))
    p.append(line((BB[0] + 8, BB[1] + 48), (BB[0] + 38, BB[1] + 48), c, 7))
    p.append(wrap_lights(ST, HTT, 3.5, 12, 1))
    p.append(wrap_lights(BB, HTB, 3.5, 13, 2))
    # Santa hat on the saddle
    p.append(f'<g transform="translate(0 8)"><path d="M44 -232 C40 -270 64 -300 98 -298 C122 -296 140 -280 140 -256 '
             f'C132 -270 116 -276 104 -268 C98 -258 100 -244 104 -232Z" fill="{RED}"/>'
             f'<rect x="36" y="-242" width="76" height="24" rx="12" fill="#fff8ea"/><circle cx="140" cy="-252" r="14" fill="#fff8ea"/></g>')
    # Snow under the wheels
    p.append(f'<path d="M-170 118 C-150 100 -60 96 40 99 C140 102 220 93 300 96 C380 99 450 100 482 114 C470 126 -160 128 -170 118Z" '
             f'fill="{CREAM}"/>')
    # String from the handlebar to the gift tag with the date
    hx, hy = 566, -112
    p.append(f'<path d="M361 -146 C420 -40 500 -40 {hx} {hy}" fill="none" stroke="#e8d6b0" stroke-width="3"/>')
    tag = (f'<polygon points="0,34 34,0 400,0 400,200 34,200 0,166" fill="{KRAFT}"/>'
           f'<polygon points="12,39 39,12 388,12 388,188 39,188 12,161" fill="none" stroke="#b9925a" stroke-width="2.5" stroke-dasharray="7 6"/>'
           f'<circle cx="40" cy="100" r="12" fill="#1b4935"/><circle cx="40" cy="100" r="13" fill="none" stroke="#c9a46a" stroke-width="4"/>'
           f'<text x="122" y="172" text-anchor="middle" font-family="Bebas" font-size="178" fill="{RED}">{DATE}</text>'
           f'<text x="176" y="76" font-family="Bebas" font-size="44" fill="{INK}" letter-spacing="1">{DAY}</text>'
           f'<text x="176" y="122" font-family="Bebas" font-size="44" fill="{RED}" letter-spacing="1">{MONTH}</text>'
           f'<text x="176" y="168" font-family="Bebas" font-size="40" fill="{INK}" letter-spacing="1">{HOURS}</text>')
    p.append(f'<g id="tag" transform="translate({hx - 40} {hy - 100}) rotate(9 40 100)">{tag}</g>')
    p.append(f'<path d="M{hx - 6} {hy - 4} q 10 -14 16 2" fill="none" stroke="#e8d6b0" stroke-width="3"/>')
    if HAPPY:
        p.append(badge(-56, -218, 96, -12))
    return f'<svg viewBox="-130 -314 1080 444" style="display:block;width:100%;height:auto;overflow:visible">{"".join(p)}</svg>'


# ---- Text blocks (s = scale) ----------------------------------------------------------------
def kicker(s, text=KICKER):
    flake_icon = (f'<svg width="{30 * s}" height="{30 * s}" viewBox="-12 -12 24 24" style="display:block">'
                  f'{flake(0, 0, 10.5, 1, 0).replace("stroke-width", "data-w").replace("<g ", "<g stroke-width=\"2.2\" ")}</svg>')
    return (f'<div class="t" style="display:inline-flex;align-items:center;gap:{16 * s}px;font-size:{38 * s}px;letter-spacing:.18em;'
            f'color:{CREAM};border:{2.5 * s}px solid rgba(251,241,223,.75);border-radius:999px;padding:{10 * s}px {30 * s}px {7 * s}px">'
            f'{flake_icon}<span style="padding-top:{3 * s}px">{text}</span>{flake_icon}</div>')

def headline(s, lead_px, head_px):
    return (f'<div class="s" style="font-size:{lead_px}px;color:{GOLD};transform:rotate(-3deg);margin-bottom:{-lead_px * .16}px">{LEAD}</div>'
            f'<div class="t" style="font-size:{head_px}px;color:{CREAM};text-shadow:0 {head_px * .04:.1f}px 0 {RED_DARK};white-space:nowrap">{HEADLINE}</div>')

def ribbon(px):
    return f'<div class="rb t" style="font-size:{px}px;letter-spacing:.03em"><span>{HERO}</span></div>'

def details(s):
    pin = (f'<svg width="{28 * s}" height="{28 * s}" viewBox="0 0 24 24" fill="{GOLD}" style="flex:none"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 '
           f'7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5Z"/></svg>')
    gift = (f'<svg width="{28 * s}" height="{28 * s}" viewBox="0 0 24 24" fill="none" stroke="{GOLD}" stroke-width="2.2" '
            f'stroke-linejoin="round" stroke-linecap="round" style="flex:none"><rect x="3" y="8" width="18" height="5" rx="1"/>'
            f'<path d="M5 13v8h14v-8M12 8v13M12 8c-1.5-3-5-4-5.5-1.5S9.5 8 12 8Zm0 0c1.5-3 5-4 5.5-1.5S14.5 8 12 8Z"/></svg>')
    contest = (f'<div style="display:flex;align-items:center;gap:{10 * s}px;font-size:{33 * s}px;font-weight:700;color:{GOLD};'
               f'margin-top:{12 * s}px">{gift}{CONTEST}</div>') if CONTEST else ""
    return (f'<div style="font-size:{33 * s}px;font-weight:500">{EXTRA}</div>{contest}'
            f'<div style="display:flex;align-items:center;gap:{10 * s}px;font-size:{33 * s}px;font-weight:700;margin-top:{12 * s}px">{pin}{PLACE}</div>')

def footer(s):
    return (f'<div style="display:flex;align-items:center;gap:{24 * s}px">'
            f'<img src="{LOGO}" style="width:{118 * s}px;height:{118 * s}px;flex:none">'
            f'<div style="text-align:left"><div class="s" style="font-size:{92 * s}px;color:{GOLD}">Iedereen welkom!</div>'
            f'<div style="font-size:{25 * s}px;margin-top:{2 * s}px;opacity:.85;white-space:nowrap">cyclingclubwaregem.be &middot; @cyclingclubwaregem</div>'
            f'</div></div>')

def shade(side, at):
    """Soft shadow along a knitted band. A gradient strip, because Chrome turns blurred box-shadows
    into hard dark blocks when it prints to PDF."""
    direction = "to top" if side == "bottom" else "to bottom"
    return (f'<div style="position:absolute;left:0;right:0;{side}:{at:.1f}px;height:22px;'
            f'background:linear-gradient({direction}, rgba(0,0,0,.32), rgba(0,0,0,0))"></div>')

def page(body, w, h, unit="px", pdf=False):
    size = f"@page {{ size: {w}{unit} {h}{unit}; margin: 0; }}" if pdf else ""
    return (f"<!doctype html><html lang='nl-BE'><head><meta charset='utf-8'><style>{CSS}{size}"
            f"html, body {{ width: {w}{unit}; height: {h}{unit}; }}</style></head><body>{body}</body></html>")


# ---- Designs --------------------------------------------------------------------------------
def portrait(w, h, s, top, gaps, illus_w, lead_px, head_px, rib_px, cols, seed, lights_r=1.0, anim=False):
    """Shared layout of the A3 poster, the Instagram post and the story (anim=True: falling snow for the videos)."""
    band, band_h = knit(cols, w / cols)
    g = gaps
    snow = (snowfall(w, h - band_h, 0, 7, seed, s) + snow_layers(w, h - band_h, seed, s) if anim
            else snowfall(w, h - band_h, int(70 * s * h / 1587 * 1.4), 7, seed, s))
    return f"""<div class="canvas">{defs()}
  {snow}
  {garland(w, 190 * lights_r, -24 * lights_r, 48 * lights_r, 5, 5, .72 * lights_r, seed + 1, .55)}
  {garland(w, 190 * lights_r, -10 * lights_r, 62 * lights_r, 4, 6, lights_r, seed + 2)}
  <div class="flow" style="top:{top}px">
    {kicker(s)}
    <div style="margin-top:{g[0]}px">{headline(s, lead_px, head_px)}</div>
    <div style="width:{illus_w}px;margin-top:{g[1]}px">{bike_scene()}</div>
    <div style="margin-top:{g[2]}px">{ribbon(rib_px)}</div>
    <div style="margin-top:{g[3]}px">{details(s)}</div>
    <div style="margin-top:{g[4]}px">{footer(s)}</div>
  </div>
  {shade("bottom", band_h)}
  <div style="position:absolute;left:0;right:0;bottom:0">{band}</div>
</div>"""

def facebook_cover():
    w, h = 1920, 1005
    band, band_h = knit(128, 15)
    return f"""<div class="canvas">{defs()}
  {snowfall(w, h - band_h, 90, 9, 21)}
  {garland(w, 170, -22, 44, 7, 5, .66, 22, .55)}
  {garland(w, 170, -10, 56, 6, 6, .9, 23)}
  <div style="position:absolute;left:0;right:0;top:0;bottom:{band_h:.0f}px;display:flex;align-items:center;justify-content:center;gap:70px;padding-top:70px">
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center">
      {kicker(.85)}
      <div style="margin-top:14px">{headline(.85, 92, 156)}</div>
      <div style="margin-top:30px">{ribbon(62)}</div>
      <div style="margin-top:32px">{details(.85)}</div>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:26px">
      <div style="width:820px">{bike_scene()}</div>
      {footer(.78)}
    </div>
  </div>
  {shade("bottom", band_h)}
  <div style="position:absolute;left:0;right:0;bottom:0">{band}</div>
</div>"""

def counter_sign(qr):
    """A4 sign for on the counter: from visitor to follower or trial rider."""
    w = 210 * 96 / 25.4
    band, band_h = knit(64, w / 64, zig_at_top=False)
    group = lambda g, t, v: (f'<div style="flex:1;border:3px solid {RED};border-radius:16px;padding:14px 0 10px;background:#fff">'
                             f'<div class="t" style="font-size:40px;color:{RED}">Groep {g}</div>'
                             f'<div class="t" style="font-size:62px;margin-top:2px;color:{INK}">{t}</div>'
                             f'<div style="font-size:20px;color:#5b4d43;margin-top:2px">gemiddeld &plusmn; {v} km/u</div></div>')
    return f"""<div class="canvas">{defs()}
  <div style="position:absolute;left:0;right:0;top:0">{band}</div>
  {shade("top", band_h)}
  {snowfall(w, 1123, 40, 4, 31, .8)}
  <div class="flow" style="top:{band_h + 22:.0f}px">
    <div class="s" style="font-size:78px;color:{GOLD};transform:rotate(-3deg);margin-bottom:-10px">Zin om</div>
    <div class="t" style="font-size:104px;text-shadow:0 4px 0 {RED_DARK}">Mee te fietsen?</div>
    <div style="font-size:25px;font-weight:500;margin-top:12px">Rij 3 keer gratis mee met Cycling Club Waregem</div>
    <div style="background:{CREAM};color:{INK};border-radius:22px;margin-top:26px;padding:26px 34px;width:680px;box-shadow:0 7px 0 rgba(0,0,0,.25)">
      <div style="font-size:22px;line-height:1.4">Elke <b>zondagvoormiddag</b> vertrekken we aan<br><b>Eetcaf&eacute; De Karekiet</b>, Bessemstraat 20, Waregem</div>
      <div style="display:flex;gap:22px;margin-top:20px">{group("A", "8u00", "28")}{group("B", "8u30", "24")}</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:28px;margin-top:22px;text-align:left">
        {qr}
        <div style="max-width:250px">
          <div class="s" style="font-size:64px;color:{RED}">Scan mij!</div>
          <div style="font-size:20px;line-height:1.4;margin-top:4px">Alle info, en vraag meteen toegang tot onze <span style="white-space:nowrap">WhatsApp-groep</span>.</div>
        </div>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:18px;margin-top:26px">
      <img src="{LOGO}" style="width:80px;height:80px">
      <div style="text-align:left">
        <div style="font-size:22px">Volg de club: <b>@cyclingclubwaregem</b></div>
        <div style="font-size:17px;opacity:.8;margin-top:3px">Save the date: Lamett Classic &middot; 3 &amp; 4 juli 2027</div>
      </div>
    </div>
  </div>
</div>"""


def menu_post():
    """'Wat schenken we?': the drinks list as an Instagram/Facebook post, like a chalkboard menu."""
    w, h = 1080, 1350
    band, band_h = knit(76, w / 76)
    section = lambda title, items: (
        f'<div style="margin-bottom:26px"><div class="rb t" style="font-size:40px;letter-spacing:.05em"><span>{title}</span></div>'
        f'<div style="font-size:33px;font-weight:500;line-height:1.42;margin-top:14px">{"".join(f"<div>{i}</div>" for i in items)}</div></div>')
    column = lambda sections: f'<div style="width:420px">{"".join(section(t, i) for t, i in sections)}</div>'
    return f"""<div class="canvas">{defs()}
  {snowfall(w, h - band_h, 60, 6, 41, .86)}
  {garland(w, 171, -22, 43, 5, 5, .65, 42, .55)}
  {garland(w, 171, -9, 56, 4, 6, .9, 43)}
  <div class="flow" style="top:86px">
    {kicker(.86, KICKER + " &middot; 5 december")}
    <div class="s" style="font-size:122px;color:{GOLD};transform:rotate(-3deg);margin-top:18px">Wat schenken we?</div>
    <div style="display:flex;gap:70px;margin-top:36px">{column(MENU_LEFT)}{column(MENU_RIGHT)}</div>
    {section(*MENU_BOTTOM)}
    <div style="display:flex;align-items:center;gap:18px;margin-top:6px;text-align:left">
      <img src="{LOGO}" style="width:78px;height:78px">
      <div><div style="font-size:26px;font-weight:700">De chalet van Cycling Club Waregem</div>
      <div style="font-size:23px;opacity:.85;margin-top:2px">Zaterdag 5 december &middot; {HOURS} &middot; ijspiste op de Markt</div></div>
    </div>
  </div>
  {shade("bottom", band_h)}
  <div style="position:absolute;left:0;right:0;bottom:0">{band}</div>
</div>"""


# ---- QR code and rendering ------------------------------------------------------------------
def qr_svg(url, size, color=INK):
    """QR code as crisp SVG, generated by macOS CoreImage (no packages needed)."""
    js = WORK / "qr.js"
    js.write_text("""ObjC.import('CoreImage'); ObjC.import('AppKit');
function run(argv) {
  const f = $.CIFilter.filterWithName('CIQRCodeGenerator');
  f.setValueForKey($(argv[0]).dataUsingEncoding($.NSUTF8StringEncoding), 'inputMessage');
  f.setValueForKey($('M'), 'inputCorrectionLevel');
  const rep = $.NSBitmapImageRep.alloc.initWithCIImage(f.outputImage);
  const rows = [];
  for (let y = 0; y < rep.pixelsHigh; y++) { let r = '';
    for (let x = 0; x < rep.pixelsWide; x++) r += rep.colorAtXY(x, y).brightnessComponent < .5 ? '1' : '0';
    rows.push(r); }
  return rows.join('\\n');
}""")
    rows = subprocess.run(["osascript", "-l", "JavaScript", str(js), url], check=True, capture_output=True, text=True).stdout.split()
    while rows and "1" not in rows[0]: rows.pop(0)
    while rows and "1" not in rows[-1]: rows.pop()
    first = min(r.index("1") for r in rows if "1" in r)
    last = max(r.rindex("1") for r in rows if "1" in r)
    rows = [r[first:last + 1] for r in rows]
    n, q = len(rows), 4
    path = "".join(f"M{x + q} {y + q}h1v1h-1z" for y, r in enumerate(rows) for x, c in enumerate(r) if c == "1")
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 {n + 2 * q} {n + 2 * q}" shape-rendering="crispEdges" style="flex:none;border-radius:10px">'
            f'<rect width="100%" height="100%" fill="#fff"/><path d="{path}" fill="{color}"/></svg>')

def png(name, html, w, h, scale=1):
    src = WORK / f"{name}.html"
    src.write_text(html)
    shot = WORK / f"{name}-shot.png"
    # The headless window loses ~85 px to its frame, so render taller and crop
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--force-device-scale-factor={scale}",
                    f"--window-size={w},{h + 200}", "--virtual-time-budget=5000", f"--screenshot={shot}", src.as_uri()],
                   check=True, capture_output=True)
    subprocess.run(["magick", str(shot), "-crop", f"{int(w * scale)}x{int(h * scale)}+0+0", "+repage", "-strip",
                    str(OUT / f"{name}.png")], check=True)
    print("png", name)

def pdf(name, html):
    src = WORK / f"{name}.html"
    src.write_text(html)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=5000",
                    f"--print-to-pdf={OUT / (name + '.pdf')}", src.as_uri()], check=True, capture_output=True)
    print("pdf", name)


OUT.mkdir(parents=True, exist_ok=True)
MM = 96 / 25.4  # CSS px per mm
only = set(sys.argv[3:])  # optional: render only some designs while tweaking
want = lambda name: not only or name in only

a3w, a3h = 297 * MM, 420 * MM
if want("affiche"):
    a3 = portrait(a3w, a3h, 1, top=112, gaps=(10, 34, 34, 24, 34), illus_w=990, lead_px=104, head_px=184, rib_px=74, cols=70, seed=1)
    pdf("affiche-a3", page(a3, 297, 420, "mm", pdf=True))
    png("affiche", page(a3, int(a3w), int(a3h)), int(a3w), int(a3h), scale=2)
POST = dict(w=1080, h=1350, s=.86, top=84, gaps=(4, 16, 22, 14, 16), illus_w=860, lead_px=88, head_px=160, rib_px=62, cols=76, seed=2, lights_r=.9)
STORY = dict(w=1080, h=1920, s=.96, top=270, gaps=(20, 62, 56, 36, 66), illus_w=980, lead_px=104, head_px=178, rib_px=72, cols=70, seed=4)
if want("post"):
    png("post-instagram", page(portrait(**POST), 1080, 1350), 1080, 1350)
if want("story"):
    png("story-instagram", page(portrait(**STORY), 1080, 1920), 1080, 1920)
if want("facebook"):
    png("facebook-evenement", page(facebook_cover(), 1920, 1005), 1920, 1005)
if want("toogkaart"):
    sign = counter_sign(qr_svg(RIDE_URL, 210))
    pdf("toogkaart-a4", page(sign, 210, 297, "mm", pdf=True))
    png("toogkaart", page(sign, int(210 * MM), int(297 * MM)), int(210 * MM), int(297 * MM), scale=2)
if want("drankkaart"):
    png("drankkaart-instagram", page(menu_post(), 1080, 1350), 1080, 1350)

# Looping ad videos (8 s): only when asked for with the extra argument "video", because they take a minute or two.
# Frames come from Chrome (capture.mjs, needs Node 22+), the MP4 from macOS AVFoundation (encode.swift): nothing to install.
if "video" in only:
    here, seconds, fps = pathlib.Path(__file__).resolve().parent, 8, 30
    encoder = WORK / "encode"
    subprocess.run(["swiftc", "-O", str(here / "encode.swift"), "-o", str(encoder)], check=True)
    for name, args in [("video-story", STORY), ("video-post", POST)]:
        src = WORK / f"{name}.html"
        src.write_text(page(portrait(**args, anim=True) + f"<script>{ANIM_JS.replace('SECONDS', str(seconds))}</script>",
                            args["w"], args["h"]))
        frames = WORK / f"{name}-frames"
        subprocess.run(["node", str(here / "capture.mjs"), CHROME, str(src), str(frames), str(args["w"]), str(args["h"]),
                        str(seconds * fps), str(seconds)], check=True)
        subprocess.run([str(encoder), str(frames), str(OUT / f"{name}.mp4"), str(fps)], check=True)
        print("video", name)
