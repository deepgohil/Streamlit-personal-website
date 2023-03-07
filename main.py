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
# st.write('{"Name":"DeepGohil"  <br>"age"}')






st.write("""<pre>
{ 
  <br>"Name": "Deep Gohil",
  <br>"Email": "hello@deepgohil.engineer",
  <br>"Phone": "+918104680835", <br>
  "Work_Experience":   <br>{
      <br>&emsp;&emsp;"company": "Nilee Games",
      <br>&emsp;&emsp;"position": "Backend Developer",
      <br>&emsp;&emsp;"start_date": "Feb-2022",
      <br>&emsp;&emsp;"end_date": "Dec-2022"
      <a href='https://www.streamlit.io/'>link</a>
      <br>&emsp;&emsp;"tasks":" Working as backend platform developer for TMKUCtaarak mehta ka ulta chashma) upcoming game which can handle upto 10 lakh user
  <br>Active contributor in architecture discussions and development of various python micro services on AWS Cloud Infrastructure(E.g payment, KYC,prize distribution)
  <br>Automate CI/CD pipelines using AWS CodePipeline Technologies used are node js python, AWS SQS AWS ElastiCache AWS lambda etc"
    <br>},
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

</pre>""", unsafe_allow_html=True)


st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")
