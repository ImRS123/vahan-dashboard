import streamlit as st

# Set the page configuration to wide mode
st.set_page_config(layout="wide")

# Create a simple dashboard
st.title("My Dashboard")

# Save the HTML file
with open("dashboard.html", "r") as f:
    f.read()

# Open the HTML file in a web browser
#import webbrowser
#webbrowser.open("dashboard.html")
