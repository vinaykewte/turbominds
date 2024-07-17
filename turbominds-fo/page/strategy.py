# pages/brief.py
import streamlit as st
from state.session_state import get_brief_class

def show():
    brief_state = get_brief_class()

    st.title("Creative Page")
    st.write("This is the Brief page.")
    st.write(brief_state.get_brief_info())

    if st.button("Update Brief Strategy Results"):
        brief_state.update_strategy_result({
            'name': 'John Doe',
            'description': 'A creative strategy for the project'
        })



