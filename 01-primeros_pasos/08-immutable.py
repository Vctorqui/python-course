
# ¿Qué es inmutabilidad? Signfica que algo no puede ser cambiado

nombre = 'Victor'
nombre = 'Samar'  # Se puede cambiar el valor, se sustituyó la referencia completo a otro valor en memoria.
print(nombre)

# Las cadenas de texto (strings) son inmutables
name = 'Victor'
name[0] = 'S' # Esto generará un error porque las strings son inmutables (TypeError: 'str' object does not support item assignment)

print(name)
