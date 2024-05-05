# Método clear(): Elimina todos los elementos del diccionario.
diccionario_1 = {"a": 1, "b": 2, "c": 3}
diccionario_1.clear()
print("clear():", diccionario_1)  # Salida: {}

# Método copy(): Retorna una copia superficial del diccionario.
diccionario_2 = {"a": 1, "b": 2, "c": 3}
copia = diccionario_2.copy()
print("copy():", copia)  # Salida: {'a': 1, 'b': 2, 'c': 3}

# Método get(): Retorna el valor asociado a una clave, o un valor por defecto si la clave no está presente.
diccionario_3 = {"a": 1, "b": 2, "c": 3}
valor = diccionario_3.get("b")
print("get():", valor)  # Salida: 2
print("o usando []:", diccionario_3["b"])  # Salida: 2

# Método items(): Retorna una vista de tuplas de todos los pares (clave, valor) en el diccionario.
diccionario_4 = {"a": 1, "b": 2, "c": 3}
items = diccionario_4.items()
print("items():", items)  # Salida: dict_items([('a', 1), ('b', 2), ('c', 3)]) -> tupla

# Método keys(): Retorna una vista de todas las claves en el diccionario.
diccionario_5 = {"a": 1, "b": 2, "c": 3}
claves = diccionario_5.keys()
print("keys():", claves)  # Salida: dict_keys(['a', 'b', 'c'])

# Método values(): Retorna una vista de todos los valores en el diccionario.
diccionario_6 = {"a": 1, "b": 2, "c": 3}
valores = diccionario_6.values()
print("values():", valores)  # Salida: dict_values([1, 2, 3])

# Método pop(): Elimina y retorna el valor asociado a una clave.
diccionario_7 = {"a": 1, "b": 2, "c": 3}
valor = diccionario_7.pop("b")
print("pop():", valor, diccionario_7)  # Salida: 2 {'a': 1, 'c': 3}

# Método popitem(): Elimina y retorna un par (clave, valor) aleatorio del diccionario.
diccionario_8 = {"a": 1, "b": 2, "c": 3}
par = diccionario_8.popitem()
print("popitem():", par, diccionario_8)  # Salida: ('c', 3) {'a': 1, 'b': 2}

# Método update(): Actualiza el diccionario con elementos de otro diccionario o con pares (clave, valor) proporcionados como argumentos.
diccionario_9 = {"a": 1, "b": 2}
diccionario_10 = {"b": 3, "c": 4}
diccionario_9.update(diccionario_10)
print("update():", diccionario_9)  # Salida: {'a': 1, 'b': 3, 'c': 4}
