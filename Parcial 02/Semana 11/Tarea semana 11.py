#TAREA SEMANA 11
#


import json
import os

# -------------------------
# Clase Producto
# -------------------------
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def to_dict(self):
        """Convierte el producto a diccionario para guardar en JSON"""
        return {"id": self.id, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

    @classmethod
    def from_dict(cls, data):
        """Crea un objeto Producto a partir de un diccionario"""
        return cls(data["id"], data["nombre"], data["cantidad"], data["precio"])


# -------------------------
# Clase Inventario
# -------------------------
class Inventario:
    ARCHIVO = "inventario.txt"

    def __init__(self):
        # Usamos diccionario para búsqueda rápida por ID
        self.productos = {}
        self.cargar_inventario()

    # ---------- Manejo de Archivos ----------
    def guardar_inventario(self):
        try:
            with open(self.ARCHIVO, "w", encoding="utf-8") as f:
                json.dump({pid: p.to_dict() for pid, p in self.productos.items()}, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar inventario: {e}")

    def cargar_inventario(self):
        if os.path.exists(self.ARCHIVO):
            try:
                with open(self.ARCHIVO, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.productos = {pid: Producto.from_dict(p) for pid, p in data.items()}
            except (json.JSONDecodeError, FileNotFoundError):
                print("Archivo corrupto o inexistente. Se creará uno nuevo.")
                self.productos = {}
        else:
            self.productos = {}

    # ---------- Funciones principales ----------
    def añadir_producto(self, producto):
        if producto.id in self.productos:
            print("Error: ese ID ya existe en el inventario.")
            return
        self.productos[producto.id] = producto
        self.guardar_inventario()
        print("Producto añadido.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print("Producto eliminado.")
        else:
            print("No se encontró el producto.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            self.guardar_inventario()
            print("Producto actualizado.")
        else:
            print("No se encontró el producto.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos.")

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos.values():
                print(p)


# -------------------------
# Programa Principal
# -------------------------
def menu():
    inventario = Inventario()

    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID: ")
            nombre = input("Ingrese nombre: ")
            try:
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: cantidad y precio deben ser numéricos.")

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            try:
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))
                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("Error: cantidad y precio deben ser numéricos.")

        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo y guardando inventario...")
            inventario.guardar_inventario()
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()