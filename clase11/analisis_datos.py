# app_analizar_datos.py
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet


@st.cache_data
def cargar_datos():
    return pd.read_excel("reporte_ventas.xlsx", sheet_name="Ventas")


def generar_pdf(resumen_producto, ventas_totales, ventas_por_dia):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elementos = []

    estilos = getSampleStyleSheet()
    estilo_titulo = estilos["Heading1"]

    elementos.append(Paragraph("Reporte de Ventas", estilo_titulo))

    # Tabla de resultados
    tabla_datos = [resumen_producto.columns.tolist()] + resumen_producto.values.tolist()
    tabla = Table(tabla_datos)
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elementos.append(tabla)
    doc.build(elementos)
    buffer.seek(0)
    return buffer


st.title("Análisis de Ventas en Tiempo Real")
df_ventas = cargar_datos()

# Procesamiento de datos
df_ventas['Total Venta'] = df_ventas['Cantidad'] * df_ventas['Precio Unitario']

# Resumen por producto
resumen_producto = df_ventas.groupby("Producto").agg(
    Total_Ventas=('Total Venta', 'sum'),
    Cantidad_Vendida=('Cantidad', 'sum')
).reset_index()

# Producto más y menos vendido
producto_mas_vendido = resumen_producto.loc[resumen_producto['Cantidad_Vendida'].idxmax()]
producto_menos_vendido = resumen_producto.loc[resumen_producto['Cantidad_Vendida'].idxmin()]

# Resumen general
ventas_totales = df_ventas['Total Venta'].sum()
ventas_por_dia = df_ventas.groupby("Fecha")["Total Venta"].sum().reset_index()

# Mostrar resultados en Streamlit
st.subheader("Reporte de Ventas por Producto")
st.dataframe(resumen_producto)

st.subheader("Ventas Totales")
st.write(ventas_totales)

st.subheader("Ventas por Día")
st.dataframe(ventas_por_dia)

st.subheader("Producto Más Vendido")
st.write(producto_mas_vendido.to_dict())

st.subheader("Producto Menos Vendido")
st.write(producto_menos_vendido.to_dict())

# Gráficos
fig, ax = plt.subplots(figsize=(8, 6))
resumen_producto.plot(kind="bar", x="Producto", y="Total_Ventas", ax=ax, color="skyblue")
st.pyplot(fig)

# Botón para descargar el PDF
if st.button("Descargar Reporte en PDF"):
    pdf_buffer = generar_pdf(resumen_producto, ventas_totales, ventas_por_dia)
    st.download_button(
        label="Descargar PDF",
        data=pdf_buffer,
        file_name="reporte_ventas.pdf",
        mime="application/pdf"
    )
