import pandas as pd
import plotly.express as px
import streamlit as st

# Título
st.header('Análisis de Vehículos Usados')

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Botones en fila
col1, col2 = st.columns(2)

with col1:
    hist_button = st.button('📊 Histograma del Odómetro')

with col2:
    scatter_button = st.button('🔘 Dispersión Odómetro vs Precio')

# Histograma
if hist_button:
    st.write('**Histograma del Odómetro**')
    fig = px.histogram(car_data, x="odometer", title="Distribución del Kilometraje")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión
if scatter_button:
    st.write('**Relación entre Odómetro y Precio**')
    fig = px.scatter(car_data, x="odometer", y="price", 
                     title="Odómetro vs Precio",
                     labels={'odometer': 'Odómetro (millas)', 'price': 'Precio ($)'})
    st.plotly_chart(fig, use_container_width=True)

# Información adicional
if hist_button or scatter_button:
    st.divider()
    st.write(f'📌 **Datos del dataset:** {len(car_data)} vehículos, {len(car_data.columns)} columnas')
