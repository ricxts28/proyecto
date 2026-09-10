class Dueno:
    total_duenos = 0

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        Dueno.total_duenos += 1

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()

    @classmethod
    def cantidad_duenos(cls):
        return cls.total_duenos

    @staticmethod
    def validar_telefono(telefono):
        return telefono.isdigit() and len(telefono.strip()) >= 6

    def __str__(self):
        return f"Dueño: {self.__nombre} | Teléfono: {self.telefono}"


class Mascota:
    def __init__(self, nombre, especie, dueno, peso):
        self.nombre = nombre
        self.especie = especie
        self.dueno = dueno  # Relación con la clase Dueno
        self.__peso = peso
        self.__atendida = False

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("Peso inválido.")
        self.__peso = valor

    def atender(self):
        if not self.__atendida:
            self.__atendida = True
            return True
        return False

    @staticmethod
    def es_peso_valido(peso):
        return isinstance(peso, (int, float)) and peso > 0

    def __str__(self):
        estado = "Atendida" if self.__atendida else "En espera"
        return f"Mascota: {self.nombre} ({self.especie}) | Dueño: {self.dueno.nombre} | Peso: {self.__peso}kg | Estado: {estado}"


class Veterinaria:
    total_veterinarias = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.__pacientes = []
        Veterinaria.total_veterinarias += 1

    def registrar_mascota(self, mascota):
        self.__pacientes.append(mascota)

    def buscar_mascota(self, nombre):
        for mascota in self.__pacientes:
            if mascota.nombre.lower() == nombre.lower():
                return mascota
        return None

    def listar_mascotas(self):
        if not self.__pacientes:
            print("No hay mascotas registradas.")
            return
        for mascota in self.__pacientes:
            print(mascota)

    def atender_mascota(self, nombre):
        mascota = self.buscar_mascota(nombre)
        if mascota is None:
            print("Mascota no encontrada.")
            return
        if mascota.atender():
            print(f"'{mascota.nombre}' ha sido atendida exitosamente.")
        else:
            print(f"'{mascota.nombre}' ya fue atendida previamente.")

    def modificar_peso(self, nombre, nuevo_peso):
        mascota = self.buscar_mascota(nombre)
        if mascota is None:
            print("Mascota no encontrada.")
            return
        if Mascota.es_peso_valido(nuevo_peso):
            mascota.peso = nuevo_peso
            print(f"Peso de '{mascota.nombre}' actualizado a {nuevo_peso}kg.")
        else:
            print("Peso inválido.")

    def __str__(self):
        return f"Veterinaria: {self.nombre} | Pacientes registrados: {len(self.__pacientes)}"


def menu():
    vet = Veterinaria("Clínica Vet Feliz")

    while True:
        print("\n===== MENÚ VETERINARIA =====")
        print("1. Registrar dueño y mascota")
        print("2. Listar todas las mascotas")
        print("3. Buscar mascota")
        print("4. Marcar mascota como atendida")
        print("5. Modificar peso de una mascota")
        print("6. Ver información de la veterinaria")
        print("7. Ver total de dueños registrados")
        print("8. Salir")

        opcion = input("\nElige una opción: ").strip()

        if opcion == "1":
            nombre_dueno = input("Nombre del dueño: ").strip()
            telefono = input("Teléfono del dueño (solo números): ").strip()
            if not Dueno.validar_telefono(telefono):
                print("Teléfono inválido.")
                continue
            
            try:
                dueno = Dueno(nombre_dueno, telefono)
            except ValueError as e:
                print(e)
                continue

            nombre_mascota = input("Nombre de la mascota (ej. Firulais): ").strip()
            especie = input("Especie de la mascota (ej. Perro, Gato): ").strip()
            try:
                peso = float(input("Peso (kg): ").strip())
            except ValueError:
                print("El peso debe ser un número.")
                continue
            
            if not Mascota.es_peso_valido(peso):
                print("Peso inválido. Debe ser mayor a 0.")
                continue
            
            mascota = Mascota(nombre_mascota, especie, dueno, peso)
            vet.registrar_mascota(mascota)
            print(f"Mascota '{nombre_mascota}' registrada correctamente.")

        elif opcion == "2":
            vet.listar_mascotas()

        elif opcion == "3":
            nombre = input("Nombre de la mascota a buscar: ").strip()
            mascota = vet.buscar_mascota(nombre)
            if mascota:
                print(mascota)
            else:
                print("Mascota no encontrada.")

        elif opcion == "4":
            nombre = input("Nombre de la mascota a atender: ").strip()
            vet.atender_mascota(nombre)

        elif opcion == "5":
            nombre = input("Nombre de la mascota a modificar: ").strip()
            try:
                nuevo_peso = float(input("Nuevo peso (kg): ").strip())
            except ValueError:
                print("El peso debe ser un número.")
                continue
            vet.modificar_peso(nombre, nuevo_peso)

        elif opcion == "6":
            print(vet)

        elif opcion == "7":
            print(f"Total de dueños registrados en el sistema: {Dueno.cantidad_duenos()}")

        elif opcion == "8":
            print("Saliendo del sistema. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Por favor elige entre 1 y 8.")


if __name__ == "__main__":
    menu()