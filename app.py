import streamlit as st
import pandas as pd
import prediction
from combined_attributes_adder import CombinedAttributesAdder
from sklearn.base import BaseEstimator, TransformerMixin

st.title('Real-Estate-Value')

with st.sidebar:
    st.write("Enter Geographic Information:")
    longitude = st.number_input('Length', min_value = -124.0, max_value = -110.0, format = "%.2f")
    latitude = st.number_input('Latitude', min_value = 30.0, max_value = 50.0, format = "%.2f")
    total_rooms = st.number_input('Total Rooms', min_value = 1.0, max_value = 50000.0, format = "%.0f")
    total_bedrooms = st.number_input('Total Bedrooms', min_value = 1.0, max_value = 7000.0, format = "%.0f")

with st.sidebar:
    population = st.number_input('Population', min_value = 1.0, max_value = 50000.0, format = "%.0f")
    ocean_proximity = st.selectbox('Ocean Proximity', ['<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR BAY', 'ISLAND'])

with st.sidebar:
    households = st.number_input('Households', min_value = 1.0, max_value = 10000.0, format = "%.0f")
    housing_median_age = st.number_input('Housing median age', step=1.0, min_value=1.0, max_value=100.0, format = "%.0f")
    median_income = st.number_input('Average income', min_value = 0.0, max_value = 17.0, format = "%.4f")

model = 'Random Forest Regression'

if st.button('PREDICTION'):
    data = pd.DataFrame({
        'longitude': [longitude],
        'latitude': [latitude],
        'housing_median_age': [housing_median_age],
        'total_rooms': [total_rooms],
        'total_bedrooms': [total_bedrooms],
        'population': [population],
        'households': [households],
        'median_income': [median_income],
        'ocean_proximity': [ocean_proximity]})

    result = prediction.predict(data, model)

    st.markdown('**Prediction:**')
    st.write("$ {:.1f} dlls".format(result[0]))
