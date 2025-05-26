def leer_entero(mensaje:str)->int:
    repetir = True
    while repetir:
        try:
            valor = int(input(mensaje))
            repetir = False
        except:
            print("Error, debes ingresar un número entero")
    return valor

# 1.	Implemente una función que, dada una lista de números, devuelva una nueva lista que contenga el cuadrado de cada número utilizando list comprehensions.

def cuadrados_de_la_lista(lista:list[int])->list[int]:
    """Dada una lista de números, devuelve una nueva lista que contenga el cuadrado de cada número."""
    return [x**2 for x in lista]

# 2.	Implemente una función que, dada una lista de nombres, devuelva una nueva lista que contenga solo los nombres que tengan una longitud 
# mayor o igual a una cantidad de caracteres pasada por parámetro, utilizando list comprehensions.

def nombres_con_longitud_mayor_o_igual_a(lista:list[str], longitud:int)->list[str]:
    """Dada una lista de nombres, devuelve una nueva lista que contenga solo los nombres que tengan una longitud mayor o igual a la longitud pasada por parámetro."""
    return [nombre for nombre in lista if len(nombre)>=longitud]

# 3.	Lee el contenido de un archivo de texto llamado "datos.txt" y crea una lista con todas las líneas del archivo, utilizando list comprehensions.

def ejercicio3():
    """Lee el contenido de un archivo de texto y crea una lista con todas las líneas del archivo."""
    with open("datos.txt", "r") as archivo:
        lista_lineas = [linea.strip() for linea in archivo]
    return lista_lineas

# 4.	Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo las palabras que comienzan con una letra específica (por ejemplo, "a") 
# indicada por el usuario, utilizando list comprehensions.

def ejercicio4():
    """Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo las palabras que comienzan con una letra específica indicada por el usuario."""
    diccionario = {"casa": "Lugar donde se habita", "auto": "Vehículo de motor", "perro": "Animal doméstico", "gato": "Animal doméstico"}
    # pedimos una letra (tomamos el primer caracter en caso que ingrese una palabra)
    letra = input("Ingrese una letra: ")[0]
    lista_palabras = [palabra for palabra in diccionario if palabra[0].lower()==letra.lower()]
    print(f"Palabras que comienzan con '{letra}': {lista_palabras}")

# 5.	Dado un rango de números, crea una lista que contenga todos los números primos dentro de ese rango utilizando list comprehensions.

def es_primo(numero:int)->bool:
    """Determina si un número es primo."""
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def ejercicio5():
    """Dado un rango de números, crea una lista que contenga todos los números primos dentro de ese rango."""
    inicio = leer_entero("Ingrese el número de inicio del rango: ")
    fin = leer_entero("Ingrese el número de fin del rango: ")
    lista_primos = [numero for numero in range(inicio, fin+1) if es_primo(numero)]
    print(f"Números primos en el rango {inicio} - {fin}: {lista_primos}")

# 6.	Dado un diccionario de personas y sus edades, crea una lista que contenga solo los nombres de las personas cuya edad es mayor a una edad ingresada por el usuario,
#  utilizando list comprehensions.

def ejercicio6():
    """Dado un diccionario de personas y sus edades, crea una lista que contenga solo los nombres de las personas cuya edad es mayor a una edad ingresada por el usuario."""
    diccionario = {"Juan": 20, "Maria": 30, "Pedro": 40, "Ana": 50}
    edad=leer_entero("Ingrese una edad: ")
    lista_nombres = [nombre for nombre, edad_persona in diccionario.items() if edad_persona > edad]
    print(f"Personas mayores a {edad} años: {lista_nombres}")

# 7.	Implemente un programa que le pida una palabra al usuario y cuenta la cantidad de vocales en ella. El programa deberá pedirle palabras al usuario hasta que éste
#  introduzca la palabra “salir”.

def contar_vocales(palabra:str)->int:
    """Cuenta la cantidad de vocales en una palabra."""
    contador =0 
    for letra in palabra:
        if letra.lower() in "aeiouáéíóú":
            contador += 1
    return contador

def ejercicio7():
    palabra =""
    while palabra.lower() != "salir":
        palabra = input("Ingrese una palabra o 'salir' para terminar: ")
        if palabra.lower() != "salir":
            print(f"La palabra tiene {contar_vocales(palabra)} vocales.")

# 8.	Dada una lista con elementos duplicados, crea una nueva lista que contenga solo los elementos únicos utilizando list comprehensions.

def ejercicio8():
    lista=[1,1,1,2,2,2,3,3,3,4,4,4,5,6,7,8,9]
    lista_unicos= [elemento for elemento in lista if lista.count(elemento) == 1]
    print(f"Lista original: {lista}")
    print(f"Lista de elementos únicos: {lista_unicos}")

# 9.	Dada una lista de números, crea dos listas separadas: una que contenga los números pares y otra que contenga los números impares utilizando list comprehensions.

def ejercicio9():
    lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    pares = [numero for numero in lista if numero % 2 == 0]
    impares = [numero for numero in lista if numero % 2 != 0]
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")

# 10.	Dada una lista de diccionarios que contienen información de estudiantes de una materia (nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final) ,
#  utilizando list comprehensions:
# a.	Crea una lista que contenga los nombres de todos los estudiantes. Salida ejemplo: nombres: ['Pepe', 'María', 'Pedro', 'Ana']
# b.	Crea una lista que contenga los nombres de todos los estudiantes que han obtenido una calificación superior a 70 en todos los exámenes
# c.	Crea una lista que contenga los nombres de todos los estudiantes que han obtenido una calificación inferior a 60 en al menos un examen.

def ejercicio10():
    estudiantes = [
        {"nombre_apellido": "Juan Perez", "legajo": 123, "nota_parcial1": 80, "nota_parcial2": 70, "nota_final": 75},
        {"nombre_apellido": "Maria Rodriguez", "legajo": 124, "nota_parcial1": 60, "nota_parcial2": 70, "nota_final": 65},
        {"nombre_apellido": "Pedro Gomez", "legajo": 125, "nota_parcial1": 70, "nota_parcial2": 80, "nota_final": 75},
        {"nombre_apellido": "Ana Fernandez", "legajo": 126, "nota_parcial1": 50, "nota_parcial2": 60, "nota_final": 55}
    ]
    # a
    nombres = [estudiante["nombre_apellido"] for estudiante in estudiantes]
    print(f"Nombres: {nombres}")
    # b
    aprobados = [estudiante["nombre_apellido"] for estudiante in estudiantes if estudiante["nota_parcial1"] > 70 and estudiante["nota_parcial2"] > 70 and estudiante["nota_final"] > 70]
    print(f"Aprobados: {aprobados}")
    # c
    desaprobados = [estudiante["nombre_apellido"] for estudiante in estudiantes if estudiante["nota_parcial1"] < 60 or estudiante["nota_parcial2"] < 60 or estudiante["nota_final"] < 60]
    print(f"Desaprobados: {desaprobados}")