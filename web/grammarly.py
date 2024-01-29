import streamlit as st
import time
from services.grammarly_api import grammarly_api

st.title("Grammarly")

st.write("")

input = st.text_area(
    "Format and check grammar",
    "",
    height=200
)

submit_button_clicked = st.button("Submit", type="primary")
if submit_button_clicked:
    if input:
        print(f"input = {input}")

        output_text = grammarly_api(input)
        if output_text:
            with st.spinner('Loading...'):
                time.sleep(2)
                st.write(f"Result: {output_text}")