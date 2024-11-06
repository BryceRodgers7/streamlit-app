import streamlit as st
from menu import menu_with_redirect
from fastai.vision.all import *
from PIL import Image

menu_with_redirect()

PATH = './.static/models/allfourfinetuned.pkl'
categories = ('Grunt', 'Footman', 'Ghoul', 'Night Elf Archer')

@st.cache(allow_output_mutation=True)
def load_model():
    learner = load_learner(PATH)
    return learner

model = load_model()

st.title('Warcraft Factions')
st.subheader('The Roster')
st.write('In warcraft, each faction has a basic type of soldier that makes up the bulk of their numbers')

def display_images_side_by_side(image_paths, captions, width=150):  
    # Create columns based on the number of images
    columns = st.columns(len(image_paths))
    
    # Display each image in its respective column, along with caption
    for col, img, caption in zip(columns, image_paths, captions):
        with col:
            st.image(img, caption=caption, use_column_width=False, width=width)

# st.write("The Roster of Warcraft World")
image_paths = ["./.static/footman.jpg", "./.static/grunt.jpg", "./.static/ghoul.jpg", "./.static/nearcher.jpg"]
captions = ["Footman", "Grunt", "Ghoul", "Night Elf Archer"]
# Call the function with the images you want to display side-by-side
display_images_side_by_side(image_paths, captions)

uploaded_file = st.file_uploader("Upload an image (to determine if it resembles anything in the roster)", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Predict the class of the image
    st.write("Classifying...")
    pred, pred_idx, probs = model.predict(image)
    
    # Display the result
    st.write(f"Prediction: {pred}")
    st.write(f"Confidence: {probs[pred_idx]:.4f}")
else:
    st.write("Please upload an image to classify.")