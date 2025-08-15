#Tarea de la semana 9
#Sistema de Gestión de Inventarios
# Lista de productos
inventario = []

# Función para añadir producto
def añadir_producto():
    id_producto = input("Ingrese ID: ")
    # Verificar que el ID no se repita
    for p in inventario:
        if p["id"] == id_producto:
            print("Ese ID ya existe.")
            return
    nombre = input("Ingrese nombre: ")
    cantidad = int(input("Ingrese cantidad: "))
    precio = float(input("Ingrese precio: "))
    inventario.append({"id": id_producto, "nombre": nombre, "cantidad": cantidad, "precio": precio})
    print("Producto añadido.")

# Función para eliminar producto
def eliminar_producto():
    id_producto = input("Ingrese ID del producto a eliminar: ")
    for p in inventario:
        if p["id"] == id_producto:
            inventario.remove(p)
            print("Producto eliminado.")
            return
    print("No se encontró el producto.")

# Función para actualizar producto
def actualizar_producto():
    id_producto = input("Ingrese ID del producto a actualizar: ")
    for p in inventario:
        if p["id"] == id_producto:
            p["cantidad"] = int(input("Nueva cantidad: "))
            p["precio"] = float(input("Nuevo precio: "))
            print("Producto actualizado.")
            return
    print("No se encontró el producto.")

# Función para buscar por nombre
def buscar_producto():
    nombre = input("Ingrese nombre a buscar: ").lower()
    encontrados = [p for p in inventario if nombre in p["nombre"].lower()]
    if encontrados:
        for p in encontrados:
            print(p)
    else:
        print("No se encontraron productos.")

# Función para mostrar todos
def mostrar_todos():
    if not inventario:
        print("Inventario vacío.")
    else:
        for p in inventario:
            print(p)

# Menú principal
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
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")