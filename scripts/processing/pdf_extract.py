import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file using PyMuPDF
    """
    text = []

    doc = fitz.open(pdf_path)
    for page in doc:
        page_text = page.get_text()
        if page_text:
            text.append(page_text)

    doc.close()
    return "\n".join(text)
