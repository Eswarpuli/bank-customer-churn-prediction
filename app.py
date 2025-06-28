import streamlit as st
import pandas as pd
import joblib

st.title("📊 Bank Customer Churn Prediction")

# Load the model
model = joblib.load("random_forest_churn_model.pkl")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file with customer data", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("📋 Uploaded Data Preview:")
    st.dataframe(data)

    if st.button("Predict Churn"):
        predictions = model.predict(data)
        data['Churn Prediction'] = ["Yes" if val == 1 else "No" for val in predictions]
        st.success("✅ Prediction Complete")
        st.write(data[['Churn Prediction']])
