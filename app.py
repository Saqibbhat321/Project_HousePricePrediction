import streamlit as st
import pickle
import numpy as np

with open("house_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("House Price Prediction")

area = st.number_input(
    "Area (sq ft)",
    min_value=500,
    max_value=10000,
    value=1500
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

age = st.number_input(
    "Age of House",
    min_value=0,
    max_value=50,
    value=5
)

if st.button("Predict Price"):

    features = np.array([
        [area, bedrooms, bathrooms, age]
    ])

    prediction = model.predict(features)

    st.success(
        f"Estimated House Price: ${prediction[0]:,.2f}"
    )