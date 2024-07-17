import streamlit as st
from state.session_state import get_brief_class

st.write(get_brief_class())