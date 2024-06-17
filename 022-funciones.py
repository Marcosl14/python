# Definición básica de una función
def saludar():
    """
    Esta función imprime un saludo.
    """
    print("¡Hola, mundo!")

# Llamada a la función
saludar()

print("---")

# Función con parámetros
def saludar_persona(nombre):
    """
    Esta función saluda a una persona específica.
    :param nombre: Nombre de la persona a saludar.
    """
    print(f"¡Hola, {nombre}!")

# Llamada a la función con un argumento
saludar_persona("Alice")

print("---")

# Función con parámetros y valores por defecto
def saludar_persona_defecto(nombre="invitado"):
    """
    Esta función saluda a una persona específica, con un valor por defecto si no se proporciona nombre.
    :param nombre: Nombre de la persona a saludar. Por defecto es "invitado".
    """
    print(f"¡Hola, {nombre}!")

# Llamada a la función sin argumento (usa el valor por defecto)
saludar_persona_defecto()
# Llamada a la función con un argumento
saludar_persona_defecto("Bob")

print("---")

# Función con varios parámetros
def sumar(a, b):
    """
    Esta función suma dos números.
    :param a: Primer número.
    :param b: Segundo número.
    :return: La suma de a y b.
    """
    return a + b

# Llamada a la función con argumentos posicionales
resultado = sumar(3, 4)
print(f"La suma de 3 y 4 es {resultado}")

# Llamada a la función con argumentos nombrados
resultado = sumar(a=5, b=7)
print(f"La suma de 5 y 7 es {resultado}")

print("---")

# Función con argumentos variables
def listar_args(*args):
    """
    Esta función lista todos los argumentos posicionales recibidos.
    :param args: Lista de argumentos posicionales.
    """
    for arg in args:
        print(arg)

# Llamada a la función con múltiples argumentos
listar_args(1, 2, 3, 4)

print("---")

# Función con argumentos nombrados variables
def listar_kwargs(**kwargs):
    """
    Esta función lista todos los argumentos nombrados recibidos.
    :param kwargs: Diccionario de argumentos nombrados.
    """
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# Llamada a la función con múltiples argumentos nombrados
listar_kwargs(nombre="Carlos", edad=30, ciudad="Madrid")

print("---")

# Función con anotaciones de tipo
def multiplicar(a: int, b: int) -> int:
    """
    Esta función multiplica dos números enteros.
    :param a: Primer número.
    :param b: Segundo número.
    :return: El producto de a y b.
    """
    return a * b

# Llamada a la función con argumentos
resultado = multiplicar(6, 7)
print(f"El producto de 6 y 7 es {resultado}")

print("---")

# Función lambda (anónima)
multiplicar_lambda = lambda x, y: x * y

# Llamada a la función lambda
resultado_lambda = multiplicar_lambda(6, 7)
print(f"El producto de 6 y 7 usando lambda es {resultado_lambda}")

print("---")

# Función con combinación de argumentos y parámetros
def combinar(a, b=2, *args, **kwargs):
    """
    Esta función combina argumentos posicionales, con valores por defecto, variables y nombrados.
    :param a: Primer argumento.
    :param b: Segundo argumento, con valor por defecto de 2.
    :param args: Argumentos posicionales adicionales.
    :param kwargs: Argumentos nombrados adicionales.
    """
    print(f"a = {a}, b = {b}")
    print("args =", args)
    print("kwargs =", kwargs)

# Llamada a la función con diferentes tipos de argumentos
combinar(1, 3, 4, 5, x=10, y=20)
