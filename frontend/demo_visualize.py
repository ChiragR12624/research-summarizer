import requests
import networkx as nx
import matplotlib.pyplot as plt

payload = {
    "text": open("sample_paper.txt").read(),
    "abstract": "This paper proposes a transformer-based NLP system.",
    "sections": [
        "Introduction",
        "Related Work",
        "Methodology",
        "Experiments",
        "Conclusion"
    ],
    "corpus_abstracts": [
        "We propose a transformer architecture.",
        "CNN based approaches for vision tasks."
    ]
}

res = requests.post(
    "http://127.0.0.1:8000/analyze-paper",
    json=payload
)

data = res.json()

# ---- Graph ----
G = nx.DiGraph()
G.add_edges_from(data["section_graph"]["edges"])

nx.draw(G, with_labels=True, node_size=3000)
plt.title(f"Novelty Score: {data['novelty_score']}")
plt.show()

# ---- Print gaps ----
print("\n🔍 Research Gaps:")
for g in data["research_gaps"]["gap_sentences"]:
    print("-", g)
