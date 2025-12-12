from .pdf_extract import extract_text_from_pdf
def test_extract_sample():
    res = extract_text_from_pdf("backend/app/Users/chiragrgowda/Documents/LLM/IEEE_Format_LLM_Research_Paper_Summarizer.pdf")
    assert isinstance(res["text"], str)
    assert len(res["text"]) > 100
