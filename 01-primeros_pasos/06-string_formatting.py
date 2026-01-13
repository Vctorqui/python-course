
# Concatenación de strings
name = 'Víctor'
last_name = 'Quinones'
age = 27

# full_name = name + " " + last_name  # -> eso no esta bien, no es una buena práctica.

full_name = f'{name} {last_name}' # Usando f-strings (formatted strings)
message = f'{full_name} tiene {age} años.'


print(full_name)  # Víctor Quinones
print(message)    # Víctor Quinones tiene 27 años.