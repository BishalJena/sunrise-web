"""KESHA card scenes: the flame in its bowl, in the mood each moment calls
for (rendered from the app's own flame.js), with the Dynamic Island, the
road strip to Eldoret, the big awake button and the CarPlay screen."""

FONTS = (
    "https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@800;900&family=IBM+Plex+Mono:wght@500;600&family=Caveat:wght@700&display=swap",
)


def flame(mood, cls="", style=""):
    return f'<img class="flame {mood} {cls}" src="assets/art/img/flame-{mood}.svg" alt="" style="{style}">'


def island(text, cls=""):
    bars = '<span class="bars"><i></i><i></i><i></i><i></i></span>' if "listen" in cls else ""
    return f'<div class="isl {cls}"><span class="drop"></span><span>{text}</span>{bars}</div>'


def road(at, hot=None, ok=()):
    spots = "".join(
        f'<span class="sp{" hot" if n == hot else ""}{" ok" if n in ok else ""}" style="left: {x}%"><b>{n}{" ✓" if n in ok else ""}</b></span>'
        for n, x in (("Salgaa", 56), ("Sachangwan", 84)))
    return f'''<div class="road"><span class="end">Nairobi</span><span class="end r">Eldoret</span>
  <span class="ln"></span><span class="done" style="width: {at}%"></span>{spots}<span class="me" style="left: {at}%"></span></div>'''


CARDS = {
    # It starts with his name and route
    1: f'''
<div class="surface night"></div>
{island("Eldoret · 310 km")}
{flame("listen", style="--h: 52%")}
<div class="say"><span class="cap">Friday night.<br>Eldoret again?</span><span class="reply">“Yeah” · <em>0.6 s</em></span></div>
''',
    # The flame moves with the drive
    2: f'''
<div class="surface night"></div>
<div class="moment" style="left: 4%">
  {island("Salgaa · 48 km")}
  {flame("dance", cls="dancing", style="--h: 62%")}
  <div class="say"><span class="cap s">Malaika</span><span class="sub">Nyashinski</span></div>
  <div class="np"><span class="eq"><i></i><i></i><i></i></span>Suzanna · Sauti Sol</div>
</div>
<div class="moment" style="right: 4%">
  {island("Listening", cls="listen")}
  {flame("listen", cls="rising", style="--h: 66%")}
  <div class="say"><span class="cap s">Still with<br>me, Ken?</span></div>
  <div class="np paused"><span class="eq"><i></i><i></i><i></i></span>music ducked</div>
</div>
''',
    # When replies slow, the flame rises
    3: f'''
<div class="surface night warm"></div>
{island("Talk to me", cls="hot")}
{flame("nag", cls="throb", style="--h: 66%")}
<div class="say"><span class="cap">Talk to me.</span><span class="sub">Best thing you ate this week?</span><span class="reply slow">Reply 3.4 s · <em>slow</em></span></div>
''',
    # One huge awake check
    4: f'''
<div class="surface night ember"></div>
{island("Tap if awake", cls="hot")}
{flame("nag", cls="throb small", style="--h: 42%")}
<div class="say high"><span class="cap s">Tap if<br>you’re awake.</span></div>
<div class="awake"><b>I’m awake</b></div>
<span class="mono foot">No tap in 10 s, and I get louder.</span>
''',
    # Eyes up before the dangerous stretch
    5: f'''
<div class="surface night blood"></div>
<div class="moment" style="left: 4%">
  {island("Salgaa · 3 km", cls="hot")}
  {flame("spot", style="--h: 66%")}
  <div class="say"><span class="cap s">Salgaa.<br>Eyes up.</span><span class="sub">Black spot · bends and trucks</span></div>
</div>
<div class="moment" style="right: 4%">
  <div class="spotcard"><span class="k">Next black spot</span><b>Salgaa</b><span class="km">3<small>km</small></span></div>
  {road(52, hot="Salgaa")}
  <div class="spotcard calm"><span class="k">After that</span><b>Sachangwan</b><span class="km">31<small>km</small></span></div>
</div>
''',
    # A voice note from family
    6: f'''
<div class="surface night rose"></div>
{flame("ded", style="--h: 52%")}
<div class="say"><span class="ded">for Ken<small>from Wanjiru, with love</small></span>
<span class="vwave"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></span>
<span class="cap s quote">“Drive safe, baba.”</span></div>
''',
    # Now Playing becomes the co-driver
    7: f'''
<div class="surface night"></div>
<div class="cpl">
  <div class="cp-side"><span class="cp-time">03:20</span><i></i><i class="lit"></i><i></i><i class="sq"></i></div>
  <div class="cp-map">
    <div class="cp-turn"><b>Continue on A104</b><small>Salgaa · 3 km</small></div>
    <svg viewBox="0 0 100 100" preserveAspectRatio="none"><path class="old" d="M-10 70 C 20 60, 40 80, 110 40"/><path class="old" d="M-5 20 C 30 40, 60 10, 110 30"/><path class="rt" d="M38 104 L38 78 C38 60, 50 56, 64 46 C78 36, 84 20, 90 -4"/></svg>
    <span class="cp-me"></span>
    <small class="cp-note">Your navigation app stays in charge.</small>
  </div>
  <div class="cp-col">
    <div class="cp-np">
      <div class="cp-art">{flame("spot", style="--h: 92%")}<b>Salgaa · 3 km</b></div>
      <b class="cp-t">Salgaa · eyes up</b><small>Kesha · black spot</small>
      <span class="cp-ctl">⏮ ⏸ ⏭</span>
    </div>
    <div class="cp-warn"><span class="drop"></span><span><small>Black spot · bends + trucks</small><b>Salgaa</b></span><span class="km">3 km</span></div>
  </div>
</div>
''',
}
