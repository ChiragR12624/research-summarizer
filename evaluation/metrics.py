"""
Evaluation metrics for research summarization.

NOTE:
- ROUGE and BLEU are always computed.
- BERTScore is computed ONLY if environment supports it.
- On Python 3.13, BERTScore + matplotlib may fail → handled safely.
"""

from rouge_score import rouge_scorer
import sacrebleu

# ---------------------------
# ROUGE
# ---------------------------

def compute_rouge(reference: str, prediction: str) -> dict:
    scorer = rouge_scorer.RougeScorer(
        ["rouge1", "rouge2", "rougeL"], use_stemmer=True
    )
    scores = scorer.score(reference, prediction)

    return {
        "rouge1": scores["rouge1"].fmeasure,
        "rouge2": scores["rouge2"].fmeasure,
        "rougeL": scores["rougeL"].fmeasure,
    }

# ---------------------------
# BLEU
# ---------------------------

def compute_bleu(reference: str, prediction: str) -> float:
    return sacrebleu.sentence_bleu(prediction, [reference]).score

# ---------------------------
# BERTScore (SAFE FALLBACK)
# ---------------------------

def compute_bertscore(reference: str, prediction: str):
    """
    Attempts to compute BERTScore.
    If environment breaks (Python 3.13 issue), returns None.
    """
    try:
        from bert_score import score as bert_score

        P, R, F1 = bert_score(
            [prediction],
            [reference],
            lang="en",
            rescale_with_baseline=True,
            verbose=False
        )
        return float(F1[0])

    except Exception as e:
        print("⚠️  BERTScore skipped due to environment issue:", str(e))
        return None
