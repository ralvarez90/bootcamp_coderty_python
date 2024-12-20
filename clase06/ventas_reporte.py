from pprint import pprint

import pandas as pd
import matplotlib.pyplot as plt

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors


def main():
    """PREGUNTAS A RESPONDER
    1.- Ventas por región
    2.- Ventas por producto
    3.- Ventas por fecha
    """

    # retorna un dataframe
    df = pd.read_csv('ventas_reporte.csv')

    # convertimos fecha de string a datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])

    # agrupaciones
    ventas_por_region = df.groupby(by='Region')['Ventas'].sum()
    ventas_por_producto = df.groupby(by='Producto')['Ventas'].sum()
    ventas_por_fecha = df.groupby(by='Fecha')['Ventas'].sum()
    producto_mas_vendido = ventas_por_producto.idxmax()

    # gráfico, ventas por región
    colors_bar = plt.cm.Paired(range(len(ventas_por_region)))
    plt.figure(figsize=(8, 6))
    ventas_por_region.plot(kind='bar', color=colors_bar, title='Ventas por región')
    plt.xlabel('Región')
    plt.ylabel('Ventas')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('grafica1.png')
    plt.close()

    # gráfico, ventas por tiempo
    plt.figure(figsize=(8, 6))
    ventas_por_fecha.plot(marker='o', color='green', title='Ventas por fecha')
    plt.xlabel('Fecha')
    plt.ylabel('Ventas')
    plt.tight_layout()
    plt.savefig('grafica2.png')
    plt.close()

    # creación de pdf
    pdf_path = 'Resultado_analisis_ventas.pdf'
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont('Helvetica', 10)

    # título del documento
    c.setFont('Helvetica-Bold', 16)
    c.drawString(x=30, y=750, text='Análisis de Ventas')

    # descripción de los datos
    c.setFont('Helvetica', 10)
    c.drawString(x=30, y=730, text='Análisis de ventas por región y productos basados en el archivo ventas_reporte.csv')
    c.drawString(x=30, y=715, text=f'Producto más vendido: {producto_mas_vendido}')

    # tabla con resultados
    data_region = [['Región', 'Ventas']] + [[region, ventas] for region, ventas in ventas_por_region.items()]
    tabla_region = Table(data_region)
    tabla_region.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    tabla_region.wrapOn(c, 30, 500)
    tabla_region.drawOn(c, 30, 600)

    # segunda tablA
    data_producto = [['Producto', 'Ventas']] + [[producto, ventas] for producto, ventas in ventas_por_region.items()]
    tabla_producto = Table(data_producto)
    tabla_producto.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    tabla_producto.wrapOn(c, 300, 500)
    tabla_producto.drawOn(c, 300, 600)

    # insertamos gráficos
    c.drawImage('grafica1.png', 50, 400, width=250, height=200)
    c.drawImage('grafica2.png', 300, 400, width=250, height=200)

    # se salva pdf
    c.save()
    print('PDF Generado!')


if __name__ == '__main__':
    main()
