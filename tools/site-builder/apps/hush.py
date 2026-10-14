"""HUSH app content."""

APP = {
    "name": "HUSH",
    "title": "Check your room before you settle in",
    "description": "HUSH turns a hotel room or Airbnb into a one-minute room check: Wi-Fi devices, hidden lenses, and a shareable report if something can see or hear you.",
    "brand": "#E8A33A",
    "brand2": "#FFD58A",
    "font_links": (
        "https://fonts.googleapis.com/css2?family=Caveat:wght@500;600&family=Geist:wght@400;500;600;700&family=Instrument+Serif&display=swap",
    ),
    "theme": {
        "page": "#E9E5DD",
        "card": "#FBF8F1",
        "inset": "#F4EEE3",
        "line": "#D8D0C2",
        "ink": "#17120E",
        "muted": "#5F564C",
        "faint": "#5E554A",
        "hairline": "rgb(23 18 14 / .12)",
        "button": "#17120E",
        "on_button": "#FBF8F1",
        "shadow_card": "0 0 0 1px rgb(23 18 14 / .08), 0 24px 60px -38px rgb(23 18 14 / .45)",
        "shadow_float": "0 0 0 1px rgb(23 18 14 / .10), 0 18px 36px -22px rgb(23 18 14 / .45)",
        "font_text": '"Geist", -apple-system, BlinkMacSystemFont, "Inter", sans-serif',
        "font_display": '"Instrument Serif", Georgia, serif',
        "font_rounded": '"Geist", -apple-system, BlinkMacSystemFont, "Inter", sans-serif',
        "accents": {
            "blue": "#68747B",
            "green": "#5C7861",
            "indigo": "#6E625A",
            "mint": "#767065",
            "orange": "#946825",
            "pink": "#FFD58A",
            "purple": "#8E6A41",
            "red": "#A8442E",
        },
    },
    "icon": {
        "from": "#FBF8F1", "to": "#E8A33A",
        "stroke": "#17120E",
        # Door hanger companion from the final prototype.
        "glyph": '<path d="M48 24h25v72H40V41c0-10 8-17 20-17Z"/><circle cx="60" cy="42" r="7"/><path d="M49 69h22"/>',
    },
    "status": "One room check",
    "h1": "Just you<br>in here.",
    "sub": "HUSH guides a tired traveller through one calm check when she arrives: the room Wi-Fi, the view from the bed, and the shower.",
    "hero_shot": "The room check",
    "hero_note": "No spam. One note when TestFlight is ready.",
    "chips": [('sensor_door', 'orange', 'Door hanger', 'Next small step'), ('ios_share', 'green', 'Report', 'Share sheet only')],
    "features_title": "A stranger's room<br>becomes her room.",
    "features": [
        {
            "size": "third", "color": "orange", "kicker": "Live camera",
            "title": "The room warms as she checks",
            "text": "The real camera stays in the background. Cold corners turn lamp-lit where she has looked.",
        },
        {
            "size": "two-thirds", "color": "green", "kicker": "Wi-Fi devices",
            "title": "Ordinary things are named ordinary",
            "text": "Devices on the room network appear as small paper tags, so a lamp stays a lamp and only unusual devices get attention.",
            "shots": ["Network tags", "Ordinary device"],
        },
        {
            "size": "half", "color": "red", "kicker": "Hidden lenses",
            "title": "A closer look, not an alarm",
            "text": "If something needs attention, HUSH asks her to hold the phone there for a few seconds and records the evidence.",
        },
        {
            "size": "half", "color": "orange", "kicker": "Bed and shower",
            "title": "The exposed places are checked",
            "text": "The check ends where it matters: from the bed and from the shower, with the end always in sight.",
        },
        {
            "size": "two-thirds", "color": "purple", "kicker": "Result",
            "title": "The hanger tells the truth",
            "text": 'Nothing found ends with "Just you in here." If something can see or hear her, the hanger turns dark and shows calm facts.',
            "shots": ["Just you in here", "Worth a closer look"],
        },
        {
            "size": "third", "color": "blue", "kicker": "No archive",
            "title": "Nothing is stored by default",
            "text": "When the check ends, she can leave it there or share the report herself.",
        },
        {
            "size": "full", "color": "mint", "kicker": "Report",
            "title": "Written for the host, Airbnb, or a friend",
            "text": "The report includes the time, the devices found, the spots checked, and what the check cannot see.",
            "shots": ["Report ready", "Share sheet", "Message drafted"],
        },
    ],
    "faq": [
        ("What does HUSH check?",
         "It checks devices on the room Wi-Fi and guides a short camera check for hidden lenses from the bed and the shower."),
        ("Can it find everything?",
         "No room check can promise that. Some devices record locally and never connect to a network. HUSH tells you what it checked and what it could not check."),
        ("What happens if it finds something?",
         "It keeps the language calm, shows the evidence, and prepares a report you can send to the host, Airbnb, a friend, or local authorities."),
        ("Does HUSH save scan history?",
         "No. The report is offered through the iOS share sheet. Nothing is stored automatically."),
    ],
    "values_title": "Made for the arrival moment",
    "values": [
        ("lock", "blue", "Private by default", "Checks run on the iPhone. Reports leave only when she chooses to share them."),
        ("light_mode", "orange", "Calm through visuals", "Warmth, paper, and one next step replace sirens and panic copy."),
        ("hotel", "green", "Built for stays", "Hotels, rentals, and hostels: one check when she walks in, then she can settle."),
    ],
    "cta_title": "Check the room, then put the phone down",
    "cta_sub": "Join the waitlist for the first HUSH TestFlight.",
    "release_notes": [
        {
            "tag": "Pre-launch", "date": "October 9, 2026", "title": "The waitlist is open",
            "body": '''        <p>HUSH is in development: an iPhone room check for women arriving at hotels, rentals and hostels.</p>
        <p>Here is what we are building first:</p>
        <ul>
          <li>A live-camera room check that turns cold corners warm as they are checked</li>
          <li>Wi-Fi device naming, with ordinary devices called ordinary</li>
          <li>A short hidden-lens check from the bed and the shower</li>
          <li>A report that is shared only through the iOS share sheet</li>
        </ul>''',
        },
    ],
    "roadmap": [
        ("done", "Waitlist opens", "This website and early sign-ups."),
        ("now", "Hotel-room tests", "Testing Wi-Fi cameras and memory-card spy cameras in real rooms."),
        ("", "Device naming", "Building the ordinary-device library so the app does not overreact."),
        ("", "Traveller interviews", "Learning from women who arrive tired and want the check over quickly."),
        ("", "TestFlight beta", "Early access for people on the waitlist."),
    ],
    "contact_email": "hello@lotus-f1.app",
    "contact_topics": ["General question", "Feature idea", "Hotel and rental partnerships", "Press"],
    "privacy_intro": "HUSH is designed for a private room, so it collects as little as possible. This policy explains the waitlist today and the app we are building.",
    "privacy": [
        ("Room checks (once the app launches)", '''        <p>Wi-Fi and camera checks run on your iPhone. Reports are created on device and leave only if you share them yourself.</p>'''),
    ],
    "terms": [
        ("What HUSH can and cannot do", '''        <p>HUSH helps you check for devices that can see or hear you, but no tool can detect every device. A clear check is not a guarantee, and a flagged device is not proof of wrongdoing.</p>
        <p>If you believe you are in danger, contact local emergency services. If you find a device, do not tamper with it. Report it to the property and the police.</p>'''),
        ("Lawful use", '''        <p>Use HUSH only to check spaces you are staying in or are responsible for. Do not use it to interfere with other people's networks or devices.</p>'''),
    ],
}
