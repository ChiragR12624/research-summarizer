from fastapi import APIRouter
from pydantic import BaseModel

from app.cache.sqlite_cache import CacheDB
from app.core.rag import answer_question

router = APIRouter()

class QueryRequest(BaseModel):
    paper_id: str
    question: str

@router.post("/rag_query")
def rag_query(payload: QueryRequest):
    cache = CacheDB()
    paper = cache.get_paper(payload.paper_id)

    if not paper:
        return {"error": "Paper not found"}

    answer, sources = answer_question(
        payload.question,
        paper["chunks"],
        paper["embeddings"]
    )

    return {
        "answer": answer,
        "sources": sources
    }
