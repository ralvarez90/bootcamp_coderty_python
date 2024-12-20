"""CLASE 04.

1. Manejo de Archivos
Python ofrece una forma sencilla y eficiente de trabajar con archivos. Los
archivos se crean empleando la función open que recibe como parámetro
un modo.

1.1 Modo 'r'
Modo default de la función open, si no existe un archivo se lanza una
excepción FileNotFoundError.

1.2 Modo 'w'
Modo de escritura, si no existe el archivo lo crea. Si ya existe sobreescribe
el archivo.

1.3 Modo 'a'
El modo append escribe al final del archivo el nuevo contenido, es decir no
sobrescribe el archivo si ya existe. Si no existe lo genera.

1.4 Modo 'x'
Se emplea para generar un nuevo archivo, si ya existe lanza un FileExistsError.
"""

import os


def example_01_r_mode():
    name: str = 'ejemplo.txt'
    file_name: str = f'{os.getcwd()}{os.sep}{name}'
    try:
        with open(file_name, mode='r') as f:
            content: str = f.read()
            print(content)

    except FileNotFoundError:
        print(f'Archivo no encontrado: "{name}"')


def example_02_w_mode():
    name: str = 'archivo.txt'
    file_name: str = f'{os.getcwd()}{os.sep}{name}'
    with open(file_name, mode='w') as f:
        f.write("Hola Mundo desde Python3\n")
        f.write("Estamos ejemplificando el uso del modo 'w'.\n")


def example_03_a_mode():
    name: str = 'ejemplo.txt'
    file_name: str = f'{os.getcwd()}{os.sep}{name}'
    with open(file_name, mode='a') as f:
        f.write("Agregando al final de la línea.\n")


def example_04_x_mode():
    name: str = '__init__.py'
    file_name: str = f'{os.getcwd()}{os.sep}{name}'
    try:
        with open(file_name, mode='x') as f:
            pass
    except FileExistsError:
        print(f'Archivo "{name}" ya existe')


def main():
    example_01_r_mode()
    example_02_w_mode()
    example_03_a_mode()
    example_02_w_mode()


if __name__ == '__main__':
    main()
