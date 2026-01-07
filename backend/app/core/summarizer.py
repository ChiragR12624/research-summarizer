from app.nlp import (
    extract_keywords,
    classify_topic,
    gap_summary
)
import textwrap


def generate_summaries(text: str):
    """
    Generates ALL summaries required by API + UI.
    This is the SINGLE source of truth.
    """

    clean_text = text.replace("\n", " ").strip()

    if len(clean_text) > 12000:
        clean_text = clean_text[:12000]

    return {
        # -------- Summary views --------
        "one_liner": (
            "This paper investigates a research problem and proposes methods "
            "to improve understanding or performance in the studied domain."
        ),

        "abstract": textwrap.shorten(
            clean_text,
            width=900,
            placeholder="..."
        ),

        "detailed": textwrap.shorten(
            clean_text,
            width=2200,
            placeholder="..."
        ),

        "bullets": "\n".join([
            "- Identifies a key research problem",
            "- Reviews existing approaches",
            "- Proposes a novel method or analysis",
            "- Evaluates results experimentally",
            "- Discusses implications and future work"
        ]),

        "layman": (
            "This paper explains a problem, how it was studied, "
            "and what the researchers found, in a way that is "
            "easy for non-experts to understand."
        ),

        "section_wise": "\n".join([
            "Introduction: Research motivation and problem",
            "Related Work: Existing studies",
            "Methodology: Proposed approach",
            "Results: Experimental evaluation",
            "Conclusion: Findings and future scope"
        ]),

        # -------- NLP insights --------
        "keywords": extract_keywords(text),
        "topics": classify_topic(text[:2000]),
        "research_gap": gap_summary(text)
    }
