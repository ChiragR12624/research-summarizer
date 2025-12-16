# backend/app/nlp/novelty.py

from sentence_transformers import SentenceTransformer, util
from functools import lru_cache

_model = SentenceTransformer("all-MiniLM-L6-v2")

def novelty_score(abstract: str, corpus_abstracts: list[str]) -> float:
    paper_emb = _model.encode(abstract, convert_to_tensor=True)
    corpus_emb = _model.encode(corpus_abstracts, convert_to_tensor=True)

    similarities = util.cos_sim(paper_emb, corpus_emb)[0]
    max_similarity = similarities.max().item()

    return round(1 - max_similarity, 3)


@lru_cache(maxsize=256)
def encode_text(text):
    return _model.encode(text, convert_to_tensor=True)