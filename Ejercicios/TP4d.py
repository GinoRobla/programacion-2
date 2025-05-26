class Tamagochi:
    # Atributos de clase
    MAX_VALOR = 100
    MIN_VALOR = 0

    def __init__(self, nombre: str):  # Constructor
        # Validación de nombre
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de caracteres")
        # Atributos de instancia protegidos
        self._nombre = nombre
        self._energia = Tamagochi.MAX_VALOR
        self._diversion = Tamagochi.MAX_VALOR
        self._higiene = Tamagochi.MAX_VALOR
        self._dormido = False
        self._accionesConsecutivas = 0
        self._vivo = True

    # Método para verificar límites de atributos
    def _verificarLimites(self):
        self._energia = max(Tamagochi.MIN_VALOR, min(self._energia, Tamagochi.MAX_VALOR))
        self._diversion = max(Tamagochi.MIN_VALOR, min(self._diversion, Tamagochi.MAX_VALOR))
        self._higiene = max(Tamagochi.MIN_VALOR, min(self._higiene, Tamagochi.MAX_VALOR))

    # Comandos
    def comer(self):
        if self._estadoActivo():
            self._energia = min(self._energia + 20, Tamagochi.MAX_VALOR)
            self._resetearAccionesConsecutivas()
        self._verificarLimites()

    def beber(self):
        if self._estadoActivo():
            self._energia = min(self._energia + 10, Tamagochi.MAX_VALOR)
            self._resetearAccionesConsecutivas()
        self._verificarLimites()

    def dormir(self):
        if self._estadoActivo():
            self._dormido = True
            self._energia = min(self._energia + 20, Tamagochi.MAX_VALOR)
            self._diversion = max(self._diversion - 10, Tamagochi.MIN_VALOR)
            self._resetearAccionesConsecutivas()
        self._verificarLimites()

    def despertar(self):
        if self._dormido and self._vivo:
            self._dormido = False

    def jugar(self):
        if self._estadoActivo():
            self._diversion = min(self._diversion + 40, Tamagochi.MAX_VALOR)
            self._reducirEnergia(20)
            self._higiene = max(self._higiene - 15, Tamagochi.MIN_VALOR)
            self._incrementarAccionesConsecutivas()
        self._verificarLimites()

    def caminar(self):
        if self._estadoActivo():
            self._diversion = min(self._diversion + 20, Tamagochi.MAX_VALOR)
            self._reducirEnergia(10)
            self._higiene = max(self._higiene - 8, Tamagochi.MIN_VALOR)
            self._incrementarAccionesConsecutivas()
        self._verificarLimites()

    def saltar(self):
        if self._estadoActivo():
            self._diversion = min(self._diversion + 10, Tamagochi.MAX_VALOR)
            self._reducirEnergia(15)
            self._higiene = max(self._higiene - 10, Tamagochi.MIN_VALOR)
            self._incrementarAccionesConsecutivas()
        self._verificarLimites()

    def bañar(self):
        if self._estadoActivo():
            self._higiene = min(self._higiene + 40, Tamagochi.MAX_VALOR)
            self._diversion = max(self._diversion - 10, Tamagochi.MIN_VALOR)
            self._resetearAccionesConsecutivas()
        self._verificarLimites()

    # Métodos auxiliares
    def _estadoActivo(self):
        return not self._dormido and self._vivo

    def _resetearAccionesConsecutivas(self):
        self._accionesConsecutivas = 0

    def _incrementarAccionesConsecutivas(self):
        self._accionesConsecutivas += 1
        if self._accionesConsecutivas >= 3:
            print("La mascota ha realizado demasiadas acciones seguidas y ahora se dormirá.")
            self.dormir()

    def _reducirEnergia(self, cantidad):
        if self._energia - cantidad <= Tamagochi.MIN_VALOR:
            self._energia = Tamagochi.MIN_VALOR
            self._vivo = False
            print("La mascota ha perdido toda su energía y ha fallecido.")
        else:
            self._energia -= cantidad

    # Consultas
    def obtenerNombre(self):
        return self._nombre

    def obtenerEnergia(self):
        return self._energia

    def obtenerDiversion(self):
        return self._diversion

    def obtenerHigiene(self):
        return self._higiene

    def obtenerDormido(self):
        return self._dormido

    def estaVivo(self):
        return self._vivo

    def obtenerHumor(self):
        if self._energia > 70 and self._diversion > 70 and self._higiene > 70:
            return "Estoy feliz"
        elif self._energia >= 50 and self._diversion >= 50 and self._higiene >= 50:
            return "Estoy alegre"
        elif (30 <= self._energia <= 50 and 30 <= self._diversion <= 50) or \
            (30 <= self._energia <= 50 and 30 <= self._higiene <= 50) or \
            (30 <= self._diversion <= 50 and 30 <= self._higiene <= 50):
            return "Estoy neutral"
        elif (10 <= self._energia <= 30 and 10 <= self._diversion <= 30) or \
            (10 <= self._energia <= 30 and 10 <= self._higiene <= 30) or \
            (10 <= self._diversion <= 30 and 10 <= self._higiene <= 30):
            return "Estoy triste"
        elif self._energia < 10 or self._diversion < 10 or self._higiene < 10:
            return "Estoy muy triste"
        return "Estoy en un estado desconocido"

class TesterTamagochi:
    def __init__(self):
        # Crear instancia de Tamagochi con un nombre ingresado por el usuario
        nombre = input("Ingresa el nombre de tu Tamagochi: ")
        self.tamagochi = Tamagochi(nombre)

    def mostrar_menu(self):
        print("\n--- Menú de Interacción ---")
        print("1. Comer")
        print("2. Beber")
        print("3. Jugar")
        print("4. Caminar")
        print("5. Saltar")
        print("6. Dormir")
        print("7. Despertar")
        print("8. Bañar")
        print("9. Ver estado de la mascota")
        print("0. Salir")

    def ejecutar(self):
        while self.tamagochi.estaVivo():
            self.mostrar_menu()
            opcion = input("Elige una opción: ")
            
            if opcion == "1":
                self.tamagochi.comer()
                print("La mascota ha comido. Energía actual:", self.tamagochi.obtenerEnergia())
            elif opcion == "2":
                self.tamagochi.beber()
                print("La mascota ha bebido. Energía actual:", self.tamagochi.obtenerEnergia())
            elif opcion == "3":
                self.tamagochi.jugar()
                print("La mascota ha jugado. Diversión actual:", self.tamagochi.obtenerDiversion(), "Energía actual:", self.tamagochi.obtenerEnergia(), "Higiene actual:", self.tamagochi.obtenerHigiene())
            elif opcion == "4":
                self.tamagochi.caminar()
                print("La mascota ha caminado. Diversión actual:", self.tamagochi.obtenerDiversion(), "Energía actual:", self.tamagochi.obtenerEnergia(), "Higiene actual:", self.tamagochi.obtenerHigiene())
            elif opcion == "5":
                self.tamagochi.saltar()
                print("La mascota ha saltado. Diversión actual:", self.tamagochi.obtenerDiversion(), "Energía actual:", self.tamagochi.obtenerEnergia(), "Higiene actual:", self.tamagochi.obtenerHigiene())
            elif opcion == "6":
                self.tamagochi.dormir()
                print("La mascota se ha dormido.")
            elif opcion == "7":
                self.tamagochi.despertar()
                print("La mascota se ha despertado.")
            elif opcion == "8":
                self.tamagochi.bañar()
                print("La mascota ha sido bañada. Higiene actual:", self.tamagochi.obtenerHigiene())
            elif opcion == "9":
                self.mostrar_estado()
            elif opcion == "0":
                print("Saliendo del juego.")
                break
            else:
                print("Opción no válida. Por favor, elige nuevamente.")
            
            # Verificar si la mascota sigue viva después de cada acción
            if not self.tamagochi.estaVivo():
                print("Lamentablemente, la mascota ha fallecido. Fin del juego.")
                break

    def mostrar_estado(self):
        print("\n--- Estado de la mascota ---")
        print("Nombre:", self.tamagochi.obtenerNombre())
        print("Energía:", self.tamagochi.obtenerEnergia())
        print("Diversión:", self.tamagochi.obtenerDiversion())
        print("Higiene:", self.tamagochi.obtenerHigiene())
        print("Dormido:", "Sí" if self.tamagochi.obtenerDormido() else "No")
        print("Vivo:", "Sí" if self.tamagochi.estaVivo() else "No")
        print("Humor:", self.tamagochi.obtenerHumor())

# Crear y ejecutar el tester
tester = TesterTamagochi()
tester.ejecutar()