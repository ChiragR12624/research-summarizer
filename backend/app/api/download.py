from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.cache.sqlite_cache import CacheDB
import json
import os

router = APIRouter()

@router.get("/download_report/{paper_id}")
def download_report(paper_id: str):
    cache = CacheDB()
    paper = cache.get_paper(paper_id)

    if not paper:
        return {"error": "Paper not found"}

    os.makedirs("data/reports", exist_ok=True)
    path = f"data/reports/{paper_id}.json"

    with open(path, "w") as f:
        json.dump(paper, f, indent=2)

    return FileResponse(path, filename=f"{paper_id}_report.json")
