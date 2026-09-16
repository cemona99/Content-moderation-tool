from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from rules import check_banned_words, check_spam_patterns

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    return scores["compound"]

def moderate_text(text):
    banned = check_banned_words(text)
    spam = check_spam_patterns(text)
    sentiment = analyze_sentiment(text)

    reasons = []
    if banned:
        reasons.append(f"banned words: {banned}")
    if spam:
        reasons.append(f"spam patterns: {spam}")
    if sentiment <= -0.5:
        reasons.append(f"highly negative sentiment ({sentiment})")

    if banned or spam:
        status = "REJECTED"
    elif sentiment <= -0.5:
        status = "FLAGGED"
    else:
        status = "APPROVED"

    return {
        "text": text,
        "status": status,
        "sentiment": sentiment,
        "reasons": reasons
    }
    