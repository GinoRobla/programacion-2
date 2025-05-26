from abc import ABC, abstractmethod

# Clase abstracta Producto
class Producto(ABC):
    def __init__(self, nombre: str, precio: float, tasaImpuesto: float):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un string.")
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("El precio debe ser un número positivo.")
        if not isinstance(tasaImpuesto, (float, int)) or not (0 <= tasaImpuesto <= 1):
            raise ValueError("La tasa de impuesto debe estar entre 0 y 1.")
        self._nombre = nombre
        self._precio = precio
        self._tasaImpuesto = tasaImpuesto
    
    # Métodos de consulta (getters)
    def get_nombre(self) -> str:
        return self._nombre
    def get_precio(self) -> float:
        return self._precio
    def get_tasaImpuesto(self) -> float:
        return self._tasaImpuesto
    
    # Métodos para establecer valores (setters)
    def set_nombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un string.")
        self._nombre = nombre
    def set_precio(self, precio: float):
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("El precio debe ser un número positivo.")
        self._precio = precio
    def set_tasaImpuesto(self, tasaImpuesto: float):
        if not isinstance(tasaImpuesto, (float, int)) or not (0 <= tasaImpuesto <= 1):
            raise ValueError("La tasa de impuesto debe estar entre 0 y 1.")
        self._tasaImpuesto = tasaImpuesto
    
    @abstractmethod
    def calcularImpuesto(self) -> float:
        pass



# Clase ProductoNacional
class ProductoNacional(Producto):
    def calcularImpuesto(self) -> float:
        return self._precio * self._tasaImpuesto



# Clase ProductoImportado
class ProductoImportado(Producto):
    def __init__(self, nombre: str, precio: float, tasaImpuesto: float, tasaArancel: float):
        super().__init__(nombre, precio, tasaImpuesto)
        if not isinstance(tasaArancel, (float, int)) or not (0 <= tasaArancel <= 1):
            raise ValueError("La tasa de arancel debe estar entre 0 y 1.")
        self._tasaArancel = tasaArancel
    
    # Getter y setter para tasaArancel
    def get_tasaArancel(self) -> float:
        return self._tasaArancel
    def set_tasaArancel(self, tasaArancel: float):
        if not isinstance(tasaArancel, (float, int)) or not (0 <= tasaArancel <= 1):
            raise ValueError("La tasa de arancel debe estar entre 0 y 1.")
        self._tasaArancel = tasaArancel
    def calcularImpuesto(self) -> float:
        impuesto = self._precio * self._tasaImpuesto
        arancel = self._precio * self._tasaArancel
        return impuesto + arancel



# Clase ProductoDeLujo
class ProductoDeLujo(Producto):
    def __init__(self, nombre: str, precio: float, tasaImpuesto: float, tasaImpuestoDeLujo: float):
        super().__init__(nombre, precio, tasaImpuesto)
        if not isinstance(tasaImpuestoDeLujo, (float, int)) or not (0 <= tasaImpuestoDeLujo <= 1):
            raise ValueError("La tasa de impuesto de lujo debe estar entre 0 y 1.")
        self._tasaImpuestoDeLujo = tasaImpuestoDeLujo
    
    # Getter y setter para tasaImpuestoDeLujo
    def get_tasaImpuestoDeLujo(self) -> float:
        return self._tasaImpuestoDeLujo
    def set_tasaImpuestoDeLujo(self, tasaImpuestoDeLujo: float):
        if not isinstance(tasaImpuestoDeLujo, (float, int)) or not (0 <= tasaImpuestoDeLujo <= 1):
            raise ValueError("La tasa de impuesto de lujo debe estar entre 0 y 1.")
        self._tasaImpuestoDeLujo = tasaImpuestoDeLujo
    def calcularImpuesto(self) -> float:
        impuesto_base = self._precio * self._tasaImpuesto
        impuesto_lujo = self._precio * self._tasaImpuestoDeLujo
        return impuesto_base + impuesto_lujo