"""Lotus G-1: speed camera alerts as an iOS Live Activity."""

APP = {
    "listed": False,
    "name": "Lotus G-1",
    "title": "Speed camera alerts on your Lock Screen",
    "description": "Lotus G-1 warns you before speed cameras, right on your Lock Screen and Dynamic Island, so you can slow down in time. Launching first in Bali.",
    "brand": "var(--accent-orange)",
    "brand2": "var(--accent-red)",
    "icon": {
        "from": "#ffb340", "to": "#ff5a36",
        "stroke": "#1D1612",
        # speedometer arc + needle
        "glyph": '<path d="M28 78a32 32 0 1 1 64 0"/><path d="M60 78l16-20"/><circle cx="60" cy="78" r="3" fill="#1D1612"/>',
    },
    "status": "Launching first in Bali",
    "h1": "Slow down before<br>the speed camera.",
    "sub": "Electronic traffic cameras now record violations on Bali's roads, and the fine arrives later. Lotus G-1 warns you before every known speed camera so you can slow down in time.",
    "hero_shot": "Lock Screen with Live Activity",
    "hero_note": "One email when Lotus G-1 is ready to try. No spam.",
    "chips": [("photo_camera", "red", "850 m", "Next camera"), ("verified", "green", "Slow down", "Limit ahead")],
    "features_eyebrow": "How it works",
    "features_title": "How Lotus G-1 warns you",
    "features": [
        {
            "size": "third", "color": "orange", "kicker": "Live Activity",
            "title": "On your Lock Screen",
            "text": "See the next camera, its speed limit and how far away it is on your Lock Screen and Dynamic Island.",
        },
        {
            "size": "two-thirds", "color": "red", "kicker": "Alerts",
            "title": "Spoken and on-screen warnings",
            "text": "As you get close, you hear and see a warning with the distance and the speed limit.",
            "shots": ["Proximity alert", "Alert details"],
        },
        {
            "size": "half", "color": "green", "kicker": "Speed check",
            "title": "Tells you if you're too fast",
            "text": "Lotus G-1 compares your speed with the limit ahead and tells you to slow down, or suggests another route.",
        },
        {
            "size": "half", "color": "blue", "kicker": "Driver reports",
            "title": "Report cameras and police checks",
            "text": "Report a new camera or a police check in one tap to warn other drivers.",
        },
        {
            "size": "two-thirds", "color": "pink", "kicker": "Starting in Bali",
            "title": "Launching in Bali first",
            "text": "We're starting with a speed camera map of Bali, then adding more regions.",
            "shots": ["Camera map", "Camera details"],
        },
        {
            "size": "third", "color": "purple", "kicker": "Settings",
            "title": "Choose when you're warned",
            "text": "Set how far ahead you want to hear about a camera, and how.",
        },
        {
            "size": "full", "color": "indigo", "kicker": "Hands-free",
            "title": "Made for driving",
            "text": "Large alerts you can read at a glance, and spoken warnings so you keep your eyes on the road.",
            "shots": ["Driving view", "Spoken alerts", "Trip summary"],
        },
    ],
    "faq": [
        ("Does this help me speed without getting caught?",
         "No. Lotus G-1 is for careful drivers who want to stay within the limit. It reminds you of the limit ahead so you can slow down in time."),
        ("Where will it work?",
         "We're starting in Bali, Indonesia, and will add more regions over time."),
        ("Do I need to keep the app open?",
         "No. Alerts show on your Lock Screen and Dynamic Island, so you can keep using Maps or music."),
        ("Are camera alert apps legal?",
         "In many countries, but not all. Check the rules where you drive. We'll only offer the app where it's allowed."),
    ],
    "values_eyebrow": "Why Lotus G-1",
    "values_title": "Why not just watch for the signs?",
    "values": [
        ("visibility", "orange", "Warned in advance", "Cameras are easy to miss. Lotus G-1 tells you well before you reach one."),
        ("groups", "green", "Updated by drivers", "Other drivers report new cameras and police checks, so the map stays current."),
        ("lock", "blue", "Private", "Your location is used on your phone to find nearby cameras. We don't sell where you drive."),
    ],
    "cta_title": "Get warned before your next speed camera",
    "cta_sub": "Join the waitlist and we'll email you when Lotus G-1 is ready to try.",
    "release_notes": [
        {
            "tag": "Pre-launch", "date": "October 9, 2026", "title": "The waitlist is open",
            "body": '''        <p>Lotus G-1 is in development. It's a Live Activity for iPhone that shows the nearest speed camera on your route and warns you to slow down before you reach it.</p>
        <p>Here's what we're building first:</p>
        <ul>
          <li>Live Activity on the Lock Screen and Dynamic Island</li>
          <li>Visual and spoken alerts at a distance you choose</li>
          <li>Speed advisory comparing your speed with the limit ahead</li>
          <li>Community reports for police checks and new cameras</li>
          <li>A speed camera database for Bali, Indonesia</li>
        </ul>''',
        },
    ],
    "roadmap": [
        ("done", "Waitlist opens", "This website and early sign-ups."),
        ("now", "Bali camera database", "Collecting and verifying camera locations and limits."),
        ("", "Driver interviews", "Riding along with car and motorbike drivers to shape the alerts."),
        ("", "Route simulation", "Testing alerts on simulated drives before real-world tests."),
        ("", "CarPlay notifications", "Showing alerts on the car's display."),
        ("", "TestFlight beta", "Early access for people on the waitlist."),
    ],
    "contact_email": "hello@lotus-g1.app",
    "contact_topics": ["General question", "Report a camera location", "Feature idea", "Partnerships", "Press"],
    "privacy_intro": "Lotus G-1 is designed to collect as little as possible. This policy explains what we collect through this website today and what the app is designed to do once it launches.",
    "privacy": [
        ("Location (once the app launches)", '''        <p>The app needs your location and speed to find cameras on your route and warn you in time. This is processed on your device. We don't build a history of your trips or sell location data.</p>'''),
        ("Community reports", '''        <p>When you report a camera or a police check, we store the report's location and time so other drivers can see it. Reports aren't linked to your name.</p>'''),
    ],
    "terms": [
        ("Drive safely and legally", '''        <p>Lotus G-1 is a driving aid, not a substitute for attention or for road signs. Always obey posted limits, traffic laws and police instructions. Don't interact with your phone while driving.</p>
        <p>Camera locations come from our database and community reports and may be incomplete or out of date. We can't guarantee that every camera is listed, and we're not responsible for fines or penalties.</p>
        <p>Using camera alert apps is restricted in some countries. You're responsible for making sure it's legal where you drive.</p>'''),
        ("Community reports", '''        <p>Only report what you've actually seen. We may remove reports or restrict accounts that post false or abusive information.</p>'''),
    ],
}
