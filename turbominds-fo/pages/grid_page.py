import streamlit as st

def main():
    st.title("Grid Page")
    st.write("Welcome to the Grid Page!")
    
    cols = st.columns(4)
    for i in range(4):
        for j in range(4):
            with cols[j]:
                if st.button(f'Button {i*4 + j + 1}'):
                    st.write(f'Button {i*4 + j + 1} clicked')
