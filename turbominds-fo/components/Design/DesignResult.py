import streamlit as st
from state.session_state import get_brief_class

def show():
    st.image(st.session_state.image, caption="Generated Image", use_column_width=True)
    brief_class = get_brief_class()
    _col1, _col2 = st.columns([3, 1])
    with _col1:
        st.write(brief_class.title)
    with _col2:
        if st.button("Add to Brief"):
            brief_class.update_design_result(st.session_state.image)
            st.session_state["selected_page"] = "My File"
            st.experimental_rerun()
    

if __name__ == "__main__":
    show()
