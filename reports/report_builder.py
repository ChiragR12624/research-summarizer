import json

def build_report(paper, summary, evaluation):
    return {
        "Title": paper["title"],
        "Abstract": paper["abstract"],
        "One-line Summary": summary["one_liner"],
        "Abstract Summary": summary["abstract_summary"],
        "Bullet Summary": "\n".join(summary["bullets"]),
        "Layman Summary": summary["layman"],
        "Keywords": ", ".join(summary["keywords"]),
        "Topics": ", ".join(summary["topics"]),
        "Research Gaps": "\n".join(summary["research_gaps"]),
        "Novelty Score": summary["novelty_score"],
        "Evaluation": evaluation
    }
