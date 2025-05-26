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

class Socio:
    def __init__(self, nombre: str, fecha_nacimiento: 'Fecha'):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de caracteres.")
        if not isinstance(fecha_nacimiento, Fecha):
            raise ValueError("La fecha de nacimiento debe ser una instancia de Fecha.")
        self._nombre = nombre
        self._fecha_nacimiento = fecha_nacimiento
        self._fecha_penalizacion = None
    def establecer_nombre(self, nombre:str):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres.")
    def establecer_fecha_nacimiento(self, fecha_nacimiento: 'Fecha'):
        if isinstance(fecha_nacimiento, Fecha):
            self._fecha_nacimiento = fecha_nacimiento
        else:
            raise ValueError("La fecha de nacimiento debe ser una instancia de Fecha.")
    def establecer_fecha_penalizacion(self, fecha_penalizacion:Fecha or None):
        if fecha_penalizacion is None or isinstance(fecha_penalizacion, Fecha):
            self._fecha_penalizacion = fecha_penalizacion
        else:
            raise ValueError("La fecha de penalización debe ser None o una instancia de Fecha.")
    #consultas
    def esta_habilitado(self, fecha: 'Fecha') -> bool:
        if not isinstance(fecha, Fecha):
            raise ValueError("La fecha debe ser una instancia de Fecha.")
        if self._fecha_penalizacion is None or self._fecha_penalizacion < fecha:
            return True
        return False
    def obtener_nombre(self) -> str:
        return self._nombre
    def obtener_fecha_nacimiento(self) -> 'Fecha':
        return self._fecha_nacimiento
    def obtener_fecha_penalizacion(self) -> 'Fecha':
        return self._fecha_penalizacion
    def __str__(self) -> str:
        return f"Socio(nombre: {self._nombre}, fecha_nacimiento: {self._fecha_nacimiento}, fecha_penalización: {self._fecha_penalizacion})"

class Libro:
    def __init__(self, nombre:str, autor:str, editorial:str, categoria:str):
        if not isinstance(nombre, str) or not isinstance(autor, str) or not isinstance(editorial, str) or not isinstance(categoria, str):
            raise ValueError("Los parámetros deben ser cadenas de caracteres.")
        self._nombre = nombre
        self._autor = autor
        self._editorial = editorial
        self._categoria = categoria
    def establecer_nombre(self, nombre:str):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres.")
    def establecer_autor(self, autor:str):
        if isinstance(autor, str):
            self._autor = autor
        else:
            raise ValueError("El autor debe ser una cadena de caracteres.")
    def establecer_editorial(self, editorial:str):
        if isinstance(editorial, str):
            self._editorial = editorial
        else:
            raise ValueError("La editorial debe ser una cadena de caracteres.")
    def establecer_categoria(self, categoria: str):
        if isinstance(categoria, str) and categoria.upper() in ['A', 'B', 'C']:
            self._categoria = categoria.upper()
        else:
            raise ValueError("La categoría debe ser A, B o C.")
    def obtener_nombre(self)->str:
        return self._nombre
    def obtener_autor(self)->str:
        return self._autor
    def obtener_editorial(self)->str:
        return self._editorial
    def obtener_categoria(self)->str:
        return self._categoria
    def __str__(self)->str:
        return f"Libro(nombre: {self._nombre}, autor: {self._autor}, editorial: {self._editorial}, categoria: {self._categoria})"

class Prestamo:
    def __init__(self, libro: 'Libro', socio: 'Socio', fecha_prestamo: 'Fecha', dias: int):
        if not isinstance(libro, Libro):
            raise ValueError("El libro debe ser una instancia de Libro.")
        if not isinstance(socio, Socio):
            raise ValueError("El socio debe ser una instancia de Socio.")
        if not isinstance(fecha_prestamo, Fecha):
            raise ValueError("La fecha de préstamo debe ser una instancia de Fecha.")
        if dias <= 0:
            raise ValueError("Los días de préstamo deben ser mayores a 0.")
        self._libro = libro
        self._socio = socio
        self._fecha_prestamo = fecha_prestamo
        self._dias = dias
        self._fecha_devolucion = None
    def establecer_fecha_devolucion(self, fecha_devolucion: 'Fecha'):
        if not isinstance(fecha_devolucion, Fecha):
            raise ValueError("La fecha de devolución debe ser una instancia de Fecha.")
        if fecha_devolucion.es_anterior(self._fecha_prestamo):
            raise ValueError("La fecha de devolución no puede ser anterior a la fecha de préstamo.")
        
        self._fecha_devolucion = fecha_devolucion
        # Verificar penalización
        fecha_limite = self._fecha_prestamo.suma_dias(self._dias)
        if fecha_devolucion.es_anterior(fecha_limite) or fecha_devolucion.igual_que(fecha_limite):
            self._socio.establecer_fecha_penalizacion(None)  # No hay penalización.
        else:
            self._socio.establecer_fecha_penalizacion(self.penalizacion())
    def obtener_fecha_devolucion(self) -> 'Fecha':
        return self._fecha_devolucion
    def esta_atrasado(self, fecha_actual: 'Fecha') -> bool:
        if self._fecha_devolucion is not None:
            return False  # Ya se devolvió.
        fecha_limite = self._fecha_prestamo.suma_dias(self._dias)
        return fecha_actual.es_anterior(fecha_limite) is False
    def penalizacion(self) -> 'Fecha':
        if not self._fecha_devolucion:
            raise ValueError("El libro no ha sido devuelto, no se puede calcular la penalización.")
        
        fecha_limite = self._fecha_prestamo.suma_dias(self._dias)
        dias_atraso = (self._fecha_devolucion._dias - fecha_limite._dias) + \
                      ((self._fecha_devolucion._mes - fecha_limite._mes) * 30) + \
                      ((self._fecha_devolucion._anio - fecha_limite._anio) * 365)
        if dias_atraso < 7:
            dias_penalizacion = 3
        elif dias_atraso < 21:
            dias_penalizacion = 5
        else:
            dias_penalizacion = 10
        if self._libro.obtener_categoria() == "A":
            dias_penalizacion *= 2
        return self._fecha_devolucion.suma_dias(dias_penalizacion)