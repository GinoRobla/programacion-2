class Participante:
    # atributos de clase
    def __init__(self, nombre: str, edad: int, nacionalidad: str):  # constructor
        # validaciones
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de caracteres.")
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un número entero positivo.")
        if not isinstance(nacionalidad, str):
            raise ValueError("La nacionalidad debe ser una cadena de caracteres.")
        # atributos de instancia
        self._nombre = nombre
        self._edad = edad
        self._nacionalidad = nacionalidad
        self._disciplinas = []
    # comandos
    def inscribir_diciplina(self, disciplina):
        if disciplina not in self._disciplinas:
            self._disciplinas.append(disciplina)
        else:
            raise ValueError("Esta disciplina ya está registrada.")
    def eliminar_diciplina(self, disciplina):
        if disciplina in self._disciplinas:
            self._disciplinas.remove(disciplina)
        else:
            raise ValueError("Esta disciplina no está registrada.")
    # consultas
    def obtener_nombre(self) -> str:
        return self._nombre
    def obtener_edad(self) -> int:
        return self._edad
    def obtener_nacionalidad(self) -> str:
        return self._nacionalidad
    def obtener_disciplinas(self):
        return self._disciplinas
    def __str__(self):
        return f"Participante: {self._nombre}, Edad: {self._edad}, Nacionalidad: {self._nacionalidad}"

class Disciplina:
    # atributos de clase
    def __init__(self, nombre, descripcion):  # constructor
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de caracteres.")
        if not isinstance(descripcion, str):
            raise ValueError("La descripción debe ser una cadena de caracteres.")
        # atributos de instancia
        self._nombre = nombre
        self._descripcion = descripcion
        self._participantes = []
    # comandos
    def inscribir_participante(self, participante):
        if participante not in self._participantes:
            self._participantes.append(participante)
        else:
            raise ValueError("Este participante ya está registrado en esta disciplina.")
    def eliminar_participante(self, participante):
        if participante in self._participantes:
            self._participantes.remove(participante)
        else:
            raise ValueError("Este participante no está registrado en esta disciplina.")
    # consultas
    def obtener_nombre(self) -> str:
        return self._nombre
    def obtener_descripcion(self) -> str:
        return self._descripcion
    def obtener_participantes(self):
        return self._participantes 
    def __str__(self):
        return f"Disciplina: {self._nombre}, Descripción: {self._descripcion}"

class Tester:
    def __init__(self):
        self._participantes = []  # Lista de participantes registrados
        self._disciplinas = []    # Lista de disciplinas registradas

    def registrar_participante(self):
        nombre = input("Ingrese el nombre del participante: ")
        edad = int(input("Ingrese la edad del participante: "))
        nacionalidad = input("Ingrese la nacionalidad del participante: ")
        participante = Participante(nombre, edad, nacionalidad)
        self._participantes.append(participante)

    def registrar_disciplina(self):
        nombre = input("Ingrese el nombre de la disciplina: ")
        descripcion = input("Ingrese la descripción de la disciplina: ")
        disciplina = Disciplina(nombre, descripcion)
        self._disciplinas.append(disciplina)

    def inscribir_participante(self):
        nombre_participante = input("Ingrese el nombre del participante: ")
        nombre_disciplina = input("Ingrese el nombre de la disciplina: ")
        participante = None
        disciplina = None

        # Buscar participante
        for p in self._participantes:
            if p.obtener_nombre() == nombre_participante:
                participante = p
                break

        # Buscar disciplina
        for d in self._disciplinas:
            if d.obtener_nombre() == nombre_disciplina:
                disciplina = d
                break

        if participante and disciplina:
            participante.inscribir_diciplina(disciplina)
            disciplina.inscribir_participante(participante)
        else:
            print("Participante o disciplina no encontrado.")

    def mostrar_participantes(self):
        nombre_disciplina = input("Ingrese el nombre de la disciplina: ")
        disciplina = None

        # Buscar disciplina
        for d in self._disciplinas:
            if d.obtener_nombre() == nombre_disciplina:
                disciplina = d
                break

        if disciplina:
            print(f"Participantes en la disciplina {nombre_disciplina}:")
            for p in disciplina.obtener_participantes():
                print(p.obtener_nombre())
        else:
            print("Disciplina no encontrada.")

    def mostrar_disciplinas(self):
        nombre_participante = input("Ingrese el nombre del participante: ")
        participante = None

        # Buscar participante
        for p in self._participantes:
            if p.obtener_nombre() == nombre_participante:
                participante = p
                break

        if participante:
            print(f"Disciplinas en las que participa {nombre_participante}:")
            for d in participante.obtener_disciplinas():
                print(d.obtener_nombre())
        else:
            print("Participante no encontrado.")

    def menu(self):
        while True:
            print("\n----- MENÚ -----")
            print("1. Registrar participante")
            print("2. Registrar disciplina")
            print("3. Inscribir participante en disciplina")
            print("4. Mostrar participantes en una disciplina")
            print("5. Mostrar disciplinas de un participante")
            print("6. Salir")
            opcion = input("Elija una opción: ")

            if opcion == '1':
                self.registrar_participante()
            elif opcion == '2':
                self.registrar_disciplina()
            elif opcion == '3':
                self.inscribir_participante()
            elif opcion == '4':
                self.mostrar_participantes()
            elif opcion == '5':
                self.mostrar_disciplinas()
            elif opcion == '6':
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida, intente nuevamente.")

# Ejecutando el tester
tester = Tester()
tester.menu()