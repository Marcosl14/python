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
