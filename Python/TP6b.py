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

class Borde:
    def __init__(self, grosor: int, color: RGB):
        if not isinstance(grosor, int) or grosor < 0:
            raise ValueError("El grosor debe ser un número entero mayor o igual a 0.")
        if not isinstance(color, RGB):
            raise ValueError("El color debe ser un objeto de la clase RGB.")
        self._grosor = grosor
        self._color = color
    def copiarValores(self, otroBorde: 'Borde'):
        if not isinstance(otroBorde, Borde):
            raise ValueError("El argumento debe ser un objeto de la clase Borde.")
        self._grosor = otroBorde._grosor
        self._color = otroBorde._color
    def clonar(self) -> 'Borde':
        return Borde(self._grosor, self._color.clonar())
    def esIgualQue(self, otroBorde: 'Borde') -> bool:
        if not isinstance(otroBorde, Borde):
            raise ValueError("El argumento debe ser un objeto de la clase Borde.")
        if self._grosor == otroBorde._grosor and self._color == otroBorde._color:
            return True
        return False
    def obtenerGrosor(self) -> int:
        return self._grosor
    def obtenerColor(self) -> RGB:
        return self._color
    def __str__(self):
        return f"Borde(grosor: {self._grosor}, color: {str(self._color)})"