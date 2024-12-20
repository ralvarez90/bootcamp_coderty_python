"""LEE LA INFORMACIÓN Y LA PROCESA
"""
import pandas as pd
import requests
import time
import matplotlib.pyplot as plt
import streamlit as st

# almacén de información leida
data = []

# streamlit page config
st.set_page_config(page_title='Análisis en Tiempo Real', layout='wide')
st.title('Sensores en tiempo real de la 🌡 para las 🍏s')

st.markdown("""
Este dashboard muestra un análisis de datos en tiempo real del simulador de la temperatura.
""")

placeholder = st.empty()


def get_sensor_data():
    """Obtiene la información del sensor."""
    try:
        response = requests.get('http://127.0.0.1:5000/get_temperature')
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        st.error(f'Error leyendo el sensor: {e}')


# inicia ciclo para leer datos
while True:
    sensor_data = get_sensor_data()
    if sensor_data:
        data.append(sensor_data)
        df = pd.DataFrame(data)
        df['temperature'] = df['temperature'].astype(float)
        df['timestamp'] = pd.to_datetime(df['timestamp'])

        # variable con información máxima
        max_temp = df['temperature'].max()
        min_temp = df['temperature'].min()
        avg_temp = df['temperature'].mean()

        with placeholder.container():
            st.subheader('Estadísticas Principales')

            col1, col2, col3 = st.columns(3)
            col1.metric('Temperatura Máxima', f'{max_temp:.2f} °C')
            col2.metric('Temperatura Mínima', f'{min_temp:.2f} °C')
            col3.metric('Temperatura Promedio', f'{avg_temp:.2f} °C')

            st.subheader('Tabla de Datos')
            st.dataframe(df.tail(10))

            st.subheader('Gráficos para el sensor de temperatura')
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(df['timestamp'], df['temperature'], label='Temperatura', color='skyblue')
            ax.axhline(max_temp, color='red', linestyle='--', label='Máxima')
            ax.axhline(min_temp, color='blue', linestyle='--', label='Minima')
            ax.set_xlabel('Tiempo')
            ax.set_ylabel('Temperatura (°C)')
            ax.legend()
            st.pyplot(fig)

        # pausa la ejecución
        time.sleep(2)
