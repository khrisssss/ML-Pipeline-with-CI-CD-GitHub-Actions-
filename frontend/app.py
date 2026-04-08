import streamlit as st
import joblib
import requests

backend_url = "http://localhost:8000"

st.title(":violet[_Iris Classification_]")

number1 = st.number_input(
    "Sepal Length (cm)", value=None, placeholder="Type a number..."
)

number2 = st.number_input(
    "Sepal Width (cm)", value=None, placeholder="Type a number..."
)

number3 = st.number_input(
    "Petal Length (cm)", value=None, placeholder="Type a number..."
)

number4 = st.number_input(
    "Petal Width (cm)", value=None, placeholder="Type a number..."
)

if st.button("Predict"):
    item = {
        "SepalLengthCm": number1,
        "SepalWidthCm": number2,
        "PetalLengthCm": number3,
        "PetalWidthCm": number4
    }

    response = requests.post(f"{backend_url}/predict", json=item)
    if response.status_code == 200:
        prediction = response.json().get("prediction")
        st.success(f"Predicted class: {prediction}")
    else:
        st.error("Error occurred while making the prediction.")


css="""
<style>
    .stButton>button {
        background-color: #FFC0CB;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #FF69B4;
    }
    .stButton>button:active {
        position: relative;
        top: 3px;
    }
    
</style>
"""
st.markdown(css, unsafe_allow_html=True)