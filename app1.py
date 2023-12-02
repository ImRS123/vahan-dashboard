import streamlit as st

# Set the page configuration to wide mode
st.set_page_config(layout="wide")

# Create a simple dashboard
st.title("My Dashboard")

# Save the HTML file
with open("dashboard.html", "w") as f:
    f.write("""
<!DOCTYPE html>
<html lang="en">
<head>
<style>
body {
  margin: 0;
  padding: 0;
}

iframe {
  width: 100vw;
  height: 100vh;
}
</style>
</head>
<body>
<iframe src="https://app.powerbi.com/view?r=eyJrIjoiNTcyNTcyNDItMjZiNS00ZmYzLWJkMTYtMzhiODM5OWY1Y2I1IiwidCI6IjJiZDAyMzJmLWNjZTEtNDZkMS04ZWE2LTQzMTE1NTVlMzAyYiJ9" 
  frameborder="0" allowFullScreen="true"
  height = "450px"
  style = "width:100%; border:none;"></iframe>
</body>
</html>
""")

# Open the HTML file in a web browser
import webbrowser
webbrowser.open("dashboard.html")
