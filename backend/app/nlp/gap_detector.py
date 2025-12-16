# backend/app/nlp/gap_detector.py

GAP_PHRASES = [
    "however",
    "limited",
    "few studies",
    "not explored",
    "challenge remains",
    "future work",
    "open problem",
    "lack of"
]

def heuristic_gap_detector(text: str) -> list[str]:
    sentences = text.split(".")
    gaps = [
        s.strip() for s in sentences
        if any(phrase in s.lower() for phrase in GAP_PHRASES)
    ]
    return gaps

def gap_summary(text: str):
    gaps = heuristic_gap_detector(text)
    return {
        "gap_count": len(gaps),
        "gap_sentences": gaps[:5]  # limit output
    }
