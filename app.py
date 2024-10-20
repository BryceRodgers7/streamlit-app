import streamlit as st
from menu import menu


st.title("Data Science Demo Site")
st.write("By Bryce Rodgers")
menu() # Render the dynamic menu!

st.session_state.role = "user"


st.subheader("Navigate using the sidebar, or the links below")
st.write("This Llama-2 Chatbot thinks he's a pirate!")
st.page_link("pages/chatbot.py", label="Pirate Chatbot")
st.write("Tell StabilityAI to make a picture for you!")
st.page_link("pages/stability.py", label="Picture Page")
st.write("Generate a Star Trek script using VoyagerGPT!")
st.page_link("pages/voyagergpt.py", label="VoyagerGPT")
st.write("Familiarize yourself with different warriors in Warcraft World!")
st.page_link("pages/warcraft.py", label="Warcraft World")
st.write("Discover the Dune Universe like you've never experienced it before!... A Topic Model using TF-IDF.")
st.page_link("pages/dune.py", label="Dune Universe")
st.write("Check out the Dune (2021) script and compare the topics against the books!")
st.page_link("pages/pps.py", label="Dune Movie")