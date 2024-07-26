import streamlit as st
import time

# Define a reusable component for rounded rectangles with image and text
def rounded_rectangle(image_url, text):
    # Container for the rounded rectangle
    with st.container():
        # CSS styling for the container
        st.markdown(
            """
            <style>
            .rounded-rectangle {
                display: flex;
                align-items: center;
                border: 2px solid black;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
            }
            .rounded-rectangle img {
                border-radius: 50%;
                margin-right: 10px;
                width: 50px; /* Adjust size as needed */
                height: 50px; /* Adjust size as needed */
            }
            .rounded-rectangle .text {
                flex: 1;
            }
            .progress-bar-container {
                width: 100%;
                background-color: #e0e0e0; /* Light grey background */
                border-radius: 10px;
                overflow: hidden;
            }
            .progress-bar {
                height: 10px;
                background-color: #00abb2; /* Red color */
                width: 0%; /* Initial width */
                transition: width 0.2s ease-in-out;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Content of the rounded rectangle
        st.markdown(
            f"""
            <div class="rounded-rectangle">
                <img src="{image_url}" alt="Image" />
                <div class="text">{text}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

def show(agents, category):
    st.title(f"Processing {category}")
    progress_bar_container = st.empty()
    
    # Define the total steps
    total_steps = 200
    agent_display_intervals = total_steps // (len(agents)*2)
    
    for i in range(total_steps):
        # Update progress bar
        progress_percentage = (i / (total_steps * 4 - 1)) * 100
        progress_bar_container.markdown(
            f"""
            <div class="progress-bar-container">
                <div class="progress-bar" style="width: {progress_percentage}%"></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        # Interleave the display of agents
        if i % agent_display_intervals == 0 and i // agent_display_intervals < len(agents):
            agent_index = i // agent_display_intervals
            rounded_rectangle(agents[agent_index]["image_url"], agents[agent_index]["text"])
        
        time.sleep(0.05)
