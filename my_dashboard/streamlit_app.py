import streamlit as st

# Basic Streamlit Dashboard Template
st.title("Welcome to Learning Analytics Dashboard")
st.write("This is a basic dashboard template for analyzing student learning data.")

# Text input section
st.header("Text Input")
user_input = st.text_area("Enter your text here:", height=150)

# Output area
st.header("Output")
if user_input:
    st.write("You entered:")
    st.info(user_input)
    st.write(f"Character count: {len(user_input)}")
    st.write(f"Word count: {len(user_input.split())}")
else:
    st.write("No input yet. Please enter some text above.")
