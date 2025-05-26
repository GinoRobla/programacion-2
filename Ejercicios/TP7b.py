from abc import ABC, abstractmethod
class Inmueble(ABC):
    def __init__(self, codigo:int, domicilio:str, propietario:str, metrosCuadrado:int, estado:int):
        if not isinstance(codigo, int) or codigo <= 0:
            raise TypeError
        if not isinstance(domicilio, str):
            raise TypeError
        if not isinstance(propietario, str):
            raise TypeError
        if not isinstance(metrosCuadrado, int) or metrosCuadrado <= 0:
            raise TypeError
        if not isinstance(estado, int) or estado < 0 or estado > 1:
            raise TypeError
        self._codigo = codigo
        self._domicilio = domicilio
        self._propietario = propietario
        self._metrosCuadrado = metrosCuadrado
        self._estado = estado
    
    
    def establecerCodigo(self, codigo):
        if not isinstance(codigo, int) or codigo <= 0:
            raise TypeError
        self._codigo = codigo
    def establecerDomicilio(self, domicilio):
        if not isinstance(domicilio, str):
            raise TypeError
        self._domicilio = domicilio
    def establecerPropietario(self, propietario):
        if not isinstance(propietario, str):
            raise TypeError
        self._propietario = propietario
    def establecerMetrosCuadrado(self, metrosCuadrado):
        if not isinstance(metrosCuadrado, int) or metrosCuadrado <= 0:
            raise TypeError
        self._metrosCuadrado = metrosCuadrado
    def establecerEstado(self, estado):
        if not isinstance(estado, int) or estado < 0 or estado > 1:
            raise TypeError
        self._estado = estado
    
    
    def obtenerCodigo(self) -> int:
        return self._codigo
    def obtenerDomicilio(self) -> str:
        return self._domicilio
    def obtenerPropietario(self) -> str:
        return self._propietario
    def obtenerMetrosCuadrado(self) -> int:
        return self._metrosCuadrado
    def obtenerEstado(self) -> int:
        return self._estado
    
    
    @abstractmethod
    def costoAlquiler(self) -> float:
        pass
    @abstractmethod
    def precioVenta(self) -> float:
        pass


class Quinta(Inmueble):
    def __init__(self, codigo: int, domicilio: str, propietario: str, metrosCuadrado: int, estado: int, metrosParque: int):
        super().__init__(codigo, domicilio, propietario, metrosCuadrado, estado)
        if not isinstance(metrosParque, int) or metrosParque <= 0:
            raise TypeError
        self._metrosParque = metrosParque
    
    def establecerMetrosParque(self, metrosParque):
        if not isinstance(metrosParque, int) or metrosParque <= 0:
            raise TypeError
        self._metrosParque = metrosParque
    
    def obtenerMetrosParque(self) -> int:
        return self._metrosParque
    
    def costoAlquiler(self, base: int) -> float:
        """
        Calcula el costo del alquiler considerando:
        - base: costo base por metro cuadrado.
        - Incrementa el costo según los metros del parque (10% adicional por m² del parque).
        """
        if not isinstance(base, int) or base <= 0:
            raise ValueError("La base debe ser un entero positivo.")
        costo = (self._metrosCuadrado + self._metrosParque * 0.1) * base
        return costo
    
    def precioVenta(self, base: int) -> float:
        """
        Calcula el precio de venta considerando:
        - base: precio base por metro cuadrado.
        - Incrementa el precio según los metros del parque (20% adicional por m² del parque).
        """
        if not isinstance(base, int) or base <= 0:
            raise ValueError("La base debe ser un entero positivo.")
        precio = (self._metrosCuadrado + self._metrosParque * 0.2) * base
        return precio


class Departamento(Inmueble):
    def __init__(self, codigo: int, domicilio: str, propietario: str, metrosCuadrado: int, estado: int, gastosComunes: float, cochera: bool):
        super().__init__(codigo, domicilio, propietario, metrosCuadrado, estado)
        if not isinstance(gastosComunes, (int, float)) or gastosComunes < 0:
            raise TypeError("Los gastos comunes deben ser un número positivo.")
        if not isinstance(cochera, bool):
            raise TypeError("El valor de cochera debe ser booleano (True o False).")
        self._gastosComunes = gastosComunes
        self._cochera = cochera

    def establecerGastosComunes(self, gastosComunes):
        if not isinstance(gastosComunes, (int, float)) or gastosComunes < 0:
            raise TypeError("Los gastos comunes deben ser un número positivo.")
        self._gastosComunes = gastosComunes

    def establecerCochera(self, cochera):
        if not isinstance(cochera, bool):
            raise TypeError("El valor de cochera debe ser booleano (True o False).")
        self._cochera = cochera

    def obtenerGastosComunes(self) -> float:
        return self._gastosComunes

    def obtenerCochera(self) -> bool:
        return self._cochera

    def costoAlquiler(self, base: int) -> float:
        """
        Calcula el costo del alquiler considerando:
        - base: costo base por metro cuadrado.
        - Incrementa el costo según los gastos comunes.
        - Si tiene cochera, suma un monto adicional fijo (50% de la base).
        """
        if not isinstance(base, int) or base <= 0:
            raise ValueError("La base debe ser un entero positivo.")
        costo = self._metrosCuadrado * base + self._gastosComunes
        if self._cochera:
            costo += base * 0.5  # Incremento por cochera
        return costo

    def precioVenta(self, base: int) -> float:
        """
        Calcula el precio de venta considerando:
        - base: precio base por metro cuadrado.
        - Incrementa el precio según los gastos comunes.
        - Si tiene cochera, suma un monto adicional fijo (10% del precio base).
        """
        if not isinstance(base, int) or base <= 0:
            raise ValueError("La base debe ser un entero positivo.")
        precio = self._metrosCuadrado * base
        if self._cochera:
            precio += base * 0.1  # Incremento por cochera
        return precio