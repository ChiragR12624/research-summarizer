import json
from pathlib import Path

# --------------------------------------------------
# Imports (all code is inside scripts/)
# --------------------------------------------------
from embeddings.embedder import Embedder
from vectorstore.faiss_store import FAISSStore
from summarizer.summarize import Summarizer
from summarizer.styles import SUMMARY_STYLES


def main():
    print("🚀 Starting summarization pipeline...")

    # Initialize components
    embedder = Embedder()
    store = FAISSStore()
    summarizer = Summarizer()

    # Ensure results directory exists
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    # Query to retrieve relevant chunks
    query = "machine learning research paper"
    query_embedding = embedder.embed([query])[0]

    retrieved_chunks = store.search(query_embedding, k=8)
    if not retrieved_chunks:
        print("❌ No chunks retrieved. Did you run indexing?")
        return

    # Build context safely (avoid token overflow)
    context = " ".join(chunk["text"] for chunk in retrieved_chunks)
    context = context[:3000]

    summaries = {}

    # Generate all summary styles
    for style, cfg in SUMMARY_STYLES.items():
        print(f"📝 Generating {style} summary...")
        summary = summarizer.summarize(
            context,
            max_length=cfg["max"],
            min_length=cfg["min"]
        )
        summaries[style] = summary

    # Save output
    output_path = results_dir / "sample_summaries.json"
    with open(output_path, "w") as f:
        json.dump(summaries, f, indent=2)

    print(f"\n✅ Summaries saved successfully at: {output_path}")


if __name__ == "__main__":
    main()
