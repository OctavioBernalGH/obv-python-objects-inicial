<table>
<tr>
<td width="100px"><img src="https://user-images.githubusercontent.com/103035621/170483040-a88d598b-145b-4903-accb-948ceff05811.png" alt="Team MSKA"/></td>
<td width="1100px"> <h2>obv: Creación de objetos en Python 1</h2> </td>
</tr>
</table>

[![Python](https://img.shields.io/badge/Backend-Python-success)]()

Se crea un objeto llamado Vehículo con los atributos de clase:

```python
if __name__ == '__main__':

    # Se crea la clase vehículo
    class Vehiculo():

        # Se crean atributos própios de clase.
        __marca = ""
        __modelo = ""
        __potencia = ""
        __ruedas = ""

```

Se crea un constructor de clase vacío con valores por defecto:

```python
        # Constructor vacío con valores por defecto.
        def __init__(self):
            self.__marca = None
            self.__modelo = None
            self.__potencia = None
            self.__ruedas = None
            print("\nConstructor vacío ...")
```

Se definen los getters y setters y el método toString de python:

```java
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
```

Por último se verifica el correcto funcionamiento:

```python
    # Se crea una instancia coche1 del tipo Vehiculo.
    coche1 = Vehiculo()
    # Se asignan los nuevos valores a los atributos mediante los setters.
    coche1.marca    = 'Ford'
    coche1.modelo   = 'Focus 2'
    coche1.potencia = 110
    coche1.ruedas   = 4
    # Se imprime el objeto gracias al método __str__
    print(coche1)
    # Se accede a un atributo mediante el getter.
    print("La marca del coche es: " + coche1.marca)
```
