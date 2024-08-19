import streamlit as st
import time
from services.best_deal_api import best_deal_api

st.title("Best deal")

st.write("")

location = st.text_input(
    label="Location",
    placeholder="Enter location"
)

timeline = st.selectbox(
    label="Timeline",
    placeholder="Select timeline",
    options=["today", "this week", "this month"]
)

submit_button_clicked = st.button("Submit", type="primary")
if submit_button_clicked:
    if location and timeline:
        print(f"location = {location}")
        print(f"timeline = {timeline}")

        output_text = best_deal_api(location, timeline)
        if output_text:
            with st.spinner('Loading...'):
                time.sleep(2)
                st.write(f"Result: {output_text}")
