#Tarea de la semana 6
#Aplicaciones de los conceptos de POO
# Definimos una clase base llamada Animal (clase padre)
class Animal:
    def __init__(self, nombre):  # Constructor
        self.nombre = nombre      # Atributo

    def hacer_sonido(self):       # Método
        print("Este animal hace un sonido")

# Clase Perro que hereda de Animal
class Perro(Animal):
    def hacer_sonido(self):  # Polimorfismo: sobrescribe el método del padre
        print(f"{self.nombre} dice: Guau Guau")

# Clase Gato que también hereda de Animal
class Gato(Animal):
    def hacer_sonido(self):  # Polimorfismo
        print(f"{self.nombre} dice: Miau")

# Programa principal
# Creamos objetos (instancias)
mi_perro = Perro("Tommy")
mi_gato = Gato("Theo")

# Llamamos a sus métodos
mi_perro.hacer_sonido()
mi_gato.hacer_sonido()