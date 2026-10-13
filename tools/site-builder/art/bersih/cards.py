"""BERSIH card scenes: every photo is a print on a table. The front is the
image, the back holds the private details in ballpoint, and the app speaks
through a photo-lab envelope with a red band."""

MAP = '''<svg class="pmap" viewBox="0 0 90 68" aria-hidden="true"><g opacity=".13">
<rect x="3" y="3" width="22" height="16" rx="1.5"/><rect x="30" y="3" width="28" height="16" rx="1.5"/><rect x="63" y="3" width="24" height="16" rx="1.5"/>
<rect x="3" y="25" width="18" height="20" rx="1.5"/><rect x="26" y="25" width="24" height="20" rx="1.5"/><rect x="55" y="25" width="14" height="20" rx="1.5"/>
<rect x="74" y="25" width="13" height="20" rx="1.5"/><rect x="3" y="51" width="30" height="14" rx="1.5"/><rect x="38" y="51" width="20" height="14" rx="1.5"/><rect x="63" y="51" width="24" height="14" rx="1.5"/></g>
<g class="roads"><path d="M1 22 C30 21 58 23 89 21"/><path d="M1 48 C30 47 58 49 89 47"/><path d="M27 1 C27.5 24 26.5 46 27.5 67"/><path d="M60 1 C59.5 24 60.5 46 59.5 67"/></g>
<g transform="translate(44 36)"><circle r="9" class="mpin" opacity=".15"/><path class="mpin" d="M0 4 C-6 -3 -6 -9 0 -11.5 C6 -9 6 -3 0 4Z"/><circle cy="-6" r="2" fill="#F6F1E7"/></g></svg>'''

BACK = ("Jl. Kemang Raya 12", "Fri 10 Oct · 21:40", "iPhone 15 Pro")


def front(photo="glass", style="", cls="", extra=""):
    return f'<div class="pr front {cls}" style="{style}"><div class="img" style="background-image: url(assets/art/img/{photo}.webp)"></div>{extra}</div>'


def back(lines=BACK, style="", cls="", map=True):
    text = "".join(f'<span class="ln">{l}</span>' for l in lines)
    return f'<div class="pr back {cls}" style="{style}"><div class="lines">{text}</div>{MAP if map else ""}</div>'


def envelope(band, count, say, button=None, window="glass", style="", cls=""):
    win = f'<div class="win" style="background-image: url(assets/art/img/{window}.webp)"></div>' if window else '<div class="win empty"></div>'
    go = f'<div class="go"><span>{button}</span><span>→</span></div>' if button else ""
    return f'''<div class="env {cls}" style="{style}">
  <div class="band"><span>{band}</span><small>{count}</small></div>
  <div class="body"><div class="say">{say}{go}</div>{win}</div>
</div>'''


CARDS = {
    # A photo turns over like a print
    1: f'''
<div class="surface table"></div>
<div class="flip">
  <div class="flip-in">
    {front("glass", cls="side")}
    {back(cls="side rear")}
  </div>
</div>
<span class="hand" style="left: 8%; top: 9%">the front<br>is the image</span>
<span class="hand" style="right: 7%; bottom: 14%">the back<br>is private</span>
''',
    # Where, when, and on which phone
    2: f'''
<div class="surface table"></div>
{back(style="left: 8%; top: 9%; --r: -4deg", cls="big")}
<div class="fields">
  <div class="field"><b>Location</b><span>Jl. Kemang Raya 12, Jakarta</span></div>
  <div class="field"><b>Date and time</b><span>Friday 10 October, 21:40</span></div>
  <div class="field"><b>Phone</b><span>iPhone 15 Pro · main camera</span></div>
  <div class="field"><b>Software</b><span>iOS 18.6 · Photos</span></div>
</div>
''',
    # The words go home
    3: f'''
<div class="surface table"></div>
{back(style="left: 7%; top: 12%; --r: -5deg", cls="mid")}
{back(lines=("", "", ""), style="right: 7%; top: 24%; --r: 4deg", cls="mid blank", map=False)}
<div class="flying" aria-hidden="true">
  <i style="--x: 58%; --y: 30%; --d: 0s">K</i><i style="--x: 63%; --y: 40%; --d: .3s">e</i><i style="--x: 55%; --y: 50%; --d: .6s">m</i>
  <i style="--x: 62%; --y: 60%; --d: .9s">a</i><i style="--x: 52%; --y: 68%; --d: 1.2s">n</i><i style="--x: 58%; --y: 20%; --d: 1.5s">g</i>
</div>
''',
    # Clean where she already shares
    4: '''
<div class="pic share-photo"><img src="assets/art/img/glass.webp" alt=""></div>
<div class="share">
  <div class="grab"></div>
  <div class="sh-hd"><i style="background-image: url(assets/art/img/glass.webp)"></i><span><b>1 Photo Selected</b><small>Options ›</small></span></div>
  <div class="apps"><span><i style="--c: #34C759"></i>Messages</span><span><i style="--c: #25D366"></i>WhatsApp</span><span><i style="--c: #1E7CF2"></i>Mail</span><span><i class="ig"></i>Instagram</span></div>
  <div class="acts">
    <div class="act on"><span>Clean Copy</span><i class="ic"></i></div>
    <div class="act"><span>Copy Photo</span><span class="gr">⧉</span></div>
    <div class="act"><span>Save to Files</span><span class="gr">▭</span></div>
  </div>
</div>
''',
    # Nothing is lost from her memory
    5: f'''
<div class="surface table"></div>
<div class="pair" style="left: 7%">
  {back(style="--r: -4deg", cls="mid")}
  <span class="tag">In her library<small>back intact</small></span>
</div>
<div class="pair" style="right: 7%">
  {back(lines=("", "", ""), style="--r: 3deg", cls="mid blank", map=False)}
  <span class="tag red">The copy<small>blank back</small></span>
</div>
''',
    # Two seconds
    6: f'''
<div class="surface table"></div>
{back(style="left: 18%; top: 4%; --r: -3deg", cls="small fading")}
{envelope("Clean copy", "0:02", "Taking the back off…", window="glass", cls="timer")}
''',
    # One clean action for the media she posts
    7: f'''
<div class="surface table"></div>
<div class="group" style="left: 4%">
  {front("glass", style="--r: -9deg; left: 0; top: 10%", cls="stack")}
  {front("sunset", style="--r: -3deg; left: 8%; top: 7%", cls="stack")}
  {front("glass", style="--r: 4deg; left: 16%; top: 9%", cls="stack")}
  {back(lines=("", "", ""), style="--r: 8deg; left: 26%; top: 13%", cls="stack blank", map=False)}
  <span class="label">Four photos</span>
</div>
<div class="group" style="left: 37%">
  {front("sunset", style="--r: -2deg; left: 10%; top: 8%", cls="video", extra='<span class="play"></span><span class="dur">0:12</span>')}
  <span class="label">A video</span>
</div>
{envelope("Clean copy", "4 prints", "Four clean copies. The backs stay with you.", button="Share 4 copies", window="sunset", style="right: 4%", cls="share-again")}
''',
}
