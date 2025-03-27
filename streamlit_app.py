import streamlit as st
import pandas as pd

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")

name = st.text_input("Enter your name")
age = st.slider("Select your age", 0, 100)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)
    
    

if st.button("Click Me"):
    st.write(f"Hello, {name}! You are {age} years old.")
    

option = st.selectbox(
    'Choose an option',
    ['Option 1', 'Option 2', 'Option 3']
)
st.write('You selected:', option)
