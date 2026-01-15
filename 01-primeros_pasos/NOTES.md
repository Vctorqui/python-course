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
Podemos acceder a caracteres específicos o rangos (slices) de una cadena.
La sintaxis general es `[start:stop:stepover]`.

- `start`: Índice donde comienza (incluido). Si se omite, es 0.
- `stop`: Índice donde termina (NO incluido). Si se omite, va hasta el final.
- `stepover`: Saltos entre caracteres. Si se omite, es 1.

```python
name = "Victor"
print(name[0])      # 'V' (Primer caracter)
print(name[-1])     # 'r' (Último caracter)

# [start:stop] -> El stop no se incluye
print(name[0:3])    # 'Vic' (Indices 0, 1, 2)

# [start:stop:stepover] -> Salta índices
print(name[0:3:2])  # 'Vc' (Toma 1, salta 1)

# [::] -> Al omitir start y stop, toma toda la cadena
# El stepover -1 invierte la cadena (de atrás hacia adelante)
print(name[::-1])   # 'rotciV'
```

### 6. Inmutabilidad
Algunos tipos de datos no pueden modificarse una vez creados, como los `strings` o las `tuplas`.

```python
name = 'Victor'
# name[0] = 'S' # Error! No se puede asignar ítems en un string

name = 'Samar'  # Correcto: Estamos creando un nuevo string y reasignando la variable
```

### 7. Conversiones de Tipos de Datos (Casting)
Es posible convertir entre diferentes tipos de datos usando funciones como `int()`, `float()`, `str()`.

**Errores comunes:**
No se pueden operar tipos incompatibles directamente.
```python
# value = 26 + 'Hola' # Error: TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

**Conversión correcta:**
```python
value = 26
# Convertir entero a string para concatenar
texto = str(value) + ' Hola' 
print(texto) # "26 Hola"

# Convertir string a entero
numero = int('26')
print(type(numero)) # <class 'int'>

# Convertir string a float
dec = float('26.5')
print(type(dec)) # <class 'float'>
```

### 8. Operaciones Matemáticas y Funciones
Python soporta todas las operaciones aritméticas básicas y cuenta con funciones integradas para cálculos.

```python
# Operadores Aritméticos
print(2 + 2)    # Suma: 4
print(4 - 2)    # Resta: 2
print(3 * 3)    # Multiplicación: 9
print(2 / 4)    # División: 0.5 (Siempre devuelve float)
print(2 ** 3)   # Potencia: 8
print(5 // 2)   # División Entera: 2 (Descarta decimales)
print(5 % 2)    # Módulo: 1 (Resto de la división)

# Funciones Útiles
print(round(3.6)) # Redondeo: 4
print(abs(-5))    # Valor Absoluto: 5
```

### 9. Funciones Incorporadas y Métodos
Python incluye muchas funciones "built-in" listas para usar.
Para ver la lista completa, consulta la [Documentación Oficial de Python](https://docs.python.org/3/library/functions.html).

Ejemplos comunes:
```python
print("Hola")       # Imprimir en consola
type(42)            # Ver tipo de dato
str(42)             # Convertir a texto
```

**Métodos de Strings:**
Los objetos en Python tienen métodos asociados.
```python
message = "Es un buen programador"
print(message.upper()) # Mayúsculas: 'ES UN BUEN PROGRAMADOR'
print(message.replace("buen", "excelente")) # Reemplazar texto
```

### 10. Entrada de Datos (Input)
Podemos interactuar con el usuario usando `input()`.
**IMPORTANTE**: `input()` siempre devuelve un dato de tipo **string (str)**. Si necesitas un número, debes convertirlo explícitamente.

```python
name = input('¿Cuál es tu nombre? ') 
age = input('¿Cuántos años tienes? ')

# Si queremos operar con la edad, debemos convertirla
age_number = int(age)
```

### 11. Mini Proyecto: Registro de Usuario
Hora de practicar😎. Intenta resolver el siguiente ejercicio:

**Enunciado:**
Crea un script que reciba de forma dinámica (por consola):
1. Nombre
2. Año de nacimiento
3. Correo
4. Contraseña

y la respuesta se vea de la siguiente manera:

```python
"""
    Nombre: Tu nombre
    Email: Tu correo
    Tendrás n años en 2050
    Tu constraseña es: *****
"""
```

El script debe calcular tu edad en el año 2050, encriptar la contraseña (mostrando asteriscos `*` según su longitud) y mostrar un mensaje formateado con todos los datos.

Si tienes dudas o quieres ver la solución, revisa el archivo: `13-mini_project.py`.

---
