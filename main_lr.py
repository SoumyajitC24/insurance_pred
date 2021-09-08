from pkg_resources import set_extraction_path
import streamlit as st
import prediction


st.title("My Insurance Prediction Website")
st.markdown("### The ML model uses Linear Regression Algo to make predictions")


st.sidebar.title("Navigation")
page = st.sidebar.radio("Pages" , ["Home" , "Predict Values"])

if (page == "Predict Values"):
    prediction.app()
