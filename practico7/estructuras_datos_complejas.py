import re

def actividad_1():
    """Actividad 1: Añadir frutas al diccionario precios_frutas"""
    print("\n--- ACTIVIDAD 1: AÑADIR FRUTAS ---")
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    
    print("Diccionario inicial:")
    for fruta, precio in precios_frutas.items():
        print(f"{fruta}: ${precio}")
    
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300
    
    print("\nDiccionario después de añadir frutas:")
    for fruta, precio in precios_frutas.items():
        print(f"{fruta}: ${precio}")
    
    return precios_frutas

def actividad_2():
    """Actividad 2: Actualizar precios de frutas"""
    print("\n--- ACTIVIDAD 2: ACTUALIZAR PRECIOS ---")
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 
                      'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
    
    print("Diccionario antes de actualizar:")
    for fruta, precio in precios_frutas.items():
        print(f"{fruta}: ${precio}")
    
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800
    
    print("\nDiccionario después de actualizar precios:")
    for fruta, precio in precios_frutas.items():
        print(f"{fruta}: ${precio}")
    
    return precios_frutas

def actividad_3():
    """Actividad 3: Crear lista con solo las frutas"""
    print("\n--- ACTIVIDAD 3: LISTA DE FRUTAS ---")
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 
                      'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}
    
    lista_frutas = list(precios_frutas.keys())
    
    print("Lista de frutas (sin precios):")
    for i, fruta in enumerate(lista_frutas, 1):
        print(f"{i}. {fruta}")
    
    return lista_frutas

def actividad_4():
    """Actividad 4: Programa de números telefónicos"""
    print("\n--- ACTIVIDAD 4: AGENDA TELEFÓNICA ---")
    contactos = {}
    
    print("Cargar 5 contactos:")
    for i in range(5):
        nombre = input(f"Ingrese el nombre del contacto {i+1}: ").strip()
        if nombre:
            numero = input(f"Ingrese el número de {nombre}: ").strip()
            if numero:
                contactos[nombre] = numero
                print(f"Contacto '{nombre}' agregado exitosamente.")
            else:
                print("Error: El número no puede estar vacío.")
        else:
            print("Error: El nombre no puede estar vacío.")
    
    print(f"\nSe cargaron {len(contactos)} contactos.")
    
    nombre_consulta = input("\nIngrese el nombre a consultar: ").strip()
    if nombre_consulta in contactos:
        print(f"El número de {nombre_consulta} es: {contactos[nombre_consulta]}")
    else:
        print(f"No se encontró el contacto '{nombre_consulta}'.")
    
    return contactos

def actividad_5():
    """Actividad 5: Análisis de palabras en una frase"""
    print("\n--- ACTIVIDAD 5: ANÁLISIS DE FRASE ---")
    frase = input("Ingrese una frase: ").strip()
    
    if frase:
        palabras = re.findall(r'\b\w+\b', frase.lower())
        
        palabras_unicas = set(palabras)
        
        conteo_palabras = {}
        for palabra in palabras:
            conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1
        
        print(f"\nFrase original: '{frase}'")
        print(f"\nPalabras únicas ({len(palabras_unicas)}):")
        for palabra in sorted(palabras_unicas):
            print(f"- {palabra}")
        
        print(f"\nCantidad de apariciones por palabra:")
        for palabra, cantidad in sorted(conteo_palabras.items()):
            print(f"- {palabra}: {cantidad}")
        
        return palabras_unicas, conteo_palabras
    else:
        print("Error: La frase no puede estar vacía.")
        return None, None

def actividad_6():
    """Actividad 6: Promedio de notas de alumnos"""
    print("\n--- ACTIVIDAD 6: PROMEDIO DE NOTAS ---")
    alumnos = {}
    
    for i in range(3):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ").strip()
        if nombre:
            print(f"Ingrese las 3 notas de {nombre}:")
            notas = []
            for j in range(3):
                while True:
                    try:
                        nota = float(input(f"Nota {j+1}: "))
                        if 0 <= nota <= 10:
                            notas.append(nota)
                            break
                        else:
                            print("Error: La nota debe estar entre 0 y 10.")
                    except ValueError:
                        print("Error: Debe ingresar un número válido.")
            
            alumnos[nombre] = tuple(notas)
            print(f"Notas de {nombre}: {notas}")
        else:
            print("Error: El nombre no puede estar vacío.")
    
    print("\nPromedios de los alumnos:")
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"{nombre}: {promedio:.2f}")
    
    return alumnos

def actividad_7():
    """Actividad 7: Análisis de estudiantes que aprobaron parciales"""
    print("\n--- ACTIVIDAD 7: ESTUDIANTES QUE APROBARON PARCIALES ---")
    
    parcial_1 = {1, 2, 3, 4, 5, 6}
    parcial_2 = {3, 4, 5, 6, 7, 8}
    
    print(f"Estudiantes que aprobaron Parcial 1: {parcial_1}")
    print(f"Estudiantes que aprobaron Parcial 2: {parcial_2}")
    
    aprobaron_ambos = parcial_1.intersection(parcial_2)
    print(f"\nEstudiantes que aprobaron ambos parciales: {aprobaron_ambos}")
    
    solo_parcial_1 = parcial_1 - parcial_2
    solo_parcial_2 = parcial_2 - parcial_1
    aprobaron_solo_uno = solo_parcial_1.union(solo_parcial_2)
    print(f"Estudiantes que aprobaron solo Parcial 1: {solo_parcial_1}")
    print(f"Estudiantes que aprobaron solo Parcial 2: {solo_parcial_2}")
    print(f"Estudiantes que aprobaron solo uno de los dos: {aprobaron_solo_uno}")
    
    aprobaron_al_menos_uno = parcial_1.union(parcial_2)
    print(f"Estudiantes que aprobaron al menos un parcial: {aprobaron_al_menos_uno}")
    
    return aprobaron_ambos, aprobaron_solo_uno, aprobaron_al_menos_uno

def actividad_8():
    """Actividad 8: Sistema de gestión de stock"""
    print("\n--- ACTIVIDAD 8: GESTIÓN DE STOCK ---")
    stock = {}
    
    while True:
        print("\nOpciones:")
        print("1. Consultar stock de un producto")
        print("2. Agregar unidades al stock")
        print("3. Agregar nuevo producto")
        print("4. Ver todos los productos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            producto = input("Ingrese el nombre del producto a consultar: ").strip()
            if producto in stock:
                print(f"Stock de '{producto}': {stock[producto]} unidades")
            else:
                print(f"El producto '{producto}' no existe en el stock.")
        
        elif opcion == "2":
            producto = input("Ingrese el nombre del producto: ").strip()
            if producto in stock:
                try:
                    cantidad = int(input("Ingrese la cantidad a agregar: "))
                    if cantidad > 0:
                        stock[producto] += cantidad
                        print(f"Se agregaron {cantidad} unidades. Stock actual: {stock[producto]}")
                    else:
                        print("Error: La cantidad debe ser positiva.")
                except ValueError:
                    print("Error: Debe ingresar un número entero.")
            else:
                print(f"El producto '{producto}' no existe en el stock.")
        
        elif opcion == "3":
            producto = input("Ingrese el nombre del nuevo producto: ").strip()
            if producto:
                try:
                    cantidad = int(input("Ingrese el stock inicial: "))
                    if cantidad >= 0:
                        stock[producto] = cantidad
                        print(f"Producto '{producto}' agregado con {cantidad} unidades.")
                    else:
                        print("Error: El stock no puede ser negativo.")
                except ValueError:
                    print("Error: Debe ingresar un número entero.")
            else:
                print("Error: El nombre del producto no puede estar vacío.")
        
        elif opcion == "4":
            if stock:
                print("\nStock actual:")
                for producto, cantidad in stock.items():
                    print(f"- {producto}: {cantidad} unidades")
            else:
                print("No hay productos en el stock.")
        
        elif opcion == "5":
            break
        
        else:
            print("Error: Opción inválida.")
    
    return stock

def actividad_9():
    """Actividad 9: Agenda con tuplas como claves"""
    print("\n--- ACTIVIDAD 9: AGENDA CON TUPLAS ---")
    agenda = {}
    
    agenda[('Lunes', '09:00')] = 'Reunión de equipo'
    agenda[('Lunes', '14:00')] = 'Clase de Python'
    agenda[('Martes', '10:00')] = 'Entrevista de trabajo'
    agenda[('Miércoles', '16:00')] = 'Cita médica'
    agenda[('Viernes', '11:00')] = 'Presentación proyecto'
    
    print("Eventos cargados en la agenda:")
    for (dia, hora), evento in agenda.items():
        print(f"{dia} {hora}: {evento}")
    
    print("\nConsulta de eventos:")
    dia = input("Ingrese el día: ").strip().capitalize()
    hora = input("Ingrese la hora (formato HH:MM): ").strip()
    
    if (dia, hora) in agenda:
        print(f"Evento programado: {agenda[(dia, hora)]}")
    else:
        print(f"No hay eventos programados para {dia} a las {hora}.")
    
    return agenda

def actividad_10():
    """Actividad 10: Invertir diccionario países-capitales"""
    print("\n--- ACTIVIDAD 10: INVERTIR DICCIONARIO ---")
    
    paises_capitales = {
        'Argentina': 'Buenos Aires',
        'Brasil': 'Brasilia',
        'Chile': 'Santiago',
        'Colombia': 'Bogotá',
        'México': 'Ciudad de México',
        'Perú': 'Lima',
        'España': 'Madrid',
        'Francia': 'París'
    }
    
    print("Diccionario original (países -> capitales):")
    for pais, capital in paises_capitales.items():
        print(f"{pais}: {capital}")
    
    capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
    
    print("\nDiccionario invertido (capitales -> países):")
    for capital, pais in capitales_paises.items():
        print(f"{capital}: {pais}")
    
    return paises_capitales, capitales_paises

def validar_entero(mensaje):
    """Función auxiliar para validar entrada de números enteros"""
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

print("Bienvenido al Práctico 6: Estructuras de datos complejas")
print("Este programa implementa las 10 actividades sobre diccionarios, tuplas y sets.")

opcion = 0

while opcion != 11:
    print("\n" + "="*70)
    print("         PRÁCTICO 6: ESTRUCTURAS DE DATOS COMPLEJAS")
    print("="*70)
    print("1.  Añadir frutas al diccionario")
    print("2.  Actualizar precios de frutas")
    print("3.  Crear lista de frutas")
    print("4.  Agenda telefónica")
    print("5.  Análisis de frase")
    print("6.  Promedio de notas de alumnos")
    print("7.  Estudiantes que aprobaron parciales")
    print("8.  Gestión de stock")
    print("9.  Agenda con tuplas")
    print("10. Invertir diccionario países-capitales")
    print("11. Salir")
    print("="*70)
    
    entrada = input("\nSeleccione una opción (1-11): ")
    if entrada.isdigit():
        opcion = int(entrada)
    else:
        print("Error: Debe ingresar un número entero válido.")
        opcion = 0
    
    if opcion == 1:
        actividad_1()
    
    elif opcion == 2:
        actividad_2()
    
    elif opcion == 3:
        actividad_3()
    
    elif opcion == 4:
        actividad_4()
    
    elif opcion == 5:
        actividad_5()
    
    elif opcion == 6:
        actividad_6()
    
    elif opcion == 7:
        actividad_7()
    
    elif opcion == 8:
        actividad_8()
    
    elif opcion == 9:
        actividad_9()
    
    elif opcion == 10:
        actividad_10()
    
    elif opcion == 11:
        print("\n¡Gracias por usar el programa del Práctico 6!")
        print("Programa finalizado.")
    else:
        print("Error: Opción inválida. Seleccione una opción del 1 al 11.")
    
    if opcion != 11:
        input("\nPresione Enter para continuar...")
