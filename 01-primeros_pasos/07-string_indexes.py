
name = "Victor"
print(name) # Victor

print(name[0]) # V

# Cómo obtener la ultima letra
print(name[-1]) # r

# [start:stop] -> no incluye el indice el stop, es decir, no lo toma en cuenta. 
# Victor
# Vic
print(name[0:3]) # Vic

# [start:stop:stepover] -> el stepover salta indices, por ejemplo, si es 2, toma una letra y salta la siguiente. Por defecto es 1.
print(name[0:3:2]) # Vc


# Cómo puedo poner mi nombre al revés?
name_girl = 'Samar'

name_reverse_girl = name_girl[::-1]

print(name_reverse_girl)
