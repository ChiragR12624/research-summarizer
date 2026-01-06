from app.nlp import (
    extract_keywords,
    classify_topic,
    gap_summary
)

def generate_summaries(text: str):
    return {
        "keywords": extract_keywords(text),
        "topics": classify_topic(text[:2000]),
        "research_gap": gap_summary(text)
    }
