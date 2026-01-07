from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import upload, summary, query, analyze, download

app = FastAPI(title="LLM Research Paper Summarizer")

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- ROUTERS ----------------
app.include_router(upload.router, tags=["Upload"])
app.include_router(summary.router, tags=["Summary"])
app.include_router(query.router, tags=["RAG Query"])
app.include_router(analyze.router, tags=["Analysis"])
app.include_router(download.router, tags=["Download"])

# ---------------- HEALTH ----------------
@app.get("/")
def health():
    return {"status": "backend running"}
