import streamlit as st

def show_popup(button_text):
    st.session_state["popup"] = button_text

def clear_popup():
    st.session_state["popup"] = None

@st.experimental_dialog("Create Design")
def create_Design_dialog(Design_type):
    st.write(Design_type)
    content = st.text_area("Design Description")
    if st.button("Submit"):
        st.session_state.create_Design = {"design_type": Design_type, "content": content}
        clear_popup()
        st.rerun()

def show():
    if "popup" not in st.session_state:
        st.session_state["popup"] = None
    if "create_Design" not in st.session_state:
        st.session_state["create_Design"] = None

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

    st.markdown("<h1 class='centered'>Select a Design Template</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='centered'>Select a template We've got all kinds of marketing/brand requirements covered</h3>", unsafe_allow_html=True)

    # Grid layout for buttons using Streamlit columns
    buttons_data = [
        {"logo": "🎨", "text": "Digital Art"},
        {"logo": "💻", "text": "Low Poly"},
        {"logo": "📱", "text": "Photographic"},
    ]

    cols = st.columns(3)
    for i, button_data in enumerate(buttons_data):
        col = cols[i % 3]
        with col:
            if st.button(f"{button_data['logo']} {button_data['text']}", key=button_data['text']):
                show_popup(button_data["text"])

    if st.session_state["popup"]:
        create_Design_dialog(st.session_state["popup"])

    st.write("\n\n")
    st.write("<div class='centered'>💡 Did you know, 1/3 of all marketing budgets are wasted on bad briefs?</div>", unsafe_allow_html=True)

    return st.session_state.create_Design