# Módulo 1: Primeros Pasos en Python

En esta sección aprenderás los fundamentos esenciales para comenzar a programar en Python, desde tu primer "Hola Mundo" hasta la manipulación básica de datos.

## Introducción a Python

### ¿Qué es Python?
Es un lenguaje de programación interpretado de alto nivel creado por Guido Van Rossum en 1991.

Sus principales características son:
- **Sencillo**: Se parece al lenguaje humano (escribiendo en inglés).
- **Versátil**: Uso en desarrollo web, ciencia de datos, automatización, IA, etc.
- **Comunidad activa**: Gran soporte y librerías disponibles.
- **Multiplataforma**: Funciona en Windows, Mac, Linux, etc.

### Conceptos Clave
- **Alto nivel**: Lenguajes cercanos al humano (ej. Python, Java).
- **Bajo nivel**: Lenguajes cercanos a la máquina (ej. Assembly).
- **Lenguaje Interpretado**: Se ejecuta línea por línea mediante un intérprete, sin necesidad de compilación previa.
    - *Ventajas*: Pruebas rápidas, flexibilidad, legibilidad.
    - *Desventajas*: Velocidad (comparado con compilados), distribución del código fuente.

---

## Contenido del Curso

### 1. Hola Mundo
El primer programa en cualquier lenguaje. En Python usamos la función `print()` para mostrar mensajes en consola.
```python
print('Hola mundo bro')
```

### 2. Comentarios
Los comentarios son ignorados por el intérprete y sirven para documentar el código.
```python
# Este es un comentario de una sola línea

"""
Este es un comentario
multi-línea usando comillas dobles
"""

'''
Este es otro comentario
multi-línea usando comillas simples
'''
```

### 3. Variables
Las variables son espacios en memoria para guardar datos. Python es de tipado dinámico (no hace falta declarar el tipo).

Recomendaciones (PEP8):
- Usar `snake_case` para variables.
- Usar MAYÚSCULAS para constantes.

```python
name = "Victor"       # Variable string
PI = 3.1416           # Constante
nombre_completo = "Victor Quinones" # snake_case
```

### 4. Tipos de Datos
Python tiene varios tipos de datos nativos. Todo en Python es un objeto.

**Primitivos:**
- `str`: Cadenas de texto ("Hola").
- `int`: Números enteros (2000).
- `float`: Números decimales (1.75).
- `bool`: Booleanos (True, False).

**Estructuras de Datos:**
- `list`: Ordenada y mutable `[1, 2, 3]`.
- `tuple`: Ordenada e inmutable `(10, 20)`.
- `set`: Desordenada y sin duplicados `{1, 2, 3}`.
- `dict`: Pares clave-valor `{"key": "value"}`.

Para saber el tipo de un dato usamos `type()`:
```python
print(type("Texto"))  # <class 'str'>
```

### 5. Strings (Cadenas de Texto)
Manejo de texto en Python.

**Concatenación y Formato:**
Evitar concatenar con `+` si son muchas variables. Usar **f-strings** (Python 3.6+).
```python
name = 'Víctor'
age = 27
# f-string interpolación
message = f'{name} tiene {age} años.' 
print(message)
```

**Índices y Slicing:**
Podemos acceder a caracteres específicos o rangos.
```python
name = "Victor"
print(name[0])      # 'V' (Primer caracter)
print(name[-1])     # 'r' (Último caracter)
print(name[0:3])    # 'Vic' (Desde índice 0 hasta antes del 3)
print(name[::-1])   # 'rotciV' (String invertido)
```

### 6. Inmutabilidad
Algunos tipos de datos no pueden modificarse una vez creados, como los `strings` o las `tuplas`.

```python
name = 'Victor'
# name[0] = 'S' # Error! No se puede asignar ítems en un string

name = 'Samar'  # Correcto: Estamos creando un nuevo string y reasignando la variable
```

---
