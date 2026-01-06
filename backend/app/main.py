from fastapi import FastAPI

from app.api import analyze, upload, query, summary

app = FastAPI(
    title="LLM-based Research Paper Summarizer",
    description="Backend API for analyzing and querying research papers",
    version="0.1.0"
)

# -------------------------
# Register routers FIRST
# -------------------------
app.include_router(analyze.router)
app.include_router(upload.router)
app.include_router(query.router)
app.include_router(summary.router)

# -------------------------
# Root endpoint LAST
# -------------------------
@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Research Summarizer Backend is up"
    }
