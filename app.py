import streamlit as st
import joblib

# Load model
model = joblib.load("model.pkl")  # Make sure this file is in the same directory

# Streamlit UI
st.title("Customer Segment Predictor")

# Adjust the number of inputs based on your model
feature1 = st.number_input("Enter Age", value=0.0)
feature2 = st.number_input("Enter Annual Income(k$)", value=0.0)
feature3 = st.number_input("Enter Spending Score(1-100)", value=0.0)

if st.button("Predict"):
    features = [[feature1, feature2,feature3]]  # Update based on model input shape
    prediction = model.predict(features)
    st.success(f"Prediction: Cluster-{prediction[0]+1}")
