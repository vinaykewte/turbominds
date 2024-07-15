import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar menu
with st.sidebar:
    selected = option_menu("Turbo Minds", ["Brief", 'Research', 'Strategy', 'Creative', 'Design'], 
        icons=['journal', 'search', 'calendar3-event', 'palette-fill', 'card-image'], menu_icon="fire",default_index=0)

# Define a function to load the appropriate page
def load_page(selected_option):
    if selected_option == "Brief":
        import page.Brief as page
    elif selected_option == "Research":
        import page.research as page
    elif selected_option == "Strategy":
        import page.strategy as page
    elif selected_option == "Creative":
        import page.creative as page
    elif selected_option == "Design":
        import page.design as page
    else:
        st.error("Page not found")
        return
    
    page.show()

# Call the function to load the selected page
load_page(selected)
