from app.nlp.keywords import extract_keywords

def test_keywords():
    text = "Transformers are used in NLP and machine learning."
    result = extract_keywords(text)
    assert "transformers" in " ".join(result["keybert"]).lower()
