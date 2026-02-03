
# Nos va a ayudar a Evaluar condiciones

# and -> evalua si dos condiciones o más son verdaderas (Todos los valores sean verdaderos)
print (True and True) # True
print (True and False) # False
print (False and True) # False
print (False and False) # False

# or -> al menos un valor debe ser True
print (True and True) # True
print (True and False) # True
print (False and True) # True
print (False and False) # False


# nor (negar)
print (not True) # False
print (not False) # True


# Ejemplo and

age = 25
licensed = True

if age >= 18 and licensed: 
    print('Puedes conducir')


# Ejemplo or
is_student = False
membership = True

if is_student or membership:
    print('Obtienes un descuento especial')
    
# Ejemplo not
is_admmin = False

if not is_admmin:
    print('Acceso denegado')
