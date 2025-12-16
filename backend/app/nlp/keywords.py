# backend/app/nlp/keywords.py

import yake
from keybert import KeyBERT

# -------------------------
# YAKE Keyword Extraction
# -------------------------

def extract_keywords_yake(text, top_k=10):
    kw_extractor = yake.KeywordExtractor(
        lan="en",
        n=3,
        dedupLim=0.9,
        top=top_k
    )
    keywords = kw_extractor.extract_keywords(text)
    return [kw for kw, score in keywords]


# -------------------------
# KeyBERT Keyword Extraction
# -------------------------

_kw_model = KeyBERT("all-MiniLM-L6-v2")

def extract_keywords_keybert(text, top_k=10):
    keywords = _kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 3),
        stop_words="english",
        top_n=top_k
    )
    return [kw for kw, score in keywords]


# -------------------------
# Combined Keywords
# -------------------------

def extract_keywords(text, top_k=10):
    return {
        "yake": extract_keywords_yake(text, top_k),
        "keybert": extract_keywords_keybert(text, top_k)
    }
