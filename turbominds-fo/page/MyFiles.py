import streamlit as st
from streamlit_quill import st_quill
from state.session_state import get_brief_class
from state.brief_session import Brief_State


brief_class = get_brief_class()

def show():
    if brief_class is None:
        #show no brief created yet with button to add one
        st.markdown("""
            <style>
                .centered {
                    text-align: center;
                }
                
            </style>
        """, unsafe_allow_html=True)
        st.markdown("<h1 class='centered'>Ready to take on the journey for your first autonomous brief creation?</h1>", unsafe_allow_html=True)
        st.markdown("<h4 class='centered'>Create your marketing brief by going to Brief tab</h4>", unsafe_allow_html=True)
        
    else:
        st.header(brief_class.title.title())
        st_quill(brief_class.final_brief)
        if 'image' in st.session_state:
            st.image(st.session_state.image, use_column_width=True)
    

if __name__ == "__main__":
    show()
    