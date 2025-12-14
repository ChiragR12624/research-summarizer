from transformers import pipeline


class Summarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.pipe = pipeline(
            "summarization",
            model=model_name
        )

    def summarize(self, text, max_length=150, min_length=40):
        if not text.strip():
            return ""

        output = self.pipe(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )
        return output[0]["summary_text"]
