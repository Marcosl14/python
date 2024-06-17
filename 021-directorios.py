print("os")
print("/////////////////////////////////////////////////")

import os

# Crear una ruta de directorio en Python
ruta_directorio = "./hola/mundo"

# Crear directorios si no existen
os.makedirs(ruta_directorio, exist_ok=True)

# Crear un archivo en la ruta especificada
archivo_python = os.path.join(ruta_directorio, "python.txt")
with open(archivo_python, "w") as archivo:
    archivo.write("Hola mundo desde Python!\n")

# Verificar si el archivo se ha creado
if os.path.exists(archivo_python):
    print(
        f"El archivo '{os.path.basename(archivo_python)}' se ha creado en el directorio '{os.path.dirname(archivo_python)}'"
    )
else:
    print(
        f"No se pudo crear el archivo '{os.path.basename(archivo_python)}' en el directorio '{os.path.dirname(archivo_python)}'"
    )

# Listar el contenido del directorio
contenido_directorio = os.listdir(ruta_directorio)
print("Contenido del directorio './hola/mundo':", contenido_directorio)

# Cambiar el directorio de trabajo actual
os.chdir(ruta_directorio)

# Obtener la ruta absoluta del directorio actual
ruta_actual = os.getcwd()
print("El directorio de trabajo actual es:", ruta_actual)

# Eliminar el archivo creado
os.remove("./python.txt")
print("El archivo 'python.txt' se ha eliminado")

# Eliminar directorios creados
ruta_actual = os.getcwd()
os.rmdir(ruta_actual)
print(f"Los directorios en la ruta '{ruta_actual}' se han eliminado")

os.chdir("../")
ruta_actual = os.getcwd()
os.rmdir(ruta_actual)
print(f"Los directorios en la ruta '{ruta_actual}' se han eliminado")


print("Path")
print("/////////////////////////////////////////////////")

from pathlib import Path

directorio_script = Path(
    __file__
).parent.absolute()  # Path no entiende sobre rutas relativas... Por eso buscamos la posicion actual donde estamos

ruta_directorio = directorio_script / "./021-carpeta/021-archivo_1.txt"

print(f"Directorio Actual: {ruta_directorio}")
print(f"Nombre: {ruta_directorio.name}")
print(f"Suffix: {ruta_directorio.suffix}")
print(f"Nombre Archivo: {ruta_directorio.stem}")
print(f"Existe?: {ruta_directorio.exists()}")

print("/////////////////////////////////////////////////")

ruta_directorio_2 = Path(directorio_script, "021-carpeta", "021-archivo_1.txt")

print(f"Directorio Actual: {ruta_directorio_2}")
print(f"Nombre: {ruta_directorio_2.name}")
print(f"Existe?: {ruta_directorio_2.exists()}")

print("/////////////////////////////////////////////////")

ruta_directorio_3 = Path(directorio_script, "021-carpeta")
ruta_archivo = ruta_directorio_3 / "021-archivo_1.txt"

print(f"Directorio Actual: {ruta_archivo}")
print(f"Nombre: {ruta_archivo.name}")
print("Leyendo Archivo")
print(ruta_archivo.read_text())
print("Fin")
print(f"Padre: {ruta_archivo.parent}")

print("/////////////////////////////////////////////////")

for archivo in ruta_archivo.parent.glob('*.txt'):
    print(archivo)
