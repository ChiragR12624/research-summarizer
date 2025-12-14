from sentence_transformers import SentenceTransformer


class Embedder:
    """
    Wrapper around SentenceTransformer for embedding text chunks
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts: list[str]):
        if not texts:
            return []
        return self.model.encode(texts, show_progress_bar=False)
