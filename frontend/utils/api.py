import requests
import streamlit as st

BASE_URL = "http://localhost:8000"

# ---------------- Upload ----------------
def upload_pdf(file):
    try:
        files = {"file": file}
        response = requests.post(f"{BASE_URL}/upload_paper", files=files)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Upload failed: {e}")
        st.stop()


# ---------------- Summary Fetch (PER TYPE) ----------------
def get_summary(paper_id: str, summary_type: str):
    try:
        response = requests.get(
            f"{BASE_URL}/get_summary/{paper_id}/{summary_type}",
            timeout=120
        )

        if response.status_code != 200:
            st.error("Failed to fetch summary")
            st.text(response.text)
            st.stop()

        data = response.json()

        if "error" in data:
            st.warning(data["error"])
            st.stop()

        return data["content"]

    except requests.exceptions.ConnectionError:
        st.error("Backend not running")
        st.stop()


# ---------------- RAG Query ----------------
def rag_query(paper_id: str, question: str):
    try:
        response = requests.post(
            f"{BASE_URL}/rag_query",
            json={
                "paper_id": paper_id,
                "question": question
            },
            timeout=120
        )

        if response.status_code != 200:
            st.error("RAG query failed")
            st.text(response.text)
            st.stop()

        data = response.json()

        if "error" in data:
            st.warning(data["error"])
            st.stop()

        return data["answer"], data.get("sources", [])

    except requests.exceptions.ConnectionError:
        st.error("Backend not running")
        st.stop()

# ---------------- INSIGHTS ----------------

def get_keywords(paper_id: str):
    response = requests.get(f"{BASE_URL}/get_keywords/{paper_id}", timeout=60)
    data = response.json()
    if "error" in data:
        st.warning(data["error"])
        st.stop()
    return data["keywords"]


def get_topics(paper_id: str):
    response = requests.get(f"{BASE_URL}/get_topics/{paper_id}", timeout=60)
    data = response.json()
    if "error" in data:
        st.warning(data["error"])
        st.stop()
    return data["topics"]


def get_research_gap(paper_id: str):
    response = requests.get(f"{BASE_URL}/get_research_gap/{paper_id}", timeout=60)
    data = response.json()
    if "error" in data:
        st.warning(data["error"])
        st.stop()
    return data["research_gap"]
