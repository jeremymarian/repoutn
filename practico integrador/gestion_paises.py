"""
Sistema de Gestión de Datos de Países
Trabajo Práctico Integrador - Programación 1
UTN - Tecnicatura Universitaria en Programación

Este programa permite gestionar información sobre países, aplicando
listas, diccionarios, funciones, estructuras condicionales y repetitivas,
ordenamientos y estadísticas.
"""

import csv
import os


def cargar_paises_desde_csv(nombre_archivo):
    """
    Carga la lista de países desde un archivo CSV.
    
    Args:
        nombre_archivo (str): Nombre del archivo CSV a leer
        
    Returns:
        list: Lista de diccionarios con los datos de los países
    """
    paises = []
    
    if not os.path.exists(nombre_archivo):
        print(f"Advertencia: El archivo '{nombre_archivo}' no existe. Se creará uno nuevo.")
        return paises
    
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    paises.append(pais)
                except (ValueError, KeyError) as e:
                    print(f"Error al procesar la fila: {fila}. Error: {e}")
                    continue
                    
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
    
    return paises


def guardar_paises_en_csv(paises, nombre_archivo):
    """
    Guarda la lista de países en un archivo CSV.
    
    Args:
        paises (list): Lista de diccionarios con los datos de los países
        nombre_archivo (str): Nombre del archivo CSV donde guardar
    """
    try:
        with open(nombre_archivo, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
            escritor.writeheader()
            
            for pais in paises:
                escritor.writerow(pais)
                
    except Exception as e:
        print(f"Error al guardar el archivo CSV: {e}")


def validar_entrada_no_vacia(mensaje):
    """
    Valida que el usuario ingrese un valor no vacío.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        
    Returns:
        str: Valor ingresado validado
    """
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: Este campo no puede estar vacío. Por favor, ingrese un valor.")


def validar_entrada_entero_positivo(mensaje):
    """
    Valida que el usuario ingrese un número entero positivo.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        
    Returns:
        int: Número entero positivo validado
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Error: Debe ingresar un número positivo mayor a 0.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")


def agregar_pais(paises):
    """
    Agrega un nuevo país a la lista.
    No se permiten campos vacíos.
    
    Args:
        paises (list): Lista de países
        
    Returns:
        bool: True si se agregó correctamente, False en caso contrario
    """
    print("\n--- AGREGAR PAÍS ---")
    
    nombre = validar_entrada_no_vacia("Ingrese el nombre del país: ")
    
    # Verificar si el país ya existe
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"Error: El país '{nombre}' ya existe en la lista.")
            return False
    
    poblacion = validar_entrada_entero_positivo("Ingrese la población: ")
    superficie = validar_entrada_entero_positivo("Ingrese la superficie en km²: ")
    continente = validar_entrada_no_vacia("Ingrese el continente: ")
    
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    paises.append(nuevo_pais)
    print(f"\n✓ País '{nombre}' agregado correctamente.")
    return True


def actualizar_pais(paises):
    """
    Actualiza los datos de Población y Superficie de un país.
    
    Args:
        paises (list): Lista de países
        
    Returns:
        bool: True si se actualizó correctamente, False en caso contrario
    """
    print("\n--- ACTUALIZAR PAÍS ---")
    
    if not paises:
        print("Error: No hay países en la lista.")
        return False
    
    nombre_buscado = validar_entrada_no_vacia("Ingrese el nombre del país a actualizar: ")
    
    pais_encontrado = None
    for pais in paises:
        if pais["nombre"].lower() == nombre_buscado.lower():
            pais_encontrado = pais
            break
    
    if not pais_encontrado:
        print(f"Error: No se encontró el país '{nombre_buscado}'.")
        return False
    
    print(f"\nPaís encontrado: {pais_encontrado['nombre']}")
    print(f"Población actual: {pais_encontrado['poblacion']}")
    print(f"Superficie actual: {pais_encontrado['superficie']} km²")
    
    print("\nIngrese los nuevos valores (presione Enter para mantener el valor actual):")
    
    nueva_poblacion_str = input("Nueva población: ").strip()
    if nueva_poblacion_str:
        try:
            nueva_poblacion = int(nueva_poblacion_str)
            if nueva_poblacion > 0:
                pais_encontrado["poblacion"] = nueva_poblacion
            else:
                print("Error: La población debe ser un número positivo.")
                return False
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
            return False
    
    nueva_superficie_str = input("Nueva superficie (km²): ").strip()
    if nueva_superficie_str:
        try:
            nueva_superficie = int(nueva_superficie_str)
            if nueva_superficie > 0:
                pais_encontrado["superficie"] = nueva_superficie
            else:
                print("Error: La superficie debe ser un número positivo.")
                return False
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
            return False
    
    print(f"\n✓ País '{pais_encontrado['nombre']}' actualizado correctamente.")
    return True


def buscar_pais(paises):
    """
    Busca un país por nombre (coincidencia parcial o exacta).
    
    Args:
        paises (list): Lista de países
    """
    print("\n--- BUSCAR PAÍS ---")
    
    if not paises:
        print("Error: No hay países en la lista.")
        return
    
    nombre_buscado = input("Ingrese el nombre del país a buscar: ").strip().lower()
    
    if not nombre_buscado:
        print("Error: Debe ingresar un nombre para buscar.")
        return
    
    paises_encontrados = []
    for pais in paises:
        if nombre_buscado in pais["nombre"].lower():
            paises_encontrados.append(pais)
    
    if not paises_encontrados:
        print(f"No se encontraron países que coincidan con '{nombre_buscado}'.")
    else:
        print(f"\nSe encontraron {len(paises_encontrados)} país(es):")
        print("-" * 70)
        for pais in paises_encontrados:
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']:,}")
            print(f"Superficie: {pais['superficie']:,} km²")
            print(f"Continente: {pais['continente']}")
            print("-" * 70)


def filtrar_por_continente(paises):
    """
    Filtra países por continente.
    
    Args:
        paises (list): Lista de países
    """
    print("\n--- FILTRAR POR CONTINENTE ---")
    
    if not paises:
        print("Error: No hay países en la lista.")
        return
    
    continente_buscado = validar_entrada_no_vacia("Ingrese el continente: ").strip()
    
    paises_filtrados = []
    for pais in paises:
        if pais["continente"].lower() == continente_buscado.lower():
            paises_filtrados.append(pais)
    
    if not paises_filtrados:
        print(f"No se encontraron países en el continente '{continente_buscado}'.")
    else:
        print(f"\nPaíses en '{continente_buscado}' ({len(paises_filtrados)} encontrados):")
        mostrar_lista_paises(paises_filtrados)


def filtrar_por_rango_poblacion(paises):
    """
    Filtra países por rango de población.
    
    Args:
        paises (list): Lista de países
    """
    print("\n--- FILTRAR POR RANGO DE POBLACIÓN ---")
    
    if not paises:
        print("Error: No hay países en la lista.")
        return
    
    try:
        min_poblacion = int(input("Ingrese la población mínima: "))
        max_poblacion = int(input("Ingrese la población máxima: "))
        
        if min_poblacion < 0 or max_poblacion < 0:
            print("Error: Los valores de población deben ser positivos.")
            return
        
        if min_poblacion > max_poblacion:
            print("Error: La población mínima no puede ser mayor que la máxima.")
            return
        
        paises_filtrados = []
        for pais in paises:
            if min_poblacion <= pais["poblacion"] <= max_poblacion:
                paises_filtrados.append(pais)
        
        if not paises_filtrados:
            print(f"No se encontraron países con población entre {min_poblacion:,} y {max_poblacion:,}.")
        else:
            print(f"\nPaíses con población entre {min_poblacion:,} y {max_poblacion:,} ({len(paises_filtrados)} encontrados):")
            mostrar_lista_paises(paises_filtrados)
            
    except ValueError:
        print("Error: Debe ingresar números enteros válidos.")


def filtrar_por_rango_superficie(paises):
    """
    Filtra países por rango de superficie.
    
    Args:
        paises (list): Lista de países
    """
    print("\n--- FILTRAR POR RANGO DE SUPERFICIE ---")
    
    if not paises:
        print("Error: No hay países en la lista.")
        return
    
    try:
        min_superficie = int(input("Ingrese la superficie mínima (km²): "))
        max_superficie = int(input("Ingrese la superficie máxima (km²): "))
        
        if min_superficie < 0 or max_superficie < 0:
            print("Error: Los valores de superficie deben ser positivos.")
            return
        
        if min_superficie > max_superficie:
            print("Error: La superficie mínima no puede ser mayor que la máxima.")
            return
        
        paises_filtrados = []
        for pais in paises:
            if min_superficie <= pais["superficie"] <= max_superficie:
                paises_filtrados.append(pais)
        
        if not paises_filtrados:
            print(f"No se encontraron países con superficie entre {min_superficie:,} y {max_superficie:,} km².")
        else:
            print(f"\nPaíses con superficie entre {min_superficie:,} y {max_superficie:,} km² ({len(paises_filtrados)} encontrados):")
            mostrar_lista_paises(paises_filtrados)
            
    except ValueError:
        print("Error: Debe ingresar números enteros válidos.")


def ordenar_por_nombre(paises):
    """
    Ordena países por nombre (ascendente).
    
    Args:
        paises (list): Lista de países a ordenar
        
    Returns:
        list: Lista de países ordenada
    """
    return sorted(paises, key=lambda x: x["nombre"].lower())


def ordenar_por_poblacion(paises, ascendente=True):
    """
    Ordena países por población.
    
    Args:
        paises (list): Lista de países a ordenar
        ascendente (bool): True para orden ascendente, False para descendente
        
    Returns:
        list: Lista de países ordenada
    """
    return sorted(paises, key=lambda x: x["poblacion"], reverse=not ascendente)


def ordenar_por_superficie(paises, ascendente=True):
    """
    Ordena países por superficie.
    
    Args:
        paises (list): Lista de países a ordenar
        ascendente (bool): True para orden ascendente, False para descendente
        
    Returns:
        list: Lista de países ordenada
    """
    return sorted(paises, key=lambda x: x["superficie"], reverse=not ascendente)


def mostrar_lista_paises(paises):
    """
    Muestra una lista de países formateada.
    
    Args:
        paises (list): Lista de países a mostrar
    """
    if not paises:
        print("No hay países para mostrar.")
        return
    
    print("\n" + "=" * 80)
    print(f"{'Nombre':<25} {'Población':<15} {'Superficie (km²)':<20} {'Continente':<15}")
    print("=" * 80)
    
    for pais in paises:
        print(f"{pais['nombre']:<25} {pais['poblacion']:>15,} {pais['superficie']:>20,} {pais['continente']:<15}")
    
    print("=" * 80)


def mostrar_menu_ordenamiento():
    """
    Muestra el menú de opciones de ordenamiento.
    """
    print("\n--- ORDENAMIENTO ---")
    print("1. Ordenar por nombre (ascendente)")
    print("2. Ordenar por población (ascendente)")
    print("3. Ordenar por población (descendente)")
    print("4. Ordenar por superficie (ascendente)")
    print("5. Ordenar por superficie (descendente)")
    print("6. Cancelar")


def aplicar_ordenamiento(paises):
    """
    Aplica un ordenamiento a la lista de países y muestra el resultado.
    
    Args:
        paises (list): Lista de países
    """
    if not paises:
        print("Error: No hay países en la lista.")
        return
    
    mostrar_menu_ordenamiento()
    opcion = input("\nSeleccione una opción: ").strip()
    
    paises_ordenados = []
    
    if opcion == "1":
        paises_ordenados = ordenar_por_nombre(paises)
        print("\nPaíses ordenados por nombre (ascendente):")
    elif opcion == "2":
        paises_ordenados = ordenar_por_poblacion(paises, ascendente=True)
        print("\nPaíses ordenados por población (ascendente):")
    elif opcion == "3":
        paises_ordenados = ordenar_por_poblacion(paises, ascendente=False)
        print("\nPaíses ordenados por población (descendente):")
    elif opcion == "4":
        paises_ordenados = ordenar_por_superficie(paises, ascendente=True)
        print("\nPaíses ordenados por superficie (ascendente):")
    elif opcion == "5":
        paises_ordenados = ordenar_por_superficie(paises, ascendente=False)
        print("\nPaíses ordenados por superficie (descendente):")
    elif opcion == "6":
        return
    else:
        print("Error: Opción inválida.")
        return
    
    mostrar_lista_paises(paises_ordenados)


def estadistica_pais_mayor_menor_poblacion(paises):
    """
    Calcula el país con mayor y menor población.
    
    Args:
        paises (list): Lista de países
    """
    if not paises:
        print("Error: No hay países en la lista.")
        return
    
    mayor_poblacion = max(paises, key=lambda x: x["poblacion"])
    menor_poblacion = min(paises, key=lambda x: x["poblacion"])
    
    print("\n--- ESTADÍSTICAS DE POBLACIÓN ---")
    print(f"País con mayor población: {mayor_poblacion['nombre']} ({mayor_poblacion['poblacion']:,} habitantes)")
    print(f"País con menor población: {menor_poblacion['nombre']} ({menor_poblacion['poblacion']:,} habitantes)")


def estadistica_promedio_poblacion(paises):
    """
    Calcula el promedio de población.
    
    Args:
        paises (list): Lista de países
    """
    if not paises:
        print("Error: No hay países en la lista.")
        return
    
    total_poblacion = sum(pais["poblacion"] for pais in paises)
    promedio = total_poblacion / len(paises)
    
    print("\n--- PROMEDIO DE POBLACIÓN ---")
    print(f"Promedio de población: {promedio:,.2f} habitantes")


def estadistica_promedio_superficie(paises):
    """
    Calcula el promedio de superficie.
    
    Args:
        paises (list): Lista de países
    """
    if not paises:
        print("Error: No hay países en la lista.")
        return
    
    total_superficie = sum(pais["superficie"] for pais in paises)
    promedio = total_superficie / len(paises)
    
    print("\n--- PROMEDIO DE SUPERFICIE ---")
    print(f"Promedio de superficie: {promedio:,.2f} km²")


def estadistica_paises_por_continente(paises):
    """
    Calcula la cantidad de países por continente.
    
    Args:
        paises (list): Lista de países
    """
    if not paises:
        print("Error: No hay países en la lista.")
        return
    
    continentes = {}
    for pais in paises:
        continente = pais["continente"]
        continentes[continente] = continentes.get(continente, 0) + 1
    
    print("\n--- CANTIDAD DE PAÍSES POR CONTINENTE ---")
    for continente, cantidad in sorted(continentes.items()):
        print(f"{continente}: {cantidad} país(es)")


def mostrar_estadisticas(paises):
    """
    Muestra todas las estadísticas disponibles.
    
    Args:
        paises (list): Lista de países
    """
    if not paises:
        print("Error: No hay países en la lista.")
        return
    
    print("\n" + "=" * 70)
    print("ESTADÍSTICAS GENERALES")
    print("=" * 70)
    
    estadistica_pais_mayor_menor_poblacion(paises)
    estadistica_promedio_poblacion(paises)
    estadistica_promedio_superficie(paises)
    estadistica_paises_por_continente(paises)
    
    print("=" * 70)


def mostrar_menu():
    """
    Muestra el menú principal del programa.
    """
    print("\n" + "=" * 70)
    print("SISTEMA DE GESTIÓN DE DATOS DE PAÍSES")
    print("=" * 70)
    print("1. Agregar un país")
    print("2. Actualizar datos de un país (Población y Superficie)")
    print("3. Buscar un país por nombre")
    print("4. Filtrar países por continente")
    print("5. Filtrar países por rango de población")
    print("6. Filtrar países por rango de superficie")
    print("7. Ordenar países")
    print("8. Mostrar estadísticas")
    print("9. Mostrar todos los países")
    print("10. Salir")
    print("=" * 70)


def main():
    """
    Función principal que ejecuta el programa.
    Carga los países desde CSV al iniciar y guarda tras cada modificación.
    """
    nombre_archivo = "paises.csv"
    paises = cargar_paises_desde_csv(nombre_archivo)
    
    if paises:
        print(f"\n✓ Se cargaron {len(paises)} país(es) desde '{nombre_archivo}'.")
    else:
        print(f"\nℹ No hay países cargados. Puede agregar nuevos países desde el menú.")
    
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            if agregar_pais(paises):
                guardar_paises_en_csv(paises, nombre_archivo)
                print(f"✓ Datos guardados en '{nombre_archivo}'.")
        
        elif opcion == "2":
            if actualizar_pais(paises):
                guardar_paises_en_csv(paises, nombre_archivo)
                print(f"✓ Datos guardados en '{nombre_archivo}'.")
        
        elif opcion == "3":
            buscar_pais(paises)
        
        elif opcion == "4":
            filtrar_por_continente(paises)
        
        elif opcion == "5":
            filtrar_por_rango_poblacion(paises)
        
        elif opcion == "6":
            filtrar_por_rango_superficie(paises)
        
        elif opcion == "7":
            aplicar_ordenamiento(paises)
        
        elif opcion == "8":
            mostrar_estadisticas(paises)
        
        elif opcion == "9":
            print("\n--- LISTADO COMPLETO DE PAÍSES ---")
            mostrar_lista_paises(paises)
        
        elif opcion == "10":
            guardar_paises_en_csv(paises, nombre_archivo)
            print("\n✓ Datos guardados.")
            print("¡Gracias por usar el Sistema de Gestión de Datos de Países!")
            continuar = False
        
        else:
            print("\nError: Opción inválida. Por favor, seleccione una opción del 1 al 10.")
        
        if continuar:
            input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()


