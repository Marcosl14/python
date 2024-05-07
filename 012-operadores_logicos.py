# Ejemplos de operadores lógicos en Python

# Operador AND (y lógico)
# El operador AND devuelve True si ambos operandos son True, de lo contrario devuelve False

# Ejemplo 1:
condition1 = True
condition2 = False
result_and = condition1 and condition2
print(f"Resultado de condition1 AND condition2: {result_and}")  # False

# Ejemplo 2:
condition1 = True
condition2 = True
result_and = condition1 and condition2
print(f"Resultado de condition1 AND condition2: {result_and}")  # True

# Operador OR (o lógico)
# El operador OR devuelve True si al menos uno de los operandos es True, de lo contrario devuelve False

# Ejemplo 3:
condition1 = False
condition2 = True
result_or = condition1 or condition2
print(f"Resultado de condition1 OR condition2: {result_or}")  # True

# Ejemplo 4:
condition1 = False
condition2 = False
result_or = condition1 or condition2
print(f"Resultado de condition1 OR condition2: {result_or}")  # False

# Operador NOT (no lógico)
# El operador NOT devuelve True si el operando es False, y False si el operando es True

# Ejemplo 5:
condition = True
result_not = not condition
print(f"Resultado de NOT condition: {result_not}")  # False

# Ejemplo 6:
condition = False
result_not = not condition
print(f"Resultado de NOT condition: {result_not}")  # True

# Usando operadores lógicos con condiciones
# Supongamos que tenemos las variables edad y salario, y queremos verificar si una persona puede obtener un préstamo
edad = 30
salario = 50000

# Condición: la persona debe tener al menos 18 años y un salario mayor a 30000
puede_obtener_prestamo = edad >= 18 and salario > 30000
print(f"¿Puede obtener préstamo?: {puede_obtener_prestamo}")  # True

# Usando operadores lógicos para verificar si una letra es vocal o consonante
letra = 'a'

# Condición: la letra es una vocal
es_vocal = letra in 'aeiouAEIOU'
print(f"¿La letra '{letra}' es vocal?: {es_vocal}")  # True

# Condición: la letra es una consonante
es_consonante = not es_vocal
print(f"¿La letra '{letra}' es consonante?: {es_consonante}")  # False
