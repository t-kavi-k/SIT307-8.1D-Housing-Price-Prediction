import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page setup
st.set_page_config(
    page_title="Sydney Housing Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# Load the trained model
model = joblib.load("housing_price_model.pkl")

# App title
st.title("Sydney Housing Price Predictor")

st.write(
    "Enter the property details below to estimate its sale price. "
    "This model was developed using property data from Parramatta, "
    "Blacktown and Bondi."
)

# Property information
suburb = st.selectbox(
    "Suburb",
    ["Parramatta", "Blacktown", "Bondi"]
)

property_type = st.selectbox(
    "Property Type",
    ["Apartment", "House", "Townhouse", "Semi-detached", "Studio"]
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=0,
    max_value=10,
    value=2,
    step=1
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=0,
    max_value=10,
    value=1,
    step=1
)

car_spaces = st.number_input(
    "Car Spaces",
    min_value=0,
    max_value=10,
    value=1,
    step=1
)

property_size = st.number_input(
    "Property Size (m²)",
    min_value=0.0,
    value=100.0,
    step=10.0
)

sale_year = st.selectbox(
    "Sale Year",
    [2025, 2026],
    index=1
)

sale_month = st.selectbox(
    "Sale Month",
    list(range(1, 13)),
    index=8
)

# Automatically create engineered features
total_rooms = bedrooms + bathrooms
has_parking = 1 if car_spaces > 0 else 0

# Prediction button
if st.button("Predict Sale Price"):

    input_data = pd.DataFrame({
        "suburb": [suburb],
        "property_type": [property_type],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "car_spaces": [car_spaces],
        "property_size_m2": [property_size],
        "sale_year": [sale_year],
        "sale_month_num": [sale_month],
        "total_rooms": [total_rooms],
        "has_parking": [has_parking]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Sale Price: AUD {prediction:,.0f}"
    )

    st.caption(
        "This prediction is an estimate based on the collected dataset "
        "and should not be treated as a professional property valuation."
    )