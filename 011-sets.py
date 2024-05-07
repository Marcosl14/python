# Ejemplo de métodos de sets en Python

# Crear conjuntos
set_1 = set([1, 2, 3, 4, 5])
set_2 = {4, 5, 6, 7, 8}
set_3 = {1, 2, 3}

# Método add()
# Añadir un elemento a set_1
set_1.add(6)
print(f"set_1 después de add(): {set_1}")

# Método remove()
# Eliminar un elemento de set_1
set_1.remove(1)
print(f"set_1 después de remove(): {set_1}")

# Método discard()
# Eliminar un elemento de set_2 si existe, no arroja error si el elemento no existe
set_2.discard(9)
print(f"set_2 después de discard(): {set_2}")

# Método union()
# Unión de set_1 y set_2, devuelve un nuevo set con elementos de ambos sets
set_union = set_1.union(set_2)
print(f"Unión de set_1 y set_2: {set_union}")

# Método intersection()
# Intersección de set_1 y set_2, devuelve un nuevo set con elementos comunes a ambos sets
set_intersection = set_1.intersection(set_2)
print(f"Intersección de set_1 y set_2: {set_intersection}")

# Método difference()
# Diferencia entre set_1 y set_2, devuelve un nuevo set con elementos de set_1 que no están en set_2
set_difference = set_1.difference(set_2)
print(f"Diferencia entre set_1 y set_2: {set_difference}")

# Método symmetric_difference()
# Diferencia simétrica entre set_1 y set_2, devuelve un nuevo set con elementos que están en uno pero no en ambos
set_symmetric_difference = set_1.symmetric_difference(set_2)
print(f"Diferencia simétrica entre set_1 y set_2: {set_symmetric_difference}")

# Método isdisjoint()
# Verificar si set_1 y set_2 no tienen elementos en común
is_disjoint = set_1.isdisjoint(set_2)
print(f"¿set_1 y set_2 son disjuntos?: {is_disjoint}")

# Método issubset()
# Verificar si set_3 es un subconjunto de set_1
is_subset = set_3.issubset(set_1)
print(f"¿set_3 es un subconjunto de set_1?: {is_subset}")

# Método issuperset()
# Verificar si set_1 es un superconjunto de set_3
is_superset = set_1.issuperset(set_3)
print(f"¿set_1 es un superconjunto de set_3?: {is_superset}")

# Método clear()
# Limpiar todos los elementos de set_2
set_2.clear()
print(f"set_2 después de clear(): {set_2}")

# Método copy()
# Copiar set_1 a un nuevo set
set_4 = set_1.copy()
print(f"Copia de set_1: {set_4}")
