from app.cache.sqlite_cache import CacheDB
from app.core.pdf_extract import extract_text
from app.core.chunker import chunk_text
from app.core.embeddings import embed_chunks

def process_paper(paper_id: str, pdf_path: str):
    print(f"✅ Background processing started for paper_id={paper_id}")

    text = extract_text(pdf_path)
    print(f"📄 Extracted {len(text)} characters")

    chunks = chunk_text(text)
    print(f"🧩 Created {len(chunks)} text chunks")

    embeddings = embed_chunks(chunks)
    print(f"🧠 Generated {len(embeddings)} embeddings")

    cache = CacheDB()

    data = {
        "paper_id": paper_id,
        "text": text,
        "chunks": chunks,
        "embeddings": embeddings,
        "status": "processed"
    }

    cache.store_paper(paper_id, data)

    print(f"💾 Cached text + chunks + embeddings for paper_id={paper_id}")
