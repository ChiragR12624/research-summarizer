from transformers import pipeline

# Load summarization model ONCE
summarizer = pipeline(
    task="summarization",
    model="facebook/bart-large-cnn"
)

def call_llm(text: str) -> str:
    """
    Summarize text using a local Hugging Face model
    """
    summary = summarizer(
        text,
        max_length=180,
        min_length=60,
        do_sample=False
    )
    return summary[0]["summary_text"]
