import streamlit as st
from utils.api import upload_pdf

st.set_page_config(page_title="Upload Research Paper", layout="centered")

st.title("📄 Upload Research Paper (PDF)")

uploaded_file = st.file_uploader(
    "Drag and drop your research paper here",
    type=["pdf"]
)

if uploaded_file and st.button("Upload & Process"):
    with st.spinner("Uploading and processing PDF..."):
        response = upload_pdf(uploaded_file)

    # 🔐 SAFETY CHECK (IMPORTANT)
    if "paper_id" not in response:
        st.error("Upload failed: paper_id missing in backend response")
        st.json(response)
        st.stop()

    st.session_state.paper_id = response["paper_id"]

    st.success("✅ PDF uploaded successfully!")
    st.info(f"Paper ID: {st.session_state.paper_id}")

    st.markdown("👉 Go to **Summary** page to view results")
