class Automovil:
#Atributos de clase
    def __init__(self, marca: str, modelo: str, anio: int, velocidad_max: float, velocidad_actual: float = 0): #constructor
    #validaciones
        if not isinstance(marca, str):
            raise ValueError("La marca debe ser una cadena de caracteres")
        if not isinstance(modelo, str):
            raise ValueError("El modelo debe ser una cadena de caracteres")
        if not isinstance(anio, int) or anio < 1900 or anio > 2100:
            raise ValueError("El año debe ser un número entero entre 1900 y 2100")
        if not isinstance(velocidad_max, (float, int)) or velocidad_max <= 0:
            raise ValueError("La velocidad máxima debe ser un número decimal positivo")
        if not isinstance(velocidad_actual, (float, int)) or velocidad_actual < 0:
            raise ValueError("La velocidad actual debe ser un número decimal positivo")
    #atributos de instancia
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._velocidad_max = velocidad_max
        self._velocidad_actual = velocidad_actual

#comandos
    def establecer_marca(self, marca: str):
        if isinstance(marca, str):
            self._marca = marca
        else:
            raise ValueError("La marca debe ser una cadena de caracteres")
    def establecer_modelo(self, modelo: str):
        if isinstance(modelo, str):
            self._modelo = modelo
        else:
            raise ValueError("El modelo debe ser una cadena de caracteres")
    def establecer_anio(self, anio: int):
        if isinstance(anio, int) and anio >= 1900 and anio <= 2100:
            self._anio = anio
        else:
            raise ValueError("El año debe ser un número entero entre 1900 y 2100")
    def establecer_velocidad_maxima(self, velocidadMax: float):
        if isinstance(velocidadMax, float) and velocidadMax > 0:
            self._velocidad_max = velocidadMax
        else:
            raise ValueError("La velocidad máxima debe ser un número decimal o entero positivo")
    def establecer_velocidad_actual(self, velocidadActual: float):
        if isinstance(velocidadActual, float) and velocidadActual >= 0:
            self._velocidad_actual = velocidadActual
        else:
            raise ValueError("La velocidad actual debe ser un número decimal o entero positivo")
    def acelerar(self, incremento: float):
        if isinstance(incremento, (float,int)) and incremento >= 0:
            if self._velocidad_actual + incremento > self._velocidad_max:
                self._velocidad_actual = self._velocidad_max
            else:
                self._velocidad_actual += incremento
        else:
            raise ValueError("El incremento debe ser un número decimal o entero positivo")
    def desacelerar(self, decremento: float):
        if isinstance(decremento, (float,int)) and decremento >= 0:
            if self._velocidad_actual - decremento < 0:
                self._velocidad_actual = 0
            else:
                self._velocidad_actual -= decremento
        else:
            raise ValueError("El decremento debe ser un número decimal positivo")
    def frenar_completo(self):
        self._velocidad_actual = 0
    def calcularMinutosParaLlegar(self, distanciaKM: float):
        if isinstance(distanciaKM, (float,int)) and distanciaKM >= 0:
            if self._velocidad_actual > 0:
                tiempo_horas = distanciaKM / self._velocidad_actual
                tiempo_minutos = tiempo_horas * 60
                return tiempo_minutos
        else:
            raise ValueError("La distancia a recorrer debe ser un número decimal o entero positivo")

#consultas
    def obtener_marca(self):
        return self._marca
    def obtener_modelo(self):
        return self._modelo
    def obtener_anio(self):
        return self._anio
    def obtener_velocidad_actual(self):
        return self._velocidad_actual
    def obtener_velocidad_maxima(self):
        return self._velocidad_max

#tester
class TesterAutomovil:
    def probar_automovil(self):
        # Crear una instancia de Automovil
        auto = Automovil("Toyota", "Corolla", 2020, 180, 0)
        
        # Probar getters
        print("Marca:", auto.obtener_marca())  # Esperado: Toyota
        print("Modelo:", auto.obtener_modelo())  # Esperado: Corolla
        print("Año:", auto.obtener_anio())  # Esperado: 2020
        print("Velocidad máxima:", auto.obtener_velocidad_maxima())  # Esperado: 180.0
        print("Velocidad actual:", auto.obtener_velocidad_actual())  # Esperado: 0
        
        # Probar aceleración
        auto.acelerar(50)
        print("Velocidad actual tras acelerar 50 km/h:", auto.obtener_velocidad_actual())  # Esperado: 50
        
        auto.acelerar(150)
        print("Velocidad actual tras intentar acelerar otros 150 km/h:", auto.obtener_velocidad_actual())  # Esperado: 180 (no puede pasar la velocidad máxima)
        
        # Probar desaceleración
        auto.desacelerar(100)
        print("Velocidad actual tras desacelerar 100 km/h:", auto.obtener_velocidad_actual())  # Esperado: 80
        
        auto.desacelerar(200)
        print("Velocidad actual tras intentar desacelerar otros 200 km/h:", auto.obtener_velocidad_actual())  # Esperado: 0 (no puede ser negativa)
        
        # Probar freno completo
        auto.acelerar(60)
        auto.frenar_completo()
        print("Velocidad actual tras frenar completamente:", auto.obtener_velocidad_actual())  # Esperado: 0
        
        # Probar calcular tiempo para llegar
        auto.acelerar(100)  # Acelera a 100 km/h
        minutos = auto.calcularMinutosParaLlegar(200)  # Distancia de 200 km
        print(f"Minutos para llegar a 200 km a una velocidad de {auto.obtener_velocidad_actual()} km/h:", minutos)  # Esperado: 120 minutos

# Crear una instancia del tester y probar
tester = TesterAutomovil()
tester.probar_automovil()