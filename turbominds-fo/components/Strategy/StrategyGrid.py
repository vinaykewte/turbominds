import streamlit as st
from state.session_state import get_brief_class
def show_popup(button_text):
    st.session_state["popup"] = button_text

def clear_popup():
    st.session_state["popup"] = None

@st.experimental_dialog("Create Strategy")
def create_Strategy_dialog(strategy_type):
    st.write(strategy_type)
    brief_class = get_brief_class()
    objective_options = [
        "Awareness",
        "Engagement",
        "Conversion",
        "Re-marketing"
    ]
    brief_options = [brief_class.title]
    brief = st.selectbox("Choose Brief:", brief_options)
    objective = st.selectbox("Choose Objective:", objective_options)
    description = st.text_area("Strategy Description", placeholder="optional")
    if st.button("Submit"):
        brief_class = get_brief_class()
        st.session_state.create_Strategy = {"context" : brief_class.final_brief, "type": strategy_type, "objective" : objective, "description": description}
        clear_popup()
        st.rerun()

def show():
    if "popup" not in st.session_state:
        st.session_state["popup"] = None
    if "create_Strategy" not in st.session_state:
        st.session_state["create_Strategy"] = None

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

    st.markdown("<h1 class='centered'>Select a Strategy Template</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='centered'>Select a template We've got all kinds of marketing/brand requirements covered</h3>", unsafe_allow_html=True)

    # Grid layout for buttons using Streamlit columns
    buttons_data = [
        {"logo": "📣", "text": "Integrated Strategy"},
        {"logo": "🎨", "text": "Social Media Strategy"},
        {"logo": "🎉", "text": "Influencer Strategy"},
        {"logo": "💻", "text": "Google Ads"},
        {"logo": "📱", "text": "Meta Ads"},
        {"logo": "📈", "text": "PR Strategy"},
    ]

    cols = st.columns(3)
    for i, button_data in enumerate(buttons_data):
        col = cols[i % 3]
        with col:
            if st.button(f"{button_data['logo']} {button_data['text']}", key=button_data['text']):
                show_popup(button_data["text"])

    if st.session_state["popup"]:
        create_Strategy_dialog(st.session_state["popup"])

    st.write("\n\n")
    st.write("<div class='centered'>💡 A/B testing can improve conversion rates by up to 20%.</div>", unsafe_allow_html=True)

    return st.session_state.create_Strategy