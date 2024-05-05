print([1, 2, 3])
print(["hola", "mundo"])
print(["hola", 2, "mundo", 10])

#####################################################
# metodos

# largo
print(len([1, 2, 3]))  # salida: 3

# indices
print([1, 2, 3][0])  # salida: 1
print([1, 2, 3][0:2])  # salida: [1,2]

# concatenacion
print([1, 2, 3] + [4, 5])  # salida: [1,2,3,4,5]

# modificar un elemento
var1 = [1, 2, 3]
var1[0] = 10
print(var1)  # salida: [10,2,3]

# Método append(): Agrega un elemento al final de la lista.
lista_1 = [1, 2, 3]
lista_1.append(4)
print("append():", lista_1)  # Salida: [1, 2, 3, 4]

# Método extend(): Extiende la lista agregando elementos de otra lista (o cualquier iterable).
lista_2 = [1, 2, 3]
lista_2.extend([4, 5])
print("extend():", lista_2)  # Salida: [1, 2, 3, 4, 5]

# Método insert(): Inserta un elemento en una posición específica.
lista_3 = [1, 2, 3]
lista_3.insert(1, 5)
print("insert():", lista_3)  # Salida: [1, 5, 2, 3]

# Método remove(): Elimina la primera aparición del elemento especificado.
lista_4 = [1, 2, 3, 2]
lista_4.remove(2)
print("remove():", lista_4)  # Salida: [1, 3, 2]

# Método pop(): Elimina y retorna el elemento en la posición dada (o el último si no se especifica).
lista_5 = [1, 2, 3]
elemento = lista_5.pop(1)
print("pop():", elemento, lista_5)  # Salida: 2 [1, 3]

# Método index(): Retorna la primera posición de un elemento específico.
lista_6 = [1, 2, 3, 2]
indice = lista_6.index(2)
print("index():", indice)  # Salida: 1

# Método count(): Retorna el número de veces que un elemento aparece en la lista.
lista_7 = [1, 2, 3, 2]
conteo = lista_7.count(2)
print("count():", conteo)  # Salida: 2

# Método reverse(): Invierte el orden de los elementos en la lista.
lista_8 = [1, 2, 3]
lista_8.reverse()
print("reverse():", lista_8)  # Salida: [3, 2, 1]

# Método sort(): Ordena los elementos de la lista.
lista_9 = [3, 1, 2]
lista_9.sort()
print("sort():", lista_9)  # Salida: [1, 2, 3]

# Método clear(): Elimina todos los elementos de la lista.
lista_10 = [1, 2, 3]
lista_10.clear()
print("clear():", lista_10)  # Salida: []

# Desempaquetado de listas
lista_11 = [1, 2, 3]
a, b, c = lista_11
print("Desempaquetado:", a, b, c)  # Salida: 1 2 3
