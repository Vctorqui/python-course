# Tipos de datos
# Strings (Cadenas de texto)
name = "Victor"

# int (Números enteros)
number = 2000
age = 27
gatos = 1

# float (Números decimales)
height = 1.75
weight = 70.5
temperature = 36.6

# Bool o booleanos (True o False)
is_single = False
has_car = True
has_visa = True

# Datos especiales 

# Arrays o listas
lista = [1, 2, 3, 4, 5]
names = ["Victor", "Ana", "Luis"]

# Tuplas (inmutables)
tupla = (10, 20, 30)

# Set 
set_variable = {1, 2, 3, 4, 5}

# Diccionarios (key-value pairs)
spanish_to_english = {
    "hola": "hello",
    "adiós": "goodbye",
    "gracias": "thank you"
}


personal_info = {
    "name": "Victor",
    "age": 27,
    "is_single": False
}



# Para saber el tipo de dato usamos la función type()

# IMPORTANTE: Todo en Python es un objeto, incluso los tipos de datos. La ventaja de esto es que todos los tipos de datos tienen métodos asociados que podemos usar para manipularlos.

print(type(name.upper()))  # <class 'str'>
print(type(number))  # <class 'int'>