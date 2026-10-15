"""BERSIH app content."""

APP = {
    "name": "BERSIH",
    "title": "Remove hidden location data from your photos",
    "description": "BERSIH removes the location, time and phone details hidden in your photos and videos before you share them. Your original stays untouched.",
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
    "h1": "Share photos without<br>sharing your location.",
    "sub": "Photos taken on your phone can store the exact place, date and time they were taken, and some apps pass that on when you share. BERSIH removes it before your photo leaves your phone.",
    "hero_shot": "Clean copy ready",
    "hero_note": "One email when BERSIH is ready to try. No spam.",
    "chips": [("ios_share", "red", "Share sheet", "Two taps"), ("edit_note", "blue", "Original", "Unchanged")],
    "features_eyebrow": "How it works",
    "features_title": "How BERSIH cleans a photo",
    "features": [
        {
            "size": "third", "color": "red", "kicker": "Hidden details",
            "title": "Every photo carries hidden details",
            "text": "Besides the image, the file can store where, when and on which phone it was taken.",
        },
        {
            "size": "two-thirds", "color": "blue", "kicker": "See what's stored",
            "title": "Location, time and phone, in plain language",
            "text": "BERSIH shows the location, date, time, phone, camera and editing app stored in your photo.",
            "shots": ["The back of the print", "Hidden fields"],
        },
        {
            "size": "half", "color": "orange", "kicker": "Clean copy",
            "title": "Make a clean copy",
            "text": "BERSIH makes a copy of your photo with those details removed.",
        },
        {
            "size": "half", "color": "purple", "kicker": "Share sheet",
            "title": "Works from the share sheet",
            "text": "Tap Share, choose Clean Copy, then send it in the app you were already using.",
        },
        {
            "size": "two-thirds", "color": "green", "kicker": "Original kept",
            "title": "Your original stays the same",
            "text": "The photo in your library keeps all its details. Only the copy you share is cleaned.",
            "shots": ["Original with back", "Clean reprint"],
        },
        {
            "size": "third", "color": "pink", "kicker": "Fast",
            "title": "Takes seconds",
            "text": "Cleaning adds only a few seconds to sharing.",
        },
        {
            "size": "full", "color": "indigo", "kicker": "Photos and video",
            "title": "Photos and videos",
            "text": "Clean one photo, several photos, or a video at once.",
            "shots": ["Four photos", "Video", "Share again"],
        },
    ],
    "faq": [
        ("What hidden details are in a photo?",
         "Often where it was taken, the date and time, the phone and camera model, and the apps used to edit it."),
        ("Does BERSIH change my original photo?",
         "No. It makes a clean copy to share and leaves your original alone."),
        ("Does it remove AI watermarks?",
         "Not in the first version. It removes location, time, date, phone and camera details from photos and videos."),
        ("Are my photos uploaded?",
         "No. Cleaning happens on your iPhone."),
    ],
    "values_eyebrow": "Why BERSIH",
    "values_title": "Why not just trust the app you post to?",
    "values": [
        ("travel_explore", "red", "Not every app removes it", "Some apps remove these details and some don't. BERSIH removes them every time, whatever app you use."),
        ("photo_library", "blue", "Keeps your memories", "Turning off location for your camera loses it for your own photos too. BERSIH keeps it on your originals."),
        ("cloud_off", "green", "Stays on your phone", "No account, and your photos are never uploaded."),
    ],
    "cta_title": "Share your next photo safely",
    "cta_sub": "Join the waitlist and we'll email you when BERSIH is ready to try.",
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
