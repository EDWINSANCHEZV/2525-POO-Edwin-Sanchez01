# Tarea de programacion Semana 03
# Comparación de Programación Tradicional y POO en Python
# Programación Tradicional

# Codigo para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for dia in range(7):
        temp = float(input(f"Ingresar la temperatura del día {dia + 1}:"))
        temperaturas.append(temp)
    return temperaturas

# Codigo para calcular la temperatura  promedio semanal
def calcular_promedio(temperaturas):
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)

# Función
def main():
    print("TEMPERATURA SEMANAL")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"TEMPERATURA PROMEDIO SEMANAL ES: {promedio:.2f} °C")

# PROGRAMACION
if __name__ == "__main__":
    main()