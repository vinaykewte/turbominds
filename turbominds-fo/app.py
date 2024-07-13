import streamlit as st
import importlib

st.sidebar.title("Navigation")
pages = {
    # "Home": "page1",
    "About": "page2",
    # "Grid Page": "grid_page"
}

selection = st.sidebar.radio("Go to", list(pages.keys()))

page = importlib.import_module(f'pages.{pages[selection]}')
page.main()
