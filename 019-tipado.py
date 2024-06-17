from typing import List, Dict, Any

# Parámetros posicionales con anotaciones de tipo
def saludar(nombre: str, saludo: str) -> None:
    print(f"{saludo}, {nombre}!")

saludar("Juan", "Hola")  # Se pasan los argumentos en el orden esperado
print('---')

# Parámetros por palabra clave (keyword arguments) con anotaciones de tipo
def saludar(nombre: str, saludo: str) -> None:
    print(f"{saludo}, {nombre}!")

saludar(saludo="Hola", nombre="Ana")  # Se especifican los argumentos por palabra clave
print('---')

# Parámetros por defecto con anotaciones de tipo
def saludar(nombre: str, saludo: str = "Hola") -> None:
    print(f"{saludo}, {nombre}!")

saludar("Pedro")  # No se especifica el argumento 'saludo', se usa el valor por defecto
print('---')

# Parámetros arbitrarios (*args) con anotaciones de tipo
def sumar(*numeros: float) -> None:
    resultado = sum(numeros)
    print("La suma es:", resultado)

sumar(1, 2, 3, 4)  # Se pueden pasar cualquier número de argumentos
print('---')

# Parámetros arbitrarios de palabra clave (**kwargs) con anotaciones de tipo
def mostrar_info(**datos: str) -> None:
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Juan", edad="30", ciudad="Madrid")  # Se pueden pasar cualquier número de argumentos por palabra clave
print('---')

# Parámetros posicionales después de *args con anotaciones de tipo
def mostrar_info(nombre: str, *apellidos: str) -> None:
    print("Nombre:", nombre)
    print("Apellidos:", apellidos)

mostrar_info("Juan", "García", "Pérez")  # El primer argumento es el nombre y el resto son apellidos
print('---')

# Parámetros de palabra clave después de **kwargs con anotaciones de tipo
def mostrar_info(nombre: str, **datos_extra: str) -> None:
    print("Nombre:", nombre)
    for clave, valor in datos_extra.items():
        print(f"{clave}: {valor}")

mostrar_info("Ana", edad="25", ciudad="Barcelona")  # El primer argumento es el nombre y el resto son datos adicionales
print('---')
