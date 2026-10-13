"""Lotus E-2 card scenes. There's no app design yet, so these are drawn with
the site's own iOS components: the search form, results by app, the report
summary, privacy settings and the "before you talk" guidance."""

SEARCH = '''<div class="list form">
  <div class="list-row"><span class="badge icon" style="--c: var(--accent-blue)">person</span><div class="main"><span>Name</span><b>Alex</b></div></div>
  <div class="list-row"><span class="badge icon" style="--c: var(--accent-blue)">cake</span><div class="main"><span>Age</span><b>29 – 33</b></div></div>
  <div class="list-row"><span class="badge icon" style="--c: var(--accent-blue)">location_on</span><div class="main"><span>Area</span><b>Canggu · 10 km</b></div></div>
  <div class="go"><div class="big-button" style="--c: var(--accent-purple)"><span class="icon">search</span>Search 7 apps</div></div>
</div>'''

RESULTS = '''<div class="list results">
  <div class="list-row"><span class="badge icon" style="--c: var(--accent-pink)">favorite</span><div class="main"><b>Dating app 1</b><span>Searched public profiles</span></div><span class="pill" style="--c: var(--accent-green)">Clear</span></div>
  <div class="list-row flag" style="--c: var(--accent-orange)"><span class="badge solid icon" style="--c: var(--accent-orange)">favorite</span><div class="main"><b>Dating app 2</b><span>Possible match · active this week</span></div><span class="pill solid" style="--c: var(--accent-orange)">Review</span></div>
  <div class="list-row"><span class="badge icon" style="--c: var(--accent-purple)">favorite</span><div class="main"><b>Dating app 3</b><span>Searched public profiles</span></div><span class="pill" style="--c: var(--accent-green)">Clear</span></div>
  <div class="list-row"><span class="badge icon" style="--c: var(--accent-blue)">more_horiz</span><div class="main"><b>4 more apps</b><span>All clear</span></div></div>
</div>'''

REPORT = '''<div class="panel report">
  <div class="result-head">
    <span class="avatar-blur" aria-hidden="true"></span>
    <div style="flex: 1"><b>Report summary</b><div class="ui-sub">Alex, 31 · Canggu</div></div>
    <span class="pill solid" style="--c: var(--accent-orange)">1 match</span>
  </div>
  <div class="stat-tiles">
    <div class="stat-tile"><div class="num">7</div><div class="lbl">Apps checked</div></div>
    <div class="stat-tile"><div class="num" style="color: var(--accent-orange)">1</div><div class="lbl">Possible match</div></div>
    <div class="stat-tile"><div class="num">7<small>d</small></div><div class="lbl">Last active</div></div>
  </div>
  <div class="conf"><span class="ui-label">Match confidence</span><b class="rounded">Medium</b></div>
  <div class="meter"><i style="--w: 58%; --c: var(--accent-orange)"></i></div>
</div>'''

TALK = '''<div class="list talk">
  <div class="list-head"><span>Before you talk</span><span class="icon" style="font-size: 16px">favorite</span></div>
  <div class="list-row"><span class="badge icon" style="--c: var(--accent-purple)">self_improvement</span><div class="main"><b>Take a moment first</b><span>A match isn’t proof of anything</span></div></div>
  <div class="list-row"><span class="badge icon" style="--c: var(--accent-blue)">forum</span><div class="main"><b>Ask, don’t accuse</b><span>Open questions keep things calm</span></div></div>
  <div class="list-row"><span class="badge icon" style="--c: var(--accent-green)">support_agent</span><div class="main"><b>Get support</b><span>People you trust, or a counsellor</span></div></div>
</div>'''

CARDS = {
    # Just the right person
    1: f'<div class="center">{SEARCH}</div>',
    # One search, every popular app
    2: f'''
<div class="center">
  <div class="radar"><span class="blip" style="left: 30%; top: 34%; --c: var(--accent-pink)"></span><span class="blip" style="left: 72%; top: 40%; --c: var(--accent-orange)"></span><span class="blip" style="left: 58%; top: 76%; --c: var(--accent-purple)"></span><span class="core icon">travel_explore</span></div>
  {RESULTS}
</div>
''',
    # A straight answer
    3: f'<div class="center">{REPORT}</div>',
    # Only you see your searches
    4: '''
<div class="center">
  <div class="settings">
    <span class="ui-label">Your searches</span>
    <div class="list">
      <div class="set-row"><span class="badge icon" style="--c: var(--accent-green)">lock</span><span class="lbl">Stored on this iPhone only</span><span class="pill" style="--c: var(--accent-green)">On</span></div>
      <div class="set-row"><span class="badge icon" style="--c: var(--accent-blue)">face</span><span class="lbl">Face ID to open</span><span class="toggle on"></span></div>
      <div class="set-row"><span class="badge icon" style="--c: var(--accent-indigo)">visibility_off</span><span class="lbl">Hide from app switcher</span><span class="toggle on"></span></div>
    </div>
    <div class="list"><div class="set-row danger"><span class="badge icon" style="--c: var(--accent-red)">delete</span><span class="lbl">Delete all searches</span></div></div>
  </div>
</div>
''',
    # Help with the hard conversation
    5: f'''
<div class="center">
  {TALK}
  <div class="panel support">
    <span class="ui-label">Talk to someone</span>
    <div class="sup"><span class="badge icon" style="--c: var(--accent-pink)">call</span><div><b>Relationship helpline</b><span>Free · 24 hours</span></div></div>
    <div class="sup"><span class="badge icon" style="--c: var(--accent-blue)">chat</span><div><b>Text a counsellor</b><span>Usually replies in minutes</span></div></div>
    <p class="gentle">A match is a starting point, not a verdict.</p>
  </div>
</div>
''',
    # No hacking, ever
    6: '''
<div class="center">
  <div class="list checks">
    <div class="check-row"><span class="box icon">check</span><div class="main"><b>Public profiles</b><span>What anyone can already see</span></div></div>
    <div class="check-row no"><span class="box icon">close</span><div class="main"><b>No logins</b><span>We never sign in as anyone</span></div></div>
    <div class="check-row no"><span class="box icon">close</span><div class="main"><b>No private messages</b><span>Chats stay private</span></div></div>
  </div>
</div>
''',
    # Clarity without the stress
    7: f'''
<div class="center trio">
  <div class="step-card"><span class="step-n">1 · Search</span>{SEARCH}</div>
  <div class="step-card"><span class="step-n">2 · Report</span>{REPORT}</div>
  <div class="step-card"><span class="step-n">3 · Next steps</span>{TALK}</div>
</div>
''',
}
