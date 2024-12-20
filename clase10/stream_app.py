import streamlit as st
import pandas as pd
import requests
import time
import matplotlib.pyplot as plt
from io import BytesIO

st.set_page_config(page_title="Monitor de sensores", layout='wide')
st.title("Monitor de Temperatura y Humedad")

is_running = st.session_state.get('is_running', False)
data = st.session_state.get('data', pd.DataFrame(columns=["Timestamp", "Temperatura", "Humedad"]))


def fetch_data():
    try:
        response = requests.get("http://127.0.0.1:5000")
        if response.status_code == 200:
            sensor_data = response.json()
            return {
                "Timestamp": pd.Timestamp.now(),
                "Temperatura": sensor_data['temperature'],
                "Humedad": sensor_data["humidity"]
            }
    except Exception as e:
        st.error(f"Error al obtener datos: {e}")
    return None


def analyze_data(df):
    st.subheader("Análisis de Datos")
    st.write(df.describe())

    fig, ax = plt.subplots(2, 1, figsize=(10, 8))

    ax[0].plot(df['Timestamp'], df['Temperatura'], color="red", label="Temperatura ºC")
    ax[0].set_title('Evolución de la temperatura')
    ax[0].legend()

    ax[1].plot(df['Timestamp'], df['Humedad'], color="blue", label="Humedad %")
    ax[1].set_title("Evolucion de la humedad")
    ax[1].legend()

    st.pyplot(fig)


def generate_pdf(df):
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Reporte de sensores", ln=True, align='C')
    pdf.cell(200, 10, txt=f'Generado: {pd.Timestamp.now()}', ln=True, align='C')

    pdf.ln(10)
    for line in df.describe().to_string().split('\n'):
        pdf.cell(200, 10, txt=line, ln=True)

    pdf_file = BytesIO()
    pdf.output()
    pdf_file.seek(0)
    return pdf_file


st.sidebar.header("Controles")
start_button = st.sidebar.button("Iniciar")
pause_button = st.sidebar.button("Pausar")
export_pdf = st.sidebar.button("Exportar a PDF")

if start_button:
    st.session_state.is_running = True

if pause_button:
    st.session_state.is_running = False

if is_running:
    with st.spinner("Recibinedo datos del sensor"):
        new_data = fetch_data()
        if new_data:
            data = pd.concat([data, pd.DataFrame([new_data])], ignore_index=True)
            st.session_state.data = data
        time.sleep(2)

if not data.empty:
    st.subheader("Datos Recibidos")
    st.dataframe(data)
    analyze_data(data)

if export_pdf:
    if not data.empty:
        pdf = generate_pdf(data)
        st.sidebar.download_button("Descargar PDF", pdf, "Reporte_sensor.pdf")
    else:
        st.sidebar.error("No hay datos para exportar.")
