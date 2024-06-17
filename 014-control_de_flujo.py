# Ejemplos de control de flujo en Python

# Ejemplo de condicionales (`if`, `elif`, `else`)
edad = 25

# Comprobar la edad para decidir qué mensaje imprimir
if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad < 65:
    print("Eres un adulto.")
else:
    print("Eres una persona de la tercera edad.")

# solo a partir de python v3.10
# match valor:
#     case 1:
#         print("Realizando acción 1")
#     case 2:
#         print("Realizando acción 2")
#     case 3 | 4:
#         print("Realizando acción 3 o 4")
#     case _:
#         print("Valor no reconocido")

# solo a partir de python v3.10
# def validar_diccionario(diccionario):
#     match diccionario:
#         case {'nombre': str, 'edad': int}:
#             print("El diccionario tiene las claves 'nombre' y 'edad' con los tipos correctos.")
#         case {'nombre': str, 'email': str}:
#             print("El diccionario tiene las claves 'nombre' y 'email', pero falta la clave 'edad'.")
#         case _:
#             print("El diccionario no tiene la estructura esperada.")

# # Ejemplos de diccionarios a validar
# diccionario_1 = {'nombre': 'Juan', 'edad': 30}
# diccionario_2 = {'nombre': 'Ana', 'email': 'ana@example.com'}
# diccionario_3 = {'nombre': 'Pedro', 'profesion': 'Ingeniero'}

# # Validar los diccionarios
# print("Validando diccionario 1:")
# validar_diccionario(diccionario_1)

# print("\nValidando diccionario 2:")
# validar_diccionario(diccionario_2)

# print("\nValidando diccionario 3:")
# validar_diccionario(diccionario_3)