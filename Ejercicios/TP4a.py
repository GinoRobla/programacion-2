class Empleado:
    # Constructor
    def __init__(self, legajo: int, canthoras: int, valorhora: float):
        # Validaciones
        if not isinstance(legajo, int) or legajo <= 0:
            raise ValueError("El legajo debe ser un número entero positivo")
        if not isinstance(canthoras, int) or canthoras < 0:
            raise ValueError("El número de horas debe ser un número entero no negativo")
        if not isinstance(valorhora, float) or valorhora <= 0:
            raise ValueError("El valor de la hora debe ser un número decimal positivo")
        # Atributos de instancia
        self._legajo = legajo
        self._canthoras = canthoras
        self._valorhora = valorhora

    # Comandos
    def establecer_canthoras(self, hora: int):
        if isinstance(hora, int) and hora >= 0:
            self._canthoras = hora
        else:
            raise ValueError("La cantidad de horas debe ser un número entero no negativo")

    def establecer_valor_hora(self, valor: float):
        if isinstance(valor, float) and valor > 0:
            self._valorhora = valor
        else:
            raise ValueError("El valor de la hora debe ser un número decimal positivo")

    # Consultas
    def obtener_legajo(self) -> int:
        return self._legajo

    def obtener_canthoras(self) -> int:
        return self._canthoras

    def obtener_valor_hora(self) -> float:
        return self._valorhora

    def obtener_sueldo(self) -> float:
        return self._canthoras * self._valorhora

def tester():
    try:
        legajo = int(input("Ingrese el legajo del empleado: "))
        canthoras = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
        valorhora = float(input("Ingrese el valor por hora: "))

        empleado = Empleado(legajo, canthoras, valorhora)

        print(f"Legajo del empleado: {empleado.obtener_legajo()}")
        print(f"Sueldo calculado: {empleado.obtener_sueldo()}")
    except ValueError as e:
        print(f"Error: {e}")

# Ejecución del tester
tester()