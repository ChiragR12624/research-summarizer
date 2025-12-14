from .pdf_extract import extract_text_from_pdf
import sys

if __name__ == "__main__":
    path = sys.argv[1]
    out = extract_text_from_pdf(path)
    print("CHARACTERS:", len(out["text"]))
    print("FIRST 800 CHARS:")
    print(out["text"][:800])