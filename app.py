from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st
from PIL import Image

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")


genai.configure(api_key=API_KEY)

def get_gemini_response(input_message,input_image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if input_message != "":
        response = model.generate_content([input_message,input_image])
    else:
        response = model.generate_content(input_image)
    return response.text

st.set_page_config(page_title="Gemini based chatbot")
st.header("Gemini LLM Application")

st.markdown("""
    <style>
        body {
            background-color: #0b0c10;
            color: #c5c6c7;
            font-family: 'Roboto', sans-serif;
        }
        .main {
            background-color: #C0C78C;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0, 255, 0, 0.4);
        }
        .stButton button {
            background-color: #B99470;
            color: #0b0c10;
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 16px;
            border: none;
            font-weight: bold;
            transition: background-color 0.3s ease;
            font-family: 'Roboto', sans-serif;
        }
        .stButton button:hover {
            background-color: #A6B37D;
            color: #ffffff;
        }
        h1 {
            color: #66fcf1;
            text-align: center;
            font-family: 'Orbitron', sans-serif;
            margin-bottom: 20px;
            text-shadow: 0px 0px 5px #66fcf1;
        }
        .stTextInput input {
            border-radius: 5px;
            border: 1px solid #45a049;
            padding: 10px;
            background-color: #B99470;
            color: #c5c6c7;
            font-family: 'Roboto', sans-serif;
        }
        .stFileUploader label {
            color: #66fcf1;
            font-family: 'Roboto', sans-serif;
        }
        .uploaded-image {
            border: 2px solid #66fcf1;
            border-radius: 10px;
            margin-top: 10px;
            box-shadow: 0px 0px 15px rgba(102, 252, 241, 0.7);
        }
    </style>
""", unsafe_allow_html=True)

input = st.text_input("Input Prompt : ",key="Input")
uploaded_file = st.file_uploader("choose an image : ",type=['jpg',"jpeg","png"])

image =""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="uploaded image")

button = st.button("Click me")
if button:
    response = get_gemini_response(input_message=input,input_image=image)
    st.subheader("Your result!!")
    st.write(response)