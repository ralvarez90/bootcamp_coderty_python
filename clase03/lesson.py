"""CLASE 03. Practicaremos la programación orientada a objetos
usando la librería tkinter.
"""
import sys
import tkinter as tk
from tkinter import messagebox


class Coche:
    def __init__(self, marca: str, modelo: str, velocidad_max: float):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_max = velocidad_max
        self.velocidad_actual = 0

    def acelerar(self, incremento: float):
        self.velocidad_actual += incremento
        if self.velocidad_actual > self.velocidad_max:
            self.velocidad_actual = self.velocidad_max

    def frenar(self, decremento: float):
        self.velocidad_actual -= decremento
        if self.velocidad_actual < 0:
            self.velocidad_actual = 0

    def apagar(self):
        pass


class Application:
    def __init__(self, root: tk.Tk, coche: Coche):
        # elemento raíz
        self.root = root
        self.root.title('Simulador de Autos')
        self.coche = coche

        # elementos de la interfaz gráfica: labels
        self.label_marca = tk.Label(self.root, text=f'Marca: {self.coche.marca}')
        self.label_marca.pack()

        self.label_modelo = tk.Label(self.root, text=f'Modelo: {self.coche.modelo}')
        self.label_modelo.pack()

        self.label_velocidad_actual = tk.Label(self.root,
                                               text=f'Velocidad actual: {self.coche.velocidad_actual:6.2f} Km/h')
        self.label_velocidad_actual.pack()

        self.label_velocidad_max = tk.Label(self.root, text=f'Velocidad máxima: {self.coche.velocidad_max:6.2f} Km/h')
        self.label_velocidad_max.pack()

        # elementos de la interfaz gráfica: botones
        self.btn_acelerar = tk.Button(self.root, text='Acelerar', command=self.acelerar)
        self.btn_acelerar.pack()

        self.btn_frenar = tk.Button(self.root, text='Frenar', command=self.frenar)
        self.btn_frenar.pack()

        self.btn_apagar = tk.Button(self.root, text='Apagar', command=self.apagar)
        self.btn_apagar.pack()

    def frenar(self):
        self.coche.frenar(10)
        self.actualizar_velocidad()

    def acelerar(self):
        self.coche.acelerar(20)
        self.actualizar_velocidad()

    def apagar(self):
        if self.coche.velocidad_actual > 0:
            messagebox.showinfo('Advertencia', 'No se puede apagar')
            return

        self.coche.apagar()
        sys.exit(0)

    def actualizar_velocidad(self):
        self.label_velocidad_actual.config(text=f'Velocidad actual: {self.coche.velocidad_actual:6.2f} Km/h')


def main():
    # ventana raíz
    root = tk.Tk()

    # coches
    audi = Coche('Audi', 'TT', 260)

    # run application
    app = Application(root, audi)
    root.mainloop()


if __name__ == '__main__':
    main()
