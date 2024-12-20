"""SISTEMA DE VENTAS
matplotlib
pip install reportlab
"""
import csv
import os
from datetime import datetime
from collections import defaultdict

import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def cargar_datos(archivo: str) -> dict | None:
    ventas_x_dia: dict = defaultdict(float)
    try:
        with open(archivo, mode='r') as file:
            lector = csv.DictReader(file)
            for fila in lector:
                fecha = datetime.strptime(fila['fecha_compra'], '%d-%m-%Y')
                dia_semana = fecha.strftime('%A')
                monto = float(fila['monto_total'])
                ventas_x_dia[dia_semana] += monto
    except Exception as e:
        print(f'Error al leer el archivo: {e}')
        return

    return ventas_x_dia


def generar_grafico(ventas_x_dia: dict, archivo_grafico: str):
    # datos a graficar
    dias = list(ventas_x_dia.keys())
    ventas = list(ventas_x_dia.values())

    # géneramos figura
    plt.figure(figsize=(8, 6))
    plt.bar(dias, ventas, color='skyblue')
    plt.xlabel('Día de la Semana')
    plt.ylabel('Total de Ventas ($)')
    plt.title('Ventas X Día de la Semana')
    plt.savefig(archivo_grafico)
    plt.close()


def generar_pdf(archivo_csv: str, archivo_pdf: str) -> None:
    ventas_x_dia = cargar_datos(archivo_csv)
    if not ventas_x_dia:
        print('No se pudo procesar el archivo csv.')
        return

    total_ventas = sum(ventas_x_dia.values())
    dia_mayor_ventas = max(ventas_x_dia, key=ventas_x_dia.get)

    archivo_grafico = 'temporal.png'
    generar_grafico(ventas_x_dia, archivo_grafico)

    # configurar pdf
    c = canvas.Canvas(archivo_pdf, pagesize=letter)
    ancho, alto = letter
    c.setFont('Helvetica-Bold', 16)
    c.drawString(100, alto - 80, "Reporte de Ventas")

    # datos analíticos
    c.setFont("Helvetica", 12)
    c.drawString(100, alto - 120, f'Día con mayores ventas: {dia_mayor_ventas}')
    c.drawString(100, alto - 140, f'Ventas totales: ${total_ventas:,.2f}')

    # inserción de gráficos en pdf
    c.drawString(100, alto - 180, 'Gráfico de ventas por día de la semana:')
    c.drawImage(archivo_grafico, 100, alto - 500, width=400, height=300)

    # guardar y cerrar pdf
    c.save()

    # eliminamos archivo temporal
    os.remove(archivo_grafico)
    print(f'Reporte PDF generado exitosamente: "{archivo_pdf}"')


def main():
    archivo_ventas: str = os.getcwd() + os.sep + 'ventas.csv'
    archivo_pdf: str = os.getcwd() + os.sep + 'Reporte_de_ventas.pdf'
    generar_pdf(archivo_ventas, archivo_pdf)


if __name__ == '__main__':
    main()
