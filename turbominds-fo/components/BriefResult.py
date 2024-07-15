import streamlit as st
from streamlit_quill import st_quill
import json

# Sample JSON array with questions
questions_list = [
      {
        "id": "10b86364-e12e-4f0c-a01c-1f6f965b78f2",
        "question": "What specific features or benefits of the AST DOCKS jeans should be highlighted in the campaign?",
        "topic": "Requirement"
      },
      {
        "id": "586e5a8c-f99d-42e0-a6b7-f3caf130d2bb",
        "question": "Could you provide more details about the key messages and creative direction for the AST DOCKS campaign?",
        "topic": "Campaign Overview"
      },
      {
        "id": "6e2f2a1a-6e25-4e5c-a7d2-b2a2f0a8c69d",
        "question": "What are the specific metrics and targets set for the campaign, in terms of sales, leads, or brand awareness?",
        "topic": "Campaign Goals"
      },
      {
        "id": "6fec2a3a-6b5e-4b21-a801-8b76b541d21a",
        "question": "Are there any specific demographics, psychographics, or behavioral traits that define the target audience of aspiring astronauts?",
        "topic": "Target Audience"
      },
      {
        "id": "4e20660a-e448-4871-a3c0-b9d76b3d1e1f",
        "question": "What key performance indicators (KPIs) will be used to measure the success of the AST DOCKS campaign?",
        "topic": "KPIs"
      },
      {
        "id": "9d2e5c2c-46e0-478c-87f3-8e3e10e12d6f",
        "question": "What is the allocated budget for the AST DOCKS campaign, and how will it be distributed across different channels and activities?",
        "topic": "Budget"
      },
      {
        "id": "56ad5d21-b6a2-4d5a-a3f5-97e8e352d2f0",
        "question": "What is the timeline for the AST DOCKS campaign, including the start and end dates, as well as milestones and deadlines?",
        "topic": "Timeline"
      }
    ]


def show():
    col1, col2 = st.columns([3, 1])  # Create two columns with ratio 3:1

    with col1:
        content = st_quill(value="<b>Streamlit</b> is **really** ***cool***.")
    
    with col2:
        st.markdown(
            """
            <style>
            .question-box {
                background-color: #f0f0f0;
                padding: 10px;
                margin-bottom: 10px;
                border-radius: 5px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        for q in questions_list:
            st.markdown(f'<div class="question-box">{q['question']}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    show()
