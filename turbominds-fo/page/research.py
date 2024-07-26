import os
import time
import requests
import streamlit as st
from components.TopBar import top_bar_with_overlapping_images
from components.Research import ResearchGrid, ResearchResult
from components import ProgressBar
from load_dotenv import load_dotenv

load_dotenv()

agents = [
    {
        "id": 1,
        "name": "Aarav",
        "role": "Market Research Analyst",
        "image_url": "https://img.freepik.com/free-photo/young-bearded-man-with-striped-shirt_273609-5677.jpg",
        "text": "Aarav is gathering primary and secondary research data from various sources to understand market trends and consumer behavior."
        },
    {
        "id": 2,
        "name": "Nisha",
        "role": "Data Analyst",
        "image_url": "https://img.freepik.com/premium-photo/young-beautiful-woman-teacher-posing-with-gesture_1258-12099.jpg",
        "text": "Nisha is analysing collected data, identifying key insights and determining potential opportunities and threats."
    },
    {
        "id": 3,
        "name": "Rohan",
        "role": "Data Visualization Specialist",
        "image_url": "https://img.freepik.com/free-photo/headshot-attractive-mixed-race-male-student-with-stubble-tousled-hair-biting-his-lower-lip_273609-14035.jpg",
        "text": "Rohan is developing comprehensive reports that summarise the findings, including graphs, charts and other visual aids to present the data effectively."
    },
    {
        "id": 4,
        "name": "Priya",
        "role": "Documentation Specialist",
        "image_url": "https://img.freepik.com/free-photo/cheerful-curly-business-girl-wearing-glasses_176420-206.jpg",
        "text": "Priya reviewing the reports, validating the data and ensuring all insights are aligned with the overall project objectives before sharing with other teams."
    },
]

# Function to show progress bar and poll API
def show_progress_bar(research_id):
    backend_base_url = os.getenv('BACKEND_BASE_URL')
    st.empty()
    st.empty()
    st.empty()
    ProgressBar.show(agents, "Research")
    response = requests.get(f"{backend_base_url}/research/{research_id}")
    if response.status_code == 200:
        data = response.json()
        status = data.get("status")
        results = data.get("results", {})
        
        if status == "COMPLETED":
            st.info("Successfully")
            if results:
                st.session_state.research_results = results
                st.rerun()
            else:
                st.error("An error occurred. No data found.")

    else:
        st.error(f"Error fetching data: {response}")
# Function to show the brief grid
def show_research_grid():
    form_data = ResearchGrid.show()
    if form_data:
        # Make the API call with form data
        res = requests.post(f"{os.getenv('BACKEND_BASE_URL')}/research", json=form_data)
        if res.status_code == 200:
            research_id = res.json().get("research_id")
            st.session_state.research_id = research_id
            st.rerun()

# Main function to control the flow of the application
def show():
    top_bar_with_overlapping_images(
        agents, 
        "Research Agents"
    )

    if 'research_id' not in st.session_state and 'research_results' not in st.session_state:
        show_research_grid()
    if 'research_id' in st.session_state and 'research_results' not in st.session_state:
        show_progress_bar(st.session_state.research_id)
    if 'research_results' in st.session_state:
        ResearchResult.show(st.session_state.research_results)

if __name__ == "__main__":
    show()
