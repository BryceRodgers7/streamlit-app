import streamlit as st
from menu import menu_with_redirect
import replicate
import os
from random import randrange

menu_with_redirect()



st.title('Warcraft Factions')

st.write("TODO: add an upload button here to check if an image file is a Footie, Grunt, Ghoul, or NE Archer.")

st.write("Human Footman")
st.image('./.static/footman.jpg')

st.write("Orc Grunt")
st.image('./.static/grunt.jpg')

st.write("Undead Ghoul")
st.image('./.static/ghoul.jpg')

st.write("Night Elf Archer")
st.image('./.static/nearcher.jpg')