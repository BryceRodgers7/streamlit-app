import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

st.title("About Me")
st.write(f"Hi I'm Bryce, a programmer who has dabbled in data science and AI for over a decade.")
st.write(f"I have a Patent for my work integrating a Support Vector Machine into a novel Android app back in 2013. (US9299264B2) ")
st.write(f"The following year I constructed a standardized test score predictor.")
st.write(f"The engine used KNN to model the student's final subject-score.")
st.write(f"I've been a system architect, a full-stack developer, I was even a QA/test lead for part of my internship.")
st.write(f"In college I took every AI-class in the cirriculum,")
st.write(f"culminating in a course that combined data science and programming, taught by Nick Street.")
st.write(f"I have recently completed Andrej Karpathy's lecture series on YouTube,")
st.write(f"and Jeremy Howard's Practical Deep Learning for Coders 2022!")
st.write(f"Take a look around the website, where I've deployed different Machine Learning models for various tasks!!!")
