class Especie:
    def __init__(self, nombre: str):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de caracteres.")
        self._nombre = nombre
        self._machos = 0
        self._hembras = 0
        self._ritmoDeCrecimiento = 0.0

    # Comandos
    def establecer_machos(self, cantMachos: int):
        if isinstance(cantMachos, int) and cantMachos >= 0:
            self._machos = cantMachos
        else:
            raise ValueError("La cantidad de machos debe ser un número entero no negativo.")

    def establecer_hembras(self, cantHembras: int):
        if isinstance(cantHembras, int) and cantHembras >= 0:
            self._hembras = cantHembras
        else:
            raise ValueError("La cantidad de hembras debe ser un número entero no negativo.")

    def establecer_ritmo(self, ritmo: float):
        if isinstance(ritmo, (float, int)):
            self._ritmoDeCrecimiento = ritmo
        else:
            raise ValueError("El ritmo debe ser un número real.")

    def actualizar_macho(self, actMachos: int):
        if isinstance(actMachos, int) and self._machos + actMachos >= 0:
            self._machos += actMachos
        else:
            raise ValueError("La cantidad de machos actualizada no puede ser negativa.")

    def actualizar_hembra(self, actHembras: int):
        if isinstance(actHembras, int) and self._hembras + actHembras >= 0:
            self._hembras += actHembras
        else:
            raise ValueError("La cantidad de hembras actualizada no puede ser negativa.")

    def actualizar_ritmo(self, actRitmo: float):
        if isinstance(actRitmo, (float, int)):
            self._ritmoDeCrecimiento += actRitmo
        else:
            raise ValueError("El ritmo actualizado debe ser un número real.")

    # Consultas
    def poblacion_actual(self) -> int:
        return self._machos + self._hembras

    def poblacion_estimada(self, anios: int) -> int:
        if isinstance(anios, int) and anios >= 0:
            poblacion = self.poblacion_actual() * (1 + self._ritmoDeCrecimiento) ** anios
            return max(0, int(poblacion))
        else:
            raise ValueError("Los años deben ser un entero no negativo.")

    def anios_para_poblacion(self, poblacion: int) -> int:
        if not isinstance(poblacion, int) or poblacion <= 0:
            raise ValueError("La población debe ser un número entero positivo.")
        anios = 0
        poblacion_actual = self.poblacion_actual()
        while poblacion_actual < poblacion:
            poblacion_actual *= (1 + self._ritmoDeCrecimiento)
            anios += 1
        return anios

    def nivel_riesgo_extincion(self) -> str:
        if self._ritmoDeCrecimiento > 0:
            return "verde"
        elif self._ritmoDeCrecimiento == 0:
            return "amarillo"
        else:
            return "rojo"

    def mas_hembras(self) -> str:
        if self._hembras > self._machos:
            return "hembras"
        elif self._machos > self._hembras:
            return "machos"
        return "iguales"

    def mayor_ritmo(self, otra_especie:'Especie') -> str:
        if not isinstance(otra_especie, Especie):
            raise ValueError("El parámetro debe ser una instancia de Especie.")
        if self._ritmoDeCrecimiento > otra_especie._ritmoDeCrecimiento:
            return self._nombre
        elif self._ritmoDeCrecimiento < otra_especie._ritmoDeCrecimiento:
            return otra_especie._nombre
        return "igual ritmo"

    def __str__(self):
        return (f"Especie: {self._nombre}, Machos: {self._machos}, "
                f"Hembras: {self._hembras}, Ritmo: {self._ritmoDeCrecimiento}")

def tester():
    try:
        # Creación de la instancia
        especie1 = Especie("Tigre")
        print(especie1)

        # Establecer machos, hembras y ritmo de crecimiento
        especie1.establecer_machos(10)
        especie1.establecer_hembras(15)
        especie1.establecer_ritmo(0.05)
        print(f"Población actual de {especie1._nombre}: {especie1.poblacion_actual()}")

        # Población estimada en 5 años
        print(f"Población estimada de {especie1._nombre} en 5 años: {especie1.poblacion_estimada(5)}")

        # Actualizar machos, hembras y ritmo
        especie1.actualizar_macho(5)
        especie1.actualizar_hembra(3)
        especie1.actualizar_ritmo(0.02)
        print(especie1)

        # Población estimada en 10 años
        print(f"Población estimada de {especie1._nombre} en 10 años: {especie1.poblacion_estimada(10)}")

        # Consultar los años para llegar a una población específica
        print(f"Años para alcanzar 100 de población en {especie1._nombre}: {especie1.anios_para_poblacion(100)}")

        # Riesgo de extinción
        print(f"Riesgo de extinción de {especie1._nombre}: {especie1.nivel_riesgo_extincion()}")

        # Comparar con otra especie
        especie2 = Especie("León")
        especie2.establecer_machos(8)
        especie2.establecer_hembras(12)
        especie2.establecer_ritmo(0.07)

        # Comparación de ritmos
        print(f"Especie con mayor ritmo de crecimiento: {especie1.mayor_ritmo(especie2)}")

        # Más hembras o machos
        print(f"¿{especie1._nombre} tiene más hembras que machos? {especie1.mas_hembras()}")
        print(f"¿{especie2._nombre} tiene más hembras que machos? {especie2.mas_hembras()}")

    except ValueError as e:
        print(f"Error: {e}")

# Ejecutar el tester
tester()