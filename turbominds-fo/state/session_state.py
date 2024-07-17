import streamlit as st
from state.brief_session import Brief_State

brief_class = None

def get_brief_class():
    global brief_class
    if brief_class is None:
        brief_class = Brief_State("EXAMPOEL")
        return brief_class
    else:
        return brief_class