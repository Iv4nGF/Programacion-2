class Teleferico:
    def __init__(self, color_linea="", recorrido="", cantidad_cabinas=0):
        self.color_linea = color_linea
        self.recorrido = recorrido
        self.cantidad_cabinas = cantidad_cabinas
        self.total_empleados = 0
        self.lista_empleados = [['' for _ in range(3)] for _ in range(100)]
        self.edades_empleados = [0] * 100
        self.sueldos_empleados = [0] * 100

    def agregar_persona(self, nombre, apellido1, apellido2, edad, sueldo):
        if self.total_empleados < 100:
            self.lista_empleados[self.total_empleados] = [nombre, apellido1, apellido2]
            self.edades_empleados[self.total_empleados] = edad
            self.sueldos_empleados[self.total_empleados] = sueldo
            self.total_empleados += 1
            print(f"Empleado {nombre} {apellido1} {apellido2} agregado exitosamente.")
        else:
            print("No se pueden agregar más empleados. Se alcanzó la capacidad máxima.")

    def eliminar_por_apellido(self, apellido_buscado):
        i = 0
        while i < self.total_empleados:
            if apellido_buscado in self.lista_empleados[i]:
                for j in range(i, self.total_empleados - 1):
                    self.lista_empleados[j] = self.lista_empleados[j + 1]
                    self.edades_empleados[j] = self.edades_empleados[j + 1]
                    self.sueldos_empleados[j] = self.sueldos_empleados[j + 1]
                self.total_empleados -= 1
            else:
                i += 1
        print(f"Se eliminaron los empleados con apellido {apellido_buscado}.")

    def __add__(self, otra_linea):
        nombre_a_buscar = input("Ingrese el nombre completo del empleado a transferir: ")
        indice_encontrado = -1
        for i in range(self.total_empleados):
            nombre_completo = f"{self.lista_empleados[i][0]} {self.lista_empleados[i][1]} {self.lista_empleados[i][2]}"
            if nombre_completo == nombre_a_buscar:
                indice_encontrado = i
                break

        if indice_encontrado == -1:
            print(f"Empleado {nombre_a_buscar} no encontrado.")
            return otra_linea

        otra_linea.agregar_persona(*self.lista_empleados[indice_encontrado],
                                   self.edades_empleados[indice_encontrado],
                                   self.sueldos_empleados[indice_encontrado])

        for i in range(indice_encontrado, self.total_empleados - 1):
            self.lista_empleados[i] = self.lista_empleados[i + 1]
            self.edades_empleados[i] = self.edades_empleados[i + 1]
            self.sueldos_empleados[i] = self.sueldos_empleados[i + 1]

        self.total_empleados -= 1
        print(f"Empleado {nombre_a_buscar} transferido exitosamente.")

        return otra_linea

    def mostrar_lista_empleados(self, filtro=None):
        if filtro is None:
            print("Lista de Empleados:")
            filtrar_edad = filtrar_sueldo = False
        elif filtro == "mayorEdad":
            if self.total_empleados > 0:
                edad_maxima = max(self.edades_empleados[:self.total_empleados])
                print(f"Empleados con la mayor edad ({edad_maxima} años):")
                filtrar_edad = True
                filtrar_sueldo = False
            else:
                print("No hay empleados registrados.")
                return
        elif filtro == "mayorSueldo":
            if self.total_empleados > 0:
                sueldo_maximo = max(self.sueldos_empleados[:self.total_empleados])
                print(f"Empleados con el mayor sueldo ({sueldo_maximo} Bs):")
                filtrar_sueldo = True
                filtrar_edad = False
            else:
                print("No hay empleados registrados.")
                return
        else:
            print("Tipo de filtro no reconocido.")
            return

        print("{:<15} {:<15} {:<15} {:<5} {:<7}".format(
            "Nombre", "Apellido Paterno", "Apellido Materno", "Edad", "Sueldo"))
        print("-" * 65)

        for i in range(self.total_empleados):
            if filtro is None:
                print("{:<15} {:<15} {:<15} {:<5} {:<7}".format(
                    self.lista_empleados[i][0], self.lista_empleados[i][1],
                    self.lista_empleados[i][2], self.edades_empleados[i], self.sueldos_empleados[i]))
            elif filtrar_edad and self.edades_empleados[i] == edad_maxima:
                print("{:<15} {:<15} {:<15} {:<5} {:<7}".format(
                    self.lista_empleados[i][0], self.lista_empleados[i][1],
                    self.lista_empleados[i][2], self.edades_empleados[i], self.sueldos_empleados[i]))
            elif filtrar_sueldo and self.sueldos_empleados[i] == sueldo_maximo:
                print("{:<15} {:<15} {:<15} {:<5} {:<7}".format(
                    self.lista_empleados[i][0], self.lista_empleados[i][1],
                    self.lista_empleados[i][2], self.edades_empleados[i], self.sueldos_empleados[i]))


if __name__ == "__main__":
    linea1 = Teleferico("Rojo", "Estación Central, Estación Cementerio, Estación 16 de Julio", 20)
    linea1.agregar_persona("Pedro", "Rojas", "Luna", 35, 2500)
    linea1.agregar_persona("Lucy", "Sosa", "Rios", 43, 3250)
    linea1.agregar_persona("Ana", "Perez", "Rojas", 26, 2700)

    linea2 = Teleferico("Azul", "Estación 16 de Julio, Estación Río Seco", 18)
    linea2.agregar_persona("Maria", "Lopez", "Vargas", 32, 2800)
    linea2.agregar_persona("Juan", "Rojas", "Martinez", 45, 3500)
    linea2.agregar_persona("Carlos", "Mendoza", "Rojas", 29, 2700)

    print("--- Línea 1 ---")
    linea1.mostrar_lista_empleados()

    print("--- Línea 2 ---")
    linea2.mostrar_lista_empleados()

    print("Eliminando empleados con apellido Rojas de la Línea 1...")
    linea1.eliminar_por_apellido("Rojas")
    linea1.mostrar_lista_empleados()

    print("Transfiriendo un empleado de Línea 1 a Línea 2...")
    linea1 + linea2

    print("--- Línea 1 después de la transferencia ---")
    linea1.mostrar_lista_empleados()

    print("--- Línea 2 después de la transferencia ---")
    linea2.mostrar_lista_empleados()

    print("Mostrando empleados con la mayor edad de Línea 1:")
    linea1.mostrar_lista_empleados("mayorEdad")

    print("Mostrando empleados con el mayor sueldo de Línea 1:")
    linea1.mostrar_lista_empleados("mayorSueldo")
