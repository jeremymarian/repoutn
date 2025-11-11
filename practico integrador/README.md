# Sistema de Gestión de Datos de Países

## Descripción del Programa

Este es un sistema de gestión de datos de países desarrollado en Python como Trabajo Práctico Integrador (TPI) para la materia Programación 1 de la Tecnicatura Universitaria en Programación a Distancia de la UTN.

El programa permite gestionar información sobre países almacenada en un archivo CSV, ofreciendo funcionalidades para:
- Agregar y actualizar datos de países
- Buscar países por nombre
- Filtrar países por diferentes criterios
- Ordenar países por diferentes atributos
- Calcular estadísticas sobre los datos

## Características Principales

### Estructuras de Datos Utilizadas
- **Listas**: Para almacenar la colección de países
- **Diccionarios**: Para representar cada país individual con sus atributos

### Funcionalidades Implementadas
1. **Agregar país**: Permite agregar nuevos países con validación de campos no vacíos
2. **Actualizar país**: Actualiza población y superficie de países existentes
3. **Buscar país**: Búsqueda por nombre con coincidencia parcial
4. **Filtros**:
   - Por continente
   - Por rango de población
   - Por rango de superficie
5. **Ordenamientos**:
   - Por nombre (ascendente)
   - Por población (ascendente/descendente)
   - Por superficie (ascendente/descendente)
6. **Estadísticas**:
   - País con mayor y menor población
   - Promedio de población
   - Promedio de superficie
   - Cantidad de países por continente

## Instrucciones de Uso

### Requisitos Previos
- Python 3.x instalado en el sistema
- Archivo `paises.csv` en el mismo directorio que el programa (se crea automáticamente si no existe)

### Ejecución del Programa

1. Abrir una terminal/consola en el directorio del proyecto
2. Ejecutar el siguiente comando:
```bash
python gestion_paises.py
```

3. El programa cargará automáticamente los países desde `paises.csv`
4. Se mostrará un menú con las opciones disponibles
5. Seleccionar la opción deseada ingresando el número correspondiente

### Formato del Archivo CSV

El archivo CSV debe tener el siguiente formato:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Brasil,213993437,8515767,América
```

**Campos requeridos:**
- `nombre`: Nombre del país (texto)
- `poblacion`: Población total (número entero)
- `superficie`: Superficie en km² (número entero)
- `continente`: Continente al que pertenece (texto)

## Ejemplos de Uso

### Ejemplo 1: Agregar un País

```
Seleccione una opción: 1

--- AGREGAR PAÍS ---
Ingrese el nombre del país: Chile
Ingrese la población: 19120000
Ingrese la superficie en km²: 756102
Ingrese el continente: América

✓ País 'Chile' agregado correctamente.
✓ Datos guardados en 'paises.csv'.
```

### Ejemplo 2: Buscar un País

```
Seleccione una opción: 3

--- BUSCAR PAÍS ---
Ingrese el nombre del país a buscar: Arg

Se encontraron 1 país(es):
----------------------------------------------------------------------
Nombre: Argentina
Población: 45,376,763
Superficie: 2,780,400 km²
Continente: América
----------------------------------------------------------------------
```

### Ejemplo 3: Filtrar por Continente

```
Seleccione una opción: 4

--- FILTRAR POR CONTINENTE ---
Ingrese el continente: América

Países en 'América' (4 encontrados):

================================================================================
Nombre                    Población      Superficie (km²)     Continente     
================================================================================
Argentina                       45,376,763         2,780,400 América         
Brasil                         213,993,437         8,515,767 América         
Estados Unidos                 331,900,000         9,833,517 América         
México                         126,700,000         1,964,375 América         
================================================================================
```

### Ejemplo 4: Ordenar por Población

```
Seleccione una opción: 7

--- ORDENAMIENTO ---
1. Ordenar por nombre (ascendente)
2. Ordenar por población (ascendente)
3. Ordenar por población (descendente)
4. Ordenar por superficie (ascendente)
5. Ordenar por superficie (descendente)
6. Cancelar

Seleccione una opción: 3

Países ordenados por población (descendente):

================================================================================
Nombre                    Población      Superficie (km²)     Continente     
================================================================================
China                     1,400,000,000         9,596,961 Asia              
India                     1,380,000,000         3,287,263 Asia              
Estados Unidos              331,900,000         9,833,517 América          
...
```

### Ejemplo 5: Mostrar Estadísticas

```
Seleccione una opción: 8

======================================================================
ESTADÍSTICAS GENERALES
======================================================================

--- ESTADÍSTICAS DE POBLACIÓN ---
País con mayor población: China (1,400,000,000 habitantes)
País con menor población: Australia (25,690,000 habitantes)

--- PROMEDIO DE POBLACIÓN ---
Promedio de población: 261,183,467.33 habitantes

--- PROMEDIO DE SUPERFICIE ---
Promedio de superficie: 4,234,567.80 km²

--- CANTIDAD DE PAÍSES POR CONTINENTE ---
África: 1 país(es)
América: 4 país(es)
Asia: 4 país(es)
Europa: 4 país(es)
Oceanía: 1 país(es)
======================================================================
```

## Validaciones Implementadas

El programa incluye las siguientes validaciones:

1. **Campos no vacíos**: No se permiten campos vacíos al agregar países
2. **Números positivos**: La población y superficie deben ser números enteros positivos
3. **Rangos válidos**: En filtros por rango, el mínimo no puede ser mayor que el máximo
4. **Manejo de errores**: Control de errores al leer/escribir archivos CSV
5. **Países duplicados**: No se permite agregar países con el mismo nombre

## Estructura del Código

El programa está modularizado en las siguientes funciones principales:

- `cargar_paises_desde_csv()`: Carga países desde archivo CSV
- `guardar_paises_en_csv()`: Guarda países en archivo CSV
- `agregar_pais()`: Agrega un nuevo país
- `actualizar_pais()`: Actualiza datos de un país
- `buscar_pais()`: Busca países por nombre
- `filtrar_por_continente()`: Filtra por continente
- `filtrar_por_rango_poblacion()`: Filtra por rango de población
- `filtrar_por_rango_superficie()`: Filtra por rango de superficie
- `ordenar_por_nombre()`: Ordena por nombre
- `ordenar_por_poblacion()`: Ordena por población
- `ordenar_por_superficie()`: Ordena por superficie
- `mostrar_estadisticas()`: Calcula y muestra estadísticas
- `main()`: Función principal que ejecuta el programa

## Participación de los Integrantes

**[COMPLETAR CON LOS NOMBRES Y APELLIDOS DE LOS INTEGRANTES]**

- **Integrante 1**: [Nombre y Apellido]
  - Responsabilidades: [Describir tareas realizadas]
  
- **Integrante 2**: [Nombre y Apellido]
  - Responsabilidades: [Describir tareas realizadas]

## Archivos del Proyecto

- `gestion_paises.py`: Código fuente principal del programa
- `paises.csv`: Archivo CSV con los datos de países
- `README.md`: Este archivo con la documentación
- `SCRIPT_VIDEO_15MIN.md`: Script para el video tutorial

## Tecnologías Utilizadas

- **Lenguaje**: Python 3.x
- **Módulos estándar**: `csv`, `os`
- **Estructuras de datos**: Listas, Diccionarios
- **Paradigma**: Programación estructurada, modular

## Licencia

Este proyecto fue desarrollado como trabajo académico para la UTN.

## Contacto

Para consultas o sugerencias sobre este proyecto, contactar a los integrantes del equipo.

---

**Última actualización**: [Fecha]


