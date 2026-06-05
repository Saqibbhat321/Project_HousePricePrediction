import streamlit as st
import pickle
import pandas as pd

# Load model
with open("house_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🏠 House Price Prediction System")

area = st.number_input(
    "Area",
    min_value=500,
    max_value=20000,
    value=5000
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

stories = st.number_input(
    "Stories",
    min_value=1,
    max_value=5,
    value=2
)

mainroad = st.selectbox(
    "Main Road Access",
    ["yes", "no"]
)

guestroom = st.selectbox(
    "Guest Room",
    ["yes", "no"]
)

basement = st.selectbox(
    "Basement",
    ["yes", "no"]
)

hotwaterheating = st.selectbox(
    "Hot Water Heating",
    ["yes", "no"]
)

airconditioning = st.selectbox(
    "Air Conditioning",
    ["yes", "no"]
)

parking = st.number_input(
    "Parking Spaces",
    min_value=0,
    max_value=5,
    value=1
)

prefarea = st.selectbox(
    "Preferred Area",
    ["yes", "no"]
)

furnishingstatus = st.selectbox(
    "Furnishing Status",
    [
        "furnished",
        "semi-furnished",
        "unfurnished"
    ]
)

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "area":[area],
        "bedrooms":[bedrooms],
        "bathrooms":[bathrooms],
        "stories":[stories],
        "mainroad":[mainroad],
        "guestroom":[guestroom],
        "basement":[basement],
        "hotwaterheating":[hotwaterheating],
        "airconditioning":[airconditioning],
        "parking":[parking],
        "prefarea":[prefarea],
        "furnishingstatus":[furnishingstatus]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Estimated House Price: ₹{prediction[0]:,.0f}"
    )