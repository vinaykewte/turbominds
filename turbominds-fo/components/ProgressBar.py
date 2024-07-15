import streamlit as st
import time

agents = [
    {
        "id": 1,
        "name": "Vivek",
        "role": "Business Analyst Agent",
        "image_url": "https://img.freepik.com/free-photo/young-bearded-man-with-white-t-shirt_273609-6624.jpg",
        "text": "Vivek is analyzing the initial client requirements, identifying any ambiguities, and compiling all available information."
    },
    {
        "id": 2,
        "name": "Ayesha",
        "role": "Gap Analyst Agent",
        "image_url": "https://img.freepik.com/premium-vector/portrait-indian-traditional-style-beautiful-girl-face-avatar-vector-illustration_55610-7346.jpg",
        "text": "Ayesha is decoding the gathered information, pinpointing specific gaps, and formulating internal questions to clarify the client's needs."
    }
]

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
                width: 80px; /* Adjust size as needed */
                height: 80px; /* Adjust size as needed */
            }
            .rounded-rectangle .text {
                flex: 1;
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

def show(brief_id):
    st.title("Processing Brief")
    progress = st.progress(0)
    
    # Define the total steps
    total_steps = 200
    agent_display_intervals = total_steps // len(agents)
    
    for i in range(total_steps):
        # Update progress bar
        progress.progress(i / (total_steps - 1))
        
        # Interleave the display of agents
        if i % agent_display_intervals == 0 and i // agent_display_intervals < len(agents):
            agent_index = i // agent_display_intervals
            # st.write(f"Agent: {agents[agent_index]['image_url']}")
            rounded_rectangle(agents[agent_index]["image_url"], agents[agent_index]["text"])
        
        time.sleep(0.05)
    
    st.success("Process completed!")