"""TLDR NEWS card scenes (the app's working name is Underneath): every story
is a bill pasted on a limewashed wall. The rumour is on the front, the
checked story is painted underneath, and each story carries its mark."""

RUMOURS = (
    ("BANJIR!!", "is it true?", ""), ("BBM NAIK??", "forwarded many times", ""),
    ("Rp600RB??", "for everyone, click the link", "red"), ("KRL CHAOS??", "who else saw this", ""),
    ("OJOL PAY CUT!!", "pls share", ""), ("RUPIAH CRASH??", "watch till the end", ""),
    ("MRT SHUT??", "#trending", ""), ("BREAKING!!", "share before deleted", ""),
)
STORIES = (
    ("dev", "Developing", "Floods close three roads in North Jakarta"),
    ("ok", "Confirmed", "Fuel goes up 8% on Monday"),
    ("un", "Unverified", "No source backs the “Rp 600k aid” message"),
    ("ok", "Confirmed", "Late KRL trains added on the Bogor line"),
    ("dev", "Developing", "New rules for ojol driver pay announced"),
    ("ok", "Confirmed", "Rupiah holds steady against the dollar"),
    ("ok", "Confirmed", "MRT extension opens two stations"),
    ("ok", "Confirmed", "Indonesia names its Asian Cup squad"),
)
TILT = (-3, 2.5, 1.5, -2, 2, -2.5, -1.5, 2)


def rumour(i, style=""):
    head, sub, cls = RUMOURS[i]
    return f'<div class="bill rum {cls}" style="--r: {TILT[i]}deg; {style}"><b>{head}</b><small>{sub}</small></div>'


def story(i, style="", cls=""):
    sig, word, head = STORIES[i]
    return f'<div class="bill story {cls}" style="--r: {TILT[i] / 2}deg; {style}"><span class="sig {sig}"><i></i>{word}</span><b>{head}</b></div>'


def wall(items, cls=""):
    return f'<div class="grid {cls}">{"".join(items)}</div>'


CARDS = {
    # No feed, no pile
    1: f'''
<div class="surface wall"></div>
<div class="count"><span class="since">Since 21:00</span><s>3,140 stories</s><span class="big"><em>8</em> matter.</span></div>
{wall([rumour(i) for i in range(8)], cls="eight")}
''',
    # The rumour is the bill
    2: f'''
<div class="surface wall"></div>
{rumour(1, "left: 6%; top: 10%; width: 40%")}
{rumour(2, "left: 50%; top: 6%; width: 44%")}
{rumour(0, "left: 9%; top: 52%; width: 36%")}
{rumour(3, "left: 53%; top: 50%; width: 40%")}
<span class="hint">Red belongs only to the noise</span>
''',
    # The checked story is underneath
    3: f'''
<div class="surface wall"></div>
{story(1, "left: 12%; top: 12%; width: 76%; height: 72%", cls="under")}
<div class="peel" style="left: 12%; top: 12%; width: 76%; height: 72%">
  <div class="front"><b>BBM NAIK??</b><small>forwarded many times</small></div>
  <span class="curl"></span>
</div>
''',
    # Every story carries its mark
    4: '''
<div class="surface wall"></div>
<div class="marks">
  <div class="bill story" style="--r: -1.5deg"><span class="sig ok"><i></i>Confirmed</span><b>Fuel goes up 8% on Monday</b><small>Kompas · Detik · Antara</small></div>
  <div class="bill story" style="--r: 1deg"><span class="sig dev"><i></i>Developing</span><b>Floods close three roads in North Jakarta</b><small>Antara · CNN Indonesia</small></div>
  <div class="bill story" style="--r: -.5deg"><span class="sig un"><i></i>Unverified</span><b>No source backs the “Rp 600k aid” message</b><small>cekfakta.com</small></div>
  <div class="bill story struck" style="--r: 1.5deg"><span class="sig no"><i></i>False</span><b>Free data for everyone this weekend</b><small>TurnBackHoax</small></div>
</div>
''',
    # Share the checked version
    5: '''
<div class="surface wall"></div>
<div class="bill story checked" style="--r: -2deg">
  <span class="sig un"><i></i>Unverified · checked 7:04</span>
  <b>No source backs the “Rp 600k aid” message</b>
  <p>No ministry has announced it. The link asks for an ID number.</p>
  <span class="why">Why it matters</span><p>Do not enter any details.</p>
  <small>cekfakta.com · TurnBackHoax · AI draft, editor-checked</small>
</div>
<div class="chat" style="--r: 1.5deg">
  <div class="chat-hd"><i></i><span><b>Family</b><small>12 members</small></span></div>
  <div class="bubble in"><small>Tante Sri · forwarded many times</small><span class="noise">BREAKING!! Rp600rb for everyone, click before it’s deleted 🙏</span></div>
  <div class="bubble out"><span class="sig un"><i></i>Unverified · checked 7:04</span><b>No source backs the “Rp 600k aid” message</b><small>Underneath · cekfakta.com</small></div>
  <div class="bubble in short"><small>Mum</small>Ok, deleted 🙏</div>
</div>
''',
    # Jakarta and his topics
    6: '''
<div class="surface wall"></div>
<div class="city"><span class="since">Your city</span><b>Jakarta</b><small>Using your location · change any time</small></div>
<div class="topics">
  <span class="on">✓ Money</span><span class="on">✓ Transport</span><span class="on">✓ Work</span>
  <span>Weather</span><span class="on">✓ Tech</span><span>Sport</span><span>Politics</span><span>Culture</span>
</div>
''',
    # The end is visible
    7: f'''
<div class="edition" style="left: 2%">
  <div class="surface wall"></div>
  <div class="count small"><span class="since">3 of 8 read</span><span class="big"><em>5</em> left.</span></div>
  {wall([story(i) if i < 3 else rumour(i) for i in range(8)], cls="eight mini")}
</div>
<div class="edition" style="left: 34.66%">
  <div class="surface wall"></div>
  <div class="count small"><span class="since">7 of 8 read</span><span class="big"><em>1</em> left.</span></div>
  {wall([story(i) if i != 6 else rumour(i) for i in range(8)], cls="eight mini")}
</div>
<div class="edition clean" style="left: 67.33%">
  <div class="surface wall"></div>
  <div class="light"></div>
  <div class="count small"><span class="since">8 of 8 · 2 min 40 s</span><span class="big clean-word"><em>Clean.</em></span><small class="caught">48,210 in Jakarta caught up</small></div>
  <span class="painted">Edition · Fri 7:05</span>
</div>
''',
}
