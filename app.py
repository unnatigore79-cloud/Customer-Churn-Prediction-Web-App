import streamlit as st
import pickle
import numpy as np

with open('churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("📊 Customer Churn Prediction Web App")
st.write("Predict whether a customer is likely to churn or stay based on subscription patterns.")

st.sidebar.header("Customer Details")
tenure = st.sidebar.slider("Tenure (Months)", 1, 72, 12)
monthly = st.sidebar.number_input("Monthly Charges ($)", 20.0, 120.0, 65.0)
total = st.sidebar.number_input("Total Charges ($)", 100.0, 8000.0, 1500.0)
contract = st.sidebar.selectbox("Contract Type", ["Month-to-Month", "One Year", "Two Year"])
tech = st.sidebar.radio("Has Tech Support?", ["No", "Yes"])

contract_map = {"Month-to-Month": 0, "One Year": 1, "Two Year": 2}
tech_map = {"No": 0, "Yes": 1}

if st.button("Predict Churn Risk"):
    features = np.array([[tenure, monthly, total, contract_map[contract], tech_map[tech]]])
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.error("🚨 High Risk: Customer is likely to Churn!")
    else:
        st.success("✅ Low Risk: Customer is likely to Stay Retained.")
