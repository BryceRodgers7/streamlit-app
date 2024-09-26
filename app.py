import streamlit as st
from menu import menu



# Initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None

# Retrieve the role from Session State to initialize the widget
st.session_state._role = st.session_state.role

def set_role():
    # Callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role


st.title("Bryce's demo site")
# Selectbox to choose role
st.selectbox(
    "Select your role:",
    [None, "user", "admin", "super-admin"],
    key="_role",
    on_change=set_role,
)
menu() # Render the dynamic menu!
st.subheader("explore the AI using the links below")
st.write("First up, a Llama Chatbot that thinks he's a pirate!")
st.page_link("pages/chatbot.py", label="Pirate Chatbot")
st.write("Next is a page integrated with StabilityAI to make pictures!")
st.page_link("pages/stability.py", label="Picture Page")
st.write("And finally a Topic Model of the Dune Trilogy using TF-IDF")
st.page_link("pages/dune.py", label="Dune Universe")
st.write("But wait, there's more! I found the script for the new Dune film and played around some more!!")
st.page_link("pages/pps.py", label="Dune Movie")