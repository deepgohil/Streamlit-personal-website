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






st.write("""
{\n\n
  "Name": "Deep Gohil",\n
  "Email": "hello@deepgohil.engineer",\n
  "Phone": "+918104680835",\n
  "Work_Experience": \n\n{
    \n\n"company": "Nilee Games",
    \n\n"position": "Backend Developer",
    \n\n"start_date": "Feb-2022",
    \n\n"end_date": "Dec-2022"
    \n\n"tasks":" Working as backend platform developer for TMKUCtaarak mehta ka ulta chashma) upcoming game which can handle upto 10 lakh user
\n\nActive contributor in architecture discussions and development of various python micro services on AWS Cloud Infrastructure(E.g payment, KYC,prize distribution)
\n\nAutomate CI/CD pipelines using AWS CodePipeline Technologies used are node js python, AWS SQS AWS ElastiCache AWS lambda etc"
  \n\n},
  "skills": [
    "Python",
    "JavaScript",
    "SQL",
    "HTML",
    "CSS"
  ],
  "education": [
    {
      "school": "University of California, Berkeley",
      "degree": "Bachelor of Science",
      "major": "Computer Science",
      "graduation_date": "2014-05-01"
    },
    {
      "school": "Stanford University",
      "degree": "Master of Science",
      "major": "Computer Engineering",
      "graduation_date": "2016-05-01"
    }
  ],
  "references": [
    {
      "name": "Jane Smith",
      "email": "jane@example.com",
      "phone": "555-555-9012"
    },
    {
      "name": "Bob Johnson",
      "email": "bob@example.com",
      "phone": "555-555-3456"
    }
  ]
}

""")


st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")
