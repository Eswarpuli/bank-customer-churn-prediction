# 📊 Bank Customer Churn Prediction (ML Web App)

🔗 [Live Demo on Streamlit Cloud](https://bank-customer-churn-prediction-ntkv6yrvgjsuibraonv8ub.streamlit.app/)

This project is a machine learning web application that predicts whether a bank customer is likely to churn. The app is built using **Streamlit** and powered by a **Random Forest classifier** trained on customer data.

---

## 🚀 Features

- Upload a CSV file containing customer data
- Predict churn using a trained ML model
- View predictions in a simple web interface
- Reusable `.pkl` model for fast inference
- Organized project structure with dataset included

---

## 📂 Project Structure

bank-customer-churn-prediction/
│
├── app.py # Streamlit app
├── random_forest_churn_model.pkl # Trained ML model
├── requirements.txt # Required Python libraries
├── README.md # Project documentation
├── streamlit_ui.png # Screenshot of the app
├── dataset/ # Folder containing data files
│ ├── churn_data.xlsx # Dataset used for training
│ └── sample_input.xlsx # Sample file for upload testing


---

##  Model Overview

I trained multiple classification models including:
- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest ✅

**Random Forest** gave the best performance:
- Accuracy: **85%**
- Precision: **83%**
- Recall: **81%**

So it was selected for final deployment.

---

## 🧰 Tech Stack

- **Python**
- **Pandas, Scikit-learn**
- **Streamlit**
- **Joblib**

---


## Dataset
The dataset includes customer demographic details, account activity, and churn labels.
It's located in the dataset/ folder:

churn_data.xlsx – Used for training

sample_input.xlsx – Used for testing with the app




