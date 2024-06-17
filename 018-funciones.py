# Parámetros posicionales
def saludar(nombre, saludo):
    return f"{saludo}, {nombre}!"


print(saludar("Juan", "Hola"))  # Se pasan los argumentos en el orden esperado
print("---")


# Parámetros por palabra clave (keyword arguments)
def saludar(nombre, saludo):
    return f"{saludo}, {nombre}!"


print(
    saludar(saludo="Hola", nombre="Ana")
)  # Se especifican los argumentos por palabra clave
print("---")


# Parámetros por defecto
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"


print(
    saludar("Pedro")
)  # No se especifica el argumento 'saludo', se usa el valor por defecto
print("---")


# Parámetros arbitrarios (*args)
def sumar(*numeros):
    resultado = sum(numeros)
    return f"La suma es: {resultado}"


print(sumar(1, 2, 3, 4))  # Se pueden pasar cualquier número de argumentos
print("---")


# Parámetros arbitrarios de palabra clave (**kwargs)
def mostrar_info(**datos):
    values = []
    for clave, valor in datos.items():
        values.append(f"{clave}: {valor}")
    return "\n".join(values)


print(
    mostrar_info(nombre="Juan", edad=30, ciudad="Madrid")
)  # Se pueden pasar cualquier número de argumentos por palabra clave
print("---")


# Parámetros posicionales después de *args (argumentos indefinidos)
def mostrar_info(nombre, *apellidos):
    return f"{apellidos}, {nombre}"


print(
    mostrar_info("Juan", "García", "Pérez")
)  # El primer argumento es el nombre y el resto son apellidos
print("---")


# Parámetros de palabra clave después de **kwargs (argumentos indefinidos -> keyword args -> diccionarios)
def mostrar_info(nombre, **datos_extra):
    values = []
    for clave, valor in datos_extra.items():
        values.append(f"{nombre}, {clave}: {valor}")
    return "\n".join(values)


print(
    mostrar_info("Ana", edad=25, ciudad="Barcelona")
)  # El primer argumento es el nombre y el resto son datos adicionales
print("---")

def prueba(num1, num2, *args, **kwargs):
    print(f"num1 = {num1}")
    print(f"num2 = {num2}")

    for arg in args:
        print(f"arg: {arg}")
    
    for clave, valor in kwargs.items():
        print(f"karg: clave: {clave}, valor: {valor}")

args = [100,200,300,40]
kwargs = { 'x': 'uno', 'y': 'dos', 'z': 'tres'}
prueba(1,2,*args, **kwargs)
