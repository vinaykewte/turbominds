import os
import time
import requests
import streamlit as st
from components.TopBar import top_bar_with_overlapping_images
from components import BriefGrid, ProgressBar, BriefResult
from load_dotenv import load_dotenv

load_dotenv()

agents = [
    {
        "id": 1,
        "name": "Ananya",
        "role": "Requirements Analyst",
        "image_url": "https://img.freepik.com/free-photo/close-up-portrait-cheerful-glamour-girl-with-cute-make-up-smiling-white-teeth-looking-happy-camera-standing-blue-background_1258-70300.jpg",
        "text": "Ananya is analyzing the initial client requirements, identifying any ambiguities, and compiling all available information."
    },
    {
        "id": 2,
        "name": "Rajesh",
        "role": "Gap Analyst Agent",
        "image_url": "https://img.freepik.com/free-photo/young-bearded-man-with-white-t-shirt_273609-6624.jpg",
        "text": "Rajesh is decoding the gathered information, pinpointing specific gaps, and formulating internal questions to clarify the client's needs."
    },
    {
        "id": 3,
        "name": "Meera",
        "role": "Project Insights Analyst",
        "image_url": "https://img.freepik.com/free-photo/joyful-young-woman-wearing-black-undershirt-white-wall_141793-26677.jpg",
        "text": "Meera is reviewing past similar projects and using predefined guidelines to fill in the gaps and assumptions based on industry standards and client history."
    },
    {
        "id": 4,
        "name": "Vikram",
        "role": "Documentation Specialist",
        "image_url": "https://img.freepik.com/free-photo/portrait-male-tourist-visiting-great-wall-china_23-2151261922.jpg",
        "text": "Vikram finalizing the refined brief, organizing the clarified requirements into a detailed, comprehensive document that can be easily understood by the project team."
    },
]

# Function to show progress bar and poll API
def show_progress_bar(brief_id):
    ProgressBar.show(agents, "Brief")
    st.empty()
    st.empty()
    st.empty()
    if st.button("<- Back"): # back button
        brief_id = None
        show_brief_grid()
    backend_base_url = os.getenv('BACKEND_BASE_URL')
    response = requests.get(f"{backend_base_url}/brief/{brief_id}")
    if response.status_code == 200:
        data = response.json()
        status = data.get("status")
        results = data.get("results", {})
        
        if status == "COMPLETED":
            st.info("Successfully")
            if results:
                st.session_state.results = results
                st.write(st.session_state)
                st.rerun()
            else:
                st.error("An error occurred. No data found.")

    else:
        st.error(f"Error fetching data: {response}")
            

# Function to show the brief grid
def show_brief_grid():
    form_data = BriefGrid.show()
    if form_data:
        # Make the API call with form data
        res = requests.post(f"{os.getenv('BACKEND_BASE_URL')}/brief", json=form_data)
        if res.status_code == 200:
            brief_id = res.json().get("brief_id")
            # Store the brief_id in session state
            st.session_state.brief_id = brief_id
            st.rerun()

# Main function to control the flow of the application
def show():
    top_bar_with_overlapping_images(
        agents, 
        "Briefing Agents"
    )
    if 'brief_id' not in st.session_state and 'results' not in st.session_state:
        show_brief_grid()
    if 'brief_id' in st.session_state and 'results' not in st.session_state:
        show_progress_bar(st.session_state.brief_id)
    if 'results' in st.session_state:
        BriefResult.show(st.session_state.results)

if __name__ == "__main__":
    show()
