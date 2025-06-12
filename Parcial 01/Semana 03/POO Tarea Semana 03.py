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

    def ingresar_temperaturas(selfs):
        for i in range(7):
            dia = DiaClima(dia=i+1)
            temp = float(input(f"Ingresar la temperatura del día {i + 1}: "))
            dia.set_temperatura(temp)
            self.dias.append(dia)

    def calcular_promedio(self):
        total = sum(dia.get_temperatura() for dia in self.dias)
        return total / len(self.dias) if self.dias else 0

    def mostrar_datos(self):
        for dia in self.dias:
            print(dia)

# Programa
def main():
    print("Temperatura Semanal")
    print(f"Promedio semanal: {promedio:.2f} °C")

if __name__ == "__main__":
    main()