import os
import time
import requests
import streamlit as st
from components.TopBar import top_bar_with_overlapping_images
from components.Strategy import StrategyGrid, StrategyResult
from components import ProgressBar
from load_dotenv import load_dotenv

load_dotenv()

agents = [
    {
        "id": 1,
        "name": "Aisha",
        "role": "Strategic Insights Analyst",
        "image_url": "https://img.freepik.com/free-photo/portrait-happy-young-woman-wearing-casual-tshirt-waving-hands-isolated-pink-background_1150-63284.jpg",
        "text": "Aisha is reviewing market research and consumer data, identifying key trends and insights."
        },
    {
        "id": 2,
        "name": "Arjun",
        "role": "Campaign Strategist",
        "image_url": "https://img.freepik.com/free-photo/young-smiling-man-bearded-businessman-pointing-with-two-finger-upward_171337-9572.jpg",
        "text": "Arjun is developing a plan that outlines key objectives, messaging themes, and the channels to be used for the campaign."
    },
    {
        "id": 3,
        "name": "Kavya",
        "role": "Tactical Planner",
        "image_url": "https://img.freepik.com/free-photo/impressed-young-pretty-caucasian-girl-sun-glasses-pointing-side-olive-green_141793-93194.jpg",
        "text": "Kavya is focusing on the tactical aspects, determining the timing, budget, and tools required for the execution of the strategy."
    },
    {
        "id": 4,
        "name": "Sameer",
        "role": "Campaign Integration Specialist",
        "image_url": "https://img.freepik.com/free-photo/smiling-young-bald-call-center-man-putting-fingers-temples-isolated-crimson-wall_141793-94385.jpg",
        "text": "Sameer is integrating all insights and plans, finalizing the comprehensive campaign strategy to ensure alignment with overall business goals and objectives."
    },
]

# Function to show progress bar and poll API
def show_progress_bar(strategy_id):
    backend_base_url = os.getenv('BACKEND_BASE_URL')
    st.empty()
    st.empty()
    st.empty()
    ProgressBar.show(agents, "Strategy")
    response = requests.get(f"{backend_base_url}/strategy/{strategy_id}")
    if response.status_code == 200:
        data = response.json()
        status = data.get("status")
        results = data.get("results", {})
        
        if status == "COMPLETED":
            st.info("Successfully")
            if results:
                st.session_state.strategy_results = results
                st.rerun()
            else:
                st.error("An error occurred. No data found.")

    else:
        st.error(f"Error fetching data: {response}")

# Function to show the brief grid
def show_strategy_grid():
    form_data = StrategyGrid.show()
    if form_data:
        # Make the API call with form data
        res = requests.post(f"{os.getenv('BACKEND_BASE_URL')}/strategy", json=form_data)
        if res.status_code == 200:
            strategy_id = res.json().get("strategy_id")
            st.session_state.strategy_id = strategy_id
            # Store the brief_id in session state
            st.rerun()

# Main function to control the flow of the application
def show():
    top_bar_with_overlapping_images(
        agents, 
        "Strategy Agents"
    )
    if 'strategy_id' not in st.session_state and 'strategy_results' not in st.session_state:
        show_strategy_grid()
    if 'strategy_id' in st.session_state and 'strategy_results' not in st.session_state:
        show_progress_bar(st.session_state.strategy_id)
    if 'strategy_results' in st.session_state:
        StrategyResult.show(st.session_state.strategy_results)

if __name__ == "__main__":
    show()
