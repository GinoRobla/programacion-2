from abc import ABC, abstractmethod

# Clase abstracta PolizaInmueble
class PolizaInmueble(ABC):
    def __init__(self, numero: int, incendio: float, explosion: float, robo: float):
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("El número de póliza debe ser un entero positivo.")
        if not isinstance(incendio, (float, int)) or incendio < 0:
            raise ValueError("El monto por incendio debe ser un número no negativo.")
        if not isinstance(explosion, (float, int)) or explosion < 0:
            raise ValueError("El monto por explosión debe ser un número no negativo.")
        if not isinstance(robo, (float, int)) or robo < 0:
            raise ValueError("El monto por robo debe ser un número no negativo.")
        
        self._numero = numero
        self._incendio = incendio
        self._explosion = explosion
        self._robo = robo
    
    # Getters
    def get_numero(self) -> int:
        return self._numero
    def get_incendio(self) -> float:
        return self._incendio
    def get_explosion(self) -> float:
        return self._explosion
    def get_robo(self) -> float:
        return self._robo
    
    # Setters
    def set_numero(self, numero: int):
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("El número de póliza debe ser un entero positivo.")
        self._numero = numero
    def set_incendio(self, incendio: float):
        if not isinstance(incendio, (float, int)) or incendio < 0:
            raise ValueError("El monto por incendio debe ser un número no negativo.")
        self._incendio = incendio
    def set_explosion(self, explosion: float):
        if not isinstance(explosion, (float, int)) or explosion < 0:
            raise ValueError("El monto por explosión debe ser un número no negativo.")
        self._explosion = explosion
    def set_robo(self, robo: float):
        if not isinstance(robo, (float, int)) or robo < 0:
            raise ValueError("El monto por robo debe ser un número no negativo.")
        self._robo = robo
    @abstractmethod
    def costo_poliza(self) -> float:
        pass


# Clase PolizaInmuebleEscolar
class PolizaInmuebleEscolar(PolizaInmueble):
    def __init__(self, numero: int, incendio: float, explosion: float, robo: float, cant_personas: int, monto_equipamiento: float, monto_edilicio: float, monto_personal: float):
        super().__init__(numero, incendio, explosion, robo)
        if not isinstance(cant_personas, int) or cant_personas < 0:
            raise ValueError("La cantidad de personas debe ser un entero no negativo.")
        if not isinstance(monto_equipamiento, (float, int)) or monto_equipamiento < 0:
            raise ValueError("El monto por equipamiento debe ser un número no negativo.")
        if not isinstance(monto_edilicio, (float, int)) or monto_edilicio < 0:
            raise ValueError("El monto edilicio debe ser un número no negativo.")
        if not isinstance(monto_personal, (float, int)) or monto_personal < 0:
            raise ValueError("El monto personal debe ser un número no negativo.")
        
        self._cant_personas = cant_personas
        self._monto_equipamiento = monto_equipamiento
        self._monto_edilicio = monto_edilicio
        self._monto_personal = monto_personal
    
    # Getters
    def get_cant_personas(self) -> int:
        return self._cant_personas
    def get_monto_equipamiento(self) -> float:
        return self._monto_equipamiento
    def get_monto_edilicio(self) -> float:
        return self._monto_edilicio
    def get_monto_personal(self) -> float:
        return self._monto_personal
    
    # Setters
    def set_cant_personas(self, cant_personas: int):
        if not isinstance(cant_personas, int) or cant_personas < 0:
            raise ValueError("La cantidad de personas debe ser un entero no negativo.")
        self._cant_personas = cant_personas
    def set_monto_equipamiento(self, monto_equipamiento: float):
        if not isinstance(monto_equipamiento, (float, int)) or monto_equipamiento < 0:
            raise ValueError("El monto por equipamiento debe ser un número no negativo.")
        self._monto_equipamiento = monto_equipamiento
    def set_monto_edilicio(self, monto_edilicio: float):
        if not isinstance(monto_edilicio, (float, int)) or monto_edilicio < 0:
            raise ValueError("El monto edilicio debe ser un número no negativo.")
        self._monto_edilicio = monto_edilicio
    def set_monto_personal(self, monto_personal: float):
        if not isinstance(monto_personal, (float, int)) or monto_personal < 0:
            raise ValueError("El monto personal debe ser un número no negativo.")
        self._monto_personal = monto_personal
    def costo_poliza(self) -> float:
        return (
            self.get_incendio() +
            self.get_explosion() +
            self.get_robo() +
            self._monto_equipamiento +
            self._monto_edilicio +
            self._monto_personal
        )


class Aseguradora:
    def __init__(self, nombre: str):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un string.")
        self._nombre = nombre
        self._asegurados = []  
    
    #comandos
    def agregar_asegurado(self, asegurado):
        if asegurado in self._asegurados:
            raise ValueError("El asegurado ya está registrado.")
        self._asegurados.append(asegurado)
    def eliminar_asegurado(self, asegurado):
        if asegurado not in self._asegurados:
            raise ValueError("El asegurado no se encuentra en la lista.")
        self._asegurados.remove(asegurado)
    def buscar_asegurado(self, numero_poliza: int):
        for asegurado in self._asegurados:
            if asegurado.get_numero_poliza() == numero_poliza:
                return asegurado
        return None  
    def listar_asegurados(self):
        return self._asegurados[:]
    
    #consultas
    def get_nombre(self) -> str:
        return self._nombre
    def get_asegurados(self):
        return self._asegurados[:]
    def set_nombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un string.")
        self._nombre = nombre