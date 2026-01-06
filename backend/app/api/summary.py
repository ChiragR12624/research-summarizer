from fastapi import APIRouter
from app.cache.sqlite_cache import CacheDB

router = APIRouter()

@router.get("/get_summary/{paper_id}/{summary_type}")
def get_summary(paper_id: str, summary_type: str):
    cache = CacheDB()
    paper = cache.get_paper(paper_id)

    if not paper:
        return {"error": "Paper not found"}

    summaries = paper.get("summaries")
    if not summaries:
        return {"error": "Summaries not generated for this paper. Re-upload required."}

    if summary_type not in summaries:
        return {
            "error": f"Invalid summary_type '{summary_type}'. "
                     f"Valid options: {list(summaries.keys())}"
        }

    return {
        "type": summary_type,
        "content": summaries[summary_type]
    }


@router.get("/get_keywords/{paper_id}")
def get_keywords(paper_id: str):
    cache = CacheDB()
    paper = cache.get_paper(paper_id)

    if not paper or "summaries" not in paper:
        return {"error": "Summaries not available. Re-upload paper."}

    return {"keywords": paper["summaries"]["keywords"]}


@router.get("/get_topics/{paper_id}")
def get_topics(paper_id: str):
    cache = CacheDB()
    paper = cache.get_paper(paper_id)

    if not paper or "summaries" not in paper:
        return {"error": "Summaries not available. Re-upload paper."}

    return {"topics": paper["summaries"]["topics"]}


@router.get("/get_research_gap/{paper_id}")
def get_research_gap(paper_id: str):
    cache = CacheDB()
    paper = cache.get_paper(paper_id)

    if not paper or "summaries" not in paper:
        return {"error": "Summaries not available. Re-upload paper."}

    return {"research_gap": paper["summaries"]["research_gap"]}
