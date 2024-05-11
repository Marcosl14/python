# Ejemplos de bucles en Python

# Ejemplo de bucle `for`
print("Ejemplo de bucle `for`:")
print(
    "El bucle `for` se utiliza para iterar sobre elementos de una secuencia (por ejemplo, listas o cadenas)."
)
print("En este ejemplo, iteramos sobre una lista de números e imprimimos cada uno.")
numeros = [10, 20, 30, 40, 50]
for numero in numeros:
    print(f"Número: {numero}")
print("---")  # Separador

# Ejemplo de `range()` con bucle `for`
print("Ejemplo de `range()` con bucle `for`:")
print("El rango `range()` se utiliza para generar una secuencia de números.")
print(
    "En este ejemplo, iteramos sobre un rango de 0 a 4 (exclusivo) e imprimimos cada número."
)
for i in range(5):
    print(f"Iteración: {i}")
print("---")  # Separador

print(
    "En este ejemplo, iteramos sobre un rango del 20 al 30 (exclusivo), saltando cada dos, e imprimimos cada número."
)
for i in range(20, 30, 2):
    print(f"Iteración: {i}")
print("---")  # Separador

# Ejemplo de bucle `for` con cadena de texto
print("Ejemplo de bucle `for` con cadena de texto:")
print(
    "En este ejemplo, iteramos sobre cada carácter de una cadena de texto e imprimimos cada uno."
)
cadena = "Python"
for letra in cadena:
    print(f"Letra: {letra}")
print("---")  # Separador

# Ejemplo de `enumerate()` con bucle `for`
print("Ejemplo de `enumerate()` con bucle `for`:")
print(
    "El método `enumerate()` devuelve un iterador que produce tuplas con índices y valores de una secuencia."
)
print(
    "En este ejemplo, iteramos sobre una lista de nombres con `enumerate()` para obtener el índice y el valor de cada elemento."
)
nombres = ["Juan", "Ana", "Pedro", "María"]
for indice, nombre in enumerate(nombres):
    print(f"Índice: {indice}, Nombre: {nombre}")
print("---")  # Separador

# Ejemplo de `break` y `continue` en bucles
print("Ejemplo de `break` y `continue` en bucles:")
print(
    "`break` interrumpe el bucle, mientras que `continue` salta a la siguiente iteración."
)

# Usamos `break` para detener un bucle `for` cuando encontramos un número específico.
print(
    "Usamos `break` para detener un bucle `for` cuando encontramos un número específico."
)
numeros = [2, 4, 6, 7, 8, 10]
numero_objetivo = 7
for numero in numeros:
    if numero == numero_objetivo:
        print(f"Número {numero_objetivo} encontrado. Interrumpiendo el bucle.")
        break  # Interrumpir el bucle
    print(f"Viendo el número: {numero}")
print("---")  # Separador

# Usamos `continue` para saltar una iteración en un bucle `for` cuando encontramos un número específico.
print(
    "Usamos `continue` para saltar una iteración en un bucle `for` cuando encontramos un número específico."
)
numeros = [2, 4, 6, 7, 8, 10]
numero_a_saltar = 7
for numero in numeros:
    if numero == numero_a_saltar:
        print(f"Número {numero_a_saltar} encontrado. Saltando esta iteración.")
        continue  # Saltar esta iteración
    print(f"Viendo el número: {numero}")
print("---")  # Separador

# Usamos el bubcle for, enlazando listas
print(
    "Usamos el bucle for, enlazando listas."
)
nombres = ['Ana', 'Hugo', 'Valeria']
edades = [18,25,20]
ciudades = ['Lima', 'Madrid', 'Mexico']
for nombre, edad, ciudad in list(zip(nombres, edades, ciudades)):
    print(f"{nombre}, tiene {edad} y vive en {ciudad}")
print("---")  # Separador

# Ejemplos adicionales con diccionarios y listas anidadas
print("Ejemplos adicionales con diccionarios y listas anidadas:")
print("Iterar sobre las claves de un diccionario:")
diccionario = {"key1": "value1", "key2": "value2", "key3": "value3"}
for key in diccionario:
    print(key)
print("---")  # Separador

print("Iterar sobre las claves y valores de un diccionario:")
for key_value in diccionario.items():
    print(key_value)
print("---")  # Separador

print("Iterar sobre las claves y valores de un diccionario (separados):")
for a, b in diccionario.items():
    print(a, b)
print("---")  # Separador

print("Iterar solo sobre los valores de un diccionario:")
for value in diccionario.values():
    print(value)
print("---")  # Separador

print("Iterar sobre una lista anidada:")
lista_anidada = [[1, "a"], [2, "b"], [3, "c"]]
for item in lista_anidada:
    print(item)
print("---")  # Separador

print("Iterar sobre una lista anidada (separando los elementos):")
for a, b in lista_anidada:
    print(a, b)
print("---")  # Separador

# Ejemplo de bucle `while`
print("Ejemplo de bucle `while`:")
print(
    "El bucle `while` ejecuta un bloque de código mientras una condición sea verdadera."
)
print("En este ejemplo, usamos un bucle `while` para contar desde 0 hasta 4.")
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementamos el contador
else:
    print("Final del bucle while")
print("---")  # Separador

print(
    "En este ejemplo, usamos un bucle `while` para contar desde 0 hasta 4 (uso del continue y del break)."
)
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    if contador == 3:
        print("Encontramos el número 3. Rompiendo el bucle.")
        break  # Interrumpir el bucle si encontramos el número 3
    elif contador == 2:
        print("Encontramos el número 2. Saltando esta iteración.")
        contador += 1  # Incrementamos el contador
        continue  # Saltar esta iteración si encontramos el número 2
    contador += 1  # Incrementamos el contador
    print("Continuando con la siguiente iteración.")
else:
    print("Final del bucle while")  # -> nunca pasa por aca. Porque rompe antes (break)
print("---")  # Separador
