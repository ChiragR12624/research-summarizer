from fastapi import FastAPI
from pydantic import BaseModel

from app.nlp import (
    extract_keywords,
    classify_topic,
    novelty_score,
    extract_citations,
    gap_summary,
    build_section_graph,
    graph_to_dict
)

import json
from datetime import datetime
from pathlib import Path

# -------------------------
# App initialization
# -------------------------
app = FastAPI()

# -------------------------
# Input schema
# -------------------------
class PaperInput(BaseModel):
    text: str
    abstract: str
    sections: list[str]
    corpus_abstracts: list[str]

# -------------------------
# Results storage setup
# -------------------------
RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

def save_result(data: dict):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = RESULTS_DIR / f"analysis_{timestamp}.json"
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

# -------------------------
# API endpoint
# -------------------------
@app.post("/analyze-paper")
def analyze_paper(data: PaperInput):
    keywords = extract_keywords(data.text)
    topics = classify_topic(data.abstract)
    citations = extract_citations(data.text)
    novelty = novelty_score(data.abstract, data.corpus_abstracts)
    gaps = gap_summary(data.text)

    graph = build_section_graph(data.sections)
    graph_data = graph_to_dict(graph)

    # ---- FINAL RESULT ----
    result = {
        "keywords": keywords,
        "topics": topics,
        "citations": citations,
        "novelty_score": novelty,
        "research_gaps": gaps,
        "section_graph": graph_data
    }

    # ---- SAVE TO DISK ----
    save_result(result)

    return result
