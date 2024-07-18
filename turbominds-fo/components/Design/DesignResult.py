import streamlit as st
from streamlit_quill import st_quill


def show():
    content = st_quill(value="<b>Streamlit</b> is **really** ***cool***.")
    

if __name__ == "__main__":
    show()
