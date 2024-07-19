import streamlit as st
from streamlit_quill import st_quill
import json
from state.brief_session import Brief_State
from state.session_state import get_brief_class

# Sample JSON array with questions
sources_json = """[
    {
        "id": "10b86364-e12e-4f0c-a01c-1f6f965b78f2",
        "title": "Artificial Intelligence in Healthcare",
        "description": "Exploring the application of AI technologies in healthcare, including diagnostics, treatment planning, and personalized medicine.",
        "url": "https://example.com/ai-healthcare"
    },
    {
        "id": "b5a1f7f2-d4d6-4b0d-a7f6-1c1a7f3a5b6c",
        "title": "Renewable Energy Storage Solutions",
        "description": "Investigating advanced energy storage technologies to support the integration of renewable energy sources into the grid.",
        "url": "https://example.com/renewable-energy-storage"
    },
    {
        "id": "c9e3b5a1-f2d4-4b0d-a7f6-1c1a7f3a5b6c",
        "title": "Quantum Computing and Cryptography",
        "description": "Examining the potential impact of quantum computing on cryptography and the development of post-quantum secure communication protocols.",
        "url": "https://example.com/quantum-computing-cryptography"
    },
    {
        "id": "d4d6b5a1-f2d4-4b0d-a7f6-1c1a7f3a5b6c",
        "title": "Neuroscience and Machine Learning",
        "description": "Exploring the intersection of neuroscience and machine learning, including the development of brain-inspired AI algorithms and neural interfaces.",
        "url": "https://example.com/neuroscience-machine-learning"
    },
    {
        "id": "e12ef7f2-d4d6-4b0d-a7f6-1c1a7f3a5b6c",
        "title": "Sustainable Urban Planning and Design",
        "description": "Investigating innovative approaches to urban planning and design that prioritize sustainability, livability, and resilience.",
        "url": "https://example.com/sustainable-urban-planning"
    }
]"""

sources = json.loads(sources_json)


def show(result):
    col1, col2 = st.columns([3, 1])  # Create two columns with ratio 3:1

    with col1:
        content = st_quill(value=result["final_brief"])
        if st.button("Add to Brief"):
            # brief_class = get_brief_class()
            Brief_State.update_research_result(result)
            Brief_State.add_to_brief(result['final_brief'])
            # brief_class.update_research_result(result)
    
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
        for source in sources:
          st.markdown(f'<div class="question-box">{source["title"]}</div>', unsafe_allow_html=True)
          st.markdown(f'<div class="question-box">{source["description"]}</div>', unsafe_allow_html=True)
          st.markdown(f'<div class="question-box">{source["url"]}</div>', unsafe_allow_html=True)
          st.write('---')
          
if __name__ == "__main__":
    show()
