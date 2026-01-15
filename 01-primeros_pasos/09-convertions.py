
value = 26 + 'Hola' # Error: no se puede sumar int + str
type_value = type(value)
print(value) # 26
print(type_value) # <class 'int'>


# Convertir un int a string
type_value = str(value) + 'Hola'
print(value) # 26
print(type_value) # <class 'str'>


# Convertir un string a int
value = int('26')
type_value = type(value)
print(value) # 26
print(type_value) # <class 'int'>

# Convertir string a float
value = float('hola') # Error: ValueError: could not convert string to float: 'hola'
value = float('26.5')  # Esto no esta limitado a string, puede ser int a float o float a int
type_value = type(value)
print(value) # 26
print(type_value) # <class 'float'>