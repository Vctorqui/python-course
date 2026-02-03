
# Son dos palabras reservadas que va a buscar pertenencia (un grupo, item a una lista, etc)
# in
# not in


# NOTA: range() me trae un listado, se empieza a contar desde 0, Entonces seria desde el 0 hasta el 9, si quiesieramos el 10, debemos colocar 11

# print(10 in range(1,10)) 

fruits = ['Manzana', 'Banana', 'Fresa']
print('Fresa' in fruits)    #True
print("Uva" not in fruits)  #True
print('Mango' in fruits)    #False
print("Fresa" not in fruits)  #False

sencente = 'Soy programador en JS, PHP...'
print('Python' in sencente)