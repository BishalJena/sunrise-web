"""Underneath app content."""

APP = {
    "name": "Underneath",
    "title": "The news without the noise",
    "description": "Underneath gives busy young workers a finishable edition: peel the rumour, read the checked story underneath, and stop when the wall is clean.",
    "brand": "#8A4F22",
    "brand2": "#F3EEE4",
    "font_links": (
        "https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@900&family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap",
    ),
    "theme": {
        "page": "#DAD2C3",
        "card": "#F4EFE6",
        "inset": "#E6DDCD",
        "line": "#D8CDBA",
        "ink": "#16120D",
        "muted": "#4B4237",
        "faint": "#5C5348",
        "hairline": "rgb(22 18 13 / .13)",
        "button": "#16120D",
        "on_button": "#F3EEE4",
        "shadow_card": "0 0 0 1px rgb(22 18 13 / .08), 0 24px 60px -38px rgb(22 18 13 / .35)",
        "shadow_float": "0 0 0 1px rgb(22 18 13 / .10), 0 18px 36px -22px rgb(22 18 13 / .45)",
        "font_text": '"Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, "Inter", sans-serif',
        "font_display": '"Newsreader", Georgia, serif',
        "font_rounded": '"Big Shoulders Display", "Plus Jakarta Sans", sans-serif',
        "accents": {
            "blue": "#4C6570",
            "green": "#5E7254",
            "indigo": "#4B4237",
            "mint": "#716C64",
            "orange": "#8A4F22",
            "pink": "#B69D82",
            "purple": "#6D5D4A",
            "red": "#C8322A",
        },
    },
    "icon": {
        "from": "#EEE8DC", "to": "#8A4F22",
        # A bill peeling from the wall.
        "glyph": '<path d="M31 35h58v50H31Z"/><path d="M89 35v27c0 13-10 23-23 23H31"/><path d="M51 57h23M51 70h14"/><path d="M89 62 66 85"/>',
    },
    "status": "A finished edition",
    "h1": "Peel the rumour.<br>Read underneath.",
    "sub": "Underneath turns the noisy stories moving through WhatsApp, X, TikTok and LinkedIn into one checked edition with an end.",
    "hero_shot": "Bills on the wall",
    "hero_note": "No spam. One email when early access opens.",
    "chips": [('radio_button_checked', 'green', 'Confirmed', 'Signal shown'), ('wallpaper', 'orange', '8 bills', 'Then clean')],
    "features_title": "Open it, read it,<br>finish it.",
    "features": [
        {
            "size": "third", "color": "orange", "kicker": "The wall",
            "title": "No feed, no pile",
            "text": "The edition is the wall. It has a small number of stories and then it ends.",
        },
        {
            "size": "two-thirds", "color": "red", "kicker": "Noise",
            "title": "The rumour is the bill",
            "text": 'The front says what is going around: "BBM NAIK??" or "Rp600RB??". Red belongs only to that noise.',
            "shots": ["Rumour bills", "Noise on paper"],
        },
        {
            "size": "half", "color": "mint", "kicker": "Peel",
            "title": "The checked story is underneath",
            "text": "Peel the corner. The bill curls and falls. A calm story appears on fresh whitewash.",
        },
        {
            "size": "half", "color": "green", "kicker": "Signals",
            "title": "Every story carries its mark",
            "text": "Confirmed, developing, unverified or false is shown by shape and word, never by colour alone.",
        },
        {
            "size": "two-thirds", "color": "blue", "kicker": "Forward with proof",
            "title": "Share the checked version",
            "text": "A share includes the signal and sources, so a story can move without losing its proof.",
            "shots": ["Checked story", "Share with proof"],
        },
        {
            "size": "third", "color": "purple", "kicker": "Local first",
            "title": "Jakarta and his topics",
            "text": "The first edition is tuned to where he is and what he follows, without an endless recommendation trail.",
        },
        {
            "size": "full", "color": "orange", "kicker": "Clean wall",
            "title": "The end is visible",
            "text": "Bills left equals stories left. At the end, morning light leaves a clean wall and the edition painted on it.",
            "shots": ["Halfway", "Clean", "Edition painted"],
        },
    ],
    "faq": [
        ("Who is Underneath for?",
         "A busy young worker in Indonesia who gets news through social feeds and chat, but wants a clear edition he can finish."),
        ("Is every story confirmed?",
         "No. Developing and unverified stories can appear, but they are marked clearly with a signal and sources."),
        ("Who writes the summaries?",
         "AI can draft them, but the product is designed around editorial approval before anything reaches an edition."),
        ("Is it another infinite feed?",
         "No. The edition has a fixed number of stories. Nothing piles up after a few days away."),
    ],
    "values_title": "For a clear head",
    "values": [
        ("done_all", "green", "Finishable", "Up to a small number of stories, then the wall is clean."),
        ("fact_check", "blue", "Marked stories", "Every story shows its signal and sources."),
        ("block", "orange", "No engagement trap", "No unread badges, streaks, or endless next story."),
    ],
    "cta_title": "Start with tomorrow's edition",
    "cta_sub": "Join the waitlist for Underneath.",
    "release_notes": [
        {
            "tag": "Pre-launch", "date": "October 9, 2026", "title": "The waitlist is open",
            "body": '''        <p>Underneath is in development: a finishable news edition for people who get too much noise from feeds and chats.</p>
        <p>Here is what we are building first:</p>
        <ul>
          <li>One daily edition with a visible end</li>
          <li>Rumour bills that peel away to reveal checked stories</li>
          <li>Signals for confirmed, developing, unverified and false stories</li>
          <li>Sources and proof built into sharing</li>
        </ul>''',
        },
    ],
    "roadmap": [
        ("done", "Waitlist opens", "This website and early sign-ups."),
        ("now", "Edition model", "Designing a small, finishable set of stories instead of a feed."),
        ("", "Editorial checks", "Building the AI-draft and human-approval workflow."),
        ("", "Source signals", "Making every status visible by word and shape."),
        ("", "TestFlight beta", "Early access for people on the waitlist."),
    ],
    "contact_email": "hello@lotus-e3.app",
    "contact_topics": ["General question", "Feature idea", "Publishers and partnerships", "Report a correction", "Press"],
    "privacy_intro": "Underneath is built to inform you, not to track you. This policy explains the waitlist today and the app we are building.",
    "privacy": [
        ("Location and interests (once the app launches)", '''        <p>Your chosen topics and approximate location are used to prepare an edition. You can use a city instead of precise location. We do not sell reading habits or share them with advertisers.</p>'''),
    ],
    "terms": [
        ("Summaries and sources", '''        <p>Stories are summaries of reporting by third-party news outlets and may occasionally contain errors or miss context. Always refer to original sources for full details. Signals reflect editorial status, not a guarantee.</p>
        <p>Original articles belong to their publishers. Links take you to their websites, under their terms.</p>'''),
    ],
}
