import streamlit as st
from streamlit_quill import st_quill
from state.session_state import get_brief_class
from state.brief_session import Brief_State

brief = get_brief_class
st.write(brief)
def show():
    # content = st_quill(value="")
    brief = get_brief_class
    st.write(brief)
    st.write(Brief_State.get_brief_info)
    st.write(Brief_State.get_final_brief)
    

if __name__ == "__main__":
    show()