import sys
import os
import json
from pathlib import Path

# Add project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.extract_text import extract_text_from_pdf
from src.clean_text import clean_text, split_into_sections

# Input and output directories
PDF_DIR = Path("data/papers")
OUTPUT_DIR = Path("data/processed")

# Create output directory if it doesn't exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Process each PDF
for pdf in PDF_DIR.glob("*.pdf"):
    print(f"\n📄 Processing: {pdf.name}")

    # Step 1: Extract
    text = extract_text_from_pdf(str(pdf))

    # Step 2: Clean
    cleaned = clean_text(text)

    # Step 3: Split into sections
    sections = split_into_sections(cleaned)

    # Step 4: Save as JSON
    out_file = OUTPUT_DIR / f"{pdf.stem}.json"
    with open(out_file, "w") as f:
        json.dump(sections, f, indent=2)

    print(f"✅ Saved {out_file}")
    print(f"🧩 Sections detected: {list(sections.keys())}")
