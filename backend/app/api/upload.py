from fastapi import APIRouter, UploadFile, File, BackgroundTasks
from app.workers.background import process_paper
import uuid, os

router = APIRouter()

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload_paper")
async def upload_paper(
    file: UploadFile = File(...),
    background_tasks: BackgroundTasks = None
):
    paper_id = str(uuid.uuid4())
    save_path = f"{UPLOAD_DIR}/{paper_id}.pdf"

    with open(save_path, "wb") as f:
        f.write(await file.read())

    background_tasks.add_task(process_paper, paper_id, save_path)

    return {"paper_id": paper_id, "status": "processing"}
