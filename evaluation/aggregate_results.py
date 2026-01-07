import json
from statistics import mean

def aggregate(path):
    data = json.load(open(path))

    if not data:
        return {
            "rouge1": None,
            "rouge2": None,
            "rougeL": None,
            "bleu": None,
            "note": "No valid papers evaluated"
        }

    return {
        "rouge1": mean([d["rouge"]["rouge1"] for d in data]),
        "rouge2": mean([d["rouge"]["rouge2"] for d in data]),
        "rougeL": mean([d["rouge"]["rougeL"] for d in data]),
        "bleu": mean([d["bleu"] for d in data]),
    }

results = {
    "Flan-T5": aggregate("evaluation/results_flan_t5.json"),
    "LLaMA": aggregate("evaluation/results_llama.json"),
}

with open("evaluation/benchmark_summary.json", "w") as f:
    json.dump(results, f, indent=2)

print("✅ Benchmark summary created")
