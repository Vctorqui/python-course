
# Truthy -> son valores verdaderos que nos van a ayudar que en las condicioanles podamos pasar cosas. Mientras tengas valores diferentes a 0 o a la 'nada' serán verdaderos. 
bool(True) # True
bool(1) # True -> cualquier numero diferente a 0
bool(-1) # True
bool(123) # True
bool(1j) # True
bool('hola') # True
bool([1,2,3]) # True
bool((1,2,4)) # True
bool({1,2,3,4}) # True

# Falsey -> son valores falsos.
bool(False) # False 
bool(0) # False
bool(0j) # False
bool('') # False
bool([]) # False
bool(()) # False
bool({}) # False
bool(None) # False