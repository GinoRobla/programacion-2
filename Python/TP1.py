# 1) Realizar un programa que pida los tres lados de un triángulo e indique el tipo de triángulo que es según sus lados: 
# Equilátero (tres lados iguales), Isósceles (dos lados iguales) o Escaleno (tres lados distintos).
def ej1():
    lado1 = int(input("Ingrese el primer lado del triángulo: "))
    lado2 = int(input("Ingrese el segundo lado del triángulo: "))
    lado3 = int(input("Ingrese el tercer lado del triángulo: "))
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")

# 2) Implemente un programa que a partir del ancho, alto y largo de una habitación rectangular calcule cuántos litros de pintura se necesitan para pintarla. 
# Suponiendo que 1 litro de pintura sirve para 10m cuadrados y que la habitación tiene sólo una puerta de 0,80 de ancho por 2 mts de alto. 
def ej2():
    ancho = float(input("Ingrese el ancho de la habitación: "))
    alto = float(input("Ingrese el alto de la habitación: "))
    largo = float(input("Ingrese el largo de la habitación: "))
    area = 2 * (ancho * alto) + 2 * (alto * largo)
    puerta = 2*0.8
    area -= puerta
    litros = area / 10
    #si los litros no son enteros, redondeamos hacia arriba
    if litros % 1 != 0:
        litros = int(litros) + 1
    print(f"Se necesitan {litros} litros de pintura.")

# 3) Extienda el programa anterior para permitir múltiple cantidad de “manos” de pintura.
def ej3():
    ancho = float(input("Ingrese el ancho de la habitación: "))
    alto = float(input("Ingrese el alto de la habitación: "))
    largo = float(input("Ingrese el largo de la habitación: "))
    area = 2 * (ancho * alto) + 2 * (alto * largo)
    puerta = 2*0.8
    area -= puerta
    litros = area / 10
    manos = int(input("Ingrese la cantidad de manos de pintura: "))
    litros *= manos
    #si los litros no son enteros, redondeamos hacia arriba
    if litros % 1 != 0:
        litros = int(litros) + 1
    print(f"Se necesitan {litros} litros de pintura.")

# 4) Pedir 3 números enteros e implementar un algoritmo para determinar cuál es el mayor de los 3 y mostrar un mensaje por pantalla.
def ej4():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    if num1 > num2 and num1 > num3:
        print(f"El mayor número es {num1}.")
    elif num2 > num1 and num2 > num3:
        print(f"El mayor número es {num2}.")
    else:
        print(f"El mayor número es {num3}.")

# 5) Dada una cadena de texto ingresada por consola, decir cuántos “espacios” contiene.
def ej5():
    cadena = input("Ingrese una cadena de texto: ")
    contador = 0
    for letra in cadena:
        if letra == " ":
            contador += 1
    print(f"La cadena tiene {contador} espacios.")

# 6) Realizar un programa que solicite al usuario un número entero positivo, y luego en pantalla muestre la secuencia de números desde el 1 hasta el número ingresado.
# Ej: usuario ingresa 10, en pantalla se mostrará 1 2 3 4 5 6 7 8 9 10
def ej6():
    num = int(input("Ingrese un número entero positivo: "))
    for i in range(1, num+1):
        print(i, end=" ")
    print()

# 7) Realizar un programa que solicite al usuario un número entero positivo, y luego en pantalla muestre solamente los números pares desde el 1 hasta el número ingresado.
# Ej: usuario ingresa 10, en pantalla se mostrará 2 4 6 8 10
def ej7():
    num = int(input("Ingrese un número entero positivo: "))
    for i in range(2, num+1, 2):
        print(i, end=" ")
    print()

def ej7_otra_forma():
    num = int(input("Ingrese un número entero positivo: "))
    for i in range(1, num+1):
        if i % 2 == 0:
            print(i, end=" ")
    print()

# 8) Desarrollar un programa que permita al usuario indicar cuantos valores quiere ingresar, luego que permita la carga de los valores por teclado y 
# nos muestre posteriormente la suma de los valores ingresados y su promedio.
def ej8():
    cantidad = int(input("Ingrese la cantidad de valores a ingresar: "))
    suma = 0
    for i in range(cantidad):
        valor = int(input(f"Ingrese el valor {i+1}: "))
        suma += valor
    promedio = suma / cantidad
    print(f"La suma de los valores es {suma} y el promedio es {promedio}.")

# 9) Se desea realizar una aplicación que solicite al usuario tres números enteros positivos (A, B, y X), y que muestre por pantalla todos los múltiplos de X 
# que estén entre A y B inclusive. 
def ej9():
    a = int(input("Ingrese el número A: "))
    b = int(input("Ingrese el número B: "))
    x = int(input("Ingrese el número X: "))
    for i in range(a, b+1):
        if i % x == 0:
            print(i, end=" ")
    print()

# 10) Escriba un programa que permita al usuario ingresar las medidas de 2 lados de un rectángulo, y que luego mediante la impresión repetida de un caracter (ej: *) 
# lo dibuje en la pantalla. Para este ejercicio tomaremos un máximo de 40 para el lado más largo, con el fin de evitar problemas de visualización en la consola. 
# Verificar en los datos de entrada que se cumpla este requisito.
def ej10():
    lado1 = int(input("Ingrese el primer lado del rectángulo: "))
    lado2 = int(input("Ingrese el segundo lado del rectángulo: "))
    if lado1 > 40 or lado2 > 40:
        print("Los lados no pueden ser mayores a 40.")
    else:
        for i in range(lado1):
            for j in range(lado2):
                print("*", end=" ")
            print()

# 11) Escriba un programa que permita el ingreso de números enteros positivos para calcular su promedio, el ingreso finaliza cuando el usuario ingresa un número negativo. 
# Luego mostrar el promedio y la cantidad de valores que se ingresaron. Ej: “El promedio es ….. con un total de …. ingresos.”
def ej11():
    suma = 0
    cantidad = 0
    num = int(input("Ingrese un número entero positivo (o uno negativo para salir): "))
    while num >= 0:
        suma += num
        cantidad += 1
        num = int(input("Ingrese un número entero positivo (o uno negativo para salir): "))
    promedio = suma / cantidad
    print(f"El promedio es {promedio} con un total de {cantidad} ingresos.")

# 12) Escriba un programa que permita el ingreso de números enteros positivos, finalizando el ingreso con 0, y luego indique si la secuencia estaba ordenada de menor a mayor.
def ej12():
    num = int(input("Ingrese un número entero positivo (o 0 para salir): "))
    anterior = num
    ordenada = True
    while num != 0:
        if num < anterior:
            ordenada = False
        anterior = num
        num = int(input("Ingrese un número entero positivo (o 0 para salir): "))
    if ordenada:
        print("La secuencia estaba ordenada de menor a mayor.")
    else:
        print("La secuencia no estaba ordenada de menor a mayor.")

# 13) Se desea realizar una aplicación que solicite al usuario un caracter y un número natural N, y que la aplicación muestre en pantalla dicho carácter 
# repetido N veces consecutivas.
# Ej: 	Ingrese un caracter: +
# 	Ingrese la cantidad de repeticiones: 15
# 	+++++++++++++++
def ej13():
    caracter = input("Ingrese un caracter: ")
    n = int(input("Ingrese la cantidad de repeticiones: "))
    for i in range(n):
        print(caracter, end="")
    print()

# 14) Escriba un programa que dado un texto ingresado por el usuario cuente la cantidad total de vocales que aparecen y lo muestre por pantalla.
def ej14():
    texto = input("Ingrese un texto: ")
    vocales = "aeiouáéíóú"
    contador = 0
    for letra in texto:
        if letra.lower() in vocales:
            contador += 1
    print(f"El texto tiene {contador} vocales.")

# 15) Escriba un programa que, dada una oración ingresada muestre por pantalla:
# El número total de caracteres en la oración
# La cantidad total de letras (consonantes y vocales, sin signos de puntuación)
# La cantidad de palabras separadas por uno o más espacios
# En este ejercicio, para simplificar, asumiremos que los posibles caracteres de entrada son letras, espacios, dígitos, signos de puntuación, signos de interrogación y de exclamación.
# Investigar si hay funciones de strings que nos faciliten la resolución [len(), .isalpha(), .split() , etc.]
def ej15():
    oracion = input("Ingrese una oración: ")
    caracteres = len(oracion)
    cant_letras = 0
    #cuento cuantos caracteres son letras
    for letra in oracion:
        if letra.isalpha():
            cant_letras += 1
    #divido la oración en palabras 'cortándola' por los espacios y cuento cuantas palabras hay
    cant_palabras = len(oracion.split())
    print(f"El número total de caracteres en la oración es {caracteres}.")
    print(f"La cantidad total de letras es {cant_letras}.")
    print(f"La cantidad de palabras es {cant_palabras}.")

# 16) Escriba un programa que para un texto ingresado nos muestre cual es la palabra más larga dentro de ese texto y cuántas letras tiene.
def ej16():
    texto = input("Ingrese un texto: ")
    palabras = texto.split()
    palabra_larga = ""
    cant_letras_mayor = 0
    for palabra in palabras:
        if len(palabra) > cant_letras_mayor:
            cant_letras_mayor = len(palabra)
            palabra_larga = palabra
    print(f"La palabra más larga es {palabra_larga} y tiene {cant_letras_mayor} letras.")