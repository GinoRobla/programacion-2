class Atleta:
    # Atributos de clase
    max_valor = 100
    min_valor = 0

    def __init__(self, nombre: str):  # Constructor
        # Validaciones
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de caracteres.")
        # Atributos de instancia
        self._nombre = nombre
        self._energia = Atleta.max_valor
        self._destreza = Atleta.min_valor
        self._cantidadEntrenamiento = atleta.min_valor

    # Comandos
    def entrenar(self):
        if self._energia - 5 < Atleta.min_valor:
            raise ValueError("No tienes suficiente energía para entrenar.")
        self._energia -= 5
        self._cantidadEntrenamiento += 1
        if self._cantidadEntrenamiento == 5:
            self._destreza += 1
            self._cantidadEntrenamiento = 0

    def descansar(self):
        nueva_energia = self._energia + 20
        self._energia = min(nueva_energia, Atleta.max_valor)

    # Métodos de clase
    @classmethod
    def establecer_max_valor(cls, max_valor):
        if isinstance(max_valor, int) and max_valor > cls.min_valor:
            cls.max_valor = max_valor
        else:
            raise ValueError("El valor máximo debe ser un entero mayor que el valor mínimo.")

    @classmethod
    def establecer_min_valor(cls, min_valor):
        if isinstance(min_valor, int) and min_valor < cls.max_valor:
            cls.min_valor = min_valor
        else:
            raise ValueError("El valor mínimo debe ser un entero menor que el valor máximo.")

    # Consultas
    def __str__(self):
        return f"Atleta: {self._nombre}, Energía: {self._energia}, Destreza: {self._destreza}"

# Tester para la clase Atleta
if __name__ == "__main__":
    # Configuración inicial de la clase
    Atleta.establecer_min_valor(0)
    Atleta.establecer_max_valor(100)
    
    # Crear un atleta
    print("Creando un atleta llamado 'Usain Bolt'...")
    atleta = Atleta("Usain Bolt")
    
    # Mostrar el estado inicial del atleta
    print("Estado inicial del atleta:")
    print(atleta)
    
    # Entrenar varias veces
    print("\nEntrenando al atleta...")
    for i in range(6):  # Entrena 6 veces
        try:
            atleta.entrenar()
            print(f"Entrenamiento {i+1}: {atleta}")
        except ValueError as e:
            print(f"Error durante el entrenamiento: {e}")
    
    # Descansar y recuperar energía
    print("\nDescansando para recuperar energía...")
    atleta.descansar()
    print("Estado del atleta después de descansar:")
    print(atleta)
    
    # Intentar entrenar cuando la energía está baja
    print("\nAgotando energía y probando límites...")
    while True:
        try:
            atleta.entrenar()
            print(atleta)
        except ValueError as e:
            print(f"Error: {e}")
            break
    
    # Mostrar el estado final del atleta
    print("\nEstado final del atleta:")
    print(atleta)