import streamlit as st
import pandas as pd
import numpy as np
import joblib


model = joblib.load("customer_segmentation_model.pkl")

st.title("Customer Segmentation App")
st.markdown("Built using KMeans clustering on demographic and purchasing behavior features.")
st.write("Enter customer details to predict their segment")

age = st.number_input("Age", 18, 100, 35)
income = st.number_input("Income", 0, 95000, 50000)
total_spending = st.number_input("Total Spending", 0, 5000, 1000)
num_web_purchases = st.number_input("Number of Web Purchases", 0, 100, 10)
num_store_purchases = st.number_input("Number of Store Purchases", 0, 100, 10)
num_web_visits = st.number_input("Number of Web Visits Per Month", 0, 50, 3)
recency = st.number_input("Recency (days since last purchase)", 0, 365, 30)

input_data = pd.DataFrame({
    "Age": [age],
    "Income": [income],
    "total_spending": [total_spending],
    "NumWebPurchases": [num_web_purchases],
    "NumStorePurchases": [num_store_purchases],
    "NumWebVisitsMonth": [num_web_visits],
    "Recency": [recency]
})

segment_names = {
    0: "Price-Sensitive Occasional Buyers",
    1: "Premium Loyal Customers",
    2: "Low-Engagement Budget Customers",
    3: "Digital-First High-Value Shoppers"
}

if st.button("Predict Segment"):
    cluster_label = model.predict(input_data)[0]
    predicted_segment = segment_names.get(cluster_label, "Unknown Segment")
    
    st.success(f"Predicted Customer Segment: {predicted_segment}")

    st.markdown("### Segment Descriptions")
    for key, value in segment_names.items():
        st.write(f"{key}: {value}")