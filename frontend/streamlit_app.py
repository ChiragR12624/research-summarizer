import streamlit as st
import requests

API_URL = st.secrets.get("api_url", "http://localhost:8000")

st.title("Research Paper Summarizer — Demo")

uploaded = st.file_uploader("Upload PDF", type=["pdf"])
if uploaded:
    if st.button("Upload to backend"):
        files = {"file": (uploaded.name, uploaded.getvalue(), "application/pdf")}
        resp = requests.post(f"{API_URL}/upload_paper", files=files)
        st.write(resp.json())
