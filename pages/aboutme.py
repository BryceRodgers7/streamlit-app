import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

st.title("About Me")
st.image("./.static/me.jpg")
st.write(f"Hey I'm Bryce, an experienced programmer who has dabbled in data science and AI for over a decade!")
st.write(f"I have a Patent for my work integrating a Support Vector Machine into a novel Android app back in 2013. (US9299264B2) ")
st.write(f"The following year I built a standardized test score-predictor with a KNN model at its core.")
st.write(f"I've been a system architect, a full-stack developer, I even served as QA/test lead during my internship.")
st.write(f"In college I took every AI-class in the cirriculum, culminating in a course that combined data science and programming, taught by Nick Street.")
# st.write(f"")
st.write(f"I have recently completed Andrej Karpathy's lecture series on YouTube, and Jeremy Howard's Practical Deep Learning for Coders 2022!")
# st.write(f"")
st.write(f"Take a look around my website, where I've deployed different models for various Machine Learning tasks!!")
