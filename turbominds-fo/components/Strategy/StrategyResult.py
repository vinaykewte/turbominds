import streamlit as st
from streamlit_quill import st_quill
from state.session_state import get_brief_class


def show(result):
    content = st_quill(value=result["final_strategy"])
    brief_class = get_brief_class()
    _col1, _col2 = st.columns([3, 1])
    with _col1:
        st.write(brief_class.title)
    with _col2:
        if st.button("Add to Brief"):
            brief_class.add_to_brief(result['final_strategy'])
            brief_class.update_strategy_result(result)
            st.session_state["selected_page"] = "My File"
            st.experimental_rerun()

if __name__ == "__main__":
    show()
