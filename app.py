import streamlit as st
import pandas as pd
import prediction
from combined_attributes_adder import CombinedAttributesAdder
from sklearn.base import BaseEstimator, TransformerMixin

st.title('California Housing Prices Estimator')

col1, col2 = st.columns(2)
with st.container():
    st.write("Ingrese la Información Geográfica")
    longitude = col1.number_input('Longitud', min_value = -124.0, max_value = -110.0, format = "%.2f")
    latitude = col1.number_input('Latitud', min_value = 30.0, max_value = 50.0, format = "%.2f")
    total_rooms = col1.number_input('Total de habitaciones', min_value = 1.0, max_value = 50000.0, format = "%.0f")
    total_bedrooms = col1.number_input('Total de dormitorios', min_value = 1.0, max_value = 7000.0, format = "%.0f")

with st.container():
    population = col2.number_input('Población', min_value = 1.0, max_value = 50000.0, format = "%.0f")
    ocean_proximity = col2.selectbox('Ocean Proximity', ['<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR BAY', 'ISLAND'])


with st.container():
    households = col2.number_input('Hogares / Households', min_value = 1.0, max_value = 10000.0, format = "%.0f")
    housing_median_age = col2.number_input('Promedio de edad de vivienda / Housing median age', step=1.0, min_value=1.0, max_value=100.0, format = "%.0f")
    median_income = col2.number_input('Ingreso Promedio /Median income', min_value = 0.0, max_value = 17.0, format = "%.4f")

with st.container():
    model = 'Random Forest Regression'

    if st.button('Hacer prediccion'):
        data = pd.DataFrame({
            'longitude': [longitude],
            'latitude': [latitude],
            'housing_median_age': [housing_median_age],
            'total_rooms': [total_rooms],
            'total_bedrooms': [total_bedrooms],
            'population': [population],
            'households': [households],
            'median_income': [median_income],
            'ocean_proximity': [ocean_proximity]}
        )

        result = prediction.predict(data, model)
        st.write("Valor predecido es de {:.1f} dlls".format(result[0]))