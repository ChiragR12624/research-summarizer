import numpy as np
from sentence_transformers import SentenceTransformer

_model = SentenceTransformer("all-MiniLM-L6-v2")

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def answer_question(
    question: str,
    chunks: list[str],
    embeddings: list[list[float]],
    top_k: int = 3
):
    q_embedding = _model.encode([question])[0]

    scores = []
    for idx, emb in enumerate(embeddings):
        score = cosine_similarity(q_embedding, np.array(emb))
        scores.append((idx, score))

    scores.sort(key=lambda x: x[1], reverse=True)
    top_indices = [idx for idx, _ in scores[:top_k]]

    context = "\n\n".join([chunks[i] for i in top_indices])

    # Simple heuristic answer (replace with LLM later)
    answer = f"Based on the paper, the relevant context is:\n\n{context[:1000]}"

    sources = [f"chunk_{i}" for i in top_indices]

    return answer, sources
