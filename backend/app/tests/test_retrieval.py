from backend.embeddings.embedder import Embedder
from backend.vectorstore.faiss_store import FAISSStore


def test_retrieval_pipeline():
    embedder = Embedder()
    store = FAISSStore()

    query = "large language models"
    query_embedding = embedder.embed([query])[0]

    results = store.search(query_embedding, k=3)

    assert isinstance(results, list)
    assert len(results) > 0
