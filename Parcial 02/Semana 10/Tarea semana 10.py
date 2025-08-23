#Tarea semana 10


import os
import json   # Usamos JSON para guardar los datos de manera estructurada

# Archivo donde se guardará el inventario
ARCHIVO_INVENTARIO = "inventario.txt"

# Lista de productos (se carga desde archivo al iniciar)
inventario = []

# Funciones de manejo de archivo
# -------------------------
def cargar_inventario():
    """Carga el inventario desde el archivo inventario.txt si existe"""
    global inventario
    try:
        if os.path.exists(ARCHIVO_INVENTARIO):
            with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as f:
                inventario = json.load(f)
        else:
            inventario = []  # Si no existe, empieza vacío
    except (json.JSONDecodeError, FileNotFoundError):
        print("Error: El archivo estaba corrupto o no existe. Se creará uno nuevo.")
        inventario = []
    except PermissionError:
        print("No tienes permisos para leer el archivo.")
        inventario = []

def guardar_inventario():
    """Guarda el inventario en el archivo inventario.txt"""
    try:
        with open(ARCHIVO_INVENTARIO, "w", encoding="utf-8") as f:
            json.dump(inventario, f, indent=4, ensure_ascii=False)
    except PermissionError:
        print("No tienes permisos para escribir en el archivo.")
    except Exception as e:
        print(f"Error inesperado al guardar el inventario: {e}")

# -------------------------
# Funciones principales
# -------------------------
def añadir_producto():
    id_producto = input("Ingrese ID: ")
    for p in inventario:
        if p["id"] == id_producto:
            print("Ese ID ya existe.")
            return
    nombre = input("Ingrese nombre: ")
    try:
        cantidad = int(input("Ingrese cantidad: "))
        precio = float(input("Ingrese precio: "))
    except ValueError:
        print("Error: cantidad y precio deben ser numéricos.")
        return
    inventario.append({"id": id_producto, "nombre": nombre, "cantidad": cantidad, "precio": precio})
    guardar_inventario()
    print("Producto añadido y guardado en inventario.txt.")

def eliminar_producto():
    id_producto = input("Ingrese ID del producto a eliminar: ")
    for p in inventario:
        if p["id"] == id_producto:
            inventario.remove(p)
            guardar_inventario()
            print("Producto eliminado del inventario.")
            return
    print("No se encontró el producto.")

def actualizar_producto():
    id_producto = input("Ingrese ID del producto a actualizar: ")
    for p in inventario:
        if p["id"] == id_producto:
            try:
                p["cantidad"] = int(input("Nueva cantidad: "))
                p["precio"] = float(input("Nuevo precio: "))
                guardar_inventario()
                print("Producto actualizado y guardado en inventario.txt.")
            except ValueError:
                print("Error: cantidad y precio deben ser numéricos.")
            return
    print("No se encontró el producto.")

def buscar_producto():
    nombre = input("Ingrese nombre a buscar: ").lower()
    encontrados = [p for p in inventario if nombre in p["nombre"].lower()]
    if encontrados:
        for p in encontrados:
            print(p)
    else:
        print("No se encontraron productos.")

def mostrar_todos():
    if not inventario:
        print("Inventario vacío.")
    else:
        for p in inventario:
            print(p)

# -------------------------
# Programa principal
# -------------------------
cargar_inventario()  # Se carga al iniciar

while True:
    print("\nMENÚ DE INVENTARIO")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        añadir_producto()
    elif opcion == "2":
        eliminar_producto()
    elif opcion == "3":
        actualizar_producto()
    elif opcion == "4":
        buscar_producto()
    elif opcion == "5":
        mostrar_todos()
    elif opcion == "6":
        print("Saliendo y guardando inventario...")
        guardar_inventario()
        break
    else:
        print("Opción no válida.")