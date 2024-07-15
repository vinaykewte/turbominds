import streamlit as st

def show_popup(button_text):
    st.session_state["popup"] = button_text

def clear_popup():
    st.session_state["popup"] = None

@st.experimental_dialog("Create Brief")
def create_brief_dialog(brief_type):
    st.write(brief_type)
    content = st.text_area("Brief Description")
    if st.button("Submit"):
        st.session_state.create_brief = {"brief_type": brief_type, "content": content}
        clear_popup()
        st.rerun()

def show():
    if "popup" not in st.session_state:
        st.session_state["popup"] = None
    if "create_brief" not in st.session_state:
        st.session_state["create_brief"] = None

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

    st.markdown("<h1 class='centered'>Select a Brief Template</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='centered'>Select a template We've got all kinds of marketing/brand requirements covered</h3>", unsafe_allow_html=True)

    # Grid layout for buttons using Streamlit columns
    buttons_data = [
        {"logo": "📣", "text": "Integrated Campaign"},
        {"logo": "🎨", "text": "Creative Brief"},
        {"logo": "🎉", "text": "Events and Launches"},
        {"logo": "💻", "text": "Web Dev"},
        {"logo": "📱", "text": "App Dev"},
        {"logo": "📈", "text": "Meta Ads"},
        {"logo": "🔍", "text": "Google Ads"},
        {"logo": "📢", "text": "Social Media"},
        {"logo": "🎥", "text": "Videoshoot"},
        {"logo": "📸", "text": "Photoshoot"},
        {"logo": "📰", "text": "PR Campaign"},
        {"logo": "👩‍💻", "text": "Influencer Brief"},
    ]

    cols = st.columns(4)
    for i, button_data in enumerate(buttons_data):
        col = cols[i % 4]
        with col:
            if st.button(f"{button_data['logo']} {button_data['text']}", key=button_data['text']):
                show_popup(button_data["text"])

    if st.session_state["popup"]:
        create_brief_dialog(st.session_state["popup"])

    st.write("\n\n")
    st.write("<div class='centered'>💡 Did you know, 1/3 of all marketing budgets are wasted on bad briefs?</div>", unsafe_allow_html=True)

    return st.session_state.create_brief