
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

# =========================
# Page Configuration
# =========================
st.set_page_config(
    page_title="Train Journey Duration Predictor",
    page_icon="🚆",
    layout="wide"
)

# =========================
# Load Model
# =========================
with open("train_journey_model.pkl", "rb") as file:
    model = pickle.load(file)

# =========================
# Title
# =========================
st.title("🚆 Train Journey Duration Prediction System")
st.markdown(
'''
Predict train journey duration using a Machine Learning model
trained on railway route and schedule data.
'''
)

# =========================
# Sidebar Inputs
# =========================
st.sidebar.header("Journey Details")

distance = st.sidebar.number_input(
    "Total Distance (km)",
    min_value=1.0,
    value=500.0,
    step=10.0
)

stops = st.sidebar.number_input(
    "Number of Stops",
    min_value=0,
    value=5,
    step=1
)

departure_hour = st.sidebar.slider(
    "Departure Hour",
    0,
    23,
    8
)

arrival_hour = st.sidebar.slider(
    "Arrival Hour",
    0,
    23,
    18
)

# =========================
# Feature Engineering
# =========================
distance_per_stop = (
    distance / stops
    if stops > 0
    else distance
)

# =========================
# Prediction Button
# =========================
if st.sidebar.button("Predict Journey Duration"):

    input_data = pd.DataFrame({
        'Total_Distance': [distance],
        'Num_Stops': [stops],
        'Departure_Hour': [departure_hour],
        'Arrival_Hour': [arrival_hour],
        'Distance_Per_Stop': [distance_per_stop]
    })

    prediction = model.predict(input_data)[0]

    # =========================
    # Results
    # =========================
    st.subheader("Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Predicted Duration (Hours)",
            f"{prediction:.2f}"
        )

    with col2:
        hours = int(prediction)
        minutes = int((prediction - hours) * 60)

        st.metric(
            "Estimated Travel Time",
            f"{hours}h {minutes}m"
        )

    # =========================
    # Input Summary
    # =========================
    st.subheader("Journey Details")

    summary_df = pd.DataFrame({
        "Feature": [
            "Total Distance",
            "Number of Stops",
            "Departure Hour",
            "Arrival Hour",
            "Distance Per Stop"
        ],
        "Value": [
            distance,
            stops,
            departure_hour,
            arrival_hour,
            round(distance_per_stop, 2)
        ]
    })

    st.dataframe(summary_df, use_container_width=True)

    # =========================
    # Visualization
    # =========================
    st.subheader("Predicted Journey Duration Visualization")

    fig, ax = plt.subplots(figsize=(6,4))

    ax.bar(
        ["Predicted Duration"],
        [prediction]
    )

    ax.set_ylabel("Hours")
    ax.set_title("Predicted Journey Duration")

    st.pyplot(fig)

# =========================
# About Model
# =========================
st.markdown("---")

st.subheader("Model Information")

st.info(
'''
Model: Linear Regression

Features Used:
- Total Distance
- Number of Stops
- Departure Hour
- Arrival Hour
- Distance Per Stop

Target Variable:
- Journey Duration (Hours)

Developed as part of the Machine Learning-Based Train Journey Time Prediction System.
'''
)
