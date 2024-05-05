# las tuplas son inmutables, almacenan menos espacio en memoria que las listas

# Método count(): Retorna el número de veces que un elemento aparece en la tupla.
tupla_1 = (1, 2, 3, 2, 4)
conteo = tupla_1.count(2)
print("count():", conteo)  # Salida: 2

# Método index(): Retorna la primera posición de un elemento específico.
tupla_2 = (1, 2, 3, 4, 5)
indice = tupla_2.index(3)
print("index():", indice)  # Salida: 2

# Desempaquetado de tupla
tupla_3 = (1, 2, 3)
a, b, c = tupla_3
print("Desempaquetado:", a, b, c)  # Salida: 1 2 3

# Convertir tupla en lista
tupla_4 = (1, 2, 3)
lista_4 = list(tupla_4)
print("Convertir a lista:", lista_4)  # Salida: [1, 2, 3]

# Longitud de la tupla
tupla_5 = (1, 2, 3, 4)
longitud = len(tupla_5)
print("Longitud de la tupla:", longitud)  # Salida: 4

# Concatenar tuplas
tupla_6 = (1, 2)
tupla_7 = (3, 4)
tupla_concatenada = tupla_6 + tupla_7
print("Concatenar tuplas:", tupla_concatenada)  # Salida: (1, 2, 3, 4)

# Multiplicar tuplas
tupla_8 = (1, 2)
tupla_multiplicada = tupla_8 * 3
print("Multiplicar tuplas:", tupla_multiplicada)  # Salida: (1, 2, 1, 2, 1, 2)
