"""Lotus E-2: check whether someone has an active public dating profile."""

APP = {
    "listed": False,
    "name": "Lotus E-2",
    "title": "Find out if they're still on dating apps",
    "description": "Lotus E-2 checks popular dating apps for active public profiles, so you can find out instead of wondering.",
    "brand": "var(--accent-purple)",
    "brand2": "var(--accent-pink)",
    "icon": {
        "from": "#c77dff", "to": "#7b2cbf",
        # heart with a magnifier
        "glyph": '<path d="M54 86S28 70 28 50a14 14 0 0 1 26-7 14 14 0 0 1 26 7c0 6-2 11-6 16"/><circle cx="78" cy="78" r="10"/><path d="m86 86 8 8"/>',
    },
    "status": "Coming to iPhone",
    "h1": "Find out if they're<br>still on dating apps.",
    "sub": "In one survey, 42% of Tinder users said they were already married or in a relationship. Lotus E-2 checks popular dating apps for an active profile, so you can stop wondering.",
    "hero_shot": "Search report",
    "hero_note": "One email when Lotus E-2 is ready to try. No spam.",
    "chips": [("travel_explore", "purple", "7 apps", "Checked"), ("lock", "green", "Private", "Only you see it")],
    "features_eyebrow": "How it works",
    "features_title": "How Lotus E-2 works",
    "features": [
        {
            "size": "third", "color": "blue", "kicker": "Their details",
            "title": "Enter their details",
            "text": "Add their name, age and area so the search finds the right person.",
        },
        {
            "size": "two-thirds", "color": "purple", "kicker": "One search",
            "title": "One search across popular dating apps",
            "text": "Lotus E-2 checks public profiles on the most popular dating apps at once. You don't need to sign up to any of them.",
            "shots": ["Search", "Results by app"],
        },
        {
            "size": "half", "color": "orange", "kicker": "Result",
            "title": "A clear result",
            "text": "See any active profiles, how sure the match is, and when the profile was last active.",
        },
        {
            "size": "half", "color": "green", "kicker": "Private",
            "title": "Only you see your searches",
            "text": "Your searches and results are private, and you can delete them any time.",
        },
        {
            "size": "two-thirds", "color": "pink", "kicker": "Next steps",
            "title": "Help with what comes next",
            "text": "Advice on how to bring it up, because a match is a reason to talk, not proof.",
            "shots": ["Conversation guide", "Support"],
        },
        {
            "size": "third", "color": "indigo", "kicker": "Public only",
            "title": "Public profiles only",
            "text": "Lotus E-2 only checks what dating apps show publicly. It never logs in to anyone's account or reads messages.",
        },
        {
            "size": "full", "color": "mint", "kicker": "Simple",
            "title": "Simple from start to finish",
            "text": "Clear screens from search to result, made for a stressful moment.",
            "shots": ["Search", "Report", "Next steps"],
        },
    ],
    "faq": [
        ("How does Lotus E-2 search?",
         "It only looks at what dating apps show publicly, using the details you enter. It never logs in to anyone's account or reads private messages."),
        ("Will the person know I searched?",
         "No. Your searches and results are private. We never contact or notify anyone."),
        ("Is a match proof of cheating?",
         "No. A profile might be old, fake, or someone who looks similar. Use the result to start an honest conversation."),
        ("Is this legal?",
         "Lotus E-2 only uses public information. You agree to use it responsibly and lawfully, and never to harass or stalk anyone."),
    ],
    "values_eyebrow": "Why Lotus E-2",
    "values_title": "Why not just check the apps yourself?",
    "values": [
        ("travel_explore", "blue", "Every app at once", "Checking yourself means signing up to each app and searching one by one. Lotus E-2 checks them all in one search."),
        ("lock", "purple", "Nobody knows you looked", "You don't need a dating profile, and the person is never notified."),
        ("favorite", "pink", "Help with the next step", "Advice on how to talk about what you find."),
    ],
    "cta_title": "Find out instead of wondering",
    "cta_sub": "Join the waitlist and we'll email you when Lotus E-2 is ready to try.",
    "release_notes": [
        {
            "tag": "Pre-launch", "date": "October 9, 2026", "title": "The waitlist is open",
            "body": '''        <p>Lotus E-2 is in development: an iPhone app that checks popular dating apps for active public profiles, so you can get clarity about your relationship.</p>
        <p>Here's what we're building first:</p>
        <ul>
          <li>One search across popular dating apps</li>
          <li>Targeted matching by name, age and area</li>
          <li>Clear reports with match confidence and last-active time</li>
        </ul>
        <p>We're working through how to do this using only public information, in a way that respects everyone's privacy.</p>''',
        },
    ],
    "roadmap": [
        ("done", "Waitlist opens", "This website and early sign-ups."),
        ("now", "Technical approach", "Working out how to search public profiles reliably and responsibly."),
        ("", "User interviews", "Learning what people need when they're unsure about a relationship."),
        ("", "App Store review", "Making sure the app meets App Store guidelines."),
        ("", "TestFlight beta", "Early access for people on the waitlist."),
    ],
    "contact_email": "hello@lotus-e2.app",
    "contact_topics": ["General question", "Feature idea", "Remove my information", "Press"],
    "privacy_intro": "Lotus E-2 deals with sensitive questions, so we take privacy seriously for both you and the people you search for. This policy explains what we collect through this website today and what the app is designed to do once it launches.",
    "privacy": [
        ("Your searches (once the app launches)", '''        <p>The details you enter and the reports you receive are private to you. We use them only to run your search, and you can delete them at any time. We never notify the person you search for.</p>'''),
        ("People who are searched for", '''        <p>We only use information that dating apps make publicly visible. If you believe your information appears in Lotus E-2 and you'd like it removed, contact us and we'll act on it promptly.</p>'''),
    ],
    "terms": [
        ("Responsible use", '''        <p>Use Lotus E-2 only to look up a current partner or someone you're dating, and only for your own peace of mind. Don't use it to harass, stalk, threaten, embarrass or monitor anyone, or for any purpose that's illegal where you live. We may suspend access for misuse.</p>'''),
        ("Results", '''        <p>Results are based on public profile information and may be incomplete, outdated or mistaken. A possible match isn't proof that someone is using a dating app or being unfaithful. Lotus E-2 isn't affiliated with or endorsed by any dating app.</p>'''),
    ],
}
