import streamlit as st

st.title("Hello App")

# Create two columns
col1, col2 = st.columns(2)

# Input in first column (Name)
with col1:
    name = st.text_input("Name")

# Input in second column (Age)
with col2:
    age = st.number_input("Age", min_value=1, max_value=120, step=1)

# Button to show message
if st.button("Submit"):
    if name:
        st.success(f"Hello! Your name is {name} and your age is {age}.")
    else:
        st.warning("Please enter your name.")
