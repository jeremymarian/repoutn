"""
Práctico 11: Aplicación de la Recursividad
Programación I
"""


# ============================================
# EJERCICIO 1: Factorial recursivo
# ============================================

def factorial(n):
    """
    Calcula el factorial de un número de forma recursiva.
    
    Caso base: factorial(0) = 1, factorial(1) = 1
    Caso recursivo: factorial(n) = n * factorial(n-1)
    
    Args:
        n (int): Número entero positivo
    
    Returns:
        int: Factorial de n
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def mostrar_factoriales():
    """
    Calcula y muestra el factorial de todos los números entre 1 y n.
    """
    n = int(input("Ingrese un número entero positivo: "))
    
    if n < 1:
        print("Error: Debe ingresar un número mayor a 0.")
        return
    
    print(f"\nFactoriales desde 1 hasta {n}:\n")
    for i in range(1, n + 1):
        resultado = factorial(i)
        print(f"Factorial de {i} = {resultado}")


# ============================================
# EJERCICIO 2: Fibonacci recursivo
# ============================================

def fibonacci(posicion):
    """
    Calcula el valor de Fibonacci en una posición dada (recursivo).
    
    Caso base: fibonacci(0) = 0, fibonacci(1) = 1
    Caso recursivo: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    
    Args:
        posicion (int): Posición en la serie de Fibonacci
    
    Returns:
        int: Valor de Fibonacci en esa posición
    """
    if posicion == 0:
        return 0
    if posicion == 1:
        return 1
    return fibonacci(posicion - 1) + fibonacci(posicion - 2)


def mostrar_serie_fibonacci():
    """
    Muestra la serie completa de Fibonacci hasta la posición indicada.
    """
    n = int(input("Ingrese la posición hasta la cual mostrar Fibonacci: "))
    
    if n < 0:
        print("Error: Debe ingresar un número mayor o igual a 0.")
        return
    
    print(f"\nSerie de Fibonacci hasta la posición {n}:\n")
    for i in range(n + 1):
        valor = fibonacci(i)
        print(f"F({i}) = {valor}")


# ============================================
# EJERCICIO 3: Potencia recursiva
# ============================================

def potencia(base, exponente):
    """
    Calcula la potencia de un número de forma recursiva.
    Utiliza la fórmula: n^m = n * n^(m-1)
    
    Caso base: potencia(n, 0) = 1
    Caso recursivo: potencia(n, m) = n * potencia(n, m-1)
    
    Args:
        base (float): Número base
        exponente (int): Exponente (debe ser entero no negativo)
    
    Returns:
        float: base elevado a exponente
    """
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


def probar_potencia():
    """
    Prueba la función de potencia con valores ingresados por el usuario.
    """
    base = float(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente (entero no negativo): "))
    
    if exponente < 0:
        print("Error: El exponente debe ser no negativo.")
        return
    
    resultado = potencia(base, exponente)
    print(f"\n{base} elevado a {exponente} = {resultado}")


# ============================================
# EJERCICIO 4: Decimal a binario recursivo
# ============================================

def decimal_a_binario(n):
    """
    Convierte un número decimal a binario de forma recursiva.
    
    Algoritmo:
    1. Dividir el número por 2
    2. Guardar el resto (0 o 1)
    3. Repetir con el cociente hasta llegar a 0
    4. Los restos leídos de abajo hacia arriba forman el binario
    
    Caso base: Si n == 0, retorna "0", si n == 1, retorna "1"
    Caso recursivo: decimal_a_binario(n//2) + str(n%2)
    
    Args:
        n (int): Número entero positivo en base decimal
    
    Returns:
        str: Representación binaria del número
    """
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    
    # Llamada recursiva: dividir por 2 y concatenar el resto
    return decimal_a_binario(n // 2) + str(n % 2)


def probar_decimal_a_binario():
    """
    Prueba la conversión de decimal a binario.
    """
    n = int(input("Ingrese un número entero positivo: "))
    
    if n < 0:
        print("Error: Debe ingresar un número positivo.")
        return
    
    binario = decimal_a_binario(n)
    print(f"\n{n} en binario es: {binario}")


# ============================================
# EJERCICIO 5: Palíndromo recursivo
# ============================================

def es_palindromo(palabra):
    """
    Verifica si una palabra es palíndromo de forma recursiva.
    No usa [::-1] ni reversed().
    
    Caso base: 
    - Si len(palabra) <= 1: True (una letra o vacío es palíndromo)
    Caso recursivo:
    - Comparar primer y último carácter
    - Si son iguales, verificar el resto de la palabra recursivamente
    
    Args:
        palabra (str): Cadena de texto sin espacios ni tildes
    
    Returns:
        bool: True si es palíndromo, False si no lo es
    """
    # Caso base: palabra vacía o de un solo carácter
    if len(palabra) <= 1:
        return True
    
    # Comparar primer y último carácter
    if palabra[0].lower() != palabra[-1].lower():
        return False
    
    # Llamada recursiva con el resto de la palabra (sin primer y último carácter)
    return es_palindromo(palabra[1:-1])


def probar_palindromo():
    """
    Prueba si una palabra es palíndromo.
    """
    palabra = input("Ingrese una palabra (sin espacios ni tildes): ")
    
    if es_palindromo(palabra):
        print(f"\n✓ '{palabra}' es un palíndromo.")
    else:
        print(f"\n✗ '{palabra}' NO es un palíndromo.")


# ============================================
# EJERCICIO 6: Suma de dígitos recursiva
# ============================================

def suma_digitos(n):
    """
    Calcula la suma de todos los dígitos de un número de forma recursiva.
    No convierte el número a string.
    
    Caso base: Si n < 10, retorna n (un solo dígito)
    Caso recursivo: último_dígito + suma_digitos(n//10)
    
    Args:
        n (int): Número entero positivo
    
    Returns:
        int: Suma de todos los dígitos
    """
    if n < 10:
        return n
    
    # Obtener último dígito con n % 10
    # Obtener el resto del número con n // 10
    return (n % 10) + suma_digitos(n // 10)


def probar_suma_digitos():
    """
    Prueba la suma de dígitos.
    """
    n = int(input("Ingrese un número entero positivo: "))
    
    if n < 0:
        print("Error: Debe ingresar un número positivo.")
        return
    
    resultado = suma_digitos(n)
    print(f"\nLa suma de los dígitos de {n} es: {resultado}")


# ============================================
# EJERCICIO 7: Contar bloques de pirámide
# ============================================

def contar_bloques(n):
    """
    Calcula el total de bloques necesarios para construir una pirámide.
    En el nivel más bajo hay n bloques, en el siguiente n-1, y así hasta 1.
    
    Caso base: Si n == 1, retorna 1
    Caso recursivo: n + contar_bloques(n-1)
    
    Args:
        n (int): Número de bloques en el nivel más bajo
    
    Returns:
        int: Total de bloques en la pirámide
    """
    if n == 1:
        return 1
    
    return n + contar_bloques(n - 1)


def probar_contar_bloques():
    """
    Prueba el cálculo de bloques de la pirámide.
    """
    n = int(input("Ingrese el número de bloques en el nivel más bajo: "))
    
    if n < 1:
        print("Error: Debe ingresar un número mayor a 0.")
        return
    
    total = contar_bloques(n)
    print(f"\nPara una pirámide con {n} bloques en el nivel más bajo,")
    print(f"se necesitan {total} bloques en total.")


# ============================================
# EJERCICIO 8: Contar dígito en número
# ============================================

def contar_digito(numero, digito):
    """
    Cuenta cuántas veces aparece un dígito en un número de forma recursiva.
    
    Caso base: 
    - Si numero < 10: comparar con el dígito y retornar 1 o 0
    Caso recursivo:
    - Si último dígito == digito: 1 + contar_digito(numero//10, digito)
    - Si no: contar_digito(numero//10, digito)
    
    Args:
        numero (int): Número entero positivo
        digito (int): Dígito a buscar (entre 0 y 9)
    
    Returns:
        int: Cantidad de veces que aparece el dígito
    """
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    
    # Obtener último dígito
    ultimo_digito = numero % 10
    
    # Si el último dígito coincide, sumar 1, si no, sumar 0
    if ultimo_digito == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


def probar_contar_digito():
    """
    Prueba el conteo de dígitos en un número.
    """
    numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese el dígito a buscar (0-9): "))
    
    if numero < 0:
        print("Error: El número debe ser positivo.")
        return
    
    if digito < 0 or digito > 9:
        print("Error: El dígito debe estar entre 0 y 9.")
        return
    
    cantidad = contar_digito(numero, digito)
    print(f"\nEl dígito {digito} aparece {cantidad} vez/veces en {numero}.")


# ============================================
# MENÚ PRINCIPAL
# ============================================

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n" + "="*60)
    print("   PRÁCTICO 11: APLICACIÓN DE LA RECURSIVIDAD")
    print("="*60)
    print("1. Factorial recursivo")
    print("2. Serie de Fibonacci recursiva")
    print("3. Potencia recursiva")
    print("4. Decimal a binario recursivo")
    print("5. Verificar palíndromo recursivo")
    print("6. Suma de dígitos recursiva")
    print("7. Contar bloques de pirámide")
    print("8. Contar dígito en número")
    print("9. Salir")
    print("="*60)


def main():
    """Función principal con menú interactivo."""
    continuar = True
    
    while continuar:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-9): ")
        
        if opcion == "1":
            mostrar_factoriales()
        
        elif opcion == "2":
            mostrar_serie_fibonacci()
        
        elif opcion == "3":
            probar_potencia()
        
        elif opcion == "4":
            probar_decimal_a_binario()
        
        elif opcion == "5":
            probar_palindromo()
        
        elif opcion == "6":
            probar_suma_digitos()
        
        elif opcion == "7":
            probar_contar_bloques()
        
        elif opcion == "8":
            probar_contar_digito()
        
        elif opcion == "9":
            print("\n¡Hasta luego!")
            continuar = False
        
        else:
            print("\nError: Opción inválida. Seleccione una opción del 1 al 9.")


if __name__ == "__main__":
    main()

