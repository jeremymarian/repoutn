"""
TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA
Práctico 4: Estructuras repetitivas

Este programa contiene la resolución de todos los ejercicios del práctico 4
utilizando estructuras de control repetitivas (FOR, WHILE).

Autor: Mariano Mocho

"""

import random
import math

def mostrar_menu():
    """Muestra el menú principal con todos los ejercicios disponibles."""
    print("\n" + "="*60)
    print("PRÁCTICO 4: ESTRUCTURAS REPETITIVAS")
    print("="*60)
    print("1.  Imprimir números del 0 al 100")
    print("2.  Contar dígitos de un número")
    print("3.  Sumar números entre dos valores")
    print("4.  Sumar números hasta ingresar 0")
    print("5.  Juego de adivinar número aleatorio")
    print("6.  Números pares del 100 al 0 (decreciente)")
    print("7.  Sumar números del 0 a un número dado")
    print("8.  Analizar 100 números (pares, impares, positivos, negativos)")
    print("9.  Calcular media de 100 números")
    print("10. Invertir dígitos de un número")
    print("0.  Salir")
    print("="*60)

def ejercicio_1():
    """
    Ejercicio 1: Imprimir números del 0 al 100
    Crea un programa que imprima en pantalla todos los números enteros 
    desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente.
    """
    print("\n--- EJERCICIO 1: Números del 0 al 100 ---")
    print("Imprimiendo números del 0 al 100:")
    
    for i in range(0, 101):
        print(i)
    
    print(f"\nTotal de números impresos: {101}")

def ejercicio_2():
    """
    Ejercicio 2: Contar dígitos de un número
    Desarrolla un programa que solicite al usuario un número entero 
    y determine la cantidad de dígitos que contiene.
    """
    print("\n--- EJERCICIO 2: Contar dígitos ---")
    
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            break
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
    
    # Método 1: Convertir a string y contar caracteres
    digitos_str = len(str(abs(numero)))
    
    # Método 2: Usar logaritmo (más eficiente para números muy grandes)
    if numero == 0:
        digitos_log = 1
    else:
        digitos_log = int(math.log10(abs(numero))) + 1
    
    print(f"El número {numero} tiene {digitos_str} dígito(s)")
    print(f"Verificación con logaritmo: {digitos_log} dígito(s)")

def ejercicio_3():
    """
    Ejercicio 3: Sumar números entre dos valores
    Escribe un programa que sume todos los números enteros comprendidos 
    entre dos valores dados por el usuario, excluyendo esos dos valores.
    """
    print("\n--- EJERCICIO 3: Sumar números entre dos valores ---")
    
    while True:
        try:
            valor1 = int(input("Ingrese el primer valor: "))
            valor2 = int(input("Ingrese el segundo valor: "))
            break
        except ValueError:
            print("Error: Debe ingresar números enteros válidos.")
    
    # Asegurar que valor1 sea menor que valor2
    if valor1 > valor2:
        valor1, valor2 = valor2, valor1
    
    suma = 0
    numeros_sumados = []
    
    # Sumar números entre valor1 y valor2 (excluyendo los extremos)
    for i in range(valor1 + 1, valor2):
        suma += i
        numeros_sumados.append(i)
    
    print(f"\nNúmeros sumados: {numeros_sumados}")
    print(f"Suma total: {suma}")
    print(f"Cantidad de números sumados: {len(numeros_sumados)}")

def ejercicio_4():
    """
    Ejercicio 4: Sumar números hasta ingresar 0
    Elabora un programa que permita al usuario ingresar números enteros 
    y los sume en secuencia. El programa debe detenerse y mostrar el 
    total acumulado cuando el usuario ingrese un 0.
    """
    print("\n--- EJERCICIO 4: Sumar números hasta ingresar 0 ---")
    print("Ingrese números enteros (0 para terminar):")
    
    suma_total = 0
    contador = 0
    numeros_ingresados = []
    
    while True:
        try:
            numero = int(input(f"Número {contador + 1}: "))
            
            if numero == 0:
                break
            
            suma_total += numero
            numeros_ingresados.append(numero)
            contador += 1
            
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
    
    print(f"\nNúmeros ingresados: {numeros_ingresados}")
    print(f"Total de números ingresados: {contador}")
    print(f"Suma total: {suma_total}")

def ejercicio_5():
    """
    Ejercicio 5: Juego de adivinar número aleatorio
    Crea un juego en el que el usuario deba adivinar un número aleatorio 
    entre 0 y 9. Al final, el programa debe mostrar cuántos intentos 
    fueron necesarios para acertar el número.
    """
    print("\n--- EJERCICIO 5: Juego de adivinar número ---")
    print("¡Bienvenido al juego de adivinar el número!")
    print("Debes adivinar un número entre 0 y 9")
    
    # Generar número aleatorio
    numero_secreto = random.randint(0, 9)
    intentos = 0
    
    print(f"Número secreto generado: {numero_secreto} (para verificación)")
    
    while True:
        try:
            intento = int(input(f"Intento {intentos + 1}: Ingresa tu número (0-9): "))
            
            if intento < 0 or intento > 9:
                print("Error: El número debe estar entre 0 y 9")
                continue
            
            intentos += 1
            
            if intento == numero_secreto:
                print(f"¡Felicitaciones! ¡Adivinaste el número {numero_secreto}!")
                print(f"Lo lograste en {intentos} intento(s)")
                break
            elif intento < numero_secreto:
                print("El número secreto es mayor. ¡Intenta de nuevo!")
            else:
                print("El número secreto es menor. ¡Intenta de nuevo!")
                
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def ejercicio_6():
    """
    Ejercicio 6: Números pares del 100 al 0 (decreciente)
    Desarrolla un programa que imprima en pantalla todos los números pares 
    comprendidos entre 0 y 100, en orden decreciente.
    """
    print("\n--- EJERCICIO 6: Números pares del 100 al 0 ---")
    print("Números pares en orden decreciente:")
    
    numeros_pares = []
    
    # Generar números pares del 100 al 0
    for i in range(100, -1, -2):
        numeros_pares.append(i)
        print(i)
    
    print(f"\nTotal de números pares: {len(numeros_pares)}")

def ejercicio_7():
    """
    Ejercicio 7: Sumar números del 0 a un número dado
    Crea un programa que calcule la suma de todos los números 
    comprendidos entre 0 y un número entero positivo indicado por el usuario.
    """
    print("\n--- EJERCICIO 7: Sumar números del 0 a un número dado ---")
    
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            if numero < 0:
                print("Error: El número debe ser positivo.")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
    
    suma = 0
    numeros_sumados = []
    
    # Sumar números del 0 al número dado (incluyendo ambos extremos)
    for i in range(0, numero + 1):
        suma += i
        numeros_sumados.append(i)
    
    print(f"\nNúmeros sumados: {numeros_sumados}")
    print(f"Suma total: {suma}")
    print(f"Verificación con fórmula: n*(n+1)/2 = {numero}*{numero+1}/2 = {numero * (numero + 1) // 2}")

def ejercicio_8():
    """
    Ejercicio 8: Analizar 100 números
    Escribe un programa que permita al usuario ingresar 100 números enteros. 
    Luego, el programa debe indicar cuántos de estos números son pares, 
    impares, negativos y positivos.
    """
    print("\n--- EJERCICIO 8: Analizar 100 números ---")
    
    # Para facilitar las pruebas, permitir cambiar la cantidad
    cantidad = int(input("¿Cuántos números desea ingresar? (100 para el ejercicio completo): "))
    
    if cantidad <= 0:
        print("Error: La cantidad debe ser positiva.")
        return
    
    print(f"Ingrese {cantidad} números enteros:")
    
    numeros = []
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
    ceros = 0
    
    for i in range(cantidad):
        while True:
            try:
                numero = int(input(f"Número {i + 1}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
        
        # Analizar el número
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            ceros += 1
    
    print(f"\n--- ANÁLISIS DE LOS {cantidad} NÚMEROS ---")
    print(f"Números ingresados: {numeros}")
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")
    print(f"Positivos: {positivos}")
    print(f"Negativos: {negativos}")
    print(f"Ceros: {ceros}")

def ejercicio_9():
    """
    Ejercicio 9: Calcular media de 100 números
    Elabora un programa que permita al usuario ingresar 100 números enteros 
    y luego calcule la media de esos valores.
    """
    print("\n--- EJERCICIO 9: Calcular media de 100 números ---")
    
    # Para facilitar las pruebas, permitir cambiar la cantidad
    cantidad = int(input("¿Cuántos números desea ingresar? (100 para el ejercicio completo): "))
    
    if cantidad <= 0:
        print("Error: La cantidad debe ser positiva.")
        return
    
    print(f"Ingrese {cantidad} números enteros:")
    
    numeros = []
    suma_total = 0
    
    for i in range(cantidad):
        while True:
            try:
                numero = int(input(f"Número {i + 1}: "))
                numeros.append(numero)
                suma_total += numero
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
    
    media = suma_total / cantidad
    
    print(f"\n--- RESULTADOS ---")
    print(f"Números ingresados: {numeros}")
    print(f"Suma total: {suma_total}")
    print(f"Cantidad de números: {cantidad}")
    print(f"Media: {media:.2f}")

def ejercicio_10():
    """
    Ejercicio 10: Invertir dígitos de un número
    Escribe un programa que invierta el orden de los dígitos de un número 
    ingresado por el usuario. Ejemplo: si el usuario ingresa 547, 
    el programa debe mostrar 745.
    """
    print("\n--- EJERCICIO 10: Invertir dígitos de un número ---")
    
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            break
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
    
    # Método 1: Usando string
    numero_str = str(abs(numero))
    numero_invertido_str = numero_str[::-1]
    numero_invertido = int(numero_invertido_str)
    
    # Aplicar signo si el número original era negativo
    if numero < 0:
        numero_invertido = -numero_invertido
    
    # Método 2: Usando operaciones matemáticas
    numero_temp = abs(numero)
    numero_invertido_math = 0
    
    while numero_temp > 0:
        digito = numero_temp % 10
        numero_invertido_math = numero_invertido_math * 10 + digito
        numero_temp = numero_temp // 10
    
    # Aplicar signo si el número original era negativo
    if numero < 0:
        numero_invertido_math = -numero_invertido_math
    
    print(f"\nNúmero original: {numero}")
    print(f"Número invertido (método string): {numero_invertido}")
    print(f"Número invertido (método matemático): {numero_invertido_math}")

def main():
    """Función principal que maneja el menú y la navegación."""
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("\nSeleccione un ejercicio (0 para salir): "))
            
            if opcion == 0:
                print("\n¡Gracias por usar el programa! ¡Hasta luego!")
                break
            elif opcion == 1:
                ejercicio_1()
            elif opcion == 2:
                ejercicio_2()
            elif opcion == 3:
                ejercicio_3()
            elif opcion == 4:
                ejercicio_4()
            elif opcion == 5:
                ejercicio_5()
            elif opcion == 6:
                ejercicio_6()
            elif opcion == 7:
                ejercicio_7()
            elif opcion == 8:
                ejercicio_8()
            elif opcion == 9:
                ejercicio_9()
            elif opcion == 10:
                ejercicio_10()
            else:
                print("Error: Opción no válida. Por favor, seleccione un número del 0 al 10.")
            
            # Pausa antes de mostrar el menú nuevamente
            input("\nPresione Enter para continuar...")
            
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()
