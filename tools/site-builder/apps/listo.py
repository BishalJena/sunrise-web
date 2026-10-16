"""LISTO app content."""

APP = {
    "name": "LISTO",
    "title": "Know every visa and document before you book",
    "description": "LISTO shows the visas, documents, transit rules and full cost of a trip before you book, with an official source for every rule.",
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
        "faint": "#5C5348",
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
            "orange": "#7A5E00",
            "pink": "#B0442E",
            "purple": "#8A7F6A",
            "red": "#B0442E",
        },
    },
    "icon": {
        "from": "#FFD100", "to": "#D9B45A",
        "stroke": "#0B0C0E",
        # Airport luggage tag.
        "glyph": '<path d="M42 28h36l16 16v48H42Z"/><path d="M78 28v18h16"/><circle cx="54" cy="42" r="5"/><path d="M54 62h27M54 76h18"/>',
    },
    "status": "Coming to iPhone",
    "h1": "Know every document<br>before you book.",
    "sub": "In 2024, more than 1 in 4 Schengen visa applications from Africa were refused, costing applicants about €60 million in fees. LISTO shows every visa, document and cost your trip needs before you spend money.",
    "hero_shot": "Check-in, Mexico City",
    "hero_note": "One email when LISTO is ready to try. No spam.",
    "chips": [("confirmation_number", "orange", "$1,092", "Full trip cost"), ("verified", "green", "Sources", "Checked monthly")],
    "features_eyebrow": "How it works",
    "features_title": "How LISTO plans your trip",
    "features": [
        {
            "size": "third", "color": "green", "kicker": "Passport first",
            "title": "Starts with your passport",
            "text": "Tell LISTO your passport, destination and any stopovers. The rules depend on all three.",
        },
        {
            "size": "two-thirds", "color": "orange", "kicker": "Documents",
            "title": "Every document you need, in one place",
            "text": "Visas, travel authorisations, insurance and flights are listed. Anything missing is clearly marked.",
            "shots": ["Table layout", "Missing documents"],
        },
        {
            "size": "half", "color": "red", "kicker": "Order",
            "title": "What to apply for first",
            "text": "If one document is needed before another, LISTO shows the order so you don't waste money.",
        },
        {
            "size": "half", "color": "orange", "kicker": "Full cost",
            "title": "The full cost, including waiting time",
            "text": "Flights, visa fees, insurance and how long approvals take, added up together.",
        },
        {
            "size": "two-thirds", "color": "blue", "kicker": "Airport",
            "title": "Know what the airport will ask for",
            "text": "Photos of each checkpoint show which documents staff will ask to see.",
            "shots": ["Checkpoint preview", "Counter proof"],
        },
        {
            "size": "third", "color": "indigo", "kicker": "Official sources",
            "title": "Every rule has a source",
            "text": "Each requirement shows the official source and the date it was last checked.",
        },
        {
            "size": "full", "color": "orange", "kicker": "Check-in pass",
            "title": "A summary to show at check-in",
            "text": "A pass with every rule and its source, ready to show at the counter.",
            "shots": ["Official site handoff", "Wallet pass", "Ready to go"],
        },
    ],
    "faq": [
        ("Does LISTO apply for visas?",
         "No. It tells you what you need and links to the official government sites. It never applies for you and never links to visa resellers."),
        ("Does it book flights?",
         "No. LISTO helps you check a route works before you book. You book with the airline or travel site."),
        ("How are the rules checked?",
         "Our team checks every rule each month. Each one shows its source and the date it was checked."),
        ("What does the full cost include?",
         "The fare, document fees, insurance, and the time you'll wait for approvals."),
    ],
    "values_eyebrow": "Why LISTO",
    "values_title": "Why not just search online?",
    "values": [
        ("public", "green", "Rules for your passport", "Most travel sites show one set of rules. LISTO shows the rules for your passport on your route."),
        ("fact_check", "orange", "Sources you can check", "Every rule shows its official source and when it was checked."),
        ("no_transfer", "red", "No middlemen", "LISTO sends you to official government sites. It never uses visa resellers."),
    ],
    "cta_title": "Plan your next trip with no surprises",
    "cta_sub": "Join the waitlist and we'll email you when LISTO is ready to try.",
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
