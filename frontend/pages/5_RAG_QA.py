import streamlit as st
from utils.api import rag_query
from utils.state import init_state

init_state()

st.set_page_config(page_title="RAG Q&A", layout="wide")
st.title("🤖 Ask Questions About the Paper")

if "paper_id" not in st.session_state or not st.session_state.paper_id:
    st.warning("Upload a paper first.")
    st.stop()

paper_id = st.session_state.paper_id

st.markdown(
    """
Ask natural language questions about the uploaded research paper.

Examples:
- What is this paper about?
- What problem does this paper solve?
- Explain the methodology.
- What is the research gap?
"""
)

question = st.text_input(
    "Enter your question",
    placeholder="What is this paper about?"
)

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Retrieving answer using RAG..."):
            answer, sources = rag_query(paper_id, question)

        st.subheader("📌 Answer")
        st.success(answer)

        if sources:
            with st.expander("📚 Source Chunks"):
                for i, src in enumerate(sources, 1):
                    st.markdown(f"**Source {i}:**")
                    st.write(src)
