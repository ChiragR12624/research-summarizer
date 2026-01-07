import json
from pathlib import Path
from metrics import compute_rouge, compute_bleu, compute_bertscore

PROCESSED_DIR = Path("data/processed")


def extract_abstract(processed_json):
    if "sections" in processed_json and "abstract" in processed_json["sections"]:
        return processed_json["sections"]["abstract"]
    if "abstract_text" in processed_json:
        return processed_json["abstract_text"]
    if "abstract" in processed_json and isinstance(processed_json["abstract"], str):
        return processed_json["abstract"]
    raise KeyError("Abstract not found")


def run_evaluation(summary_dir, output_file):
    summary_dir = Path(summary_dir)
    results = []

    for processed_file in PROCESSED_DIR.glob("*.json"):
        paper_id = processed_file.stem
        summary_file = summary_dir / f"{paper_id}.json"

        if not summary_file.exists():
            continue

        processed = json.load(open(processed_file))
        summary = json.load(open(summary_file))

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

    Path(output_file).parent.mkdir(exist_ok=True)
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)

    print(f"✅ Evaluation saved to {output_file}")


if __name__ == "__main__":
    run_evaluation("data/summaries_flan_t5", "evaluation/results_flan_t5.json")
    run_evaluation("data/summaries_llama", "evaluation/results_llama.json")
