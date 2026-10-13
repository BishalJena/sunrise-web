"""HUSH card scenes: the live camera of a stranger's room, cold until she has
looked; a paper door hanger that hangs from the top and tells the truth; small
paper tags for the devices on the room's Wi-Fi; and the written report."""


def hanger(title, sub="", cls="", style="", body=""):
    return f'''<div class="hgr {cls}" style="{style}">
  <span class="string"></span>
  <div class="hcard"><span class="stitch"></span><b class="t">{title}</b>{f'<span class="u">{sub}</span>' if sub else ""}{body}</div>
</div>'''


def room(img, cls="", style=""):
    return f'<div class="pic cam {cls}" style="{style}"><img src="assets/art/img/{img}.webp" alt=""></div>'


CARDS = {
    # The room warms as she checks
    1: f'''
{room("room-cold")}
<div class="pic cam warm"><img src="assets/art/img/room-warm.webp" alt=""></div>
{hanger("Looking…", "slowly is perfect", cls="small sway", body='<span class="bar"><i></i></span>')}
''',
    # Ordinary things are named ordinary
    2: f'''
{room("room-warm", style="--pos: 50% 70%")}
<span class="dtag" style="left: 8%; top: 22%"><i></i>Router · ordinary</span>
<span class="dtag" style="left: 46%; top: 12%"><i></i>Speaker · ordinary</span>
<span class="dtag" style="left: 30%; top: 46%"><i></i>Lamp · ordinary</span>
<span class="dtag" style="left: 6%; top: 74%"><i></i>TV · ordinary</span>
<span class="dtag odd" style="right: 6%; top: 62%"><i></i>Unknown device · worth a look</span>
''',
    # A closer look, not an alarm
    3: f'''
{room("smoke-detector", style="--pos: 50% 55%")}
<span class="ring" style="left: 50%; top: 66%"></span>
{hanger("Hold toward it", "from the bed · 3 s", cls="small", style="left: 22%", body='<span class="bar"><i style="--to: .7"></i></span>')}
<span class="caption" style="right: 7%; bottom: 8%">The smoke detector<small>above the bed</small></span>
''',
    # The exposed places are checked
    4: f'''
{room("shower", style="--pos: 50% 45%")}
{hanger("Now the shower", "from where you stand · 3 s", cls="small", style="left: 26%", body='<span class="bar"><i style="--to: .5"></i></span>')}
<div class="spots">
  <span class="chk done"><i>✓</i>From the bed</span>
  <span class="chk now"><i></i>From the shower</span>
</div>
''',
    # The hanger tells the truth
    5: f'''
{room("room-warm", style="--pos: 50% 70%")}
{hanger("Just you in here.", "Nothing we could find can see or hear you.", cls="big", style="left: 27%", body='<span class="hand">for Amara · 22:15</span><span class="b1">Settle in</span>')}
{hanger("The smoke detector can see the bed.", "", cls="big dark", style="left: 73%", body='<span class="ev"></span><span class="u">Evidence saved at 22:16. Your report is written.</span><span class="b1">Review report</span>')}
''',
    # Nothing is stored by default
    6: f'''
{room("room-cold", style="--pos: 50% 70%")}
{hanger("Yours to keep.", "Nothing is stored or uploaded unless you share it.", cls="big solo", body='<span class="b1">Leave it here</span><span class="b2">Share report</span>')}
''',
    # Written for the host, Airbnb, or a friend
    7: '''
<div class="surface paperbg"></div>
<div class="rep" style="--r: -1.5deg">
  <span class="k found">Hush · room check report · found</span>
  <h3>A device can see the bed.</h3>
  <span class="hand">Amara · 11 Oct 2026 · 22:16</span>
  <span class="evi"></span>
  <div class="row"><span>What</span><span>lens in the smoke detector</span></div>
  <div class="row"><span>Where</span><span>ceiling, above the bed</span></div>
  <div class="row"><span>Not checked</span><span>devices on another network</span></div>
</div>
<div class="sharesheet" style="--r: 1deg">
  <div class="sh-hd"><i></i><span><b>Hush room check</b><small>PDF · 2 photos</small></span></div>
  <div class="apps"><span><i style="--c: #FF5A5F"></i>Airbnb</span><span><i style="--c: #25D366"></i>WhatsApp</span><span><i style="--c: #1E7CF2"></i>Mail</span><span><i style="--c: #34C759"></i>Messages</span></div>
</div>
<div class="msg" style="--r: -1deg">
  <span class="to">To: Host · Airbnb</span>
  <p>Hi, I found a camera lens in the smoke detector above the bed (photo attached). Please explain.</p>
  <p class="pt">Olá, encontrei uma câmara no detetor de fumo…</p>
</div>
''',
}
