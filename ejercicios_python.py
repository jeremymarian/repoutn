import math


def ejercicio1():
    print("Hola Mundo!")


def ejercicio2():
    nombre = input("Ingresa tu nombre: ")
    print(f"Hola {nombre}!")


def ejercicio3():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    residencia = input("Ingresa tu lugar de residencia: ")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


def ejercicio4():
    radio = float(input("Ingresa el radio del círculo: "))
    area = math.pi * (radio ** 2)
    perimetro = 2 * math.pi * radio
    print(f"Área: {area:.2f}")
    print(f"Perímetro: {perimetro:.2f}")


def ejercicio5():
    segundos = int(input("Ingresa la cantidad de segundos: "))
    horas = segundos / 3600
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")


def ejercicio6():
    numero = int(input("Ingresa un número: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def ejercicio7():
    num1 = int(input("Ingresa el primer número (distinto de 0): "))
    num2 = int(input("Ingresa el segundo número (distinto de 0): "))
    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")
    print(f"División: {num1 / num2}")


def ejercicio8():
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    imc = peso / (altura ** 2)
    print(f"Tu índice de masa corporal es: {imc:.2f}")


def ejercicio9():
    celsius = float(input("Ingresa la temperatura en °C: "))
    fahrenheit = (9/5) * celsius + 32
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")


def ejercicio10():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))
    promedio = (num1 + num2 + num3) / 3
    print(f"El promedio es: {promedio:.2f}")


def main():
    while True:
        opcion = input("Elegí un ejercicio (1-10) o \"q\" para salir: ").strip().lower()
        if opcion in ("q", "quit", "salir"):
            break
        if not opcion.isdigit():
            print("Opción inválida.")
            continue
        numero = int(opcion)
        if 1 <= numero <= 10:
            globals()[f"ejercicio{numero}"]()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
