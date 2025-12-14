def chunk_text(text: str, max_words: int = 200, overlap: int = 50):
    """
    Split text into overlapping chunks
    """
    if not text:
        return []

    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + max_words
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += max_words - overlap

    return chunks
