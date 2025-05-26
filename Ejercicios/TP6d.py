class Mascota:
    # Atributos de clase
    def __init__(self, nombre: str, especie: str, edad: int, descripcion: str):
        # Validaciones
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de caracteres.")
        if not isinstance(especie, str):
            raise ValueError("La especie debe ser una cadena de caracteres.")
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un número entero positivo.")
        if not isinstance(descripcion, str):
            raise ValueError("La descripción debe ser una cadena de caracteres.")
        
        # Atributos de instancia
        self._nombre = nombre
        self._especie = especie
        self._edad = edad
        self._descripcion = descripcion
        self._cuidador = None  # Inicialmente no tiene cuidador

    # Comandos
    def asignar_cuidador(self, cuidador):
        if self._cuidador is None:
            self._cuidador = cuidador
        else:
            raise ValueError("Esta mascota ya tiene un cuidador asignado.")

    def obtener_nombre(self) -> str:
        return self._nombre

    def obtener_especie(self) -> str:
        return self._especie

    def obtener_edad(self) -> int:
        return self._edad

    def obtener_descripcion(self) -> str:
        return self._descripcion

    def obtener_cuidador(self):
        return self._cuidador

    def __str__(self):
        return f"Mascota: {self._nombre}, Especie: {self._especie}, Edad: {self._edad}, Descripción: {self._descripcion}"


class Cuidador:
    # Atributos de clase
    def __init__(self, nombre: str, direccion: str, telefono: str):
        # Validaciones
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de caracteres.")
        if not isinstance(direccion, str):
            raise ValueError("La dirección debe ser una cadena de caracteres.")
        if not isinstance(telefono, str):
            raise ValueError("El teléfono debe ser una cadena de caracteres.")
        
        # Atributos de instancia
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._mascotas = []

    # Comandos
    def asignar_mascota(self, mascota):
        if mascota not in self._mascotas:
            self._mascotas.append(mascota)
            mascota.asignar_cuidador(self)  # Asigna esta mascota al cuidador
        else:
            raise ValueError("Esta mascota ya está asignada a este cuidador.")

    def obtener_nombre(self) -> str:
        return self._nombre

    def obtener_direccion(self) -> str:
        return self._direccion

    def obtener_telefono(self) -> str:
        return self._telefono

    def obtener_mascotas(self):
        return self._mascotas

    def __str__(self):
        return f"Cuidador: {self._nombre}, Dirección: {self._direccion}, Teléfono: {self._telefono}"

# Tester básico
if __name__ == "__main__":
    # Crear algunos cuidadores y mascotas
    cuidador1 = Cuidador("Juan Pérez", "Av. Siempre Viva 123", "555-1234")
    mascota1 = Mascota("Rex", "Perro", 3, "Un perro fuerte y juguetón.")
    mascota2 = Mascota("Miau", "Gato", 2, "Un gato tranquilo y cariñoso.")

    # Asignar mascotas a cuidadores
    try:
        cuidador1.asignar_mascota(mascota1)
        cuidador1.asignar_mascota(mascota2)

        # Ver detalles
        print(cuidador1)
        for mascota in cuidador1.obtener_mascotas():
            print(mascota)
    except ValueError as e:
        print(e)