import streamlit as st

def init_state():
    if "paper_id" not in st.session_state:
        st.session_state.paper_id = None
