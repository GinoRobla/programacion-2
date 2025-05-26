class Vinoteca:
    # Atributo de clase
    capacidad_maxima = 5000

    def __init__(self):
        # Atributos de instancia (privados)
        self._cant_jugo = Vinoteca.capacidad_maxima
        self._cant_blanco = Vinoteca.capacidad_maxima
        self._cant_tinto = Vinoteca.capacidad_maxima
        self._cant_anejo = Vinoteca.capacidad_maxima

    # Métodos para obtener el stock de cada tipo de bebida
    def obtener_cant_jugo(self):
        return self._cant_jugo

    def obtener_cant_blanco(self):
        return self._cant_blanco

    def obtener_cant_tinto(self):
        return self._cant_tinto

    def obtener_cant_anejo(self):
        return self._cant_anejo

    # Métodos para reponer cada tipo de bebida
    def reponer_jugo(self):
        self._cant_jugo = Vinoteca.capacidad_maxima

    def reponer_blanco(self):
        self._cant_blanco = Vinoteca.capacidad_maxima

    def reponer_tinto(self):
        self._cant_tinto = Vinoteca.capacidad_maxima

    def reponer_anejo(self):
        self._cant_anejo = Vinoteca.capacidad_maxima

    # Métodos para vender cada tipo de bebida con manejo de excepciones
    def vender_jugo(self, cantidad: int):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser un número entero positivo")
        
        if cantidad > self._cant_jugo:
            print(f"No se pudo completar la venta de jugo por falta de stock, se vendieron {self._cant_jugo} unidades.")
            self._cant_jugo = 0
        else:
            self._cant_jugo -= cantidad

    def vender_blanco(self, cantidad: int):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser un número entero positivo")
        
        if cantidad > self._cant_blanco:
            print(f"No se pudo completar la venta de vino blanco por falta de stock, se vendieron {self._cant_blanco} unidades.")
            self._cant_blanco = 0
        else:
            self._cant_blanco -= cantidad

    def vender_tinto(self, cantidad: int):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser un número entero positivo")
        
        if cantidad > self._cant_tinto:
            print(f"No se pudo completar la venta de vino tinto por falta de stock, se vendieron {self._cant_tinto} unidades.")
            self._cant_tinto = 0
        else:
            self._cant_tinto -= cantidad

    def vender_anejo(self, cantidad: int):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser un número entero positivo")
        
        if cantidad > self._cant_anejo:
            print(f"No se pudo completar la venta de vino añejo por falta de stock, se vendieron {self._cant_anejo} unidades.")
            self._cant_anejo = 0
        else:
            self._cant_anejo -= cantidad

# Clase de pruebas para la clase Vinoteca
class TesterVinoteca:
    def probar_vinoteca(self):
        # Crear una instancia de Vinoteca
        vinoteca = Vinoteca()

        # Mostrar el stock inicial de cada tipo de bebida
        print("Stock inicial:")
        print(f"Jugo: {vinoteca.obtener_cant_jugo()}")
        print(f"Blanco: {vinoteca.obtener_cant_blanco()}")
        print(f"Tinto: {vinoteca.obtener_cant_tinto()}")
        print(f"Añejo: {vinoteca.obtener_cant_anejo()}\n")

        # Probar la venta de jugo (venta exitosa)
        try:
            print("Intentando vender 3000 unidades de jugo...")
            vinoteca.vender_jugo(3000)
            print(f"Stock de jugo después de la venta: {vinoteca.obtener_cant_jugo()}\n")
        except ValueError as e:
            print(f"Error: {e}")

        # Probar la venta de tinto (venta fallida por falta de stock)
        try:
            print("Intentando vender 6000 unidades de tinto...")
            vinoteca.vender_tinto(6000)
            print(f"Stock de tinto después de la venta: {vinoteca.obtener_cant_tinto()}\n")
        except ValueError as e:
            print(f"Error: {e}")

        # Probar la reposición de jugo
        print("Reponiendo jugo...")
        vinoteca.reponer_jugo()
        print(f"Stock de jugo después de la reposición: {vinoteca.obtener_cant_jugo()}\n")

        # Probar la venta de añejo (venta parcial)
        try:
            print("Intentando vender 4500 unidades de añejo...")
            vinoteca.vender_anejo(4500)
            print(f"Stock de añejo después de la venta: {vinoteca.obtener_cant_anejo()}\n")
        except ValueError as e:
            print(f"Error: {e}")

# Ejecutar el tester
tester = TesterVinoteca()
tester.probar_vinoteca()