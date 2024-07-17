# pages/brief.py
import streamlit as st
from state.session_state import get_brief_class

def show():
    brief_state = get_brief_class()

    st.title("Creative Page")
    st.write("This is the Brief page.")
    st.write(brief_state)
