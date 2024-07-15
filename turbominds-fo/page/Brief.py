import os
import requests
import streamlit as st
from components.TopBar import top_bar_with_overlapping_images
from components import BriefGrid, ProgressBar, BriefResult
from load_dotenv import load_dotenv

load_dotenv()

def show_result():
    st.write(st.session_state.brief_id)

def show_brief_grid():
    form_data = BriefGrid.show()
    if form_data:
        # Make the API call with form data
        res = requests.post(f"{os.getenv('BACKEND_BASE_URL')}/brief", json=form_data)
        if res.status_code == 200:
            brief_id = res.json().get("brief_id")
            # Store the brief_id in session state
            st.session_state.brief_id = brief_id
            show_result()
            st.rerun()


def show_progress_bar(brief_id):
    st.empty()
    st.empty()
    st.empty()
    ProgressBar.show(brief_id)


def show():
#    st.set_page_config(page_title="Streamlit Grid Example", page_icon=":star:", layout="centered")
    top_bar_with_overlapping_images(
        [
            'https://img.freepik.com/free-photo/young-bearded-man-with-white-t-shirt_273609-6624.jpg',
            'https://img.freepik.com/premium-vector/portrait-indian-traditional-style-beautiful-girl-face-avatar-vector-illustration_55610-7346.jpg'
        ], 
        "Briefing Agents"
    )

    if 'brief_id' not in st.session_state:
        show_brief_grid()
    if 'brief_id' in st.session_state:
        show_progress_bar(st.session_state.brief_id)
    
        
    # elif st.session_state.brief_content and st.session_state.brief_result:
    #     BriefResult.show()

if __name__ == "__main__":
    show()
