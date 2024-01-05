import streamlit as st
import pickle

st.title("OCR_Project")
st.write("This project will help you to identify every alphanumeric digit in number placet vehicle")
image_uploaded= st.file_uploader("Upload Your Image")
if image_uploaded is not None:
    st.image(image_uploaded)
    

def predict_ocr(image_uploaded):
    pass