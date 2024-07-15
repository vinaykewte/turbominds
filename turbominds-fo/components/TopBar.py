# Define a component for the top bar with overlapping circles
import streamlit as st
# Define a component for the top bar with overlapping circles
def top_bar_with_overlapping_images(images, text):
    st.markdown(
        """
        <style>
        .top-bar {
            display: flex;
            align-items: center;
            padding: 10px;
            margin-bottom: 20px;
            background-color: #E8ECF9;
            border-radius: 10px;
        }
        .top-bar .circle {
            position: relative;
            display: inline-block;
            width: 40px; /* Adjust size as needed */
            height: 40px; /* Adjust size as needed */
            border-radius: 50%;
            overflow: hidden;
            margin-right: -10px; /* Adjust overlap */
            border: 2px solid black;
        }
        .top-bar .circle img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .top-bar .text {
            flex: 1;
            margin-left: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="top-bar">
            {" ".join([f'<div class="circle"><img src="{image}" alt="Image"></div>' for image in images])}
            <div class="text">{text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
