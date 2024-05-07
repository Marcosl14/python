# Ejemplos de bucles en Python

# Ejemplo de bucle `while`
# El bucle `while` ejecuta un bloque de código mientras una condición sea verdadera.
# En este ejemplo, usamos un bucle `while` para contar desde 0 hasta 4.
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementamos el contador

# Ejemplo de bucle `for`
# El bucle `for` se utiliza para iterar sobre elementos de una secuencia (por ejemplo, listas o cadenas).
# En este ejemplo, iteramos sobre una lista de números e imprimimos cada uno.
numeros = [10, 20, 30, 40, 50]
for numero in numeros:
    print(f"Número: {numero}")

# Ejemplo de `range()` con bucle `for`
# El rango `range()` se utiliza para generar una secuencia de números.
# En este ejemplo, iteramos sobre un rango de 0 a 4 (exclusivo) e imprimimos cada número.
for i in range(5):
    print(f"Iteración: {i}")

# Ejemplo de bucle `for` con cadena de texto
# En este ejemplo, iteramos sobre cada carácter de una cadena de texto e imprimimos cada uno.
cadena = "Python"
for letra in cadena:
    print(f"Letra: {letra}")

# Ejemplo de `enumerate()` con bucle `for`
# El método `enumerate()` devuelve un iterador que produce tuplas con índices y valores de una secuencia.
# En este ejemplo, iteramos sobre una lista de nombres con `enumerate()` para obtener el índice y el valor de cada elemento.
nombres = ["Juan", "Ana", "Pedro", "María"]
for indice, nombre in enumerate(nombres):
    print(f"Índice: {indice}, Nombre: {nombre}")

# Ejemplo de `break` y `continue` en bucles
# `break` interrumpe el bucle, mientras que `continue` salta a la siguiente iteración.

# Usamos `break` para detener un bucle `for` cuando encontramos un número específico.
numeros = [2, 4, 6, 7, 8, 10]
numero_objetivo = 7
for numero in numeros:
    if numero == numero_objetivo:
        print(f"Número {numero_objetivo} encontrado. Interrumpiendo el bucle.")
        break  # Interrumpir el bucle
    print(f"Viendo el número: {numero}")

# Usamos `continue` para saltar una iteración en un bucle `for` cuando encontramos un número específico.
numeros = [2, 4, 6, 7, 8, 10]
numero_a_saltar = 7
for numero in numeros:
    if numero == numero_a_saltar:
        print(f"Número {numero_a_saltar} encontrado. Saltando esta iteración.")
        continue  # Saltar esta iteración
    print(f"Viendo el número: {numero}")
