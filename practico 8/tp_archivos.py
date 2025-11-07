"""
TP - Manejo de Archivos de Texto
Programación I
"""

# ============================================
# ACTIVIDAD 1: Ya está creado productos.txt
# ============================================

# ============================================
# ACTIVIDAD 2, 3, 4, 5, 6: Programa completo
# ============================================

def cargar_productos_desde_archivo(nombre_archivo):
    """
    Actividad 4: Carga productos desde el archivo y los convierte
    en una lista de diccionarios.
    """
    productos = []
    
    # Usar 'with open()' es una buena práctica (cierra automáticamente)
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # .strip() elimina espacios y saltos de línea
            linea_limpia = linea.strip()
            
            # Si la línea está vacía, la saltamos
            if len(linea_limpia) == 0:
                continue
            
            # .split(",") separa la línea por comas
            datos = linea_limpia.split(",")
            
            # Verificar que tenga 3 elementos
            if len(datos) == 3:
                producto = {
                    "nombre": datos[0],
                    "precio": float(datos[1]),  # Convertir precio a float
                    "cantidad": int(datos[2])   # Convertir cantidad a int
                }
                productos.append(producto)
    
    return productos


def mostrar_productos(productos):
    """
    Actividad 2: Muestra los productos en el formato solicitado.
    """
    print("\n=== LISTA DE PRODUCTOS ===\n")
    
    if len(productos) == 0:
        print("No hay productos en el archivo.")
        return
    
    for producto in productos:
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")


def agregar_producto_desde_teclado(productos):
    """
    Actividad 3: Permite agregar un nuevo producto desde el teclado.
    """
    print("\n=== AGREGAR NUEVO PRODUCTO ===\n")
    
    nombre = input("Ingrese el nombre del producto: ")
    
    # Validar que el nombre no esté vacío
    if len(nombre.strip()) == 0:
        print("Error: El nombre no puede estar vacío.")
        return False
    
    # Pedir precio y validar
    precio_str = input("Ingrese el precio del producto: ")
    try:
        precio = float(precio_str)
        if precio < 0:
            print("Error: El precio debe ser mayor o igual a cero.")
            return False
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")
        return False
    
    # Pedir cantidad y validar
    cantidad_str = input("Ingrese la cantidad del producto: ")
    try:
        cantidad = int(cantidad_str)
        if cantidad < 0:
            print("Error: La cantidad debe ser mayor o igual a cero.")
            return False
    except ValueError:
        print("Error: Debe ingresar un número entero válido para la cantidad.")
        return False
    
    # Crear el nuevo producto
    nuevo_producto = {
        "nombre": nombre.strip(),
        "precio": precio,
        "cantidad": cantidad
    }
    
    # Agregar a la lista
    productos.append(nuevo_producto)
    print(f"\nProducto '{nombre}' agregado correctamente.")
    return True


def buscar_producto_por_nombre(productos):
    """
    Actividad 5: Busca un producto por nombre y muestra sus datos.
    """
    print("\n=== BUSCAR PRODUCTO ===\n")
    
    nombre_buscado = input("Ingrese el nombre del producto a buscar: ")
    nombre_buscado = nombre_buscado.strip()
    
    if len(nombre_buscado) == 0:
        print("Error: Debe ingresar un nombre.")
        return
    
    # Buscar en la lista
    encontrado = False
    for producto in productos:
        # Comparación insensible a mayúsculas/minúsculas
        if producto["nombre"].lower() == nombre_buscado.lower():
            print(f"\n✓ Producto encontrado:")
            print(f"  Nombre: {producto['nombre']}")
            print(f"  Precio: ${producto['precio']}")
            print(f"  Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"\n✗ Error: No se encontró el producto '{nombre_buscado}'.")


def guardar_productos_en_archivo(productos, nombre_archivo):
    """
    Actividad 6: Guarda todos los productos actualizados en el archivo.
    Sobrescribe el archivo completo.
    """
    # Modo 'w' sobrescribe el archivo completo
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for producto in productos:
            # Escribir en formato: nombre,precio,cantidad
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    
    print(f"\n✓ Productos guardados correctamente en '{nombre_archivo}'.")


def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n" + "="*50)
    print("   GESTIÓN DE PRODUCTOS")
    print("="*50)
    print("1. Mostrar todos los productos")
    print("2. Agregar nuevo producto")
    print("3. Buscar producto por nombre")
    print("4. Guardar y salir")
    print("="*50)


def main():
    """
    Función principal que coordina todas las actividades.
    """
    nombre_archivo = "productos.txt"
    
    # Cargar productos desde el archivo (Actividad 4)
    print("Cargando productos desde el archivo...")
    productos = cargar_productos_desde_archivo(nombre_archivo)
    print(f"✓ {len(productos)} productos cargados.")
    
    # Mostrar productos iniciales (Actividad 2)
    mostrar_productos(productos)
    
    # Menú interactivo
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            mostrar_productos(productos)
        
        elif opcion == "2":
            if agregar_producto_desde_teclado(productos):
                # Mostrar productos actualizados
                mostrar_productos(productos)
        
        elif opcion == "3":
            buscar_producto_por_nombre(productos)
        
        elif opcion == "4":
            # Guardar todos los productos antes de salir (Actividad 6)
            guardar_productos_en_archivo(productos, nombre_archivo)
            print("\n¡Hasta luego!")
            continuar = False
        
        else:
            print("\nError: Opción inválida. Seleccione 1, 2, 3 o 4.")


if __name__ == "__main__":
    main()

