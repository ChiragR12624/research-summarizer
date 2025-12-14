import faiss
import numpy as np
import pickle
from pathlib import Path


class FAISSStore:
    def __init__(self, dim: int = 384, index_path="data/faiss.index", meta_path="data/metadata.pkl"):
        self.dim = dim
        self.index_path = Path(index_path)
        self.meta_path = Path(meta_path)

        if self.index_path.exists():
            self.index = faiss.read_index(str(self.index_path))
            with open(self.meta_path, "rb") as f:
                self.metadata = pickle.load(f)
        else:
            self.index = faiss.IndexFlatL2(dim)
            self.metadata = []

    def add(self, texts, embeddings, metadata: dict):
        embeddings = np.array(embeddings).astype("float32")
        self.index.add(embeddings)

        for text in texts:
            self.metadata.append({
                "text": text,
                **metadata
            })

    def save(self):
        faiss.write_index(self.index, str(self.index_path))
        with open(self.meta_path, "wb") as f:
            pickle.dump(self.metadata, f)

    def search(self, query_embedding, k=5):
        query_embedding = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query_embedding, k)

        results = []
        for idx in indices[0]:
            if idx < len(self.metadata):
                results.append(self.metadata[idx])
        return results
