"""KESHA app content."""

APP = {
    "name": "KESHA",
    "title": "Stay awake on long drives",
    "description": "Kesha is a CarPlay app that helps long-distance drivers stay awake. It talks with you, plays your music, notices when your replies slow down, and warns you before accident black spots.",
    "brand": "#FFB547",
    "brand2": "#FF3B2F",
    "font_links": (
        "https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&display=swap",
    ),
    "theme": {
        "page": "#100C0A",
        "card": "#1A1411",
        "inset": "#241B16",
        "line": "#2E2420",
        "ink": "#F3E9DA",
        "muted": "#A3968A",
        "faint": "#A8988C",
        "hairline": "rgb(255 245 230 / .11)",
        "button": "#FFB547",
        "on_button": "#1D1612",
        "shadow_card": "inset 0 0 0 1px rgb(255 245 230 / .08), 0 30px 80px -44px rgb(0 0 0 / .95)",
        "shadow_float": "inset 0 0 0 1px rgb(255 245 230 / .10), 0 18px 42px -20px rgb(0 0 0 / .85)",
        "font_text": '"Figtree", -apple-system, BlinkMacSystemFont, "Inter", sans-serif',
        "font_display": '"Figtree", -apple-system, BlinkMacSystemFont, "Inter", sans-serif',
        "font_rounded": '"Figtree", -apple-system, BlinkMacSystemFont, "Inter", sans-serif',
        "color_scheme": "dark",
        "accents": {
            "blue": "#8FB4FF",
            "green": "#7BE08A",
            "indigo": "#A3968A",
            "mint": "#F3E9DA",
            "orange": "#FFB547",
            "pink": "#FF9B83",
            "purple": "#C8A46F",
            "red": "#FF3B2F",
        },
    },
    "icon": {
        "from": "#FFB547", "to": "#FF3B2F",
        "stroke": "#1D1612",
        # The flame that rides along in the final prototype.
        "glyph": '<path d="M61 24c13 17 1 27 15 39 8 7 11 16 7 26-5 12-16 20-29 20s-25-8-30-20c-5-13 2-28 15-39 8-7 13-16 22-26Z"/><path d="M55 75c-5 7-2 18 7 18 8 0 13-7 10-15-3-7-10-10-11-21-5 7-2 11-6 18Z"/>',
    },
    "status": "iPhone and CarPlay",
    "h1": "Stay awake on<br>long drives.",
    "sub": "About 1 in 5 fatal road crashes involves a driver who is too tired. Kesha helps long-distance drivers stay alert and get home safely.",
    "hero_shot": "Driving screen",
    "hero_note": "One email when Kesha is ready to try. No spam.",
    "chips": [('local_fire_department', 'orange', 'Status', "You're alert"), ('graphic_eq', 'red', 'Check-in', 'Still with me?')],
    "features_eyebrow": "How it works",
    "features_title": "What Kesha does<br>during your drive",
    "features": [
        {
            "size": "third", "color": "orange", "kicker": "Start a drive",
            "title": "Say where you're going",
            "text": "Or just start driving. On a route you drive often, Kesha asks if it's the same trip and you answer by voice.",
        },
        {
            "size": "two-thirds", "color": "orange", "kicker": "Music and check-ins",
            "title": "Your music plays while Kesha checks in",
            "text": 'Kesha plays your music and lowers the volume when it asks you a short question, like "Still with me?"',
            "shots": ["Company", "Still with me?"],
        },
        {
            "size": "half", "color": "red", "kicker": "Slow replies",
            "title": "If you reply slowly, Kesha keeps you talking",
            "text": "A slow reply can mean you're getting tired. Kesha asks easy questions to keep your mind active. You don't touch the screen.",
        },
        {
            "size": "half", "color": "blue", "kicker": "No reply",
            "title": "If you don't reply, Kesha asks you to tap",
            "text": 'The screen shows one large "I\'m awake" button. If you don\'t tap it within 10 seconds, the alert gets louder.',
        },
        {
            "size": "two-thirds", "color": "red", "kicker": "Black spots",
            "title": "Warnings before dangerous roads",
            "text": 'Kesha tells you when you\'re approaching a known accident black spot, for example: "Salgaa in three kilometres. Eyes up."',
            "shots": ["Black spot", "Through the bends"],
        },
        {
            "size": "third", "color": "purple", "kicker": "Voice notes",
            "title": "Voice notes from family",
            "text": "Family or friends can record a voice note that plays during your drive.",
        },
        {
            "size": "full", "color": "mint", "kicker": "CarPlay",
            "title": "Works on your CarPlay screen",
            "text": "Kesha appears on the Now Playing screen, warnings are easy to read at a glance, and audio plays through your car speakers. Your navigation app keeps working as normal.",
            "shots": ["CarPlay flame", "Live Activity", "Arrival"],
        },
    ],
    "faq": [
        ("How does Kesha know I'm getting tired?",
         'It asks short questions during your drive, like "Still with me?", and listens to how quickly and clearly you answer.'),
        ("Do I need to plan my route?",
         "No. Say where you're going, or just start driving. On a trip you've driven before, one voice answer is enough."),
        ("Do I need CarPlay?",
         "CarPlay works best, because alerts show on your dashboard and play through your car speakers. An iPhone-only version is also planned."),
    ],
    "values_eyebrow": "Why Kesha",
    "values_title": "Why not just coffee or the radio?",
    "values": [
        ("hearing", "orange", "It notices when you're tired", "Coffee and the radio can't tell when you're getting sleepy. Kesha notices when your replies slow down."),
        ("record_voice_over", "blue", "Hands-free", "Everything works by voice. The only tap is the \"I'm awake\" button, and only if you stop replying."),
        ("warning", "red", "It knows the road", "Kesha warns you before known accident black spots on your route."),
    ],
    "cta_title": "Get Kesha for your next long drive",
    "cta_sub": "Join the waitlist and we'll email you when Kesha is ready to try.",
    "release_notes": [
        {
            "tag": "Pre-launch", "date": "October 9, 2026", "title": "The waitlist is open",
            "body": '''        <p>Kesha is in development: an iPhone and CarPlay ride-along for drivers on long roads at night.</p>
        <p>Here is what we are building first:</p>
        <ul>
          <li>A voice-first drive flow with almost no taps while moving</li>
          <li>Music and sound cues that change with alertness</li>
          <li>Black-spot warnings before dangerous stretches</li>
          <li>A CarPlay flame that acts like Now Playing artwork and a Live Activity</li>
        </ul>''',
        },
    ],
    "roadmap": [
        ("done", "Waitlist opens", "This website and early sign-ups."),
        ("now", "Sound tests", "Testing the chimes, music lifts and voice prompts from the final prototype."),
        ("", "Driver interviews", "Talking to people who drive long distances alone."),
        ("", "Black spot data", "Mapping accident-prone stretches of road."),
        ("", "CarPlay prototype", "Testing the dashboard flame and audio flow."),
        ("", "TestFlight beta", "Early access for people on the waitlist."),
    ],
    "contact_email": "hello@lotus-c1.app",
    "contact_topics": ["General question", "Feature idea", "Fleet and partnerships", "Press"],
    "privacy_intro": "Kesha is built for a private drive. This policy explains what we collect through this website today and what the app is designed to do once it launches.",
    "privacy": [
        ("Voice and drive data (once the app launches)", '''        <p>Voice prompts and reply timing are designed to be processed during the drive so Kesha can decide when to check in. We will document exactly what stays on device before launch.</p>'''),
        ("Location", '''        <p>Location is used during a drive to know the route and warn before black spots. We do not sell trip data.</p>'''),
    ],
    "terms": [
        ("A driving aid, not a guarantee", '''        <p>Kesha helps a driver stay alert with voice, music and warnings, but it cannot guarantee alertness or prevent accidents. You are responsible for driving carefully and following traffic laws.</p>
        <p>Set up the app before moving. Do not interact with the phone while driving except for the large awake check when it appears.</p>'''),
        ("Audio alerts", '''        <p>Alerts and music changes can be loud by design. Keep volume at a level that is appropriate for the car and passengers.</p>'''),
    ],
}
