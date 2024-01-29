import streamlit as st
import time
import io
import base64
from PIL import Image
from services.ideal_girl_api import ideal_girl_api

def convert_base64_image_to_local_file(base64_image):
    img = Image.open(io.BytesIO(base64.decodebytes(bytes(base64_image, "utf-8"))))
    img.save('image.png')

st.title("Ideal Girl")

st.write("")

input = st.text_area(
    "Your ideal girl description",
    "high quality, 8K Ultra HD, masterpiece, realistic photo, wash technique, colorful, pale touch, smudged outline, like a fairy tale, soft touch, a Hong Kong lady, age 26, long straight hair, pretty face, shiny eyes, she is sitting on the ground, in Tokyo  city, she is wearing one piece mini skirt, sunny day, wide shot, low angle, luminism, three dimensional effect, enhanced beauty, luminism, 3d render, octane render, Isometric, awesome full sharp colors",
    height=200
)

style_preset = st.selectbox(
    "Select image style", 
    (
        '3d-model', 
        'analog-film',
        'anime',
        'cinematic',
        'comic-book',
        'digital-art',
        'enhance',
        'fantasy-art',
        'isometric',
        'line-art',
        'low-poly',
        'modeling-compound',
        'neon-punk',
        'origami',
        'photographic',
        'pixel-art',
        'tile-texture'
    ),
    index=14
)

submit_button_clicked = st.button("Submit", type="primary")
if submit_button_clicked:
    if input:
        print(f"input = {input}")

        base64_image = ideal_girl_api(input, style_preset)
        if base64_image:
            with st.spinner('Loading...'):
                time.sleep(2)

                convert_base64_image_to_local_file(base64_image)
                st.image("image.png")
