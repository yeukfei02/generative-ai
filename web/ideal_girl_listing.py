import streamlit as st
from services.get_ideal_girl_api import get_ideal_girl_api

st.title("Ideal Girl Listing")

st.write("")

grid_width = st.number_input(
    "Select Grid Width", min_value=1, max_value=5, value=3)

urls = get_ideal_girl_api()


def show_images_grid():
    groups = []

    for i in range(0, len(urls), grid_width):
        groups.append(urls[i: i + grid_width])

    for group in groups:
        cols = st.columns(grid_width)
        for i, image_file in enumerate(group):
            cols[i].image(image_file)


show_images_grid()
