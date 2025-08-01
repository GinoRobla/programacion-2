from modelos.entidades.bebidaConAlcohol import BebidaConAlcohol
from modelos.entidades.bebidaSinAlcohol import BebidaSinAlcohol
from modelos.entidades.bebida import Bebida
import json

class RepositorioBebidas:
    ruta_archivo = r"C:\Users\Gino\Desktop\Programacion\Proyectos BDD 1 y prog 2\Api-rest con python y flask\datos\bebidas.json"

    def __init__(self):
        self.__bebidas = []
        self.__cargarBebidas()

    def __cargarBebidas(self):
        try:
            with open(RepositorioBebidas.ruta_archivo, "r") as archivo:
                lista_dicc_bebidas = json.load(archivo)
                for bebida in lista_dicc_bebidas:
                    if "graduacionAlcoholica" in bebida:
                        self.__bebidas.append(BebidaConAlcohol.fromDiccionario(bebida))
                    else:
                        self.__bebidas.append(BebidaSinAlcohol.fromDiccionario(bebida))
        except FileNotFoundError:
            print("No se encontró el archivo de bebidas")
        except Exception as e:
            print("Error cargando las bebidas del archivo.\n" + str(e))

    def __guardarBebidas(self):
        try:
            with open(RepositorioBebidas.ruta_archivo, "w") as archivo:
                lista_dicc_bebidas = [bebida.toDiccionario() for bebida in self.__bebidas]
                json.dump(lista_dicc_bebidas, archivo, indent=4)
        except Exception as e:
            print("Error guardando las bebidas en el archivo.\n" + str(e))
    
    def obtenerBebidas(self):
        """Retorna una lista con todas las bebidas"""
        return self.__bebidas
    
    def obtenerBebidaPorNombre(self, nombre:str) -> Bebida:
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError("El nombre debe ser un string válido.")
        """Retorna la bebida con el nombre indicado, None si no existe"""
        for bebida in self.__bebidas:
            if bebida.obtenerNombre().lower() == nombre.lower():  # corregido
                return bebida
        return None
    
    def existeBebida(self, nombre:str) -> bool:
        """Retorna True si existe una bebida con el nombre indicado, False en caso contrario"""
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError("El nombre debe ser un string válido.")        
        for bebida in self.__bebidas:
            if bebida.obtenerNombre().lower() == nombre.lower():
                return True
        return False

    def agregarBebida(self, bebida: Bebida) -> Bebida:
        if not isinstance(bebida, Bebida):
            raise ValueError("El objeto debe ser una instancia de Bebida")
        """Agrega una bebida al repositorio. Lanza ValueError si ya existe una bebida con el mismo nombre"""
        if self.existeBebida(bebida.obtenerNombre()):
            raise ValueError("Ya existe una bebida con ese nombre")
        self.__bebidas.append(bebida)
        self.__guardarBebidas()

    def actualizarBebida(self, nombre:str, bebida: Bebida) -> bool:
        if not isinstance(bebida, Bebida):
            raise ValueError("El objeto debe ser una instancia de Bebida")
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError("El nombre debe ser un string válido.")
        """Actualiza los datos de una bebida en base a su nombre. Retorna True si la bebida fue actualizada, False en caso contrario"""
        for bebida_a_modificar in self.__bebidas:
            if bebida_a_modificar.obtenerNombre().lower() == nombre.lower():  # corregido
                self.__bebidas.remove(bebida_a_modificar)
                self.__bebidas.append(bebida)
                self.__guardarBebidas()
                return True
        return False
    
    def eliminarBebida(self, nombre:str) -> bool:
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError("El nombre debe ser un string válido.")
        """Elimina una bebida en base a su nombre. Retorna True si la bebida fue eliminada, False en caso contrario"""
        for bebida in self.__bebidas:
            if bebida.obtenerNombre().lower() == nombre.lower():  # corregido
                self.__bebidas.remove(bebida)
                self.__guardarBebidas()
                return True
        return False