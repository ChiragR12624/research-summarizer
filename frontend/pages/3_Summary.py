import streamlit as st
from utils.api import get_summary

st.set_page_config(page_title="Summary", layout="wide")
st.title("📑 Paper Summary")

# ---------- Check upload ----------
if "paper_id" not in st.session_state:
    st.warning("Please upload a paper first.")
    st.stop()

paper_id = st.session_state.paper_id

# ---------- Tabs ----------
tabs = st.tabs([
    "One-liner",
    "Abstract",
    "Detailed",
    "Bullets",
    "Layman",
    "Section-wise"
])

summary_types = [
    "one_liner",
    "abstract",
    "detailed",
    "bullets",
    "layman",
    "section_wise"
]

for tab, summary_type in zip(tabs, summary_types):
    with tab:
        with st.spinner("Loading summary..."):
            content = get_summary(paper_id, summary_type)
        st.write(content)
