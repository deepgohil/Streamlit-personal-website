import streamlit as st
import pandas as pd
from PIL import Image

im = Image.open("favi.ico")
st.set_page_config(
    page_title="Hello",
    page_icon=im
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
# st.write('{"Name":"DeepGohil" \n"age"}')
st.write("line 1\n line 2\n line 3")

st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")
