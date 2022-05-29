"Se importa la clase heredada."
from Vehiculo import Vehiculo
# Se crea la clase Coche que heredará de Vehiculo sus atributos y métodos.
class Coche(Vehiculo):
    # Atributos privados de clase
    __tamañoMaletero = 0
    __tieneRadio = False

    # Constructor de clase con herencia
    def __init__(self, marca, modelo, potencia, ruedas, tamañoMaletero, tieneRadio):
        Vehiculo.__init__(self, marca, modelo, potencia, ruedas)
        self.__tamañoMaletero = tamañoMaletero
        self.__tieneRadio = tieneRadio

    # Getter para acceder al atributo tamañoMaletero.
    @property
    def tamañoMaletero(self):
        return self.__tamañoMaletero

    # Setter para establecer un valor a tamañoMaletero.
    @tamañoMaletero.setter
    def tamañoMaletero(self, tamañoMaletero):
        self.__tamañoMaletero = tamañoMaletero

    # Getter para acceder al atributo tieneRadio.
    @property
    def tieneRadio(self):
        return self.__tieneRadio

    # Setter para establecer un valor a tieneRadio.
    @tieneRadio.setter
    def tieneRadio(self, tieneRadio):
        self.__tieneRadio = tieneRadio

    def __str__(self):
        return Vehiculo.__str__(self) + " \nTamaño del maletero {} y tiene radio {}".format(self.__tamañoMaletero,
                                                                                            self.__tieneRadio)
