import streamlit as st
import pandas as pd
import numpy as np
import requests

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     [1,2,3,4,5])

'You selected: ', option


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

res = requests.get('https://jsonplaceholder.typicode.com/todos')


if res.status_code == 200:
    data = res.json()
    st.dataframe(data)