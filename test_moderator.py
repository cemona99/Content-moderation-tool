from moderator import moderate_text

def test_approved_content():
    result = moderate_text("The weather today is quite nice")
    assert result["status"] == "APPROVED"
    print("✅ test_approved_content passed")

def test_banned_word_rejected():
    result = moderate_text("This is a scam")
    assert result["status"] == "REJECTED"
    assert "scam" in str(result["reasons"])
    print("✅ test_banned_word_rejected passed")

def test_spam_pattern_rejected():
    result = moderate_text("Click here for a free money offer")
    assert result["status"] == "REJECTED"
    print("✅ test_spam_pattern_rejected passed")

def test_negative_sentiment_flagged():
    result = moderate_text("I hate everything about this terrible day")
    assert result["status"] in ["REJECTED", "FLAGGED"]
    print("✅ test_negative_sentiment_flagged passed")

if __name__ == "__main__":
    test_approved_content()
    test_banned_word_rejected()
    test_spam_pattern_rejected()
    test_negative_sentiment_flagged()
    print("\n🎉 All tests passed!")
    