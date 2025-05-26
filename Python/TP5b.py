from datetime import date

class Fecha:
    #atributos de clase
    def __init__(self, dias:int, mes:int, anio:int): #constructor
        # Validaciones
        if not isinstance(dias, int) or dias < 1 or dias > 31:
            raise ValueError("Los días deben ser un número entero entre 1 y 31.")
        if not isinstance(mes, int) or mes < 1 or mes > 12:
            raise ValueError("El mes debe ser un número entero entre 1 y 12.")
        if not isinstance(anio, int) or anio < 1900 or anio > 2100:
            raise ValueError("El año debe ser un número entero entre 1900 y 2100.")
        # Atributos de instancia
        self._dias = dias
        self._mes = mes
        self._anio = anio
    #comandos
    def establecer_dias(self, dias:int):
        if isinstance(dias, int) and dias > 0 and dias < 32:
            self._dias = dias
    def establecer_mes(self, mes:int):
        if isinstance(mes, int) and mes > 0 and mes < 13:
            self._mes = mes
    def establecer_anio(self, anio:int):
        if isinstance(anio, int) and anio > 1899 and anio < 2101:
            self._anio = anio
    #consultas
    def obtener_dias(self) -> int:
        return self._dias
    def obtener_mes(self) -> int:
        return self._mes
    def obtener_anio(self) -> int:
        return self._anio
    def es_anterior(self, otra_fecha:'Fecha') -> bool:
        if self._anio < otra_fecha._anio:
            return True
        if self._anio == otra_fecha._anio and self._mes < otra_fecha._mes:
            return True
        if self._anio == otra_fecha._anio and self._mes == otra_fecha._mes and self._dias < otra_fecha._dias:
            return True
        return False    
    def suma_dias(self, cant_dias: int) -> 'Fecha':
        self._dias += cant_dias
        
        while self._dias > 31:
            self._dias -= 31
            self._mes += 1
            if self._mes > 12:
                self._mes = 1
                self._anio += 1
        return Fecha(self._dias, self._mes, self._anio)
    def dia_siguiente(self) -> 'Fecha':
        self._dias += 1
        
        while self._dias > 31:
            self._dias -= 31
            self._mes += 1
            if self._mes > 12:
                self._mes = 1
                self._anio += 1
        return Fecha(self._dias, self._mes, self._anio)
    def igual_que(self, otra_fecha:'Fecha') -> bool:
        if self._dias == otra_fecha._dias and self._mes == otra_fecha._mes and self._anio == otra_fecha._anio:
            return True
        return False