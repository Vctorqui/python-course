
# Registro
# Recibe de forma dinámica el nombre, año de nacimiento, correo y constraseña de un usuario.

"""
Nombre: Victor
Email: victor@gmail.com
Tendrás 55 años en 2050
Tu constraseña es: *****
"""

input_name = input('¿Cuál es tu nombre? ')
input_year_of_birth = input('¿En qué año naciste? ')
input_email = input('¿Cuál es tu correo? ')
input_password = input('¿Cuál es tu clave? ')


age_in_2025 = 2050 - int(input_year_of_birth) 

password_lenght = len(input_password)
password_encripted = '*' * password_lenght

full_message = f''''
    Nombre: {input_name} 
    Email: {input_email} 
    Tendrás {age_in_2025} años en el 2050
    Tu constraseña es: {password_encripted}
'''

print(full_message)
