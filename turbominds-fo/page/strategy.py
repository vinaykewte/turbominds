import os
import time
import requests
import streamlit as st
from components.TopBar import top_bar_with_overlapping_images
from components.Strategy import StrategyGrid, StrategyResult
from components import ProgressBar
from load_dotenv import load_dotenv

load_dotenv()

# Function to show progress bar and poll API
def show_progress_bar(strategy_id):
    backend_base_url = os.getenv('BACKEND_BASE_URL')
    polling_interval = int(os.getenv('POLLING_INTERVAL', 1))  # default to 1 second
    timeout_duration = int(os.getenv('TIMEOUT_DURATION', 30))  # default to 30 seconds
    
    start_time = time.time()
    
    st.empty()
    st.empty()
    st.empty()
    with st.spinner("Processing..."):
        while True:
            # Check if timeout duration is reached
            if time.time() - start_time > timeout_duration:
                st.error("Timeout reached. Please try again later.")
                break
            
            # Poll the API
            response = requests.get(f"{backend_base_url}/strategy/{strategy_id}")
            if response.status_code == 200:
                data = response.json()
                status = data.get("status")
                results = data.get("results", {})
                
                if status == "COMPLETE":
                    if results:
                        StrategyResult.show(results)
                    else:
                        st.error("An error occurred. No data found.")
                    break
            else:
                st.error(f"Error fetching data: {response}")
            
            time.sleep(polling_interval)

# Function to show the brief grid
def show_brief_grid():
    form_data = StrategyGrid.show()
    if form_data:
        # Make the API call with form data
        res = requests.post(f"{os.getenv('BACKEND_BASE_URL')}/Strategy", json=form_data)
        if res.status_code == 200:
            # research_id = res.json().get("research_id")
            # Store the brief_id in session state
            st.rerun()

# Main function to control the flow of the application
def show():
    top_bar_with_overlapping_images(
        [
            'https://img.freepik.com/free-photo/young-bearded-man-with-white-t-shirt_273609-6624.jpg',
            'https://img.freepik.com/premium-vector/portrait-indian-traditional-style-beautiful-girl-face-avatar-vector-illustration_55610-7346.jpg'
        ], 
        "Strategy Agents"
    )

    if 'strategy_id' not in st.session_state:
        StrategyGrid.show()
    if 'strategy_id' in st.session_state:
        show_progress_bar(st.session_state.strategy_id)

if __name__ == "__main__":
    show()
