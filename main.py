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
      <br>&emsp;&emsp;"Nilee Games":{
      <br>&emsp;&emsp;&emsp;"position": "Backend Developer",
      <br>&emsp;&emsp;&emsp;"start_date": "Feb-2022",
      <br>&emsp;&emsp;&emsp;"end_date": "Dec-2022"
      <a href='https://www.streamlit.io/'>link</a>
      <br>&emsp;&emsp;&emsp;"tasks":<br>&emsp;&emsp;&emsp;&emsp;["Workd as backend platform developer for TMKUC(taarak mehta ka ulta chashma) upcoming game which can handle upto 10 lakh user",
  <br>"Active contributor in architecture discussions and development of various python micro services on AWS Cloud Infrastructure(E.g payment, KYC,prize distribution)",
  <br>"Automate CI/CD pipelines using AWS CodePipeline Technologies used are node js python, AWS SQS AWS ElastiCache AWS lambda etc"]
    <br>},
    <br>&emsp;&emsp;"Plotsify":{
      <br>&emsp;&emsp;&emsp;"position": "Data Analyst",
      <br>&emsp;&emsp;&emsp;"start_date": "Aug-2021",
      <br>&emsp;&emsp;&emsp;"end_date": "Feb-2022"
      
      <br>&emsp;&emsp;&emsp;"tasks":<br>&emsp;&emsp;&emsp;&emsp;["Create a BOT to deliver automated messages to followers of 99acres, MagicBricks and Housing.com about our company and extract their username, Email and phone number for targeted marketing"]
    <br>}
 <br>"skills": [
  <br>&emsp;&emsp;&emsp;"AWS",
    <br>&emsp;&emsp;&emsp;"Python",
    <br>&emsp;&emsp;&emsp;"JavaScript",
    <br>&emsp;&emsp;&emsp;"SQL",
    <br>&emsp;&emsp;&emsp;"HTML",
    <br>&emsp;&emsp;&emsp;"CSS",
    
  <br>&emsp;&emsp;],
  <br>"education": [
    <br>&emsp;{
      <br>&emsp;&emsp;&emsp;"School": "S.V.P.V.Vdyalaya",
      <br>&emsp;&emsp;&emsp;"Details": "SECONDARY SCHOOL (88%)"
      <br>&emsp;&emsp;&emsp;"graduation_date": "2018"
    },
    <br>&emsp;
    {
      <br>&emsp;&emsp;&emsp;"College": "G.P Mumbai",
      <br>&emsp;&emsp;&emsp;"Details": "DIPLOMA IN INFORMATION TECHNOLOGY (94%) ",
      <br>&emsp;&emsp;&emsp;"graduation_date": "2021"
     },
     <br>&emsp;{
      <br>&emsp;&emsp;&emsp;"College": "Dwarkadas sanghvi college of engineering",
      <br>&emsp;&emsp;&emsp;"Details": "B-tech",
      <br>&emsp;&emsp;&emsp;"graduation_date": "2024"
    }
  <br>],
  <br>"Projects": [
    <br>&emsp;&emsp;&emsp;{
        "name": "Ecommerce API",
      <br>&emsp;&emsp;&emsp;"Description": "Open-soure Ecom API anyone can use for their project",
      <br>&emsp;&emsp;&emsp;"Link": "<a href='https://github.com/deepgohil/Ecom-API'>Github</a>"
    },
    <br>&emsp;&emsp;&emsp;{
      "name": "CI/CD for serverless applications",
      <br>&emsp;&emsp;&emsp;"Description": "github actions to build CI/CD pipelines for serverless applications",
      <br>&emsp;&emsp;&emsp;"Link": "<a href='https://github.com/deepgohil/pyLambdaCICDGithub.git'>Github</a>"
  
    },
        <br>&emsp;&emsp;&emsp;{
      "name": "Strees Detector",
      <br>&emsp;&emsp;&emsp;"Description": "Analysis of all parameters contributing to stress and made an API to check stress level",
      <br>&emsp;&emsp;&emsp;"Link": "<a href='https://github.com/deepgohil/StressDetector'>Github</a>"
  
    }
  ]

 <br>"Github": "<a href='https://github.com/deepgohil/'>deepgohil</a>",
  <br>"Linkedin": "<a href='https://www.linkedin.com/in/deep-gohil-b129211b6/'>Deep gohil</a>"<br>}
</pre>""", unsafe_allow_html=True)


# st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")
