# LLM-Based Research Paper Summarizer

## Quickstart (local)
1. python3 -m venv .venv && source .venv/bin/activate
2. pip install -r requirements.txt
3. uvicorn backend.app.main:app --reload --port 8000
4. streamlit run frontend/streamlit_app.py
