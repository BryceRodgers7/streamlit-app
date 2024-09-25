import streamlit as st
from menu import menu_with_redirect
import io
import json
import os
from PIL import Image
import requests
import time
import getpass
from random import randrange

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()
current_content = io.BytesIO()

# Verify the user's role
if st.session_state.role not in ["user", "admin", "super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.title("Welcome to the special Picture Page!!")

if 'STABILITY_KEY' in st.secrets:
    STABILITY_KEY = st.secrets['STABILITY_KEY']
    st.sidebar.success('API key is good.', icon='✅')
else:
    st.sidebar.warning('credentials are not working.', icon='⚠️')

host = f"https://api.stability.ai/v2beta/stable-image/generate/sd3"
st.session_state.show_pic = False

def send_generation_request(host, params,):
    headers = {
        "Accept": "image/*",
        "Authorization": f"Bearer {STABILITY_KEY}"
    }

    # Encode parameters
    files = {}
    image = params.pop("image", None)
    mask = params.pop("mask", None)
    if image is not None and image != '':
        files["image"] = open(image, 'rb')
    if mask is not None and mask != '':
        files["mask"] = open(mask, 'rb')
    if len(files)==0:
        files["none"] = ''

    # Send request
    print(f"Sending REST request to {host}...")
    response = requests.post(
        host,
        headers=headers,
        files=files,
        data=params
    )
    if not response.ok:
        raise Exception(f"HTTP {response.status_code}: {response.text}")

    return response

def get_image(content):
    global current_content
    current_content = io.BytesIO(content)
    return current_content

def get_image_bytes():
    return current_content
    
if "show_pic" not in st.session_state:
        st.session_state.show_pic = False

placeholder = st.empty()

@st.cache_data
def hit_stability(prompt):
    global placeholder
    placeholder.empty()
    params = {
        "prompt" : prompt,
        "aspect_ratio" : "1:1",
        "seed" : 42,
        "output_format" : 'jpeg',
        "model" : "sd3-medium"
    }

    response = send_generation_request(host,params)

    # Decode response
    content = response.content
    finish_reason = response.headers.get("finish-reason")
    # seed = response.headers.get("seed")

    # Check for NSFW classification
    if finish_reason == 'CONTENT_FILTERED':
        raise Warning("Generation failed NSFW classifier")

    placeholder = st.image(get_image(content), caption=prompt)

def fake_hit_stab(prompt):
    global placeholder
    placeholder.empty()
    images = ["https://cdn.prod.website-files.com/62d84e447b4f9e7263d31e94/637627ca9eebde45ae5f394c_Underwater-Nun.jpeg", 
              "https://s3-us-west-2.amazonaws.com/uw-s3-cdn/wp-content/uploads/sites/6/2017/11/04133712/waterfall.jpg",
              "https://i.ytimg.com/vi/3x0SJ6-LrcA/sddefault.jpg"]
    time.sleep(2)
    placeholder = st.image(
            images[randrange(3)],
            caption=prompt
        )

#img_prompt = st.text_area("What would you like to see? RANDOM IMAGES ENABLED", "A beautiful parrot before a lush background of jungle canopy.")
img_prompt = st.text_area("What would you like to see?", "A beautiful parrot before a lush background of jungle canopy.")
click = st.button("See It!", help="submit your prompt and get an image", use_container_width=False)

if click:
    st.session_state.show_pic = True
    
if st.session_state.show_pic:
    #fake_hit_stab(img_prompt, placeholder)
    hit_stability(img_prompt)
    img_BufferedReader = io.BufferedReader(get_image_bytes())
    dl_click = st.download_button(
      label="Download Image",
      data=img_BufferedReader,
      file_name="imagename.png",
      mime="image/jpeg",
      )
# st.button("clear it!", help="clear the image", on_click=clear_image(), use_container_width=False)