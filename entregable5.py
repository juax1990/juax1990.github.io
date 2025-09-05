# Mostrar un mensaje en pantalla
def mensaje(nombre):
    print (f"Hola {nombre}")
def programaPrincipal():
    nombre=input("Ingresa tu nombre: ")
    print(f"Hola {nombre}")
# Llamar a la función
programaPrincipal()

# Declarar variables y realizar operaciones matematicas simples
def operacionesBasicas():
    #declaración de variables
    entero=4                    #int
    decimal=3.5                 #float
    cadena="El Resultado de "   #string
    #Operaciones basicas
    suma=entero+decimal
    resta=entero-decimal
    multiplicacion=entero*decimal
    division=entero/decimal
    # Mostrar los resultados
    print(cadena, "la suma es= ", suma)
    print(cadena, "la resta es= ", resta)
    print(cadena, "la multiplicación es= ", multiplicacion)
    print(cadena, "la división es= ", division)
# Llamar a la función
operacionesBasicas()

# Concatenar cadenas de texto
def concatenarTextos():
    texto1=input("Ingresa la primer palabra o frase: ")
    texto2=input("Ingresa la segunda palabra o frase: ")

    resultado=texto1+" "+texto2
    # Mostrar el resultado
    print(f"La concatención es: {resultado}")
#Llamada a la función
concatenarTextos()

# Condicionales y bucles
# Numero par o impar
def parOimpar():
    numero=int(input("Ingresa un numero "))
    if numero%2==0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
# Lamada a la funcion
parOimpar()

# Imprimir cuadrados de una lista
def imprimirCuadrados():
    numeros=[1, 2, 3, 4, 5, 6,7]
    # iterar con for
    for n in numeros:
        print (f"El cuadrado de {n} es {n**2}")
# Llamada a la función
imprimirCuadrados()

#Pedir algo hasta una condición
def pedirHastaCondicion():
    numero=0
    #Repetir hasta que el numero sea mayor a 10
    while numero<=10:
        numero=int(input("Ingresa un numero mayor a 10 "))
    print(f"El numero {numero} es mayor a 10")
# Llamada a la función
pedirHastaCondicion()

# Listas y diccionarios
#Estudiantes
def listaEstudiantes():
    #lista de estudiantes
    estudiantes=["Jhon", "Wilder", "Adriana", "Johan"]
    # Bucle para recorrer a lista
    for nombre in estudiantes:
        print(f"Estudiante: {nombre}")
# Llamada a la función
listaEstudiantes()

#Contacto
def contacto():
    #Crear el diccionario
    contacto={
        "nombre": "Jhon Tumina",
        "correo": "j.tumina@hotmail.com"
    }

    #Mostrar claves y valores
    print("Información de contacto: ")
    for clave, valor in contacto.items():
        print(f"{clave}: {valor}")
#Llamada a la función
contacto()

#Agregar un elemento o editar una lista
def agregarEditar():
    lista=["arroz", "aceite", "huevos"]
    diccionario={"nombre": "desconocido", "telefono": "3454562354"}

    while True:
        print("-------------Menu--------")
        print("¿Que deseas hacer?")
        print("1. Agregar un elemento a una lista")
        print("2. Actualizar un valor en el diccionario")
        print("3. Mostrar lista y diccionario")
        print("4. Salir")

        opcion=input("Selecciona una opción:")

        if opcion=="1":
            elemento=input("Escribe el elemento que deseas agregar: ")
            lista.append(elemento)
            print("Lista actualizada", lista)

        elif opcion=="2":
            clave=input("Escribe la clave que deseas actualizar nombre / telefono ")
            if clave in diccionario:
                valor=input(f"Escribe el nuevo valor para clave '{clave}': ")
                diccionario[clave]=valor
                print("Diccionario actualizado: ", diccionario)
            else:
                print("Esa clave no existe en el diccionario")

        elif opcion=="3":
            print("Lista actual", lista)
            print("Diccionario actual", diccionario)

        elif opcion=="4":
            print("Saliendo del programa...")
            break
        
        else:
            print("Selecciona una opcion de la lista, intenta de nuevo")
#Llamada a la función
agregarEditar()

#Calculadora basica
def calculadora():
    while True:
        print("--------Calculadora Basica")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion=input("¿Que deseas hacer?")

        if opcion=="5":
            print("Saliendo de la calculadora...")
            break

        #Pedir datos al usuario
        try:
            num1=float(input("Ingresa el primer numero :"))
            num2=float(input("Ingresa el segundo numero :"))
        except ValueError:
            print("Ingresa un numero valido")
            continue
        if opcion=="1":
            print(f"El resultado de la suma de{num1}+{num2}es = {num1+num2}")
        elif opcion=="2":
            print(f"El resultado de la resta de {num1}-{num2}es = {num1-num2}")
        elif opcion=="3":
            print(f"El resultado de la multiplicación de {num1}*{num2}es = {num1*num2}")
        elif opcion=="4":
            if num2 !=0:
                print(f"El resultado de la división de {num1}/{num2} es = {num1/num2}")
            else:
                print("Error: No se puede dividir entre cero")
        else:
            print("Opción no valida, selecciona una de la lista")
#Llamada a la función
calculadora()

#Adivinanza
#Traer la libreria
import random

def adivinanza():
    #Generar el numero de manera aleatoria
    numSecreto=random.randint(1,10)
    intento=0
    adivinado=False

    print("Bienvenido al juego de la adivinanza")
    print("He pensado un numero entre1 y 10, ¡intenta adivinarlo!")

    #Bucle hasta que se adivine el numero
    while not adivinado:
        try:
            intento=int(input("Ingresa tu numero: "))
            if intento < numSecreto:
                print("El numero secreto es mayor.")
            elif intento > numSecreto:
                print("El numero secreto es menor.")
            else:
                print(f"¡Felicidades!, adivinaste el numero {numSecreto}")
                adivinado=True

        except ValueError:
            print("Debes ingresar un numero valido")
#Llamada a la función
adivinanza()