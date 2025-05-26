# 1) Escribir un procedimiento “reverso” que permita ingresar como parámetro una cadena, y devuelva la cadena invertida (“hola” se convierte en “aloh”).
# Escribir luego un programa que determine si una cadena de caracteres es un palíndromo (un palíndromo es un texto que se lee igual en sentido directo y en inverso, ej.: “radar”). 
# Sugerencia: para evitar diferencias entre mayúsculas y minúsculas en las cadenas, utilice la función del tipo string .upper() ó .lower() en las cadenas, ya que Radar es distinto a radaR.
def reverso(palabra:str)->str:
    invertida = ""
    for letra in palabra:
        invertida = letra + invertida
    return invertida

def ejercicio1():
    palabra = input("Ingresa una palabra: " ) 
    invertida = reverso(palabra)
    print(f"Palabra invertida: {invertida}")
    print(f"Palabra original: {palabra}")
    if palabra.lower() == invertida.lower():
        print(f"{palabra} Es palíndromo")
    else:
        print(f"{palabra} No es palíndromo")

# 2) Escriba una función llamada EsBisiesto que permita ingresar un número de año y devuelva verdadero en caso que el año sea bisiesto, o falso cuando no lo es. 
# Un año es bisiesto si: es divisible entre cuatro y (no es divisible entre 100 o es divisible entre 400). 
# Utilizarlo en un programa que permita ingresar dia, mes y año y muestre por pantalla si la fecha es válida o no.
def esBisiesto(anio:int)->bool:
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

# leer_entero la voy a usar en todos los ejercicios que necesiten leer un entero
def leer_entero(mensaje:str)->int:
    repetir = True
    while repetir:
        try:
            valor = int(input(mensaje))
            repetir = False
        except:
            print("Error, debes ingresar un número entero")
    return valor

def ejercicio2():
    dia = leer_entero("Ingrese el día: ")
    mes = leer_entero("Ingrese el mes: ")
    anio = leer_entero("Ingrese el año: ")
    if mes < 1 or mes > 12:
        print("Fecha inválida.")
    elif mes in [1, 3, 5, 7, 8, 10, 12] and (dia < 1 or dia > 31):
        print("Fecha inválida.")
    elif mes in [4, 6, 9, 11] and (dia < 1 or dia > 30):
        print("Fecha inválida.")
    elif mes == 2 and (dia < 1 or (esBisiesto(anio) and dia > 29) or (not esBisiesto(anio) and dia > 28)):
        print("Fecha inválida.")
    else:
        print("Fecha válida.")

# 3)Escriba un programa que permita cargar las notas de exámenes, primero debe permitir ingresar por teclado la cantidad de notas que desea cargar, 
# y luego cargarlas en una lista, y posteriormente debe buscar la nota más alta, mostrarla, e indicar en qué índice del arreglo se encuentra.
def leer_float(mensaje:str)->float:
    repetir = True
    while repetir:
        try:
            valor = float(input(mensaje))
            repetir = False
        except:
            print("Error, debes ingresar un número entero")
    return valor

def obtener_notas(cantidad)->list[float]:
    notas = []
    for i in range(cantidad):
        nota = leer_float(f"Ingrese la nota {i+1}: ")
        notas.append(nota)
    return notas

def buscar_indice_num_mayor(lista_numeros:list[float])->int:
    mayor=lista_numeros[0]
    indice=0
    for i in range(1,len(lista_numeros)):
        if lista_numeros[i]>mayor:
            mayor=lista_numeros[i]
            indice=i
    return indice

def ejercicio3():
    cantidad = leer_entero("Ingrese la cantidad de notas a cargar: ")
    notas = obtener_notas(cantidad)
    indice = buscar_indice_num_mayor(notas)
    mayor= notas[indice]
    print(f"La nota más alta es {mayor} y se encuentra en la posición {indice}.")

# 4) Escriba un programa que permita ingresar un número, se debe validar que realmente se haya ingresado un número, y crear una lista para almacenar 
# por separado los dígitos del número. Luego recorrer la lista y mostrar el índice que contiene el dígito mayor.
def obtener_digitos(numero:int)->list[int]:
    lista_digitos = []
    for digito in str(numero):
        lista_digitos.append(int(digito))
    return lista_digitos

def obtener_digitos_v2(numero:int)->list[int]:
    digitos = []
    while numero > 0:
        digito = numero % 10
        digitos.insert(0, digito)
        numero = numero // 10  
    return digitos

def ejercicio4():
    numero = leer_entero("Ingrese un número: ")
    digitos = obtener_digitos_v2(numero)
    indice = buscar_indice_num_mayor(digitos)
    digito_mayor = digitos[indice]
    print(f"El dígito mayor es {digito_mayor} y se encuentra en la posición {indice}.")


# 5) Escriba un programa que permita cargar una lista de alumnos junto con su nota del parcial. Seleccione la estructura de datos que mejor se adapte al problema. 
# Luego de ingresados los datos debe generar una lista donde figure si aprobaron o no (se aprueba con 40 o más). 
# El listado a mostrar por pantalla debe ser como el siguiente (el resultado no se almacena, se calcula):
# ALUMNOS      		PARCIAL	    	RESULTADO
# Smith, Juan		    70			Aprobado
# Suárez, María		    35			Desaprobado

def pedir_nota(mensaje:str)->int:
    repetir = True
    while repetir:
        nota=leer_entero(mensaje)
        if nota<0 or nota>100:
            print("Error, la nota debe estar entre 0 y 100")
        else:
            repetir=False
    return nota

def obtener_alumnos_con_notas(cantidad:int)->list[dict]:
    alumnos = []
    for i in range(cantidad):
        nombre = input("Ingrese el nombre del alumno: ")
        nota = pedir_nota("Ingrese la nota del parcial: ")
        alumnos.append({"nombre":nombre, "nota":nota, "resultado":"Aprobado" if nota>=40 else "Desaprobado"})
    return alumnos

def ejercicio5():
    cantidad = leer_entero("Ingrese la cantidad de alumnos a cargar: ")
    alumnos = obtener_alumnos_con_notas(cantidad)
    print(f"| {'Nombre':<20} | {'Nota':>5} | {'Resultado':^15} |")
    print('-' * 50) # Línea divisoria
    for alumno in alumnos:
        print(f"| {alumno['nombre']:<20} | {alumno['nota']:>5} | {alumno['resultado']:^15} |")
        print('-' * 50) # Línea divisoria


# 6) Escriba un programa que permita leer de un archivo distancias.txt (cada renglón tiene una distancia válida) las distancias recorridas por el vehículo de una empresa, luego calcular cual es la distancia promedio, y mostrar por pantalla el promedio y todas las distancias mayores al promedio.
# Ej del contenido del archivo:
# 150
# 120
# 50
# 34
# 250
# Salida: “La distancia promedio de los viajes es … y los viajes con distancia mayor son: … , … , …. , …. “

def leer_distancias()->list[int]:
    distancias = []
    try:
        with open("distancias.txt", "r") as archivo:
            for linea in archivo:
                distancia = int(linea)
                distancias.append(distancia)
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except ValueError:
        print("Error al leer un numero del archivo.")
    return distancias

def ejercicio6():
    distancias = leer_distancias()
    suma = 0
    if len(distancias)>0:
        for dist in distancias:
            suma += dist
        promedio = suma / len(distancias)
        dist_mayores=[]
        for dist in distancias:
            if dist > promedio:
                dist_mayores.append(dist)
        print(f"La distancia promedio de los viajes es {promedio} y los viajes con distancia mayor son: {dist_mayores}")
    else:
        print("No hay distancias para calcular el promedio")

# 7) Un almacén guarda los códigos, los nombres de los productos y sus precios, respectivamente, separados por punto y coma ( ; ) en el archivo productos.txt. 
# Hacer un algoritmo y luego los procedimientos necesarios que permitan tomar los datos del archivo y buscar el precio de un artículo ingresado por teclado. 
# Para probar el algoritmo crear un archivo “productos.txt” y cargarle datos al estilo:
# 100;arroz;10
# 102;fideos;5
# 135;lentejas;8
# 138;porotos;6
# 140;sal gruesa;5
# 201;aceite;20       (  etc…  )

def leer_productos()->list[dict]:
    productos = []
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")
                codigo = int(datos[0])
                nombre = datos[1]
                precio = int(datos[2])
                productos.append({"codigo":codigo, "nombre":nombre, "precio":precio})
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except ValueError:
        print("Error al leer un numero del archivo.")
    return productos

def ejercicio7():
    productos = leer_productos()
    codigo = leer_entero("Ingrese el código del producto: ")
    encontrado = False
    for producto in productos:
        if producto["codigo"] == codigo:
            print(f"El precio del producto {producto['nombre']} es {producto['precio']}")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró el producto.")

# 8) El mismo almacén del punto anterior almacena los datos del stock de productos en el archivo stock.txt separados por punto y coma ( ; ) con el formato 
# “codigo de producto; stock mínimo; stock real”. Escriba un programa, que a partir de información contenida en los archivos, genere otro archivo de texto, Compras.txt, 
# conteniendo todos los productos cuyo stock se encuentra por debajo del mínimo. 
# Utilizar el archivo productos.txt del punto anterior, y crear un archivo stock.txt y cargarle datos utilizando los códigos de los productos del archivo anterior. 
# Ej:
# 100;50;60
# 102;50;20
# 135;20;15
# 138;20;20
# 140;10;8
# 201;20;30       (  etc…  )

def leer_stock()->list[dict]:
    stocks = []
    try:
        with open("stock.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")
                codigo = int(datos[0])
                stock_min = int(datos[1])
                stock_real = int(datos[2])
                stocks.append({"codigo":codigo, "stock_min":stock_min, "stock_real":stock_real})
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except ValueError:
        print("Error al leer un numero del archivo.")
    return stocks

def ejercicio8():
    productos = leer_productos()
    stocks = leer_stock()
    with open("Compras.txt", "w") as archivo:
        for stock in stocks:
            if stock["stock_real"] < stock["stock_min"]:
                for producto in productos:
                    if producto["codigo"] == stock["codigo"]:
                        archivo.write(f"{producto['codigo']};{producto['nombre']};{stock['stock_min']};{stock['stock_real']}\n")


# 9) Un profesor almacenó los datos de los alumnos de su materia en un archivo alumnos.txt. En cada línea guardó el número de legajo del alumno y sus tres notas finales 
# (oral, escrito y trabajos prácticos). El archivo está ordenado por número de legajo. 
# En otro archivo, ordenado alfabéticamente por apellido, guarda por línea, número de legajo, apellido y nombre de cada uno.
# En ambos archivos los datos están separados por punto y coma  ( ; )  .
# Desea escribir un programa para generar un archivo Promoción.txt con los apellidos y nombres de los alumnos que promocionan la materia, 
# esto es, alumnos que el promedio de las tres notas supere los 7 puntos. 
# El archivo debe quedar ordenado alfabéticamente
# ej notas.txt
# 1;70;80;90
# 2;60;70;80
# 3;70;70;70
# 4;80;90;100

# ej alumnos.txt
# 1;Perez;Pedro
# 2;Gonzalez;Maria
# 3;Rodriguez;Carlos
# 4;Gomez;Ana

def buscar_legajos_promocionados()->list[int]:
    """Devuelve una lista con los legajos de los alumnos que promocionan la materia."""
    alumnos = []
    try:
        with open("notas.txt", "r") as archivo:
            for linea in archivo:
                #cada linea tiene: legajo;nota_oral;nota_escrito;nota_practicos
                datos = linea.strip().split(";")
                legajo = int(datos[0])
                oral = float(datos[1])
                escrito = float(datos[2])
                practicos = float(datos[3])
                if (oral + escrito + practicos) / 3 > 7:
                    alumnos.append(legajo)
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except ValueError:
        print("Error al leer un numero del archivo.")
    return alumnos

def cargar_alumnos()->list[dict]:
    """Devuelve los alumnos del archivo alumnos.txt en una lista de diccionarios.
    Los alumnos en el archivo están ordenados alfabéticamente por apellido."""
    alumnos = []
    try:
        with open("alumnos.txt", "r") as archivo:
            for linea in archivo:
                #cada linea tiene: legajo;apellido;nombre
                datos = linea.strip().split(";")
                legajo = int(datos[0])
                apellido = datos[1]
                nombre = datos[2]
                alumnos.append({"legajo":legajo, "apellido":apellido, "nombre":nombre})
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except ValueError:
        print("Error al leer un numero del archivo.")
    return alumnos


def ejercicio9():
    legajos_promocionados = buscar_legajos_promocionados()
    alumnos = cargar_alumnos()
    promocionados = []
    # itero sobre la lista de alumnos porque ya está ordenada alfabéticamente
    for alumno in alumnos:
        if alumno["legajo"] in legajos_promocionados:
            promocionados.append(alumno)
    with open("Promocion.txt", "w") as archivo:
        for alumno in promocionados:
            archivo.write(f"{alumno['legajo']};{alumno['apellido']};{alumno['nombre']}\n")