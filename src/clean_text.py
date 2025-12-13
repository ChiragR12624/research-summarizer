import re

def clean_text(text):
    """
    Cleans raw extracted text from PDF
    """
    # Remove citation numbers like [1], [23]
    text = re.sub(r'\[\d+\]', '', text)

    # Remove multiple spaces/newlines
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def split_into_sections(text):
    """
    Splits cleaned text into research paper sections
    """
    sections = {}

    pattern = r"(ABSTRACT|INTRODUCTION|METHODOLOGY|METHODS|RESULTS|DISCUSSION|CONCLUSION|REFERENCES)"
    parts = re.split(pattern, text, flags=re.IGNORECASE)

    for i in range(1, len(parts), 2):
        title = parts[i].upper()
        content = parts[i + 1].strip()
        sections[title] = content

    return sections
