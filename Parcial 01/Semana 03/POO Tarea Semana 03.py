# Tarea de programacion Semana 03
# Comparación de Programación Tradicional y POO en Python
# Programación POO
# Codigo para ingresar las temperaturas diarias

# ABTRACCION
class Clima:
    def __init__(self, dia, temperatura=0.0):
        self.__dia =dia
        self.__temperatura =temperatura

# ENCAUPSULAMIENTO

    def set_temperatura(self, temperatura):
        self.__temperatura = temperatura

    def get_temperatura(self):
        return self.__temperatura

    def __str__(self):
        return f"Dia {self.__dia}: {self._temperatura} °C"

class SemanaClima
    def __init__(self):
        self.dias =[]
