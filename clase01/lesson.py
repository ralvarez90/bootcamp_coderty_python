"""CLASE 01. Introducción
"""
import sys


def example_01():
    """Muestra el uso de la función **print** en python."""
    msg: str = 'Hello World in Python3'
    print(msg, file=sys.stdout)


def example_02():
    """Imprime algunas de las librerías más populares de python."""
    content: str = """Librerías Populares en Python:
    \r- Numpy
    \r- Pandas
    \r- Matplotlib y Seaborn
    \r- Scikit-learn
    \r- TensorFlow y PyTorch
    \r- Django y Flask
    \r- Requests
    \r- BeautifulSoap
    \r- SQLAlchemy
    """
    print(content)


def example_03():
    """Lista de manera general el flujo básico de un análisis de datos."""
    content: str = """Flujo Básico de un Análisis de Datos
    \r- Importación de Librerías
    \r- Carga y Limpieza de Datos
    \r- Exploración de Datos
    \r- Transformación y Modelado
    \r- Interpretación y Visualización
    """
    print(content)


def main():
    example_01() or print()
    example_02() or print()
    example_03() or print()


if __name__ == '__main__':
    main()
