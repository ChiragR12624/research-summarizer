def chunk_text(
    text: str,
    chunk_size: int = 800,
    overlap: int = 100
) -> list[str]:
    """
    Splits text into overlapping chunks.
    chunk_size and overlap are measured in words.
    """
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = words[start:end]
        chunks.append(" ".join(chunk))
        start = end - overlap

        if start < 0:
            start = 0

    return chunks
