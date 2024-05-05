# string literals

print("The {} {} {}".format("car", "yellow", "fast"))  # empty braces
# The car yellow fast
print("The {2} {1} {0}".format("car", "yellow", "fast"))  # index
# The fast yellow car
print("The {f} {y} {c}".format(c="car", y="yellow", f="fast"))
# The fast yellow car

name = "Peter"
print(f"Nice to meet you, {name}")


#####################################################
# text wrapping:

print(
    """hola
me llamo
marcos"""
)

#####################################################
# metodos

print("hola mundo".capitalize())  # Salida: Hola mundo

print("hola mundo".upper())  # Salida: HOLA MUNDO

print("HOLA MUNDO".lower())  # Salida: hola mundo

print("hola mundo".title())  # Salida: Hola Mundo

print("  hola mundo   ".strip())  # Salida: hola mundo

print("hola,mundo,cómo,estás".split(","))  # Salida: ['hola', 'mundo', 'cómo', 'estás']

print(",".join(["hola", "mundo", "cómo", "estás"]))  # Salida: hola,mundo,cómo,estás

print("hola mundo".replace("mundo", "amigo"))  # Salida: hola amigo
print("aaa".replace("a", "x"))  # Salida: xxx

print("hola mundo".find("mundo"))  # Salida: 5

print("hola mundo".startswith("hola"))  # Salida: True

print("hola mundo".endswith("mundo"))  # Salida: True

print(len("hola mundo"))  # Salida: 10

print("agua" in "hola mundo")
print("agua" not in "hola mundo")

value = "Esta es una prueba"

print(value[0])
print(value[-1])  # Reverso

#####################################################
# indices
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
