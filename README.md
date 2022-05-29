<table>
<tr>
<td width="100px"><img src="https://user-images.githubusercontent.com/103035621/170879657-753152ec-7368-4de6-abe6-dc3240ce57a8.png" alt="Team MSKA"/></td>
<td width="1100px"> <h2>obv: Iniciación a objetos Python + Herencia de clases.</h2> </td>
</tr>
</table>

Se realiza esta actividad para aprender el funcionamiento de objetos y herencia en python.

[![Python](https://img.shields.io/badge/Backend-Python-success)]()

## Clase Vehiculo.py

Para este aprendizaje se crea la clase "Vehiculo". Dicha clase tendra sus atributos de clase privados, para ello se ha de agregar "__" al nombre de los atributos, de esta forma se convierten en privados.

```python
"Se crea la clase Vehículo."
class Vehiculo():
    # Se crean atributos própios de clase.
    __marca = ""
    __modelo = ""
    __potencia = ""
    __ruedas = ""
```

A continuación se crea el constructor con todos los parámetros y un mensaje diciendo "Constructor con todos los atributos", de esta forma verifico la entrada al constructor:

```python
    # Constructor con todos los valores
    def __init__(self, marca, modelo, potencia, ruedas):
        self.__marca = marca
        self.__modelo = modelo
        self.__potencia = potencia
        self.__ruedas = ruedas
        print("\nConstructor con todos los atributos ...")
```

Seguido a esto se generan los getters y setters, en python se indica que son getters mediante la anotación @property y los setters mediante @nombreAtributo.setter.

```python
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
```

Por último se crea el método toString de python y se introducen los atributos de la clase, de esta forma cuando se realice un print sobre la instancia del objeto Vehiculo se mostrará por pantalla una cadena con los atributos de clase.

```python
    # Método toString en python el cual devolverá los valores asignador por pantalla.
    def __str__(self):
        return "- Marca: {}\n- Modelo: {}\n- Potencia: {}\n- Ruedas: {}".format(
            self.__marca, self.__modelo, self.__potencia, self.__ruedas)
```

## Clase Coche.py

Esta clase heredará los métodos y atributos de la clase padre Vehiculo, para ello se introducirá el nombre de la clase padre en la definición de la clase como se puede observar en el siguiente fragmento de código:

```python
"Se importa la clase heredada."
from Vehiculo import Vehiculo

# Se crea la clase Coche que heredará de Vehiculo sus atributos y métodos.
class Coche(Vehiculo):
    # Atributos privados de clase
    __tamañoMaletero = 0
    __tieneRadio = False
```

En el fragmento anterior se importa la clase Vehiculo y se definen los atributos privados de la clase Coche. Mediante la herencia se podrá acceder a los métodos y atributos propios de la clase padre, para ello se definen en el constructor:

```python
    # Constructor de clase con herencia
    def __init__(self, marca, modelo, potencia, ruedas, tamañoMaletero, tieneRadio):
        Vehiculo.__init__(self, marca, modelo, potencia, ruedas)
        self.__tamañoMaletero = tamañoMaletero
        self.__tieneRadio = tieneRadio
```

Una vez definido el constructor de clase con la superclase, se definirán los getters y setters mediante las anotaciones @property y @nombreAtributo.setter.

```python
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
```

Para finalizar esta clase, se sobreescribe el método toString de python generando una cadena de texto que contendrá los valores de la superclase y de la clase coche:

```python
 def __str__(self):
        return Vehiculo.__str__(self) + " \nTamaño del maletero {} y tiene radio {}".format(self.__tamañoMaletero,
                                                                                            self.__tieneRadio)
```

## Clase Main.py

Des del método main se verifica el correcto funcionamiento, para ello primero de todo se genera una instancia de la clase coche que heredará de la clase Vehiculo:

```python
"Se importa la clase coche."
from Coche import Coche

"Clase main"
if __name__ == '__main__':

    "Se crea una instancia de la clase Coche"
    coche1 = Coche('Ford', 'Focus', 111, 4, 180, True)
    "Se imprime dicha instancia mediante el método toString definido en el objeto."
    print(coche1)
```

Mediante el print(coche1) se accede al método toString de la clase Coche que sobreescribe el de la superclase y de esta forma mostrará por consola todos los atributos de ambas clases:

<p align="center">
    <img src="https://user-images.githubusercontent.com/103035621/170886988-ceb944bb-ec98-4cf7-8556-80950b34f446.png">
</p>
