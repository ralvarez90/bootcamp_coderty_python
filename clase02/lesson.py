"""CLASE 02. POO

Python es un lenguaje orientado a objetos basado en clases. Los principales
"""


def example_01():
    content: str = """Componentes de POO en Python
    \r- Clases
    \r- Atributos
    \r- Métodos
    \r- Objetos
    \r- Herencia
    \r- Polimorfismo
    
    \r1. Clase
    Elemento de programación que actúa como plantilla o molde que define y
    establece las características y comportamiento de entidades creadas
    a partir de dicha clase.
    
    \r2. Atributos
    Son las características de las entidades que establecerán el estado
    del objeto.
    
    \r3. Métodos
    Son funciones asociados a los objetos que definen el comportamiento
    de entidades/objetos/instancias creadas.
    
    \r4. Herencia
    Pilar de la POO que establece que si una clase B extiende de una clase
    A, heredará atributos y comportamientos de A. Instancias de B y de A
    cumplirán la relación "es un A".
    
    \r5. Polimorfismo
    Permite que objetos de diferentes clases se traten como objetos de una clase 
    común. Esto se traduce en la capacidad de usar un mismo nombre de función 
    para realizar diferentes acciones dependiendo del objeto al que se aplica.
    """
    print(content)


class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f'Persona(nombre="{self.nombre}", edad={self.edad})')


def example_02():
    """Ejemplo de clases. Creación de instancias de Persona."""

    # creación de instancias
    persona1 = Persona('John Wick', 45)
    persona2 = Persona('Juán Güic', 45)

    # invocación de métodos
    persona1.mostrar_info()
    persona2.mostrar_info()


def main():
    example_01() or print()
    example_02() or print()


if __name__ == '__main__':
    main()
