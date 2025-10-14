import math

def imprimir_hola_mundo():
    """Función que imprime 'Hola Mundo!' por pantalla"""
    print("Hola Mundo!")

def saludar_usuario(nombre):
    """Función que recibe un nombre y devuelve un saludo personalizado"""
    return f"Hola {nombre}!"

def informacion_personal(nombre, apellido, edad, residencia):
    """Función que recibe cuatro parámetros e imprime información personal"""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def calcular_area_circulo(radio):
    """Función que recibe el radio y devuelve el área del círculo"""
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    """Función que recibe el radio y devuelve el perímetro del círculo"""
    return 2 * math.pi * radio

def segundos_a_horas(segundos):
    """Función que recibe segundos y devuelve las horas correspondientes"""
    return segundos / 3600

def tabla_multiplicar(numero):
    """Función que recibe un número e imprime su tabla de multiplicar del 1 al 10"""
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def operaciones_basicas(a, b):
    """Función que recibe dos números y devuelve una tupla con suma, resta, multiplicación y división"""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "Error: División por cero"
    return (suma, resta, multiplicacion, division)

def calcular_imc(peso, altura):
    """Función que recibe peso y altura y devuelve el índice de masa corporal"""
    return peso / (altura ** 2)

def celsius_a_fahrenheit(celsius):
    """Función que recibe temperatura en Celsius y devuelve su equivalente en Fahrenheit"""
    return (celsius * 9/5) + 32

def calcular_promedio(a, b, c):
    """Función que recibe tres números y devuelve su promedio"""
    return (a + b + c) / 3

def validar_entero(mensaje):
    """Función auxiliar para validar entrada de números enteros"""
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def validar_float(mensaje):
    """Función auxiliar para validar entrada de números decimales"""
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debe ingresar un número válido.")

print("Bienvenido al Práctico 2: Funciones en Python")
print("Este programa implementa las 10 funciones solicitadas en el práctico.")

opcion = 0

while opcion != 11:
    print("\n" + "="*60)
    print("              PRÁCTICO 2: FUNCIONES EN PYTHON")
    print("="*60)
    print("1.  Imprimir Hola Mundo")
    print("2.  Saludar Usuario")
    print("3.  Información Personal")
    print("4.  Calcular Área y Perímetro de Círculo")
    print("5.  Convertir Segundos a Horas")
    print("6.  Tabla de Multiplicar")
    print("7.  Operaciones Básicas")
    print("8.  Calcular IMC")
    print("9.  Convertir Celsius a Fahrenheit")
    print("10. Calcular Promedio")
    print("11. Salir")
    print("="*60)
    
    entrada = input("\nSeleccione una opción (1-11): ")
    if entrada.isdigit():
        opcion = int(entrada)
    else:
        print("Error: Debe ingresar un número entero válido.")
        opcion = 0
    
    if opcion == 1:
        print("\n--- EJERCICIO 1: IMPRIMIR HOLA MUNDO ---")
        imprimir_hola_mundo()
    
    elif opcion == 2:
        print("\n--- EJERCICIO 2: SALUDAR USUARIO ---")
        nombre = input("Ingrese su nombre: ").strip()
        if nombre:
            saludo = saludar_usuario(nombre)
            print(saludo)
        else:
            print("Error: El nombre no puede estar vacío.")
    
    elif opcion == 3:
        print("\n--- EJERCICIO 3: INFORMACIÓN PERSONAL ---")
        nombre = input("Ingrese su nombre: ").strip()
        if nombre:
            apellido = input("Ingrese su apellido: ").strip()
            if apellido:
                edad = validar_entero("Ingrese su edad: ")
                residencia = input("Ingrese su lugar de residencia: ").strip()
                if residencia:
                    informacion_personal(nombre, apellido, edad, residencia)
                else:
                    print("Error: La residencia no puede estar vacía.")
            else:
                print("Error: El apellido no puede estar vacío.")
        else:
            print("Error: El nombre no puede estar vacío.")
    
    elif opcion == 4:
        print("\n--- EJERCICIO 4: ÁREA Y PERÍMETRO DE CÍRCULO ---")
        radio = validar_float("Ingrese el radio del círculo: ")
        if radio >= 0:
            area = calcular_area_circulo(radio)
            perimetro = calcular_perimetro_circulo(radio)
            print(f"\nRadio: {radio}")
            print(f"Área: {area:.2f}")
            print(f"Perímetro: {perimetro:.2f}")
        else:
            print("Error: El radio debe ser un número positivo.")
    
    elif opcion == 5:
        print("\n--- EJERCICIO 5: CONVERTIR SEGUNDOS A HORAS ---")
        segundos = validar_entero("Ingrese la cantidad de segundos: ")
        if segundos >= 0:
            horas = segundos_a_horas(segundos)
            print(f"\n{segundos} segundos = {horas:.2f} horas")
        else:
            print("Error: Los segundos deben ser un número positivo.")
    
    elif opcion == 6:
        print("\n--- EJERCICIO 6: TABLA DE MULTIPLICAR ---")
        numero = validar_entero("Ingrese un número para generar su tabla de multiplicar: ")
        tabla_multiplicar(numero)
    
    elif opcion == 7:
        print("\n--- EJERCICIO 7: OPERACIONES BÁSICAS ---")
        a = validar_float("Ingrese el primer número: ")
        b = validar_float("Ingrese el segundo número: ")
        
        resultados = operaciones_basicas(a, b)
        suma, resta, multiplicacion, division = resultados
        
        print(f"\nResultados con los números {a} y {b}:")
        print(f"Suma: {suma}")
        print(f"Resta: {resta}")
        print(f"Multiplicación: {multiplicacion}")
        print(f"División: {division}")
    
    elif opcion == 8:
        print("\n--- EJERCICIO 8: CALCULAR IMC ---")
        peso = validar_float("Ingrese su peso en kilogramos: ")
        altura = validar_float("Ingrese su altura en metros: ")
        
        if peso > 0 and altura > 0:
            imc = calcular_imc(peso, altura)
            print(f"\nPeso: {peso} kg")
            print(f"Altura: {altura} m")
            print(f"IMC: {imc:.2f}")
        else:
            print("Error: El peso y la altura deben ser números positivos.")
    
    elif opcion == 9:
        print("\n--- EJERCICIO 9: CONVERTIR CELSIUS A FAHRENHEIT ---")
        celsius = validar_float("Ingrese la temperatura en grados Celsius: ")
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"\n{celsius}°C = {fahrenheit:.2f}°F")
    
    elif opcion == 10:
        print("\n--- EJERCICIO 10: CALCULAR PROMEDIO ---")
        a = validar_float("Ingrese el primer número: ")
        b = validar_float("Ingrese el segundo número: ")
        c = validar_float("Ingrese el tercer número: ")
        
        promedio = calcular_promedio(a, b, c)
        print(f"\nNúmeros ingresados: {a}, {b}, {c}")
        print(f"Promedio: {promedio:.2f}")
    
    elif opcion == 11:
        print("\n¡Gracias por usar el programa del Práctico 2!")
        print("Programa finalizado.")
    else:
        print("Error: Opción inválida. Seleccione una opción del 1 al 11.")
    
    if opcion != 11:
        input("\nPresione Enter para continuar...")
