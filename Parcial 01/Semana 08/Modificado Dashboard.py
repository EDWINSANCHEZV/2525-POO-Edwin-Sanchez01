# Adaptado por Edwin Sánchez
# Este script permite visualizar el contenido de scripts organizados por unidades.
# Tarea de Programación Orientada a Objetos
# Modificado el 19/07/2025


import os

def mostrar_codigo(ruta_script):
    """
    Función que muestra el contenido de un script Python dado su nombre o ruta relativa.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    """
    Función que muestra el menú principal del dashboard y permite elegir un archivo para visualizar.
    """
    ruta_base = os.path.dirname(__file__)  # Obtiene la ruta donde está este archivo

    # Diccionario de rutas organizadas por unidades y ejemplos
    opciones = {
        '1': 'UNIDAD 1/1.2. Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py',
        '2': 'UNIDAD 2/2.1. Clases y Objetos/2.1.1. Ejemplo Clases.py',
        '3': 'UNIDAD 3/3.1. Herencia/3.1.1. Ejemplo Herencia.py',   #AUMENTADO
        '4': 'UNIDAD 4/4.1. Encapsulamiento/4.1.1. Ejemplo Encapsulamiento.py' #AUMENTADO
        # Puedes seguir agregando más scripts aquí
    }

    while True:
        print("\nMenú de Tareas de POO - Dashboard Personal de Edwin")
        for key in opciones:
            print(f"{key} - Ver código: {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un número para ver el código o '0' para salir: ")
        if eleccion == '0':
            print("Saliendo del Dashboard. ¡Hasta luego!")
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()