import streamlit as st
from streamlit_quill import st_quill
from state.brief_session import Brief_State
from state.session_state import get_brief_class


def show(result):
    
    content = st_quill(value=result["final_brief"])
    if st.button("Add to Brief"):
        # brief_class = get_brief_class()
        # brief_class.add_to_brief(result['final_brief'])
        # brief_class.update_strategy_result(result)
        Brief_State.update_research_result(result)
        Brief_State.add_to_brief(result['final_brief'])

if __name__ == "__main__":
    show()
