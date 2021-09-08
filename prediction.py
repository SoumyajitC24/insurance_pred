import streamlit as st
from preprocess_lr import model, load_data;



def app():
    st.subheader("Select Values:")

    age = st.slider("Age" , 0 , 100)
    sex = st.radio("Sex" , ["Male" , "Female"])
    bmi = st.slider("BMI" , 10.0 , 35.0)
    children = st.slider("Children" , 0 , 10)
    smoker = st.radio("Smoker" , ["Yes" , "No"])
    region = st.selectbox("Region" , ["Northeast" , "Northwest" , "Southeast" , "Southwest"])    

    if (region == "northwest"):
        region = 0
    elif (region == "northeast"):
        region = 1
    elif (region == "southeast"):
        region = 2
    else:
        region = 3

    if (sex == "Male"):
        sex = 0
    else:
        sex = 1

    if (smoker == "No"):
        smoker = 0
    else:
        smoker = 1

    feature = [[age , sex , bmi , children , smoker , region]]

    if st.button("Predict"):
        my_model, acc = model()

        prediction = my_model.predict(feature)
        st.info(f"Our Model acc is {round(acc*100 , 2)}%")

        st.success(f"Charges value is {round(prediction[0] , 2)}")