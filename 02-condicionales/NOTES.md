# ¿Qué es una condicional?

Es una forma en la que una computadora puede tomar decisiones.

## Ejemplo de toma de decisiones en la _vida cotidiana_:

- 'Si está lloviendo, llevo un paraguas.'
- 'Si hace frio, me pongo un suéter.'
- 'Si no hace frio ni llueve, salgo sin nada especial.'

¿Hay café?

![alt text](./images/image.png)

¿Puedo conducir?

![alt text](./images/image-1.png)

## Ejemplo de toma de decisiones en la _programación_:

- 'Si el usuario está autenticado, mostrar el dashboard.'
- 'Si el usuario no está autenticado, redirigir al login.'
- 'Si el usuario es admin, mostrar el dashboard de admin.'

En Python, las condicionales se implementan con la sentencia `if`.

## Sentencia `if` y `else`

Se utiliza para ejecutar un bloque de código si una condición es verdadera, y otro bloque si es falsa.

```python
is_old = True

if is_old:
    print('Puedes manejar')
else:
    print('Espero que cumplas 18')
```

## Sentencia `elif`

Se utiliza cuando queremos evaluar múltiples condiciones de forma secuencial.

```python
is_old = False
is_licenced = True

if is_old:
    print('Tienes edad para manejar')
elif is_licenced:
    print('Puedes manejar con tu licencia en la ciudad.')
else:
    print('Espera a cumplir la mayoria de edad o trámita tu licencia')
```

## Operador Ternario (If en una sola línea)

Es una forma concisa de escribir un `if-else`.

**Sintaxis:** `valor_si_true if condicion else valor_si_false`

```python
is_student = True
get_license = 'Licencia de estudiante' if is_student else 'Licencia normal'
```

> [!NOTE]
> Es muy similar al operador ternario en JavaScript (`condición ? true : false`), pero con una sintaxis más natural al lenguaje inglés.

## Valores Truthy y Falsey

En Python, no solo los booleanos `True` y `False` se evalúan en una condicional. Los valores que no son estrictamente booleanos pueden ser "veraces" (Truthy) o "falsos" (Falsey).

### Truthy (Valores que se evalúan como `True`)

Cualquier valor que no sea "vacío" o cero.

- Números diferentes a 0 (ej. `1`, `-1`, `123`, `1j`).
- Strings no vacíos (ej. `'hola'`).
- Colecciones no vacías (ej. `[1,2]`, `(3,4)`, `{5,6}`).

### Falsey (Valores que se evalúan como `False`)

- `False`
- `None`
- El número `0` y `0j`.
- Strings vacíos `''`.
- Colecciones vacías `[]`, `()`, `{}`.

```python
# Ejemplo
if [1,2,3]: # Esto es Truthy
    print("La lista no está vacía")

if '': # Esto es Falsey
    print("Esto no se imprimirá")
```
