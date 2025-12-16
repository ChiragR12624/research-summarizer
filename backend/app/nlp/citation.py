# backend/app/nlp/citation.py

import re

def extract_reference_section(text: str) -> str:
    parts = re.split(r"\nreferences\n|\nbibliography\n", text.lower())
    return parts[1] if len(parts) > 1 else ""

def parse_references(reference_text: str) -> list[str]:
    refs = reference_text.split("\n")
    return [r.strip() for r in refs if len(r.strip()) > 20]

def extract_inline_citations(text: str) -> list[str]:
    patterns = [
        r"\([A-Za-z]+ et al\., \d{4}\)",
        r"\[\d+\]"
    ]
    citations = []
    for p in patterns:
        citations.extend(re.findall(p, text))
    return list(set(citations))

def extract_citations(text: str):
    ref_section = extract_reference_section(text)
    return {
        "inline": extract_inline_citations(text),
        "references": parse_references(ref_section)
    }
