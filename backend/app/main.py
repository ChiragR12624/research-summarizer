from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import uuid
from pathlib import Path

app = FastAPI(title="Research Summarizer Backend")

DATA_DIR = Path("data/uploads")
DATA_DIR.mkdir(parents=True, exist_ok=True)

@app.get("/")
def root():
    return {"status": "ok", "message": "Backend running successfully"}

@app.post("/upload_paper")
async def upload_paper(file: UploadFile = File(...)):
    # Create unique paper ID
    paper_id = str(uuid.uuid4())[:8]

    # Save directory
    save_dir = DATA_DIR / paper_id
    save_dir.mkdir(parents=True, exist_ok=True)

    # Save PDF
    pdf_path = save_dir / file.filename
    contents = await file.read()
    with open(pdf_path, "wb") as f:
        f.write(contents)

    return JSONResponse({
        "status": "uploaded",
        "paper_id": paper_id,
        "filename": file.filename
    })
