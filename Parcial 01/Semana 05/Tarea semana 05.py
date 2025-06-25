# TAREA DE TIPOS DE DATOS E IDENTIFICADORES
# CALCULAR LA MUESTRA Y EL AREA DE UN RECTANGULO

# Función para calcular el área
def calcular_area_rectangulo(ancho, alto):
    area = ancho * alto  # multiplicamos ancho por alto
    return area

# Solicitar datos al usuario
print("Calculadora de área de un rectángulo")

# Solicitar los valores
ancho_str = input("Ancho del rectángulo: ")
alto_str = input("Alto del rectángulo: ")

# Convertimos los datos ingresados a float
ancho = float(ancho_str)
alto = float(alto_str)

# Medidas son mayores que cero
es_valido = ancho > 0 and alto > 0
if es_valido:
    # La función calcula el área
    area = calcular_area_rectangulo(ancho, alto)
    print("El área del rectángulo es:", area, "metros cuadrados")
else:
    print("Por favor, ingresa valores mayores que cero.")