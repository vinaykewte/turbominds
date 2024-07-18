import streamlit as st
from streamlit_quill import st_quill
from state.session_state import get_brief_class
from streamlit_extras.stylable_container import stylable_container

def show(result):
    col1, col2 = st.columns([3, 1])  # Create two columns with ratio 3:1

    with col1:
        # Add custom CSS for rounded corners to the st_quill editor and right-aligned button
        st.markdown(
            """
            <style>
            .quill .ql-container {
                border-radius: 15px !important;
                border: 1px solid #ccc !important;
                padding: 10px !important;
                background-color: #f9f9f9 !important;
            }
            .button-container {
                display: flex;
                justify-content: flex-end;
                margin-top: 10px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        content = st_quill(value=result['final_brief'])

        # Add a right-aligned button
        # with stylable_container(
        #     key="Upload_Data",
        #     css_styles="""
        #     button{
        #         display: flex;
        #         justify-content: flex-end;
        #         width: 100%;
        #     }
        #     """
        # ):
        #     st.button("Upload Data")

        if st.button("Add to Brief"):
            brief_class = get_brief_class()
            brief_class.add_to_brief(result['final_brief'])
            brief_class.update_brief_result(result)

    with col2:
        # Add custom CSS for the questions list with vertical scroll
        st.markdown(
            """
            <style>
            .question-box {
                background-color: #f0f0f0;
                padding: 10px;
                margin-bottom: 10px;
                border-radius: 5px;
            }
            .question-container {
                max-height: 70vh; /* Adjust the height as needed */
                overflow-y: auto;
                padding-right: 10px; /* Add some padding for better look */
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown('<div class="question-container">', unsafe_allow_html=True)
        for q in result['questions']:
            st.markdown(f'<div class="question-box">{q["question"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    # Example JSON data for testing
    result = {
        "final_brief": "This is an example final brief text.",
            "questions": [
                {"question": "What is your name?"},
                {"question": "How old are you?"},
                {"question": "Where do you live?"},
                {"question": "What is your profession?"},
                {"question": "What are your hobbies?"},
                {"question": "What is your favorite book?"},
                {"question": "What is your favorite movie?"},
                {"question": "What is your favorite food?"},
                {"question": "What is your favorite color?"},
                {"question": "What is your favorite sport?"}
            ]
    }

    show(result)
