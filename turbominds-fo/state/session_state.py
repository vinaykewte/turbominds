import streamlit as st
from state.brief_session import Brief_State

brief_class = None

def get_brief_class():
    global brief_class

    ################################################################
    if brief_class is None:
        brief_class = Brief_State(id=1, title="Default Brief")
        brief_class.add_to_brief("Default Brief")
    ########################################
    return brief_class

def create_brief_class(title):
    global brief_class
    brief_class = Brief_State(id=1, title=title)
    return brief_class