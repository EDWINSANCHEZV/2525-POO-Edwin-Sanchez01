#Tarea semana 07
#Constructor y destructor
#Clase para trabajar con autos
#Metodo constructor, se realiza para crear un objeto
class Vehiculo():
    def __init__(self, marca, modelo, tipo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        print(f"Vehiculo creado: {self.marca} {self.modelo}, Tipo:{self.tipo}")

#Mostrar informacion del vehiculo
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Tipo:{self.tipo}")

#Metodo destructor, se realiza para eliminar un objeto
    def __del__ (self):
        print(f"Vehiculo eliminado: {self.marca} {self.modelo}")

#Objetos creados
auto1 = Vehiculo("Chevrolet", "Spark","Automovil" )
auto2 = Vehiculo("Ford", "Expedition", "Camioneta")
auto3 = Vehiculo("Hyundai", "i10", "Automovil")

# Mostrar la información de los vehículos
auto1.mostrar_informacion()
auto2.mostrar_informacion()
auto3.mostrar_informacion()

# Eliminar uno de los objetos manualmente
del auto2