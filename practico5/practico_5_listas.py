"""
TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA
Práctico 5: Listas

Este programa contiene la resolución de todos los ejercicios del práctico 5
utilizando listas, indexación, slicing, métodos integrados y listas anidadas.

Autor: Mariano Mocho

"""

import random

def mostrar_menu():
    """Muestra el menú principal con todos los ejercicios disponibles."""
    print("\n" + "="*60)
    print("PRÁCTICO 5: LISTAS")
    print("="*60)
    print("1.  Notas de 10 estudiantes")
    print("2.  Lista de 5 productos")
    print("3.  Números aleatorios pares e impares")
    print("4.  Eliminar elementos repetidos")
    print("5.  Lista de estudiantes (agregar/eliminar)")
    print("6.  Rotar elementos de una lista")
    print("7.  Matriz de temperaturas semanales")
    print("8.  Matriz de notas de estudiantes")
    print("9.  Juego Ta-Te-Ti")
    print("10. Ventas de productos en una tienda")
    print("0.  Salir")
    print("="*60)

def mostrar_lista(lista, titulo="Lista"):
    """Función auxiliar para mostrar listas usando estructuras repetitivas."""
    print(f"\n{titulo}:")
    for i, elemento in enumerate(lista):
        print(f"  {i+1}. {elemento}")

def ejercicio_1():
    """
    Ejercicio 1: Notas de 10 estudiantes
    Crear una lista con las notas de 10 estudiantes.
    • Mostrar la lista completa.
    • Calcular y mostrar el promedio.
    • Indicar la nota más alta y la más baja.
    """
    print("\n--- EJERCICIO 1: Notas de 10 estudiantes ---")
    
    # Crear lista con notas de 10 estudiantes (simuladas)
    notas = [85, 92, 78, 96, 88, 91, 83, 89, 94, 87]
    
    print("Notas de los 10 estudiantes:")
    mostrar_lista(notas, "Notas")
    
    # Calcular promedio
    promedio = sum(notas) / len(notas)
    print(f"\nPromedio: {promedio:.2f}")
    
    # Nota más alta y más baja
    nota_maxima = max(notas)
    nota_minima = min(notas)
    
    print(f"Nota más alta: {nota_maxima}")
    print(f"Nota más baja: {nota_minima}")
    
    # Mostrar estadísticas adicionales
    print(f"\nEstadísticas adicionales:")
    print(f"Total de estudiantes: {len(notas)}")
    print(f"Suma total: {sum(notas)}")

def ejercicio_2():
    """
    Ejercicio 2: Lista de 5 productos
    Pedir al usuario que cargue 5 productos en una lista.
    • Mostrar la lista ordenada alfabéticamente.
    • Preguntar al usuario qué producto desea eliminar y actualizar la lista.
    """
    print("\n--- EJERCICIO 2: Lista de 5 productos ---")
    
    productos = []
    print("Ingrese 5 productos:")
    
    for i in range(5):
        while True:
            producto = input(f"Producto {i+1}: ").strip()
            if producto:
                productos.append(producto)
                break
            else:
                print("Error: El producto no puede estar vacío.")
    
    # Mostrar lista original
    mostrar_lista(productos, "Lista original")
    
    # Mostrar lista ordenada alfabéticamente
    productos_ordenados = sorted(productos)
    mostrar_lista(productos_ordenados, "Lista ordenada alfabéticamente")
    
    # Eliminar producto
    print(f"\nProductos disponibles para eliminar:")
    for i, producto in enumerate(productos):
        print(f"  {i+1}. {producto}")
    
    while True:
        try:
            indice = int(input("Ingrese el número del producto a eliminar: ")) - 1
            if 0 <= indice < len(productos):
                producto_eliminado = productos.pop(indice)
                print(f"Producto '{producto_eliminado}' eliminado exitosamente.")
                break
            else:
                print("Error: Número fuera de rango.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")
    
    # Mostrar lista final
    mostrar_lista(productos, "Lista final actualizada")

def ejercicio_3():
    """
    Ejercicio 3: Números aleatorios pares e impares
    Generar una lista con 15 números enteros al azar entre 1 y 100.
    • Crear una lista con los pares y otra con los impares.
    • Mostrar cuántos números tiene cada lista.
    """
    print("\n--- EJERCICIO 3: Números aleatorios pares e impares ---")
    
    # Generar lista con 15 números aleatorios
    numeros = [random.randint(1, 100) for _ in range(15)]
    
    print("Números generados:")
    mostrar_lista(numeros, "Lista original")
    
    # Separar en pares e impares
    pares = []
    impares = []
    
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    # Mostrar resultados
    mostrar_lista(pares, "Números pares")
    mostrar_lista(impares, "Números impares")
    
    print(f"\nCantidad de números pares: {len(pares)}")
    print(f"Cantidad de números impares: {len(impares)}")
    print(f"Total de números: {len(numeros)}")

def ejercicio_4():
    """
    Ejercicio 4: Eliminar elementos repetidos
    Dada una lista con valores repetidos:
    • Crear una nueva lista sin elementos repetidos.
    • Mostrar el resultado.
    """
    print("\n--- EJERCICIO 4: Eliminar elementos repetidos ---")
    
    # Lista con valores repetidos
    lista_con_repetidos = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 8, 2, 9, 1, 5]
    
    print("Lista original con repetidos:")
    mostrar_lista(lista_con_repetidos, "Lista original")
    
    # Método 1: Usando set (más eficiente)
    lista_sin_repetidos_set = list(set(lista_con_repetidos))
    
    # Método 2: Usando bucle (mantiene orden original)
    lista_sin_repetidos_orden = []
    for elemento in lista_con_repetidos:
        if elemento not in lista_sin_repetidos_orden:
            lista_sin_repetidos_orden.append(elemento)
    
    print("\nLista sin repetidos (usando set):")
    mostrar_lista(lista_sin_repetidos_set, "Sin repetidos (set)")
    
    print("\nLista sin repetidos (manteniendo orden):")
    mostrar_lista(lista_sin_repetidos_orden, "Sin repetidos (orden original)")
    
    print(f"\nElementos originales: {len(lista_con_repetidos)}")
    print(f"Elementos únicos: {len(lista_sin_repetidos_orden)}")
    print(f"Elementos repetidos eliminados: {len(lista_con_repetidos) - len(lista_sin_repetidos_orden)}")

def ejercicio_5():
    """
    Ejercicio 5: Lista de estudiantes (agregar/eliminar)
    Crear una lista con los nombres de 8 estudiantes presentes en clase.
    • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
    • Mostrar la lista final actualizada.
    """
    print("\n--- EJERCICIO 5: Lista de estudiantes ---")
    
    # Lista inicial de 8 estudiantes
    estudiantes = ["Ana", "Carlos", "María", "Juan", "Laura", "Pedro", "Sofia", "Diego"]
    
    print("Lista inicial de estudiantes:")
    mostrar_lista(estudiantes, "Estudiantes presentes")
    
    while True:
        print(f"\nOpciones:")
        print("1. Agregar un estudiante")
        print("2. Eliminar un estudiante")
        print("3. Finalizar")
        
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            # Agregar estudiante
            nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ").strip()
            if nuevo_estudiante and nuevo_estudiante not in estudiantes:
                estudiantes.append(nuevo_estudiante)
                print(f"Estudiante '{nuevo_estudiante}' agregado exitosamente.")
            elif nuevo_estudiante in estudiantes:
                print("Error: El estudiante ya está en la lista.")
            else:
                print("Error: El nombre no puede estar vacío.")
        
        elif opcion == "2":
            # Eliminar estudiante
            if not estudiantes:
                print("No hay estudiantes para eliminar.")
                continue
            
            print("Estudiantes disponibles para eliminar:")
            for i, estudiante in enumerate(estudiantes):
                print(f"  {i+1}. {estudiante}")
            
            try:
                indice = int(input("Ingrese el número del estudiante a eliminar: ")) - 1
                if 0 <= indice < len(estudiantes):
                    estudiante_eliminado = estudiantes.pop(indice)
                    print(f"Estudiante '{estudiante_eliminado}' eliminado exitosamente.")
                else:
                    print("Error: Número fuera de rango.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")
        
        elif opcion == "3":
            break
        
        else:
            print("Error: Opción no válida.")
        
        # Mostrar lista actualizada
        mostrar_lista(estudiantes, "Lista actualizada")
    
    print(f"\nLista final de estudiantes ({len(estudiantes)} estudiantes):")
    mostrar_lista(estudiantes, "Lista final")

def ejercicio_6():
    """
    Ejercicio 6: Rotar elementos de una lista
    Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha
    (el último pasa a ser el primero).
    """
    print("\n--- EJERCICIO 6: Rotar elementos de una lista ---")
    
    # Lista con 7 números
    numeros = [10, 20, 30, 40, 50, 60, 70]
    
    print("Lista original:")
    mostrar_lista(numeros, "Lista original")
    
    # Rotar una posición hacia la derecha
    # El último elemento pasa a ser el primero
    numeros_rotados = [numeros[-1]] + numeros[:-1]
    
    print("\nLista rotada una posición hacia la derecha:")
    mostrar_lista(numeros_rotados, "Lista rotada")
    
    # Mostrar el cambio específico
    print(f"\nCambio realizado:")
    print(f"Último elemento ({numeros[-1]}) ahora es el primero")
    print(f"Todos los demás elementos se movieron una posición hacia la derecha")

def ejercicio_7():
    """
    Ejercicio 7: Matriz de temperaturas semanales
    Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
    • Calcular el promedio de las mínimas y el de las máximas.
    • Mostrar en qué día se registró la mayor amplitud térmica.
    """
    print("\n--- EJERCICIO 7: Matriz de temperaturas semanales ---")
    
    # Matriz 7x2: [temperatura_minima, temperatura_maxima] para cada día
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = [
        [15, 25],  # Lunes
        [12, 22],  # Martes
        [18, 28],  # Miércoles
        [14, 26],  # Jueves
        [16, 24],  # Viernes
        [20, 30],  # Sábado
        [17, 27]   # Domingo
    ]
    
    print("Temperaturas de la semana:")
    print("Día\t\tMínima\tMáxima\tAmplitud")
    print("-" * 40)
    
    amplitudes = []
    for i, (dia, temp) in enumerate(zip(dias_semana, temperaturas)):
        amplitud = temp[1] - temp[0]  # máxima - mínima
        amplitudes.append(amplitud)
        print(f"{dia}\t\t{temp[0]}°C\t{temp[1]}°C\t{amplitud}°C")
    
    # Calcular promedios
    minimas = [temp[0] for temp in temperaturas]
    maximas = [temp[1] for temp in temperaturas]
    
    promedio_minimas = sum(minimas) / len(minimas)
    promedio_maximas = sum(maximas) / len(maximas)
    
    print(f"\nPromedio de temperaturas mínimas: {promedio_minimas:.1f}°C")
    print(f"Promedio de temperaturas máximas: {promedio_maximas:.1f}°C")
    
    # Día con mayor amplitud térmica
    indice_mayor_amplitud = amplitudes.index(max(amplitudes))
    dia_mayor_amplitud = dias_semana[indice_mayor_amplitud]
    mayor_amplitud = amplitudes[indice_mayor_amplitud]
    
    print(f"Día con mayor amplitud térmica: {dia_mayor_amplitud} ({mayor_amplitud}°C)")

def ejercicio_8():
    """
    Ejercicio 8: Matriz de notas de estudiantes
    Crear una matriz con las notas de 5 estudiantes en 3 materias.
    • Mostrar el promedio de cada estudiante.
    • Mostrar el promedio de cada materia.
    """
    print("\n--- EJERCICIO 8: Matriz de notas de estudiantes ---")
    
    # Matriz 5x3: 5 estudiantes, 3 materias
    estudiantes = ["Ana", "Carlos", "María", "Juan", "Laura"]
    materias = ["Matemáticas", "Física", "Química"]
    
    # Notas de los estudiantes en cada materia
    notas = [
        [85, 92, 78],  # Ana
        [91, 88, 94],  # Carlos
        [76, 89, 82],  # María
        [88, 85, 90],  # Juan
        [93, 91, 87]   # Laura
    ]
    
    print("Notas de los estudiantes:")
    print("Estudiante\t", end="")
    for materia in materias:
        print(f"{materia}\t", end="")
    print("Promedio")
    print("-" * 60)
    
    # Calcular promedio de cada estudiante
    promedios_estudiantes = []
    for i, estudiante in enumerate(estudiantes):
        promedio = sum(notas[i]) / len(notas[i])
        promedios_estudiantes.append(promedio)
        
        print(f"{estudiante}\t\t", end="")
        for nota in notas[i]:
            print(f"{nota}\t\t", end="")
        print(f"{promedio:.1f}")
    
    print("\nPromedio por materia:")
    print("Materia\t\tPromedio")
    print("-" * 25)
    
    # Calcular promedio de cada materia
    for j, materia in enumerate(materias):
        suma_materia = sum(notas[i][j] for i in range(len(estudiantes)))
        promedio_materia = suma_materia / len(estudiantes)
        print(f"{materia}\t{promedio_materia:.1f}")

def ejercicio_9():
    """
    Ejercicio 9: Juego Ta-Te-Ti
    Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
    • Inicializarlo con guiones "-" representando casillas vacías.
    • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
    • Mostrar el tablero después de cada jugada.
    """
    print("\n--- EJERCICIO 9: Juego Ta-Te-Ti ---")
    
    # Inicializar tablero 3x3
    tablero = [["-" for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"
    
    def mostrar_tablero():
        print("\nTablero actual:")
        print("  0 1 2")
        for i, fila in enumerate(tablero):
            print(f"{i} {' '.join(fila)}")
    
    def verificar_ganador():
        # Verificar filas
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] != "-":
                return fila[0]
        
        # Verificar columnas
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] != "-":
                return tablero[0][col]
        
        # Verificar diagonales
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != "-":
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != "-":
            return tablero[0][2]
        
        return None
    
    def tablero_lleno():
        for fila in tablero:
            if "-" in fila:
                return False
        return True
    
    print("¡Bienvenido al Ta-Te-Ti!")
    print("Jugador X vs Jugador O")
    print("Ingrese las coordenadas (fila, columna) del 0 al 2")
    
    while True:
        mostrar_tablero()
        
        print(f"\nTurno del jugador {jugador_actual}")
        
        while True:
            try:
                fila = int(input("Fila (0-2): "))
                col = int(input("Columna (0-2): "))
                
                if 0 <= fila <= 2 and 0 <= col <= 2:
                    if tablero[fila][col] == "-":
                        tablero[fila][col] = jugador_actual
                        break
                    else:
                        print("Error: Esa casilla ya está ocupada.")
                else:
                    print("Error: Las coordenadas deben estar entre 0 y 2.")
            except ValueError:
                print("Error: Debe ingresar números válidos.")
        
        # Verificar si hay ganador
        ganador = verificar_ganador()
        if ganador:
            mostrar_tablero()
            print(f"\n¡Felicidades! El jugador {ganador} ha ganado!")
            break
        
        # Verificar si el tablero está lleno
        if tablero_lleno():
            mostrar_tablero()
            print("\n¡Empate! El tablero está lleno.")
            break
        
        # Cambiar jugador
        jugador_actual = "O" if jugador_actual == "X" else "X"

def ejercicio_10():
    """
    Ejercicio 10: Ventas de productos en una tienda
    Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
    • Mostrar el total vendido por cada producto.
    • Mostrar el día con mayores ventas totales.
    • Indicar cuál fue el producto más vendido en la semana.
    """
    print("\n--- EJERCICIO 10: Ventas de productos en una tienda ---")
    
    # Matriz 4x7: 4 productos, 7 días
    productos = ["Laptop", "Mouse", "Teclado", "Monitor"]
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    # Ventas de cada producto por día (simuladas)
    ventas = [
        [5, 3, 7, 4, 6, 8, 2],   # Laptop
        [12, 15, 8, 10, 14, 18, 6],  # Mouse
        [8, 6, 9, 7, 11, 13, 4],     # Teclado
        [3, 2, 4, 3, 5, 6, 1]        # Monitor
    ]
    
    print("Ventas de la semana:")
    print("=" * 95)
    
    # Encabezado de la tabla con mejor espaciado
    print(f"{'Producto':<12} {'Lunes':<6} {'Martes':<6} {'Miércoles':<9} {'Jueves':<6} {'Viernes':<7} {'Sábado':<6} {'Domingo':<7} {'Total':<6}")
    print("-" * 95)
    
    # Calcular total por producto
    totales_productos = []
    for i, producto in enumerate(productos):
        total = sum(ventas[i])
        totales_productos.append(total)
        
        print(f"{producto:<12} {ventas[i][0]:<6} {ventas[i][1]:<6} {ventas[i][2]:<9} {ventas[i][3]:<6} {ventas[i][4]:<7} {ventas[i][5]:<6} {ventas[i][6]:<7} {total:<6}")
    
    print("-" * 95)
    
    # Calcular total por día
    totales_dias = []
    for j in range(7):
        total_dia = sum(ventas[i][j] for i in range(4))
        totales_dias.append(total_dia)
    
    # Mostrar totales por día con mejor formato
    print(f"{'Total por día':<12} {totales_dias[0]:<6} {totales_dias[1]:<6} {totales_dias[2]:<9} {totales_dias[3]:<6} {totales_dias[4]:<7} {totales_dias[5]:<6} {totales_dias[6]:<7}", end="")
    
    # Calcular total general
    total_general = sum(totales_productos)
    print(f" {total_general:<6}")
    
    print("=" * 95)
    
    # Día con mayores ventas
    indice_dia_max = totales_dias.index(max(totales_dias))
    dia_max_ventas = dias[indice_dia_max]
    max_ventas = totales_dias[indice_dia_max]
    
    print(f"\nDía con mayores ventas: {dia_max_ventas} ({max_ventas} unidades)")
    
    # Producto más vendido
    indice_producto_max = totales_productos.index(max(totales_productos))
    producto_max_ventas = productos[indice_producto_max]
    max_ventas_producto = totales_productos[indice_producto_max]
    
    print(f"Producto más vendido: {producto_max_ventas} ({max_ventas_producto} unidades)")
    
    # Estadísticas adicionales
    print(f"\nEstadísticas adicionales:")
    print(f"Total general de ventas: {total_general} unidades")
    print(f"Promedio de ventas por día: {total_general/7:.1f} unidades")
    print(f"Promedio de ventas por producto: {total_general/4:.1f} unidades")
    
    # Mostrar resumen por producto
    print(f"\nResumen por producto:")
    for i, producto in enumerate(productos):
        promedio_producto = totales_productos[i] / 7
        print(f"  {producto}: {totales_productos[i]} unidades (promedio: {promedio_producto:.1f}/día)")
    
    # Mostrar resumen por día
    print(f"\nResumen por día:")
    for i, dia in enumerate(dias):
        promedio_dia = totales_dias[i] / 4
        print(f"  {dia}: {totales_dias[i]} unidades (promedio: {promedio_dia:.1f}/producto)")

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
