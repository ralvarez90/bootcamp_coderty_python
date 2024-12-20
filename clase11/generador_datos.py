from pprint import pprint

import pandas as pd
import random


def generar_datos_aleatorios(cantidad: int):
    products = ['Laptop', 'Mouse', 'Teclado', 'Monitor']

    data = {
        'Fecha': pd.date_range(start='2024-09-01', periods=cantidad).strftime('%Y-%m-%d').tolist(),
        'Producto': [random.choice(products) for _ in range(cantidad)],
        'Cantidad': random.randint(1, 10),
        'Precio_unitario': [random.randint(20, 1000) for _ in range(cantidad)],
        'Departamento': ['Tecnología'] * cantidad,
    }

    df = pd.DataFrame(data)
    df.to_excel('reporte_ventas.xlsx', index=False, sheet_name='ventas')


"""Generar otra info, en mismo excel pero en otra hoja"""
if __name__ == '__main__':
    cantidad_datos = 45
    generar_datos_aleatorios(cantidad_datos)
