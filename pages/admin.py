import streamlit as st
from menu import menu_with_redirect
from io import BytesIO
import json
import os
from PIL import Image
import requests
import time
import getpass

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

# Verify the user's role
if st.session_state.role not in ["admin", "super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.title("Welcome to the special Picture Page!!")

if 'STABILITY_KEY' in st.secrets:
    STABILITY_KEY = st.secrets['STABILITY_KEY']
    st.sidebar.success('API key is good.', icon='✅')
else:
    st.sidebar.warning('credentials are not working.', icon='⚠️')

host = f"https://api.stability.ai/v2beta/stable-image/generate/sd3"
img_prompt = st.text_area("what do you want to see?", "A scarred landscape from above, dotted with Battlemechs in the midst of battle.")

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

@st.cache_data
def get_image(content):
    return BytesIO(content)

def hit_stability(prompt):
    params = {
        "prompt" : prompt,
        "aspect_ratio" : "1:1",
        "seed" : 0,
        "output_format" : 'jpeg',
        "model" : "sd3-medium"
    }

    response = send_generation_request(host,params)

    # Decode response
    output_image = response.content
    finish_reason = response.headers.get("finish-reason")
    seed = response.headers.get("seed")

    # Check for NSFW classification
    if finish_reason == 'CONTENT_FILTERED':
        raise Warning("Generation failed NSFW classifier")

    st.image(get_image(output_image), key=72, caption=prompt)

def fake_hit_stab(prompt):
    st.image(
            "https://s3-us-west-2.amazonaws.com/uw-s3-cdn/wp-content/uploads/sites/6/2017/11/04133712/waterfall.jpg",
            key=72,
            width=400, # Manually Adjust the width of the image as per requirement
            caption=prompt
        )

def clear_image():
    with st.empty():
        st.image(key=72)

st.button("See It!", help="submit your prompt and get an image", on_click=fake_hit_stab(img_prompt), use_container_width=False)
st.button("clear it!", help="clear the image", on_click=clear_image(), use_container_width=False)