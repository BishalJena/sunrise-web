"""LISTO app content."""

APP = {
    "name": "LISTO",
    "title": "Every trip, laid out",
    "description": "LISTO lays out the documents, transit rules, true cost, and check-in proof for a trip before you book it.",
    "brand": "#FFD100",
    "brand2": "#1F3A2E",
    "font_links": (
        "https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@400;500;600;700&family=Instrument+Serif&display=swap",
    ),
    "theme": {
        "page": "#E7E5E0",
        "card": "#FBF8F1",
        "inset": "#EFE9DE",
        "line": "#D2CEC6",
        "ink": "#0B0C0E",
        "muted": "#5D6470",
        "faint": "#807766",
        "hairline": "rgb(11 12 14 / .12)",
        "button": "#0B0C0E",
        "on_button": "#FFD100",
        "shadow_card": "0 0 0 1px rgb(11 12 14 / .08), 0 24px 60px -36px rgb(11 12 14 / .35)",
        "shadow_float": "0 0 0 1px rgb(11 12 14 / .10), 0 18px 36px -22px rgb(11 12 14 / .45)",
        "font_text": '"Barlow", -apple-system, BlinkMacSystemFont, "Inter", sans-serif',
        "font_display": '"Instrument Serif", Georgia, serif',
        "font_rounded": '"Barlow Condensed", "Barlow", sans-serif',
        "accents": {
            "blue": "#2E5F8A",
            "green": "#1F3A2E",
            "indigo": "#3F4654",
            "mint": "#EFE9DE",
            "orange": "#FFD100",
            "pink": "#B0442E",
            "purple": "#8A7F6A",
            "red": "#B0442E",
        },
    },
    "icon": {
        "from": "#FFD100", "to": "#D9B45A",
        # Airport luggage tag.
        "glyph": '<path d="M42 28h36l16 16v48H42Z"/><path d="M78 28v18h16"/><circle cx="54" cy="42" r="5"/><path d="M54 62h27M54 76h18"/>',
    },
    "status": "Coming to iPhone",
    "h1": "Here's everything<br>you'll need.",
    "sub": "LISTO lays the trip on the table: documents, transit rules, true cost, timing, and what to show at the counter.",
    "hero_shot": "Trip laid out",
    "hero_note": "No spam. One email when early access opens.",
    "chips": [('confirmation_number', 'orange', '$1,092', 'True total'), ('verified', 'green', 'Sources', 'Checked monthly')],
    "features_title": "Before he books,<br>he knows the whole trip.",
    "features": [
        {
            "size": "third", "color": "green", "kicker": "Passport first",
            "title": "Built for restricted passports",
            "text": "LISTO starts with who is travelling, where they are going, and where they will transit.",
        },
        {
            "size": "two-thirds", "color": "orange", "kicker": "Laid out",
            "title": "Documents appear on the linen table",
            "text": "Visas, eTAs, insurance, and flights drop into place. Missing items stay as labelled outlines.",
            "shots": ["Table layout", "Missing documents"],
        },
        {
            "size": "half", "color": "red", "kicker": "Dependencies",
            "title": "The red thread shows what blocks what",
            "text": "If one visa unlocks another permit, the thread makes the order visible before money is spent.",
        },
        {
            "size": "half", "color": "orange", "kicker": "True total",
            "title": "Time counts as a cost",
            "text": "Flights, fees, insurance, and visa wait time sit on the same yellow luggage tag.",
        },
        {
            "size": "two-thirds", "color": "blue", "kicker": "Walk it before you fly",
            "title": "The airport, step by step",
            "text": "Real checkpoint photos show what staff will ask for and which documents to have in hand.",
            "shots": ["Checkpoint preview", "Counter proof"],
        },
        {
            "size": "third", "color": "indigo", "kicker": "Official sources",
            "title": "Rules with dates, not guesses",
            "text": "Every requirement names the source and the date it was checked.",
        },
        {
            "size": "full", "color": "orange", "kicker": "Counter pass",
            "title": "Something to show at check-in",
            "text": "The pass summarizes each rule and source, so the trip is ready at the counter.",
            "shots": ["Official site handoff", "Wallet pass", "Ready to go"],
        },
    ],
    "faq": [
        ("Does LISTO apply for visas?",
         "No. It explains what is needed and hands off to official government sites. It never applies for you and never links to visa resellers."),
        ("Does it book flights?",
         "No. LISTO helps decide whether a route works before you book. Booking stays with the airline or travel provider."),
        ("How are rules checked?",
         "The database is curated by the team and re-checked every month. Each rule shows its source and checked date."),
        ("What is the true total?",
         "The fare plus document fees, insurance, and the time cost of waiting for approvals. A cheaper route is not cheaper if it needs months of paperwork."),
    ],
    "values_title": "For travellers who cannot wing it",
    "values": [
        ("public", "green", "Passport-aware", "The same route can mean different rules for different passports."),
        ("fact_check", "orange", "Proof over promises", "Rules, sources and checked dates stay visible."),
        ("no_transfer", "red", "No resellers", "LISTO guides and hands off. It does not book, apply or pretend to be official."),
    ],
    "cta_title": "Know the documents before the fare",
    "cta_sub": "Join the waitlist for LISTO: Travel Ready.",
    "release_notes": [
        {
            "tag": "Pre-launch", "date": "October 9, 2026", "title": "The waitlist is open",
            "body": '''        <p>LISTO is in development for travellers whose routes depend on the passport they hold, the countries they transit, and the rules at the counter.</p>
        <p>Here is what we are building first:</p>
        <ul>
          <li>A trip table with documents, dependencies and missing items</li>
          <li>A true total that includes fees, insurance and visa wait time</li>
          <li>Official-source handoffs with checked dates</li>
          <li>An airport walk and a counter pass to show what is ready</li>
        </ul>''',
        },
    ],
    "roadmap": [
        ("done", "Waitlist opens", "This website and early sign-ups."),
        ("now", "Rules database", "Curating requirements by passport, destination and transit airport."),
        ("", "Source checks", "Attaching official links and monthly checked dates."),
        ("", "Airport walk", "Designing checkpoint previews for common routes."),
        ("", "TestFlight beta", "Early access for people on the waitlist."),
    ],
    "contact_email": "hello@lotus-f2.app",
    "contact_topics": ["General question", "Feature idea", "Travel data partnerships", "Press"],
    "privacy_intro": "LISTO is built around sensitive travel plans. This policy explains what this website collects today and how the app is designed to handle trip data.",
    "privacy": [
        ("Trip details (once the app launches)", '''        <p>Trips and document checklists are designed to stay on your device. If you turn on iCloud, they sync through your private iCloud account.</p>'''),
        ("Rule checks", '''        <p>We may use anonymous route demand to decide which passport and country rules to curate next. We do not sell travel plans.</p>'''),
    ],
    "terms": [
        ("Guidance, not official advice", '''        <p>LISTO provides travel-document guidance, not legal advice. Entry rules change often. Always confirm requirements with official government sources and your airline before you travel.</p>'''),
        ("No booking or applications", '''        <p>LISTO does not book flights, submit visa applications, or act as a government service. Links to official sites are provided so you can continue there yourself.</p>'''),
    ],
}
