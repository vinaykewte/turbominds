import streamlit as st
from streamlit_option_menu import option_menu

# Initialize session state for selected page if it doesn't exist
if "selected_page" not in st.session_state:
    st.session_state["selected_page"] = "Brief"

# Define menu options
menu_options = ["Brief", 'Research', 'Strategy', 'Design', 'My File']

# Sidebar menu
with st.sidebar:
    selected = option_menu("Turbo Minds", menu_options, 
        icons=['journal', 'search', 'calendar3-event', 'card-image', 'file-earmark-text'], 
        menu_icon="fire", 
        default_index=menu_options.index(st.session_state["selected_page"]),
        key="menu",
        styles={
            "container": {"padding": "0!important", "background-color": "#F0F2F6"},
            "nav-link-selected": {"background-color": "#800000", "color": "white"},
        })

# Update selected_page in session state based on menu selection
st.session_state["selected_page"] = selected

# Define a function to load the appropriate page
def load_page(selected_option):
    if selected_option == "Brief":
        import page.Brief as page
    elif selected_option == "Research":
        import page.Research as page
    elif selected_option == "Strategy":
        import page.Strategy as page
    elif selected_option == "Design":
        import page.Design as page
    elif selected_option == "My File":
        import page.MyFiles as page
    else:
        st.error("Page not found")
        return
    
    page.show()

def navigate_to(page):
    st.session_state["selected_page"] = page
    st.experimental_rerun()

# Call the function to load the selected page
load_page(st.session_state["selected_page"])
