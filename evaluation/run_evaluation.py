import json
from pathlib import Path
from metrics import compute_rouge, compute_bleu, compute_bertscore

PROCESSED_DIR = Path("data/processed")
SUMMARIES_DIR = Path("data/summaries")
OUTPUT_FILE = Path("evaluation/results.json")


def extract_abstract(processed_json):
    """
    Safely extract abstract from different processed JSON schemas.
    """
    # Case 1: sections -> abstract
    if "sections" in processed_json and "abstract" in processed_json["sections"]:
        return processed_json["sections"]["abstract"]

    # Case 2: flat abstract_text
    if "abstract_text" in processed_json:
        return processed_json["abstract_text"]

    # Case 3: direct abstract string
    if "abstract" in processed_json and isinstance(processed_json["abstract"], str):
        return processed_json["abstract"]

    raise KeyError("Abstract not found in processed JSON")


results = []

for processed_file in PROCESSED_DIR.glob("*.json"):
    paper_id = processed_file.stem
    summary_file = SUMMARIES_DIR / f"{paper_id}.json"

    if not summary_file.exists():
        continue

    with open(processed_file) as f:
        processed = json.load(f)

    with open(summary_file) as f:
        summary = json.load(f)

    try:
        reference = extract_abstract(processed)
        prediction = summary.get("abstract_summary")

        if not prediction:
            raise KeyError("abstract_summary missing")

        scores = {
            "paper_id": paper_id,
            "rouge": compute_rouge(reference, prediction),
            "bleu": compute_bleu(reference, prediction),
            "bertscore": compute_bertscore(reference, prediction),
        }

        results.append(scores)

    except Exception as e:
        print(f"⚠️ Skipping {paper_id}: {e}")

# Ensure output folder exists
OUTPUT_FILE.parent.mkdir(exist_ok=True)

with open(OUTPUT_FILE, "w") as f:
    json.dump(results, f, indent=2)

print("✅ Evaluation completed successfully")
