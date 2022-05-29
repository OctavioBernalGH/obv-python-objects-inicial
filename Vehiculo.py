"Se crea la clase Vehículo."
class Vehiculo():
    # Se crean atributos própios de clase.
    __marca = ""
    __modelo = ""
    __potencia = ""
    __ruedas = ""

    # Constructor con todos los valores
    def __init__(self, marca, modelo, potencia, ruedas):
        self.__marca = marca
        self.__modelo = modelo
        self.__potencia = potencia
        self.__ruedas = ruedas
        print("\nConstructor con todos los atributos ...")

    # Getter para acceder al atributo marca.
    @property
    def marca(self):
        return self.__marca

    # Setter para establecer un valor a marca.
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    # Getter para acceder al atributo modelo.
    @property
    def modelo(self):
        return self.__modelo

    # Setter para establecer un valor a modelo.
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    # Getter para acceder al atributo potencia.
    @property
    def potencia(self):
        return self.__potencia

    # Setter para establecer un valor a potencia.
    @potencia.setter
    def potencia(self, potencia):
        self.__potencia = potencia

    # Getter para acceder al atributo ruedas.
    @property
    def ruedas(self):
        return self.__ruedas

    # Setter para establecer un valor a ruedas
    @ruedas.setter
    def ruedas(self, ruedas):
        self.__ruedas = ruedas

    # Método toString en python el cual devolverá los valores asignador por pantalla.
    def __str__(self):
        return "- Marca: {}\n- Modelo: {}\n- Potencia: {}\n- Ruedas: {}".format(
            self.__marca, self.__modelo, self.__potencia, self.__ruedas)
