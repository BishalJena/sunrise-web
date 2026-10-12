"""KESHA app content."""

APP = {
    "name": "KESHA",
    "title": "Stay awake driving",
    "description": "KESHA is a flame for long drives: voice, music, CarPlay, black-spot warnings, and awake checks when the road gets heavy.",
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
        "faint": "#6E625A",
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
        # The flame that rides along in the final prototype.
        "glyph": '<path d="M61 24c13 17 1 27 15 39 8 7 11 16 7 26-5 12-16 20-29 20s-25-8-30-20c-5-13 2-28 15-39 8-7 13-16 22-26Z"/><path d="M55 75c-5 7-2 18 7 18 8 0 13-7 10-15-3-7-10-10-11-21-5 7-2 11-6 18Z"/>',
    },
    "status": "iPhone and CarPlay",
    "h1": "Light it.<br>Keep driving.",
    "sub": "Kesha talks to a tired driver, plays his music, and warns before black spots. How fast he answers is how the flame knows he is still with it.",
    "hero_shot": "The flame on the road",
    "hero_note": "No spam. One email when the ride-along opens.",
    "chips": [('local_fire_department', 'orange', 'Flame', 'Amber and awake'), ('graphic_eq', 'red', 'Voice', 'Still with me?')],
    "features_title": "A flame that keeps<br>him company.",
    "features": [
        {
            "size": "third", "color": "orange", "kicker": "Ride-along",
            "title": "It starts with his name and route",
            "text": 'On repeat drives, "Eldoret again?" can be answered by voice.',
        },
        {
            "size": "two-thirds", "color": "orange", "kicker": "Music and voice",
            "title": "The flame moves with the drive",
            "text": "Music stays soft in the background. Kesha ducks it for a two-note check or a real question.",
            "shots": ["Company", "Still with me?"],
        },
        {
            "size": "half", "color": "red", "kicker": "Slow reply",
            "title": "When replies slow, the flame rises",
            "text": "Kesha asks something easy to answer. No taps while moving, unless voice does not come back.",
        },
        {
            "size": "half", "color": "blue", "kicker": "No answer",
            "title": "One huge awake check",
            "text": 'If there is no voice, the screen becomes one big "I am awake" button before anything escalates.',
        },
        {
            "size": "two-thirds", "color": "red", "kicker": "Black spots",
            "title": "Eyes up before the dangerous stretch",
            "text": 'The flame turns red and still. "Salgaa in three kilometres. Eyes up."',
            "shots": ["Black spot", "Through the bends"],
        },
        {
            "size": "third", "color": "purple", "kicker": "Dedication",
            "title": "A voice note from family",
            "text": "A rose-gold moment can come from someone who wants him home.",
        },
        {
            "size": "full", "color": "mint", "kicker": "CarPlay",
            "title": "Now Playing becomes the co-driver",
            "text": "On CarPlay, the flame is the artwork, the warning is glanceable, and the audio stays in the car speakers.",
            "shots": ["CarPlay flame", "Live Activity", "Arrival"],
        },
    ],
    "faq": [
        ("How does Kesha measure alertness?",
         'By the drive and the reply. It listens for how quickly and clearly the driver answers simple prompts like "Still with me?"'),
        ("Does it need planning?",
         "No. Say where you are going, or just start driving. Repeat trips can be resumed with one voice answer."),
        ("Do I need CarPlay?",
         "CarPlay is the best version because the flame and alerts live on the dashboard and audio comes through the car speakers. The iPhone version is planned too."),
        ("Does it tell the driver to stop?",
         "No. The final design is about staying awake while driving: voice, music, black-spot warnings, and an awake check when needed."),
    ],
    "values_title": "For a driver with almost no attention left",
    "values": [
        ("record_voice_over", "orange", "Voice first", "After Light it, the app is spoken and heard."),
        ("touch_app", "blue", "One exception", "Only the awake check asks for a giant tap when voice does not come back."),
        ("music_note", "red", "Sound matters", "The flame, chimes and music are part of the interface, not decoration."),
    ],
    "cta_title": "Bring the flame on the next long drive",
    "cta_sub": "Join the waitlist for Kesha: Stay Awake Driving.",
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
