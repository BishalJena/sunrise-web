"""BERSIH app content."""

APP = {
    "name": "BERSIH",
    "title": "Every photo has two sides",
    "description": "BERSIH makes a clean copy from the share sheet: the front goes out, while the location, time and phone details stay on the original.",
    "brand": "#D9452B",
    "brand2": "#24408E",
    "font_links": (
        "https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Caveat:wght@500;600&family=Inter:opsz,wght@14..32,400..700&display=swap",
    ),
    "theme": {
        "page": "#E8E2D8",
        "card": "#F2E9D9",
        "inset": "#E9DDCB",
        "line": "#D9CCB8",
        "ink": "#1A1714",
        "muted": "#5E554A",
        "faint": "#5C5348",
        "hairline": "rgb(26 23 20 / .13)",
        "button": "#BD3C25",
        "on_button": "#FFF7EA",
        "shadow_card": "0 0 0 1px rgb(26 23 20 / .08), 0 24px 60px -38px rgb(26 23 20 / .38)",
        "shadow_float": "0 0 0 1px rgb(26 23 20 / .10), 0 18px 36px -22px rgb(26 23 20 / .45)",
        "font_text": '"Inter", -apple-system, BlinkMacSystemFont, sans-serif',
        "font_display": '"Barlow Condensed", "Inter", sans-serif',
        "font_rounded": '"Caveat", "Inter", sans-serif',
        "accents": {
            "blue": "#24408E",
            "green": "#53705A",
            "indigo": "#5A4FA6",
            "mint": "#F2E9D9",
            "orange": "#BD3C25",
            "pink": "#856152",
            "purple": "#5A4FA6",
            "red": "#BD3C25",
        },
    },
    "icon": {
        "from": "#F2E9D9", "to": "#D9452B",
        "stroke": "#1A1714",
        # Photo-lab envelope with a print inside.
        "glyph": '<path d="M26 43h68v42H26Z"/><path d="m26 43 34 25 34-25"/><path d="M39 30h42v33H39Z"/>',
    },
    "status": "Share sheet first",
    "h1": "The front is for everyone.<br>The back is just for you.",
    "sub": "BERSIH keeps the memory on your original and sends out a clean copy with the location, time and phone details removed.",
    "hero_shot": "Clean copy ready",
    "hero_note": "No spam. One email when early access opens.",
    "chips": [('ios_share', 'red', 'Share sheet', 'Two extra taps'), ('edit_note', 'blue', 'Back kept', 'Original unchanged')],
    "features_title": "The words go home<br>before the photo leaves.",
    "features": [
        {
            "size": "third", "color": "red", "kicker": "Two sides",
            "title": "A photo turns over like a print",
            "text": "The front is the image. The back is where the private details were written.",
        },
        {
            "size": "two-thirds", "color": "blue", "kicker": "Metadata",
            "title": "Where, when, and on which phone",
            "text": "Location, date, time, device, camera and software details are shown in plain language.",
            "shots": ["The back of the print", "Hidden fields"],
        },
        {
            "size": "half", "color": "orange", "kicker": "The peak",
            "title": "The words go home",
            "text": "A clean reprint slides out. The private words lift off the copy and settle back onto the original.",
        },
        {
            "size": "half", "color": "purple", "kicker": "Share sheet",
            "title": "Clean where she already shares",
            "text": "Pick Clean Copy from the share sheet, then send the copy to the app she was already using.",
        },
        {
            "size": "two-thirds", "color": "green", "kicker": "Original kept",
            "title": "Nothing is lost from her memory",
            "text": "Her library keeps the photo with its back intact. Only the copy has a blank back.",
            "shots": ["Original with back", "Clean reprint"],
        },
        {
            "size": "third", "color": "pink", "kicker": "After the first time",
            "title": "Two seconds",
            "text": "Once she knows the move, cleaning adds only a few seconds to a normal share.",
        },
        {
            "size": "full", "color": "indigo", "kicker": "Photos and video",
            "title": "One clean action for the media she posts",
            "text": "A single photo, several photos, or a video can leave with a blank back.",
            "shots": ["Four photos", "Video", "Share again"],
        },
    ],
    "faq": [
        ("What is on the back of a photo?",
         "The hidden file details: often where the photo was taken, the date and time, the phone and camera, and the software that touched it."),
        ("Does BERSIH delete my memory?",
         "No. The original stays as it is. BERSIH creates a clean copy to share and leaves your own photo alone."),
        ("Does it remove AI watermarks?",
         "Not in v1. The first version is focused on metadata: location, time, date, phone and camera details for photos and videos."),
        ("Are photos uploaded?",
         "No. The cleaning is designed to happen on your iPhone, inside the share flow."),
    ],
    "values_title": "For the moment before posting",
    "values": [
        ("photo_library", "blue", "Memory stays", "Your original keeps its back. The shared copy does not."),
        ("ios_share", "red", "No new habit", "It lives where she already shares: the iOS share sheet."),
        ("cloud_off", "green", "On device", "No account and no upload path for the media being cleaned."),
    ],
    "cta_title": "Post the front. Keep the back.",
    "cta_sub": "Join the waitlist for the first BERSIH TestFlight.",
    "release_notes": [
        {
            "tag": "Pre-launch", "date": "October 9, 2026", "title": "The waitlist is open",
            "body": '''        <p>BERSIH is in development: an iPhone share-sheet action that makes a clean copy before a photo or video leaves your phone.</p>
        <p>Here is what we are building first:</p>
        <ul>
          <li>Removal of location, date, time, phone and camera metadata</li>
          <li>A clean-copy flow that keeps the original unchanged</li>
          <li>Support for photos, multiple photos and video</li>
          <li>Fully on-device processing</li>
        </ul>''',
        },
    ],
    "roadmap": [
        ("done", "Waitlist opens", "This website and early sign-ups."),
        ("now", "Metadata engine", "Removing location, time, device and camera fields from common formats."),
        ("", "Share-sheet action", "Cleaning media inside the flow people already use."),
        ("", "Video support", "Handling long files without making the wait feel stuck."),
        ("", "TestFlight beta", "Early access for people on the waitlist."),
    ],
    "contact_email": "hello@lotus-e1.app",
    "contact_topics": ["General question", "Feature idea", "Partnerships", "Press"],
    "privacy_intro": "BERSIH is a privacy tool, so it is built to collect nothing it does not need. This policy explains the waitlist today and the app we are building.",
    "privacy": [
        ("Your photos and videos (once the app launches)", '''        <p>Media you clean is processed entirely on your iPhone. We never upload, view or store your photos or videos, and the app does not need an account.</p>'''),
    ],
    "terms": [
        ("Using BERSIH", '''        <p>Use BERSIH only with media you own or have the right to share, and in line with the laws where you live and the rules of the platforms you post to.</p>
        <p>We remove metadata fields we know about, but file formats change and we cannot guarantee that every piece of identifying information is removed in every case.</p>'''),
    ],
}
