"Se importa la clase coche."
from Coche import Coche

"Clase main"
if __name__ == '__main__':

    "Se crea una instancia de la clase Coche"
    coche1 = Coche('Ford', 'Focus', 111, 4, 180, True)
    "Se imprime dicha instancia mediante el método toString definido en el objeto."
    print(coche1)
