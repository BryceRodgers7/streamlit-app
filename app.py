import streamlit as st
from menu import menu

st.title("Bryce Rodgers'")
st.subheader('Data Science Demo Site')
# st.write("By Bryce Rodgers")
menu() # Render the dynamic menu!

# st.write("choose a role ffs")
# Initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = 'user'
# Retrieve the role from Session State to initialize the widget
st.session_state._role = st.session_state.role

def set_role():
    # Callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role

# Selectbox to choose role
# st.selectbox(
#     "Select your role:",
#     [None, "user", "admin", "super-admin"],
#     key="_role",
#     on_change=set_role,
# )

st.markdown("<p style='font-size:20px; font-weight:bold;'>Navigate using the sidebar, or the links below</p>", unsafe_allow_html=True)

# st.write("Navigate using the sidebar, or the links below")
st.write("This Llama-2 Chatbot thinks he's a pirate!")
st.page_link("pages/chatbot.py", label="Pirate Chatbot")
st.write("Tell StabilityAI to make a picture for you!")
st.page_link("pages/stability.py", label="Picture Page")
st.write("Generate a Star Trek script using VoyagerGPT!")
st.page_link("pages/voyagergpt.py", label="VoyagerGPT")
st.write("Familiarize yourself with different warriors in the world of Warcraft!")
st.page_link("pages/warcraft.py", label="Warcraft World")
st.write("Discover the Dune Universe like you've never experienced it before!... A Topic Model using TF-IDF.")
st.page_link("pages/dune.py", label="Dune Universe")
st.write("Check out the Dune (2021) script and compare the topics against the books!")
st.page_link("pages/pps.py", label="Dune Movie")