# streamlit_app.py

import streamlit as st
import pickle
import pandas as pd

# Custom CSS for background and font colors
st.markdown(
    """
    <style>
    /* Background color */
    .stApp {
        background-color: #F9DFDF;  /* Light pinkish background */
    }

    /* Main title */
    .custom-title {
        color: #003366;  /* Dark blue */
        font-size: 48px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }

    /* Subheaders (Prediction Result) */
    .custom-subheader {
        color: #003366;  /* Dark blue */
        font-size: 28px;
        font-weight: bold;
        margin-top: 20px;
    }

    /* Markdown text */
    .custom-markdown {
        color: #333333;  /* Dark gray */
        font-size: 18px;
    }

    /* Input widgets (text boxes, number inputs, selectboxes) */
    .stTextInput>div>div>input,
    .stNumberInput>div>div>input,
    .stSelectbox>div>div>div>div {
        background-color: #FBEFEF;  /* Light background for inputs */
        color: #333333;  /* Dark text inside inputs */
    }

    /* Button */
    div.stButton>button {
        background-color: #003366;
        color: #FFFFFF;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add header image
st.image("https://github.com/Afraa0506/Stroke-Risk-Predictor/blob/main/header.jpg", width=700)

# Load trained pipeline model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Stroke Risk Predictor", layout="centered")

# Title using HTML for styling
st.markdown('<div class="custom-title">Stroke Risk Prediction System</div>', unsafe_allow_html=True)

# Description
st.markdown(
    '<div class="custom-markdown">This tool predicts the likelihood of a stroke based on patient health parameters.<br>Please enter the details below.</div>',
    unsafe_allow_html=True
)

# User Input Fields
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=45)
    avg_glucose = st.number_input("Average Glucose Level", min_value=50.0, max_value=300.0, value=110.0)
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
    residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])

with col2:
    gender = st.selectbox("Gender", ["Male", "Female"])
    hypertension = st.selectbox("Hypertension", ["No", "Yes"])
    heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
    ever_married = st.selectbox("Ever Married", ["No", "Yes"])

work_type = st.selectbox("Work Type", ["children", "Govt_job", "Never_worked", "Private", "Self-employed"])
smoking_status = st.selectbox("Smoking Status", ["never smoked", "formerly smoked", "smokes", "Unknown"])

# Prepare Input for Prediction
def create_input_df():
    input_dict = {
        "gender": [gender],
        "age": [age],
        "hypertension": [1 if hypertension == "Yes" else 0],
        "heart_disease": [1 if heart_disease == "Yes" else 0],
        "ever_married": [ever_married],
        "work_type": [work_type],
        "Residence_type": [residence_type],
        "avg_glucose_level": [avg_glucose],
        "bmi": [bmi],
        "smoking_status": [smoking_status]
    }
    return pd.DataFrame(input_dict)

# Predict Button
if st.button("Predict Stroke Risk"):
    input_df = create_input_df()
    
    probability = model.predict_proba(input_df)[0][1]
    prediction = model.predict(input_df)[0]

    st.markdown('<div class="custom-subheader">Prediction Result</div>', unsafe_allow_html=True)
    if prediction == 1:
        st.error(f"High Stroke Risk Detected. Probability: {probability:.2f}")
    else:
        st.success(f"Low Stroke Risk. Probability: {probability:.2f}")

    st.markdown(
        '<div class="custom-markdown">This prediction is based on statistical modeling and should not be considered medical advice.</div>',
        unsafe_allow_html=True
    )
