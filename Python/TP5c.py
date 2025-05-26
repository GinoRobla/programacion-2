class RGB:
    #atributos de clase
    def __init__(self, rojo = 0, verde = 0, azul = 0): #constructor
        #validacion
        if not isinstance(rojo, int) or rojo < 0 or rojo > 255:
            raise ValueError("El valor del rojo debe estar entre 0 y 255.")
        if not isinstance(verde, int) or verde < 0 or verde > 255:
            raise ValueError("El valor del verde debe estar entre 0 y 255.")
        if not isinstance(azul, int) or azul < 0 or azul > 255:
            raise ValueError("El valor del azul debe estar entre 0 y 255.")
        #atributos de instancia
        self._rojo = rojo
        self._verde = verde
        self._azul = azul
    
    # Comandos
    def variar(self, valor: int):
        if not isinstance(valor, int):
            raise ValueError("El valor debe ser un número entero.")
        self._rojo = min(max(self._rojo + valor, 0), 255)
        self._verde = min(max(self._verde + valor, 0), 255)
        self._azul = min(max(self._azul + valor, 0), 255)

    def variarRojo(self, valor:int):
        if isinstance(self._rojo, int) and valor >= 0 and valor <= 255:
            self._rojo = min(max(self._rojo + valor, 0), 255)
        else:
            raise ValueError("El valor debe ser un entero y estar entre 0 y 255.")
    def variarVerde(self, valor:int):
        if isinstance(self._verde, int) and valor >= 0 and valor <= 255:
            self._verde = min(max(self._verde + valor, 0), 255)
        else:
            raise ValueError("El valor debe ser un entero y estar entre 0 y 255.")
    def variarAzul(self, valor:int):
        if isinstance(self._azul, int) and valor >= 0 and valor <= 255:
            self._azul = min(max(self._azul + valor, 0), 255)
        else:
            raise ValueError("El valor debe ser un entero y estar entre 0 y 255.")
    def establecerRojo(self, valor:int):
        if isinstance(valor, int) and valor >= 0 and valor <= 255:
            self._rojo = valor
        else:
            raise ValueError("El valor debe ser un entero y estar entre 0 y 255.")
    def establecerVerde(self, valor:int):
        if isinstance(valor, int) and valor >= 0 and valor <= 255:
            self._verde = valor
        else:
            raise ValueError("El valor debe ser un entero y estar entre 0 y 255.")
    def establecerAzul(self, valor:int):
        if isinstance(valor, int) and valor >= 0 and valor <= 255:
            self._azul = valor
        else:
            raise ValueError("El valor debe ser un entero y estar entre 0 y 255.")
    def copiar(self, otroColor:'RGB'):
        self._rojo = otroColor._rojo
        self._verde = otroColor._verde
        self._azul = otroColor._azul
    
    # Consultas
    def obtenerRojo(self) -> int:
        return self._rojo
    def obtenerVerde(self) -> int:
        return self._verde
    def obtenerAzul(self) -> int:
        return self._azul
    def esRojo(self) -> bool:
        if self._rojo == 255 and self._verde == 0 and self._azul == 0:
            return True
        return False
    def esGris(self) -> bool:
        if self._rojo == self._verde == self._azul:
            return True
        return False
    def esNegro(self) -> bool:
        if self._rojo == 0 and self._verde == 0 and self._azul == 0:
            return True
        return False
    def complemento(self) -> 'RGB':
        return RGB(255 - self._rojo, 255 - self._verde, 255 - self._azul)
    def esIgualQue(self, otroColor:'RGB')->bool:
        if (self._rojo == otroColor._rojo and
                self._verde == otroColor._verde and
                self._azul == otroColor._azul):
            return True
        return False
    def clonar(self) -> 'RGB':
        return RGB(self._rojo, self._verde, self._azul)
    def __str__(self):
        return f"Color(R: {self._rojo}, G: {self._verde}, B: {self._azul})"

if __name__ == "__main__":
    print("=== Tester de la clase RGB ===")

    # Crear colores iniciales
    print("\nCreando colores...")
    color1 = RGB(255, 0, 0)  # Rojo puro
    color2 = RGB(128, 128, 128)  # Gris
    color3 = RGB()  # Negro por defecto

    print("Color 1:", color1)
    print("Color 2:", color2)
    print("Color 3:", color3)

    # Probar métodos de consulta
    print("\nConsultas:")
    print(f"Color 1 es rojo: {color1.esRojo()}")
    print(f"Color 2 es gris: {color2.esGris()}")
    print(f"Color 3 es negro: {color3.esNegro()}")

    # Probar variaciones
    print("\nVariaciones de colores:")
    color1.variar(-50)
    print("Color 1 tras variar(-50):", color1)

    color2.variarRojo(100)
    print("Color 2 tras variarRojo(100):", color2)

    color3.variar(300)  # Debería quedar en el máximo (255, 255, 255)
    print("Color 3 tras variar(300):", color3)

    # Probar complementos
    print("\nComplemento de colores:")
    complemento_color1 = color1.complemento()
    print("Complemento de Color 1:", complemento_color1)

    complemento_color2 = color2.complemento()
    print("Complemento de Color 2:", complemento_color2)

    # Probar clonación
    print("\nClonando colores:")
    color_clonado = color3.clonar()
    print("Color clonado de Color 3:", color_clonado)

    # Verificar igualdad
    print("\nComparando colores:")
    print(f"Color 1 es igual a su complemento: {color1.esIgualQue(complemento_color1)}")
    print(f"Color 3 es igual a su clon: {color3.esIgualQue(color_clonado)}")

    # Probar métodos de establecimiento
    print("\nEstableciendo nuevos valores:")
    color1.establecerRojo(0)
    color1.establecerVerde(255)
    color1.establecerAzul(0)  # Ahora es verde puro
    print("Color 1 tras establecerRojo(0), establecerVerde(255), establecerAzul(0):", color1)

    # Probar copia de colores
    print("\nCopiando colores:")
    color1.copiar(color2)
    print("Color 1 tras copiar Color 2:", color1)

    print("\n=== Fin del tester ===")