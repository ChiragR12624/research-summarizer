from app.nlp.novelty import novelty_score

def test_novelty():
    abstract = "This paper introduces a novel transformer architecture."
    corpus = ["We propose a transformer model.", "CNNs for vision."]
    score = novelty_score(abstract, corpus)
    assert 0 <= score <= 1
