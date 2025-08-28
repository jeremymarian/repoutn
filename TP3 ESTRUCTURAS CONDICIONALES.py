# TP3 - Estructuras Condicionales - Python
# Menu Principal para el Profesor
# Autor: MARIANO JEREMIAS MOCHO
# Este programa permite seleccionar y ejecutar cualquier ejercicio del TP

import os
import sys

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_titulo():
    """Muestra el título principal del programa"""
    print("="*70)
    print("TRABAJO PRACTICO N°3 - ESTRUCTURAS CONDICIONALES")
    print("Universidad Tecnologica Nacional (UTN)")
    print("Programacion en Python")
    print("="*70)
    print()

def mostrar_menu():
    """Muestra el menú de opciones disponibles"""
    print("SELECCIONE EL EJERCICIO QUE DESEA PROBAR:")
    print()
    print("   1.  Verificar si es mayor de edad")
    print("   2.  Evaluar nota de aprobacion")
    print("   3.  Verificar si un numero es par")
    print("   4.  Categorizar por edades")
    print("   5.  Validar contrasena")
    print("   6.  Analisis de sesgo estadistico")
    print("   7.  Agregar exclamacion a vocales")
    print("   8.  Transformar nombre")
    print("   9.  Clasificar terremotos (Escala Richter)")
    print("   10. Determinar estacion del ano")
    print()
    print("   0.  Salir del programa")
    print("-"*70)

def ejecutar_ejercicio_1():
    """Ejercicio 1: Verificar mayor de edad"""
    print("EJERCICIO 1: VERIFICAR MAYOR DE EDAD")
    print("="*50)
    print("Descripcion: Le pido la edad al usuario y chequeo si ya es mayor")
    print()
    
    try:
        edad = int(input("Ingrese su edad: "))
        print()
        
        if edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")
    except ValueError:
        print("Error: Por favor ingrese un numero valido")

def ejecutar_ejercicio_2():
    """Ejercicio 2: Evaluar nota"""
    print("EJERCICIO 2: EVALUAR NOTA DE APROBACION")
    print("="*50)
    print("Descripcion: Le pido la nota al usuario y veo si zafo o la clavo")
    print()
    
    try:
        nota = float(input("Ingrese su nota (0-10): "))
        print()
        
        if nota >= 6:
            print("Aprobado! Zafaste con la nota")
        else:
            print("Desaprobado, a estudiar mas para la proxima")
    except ValueError:
        print("Error: Por favor ingrese un numero valido")

def ejecutar_ejercicio_3():
    """Ejercicio 3: Número par"""
    print(" EJERCICIO 3: VERIFICAR NÚMERO PAR")
    print("="*50)
    print(" Descripción: Solo dejo pasar números pares usando el módulo (%)")
    print()
    
    try:
        numero = int(input(" Ingrese un número: "))
        print()
        
        if numero % 2 == 0:
            print(" Perfecto! Ha ingresado un número par")
        else:
            print(" Por favor, ingrese un número par")
    except ValueError:
        print("Error: Por favor ingrese un numero valido")

def ejecutar_ejercicio_4():
    """Ejercicio 4: Categorizar edades"""
    print(" EJERCICIO 4: CATEGORIZAR POR EDADES")
    print("="*50)
    print(" Descripción: Pongo a cada persona en su categoría según los años que tenga")
    print()
    
    try:
        edad = int(input("Ingrese su edad: "))
        print()
        
        if edad < 12:
            print(" Niño/a")
        elif edad >= 12 and edad < 18:
            print(" Adolescente")
        elif edad >= 18 and edad < 30:
            print(" Adulto/a joven")
        else:
            print(" Adulto/a")
    except ValueError:
        print("Error: Por favor ingrese un numero valido")

def ejecutar_ejercicio_5():
    """Ejercicio 5: Validar contraseña"""
    print(" EJERCICIO 5: VALIDAR CONTRASEÑA")
    print("="*50)
    print(" Descripción: Me fijo que tenga entre 8 y 14 caracteres usando len()")
    print()
    
    contrasena = input(" Ingrese una contraseña: ")
    print()
    
    if len(contrasena) >= 8 and len(contrasena) <= 14:
        print(" Contraseña válida! Tiene la longitud correcta")
    else:
        print(" Contraseña inválida. Debe tener entre 8 y 14 caracteres")
        print(f"   (Su contraseña tiene {len(contrasena)} caracteres)")

def ejecutar_ejercicio_6():
    """Ejercicio 6: Sesgo estadístico"""
    print("EJERCICIO 6: ANALISIS DE SESGO ESTADISTICO")
    print("="*50)
    print("Descripcion: Calculo moda, mediana y media para ver si esta sesgado")
    print()
    
    import random
    from statistics import median, mean
    
    try:
        # Hago una lista con numeros random
        numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
        
        print(f"Lista de numeros: {numeros_aleatorios}")
        print()
        
        # Saco los valores estadisticos
        mediana = median(numeros_aleatorios)
        media = mean(numeros_aleatorios)
        
        # Calculo la moda manualmente para evitar errores
        # Cuenta la frecuencia de cada numero
        frecuencias = {}
        for num in numeros_aleatorios:
            frecuencias[num] = frecuencias.get(num, 0) + 1
        
        # Encuentra el numero con mayor frecuencia
        max_frecuencia = max(frecuencias.values())
        modas = [num for num, freq in frecuencias.items() if freq == max_frecuencia]
        
        if len(modas) == len(frecuencias):
            # Todos los numeros aparecen la misma cantidad de veces
            moda = sum(numeros_aleatorios) / len(numeros_aleatorios)  # usar la media
            print("No hay moda clara (todos los valores aparecen igual), usando la media")
        else:
            moda = modas[0]  # tomo la primera moda
        
        print(f"Moda: {moda}")
        print(f"Mediana: {mediana}")
        print(f"Media: {media:.2f}")
        print()
        
        # Me fijo que tipo de sesgo es
        print("Analisis del sesgo:")
        if media > mediana and mediana > moda:
            print("La distribucion tiene sesgo positivo o a la derecha")
            print("(Media > Mediana > Moda)")
        elif media < mediana and mediana < moda:
            print("La distribucion tiene sesgo negativo o a la izquierda") 
            print("(Media < Mediana < Moda)")
        elif abs(media - mediana) < 2 and abs(mediana - moda) < 2:
            print("La distribucion no tiene sesgo significativo")
            print("(Los valores son muy parecidos)")
        else:
            # Analisis mas flexible
            if media > mediana:
                print("La distribucion tiende a tener sesgo positivo")
                print("(La media es mayor que la mediana)")
            elif media < mediana:
                print("La distribucion tiende a tener sesgo negativo")
                print("(La media es menor que la mediana)")
            else:
                print("La distribucion es aproximadamente simetrica")
                print("(Media y mediana son iguales)")
    except Exception as e:
        print(f"Error en el calculo estadistico: {e}")

def ejecutar_ejercicio_7():
    """Ejercicio 7: Vocal con exclamación"""
    print(" EJERCICIO 7: AGREGAR EXCLAMACIÓN A VOCALES")
    print("="*50)
    print(" Descripción: Me fijo si la palabra termina en vocal y le pongo !")
    print()
    
    frase = input(" Ingrese una frase o palabra: ")
    print()
    
    if frase:
        vocales = "aeiouAEIOU"
        
        if frase[-1] in vocales:
            resultado = frase + "!"
            print(f" Resultado: {resultado}")
        else:
            print(f" Resultado: {frase}")
    else:
        print("  No ingresó ninguna palabra")

def ejecutar_ejercicio_8():
    """Ejercicio 8: Transformar nombre"""
    print(" EJERCICIO 8: TRANSFORMAR NOMBRE")
    print("="*50)
    print(" Descripción: Deja convertir el nombre a mayúsculas, minúsculas o solo la primera en mayúscula")
    print()
    
    nombre = input(" Ingrese su nombre: ")
    print()
    print("  Seleccione una opción:")
    print("   1. Nombre en MAYÚSCULAS")
    print("   2. Nombre en minúsculas") 
    print("   3. Nombre con Primera Letra Mayúscula")
    print()
    
    try:
        opcion = int(input(" Ingrese el número de opción (1, 2 o 3): "))
        print()
        
        if opcion == 1:
            resultado = nombre.upper()
            print(f" Resultado: {resultado}")
        elif opcion == 2:
            resultado = nombre.lower()
            print(f" Resultado: {resultado}")
        elif opcion == 3:
            resultado = nombre.title()
            print(f" Resultado: {resultado}")
        else:
            print(" Opción no válida. Por favor, ingrese 1, 2 o 3.")
    except ValueError:
        print("Error: Por favor ingrese un numero valido")

def ejecutar_ejercicio_9():
    """Ejercicio 9: Escala de Richter"""
    print(" EJERCICIO 9: CLASIFICAR TERREMOTOS (ESCALA RICHTER)")
    print("="*50)
    print(" Descripción: Dependiendo de la magnitud te dice qué tan groso es el terremoto")
    print()
    
    try:
        magnitud = float(input(" Ingrese la magnitud del terremoto: "))
        print()
        
        if magnitud < 3:
            print(" Muy leve (imperceptible)")
        elif magnitud >= 3 and magnitud < 4:
            print(" Leve (ligeramente perceptible)")
        elif magnitud >= 4 and magnitud < 5:
            print(" Moderado (sentido por personas, pero generalmente no causa daños)")
        elif magnitud >= 5 and magnitud < 6:
            print(" Fuerte (puede causar daños en estructuras débiles)")
        elif magnitud >= 6 and magnitud < 7:
            print(" Muy Fuerte (puede causar daños significativos)")
        else:
            print(" Extremo (puede causar graves daños a gran escala)")
    except ValueError:
        print("Error: Por favor ingrese un numero valido")

def ejecutar_ejercicio_10():
    """Ejercicio 10: Estaciones del año"""
    print(" EJERCICIO 10: DETERMINAR ESTACIÓN DEL AÑO")
    print("="*50)
    print(" Descripción: Dependiendo si estás en el norte o sur, y la fecha, te dice la estación")
    print()
    
    try:
        hemisferio = input(" ¿En qué hemisferio se encuentra? (N/S): ").upper()
        mes = int(input(" ¿Qué mes del año es? (1-12): "))
        dia = int(input(" ¿Qué día es? (1-31): "))
        print()
        
        # Calculo la estación según el hemisferio norte
        if (mes == 12 and dia >= 21) or (mes >= 1 and mes <= 2) or (mes == 3 and dia <= 20):
            estacion_norte = "Invierno "
            estacion_sur = "Verano "
        elif (mes == 3 and dia >= 21) or (mes >= 4 and mes <= 5) or (mes == 6 and dia <= 20):
            estacion_norte = "Primavera "
            estacion_sur = "Otoño "
        elif (mes == 6 and dia >= 21) or (mes >= 7 and mes <= 8) or (mes == 9 and dia <= 20):
            estacion_norte = "Verano "
            estacion_sur = "Invierno "
        else:  # (mes == 9 and dia >= 21) or (mes >= 10 and mes <= 11) or (mes == 12 and dia <= 20)
            estacion_norte = "Otoño "
            estacion_sur = "Primavera "
        
        # Muestro el resultado según el hemisferio
        if hemisferio == "N":
            print(f" Se encuentra en {estacion_norte}")
        elif hemisferio == "S":
            print(f" Se encuentra en {estacion_sur}")
        else:
            print(" Hemisferio no válido. Por favor, ingrese N o S.")
    except ValueError:
        print("Error: Por favor ingrese valores numericos validos")

def pausar():
    """Pausa el programa hasta que el usuario presione Enter"""
    print()
    input("Presione Enter para continuar...")

def main():
    """Función principal del programa"""
    while True:
        limpiar_pantalla()
        mostrar_titulo()
        mostrar_menu()
        
        try:
            opcion = input("Seleccione una opcion: ")
            print()
            
            if opcion == "1":
                ejecutar_ejercicio_1()
            elif opcion == "2":
                ejecutar_ejercicio_2()
            elif opcion == "3":
                ejecutar_ejercicio_3()
            elif opcion == "4":
                ejecutar_ejercicio_4()
            elif opcion == "5":
                ejecutar_ejercicio_5()
            elif opcion == "6":
                ejecutar_ejercicio_6()
            elif opcion == "7":
                ejecutar_ejercicio_7()
            elif opcion == "8":
                ejecutar_ejercicio_8()
            elif opcion == "9":
                ejecutar_ejercicio_9()
            elif opcion == "10":
                ejecutar_ejercicio_10()
            elif opcion == "0":
                print("Gracias por usar el programa!")
                print("Trabajo Practico completado - UTN")
                break
            else:
                print("Opcion no valida. Por favor, seleccione un numero del 0 al 10.")
            
            pausar()
            
        except KeyboardInterrupt:
            print("\n\nPrograma finalizado por el usuario.")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
            pausar()

if __name__ == "__main__":
    main()