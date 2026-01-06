# backend/app/nlp/topic_classifier.py

from transformers import AutoTokenizer, AutoModel
from functools import lru_cache
import torch

_MODEL_NAME = "allenai/scibert_scivocab_uncased"

tokenizer = AutoTokenizer.from_pretrained(_MODEL_NAME)
model = AutoModel.from_pretrained(_MODEL_NAME)
model.eval()

TOPIC_KEYWORDS = {
    "Machine Learning": ["learning", "neural", "model"],
    "Natural Language Processing": ["language", "text", "nlp"],
    "Computer Vision": ["image", "vision", "cnn"],
    "Healthcare AI": ["medical", "clinical", "patient"],
    "Robotics": ["robot", "control", "sensor"],
}

def classify_topic(text: str):
    text_lower = text.lower()
    matched = [
        topic for topic, kws in TOPIC_KEYWORDS.items()
        if any(kw in text_lower for kw in kws)
    ]
    return matched if matched else ["Other"]

@lru_cache(maxsize=128)
def get_scibert_embedding(text: str):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)
