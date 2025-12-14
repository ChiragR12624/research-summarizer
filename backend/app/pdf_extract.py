# backend/app/pdf_extract.py
import fitz  # pymupdf
from pathlib import Path
from typing import Dict

def extract_text_from_pdf(pdf_path: str) -> Dict:
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc):
        txt = page.get_text("text")
        pages.append({"page": i+1, "text": txt})
    combined = "\n\n".join(p["text"] for p in pages)
    return {"text": combined, "pages": pages}



import logging
logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        logger.exception("Failed to open PDF: %s", pdf_path)
        raise
    # rest as before...