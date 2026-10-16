"""Underneath app content."""

APP = {
    "name": "Underneath",
    "title": "Checked news you can finish",
    "description": "Underneath is a short daily edition of checked news for busy young Indonesians. Every story shows whether it is confirmed, and the edition has an end.",
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
    "h1": "The news, checked.<br>In a few minutes.",
    "sub": "Indonesia's communications ministry identified more than 11,000 hoaxes between 2018 and 2023. Underneath gives you a short daily edition of checked news, so you know what's true without scrolling for hours.",
    "hero_shot": "Today's edition",
    "hero_note": "One email when Underneath is ready to try. No spam.",
    "chips": [("radio_button_checked", "green", "Confirmed", "Source shown"), ("wallpaper", "orange", "8 stories", "Then done")],
    "features_eyebrow": "How it works",
    "features_title": "How Underneath works",
    "features": [
        {
            "size": "third", "color": "orange", "kicker": "Short edition",
            "title": "A few stories, then you're done",
            "text": "Each edition has a small number of stories and a clear end. No endless feed.",
        },
        {
            "size": "two-thirds", "color": "red", "kicker": "Rumours",
            "title": "See the rumour going around",
            "text": "Each story starts with the claim you may have seen on WhatsApp, X or TikTok.",
            "shots": ["Rumour bills", "Noise on paper"],
        },
        {
            "size": "half", "color": "mint", "kicker": "The facts",
            "title": "Then read what's actually true",
            "text": "Swipe away the rumour to read the checked story.",
        },
        {
            "size": "half", "color": "green", "kicker": "Labels",
            "title": "Every story is labelled",
            "text": "Each story is marked confirmed, developing, unverified or false.",
        },
        {
            "size": "two-thirds", "color": "blue", "kicker": "Share",
            "title": "Share the checked version",
            "text": "When you share a story, its label and sources go with it.",
            "shots": ["Checked story", "Share with proof"],
        },
        {
            "size": "third", "color": "purple", "kicker": "Local first",
            "title": "News for where you live",
            "text": "Your edition starts with Jakarta and the topics you follow.",
        },
        {
            "size": "full", "color": "orange", "kicker": "Finish",
            "title": "You can see when you're done",
            "text": "The edition shows how many stories are left. When they're gone, you're up to date.",
            "shots": ["Halfway", "Clean", "Edition painted"],
        },
    ],
    "faq": [
        ("Who is Underneath for?",
         "Busy young workers in Indonesia who get their news from social media and group chats, and want a short, checked summary instead."),
        ("Is every story confirmed?",
         "No. Developing and unverified stories can appear, but each one is clearly labelled with its sources."),
        ("Who writes the stories?",
         "AI can draft them, but an editor approves every story before it goes into an edition."),
        ("Is it another endless feed?",
         "No. Each edition has a fixed number of stories. Nothing piles up if you miss a few days."),
    ],
    "values_eyebrow": "Why Underneath",
    "values_title": "Why not just follow the news on social media?",
    "values": [
        ("fact_check", "blue", "Checked, not viral", "Social feeds show what's popular. Underneath shows what's been checked."),
        ("done_all", "green", "It ends", "A few stories a day, then you're done."),
        ("block", "orange", "Nothing to keep you scrolling", "No unread badges, streaks or autoplay."),
    ],
    "cta_title": "Get tomorrow's edition",
    "cta_sub": "Join the waitlist and we'll email you when Underneath is ready to try.",
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
