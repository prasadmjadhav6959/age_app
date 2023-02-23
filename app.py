import streamlit as st
from datetime import datetime

# Set the app title and layout
st.set_page_config(page_title="Age Calculator", layout="wide")

# Define the app header and subheader
st.title("Age Calculator App")
st.subheader("Enter your birthdate to calculate your age")

# Define the input fields for the user's birthdate
year = st.number_input("Year of Birth", min_value=1900, max_value=datetime.now().year, step=1)
month = st.number_input("Month of Birth", min_value=1, max_value=12, step=1)
day = st.number_input("Day of Birth", min_value=1, max_value=31, step=1)

# Calculate the age based on the input fields
birthdate = datetime(year, month, day)
today = datetime.now()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Display the calculated age
st.write(f"Your age is {age} years old.")