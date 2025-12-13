import requests
from pathlib import Path

# Where PDFs will be stored
SAVE_DIR = Path("data/papers")
SAVE_DIR.mkdir(parents=True, exist_ok=True)

# Open-access research paper PDFs (arXiv)
PDF_URLS = {
    "llm_survey.pdf": "https://arxiv.org/pdf/2303.18223.pdf",
    "deep_learning_overview.pdf": "https://arxiv.org/pdf/2001.08361.pdf",
    "ml_healthcare.pdf": "https://arxiv.org/pdf/1904.02677.pdf",
}

def download_pdf(name, url):
    print(f"Downloading {name} ...")
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    file_path = SAVE_DIR / name
    with open(file_path, "wb") as f:
        f.write(response.content)

    print(f"Saved to {file_path}")

if __name__ == "__main__":
    for name, url in PDF_URLS.items():
        download_pdf(name, url)

    print("\n✅ All PDFs downloaded successfully")
