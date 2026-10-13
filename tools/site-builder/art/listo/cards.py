"""LISTO card scenes, drawn from the app's own objects: the linen table, the
green passport, yellow luggage tags, dashed outlines for what's missing, the
red thread, the receipt slip, the airport photos and the yellow pass."""

CARDS = {
    # Built for restricted passports
    1: '''
<div class="surface linen"></div>
<div class="ppt lift" style="left: 9%; top: 16%; --r: -5deg"><span>Pasaporte</span><i></i><span>México</span></div>
<div class="ptag lift" style="right: 6%; top: 14%; --r: -6deg">MEX → IAH<small>Houston · change planes</small></div>
<div class="ptag lift" style="right: 10%; top: 40%; --r: 4deg">IAH → YYZ<small>Toronto · 14 Jun</small></div>
<div class="ptag pale lift" style="right: 16%; top: 65%; --r: -2deg">+ Add a stop</div>
''',
    # Documents appear on the linen table
    2: '''
<div class="surface linen"></div>
<div class="ppt" style="left: 5%; top: 12%; --r: -4deg"><span>Pasaporte</span><i></i><span>México</span></div>
<div class="visa lift" style="left: 30%; top: 9%; --r: 3deg"><b>US B1/B2</b>Valid to 2036</div>
<div class="visa eta lift" style="left: 33%; top: 47%; --r: -2deg"><b>eTA Canada</b>Linked to passport</div>
<div class="ins lift" style="left: 6%; top: 60%; --r: 2deg"><b>Insurance</b>AXA · €30k</div>
<div class="out wide" style="right: 5%; top: 12%"><b>Flight · MEX–IAH–YYZ</b>book once the visa is in</div>
<div class="ptag lift" style="right: 9%; top: 62%; --r: -5deg">$1,092 all in<small>about 4 months · start by 14 Jan</small></div>
''',
    # The red thread shows what blocks what
    3: '''
<div class="surface linen"></div>
<svg class="thread" viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M22 31 C 28 52, 46 44, 58 58" vector-effect="non-scaling-stroke"/></svg>
<div class="out wake" style="left: 8%; top: 8%"><b>US visa</b>3–14 months<br>blocks the transit</div>
<div class="out" style="left: 52%; top: 58%"><b>Canada eTA</b>minutes, once you<br>have the US visa</div>
<div class="knot" style="left: 22%; top: 31%"></div>
<div class="knot" style="left: 58%; top: 58%"></div>
''',
    # Time counts as a cost
    4: '''
<div class="surface linen"></div>
<div class="slip lift" style="left: 7%; top: 9%; --r: -1.5deg">
  <div class="l"><span>Flights MEX–IAH–YYZ</span><span>$612</span></div>
  <div class="l"><span>US visa (fee + integrity fee)</span><span>$435</span></div>
  <div class="l"><span>Canada eTA</span><span>C$7</span></div>
  <div class="l"><span>Travel insurance</span><span>$38</span></div>
  <div class="t"><span>Total</span><span>$1,092</span></div>
</div>
<div class="ptag big swing" style="right: 6%; bottom: 10%; --r: -7deg">+ about 4 months<small>start the US visa by 14 Jan</small></div>
''',
    # The airport, step by step
    5: '''
<div class="walk" style="left: 0; --r: -1.5deg">
  <img src="assets/art/img/checkin.webp" alt="">
  <span class="where">Check-in,<br>Mexico City.</span>
  <div class="sg"><span class="n">1</span><span><b>They'll ask for</b><small>Passport · US visa (for Houston)</small></span><span class="st">✓ Ready</span></div>
</div>
<div class="walk second" style="right: 0; --r: 1.5deg">
  <img src="assets/art/img/passport-control.webp" alt="">
  <span class="where">US passport<br>control, Houston.</span>
  <div class="objs"><span class="ob p">Pasaporte</span><span class="ob v">US visa</span></div>
  <div class="sg"><span class="n">2</span><span><b>They'll ask for</b><small>Passport · US visa B1/B2</small></span><span class="st">✓ Ready</span></div>
</div>
''',
    # Rules with dates, not guesses
    6: '''
<div class="surface linen"></div>
<div class="sheet">
  <span class="k">US visa · B1/B2</span>
  <h3>Needed even to change planes.</h3>
  <div class="rw"><span>Why</span><span>No transit without a visa</span></div>
  <div class="rw"><span>Time</span><span>3–14 months</span></div>
  <div class="rw"><span>Fee</span><span>$185 + $250</span></div>
  <div class="rw"><span>Source</span><span>US State Dept</span></div>
  <div class="rw"><span>Checked</span><span>12 Jan</span></div>
  <div class="go"><span><b>Official site</b><small>ceac.state.gov</small></span><span>→</span></div>
</div>
''',
    # Something to show at check-in
    7: '''
<div class="pic counter"><img src="assets/art/img/counter.webp" alt=""></div>
<div class="pass lift" style="--r: -1.5deg">
  <div class="hd"><span>Show at check-in</span><span>Rishi · México</span></div>
  <div class="rt">MEX→YYZ</div>
  <div class="ls">✓ US visa: needed for Houston transit · State Dept<br>✓ Canada eTA: valid with US visa · IRCC<br>✓ Passport: valid beyond stay</div>
  <div class="qr"><i></i><span>Official rules and sources, checked 12 Jun. Scan to verify.</span></div>
</div>
<div class="agent lift" style="--r: 2deg">
  <span class="k">For the agent · US transit</span>
  <h3>A visa is required to transit the US.</h3>
  <div class="rw"><span>Holds</span><span>US B1/B2, valid to 2036</span></div>
  <div class="rw"><span>Source</span><span>US Department of State</span></div>
  <div class="rw"><span>Checked</span><span>12 Jun 2026</span></div>
</div>
''',
}
