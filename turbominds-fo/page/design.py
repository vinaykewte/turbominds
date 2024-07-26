import os
import time
import requests
import streamlit as st
from components.Design import DesignGrid, DesignResult
from load_dotenv import load_dotenv
from PIL import Image
from io import BytesIO

load_dotenv()

# Function to show the brief grid
def show_brief_grid():
    form_data = DesignGrid.show()
    if form_data:
        st.session_state['is_context_submitted'] = True
        st.session_state.design_form_data = form_data
        st.rerun()
        
def show_spinner():
    st.empty()
    st.empty()
    st.empty()
    st.empty()
    with st.spinner('Fetching design...'):
        res = requests.post(f"{os.getenv('BACKEND_BASE_URL')}/design", json=st.session_state.design_form_data)
        if res.status_code == 200:
            image = Image.open(BytesIO(res.content))
            st.session_state['image'] = image
            st.rerun()
        else:
            st.error("Failed to fetch image from API")
            return None

# Main function to control the flow of the application
def show():
    if 'image' not in st.session_state and 'is_context_submitted' not in st.session_state:
        show_brief_grid()
    if 'image' not in st.session_state and 'is_context_submitted' in st.session_state:
        show_spinner()
    if 'image' in st.session_state and 'is_context_submitted' in st.session_state:
        DesignResult.show()

if __name__ == "__main__":
    show()
