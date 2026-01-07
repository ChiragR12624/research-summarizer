import streamlit as st
from utils.api import get_keywords, get_topics, get_research_gap
from utils.state import init_state

init_state()

st.set_page_config(page_title="Insights", layout="wide")
st.title("📊 Insights")

if "paper_id" not in st.session_state or not st.session_state.paper_id:
    st.warning("Upload a paper first.")
    st.stop()

paper_id = st.session_state.paper_id

# ---------- Keywords ----------
with st.spinner("Loading keywords..."):
    keywords = get_keywords(paper_id)

st.subheader("🔑 Keywords")
st.write(keywords)

# ---------- Topics ----------
with st.spinner("Loading topics..."):
    topics = get_topics(paper_id)

st.subheader("🧠 Topics")
st.write(topics)

# ---------- Research Gap ----------
with st.spinner("Loading research gap..."):
    gap = get_research_gap(paper_id)

st.subheader("🚧 Research Gap")
st.write(gap)
