"""Lotus G-1 card scenes. There's no app design yet, so these are drawn with
the site's own iOS components: the Live Activity on a Lock Screen, alert
banners, the speed gauge, the camera map and CarPlay."""

WAVE = "".join(f'<i style="--h: {h}px; --i: {i}"></i>' for i, h in enumerate((18, 30, 40, 24, 36, 40, 26, 34, 20, 30)))

CARDS = {
    # Always on your Lock Screen
    1: '''
<div class="bottom">
  <div class="wallpaper bleed lock">
    <span class="lock-time">9:41</span>
    <div class="island compact"><span class="la-sign sm">60</span><span class="rounded">850 m</span></div>
    <div class="live-activity">
      <div class="la-row"><span class="la-sign">60</span><div class="la-main"><b>Camera</b><span>Bypass Ngurah Rai</span></div><div class="la-dist">850<small>m</small></div></div>
      <div class="la-bar" style="--p: 62%"><i></i></div>
      <div class="la-foot"><span>You: 58 km/h</span><span style="color: var(--accent-green)">Within limit</span></div>
    </div>
  </div>
</div>
''',
    # Heard and seen
    2: f'''
<div class="center">
  <div class="notif-stack">
    <div class="notif"><img class="n-icon" src="assets/app-icon.svg" alt=""><div class="n-body"><div class="n-head"><b>Lotus G-1</b><time>now</time></div><p>Speed camera in 500 m. Limit 60 km/h.</p></div></div>
    <div class="notif"><img class="n-icon" src="assets/app-icon.svg" alt=""><div class="n-body"><div class="n-head"><b>Lotus G-1</b><time>2 km</time></div><p>Camera ahead in 2 km.</p></div></div>
  </div>
  <div class="device-panel alert-screen">
    <span class="big-icon icon">photo_camera</span>
    <h4>Camera in 500 m</h4>
    <p>Limit 60 km/h · you’re at 68</p>
    <div class="wave">{WAVE}</div>
    <span class="said">“Speed camera ahead. Ease off to sixty.”</span>
  </div>
</div>
''',
    # Knows when you're too fast
    3: '''
<div class="center col">
  <div class="gauge">
    <svg viewBox="0 0 200 120">
      <path d="M20 110a80 80 0 0 1 160 0" fill="none" stroke="var(--color-fill-3)" stroke-width="14" stroke-linecap="round"/>
      <path d="M20 110a80 80 0 0 1 160 0" fill="none" stroke="var(--accent-green)" stroke-width="14" stroke-linecap="round" stroke-dasharray="126 252"/>
      <path d="M20 110a80 80 0 0 1 160 0" fill="none" stroke="var(--accent-orange)" stroke-width="14" stroke-linecap="round" stroke-dasharray="0 126 26 252"/>
    </svg>
    <div class="gauge-read"><b>72</b><span>km/h · limit 60</span></div>
  </div>
  <div class="advice"><span class="icon">south</span><div><b>Ease off by 12 km/h</b><span>Camera in 1.4 km, or take Jl. Raya Kuta</span></div></div>
</div>
''',
    # Drivers looking out for drivers
    4: '''
<div class="center">
  <div class="list">
    <div class="list-row"><span class="badge solid icon" style="--c: var(--accent-blue)">local_police</span><div class="main"><b>Police check</b><span>Reported 4 min ago · 1.2 km</span></div><span class="pill" style="--c: var(--accent-blue)">+12</span></div>
    <div class="list-row"><span class="badge solid icon" style="--c: var(--accent-red)">photo_camera</span><div class="main"><b>New fixed camera</b><span>Confirmed by 8 drivers</span></div><span class="pill" style="--c: var(--accent-green)">✓ Verified</span></div>
    <div class="list-row"><span class="badge solid icon" style="--c: var(--accent-orange)">add</span><div class="main"><b>Report something</b><span>Takes one tap</span></div></div>
  </div>
</div>
''',
    # Built on a verified camera map
    5: '''
<div class="map fill" role="img" aria-label="Map of Bali with speed cameras along a route">
  <svg viewBox="0 0 400 225" preserveAspectRatio="none" aria-hidden="true">
    <path d="M60 -10 C 90 80, 150 140, 140 240" fill="none" stroke="var(--color-fill-3)" stroke-width="5"/>
    <path d="M250 -10 C 240 60, 300 120, 290 240" fill="none" stroke="var(--color-fill-3)" stroke-width="4"/>
    <path d="M-10 190 C 80 170, 110 120, 170 118 S 270 70, 410 40" fill="none" stroke="var(--brand)" stroke-width="7" stroke-linecap="round" opacity=".85"/>
  </svg>
  <span class="pin me" style="left: 12%; top: 80%"></span>
  <span class="pin icon" style="left: 42%; top: 52%">photo_camera</span>
  <span class="label" style="left: 42%; top: 62%">60 km/h</span>
  <span class="pin icon" style="left: 74%; top: 30%; --c: var(--accent-blue)">local_police</span>
  <span class="pin icon small" style="left: 86%; top: 66%">photo_camera</span>
  <span class="pin icon small" style="left: 24%; top: 26%">photo_camera</span>
  <div class="cam-card">
    <div class="cam-head"><span class="la-sign sm">60</span><div><b>Fixed camera</b><span>Jl. Bypass Ngurah Rai, Kuta</span></div></div>
    <div class="cam-rows"><span>Type<b>Fixed, both ways</b></span><span>Verified<b>12 Oct 2026</b></span></div>
  </div>
</div>
''',
    # Warnings when you want them
    6: '''
<div class="center">
  <div class="settings">
    <span class="ui-label">Warn me at</span>
    <div class="segmented"><span>500 m</span><span>1 km</span><span class="on">2 km</span></div>
    <div class="list">
      <div class="set-row"><span class="badge icon" style="--c: var(--accent-purple)">record_voice_over</span><span class="lbl">Spoken warnings</span><span class="toggle on"></span></div>
      <div class="set-row"><span class="badge icon" style="--c: var(--accent-blue)">local_police</span><span class="lbl">Police reports</span><span class="toggle on"></span></div>
      <div class="set-row"><span class="badge icon" style="--c: var(--accent-orange)">speed</span><span class="lbl">Mobile cameras</span><span class="toggle"></span></div>
    </div>
  </div>
</div>
''',
    # Glanceable and hands-free
    7: f'''
<div class="center">
  <div class="spoken">
    <div class="island"><img class="n-icon" src="assets/app-icon.svg" alt=""><div class="wave">{WAVE}</div><span class="rounded">500 m</span></div>
    <span class="said">“Speed camera in five hundred metres. Limit sixty.”</span>
  </div>
  <div class="carplay">
    <div class="carplay-screen">
      <div class="cp-dock">
        <span>9:41</span>
        <span class="app icon" style="--c: var(--accent-green)">call</span>
        <span class="app icon" style="--c: var(--accent-blue)">near_me</span>
        <span class="app icon" style="--c: var(--accent-pink)">music_note</span>
        <img class="app" src="assets/app-icon.svg" alt="">
      </div>
      <div class="cp-main">
        <div class="ring-wrap">
          <svg viewBox="0 0 120 120" aria-hidden="true">
            <circle cx="60" cy="60" r="50" fill="none" stroke="rgb(255 255 255 / 0.1)" stroke-width="12"/>
            <circle cx="60" cy="60" r="50" fill="none" stroke="var(--accent-orange)" stroke-width="12" stroke-linecap="round" stroke-dasharray="196 314"/>
          </svg>
          <div class="ring-center"><div><b>500</b><span>metres</span></div></div>
        </div>
        <div class="cp-info">
          <h4>Speed camera ahead</h4>
          <div class="row"><span class="icon">speed</span>Limit 60 km/h · you 58</div>
          <div class="row"><span class="icon">location_on</span>Jl. Bypass Ngurah Rai</div>
          <div class="cp-alert"><span class="icon" style="font-size: 18px">volume_up</span>Spoken warning on</div>
        </div>
      </div>
    </div>
  </div>
</div>
''',
}
