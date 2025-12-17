import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Welcome Vijaya",
    page_icon="👋",
    layout="centered"
)

# Title
st.title("👋 Welcome, Vijaya!")

# Subtitle
st.write("This is a sample Streamlit app running successfully 🚀")

# Divider
st.divider()

# User input
name = st.text_input("Enter your name", value="Vijaya")
age = st.number_input("Enter your age", min_value=1, max_value=100, value=25)

# Button action
if st.button("Submit"):
    st.success(f"Hello {name}! 🎉")
    st.write(f"Your age is **{age}**")
    st.write(f"Current time: **{datetime.now().strftime('%d %b %Y, %I:%M %p')}**")

# Sidebar
st.sidebar.header("User Info")
st.sidebar.write("Name:", name)
st.sidebar.write("Age:", age)

# Footer
st.divider()
st.caption("Created using Streamlit ❤️")
