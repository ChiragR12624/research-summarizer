import json

def fmt(value, decimals=2):
    """Format float safely; show N/A if None"""
    if value is None:
        return "N/A"
    return f"{value:.{decimals}f}"

data = json.load(open("evaluation/benchmark_summary.json"))

print("\nModel Comparison Results\n")
print(f"{'Model':<10} {'ROUGE-1':<10} {'ROUGE-2':<10} {'ROUGE-L':<10} {'BLEU':<10}")
print("-" * 55)

for model, scores in data.items():
    print(
        f"{model:<10} "
        f"{fmt(scores.get('rouge1')):<10} "
        f"{fmt(scores.get('rouge2')):<10} "
        f"{fmt(scores.get('rougeL')):<10} "
        f"{fmt(scores.get('bleu'), 1):<10}"
    )
