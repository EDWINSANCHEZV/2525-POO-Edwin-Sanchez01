# Sistema de Mantenimiento de Helicópteros

# Clase que representa un helicóptero
class Helicoptero:
    def __init__(self, matricula, modelo, horas_vuelo):
        self.matricula = matricula
        self.modelo = modelo
        self.horas_vuelo = horas_vuelo
        self.en_mantenimiento = False

    def volar(self, horas):
        """Aumenta las horas de vuelo del helicóptero"""
        self.horas_vuelo += horas
        print(f"{self.modelo} voló {horas} horas. Total: {self.horas_vuelo} horas.")

    def iniciar_mantenimiento(self):
        """Marca el helicóptero como en mantenimiento"""
        self.en_mantenimiento = True
        print(f"{self.modelo} está en mantenimiento.")

    def finalizar_mantenimiento(self):
        """Marca el helicóptero como disponible"""
        self.en_mantenimiento = False
        print(f"{self.modelo} ha salido del mantenimiento.")


# Clase que representa a un técnico de mantenimiento
class Tecnico:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def realizar_mantenimiento(self, helicoptero):
        """Realiza el mantenimiento si el helicóptero está marcado como en mantenimiento"""
        if helicoptero.en_mantenimiento:
            print(f"{self.nombre} está trabajando en el mantenimiento de {helicoptero.modelo}.")
        else:
            print(f"{helicoptero.modelo} no está marcado como en mantenimiento.")


# Clase que representa una orden de mantenimiento
class Mantenimiento:
    def __init__(self, helicoptero, tecnico, descripcion):
        self.helicoptero = helicoptero
        self.tecnico = tecnico
        self.descripcion = descripcion

    def ejecutar(self):
        """Ejecuta el mantenimiento completo"""
        print("\n--- INICIO DEL MANTENIMIENTO ---")
        self.helicoptero.iniciar_mantenimiento()
        self.tecnico.realizar_mantenimiento(self.helicoptero)
        print(f"Trabajo realizado: {self.descripcion}")
        self.helicoptero.finalizar_mantenimiento()
        print("--- FIN DEL MANTENIMIENTO ---\n")


# ===========================
# Ejecución principal
# ===========================
if __name__ == "__main__":
    # Crear un helicóptero
    heli1 = Helicoptero("AEE-326", "ECUREUIL B3e", 1600)

    # Crear un técnico de mantenimiento
    tecnico1 = Tecnico("Cbop Sanchez", "Técnico General")

    # Simulación de vuelo
    heli1.volar(10)

    # Crear y ejecutar una orden de mantenimiento
    orden1 = Mantenimiento(heli1, tecnico1, "Inspección de 100 horas")
    orden1.ejecutar()