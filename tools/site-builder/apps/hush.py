"""HUSH app content."""

APP = {
    "name": "HUSH",
    "title": "Check your room for hidden cameras",
    "description": "HUSH helps travellers check a hotel room or rental for hidden cameras in a few minutes, and writes a report you can send to the host if it finds one.",
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
    "h1": "Check your room for<br>hidden cameras.",
    "sub": "In a 2025 survey, nearly half of US renters said they had found a camera during a stay, and most don't know how to check for one. HUSH helps you check your hotel room or rental in a few minutes.",
    "hero_shot": "Room check",
    "hero_note": "One email when HUSH is ready to try. No spam.",
    "chips": [("sensor_door", "orange", "Room check", "In progress"), ("ios_share", "green", "Report", "Ready to send")],
    "features_eyebrow": "How it works",
    "features_title": "How a room check works",
    "features": [
        {
            "size": "third", "color": "orange", "kicker": "Guided check",
            "title": "Point your phone around the room",
            "text": "HUSH uses your camera to guide you through the room, one spot at a time.",
        },
        {
            "size": "two-thirds", "color": "green", "kicker": "Wi-Fi devices",
            "title": "See what's on the room Wi-Fi",
            "text": "HUSH lists the devices on the room's network and points out any that could be a camera.",
            "shots": ["Network tags", "Ordinary device"],
        },
        {
            "size": "half", "color": "red", "kicker": "Hidden lenses",
            "title": "Check suspicious spots up close",
            "text": "If something looks wrong, HUSH asks you to hold your phone on it for a few seconds and saves a photo as evidence.",
        },
        {
            "size": "half", "color": "orange", "kicker": "Bed and shower",
            "title": "Check the bed and the shower",
            "text": "The check covers the places where privacy matters most.",
        },
        {
            "size": "two-thirds", "color": "purple", "kicker": "Result",
            "title": "A clear result",
            "text": "If nothing is found, HUSH tells you. If something is found, it shows you what it is and where.",
            "shots": ["Just you in here", "Worth a closer look"],
        },
        {
            "size": "third", "color": "blue", "kicker": "Private",
            "title": "Nothing is saved unless you choose",
            "text": "Your check stays on your phone. You decide whether to share the report.",
        },
        {
            "size": "full", "color": "mint", "kicker": "Report",
            "title": "A report you can send",
            "text": "The report lists the time, what was found, where it was, and what the check could not cover. Send it to your host, Airbnb, or a friend.",
            "shots": ["Report ready", "Share sheet", "Message drafted"],
        },
    ],
    "faq": [
        ("What does HUSH check?",
         "Devices on the room Wi-Fi, and hidden camera lenses around the room, including the bed and the shower."),
        ("Can it find every hidden camera?",
         "No. Some cameras record without connecting to Wi-Fi. HUSH tells you what it checked and what it couldn't."),
        ("What happens if it finds something?",
         "It shows you the evidence and writes a report you can send to your host, Airbnb, a friend, or the police."),
        ("Does HUSH save my checks?",
         "No. Nothing is saved automatically. You share the report only if you want to."),
    ],
    "values_eyebrow": "Why HUSH",
    "values_title": "Why not just look around yourself?",
    "values": [
        ("visibility", "blue", "It knows where to look", "Most people don't know what a hidden camera looks like. HUSH guides you to the places to check."),
        ("wifi", "orange", "It checks the Wi-Fi too", "Some cameras connect to the room network. HUSH lists the devices it finds so you can spot the odd one out."),
        ("description", "green", "Proof you can send", "If you find something, you have a report with photos ready for your host or Airbnb."),
    ],
    "cta_title": "Check your next room before you settle in",
    "cta_sub": "Join the waitlist and we'll email you when HUSH is ready to try.",
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
