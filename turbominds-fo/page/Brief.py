import os
import asyncio
import time
import aiohttp
import requests
import streamlit as st
from components.TopBar import top_bar_with_overlapping_images
from components import BriefGrid, ProgressBar, BriefResult
from dotenv import load_dotenv

load_dotenv()

# Asynchronous function to show progress bar and poll API
async def show_progress_bar(brief_id):
    backend_base_url = os.getenv('BACKEND_BASE_URL')
    polling_interval = int(os.getenv('POLLING_INTERVAL', 1))  # default to 1 second
    timeout_duration = int(os.getenv('TIMEOUT_DURATION', 30))  # default to 30 seconds
    
    # Show the progress bar
    st.empty()
    st.empty()
    st.empty()
    asyncio.create_task(ProgressBar.show(brief_id))

    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        while True:
            # Check if timeout duration is reached
            if time.time() - start_time > timeout_duration:
                st.error("Timeout reached. Please try again later.")
                break
            
            # Poll the API
            async with session.get(f"{backend_base_url}/brief/{brief_id}") as response:
                if response.status == 200:
                    data = await response.json()
                    status = data.get("status")
                    result = data.get("result", {})
                    
                    if status == "COMPLETED":
                        if result:
                            BriefResult.show(result)
                        else:
                            st.error("An error occurred. No data found.")
                        break
                else:
                    st.error(f"Error fetching data: {response.status}")
            
            await asyncio.sleep(polling_interval)

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
            st.experimental_rerun()

# Main function to control the flow of the application
def show():
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
        asyncio.run(show_progress_bar(st.session_state.brief_id))

if __name__ == "__main__":
    show()
