"""
Archivo de pruebas para verificar todas las funciones recursivas
"""

from practico11_recursividad import (
    factorial,
    fibonacci,
    potencia,
    decimal_a_binario,
    es_palindromo,
    suma_digitos,
    contar_bloques,
    contar_digito
)


def test_todas_las_funciones():
    """Prueba todas las funciones con ejemplos."""
    
    print("="*60)
    print("PRUEBAS DE FUNCIONES RECURSIVAS")
    print("="*60)
    
    # Test 1: Factorial
    print("\n1. FACTORIAL:")
    print(f"   factorial(5) = {factorial(5)}")  # 120
    print(f"   factorial(0) = {factorial(0)}")  # 1
    print(f"   factorial(3) = {factorial(3)}")  # 6
    
    # Test 2: Fibonacci
    print("\n2. FIBONACCI:")
    print(f"   fibonacci(0) = {fibonacci(0)}")  # 0
    print(f"   fibonacci(1) = {fibonacci(1)}")  # 1
    print(f"   fibonacci(5) = {fibonacci(5)}")  # 5
    print(f"   fibonacci(7) = {fibonacci(7)}")  # 13
    
    # Test 3: Potencia
    print("\n3. POTENCIA:")
    print(f"   potencia(2, 3) = {potencia(2, 3)}")  # 8
    print(f"   potencia(5, 0) = {potencia(5, 0)}")  # 1
    print(f"   potencia(3, 4) = {potencia(3, 4)}")  # 81
    
    # Test 4: Decimal a binario
    print("\n4. DECIMAL A BINARIO:")
    print(f"   decimal_a_binario(10) = {decimal_a_binario(10)}")  # "1010"
    print(f"   decimal_a_binario(5) = {decimal_a_binario(5)}")   # "101"
    print(f"   decimal_a_binario(15) = {decimal_a_binario(15)}") # "1111"
    print(f"   decimal_a_binario(0) = {decimal_a_binario(0)}")  # "0"
    
    # Test 5: Palíndromo
    print("\n5. PALÍNDROMO:")
    print(f"   es_palindromo('ana') = {es_palindromo('ana')}")  # True
    print(f"   es_palindromo('hola') = {es_palindromo('hola')}")  # False
    print(f"   es_palindromo('reconocer') = {es_palindromo('reconocer')}")  # True
    print(f"   es_palindromo('python') = {es_palindromo('python')}")  # False
    
    # Test 6: Suma de dígitos
    print("\n6. SUMA DE DÍGITOS:")
    print(f"   suma_digitos(1234) = {suma_digitos(1234)}")  # 10
    print(f"   suma_digitos(9) = {suma_digitos(9)}")  # 9
    print(f"   suma_digitos(305) = {suma_digitos(305)}")  # 8
    
    # Test 7: Contar bloques
    print("\n7. CONTAR BLOQUES:")
    print(f"   contar_bloques(1) = {contar_bloques(1)}")  # 1
    print(f"   contar_bloques(2) = {contar_bloques(2)}")  # 3
    print(f"   contar_bloques(4) = {contar_bloques(4)}")  # 10
    print(f"   contar_bloques(5) = {contar_bloques(5)}")  # 15
    
    # Test 8: Contar dígito
    print("\n8. CONTAR DÍGITO:")
    print(f"   contar_digito(12233421, 2) = {contar_digito(12233421, 2)}")  # 3
    print(f"   contar_digito(5555, 5) = {contar_digito(5555, 5)}")  # 4
    print(f"   contar_digito(123456, 7) = {contar_digito(123456, 7)}")  # 0
    print(f"   contar_digito(1001, 0) = {contar_digito(1001, 0)}")  # 2
    
    print("\n" + "="*60)
    print("TODAS LAS PRUEBAS COMPLETADAS")
    print("="*60)


if __name__ == "__main__":
    test_todas_las_funciones()

