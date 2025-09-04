#Tarea semana 12

# =========================================
# Sistema de Gestión de Biblioteca Digital
# =========================================

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Título y autor en tupla, ya que son inmutables
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} - {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}          # diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}        # diccionario con ID como clave y objeto Usuario como valor
        self.ids_usuarios = set() # conjunto para asegurar IDs únicos

    # --- Gestión de libros ---
    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print("El libro ya está registrado en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"Libro eliminado: {eliminado}")
        else:
            print("No existe un libro con ese ISBN.")

    # --- Gestión de usuarios ---
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("Ya existe un usuario con ese ID.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario}")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            eliminado = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario dado de baja: {eliminado}")
        else:
            print("No existe un usuario con ese ID.")

    # --- Préstamos ---
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        if isbn not in self.libros:
            print("Libro no disponible.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros.pop(isbn)  # quitamos de disponibles
        usuario.libros_prestados.append(libro)
        print(f"{usuario.nombre} ha tomado prestado: {libro}")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return

        usuario = self.usuarios[id_usuario]
        libro_a_devolver = None

        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                libro_a_devolver = libro
                break

        if libro_a_devolver:
            usuario.libros_prestados.remove(libro_a_devolver)
            self.libros[isbn] = libro_a_devolver
            print(f"{usuario.nombre} devolvió: {libro_a_devolver}")
        else:
            print("Ese usuario no tiene prestado ese libro.")

    # --- Búsquedas ---
    def buscar_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros.values() if libro.info[0].lower() == titulo.lower()]
        return resultados

    def buscar_por_autor(self, autor):
        resultados = [libro for libro in self.libros.values() if libro.info[1].lower() == autor.lower()]
        return resultados

    def buscar_por_categoria(self, categoria):
        resultados = [libro for libro in self.libros.values() if libro.categoria.lower() == categoria.lower()]
        return resultados

    # --- Listar libros prestados ---
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(f" - {libro}")
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# ================================
# PRUEBAS DEL SISTEMA
# ================================
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "12345")
    libro2 = Libro("Don Quijote", "Miguel de Cervantes", "Clásico", "67890")
    libro3 = Libro("Python para todos", "Charles Severance", "Tecnología", "11223")

    # Añadir libros
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    # Registrar usuarios
    usuario1 = Usuario("Ana", "U001")
    usuario2 = Usuario("Luis", "U002")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("U001", "12345")
    biblioteca.prestar_libro("U002", "67890")

    # Listar libros prestados
    biblioteca.listar_libros_prestados("U001")

    # Devolver libro
    biblioteca.devolver_libro("U001", "12345")

    # Buscar libros
    print("\nBúsqueda por autor 'Charles Severance':")
    for l in biblioteca.buscar_por_autor("Charles Severance"):
        print(l)
