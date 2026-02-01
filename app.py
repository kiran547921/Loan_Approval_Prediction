import streamlit as st
import pandas as pd

import joblib

# Load trained model
model = joblib.load("loan_knn_model.pkl")

st.set_page_config(page_title="Loan Approval Predictor",layout='centered')
st.title("Loan Approval Prediction")
st.write("Enter application details to predict loan approval")
Gender = st.selectbox("Gender", ["Male", "Female"])
Married = st.selectbox("Married", ["Yes", "No"])
Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
Credit_History = st.selectbox("Credit History", [1.0, 0.0])

CoapplicantIncome = st.number_input("CoApplicant Income",min_value=0.0,value=None,placeholder="Enter coapplicant income")
ApplicantIncome = st.number_input("Applicant Income", min_value=0.0,value=None,placeholder="Enter Applicant income")
LoanAmount = st.number_input("Loan Amount", min_value=0.0,value=None,placeholder="Enter Loan amount")
Loan_Amount_Term = st.number_input("Loan Amount Term", min_value=12.0,max_value=420.0)

if st.button("Predict Loan Status"):
    input_df = pd.DataFrame([{
        "Gender": Gender,
        "Married": Married,
        "Self_Employed": Self_Employed,
        "Education": Education,
        "Property_Area": Property_Area,
        "Credit_History": Credit_History,
        "ApplicantIncome": ApplicantIncome,
        "CoapplicantIncome": CoapplicantIncome,
        "LoanAmount": LoanAmount,
        "Loan_Amount_Term": Loan_Amount_Term
    }])

    prediction = model.predict(input_df)[0]

    if prediction == "Y":
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Not Approved")