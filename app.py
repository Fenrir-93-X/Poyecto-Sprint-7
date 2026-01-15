import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.title('Visualizador Interactivo de Datos de Vehículos')

# Selección de tipo de gráfico
graph_type = st.selectbox(
    'Selecciona el tipo de gráfico:',
    ['Histograma', 'Gráfico de Dispersión', 'Diagrama de Barras']
)

# Selección de columnas según el tipo de gráfico
if graph_type == 'Histograma':
    column = st.selectbox('Selecciona la columna:', car_data.select_dtypes(include=['number']).columns)
    if st.button('Generar Histograma'):
        fig = px.histogram(car_data, x=column, title=f'Histograma de {column}')
        st.plotly_chart(fig, use_container_width=True)

elif graph_type == 'Gráfico de Dispersión':
    col1, col2 = st.columns(2)
    with col1:
        x_column = st.selectbox('Eje X:', car_data.select_dtypes(include=['number']).columns)
    with col2:
        y_column = st.selectbox('Eje Y:', car_data.select_dtypes(include=['number']).columns)
    
    if st.button('Generar Gráfico de Dispersión'):
        fig = px.scatter(car_data, x=x_column, y=y_column, 
                        title=f'{x_column} vs {y_column}')
        st.plotly_chart(fig, use_container_width=True)

elif graph_type == 'Diagrama de Barras':
    column = st.selectbox('Selecciona la columna categórica:', 
                         car_data.select_dtypes(include=['object']).columns)
    if st.button('Generar Diagrama de Barras'):
        top_categories = car_data[column].value_counts().head(10)
        fig = px.bar(x=top_categories.index, y=top_categories.values,
                    title=f'Top 10 categorías de {column}')
        st.plotly_chart(fig, use_container_width=True)
