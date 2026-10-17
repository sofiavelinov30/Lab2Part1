# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Homepage",  # The title that appears in the browser tab
    page_icon="🏠",         # An emoji that appears as the icon in the browser tab
)

# WELCOME PAGE TITLE
st.title("Welcome to the Mappting your Ideal Weekend! ☀️")

# INTRODUCTORY TEXT
st.write("This page is designed to further examine our compatibility as friends! By using your choices for an ideal weekend we can see the break down of how we would spend an idealweekend together for both of us! If you don't find an option you like please at least choose one that you're okay with so that the chart works properly :) Enjoy!!!")

# OPTIONAL: ADD AN IMAGE
# 1. Navigate to the 'images' folder in your Lab02 directory.
# 2. Place your image file (e.g., 'welcome_image.png') inside that folder.
# 3. Uncomment the line below and change the filename to match yours.
#
st.image("images/welcome_image.png")
