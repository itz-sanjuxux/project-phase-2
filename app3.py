
import streamlit as st
import pickle
import numpy as np

# Load your trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("🔒 Credit Card Fraud Detection")

# Input fields
v1 = st.number_input("Enter V1")
v2 = st.number_input("Enter V2")
amount = st.number_input("Transaction Amount")

if st.button("Predict"):
    input_data = np.array([[v1, v2, amount]])
    prediction = model.predict(input_data)
    st.success("⚠️ Fraudulent Transaction" if prediction[0] == 1 else "✅ Legitimate Transaction")
