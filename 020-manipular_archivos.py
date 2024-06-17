mi_archivo = open("020-archivo.txt")
for linea in mi_archivo:
    print(linea.strip())
print("---")  # Separador


mi_archivo = open("020-archivo.txt")
print(mi_archivo.read())
print("---")  # Separador

mi_archivo = open("020-archivo.txt")
lineas = mi_archivo.readlines()
print(lineas)
print("---")  # Separador

mi_archivo.close()  # muy importante cerrar el archivo para liberar memoria

"""
open("020-archivo.txt") -> solo lectura (por defecto)
open("020-archivo.txt", 'r') -> solo lectura
open("020-archivo.txt", 'w') -> solo escritura
open("020-archivo.txt", 'a') -> solo escritura al final del archivo (append) -> si el archivo no existe, se crea
"""

mi_archivo = open("020-archivo.txt", 'a')
# mi_archivo.write('cuarta linea')
# mi_archivo.write("""
# cuarta linea
# quinta linea""")
