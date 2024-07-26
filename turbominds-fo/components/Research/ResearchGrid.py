import streamlit as st
from state.session_state import get_brief_class
def show_popup(button_text):
    st.session_state["popup"] = button_text

def clear_popup():
    st.session_state["popup"] = None

@st.experimental_dialog("Create Research")
def create_research_dialog(research_type):
    brief_class = get_brief_class()
    brief_options = [brief_class.title]
    objective_options = [
        "Buying patterns",
        "Media Consumption Hobbies",
        "Brand Perception",
        "Product Preferences",
        "Customer Satisfaction Levels",
        "Market Segmentation"
    ]

    st.write(research_type)
    brief = st.selectbox("Choose Brief:", brief_options)
    objective = st.selectbox("Choose Objective:", objective_options)
    description = st.text_area("Research Description", placeholder="optional")
    if st.button("Submit"):
        st.session_state.create_research = {"context" : brief_class.final_brief, "type": research_type, "objective": objective, "description": description}
        # st.write(st.session_state.create_research)
        clear_popup()
        st.rerun()

def show():
    if "popup" not in st.session_state:
        st.session_state["popup"] = None
    if "create_research" not in st.session_state:
        st.session_state["create_research"] = None

    # Custom CSS for consistent button size and center alignment
    st.markdown("""
        <style>
            .centered {
                text-align: center;
            }
            .stButton button {
                width: 150px;
                height: 50px;
                margin: 5px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='centered'>Select a Research Template</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='centered'>Select a template We've got all kinds of marketing/brand requirements covered</h3>", unsafe_allow_html=True)

    # Grid layout for buttons using Streamlit columns
    buttons_data = [
        {"logo": "📣", "text": "Industry Research"},
        {"logo": "🎨", "text": "Consumer Research"},
        {"logo": "🎉", "text": "Brand Research"},
        {"logo": "💻", "text": "Market Research"},
        {"logo": "📱", "text": "Product Research"},
        {"logo": "📈", "text": "Competitor Research"},
    ]

    cols = st.columns(3)
    for i, button_data in enumerate(buttons_data):
        col = cols[i % 3]
        with col:
            if st.button(f"{button_data['logo']} {button_data['text']}", key=button_data['text']):
                show_popup(button_data["text"])

    if st.session_state["popup"]:
        create_research_dialog(st.session_state["popup"])

    st.write("\n\n")
    st.write("<div class='centered'>💡 Approximately 90% of the data collected by marketing agencies is unstructured.</div>", unsafe_allow_html=True)

    return st.session_state.create_research