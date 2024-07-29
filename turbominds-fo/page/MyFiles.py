import streamlit as st
from datetime import datetime
from streamlit_quill import st_quill
from state.session_state import get_brief_class
from state.brief_session import Brief_State


brief_class = get_brief_class()
# Define the sections
section_1 = "Current File"
section_2 = "List of Files"

# Create a default section
default_section = section_1

# State management for the active section
if "active_section" not in st.session_state:
    st.session_state.active_section = default_section

def display_content_section():
    st.header("My Files")
    display_brief_content()

def display_brief_content():
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

def display_item_list_section(): # here we require to add the state management section, so that we will be having the recurrent brief for the concurrent title.
    st.header("Item List Section")
    items = [
        {"name": "Item 1", "date_updated": datetime(2024, 1, 1), "content": "Details of Item 1"},
        {"name": "Item 2", "date_updated": datetime(2024, 2, 15), "content": "Details of Item 2"},
        {"name": "Item 3", "date_updated": datetime(2024, 3, 10), "content": "Details of Item 3"},
    ]

    item_names = [item["name"] for item in items]
    selected_item_name = st.selectbox("Select an item to view details:", item_names)

    selected_item = next(item for item in items if item["name"] == selected_item_name)
    st.write(f"**Name:** {selected_item['name']}")
    st.write(f"**Date Updated:** {selected_item['date_updated'].strftime('%Y-%m-%d')}")
    st.write(f"**Content:** {selected_item['content']}")
    st.write("---")

def show():
    col1, col2 = st.columns(2)
    with col1:
        if st.button(section_1):
            st.session_state.active_section = section_1
    with col2:
        if st.button(section_2):
            st.session_state.active_section = section_2
    if st.session_state.active_section == section_1:
        display_content_section()
    elif st.session_state.active_section == section_2:
        display_item_list_section()

    st.info("Use the buttons above to navigate between sections.")

if __name__ == "__main__":
    show()