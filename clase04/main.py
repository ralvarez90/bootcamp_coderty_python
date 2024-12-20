"""Leer nombres, colocar primera letra en mayúsculas y ordenarlas en
orden alfabético.
"""
import os
import threading
from time import sleep


class NamesProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path

    @staticmethod
    def __save_sorted_names(sorted_names: list):
        output_file: str = os.getcwd() + os.sep + 'sorted_names.txt'
        with open(output_file, 'w') as f:
            for name in sorted_names:
                f.write(name + '\n')
        print(f'Nombres ordenados guardados en: "{output_file}"')

    @staticmethod
    def __clean_and_capitalize_name(name: str) -> str:
        return name.strip().capitalize()

    def process_names(self):
        try:
            with open(self.file_path, 'r') as f:
                names = f.readlines()
                cleaned_names = [self.__clean_and_capitalize_name(name) for name in names]
                cleaned_names.sort()
                self.__save_sorted_names(cleaned_names)
        except FileNotFoundError:
            print(f'Archivo no encontrado: {self.file_path}')

    def start_processing(self):
        def run():
            while True:
                print('Procesando nombres...')
                self.process_names()
                print('Esperando para procesar de nuevo... \n')
                sleep(3)

        thread = threading.Thread(target=run)
        thread.start()


def main():
    processor = NamesProcessor(file_path=os.getcwd() + os.sep + 'nombres.txt')
    processor.start_processing()


if __name__ == '__main__':
    main()
