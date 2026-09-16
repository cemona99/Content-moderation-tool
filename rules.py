BANNED_WORDS = [
    "spam", "scam", "fraud", "hate", "stupid", "idiot"
]

SPAM_KEYWORDS = [
    "click here", "buy now", "free money", "act now", "limited offer"
]

def check_banned_words(text):
    text_lower = text.lower()
    found = [word for word in BANNED_WORDS if word in text_lower]
    return found

def check_spam_patterns(text):
    text_lower = text.lower()
    found = [kw for kw in SPAM_KEYWORDS if kw in text_lower]

    caps_ratio = sum(1 for c in text if c.isupper()) / max(len(text), 1)
    if caps_ratio > 0.5 and len(text) > 10:
        found.append("excessive_caps")

    return found
