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

# def classify_image(img):
#     pred,idx,probs = model.predict(img)
#     return dict(zip(categories, map(float,probs)))

st.title('Warcraft Factions')

uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

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

# st.write("TODO: add an upload button here to check if an image file is a Footie, Grunt, Ghoul, or NE Archer.")

# st.write("Human Footman")
# st.image('./.static/footman.jpg')

# st.write("Orc Grunt")
# st.image('./.static/grunt.jpg')

# st.write("Undead Ghoul")
# st.image('./.static/ghoul.jpg')

# st.write("Night Elf Archer")
# st.image('./.static/nearcher.jpg')