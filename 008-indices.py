value = "Esta es una prueba"

print(value[0])
print(value[-1])  # Reverso

# index()
print(value.index("n"))  # Devuelve el indice
print(value.index("prueba"))  # Devuelve el indice de donde comienza la palabra

try:
    print(value.index("x"))  # Devuelve error
except Exception as e:
    print(e)

try:
    print(value.index("P"))  # Devuelve error porque es sensible a mayusculas
except Exception as e:
    print(e)

print(value.index("a", 5))  # Contando desde indice 5
print(value.index("a", 5, 11))  # Contando desde indice 5 hasta el indice 11

# rindex()
print(value.rindex("a"))  # Busca desde atras hacia adelante

# slicing -> devuelve una porcion de una cadena de texto
print(value[4:10])
print(value[4:10:2])  # toma la cadena cada dos caracteres
print(value[::2])  # toma toda la cadena cada dos caracteres
print(value[::-1])  # hace un reverse
