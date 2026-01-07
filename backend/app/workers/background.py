from app.cache.sqlite_cache import CacheDB
from app.core.pdf_extract import extract_text
from app.core.chunker import chunk_text
from app.core.embeddings import embed_chunks
from app.core.summarizer import generate_summaries

def process_paper(paper_id: str, pdf_path: str):
    print(f"✅ Background processing started for paper_id={paper_id}")

    # 1️⃣ Extract text
    text = extract_text(pdf_path)
    print(f"📄 Extracted {len(text)} characters")

    # 2️⃣ Chunking
    chunks = chunk_text(text)
    print(f"🧩 Created {len(chunks)} text chunks")

    # 3️⃣ Embeddings
    embeddings = embed_chunks(chunks)
    print(f"🧠 Generated {len(embeddings)} embeddings")

    # 4️⃣ Summaries + insights (SINGLE CALL)
    summaries = generate_summaries(text)

    # 5️⃣ Store in cache (EXPECTED FORMAT)
    cache = CacheDB()
    cache.store_paper(paper_id, {
        "paper_id": paper_id,
        "text": text,
        "chunks": chunks,
        "embeddings": embeddings,
        "summaries": summaries,
        "status": "processed"
    })

    print(f"💾 Cached full pipeline output for paper_id={paper_id}")
