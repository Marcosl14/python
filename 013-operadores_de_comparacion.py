# Ejemplos de operadores de comparación en Python

# Operador de comparación `==` (igual a)
# Devuelve True si ambos operandos son iguales, de lo contrario devuelve False
a = 5
b = 5
c = 7
print(f"¿a es igual a b?: {a == b}")  # True
print(f"¿a es igual a c?: {a == c}")  # False

# Operador de comparación `!=` (diferente de)
# Devuelve True si ambos operandos no son iguales, de lo contrario devuelve False
print(f"¿a es diferente de b?: {a != b}")  # False
print(f"¿a es diferente de c?: {a != c}")  # True

# Operador de comparación `<` (menor que)
# Devuelve True si el primer operando es menor que el segundo, de lo contrario devuelve False
print(f"¿a es menor que c?: {a < c}")  # True
print(f"¿c es menor que a?: {c < a}")  # False

# Operador de comparación `<=` (menor o igual que)
# Devuelve True si el primer operando es menor o igual que el segundo, de lo contrario devuelve False
print(f"¿a es menor o igual que c?: {a <= c}")  # True
print(f"¿c es menor o igual que a?: {c <= a}")  # False
print(f"¿a es menor o igual que b?: {a <= b}")  # True

# Operador de comparación `>` (mayor que)
# Devuelve True si el primer operando es mayor que el segundo, de lo contrario devuelve False
print(f"¿a es mayor que c?: {a > c}")  # False
print(f"¿c es mayor que a?: {c > a}")  # True

# Operador de comparación `>=` (mayor o igual que)
# Devuelve True si el primer operando es mayor o igual que el segundo, de lo contrario devuelve False
print(f"¿a es mayor o igual que c?: {a >= c}")  # False
print(f"¿c es mayor o igual que a?: {c >= a}")  # True
print(f"¿a es mayor o igual que b?: {a >= b}")  # True

# Comparación de cadenas de texto
# Los operadores de comparación también funcionan con cadenas de texto
str1 = "hello"
str2 = "world"
print(f"¿str1 es igual a str2?: {str1 == str2}")  # False
print(f"¿str1 es diferente de str2?: {str1 != str2}")  # True
print(f"¿str1 es menor que str2?: {str1 < str2}")  # True (porque 'h' viene antes que 'w' en el orden lexicográfico)
print(f"¿str1 es mayor que str2?: {str1 > str2}")  # False
